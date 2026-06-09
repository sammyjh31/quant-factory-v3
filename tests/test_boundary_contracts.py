"""Durable boundary contracts for the V3 federation.

These tests enforce boundaries, not history. Executed pilots are discovered
from the filesystem, so new pilots are covered automatically with zero new
test code. Pilot-level findings (scores, failure tags, comparison prose) live
only in the export records and lab-local comparison notes; tests must not
keep a second copy of the evidence.
"""

from __future__ import annotations

import hashlib
import inspect
import json
import re
import subprocess
from pathlib import Path

import pytest
from qf_v3_protocol import ValidationError, validate_record
from qf_v3_protocol.discovery import (
    active_benchmark_paths,
    invalid_example_paths,
    lab_export_paths,
    valid_example_paths,
)
from qf_v3_synthesis import synthesize_exports
from qf_v3_synthesis.cli import main as synthesis_cli_main

ROOT = Path(__file__).resolve().parents[1]
CURRENT_SCHEMA_VERSION = "0.1.2"
FIXTURE_EVIDENCE_DISCLAIMER = (
    "This is a scaffold fixture for protocol validation, not real research evidence."
)
LIVE_EVIDENCE_DISCLAIMER = (
    "This is a proposal-only live LLM pilot record, not validation, product evidence, "
    "strategy evidence, financial advice, live-trading authority, or architecture."
)
PROTOCOL_SCHEMA_NAMES = {
    "ArtifactEnvelope.schema.json",
    "BenchmarkPack.schema.json",
    "EvaluationRecord.schema.json",
    "ExperimentCard.schema.json",
    "MethodCard.schema.json",
    "ResearchNote.schema.json",
    "RunRecord.schema.json",
    "SourceRef.schema.json",
}
ALLOWED_EVALUATOR_TYPES = {
    "schema_check",
    "fixture_assertion",
    "llm_judge_placeholder",
    "manual_boundary_review",
    "manual_content_review",
}
SOURCE_REF_PREFIX = "raw_corpora_sha256:"
PILOT_PLANNING_REQUIRED_FILES = {
    "admission.md",
    "run_admission_update.md",
    "stop_condition.md",
    "evaluator_plan.md",
    "method_card.proposed.json",
    "experiment_card.proposed.json",
    "source_privacy_boundary.md",
}
ROUTER_LEDGER_PATTERNS = (
    r"labs/[^\s`]+/EXPORTS/(?:run_record|artifact_envelope|evaluation_record|research_note)"
    r"\.live_pilot_\d+\.json",
    r"evaluation_record\.live_pilot_\d+_manual_content_review\.json",
    r"manual content review (?:failed|passed) for pilot \d+",
    r"\b[a-z_]+_live_pilot_\d+\b",
)
CURRENTNESS_ROUTER_DOCS = (
    "README.md",
    "PORTFOLIO_CURRENT.md",
    "LAB_REGISTRY.md",
    "GRADUATION_LEDGER.md",
)
LAB_BOUNDARY_SENTENCE = (
    "no validation, product authority, strategy evidence, financial advice, "
    "live-trading authority, graduation, or architecture"
)
ARCHITECTURE_RULE = (
    "No new experiment becomes architecture.\n"
    "It becomes records first.\n"
    "Architecture changes only after repeated evidence and explicit ADR."
)


# ---------------------------------------------------------------------------
# Helpers and filesystem discovery
# ---------------------------------------------------------------------------


def load_json(path: Path):
    return json.loads(path.read_text())


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_json_hash(payload) -> str:
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(encoded).hexdigest()


def extract_json_block(markdown: str, marker: str):
    pattern = rf"## {re.escape(marker)}\n\n```json\n(.*?)\n```"
    match = re.search(pattern, markdown, re.DOTALL)
    assert match, f"Missing JSON block for {marker}"
    return json.loads(match.group(1))


def iter_records(path: Path):
    payload = load_json(path)
    if isinstance(payload, list):
        yield from payload
    else:
        yield payload


def all_lab_export_records():
    for path in lab_export_paths(ROOT):
        yield from iter_records(path)


def records_by_schema(schema_name: str):
    return [record for record in all_lab_export_records() if record["schema_name"] == schema_name]


def lab_dirs() -> list[Path]:
    return sorted(path for path in (ROOT / "labs").iterdir() if path.is_dir())


def executed_pilots() -> list[tuple[str, str, Path, Path]]:
    """(lab_id, pilot_number, planning_dir, exports_dir) for every executed pilot."""
    pilots = []
    for run_path in sorted(ROOT.glob("labs/*/EXPORTS/run_record.live_pilot_*.json")):
        lab_id = run_path.parents[1].name
        match = re.fullmatch(r"run_record\.live_pilot_(\d+)\.json", run_path.name)
        assert match, run_path
        number = match.group(1)
        planning_dir = ROOT / "labs" / lab_id / "PLANNING" / f"live_llm_pilot_{number}"
        pilots.append((lab_id, number, planning_dir, run_path.parent))
    assert pilots, "executed live pilots must be discoverable"
    return pilots


def base_export_names(pilot_number: str) -> set[str]:
    return {
        f"run_record.live_pilot_{pilot_number}.json",
        f"artifact_envelope.live_pilot_{pilot_number}.json",
        f"evaluation_record.live_pilot_{pilot_number}.json",
        f"research_note.live_pilot_{pilot_number}.json",
    }


def pilot_export_paths(exports_dir: Path, pilot_number: str) -> list[Path]:
    return sorted(exports_dir.glob(f"*.live_pilot_{pilot_number}*.json"))


def assert_currentness_router_not_ledger(text: str):
    assert "generated synthesis metrics" not in text.lower()
    assert "provider_payload" not in text
    assert "raw_source_text" not in text
    assert "raw_model_output" not in text
    for pattern in ROUTER_LEDGER_PATTERNS:
        assert not re.search(pattern, text), pattern


def live_pilot_schema_probe_records():
    """Synthetic records proving the protocol can represent a proposal-only pilot."""
    run_id = "schema_probe_live_pilot_run"
    artifact_id = "schema_probe_live_pilot_artifact"
    evaluation_id = "schema_probe_live_pilot_eval"
    source_ref = f"{SOURCE_REF_PREFIX}example_source_segment"
    return [
        {
            "protocol_version": "qf-v3-protocol-0.1",
            "schema_name": "RunRecord",
            "schema_version": CURRENT_SCHEMA_VERSION,
            "run_record": {
                "run_id": run_id,
                "lab_id": "long_context_judgment",
                "experiment_id": "long_context_judgment_live_pilot_001",
                "method_id": "long_context_judgment_live_pilot_001_method",
                "benchmark_pack_id": "text_judgment_v0",
                "source_refs": [source_ref],
                "artifact_ids": [artifact_id],
                "evaluation_ids": [evaluation_id],
                "run_kind": "live_llm_pilot",
                "outcome_polarity": "proposal_only",
                "status": "live_recorded",
            },
        },
        {
            "protocol_version": "qf-v3-protocol-0.1",
            "schema_name": "ArtifactEnvelope",
            "schema_version": CURRENT_SCHEMA_VERSION,
            "artifact": {
                "artifact_id": artifact_id,
                "artifact_type": "judgment_principle_proposal",
                "lab_id": "long_context_judgment",
                "method_id": "long_context_judgment_live_pilot_001_method",
                "run_id": run_id,
                "source_refs": [source_ref],
                "posture": {
                    "grounding_status": "source_linked",
                    "review_status": "self_checked",
                    "readiness_status": "study_candidate",
                    "validation_status": "none",
                    "lifecycle_status": "active",
                },
                "blockers": ["proposal_only_not_evaluated"],
                "summary": "Proposal-only live pilot artifact example for schema validation.",
                "payload": {
                    "outcome_polarity": "proposal_only",
                    "proposal_only": True,
                },
            },
        },
        {
            "protocol_version": "qf-v3-protocol-0.1",
            "schema_name": "EvaluationRecord",
            "schema_version": CURRENT_SCHEMA_VERSION,
            "evaluation": {
                "evaluation_id": evaluation_id,
                "lab_id": "long_context_judgment",
                "target_id": artifact_id,
                "target_type": "artifact",
                "evaluator_id": "manual_content_review_v0",
                "evaluator_type": "manual_content_review",
                "benchmark_pack_id": "text_judgment_v0",
                "score": 0.5,
                "pass_fail": "fail",
                "failure_tags": ["weak_source_grounding"],
                "comments": (
                    "Manual content review only; does not validate trading correctness, "
                    "product readiness, strategy evidence, financial advice, live-trading "
                    "authority, graduation, or architecture."
                ),
            },
        },
        {
            "protocol_version": "qf-v3-protocol-0.1",
            "schema_name": "ResearchNote",
            "schema_version": CURRENT_SCHEMA_VERSION,
            "research_note": {
                "note_id": "schema_probe_live_pilot_note",
                "lab_id": "long_context_judgment",
                "experiment_ids": ["long_context_judgment_live_pilot_001"],
                "benchmark_pack_ids": ["text_judgment_v0"],
                "summary": "Proposal-only live pilot note example for schema validation.",
                "what_worked": ["The record shape can preserve live-pilot boundaries."],
                "what_failed": ["No method quality claim exists in this example."],
                "negative_results": ["A proposal-only live pilot is not validation."],
                "reusable_by_other_labs": [
                    "Use evidence_disclaimer instead of fixture-only disclaimer text."
                ],
                "do_not_repeat": ["Do not relabel live pilot output as a scaffold fixture."],
                "evidence_disclaimer": LIVE_EVIDENCE_DISCLAIMER,
            },
        },
    ]


# ---------------------------------------------------------------------------
# Protocol capability contracts
# ---------------------------------------------------------------------------


def test_protocol_valid_examples_validate():
    paths = valid_example_paths(ROOT)
    assert paths, "valid protocol examples must exist"
    for path in paths:
        for record in iter_records(path):
            validate_record(record)


def test_protocol_invalid_examples_fail():
    paths = invalid_example_paths(ROOT)
    assert paths, "invalid protocol examples must exist"
    for path in paths:
        for record in iter_records(path):
            with pytest.raises(ValidationError):
                validate_record(record)


def test_protocol_examples_only_live_in_protocol_package():
    assert not (ROOT / "examples").exists()
    for path in valid_example_paths(ROOT) + invalid_example_paths(ROOT):
        assert "packages/qf_v3_protocol/examples/" in path.as_posix()


def test_protocol_supports_proposal_only_live_pilot_records():
    for record in live_pilot_schema_probe_records():
        validate_record(record)


def test_protocol_rejects_unknown_evaluation_fields():
    [_, _, evaluation, _] = live_pilot_schema_probe_records()
    evaluation["evaluation"]["content_review_payload"] = {"unknown": "field"}
    with pytest.raises(ValidationError):
        validate_record(evaluation)


def test_protocol_rejects_fixture_live_semantic_mismatches():
    [run_record, *_] = live_pilot_schema_probe_records()

    for bad_fields in [
        {"run_kind": "scaffold_fixture", "outcome_polarity": "proposal_only",
         "status": "fixture_recorded"},
        {"run_kind": "live_llm_pilot", "outcome_polarity": "positive_fixture",
         "status": "live_recorded"},
        {"run_kind": "live_llm_pilot", "outcome_polarity": "proposal_only",
         "status": "fixture_recorded"},
    ]:
        mutated = json.loads(json.dumps(run_record))
        mutated["run_record"].update(bad_fields)
        with pytest.raises(ValidationError):
            validate_record(mutated)


def test_protocol_schema_inventory_stays_tiny_and_adr_documented():
    schema_dir = ROOT / "packages" / "qf_v3_protocol" / "src" / "qf_v3_protocol" / "schemas"
    assert {path.name for path in schema_dir.glob("*.schema.json")} == PROTOCOL_SCHEMA_NAMES

    protocol_current = (ROOT / "PROTOCOL_CURRENT.md").read_text()
    assert f"Current schema version: `{CURRENT_SCHEMA_VERSION}`" in protocol_current
    assert "No other schema is part of protocol v0.1." in protocol_current
    assert "Protocol changes require an ADR." in protocol_current

    adr_paths = sorted((ROOT / "docs" / "adr").glob("*.md"))
    assert adr_paths, "protocol patches must be ADR-documented"
    adr_text = "\n".join(path.read_text() for path in adr_paths)
    assert "proposal-only live LLM pilot" in adr_text
    assert "manual_content_review" in adr_text


# ---------------------------------------------------------------------------
# Benchmark contracts
# ---------------------------------------------------------------------------


def test_active_benchmark_packs_validate_and_preserve_v2_refs():
    paths = active_benchmark_paths(ROOT)
    assert paths, "active benchmark packs must exist"
    for path in paths:
        record = load_json(path)
        validate_record(record)
        benchmark = record["benchmark_pack"]
        assert "Benchmark Pack" in benchmark["title"]
        assert "metadata-safe benchmark pack" in benchmark["purpose"].lower()
        assert benchmark["v2_lesson_refs"]
        assert benchmark["metadata_safety"] == {
            "raw_source_material_included": False,
            "private_or_provider_payload_included": False,
            "synthetic_or_placeholder_only": True,
        }


def test_future_candidate_packs_are_not_active():
    future_paths = sorted((ROOT / "benchmarks" / "future_candidates").glob("*"))
    assert future_paths
    assert all(path.suffix == ".md" for path in future_paths)


# ---------------------------------------------------------------------------
# Lab export contracts
# ---------------------------------------------------------------------------


def test_all_lab_export_records_validate():
    export_paths = lab_export_paths(ROOT)
    assert export_paths
    assert {path.parents[1].name for path in export_paths} == {
        path.name for path in lab_dirs()
    }
    for path in export_paths:
        records = list(iter_records(path))
        assert records
        for record in records:
            validate_record(record)


def test_fixture_records_cover_both_polarities_per_lab():
    fixture_paths = [
        path for path in lab_export_paths(ROOT) if path.name == "fixture_records.json"
    ]
    assert {path.parents[1].name for path in fixture_paths} == {
        path.name for path in lab_dirs()
    }
    for path in fixture_paths:
        records = list(iter_records(path))
        run_polarities = {
            record["run_record"]["outcome_polarity"]
            for record in records
            if record["schema_name"] == "RunRecord"
        }
        artifact_polarities = {
            record["artifact"]["payload"]["outcome_polarity"]
            for record in records
            if record["schema_name"] == "ArtifactEnvelope"
        }
        assert run_polarities == {"positive_fixture", "negative_fixture"}
        assert artifact_polarities == {"positive_fixture", "negative_fixture"}


def test_artifact_envelopes_use_final_posture_facets_only():
    final_names = {
        "grounding_status",
        "review_status",
        "readiness_status",
        "validation_status",
        "lifecycle_status",
    }
    forbidden_statuses = {
        "validated",
        "historically_audited",
        "production_ready",
        "strategy_ready",
        "playbook_ready",
    }
    artifacts = records_by_schema("ArtifactEnvelope")
    assert artifacts
    for record in artifacts:
        posture = record["artifact"]["posture"]
        assert set(posture) == final_names
        assert forbidden_statuses.isdisjoint(posture.values())


def test_research_note_disclaimers_match_record_kind():
    for path in lab_export_paths(ROOT):
        is_live = path.name.startswith("research_note.live_pilot_")
        for record in iter_records(path):
            if record["schema_name"] != "ResearchNote":
                continue
            disclaimer = record["research_note"]["evidence_disclaimer"]
            if is_live:
                assert disclaimer == LIVE_EVIDENCE_DISCLAIMER, path
            else:
                assert disclaimer == FIXTURE_EVIDENCE_DISCLAIMER, path


def test_evaluation_records_are_bounded():
    artifact_ids = {
        record["artifact"]["artifact_id"] for record in records_by_schema("ArtifactEnvelope")
    }
    evaluations = records_by_schema("EvaluationRecord")
    assert evaluations
    placeholder_seen = False
    for record in evaluations:
        evaluation = record["evaluation"]
        assert evaluation["evaluator_type"] in ALLOWED_EVALUATOR_TYPES
        assert 0.0 <= evaluation["score"] <= 1.0
        assert evaluation["pass_fail"] in {"pass", "fail"}
        if evaluation["target_type"] == "artifact":
            assert evaluation["target_id"] in artifact_ids
        if evaluation["evaluator_type"] == "manual_boundary_review":
            assert "method quality was not evaluated" in evaluation["comments"]
        if evaluation["evaluator_type"] == "manual_content_review":
            assert "not validation" in evaluation["comments"]
        if evaluation["evaluator_type"] == "llm_judge_placeholder":
            placeholder_seen = True
            assert evaluation["placeholder_disclaimer"] == (
                "No live LLM judge was called. This is a scaffold fixture only."
            )
    assert placeholder_seen


# ---------------------------------------------------------------------------
# Executed live pilot contracts (filesystem-discovered)
# ---------------------------------------------------------------------------


def test_every_executed_pilot_has_planning_packet_and_complete_export_set():
    for lab_id, number, planning_dir, exports_dir in executed_pilots():
        assert planning_dir.is_dir(), f"{lab_id} pilot {number} has no planning packet"
        names = {path.name for path in pilot_export_paths(exports_dir, number)}
        assert base_export_names(number).issubset(names), (lab_id, number)
        extras = names - base_export_names(number)
        for extra in extras:
            assert re.fullmatch(
                rf"evaluation_record\.live_pilot_{number}_[a-z_]+\.json", extra
            ), (lab_id, number, extra)


def test_live_run_records_are_proposal_only_and_link_planning_ids():
    benchmark_ids = {
        load_json(path)["benchmark_pack"]["benchmark_id"]
        for path in active_benchmark_paths(ROOT)
    }
    for lab_id, number, planning_dir, exports_dir in executed_pilots():
        run = load_json(exports_dir / f"run_record.live_pilot_{number}.json")["run_record"]
        method_card = load_json(planning_dir / "method_card.proposed.json")
        experiment_card = load_json(planning_dir / "experiment_card.proposed.json")
        validate_record(method_card)
        validate_record(experiment_card)

        assert run["lab_id"] == lab_id
        assert run["run_kind"] == "live_llm_pilot"
        assert run["outcome_polarity"] == "proposal_only"
        assert run["status"] == "live_recorded"
        assert run["method_id"] == method_card["method_card"]["method_id"]
        assert run["experiment_id"] == experiment_card["experiment_card"]["experiment_id"]
        assert run["method_id"] in experiment_card["experiment_card"]["method_ids"]
        assert run["benchmark_pack_id"] in benchmark_ids
        assert run["source_refs"]
        for source_ref in run["source_refs"]:
            assert source_ref.startswith(SOURCE_REF_PREFIX)

        artifact_ids = set()
        evaluation_ids = set()
        for path in pilot_export_paths(exports_dir, number):
            for record in iter_records(path):
                if record["schema_name"] == "ArtifactEnvelope":
                    artifact_ids.add(record["artifact"]["artifact_id"])
                if record["schema_name"] == "EvaluationRecord":
                    evaluation_ids.add(record["evaluation"]["evaluation_id"])
        assert set(run["artifact_ids"]).issubset(artifact_ids)
        assert set(run["evaluation_ids"]).issubset(evaluation_ids)


def test_live_artifact_payloads_keep_privacy_boundaries():
    for _lab_id, number, _, exports_dir in executed_pilots():
        envelope = load_json(exports_dir / f"artifact_envelope.live_pilot_{number}.json")
        run = load_json(exports_dir / f"run_record.live_pilot_{number}.json")["run_record"]
        artifact = envelope["artifact"]
        payload = artifact["payload"]

        assert artifact["run_id"] == run["run_id"]
        assert artifact["source_refs"] == run["source_refs"]
        assert payload["outcome_polarity"] == "proposal_only"
        assert payload["proposal_only"] is True
        assert payload["raw_source_text_committed"] is False
        assert payload["raw_provider_payload_committed"] is False
        assert payload["raw_prompt_trace_committed"] is False
        assert payload["secrets_committed"] is False
        assert payload["source_metadata"]["source_ref"] == run["source_refs"][0]
        assert 300 <= payload["source_metadata"]["excerpt_word_count"] <= 1000
        cost = payload["cost_metadata"]
        assert cost["estimated_cost_usd"] <= cost["budget_cap_usd"]
        assert "raw_source_text" not in payload
        assert "provider_payload" not in payload
        assert "api_key" not in json.dumps(payload).lower()


def test_planning_packets_contain_admission_files_and_no_live_records():
    forbidden_schemas = {"RunRecord", "ArtifactEnvelope", "EvaluationRecord", "ResearchNote"}
    for lab_id, number, planning_dir, _ in executed_pilots():
        files = {path.name for path in planning_dir.iterdir() if path.is_file()}
        required = PILOT_PLANNING_REQUIRED_FILES | {
            f"prompt_template.live_pilot_{number}.md"
        }
        assert required.issubset(files), (lab_id, number, required - files)

        json_names = {name for name in files if name.endswith(".json")}
        assert json_names == {
            "method_card.proposed.json",
            "experiment_card.proposed.json",
        }, (lab_id, number)
        for name in json_names:
            record = load_json(planning_dir / name)
            assert record["schema_name"] not in forbidden_schemas

    assert all("PLANNING" not in path.parts for path in lab_export_paths(ROOT))


def test_executed_pilot_admission_docs_are_marked_historical():
    for lab_id, number, planning_dir, _ in executed_pilots():
        run_owner = f"labs/{lab_id}/EXPORTS/run_record.live_pilot_{number}.json"
        for filename in ["admission.md", "run_admission_update.md", "stop_condition.md"]:
            text = (planning_dir / filename).read_text()
            assert "Historical status: pre-run admission record" in text, (lab_id, number)
            assert f"current run status is owned by `{run_owner}`" in text, (lab_id, number)


def test_recorded_prompt_and_config_hashes_match_planning_files():
    for lab_id, number, planning_dir, exports_dir in executed_pilots():
        update = (planning_dir / "run_admission_update.md").read_text()
        payload = load_json(exports_dir / f"artifact_envelope.live_pilot_{number}.json")[
            "artifact"
        ]["payload"]

        recorded_prompt_hash = re.search(r"Prompt template SHA-256: `([0-9a-f]{64})`", update)
        assert recorded_prompt_hash, (lab_id, number)
        prompt_template = planning_dir / f"prompt_template.live_pilot_{number}.md"
        assert recorded_prompt_hash.group(1) == sha256_file(prompt_template)
        assert payload["prompt_template_sha256"] == recorded_prompt_hash.group(1)
        assert "{{APPROVED_SOURCE_TEXT}}" in prompt_template.read_text()

        recorded_config_hash = re.search(r"Config SHA-256: `([0-9a-f]{64})`", update)
        assert recorded_config_hash, (lab_id, number)
        config_record = extract_json_block(update, "Canonical Model Config")
        assert recorded_config_hash.group(1) == canonical_json_hash(config_record)
        assert payload["config_sha256"] == recorded_config_hash.group(1)


def test_no_secret_or_raw_source_material_in_tracked_lab_files():
    tracked = subprocess.run(
        ["git", "ls-files", "labs"],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.splitlines()
    assert tracked
    key_pattern = re.compile(r"sk-[A-Za-z0-9]{8,}")
    for relative in tracked:
        text = (ROOT / relative).read_text()
        assert "BEGIN RAW SOURCE" not in text, relative
        assert not key_pattern.search(text), relative
        assert '"api_key"' not in text, relative
        parts = relative.split("/")
        if len(parts) > 2 and parts[2] == "EXPORTS":
            assert "DEEPSEEK_API_KEY" not in text, relative
            assert '"provider_payload"' not in text, relative


def test_planning_is_never_an_export_surface():
    assert all("PLANNING" not in path.parts for path in lab_export_paths(ROOT))
    for lab_dir in lab_dirs():
        assert not (lab_dir / "EXPORTS" / "comparisons").exists()
    comparison_notes = list(ROOT.glob("labs/*/PLANNING/comparisons/*.md"))
    for note_path in comparison_notes:
        note = note_path.read_text()
        assert "not a synthesis export" in note
        assert "No winner is declared." in note


# ---------------------------------------------------------------------------
# Repo material boundaries
# ---------------------------------------------------------------------------


def test_raw_corpora_boundary_keeps_source_material_local_only():
    assert (ROOT / "raw_corpora" / "README.md").exists()

    for path in [
        "raw_corpora/trader_source_corpus/example.txt",
        "raw_corpora/selected/any_pilot/source.txt",
    ]:
        result = subprocess.run(
            ["git", "check-ignore", path],
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0, path

    readme_result = subprocess.run(
        ["git", "check-ignore", "raw_corpora/README.md"],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    assert readme_result.returncode == 1


def test_generated_summaries_are_ignored_by_default():
    gitignore = (ROOT / ".gitignore").read_text()
    assert "generated/*.json" in gitignore
    assert "generated/*.md" in gitignore
    assert "!generated/README.md" in gitignore
    assert (ROOT / "generated" / "README.md").exists()


# ---------------------------------------------------------------------------
# Synthesis contracts
# ---------------------------------------------------------------------------


def test_synthesis_imports_exports_and_writes_only_under_generated():
    before = {
        path: path.read_text()
        for path in active_benchmark_paths(ROOT) + lab_export_paths(ROOT)
    }
    summary = synthesize_exports(root=ROOT)
    assert summary["record_count"] == sum(1 for _ in all_lab_export_records())
    assert summary["labs"] == {path.name for path in lab_dirs()}
    assert "proposal_only" in summary["outcome_polarities"]
    assert (ROOT / "generated" / "synthesis_summary.json").exists()
    assert (ROOT / "generated" / "synthesis_summary.md").exists()
    after = {
        path: path.read_text()
        for path in active_benchmark_paths(ROOT) + lab_export_paths(ROOT)
    }
    assert after == before


def test_synthesis_can_import_live_exports_without_reading_planning(tmp_path):
    root = tmp_path / "repo"
    export_dir = root / "labs" / "long_context_judgment" / "EXPORTS"
    planning_dir = root / "labs" / "long_context_judgment" / "PLANNING"
    export_dir.mkdir(parents=True)
    planning_dir.mkdir(parents=True)
    (root / "PORTFOLIO_CURRENT.md").write_text("test root\n")
    (root / "pyproject.toml").write_text("[project]\nname = 'tmp'\n")
    run_record = live_pilot_schema_probe_records()[0]
    (export_dir / "run_record.live_pilot_001.json").write_text(
        json.dumps(run_record, indent=2) + "\n"
    )
    (planning_dir / "run_record.live_pilot_001.json").write_text(
        json.dumps(run_record, indent=2) + "\n"
    )

    summary = synthesize_exports(root=root)
    assert summary["record_count"] == 1
    assert summary["outcome_polarities"] == ["proposal_only"]
    assert summary["statuses"] == ["live_recorded"]
    assert summary["labs"] == {"long_context_judgment"}
    assert "fixture records only" not in summary["disclaimer"]


def test_synthesis_exposes_no_alternate_output_destination(tmp_path):
    assert list(inspect.signature(synthesize_exports).parameters) == ["root"]
    with pytest.raises(SystemExit):
        synthesis_cli_main(["--output-dir", str(tmp_path)])


def test_synthesis_cli_reports_export_records_not_fixture_only(capsys):
    assert synthesis_cli_main(["--root", str(ROOT)]) == 0
    output = capsys.readouterr().out
    assert "export records" in output
    assert "fixture records" not in output


def test_synthesis_generated_output_discloses_sorting_and_metric_limits():
    summary = synthesize_exports(root=ROOT)
    assert summary["ordering_note"] == (
        "Lists and schema counts are sorted alphabetically by identifier for deterministic "
        "inspection only; ordering is not a ranking."
    )
    assert summary["metrics_note"] == (
        "Counts are export inspection aids only; they are not method authority, graduation "
        "evidence, or portfolio decisions."
    )
    generated_markdown = (ROOT / "generated" / "synthesis_summary.md").read_text()
    assert summary["ordering_note"] in generated_markdown
    assert summary["metrics_note"] in generated_markdown


# ---------------------------------------------------------------------------
# Currentness routing contracts
# ---------------------------------------------------------------------------


def test_currentness_docs_route_without_ledgering():
    for name in CURRENTNESS_ROUTER_DOCS:
        assert_currentness_router_not_ledger((ROOT / name).read_text())


def test_currentness_docs_share_one_phase_and_route_to_existing_files():
    portfolio = (ROOT / "PORTFOLIO_CURRENT.md").read_text()
    phase_match = re.search(r"Current phase: `([a-z0-9-]+)`", portfolio)
    assert phase_match, "PORTFOLIO_CURRENT must declare the current phase"
    phase_line = phase_match.group(0)

    for name in ["README.md", "LAB_REGISTRY.md", "GRADUATION_LEDGER.md"]:
        text = (ROOT / name).read_text()
        if "Current phase:" in text:
            assert phase_line in text, name
    admission = (ROOT / "docs" / "live-llm-experiment-admission.md").read_text()
    assert phase_line in admission

    for name in CURRENTNESS_ROUTER_DOCS:
        text = (ROOT / name).read_text()
        for routed in re.findall(r"(?:labs|docs)/[^\s`*)]+\.(?:md|json)", text):
            assert (ROOT / routed).exists(), (name, routed)

    assert "## Next Recommended Research Direction" in portfolio


def test_registry_lists_exactly_the_labs_on_disk():
    registry = (ROOT / "LAB_REGISTRY.md").read_text()
    listed = set(re.findall(r"### `([a-z_]+)`", registry))
    assert listed == {path.name for path in lab_dirs()}


def test_graduation_ledger_remains_evidence_disciplined():
    graduation = (ROOT / "GRADUATION_LEDGER.md").read_text()
    assert "No graduated items." in graduation
    assert "## Current Non-Graduation Rule" in graduation
    assert "Fixture records are not evidence." in graduation
    assert "A proposal-only live pilot export set is not graduation evidence by itself." in (
        graduation
    )
    assert "Generated synthesis summaries are not evidence." in graduation


def test_admission_checklist_keeps_required_gates():
    admission = (ROOT / "docs" / "live-llm-experiment-admission.md").read_text()
    for required in [
        "Active Benchmark Pack",
        "MethodCard",
        "ExperimentCard",
        "Evaluator Plan",
        "Source / Privacy Boundary",
        "Prompt / Template Hash Plan",
        "Model / Config Recording Plan",
        "Output Artifact Types",
        "Negative-Result Value",
        "Stop Condition",
        "Budget / Secrets Handling",
        "Proposal-Only Statement",
    ]:
        assert required in admission


def test_architecture_rule_present_in_authority_docs():
    readme = (ROOT / "README.md").read_text()
    lifecycle = (ROOT / "docs" / "research-lifecycle.md").read_text()
    assert ARCHITECTURE_RULE in readme
    assert ARCHITECTURE_RULE in lifecycle
    assert "Future live experiments must pass" in readme
    assert "Milestone 2" in lifecycle
    assert "Tiny Live LLM Pilot" in lifecycle


def test_lab_docs_match_phase_posture():
    labs_with_live_records = {lab_id for lab_id, *_ in executed_pilots()}
    for lab_dir in lab_dirs():
        card = (lab_dir / "LAB_CARD.md").read_text()
        readme = (lab_dir / "README.md").read_text()
        question = (lab_dir / "RESEARCH_QUESTION.md").read_text()
        if lab_dir.name in labs_with_live_records:
            assert "Status: active live-pilot lab" in card
            assert "proposal-only" in card
            assert LAB_BOUNDARY_SENTENCE in card
            assert (
                "future live runs require live LLM admission and an explicit "
                "execution instruction"
            ) in card
            assert "Status: active live-pilot lab" in readme
            assert "proposal-only live export records" in readme
            assert "future live runs require live LLM admission" in readme
            assert "proposal-only live pilot records" in question
            assert "fixture records only" not in question
        else:
            assert "Status: scaffold fixture exports only" in card
            assert LAB_BOUNDARY_SENTENCE in card
            assert "Status: scaffold fixture exports only" in readme
            assert "fixture records only" in question
            assert "No real method result exists yet." in question


# ---------------------------------------------------------------------------
# Governance doctrine contracts
# ---------------------------------------------------------------------------


def test_agent_guides_encode_v3_operating_boundaries():
    root_agents = (ROOT / "AGENTS.md").read_text()
    protocol_agents = (ROOT / "packages" / "qf_v3_protocol" / "AGENTS.md").read_text()
    synthesis_agents = (ROOT / "packages" / "qf_v3_synthesis" / "AGENTS.md").read_text()
    labs_agents = (ROOT / "labs" / "AGENTS.md").read_text()
    benchmarks_agents = (ROOT / "benchmarks" / "AGENTS.md").read_text()
    docs_agents = (ROOT / "docs" / "AGENTS.md").read_text()

    assert (
        "V3 is a federated LLM-methodology research portfolio for discovering how messy "
        "trader source material can become useful trading intelligence."
    ) in root_agents
    assert ARCHITECTURE_RULE in root_agents
    assert "V3 must not become an append-only repo." in root_agents
    for required in [
        "Before adding new files, check whether an existing file, schema, test, prompt, "
        "planning pattern, or fixture should be reused, edited, generalized, deleted, "
        "or archived.",
        "Do not create a new script, helper, doc, test, or protocol field merely "
        "because this is a new method.",
        "If a new file is added, explain why an existing file could not own that role.",
        "rework it instead of layering another workaround on top",
    ]:
        assert required in root_agents
    assert "LLM Intelligence Is Central" in root_agents
    assert "Synthesis is read-only." in root_agents
    assert (
        "fixture -> proposed run -> evaluated run -> repeated evidence -> "
        "graduation candidate -> ADR-approved architecture"
        in root_agents
    )
    for required in [
        (
            "No item graduates merely because a scaffold fixture, planning packet, "
            "proposal-only live run, manual review, or generated synthesis summary exists."
        ),
        "Future graduation is portfolio-level, not lab-level.",
        "Until then, methods are experiments, not architecture.",
    ]:
        assert required in root_agents
    assert "Before changing files, agents must read:" in root_agents
    for local_overlay in [
        "packages/qf_v3_protocol/AGENTS.md",
        "packages/qf_v3_synthesis/AGENTS.md",
        "labs/AGENTS.md",
        "benchmarks/AGENTS.md",
        "docs/AGENTS.md",
    ]:
        assert f"* `{local_overlay}`" in root_agents

    assert "canonical protocol authority is the hand-authored JSON Schema files" in protocol_agents
    assert "Python code is tooling, not truth." in protocol_agents
    assert "Do not add lab-specific runtime logic here." in protocol_agents
    assert (
        "Before adding a protocol field, check whether an existing schema field, "
        "`payload`, `notes`, or a lab-local record can own the role."
        in protocol_agents
    )

    assert (
        "read-only with respect to labs, benchmarks, protocol schemas, and currentness docs"
        in synthesis_agents
    )
    assert "Generated outputs are non-authoritative and ignored by default." in synthesis_agents
    assert "Synthesis must not imply a winner through ordering" in synthesis_agents

    assert "Labs are playgrounds for methodological exploration." in labs_agents
    assert "Do not turn a lab method into shared architecture." in labs_agents
    assert (
        "Before adding files for a new lab method, reuse existing protocol records and "
        "adapt existing lab planning structure where possible."
        in labs_agents
    )
    assert (
        "Do not create live LLM runs until the live LLM experiment admission checklist "
        "is satisfied."
        in labs_agents
    )

    assert "Benchmark packs are metadata-safe test harnesses." in benchmarks_agents
    assert "Every active benchmark pack must include `v2_lesson_refs`." in benchmarks_agents

    assert (
        "Docs should clarify current direction, not accumulate contradictory history."
        in docs_agents
    )
    assert "Generated synthesis summaries must not be copied into docs as authority." in docs_agents
    assert "Superseded by:" in docs_agents
    assert (
        "Do not create a new doc merely because guidance changed; first update stale text "
        "directly, delete it, or archive it with supersession markers."
        in docs_agents
    )


def test_agent_checklists_prevent_append_only_drift_and_random_experiments():
    stale_cleanup = (
        ROOT / "docs" / "agent-checklists" / "stale-direction-cleanup-checklist.md"
    ).read_text()
    new_experiment = (
        ROOT / "docs" / "agent-checklists" / "new-experiment-checklist.md"
    ).read_text()

    for required in [
        "What current text does this supersede?",
        "Can the old file be deleted?",
        "Should the owning currentness doc be rewritten?",
        "Do not add a new current direction without resolving the old one.",
    ]:
        assert required in stale_cleanup

    for required in [
        "research question",
        "hypothesis",
        "fixture or live experiment classification",
        "live LLM admission status",
        "protocol export plan",
        "benchmark pack",
        "evaluator plan",
        "source/provenance plan",
        "negative-result value",
        "stop condition",
        "what result would change future behavior",
        "what stale material this experiment supersedes",
        "which existing file, schema, test, prompt, planning pattern, or fixture can be reused",
        "why any new file is needed instead of editing an existing owner",
        "whether a prior hardening choice should be reworked instead of worked around",
        "why this does not require shared architecture yet",
        "why this does not require protocol changes yet",
    ]:
        assert required in new_experiment


def test_recursive_contextual_meaning_plan_remains_future_only():
    plan = (
        ROOT / "docs" / "research-plans" / "recursive-contextual-meaning-loop.md"
    ).read_text()

    for required in [
        "Status: future method plan",
        "not active lab",
        "not protocol",
        "not architecture",
        "not current milestone",
        "not export evidence",
        "not graduation",
        "not current portfolio authority",
    ]:
        assert required in plan

    for forbidden in [
        "Current state: active",
        "Status: active",
        "is protocol authority",
        "is export evidence",
        "graduation evidence",
    ]:
        assert forbidden not in plan


def test_currentness_authority_surface_does_not_creep():
    build_prompt = (ROOT / "docs" / "build-prompts" / "scaffold-milestone-one.md").read_text()
    assert not (ROOT / "MILESTONE_GUIDE.md").exists()
    assert "MILESTONE_GUIDE.md" not in build_prompt
    assert "Superseded by:" in build_prompt


def test_boundary_contracts_stay_pilot_generic():
    text = Path(__file__).read_text()
    assert not re.search(r"def test_goal\d", text), (
        "per-goal tests are a run-history ledger; write pilot-generic invariants instead"
    )
    assert len(text.splitlines()) < 1500
