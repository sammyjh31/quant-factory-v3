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
PROMPT_TEMPLATE_SHA256 = "b842070956374c17ddd6d966c069c28ad4ff22dd753b20370c72cb03df79dae6"
CONFIG_SHA256 = "390729eba63d8b3ae2364631bb98b4ab2b218683cd069ba1c84778d26f2cdfac"
GOAL3_PILOT_DIR = (
    ROOT / "labs" / "long_context_judgment" / "PLANNING" / "live_llm_pilot_001"
)
GOAL7A_PILOT_DIR = (
    ROOT / "labs" / "chunked_source_grounding" / "PLANNING" / "live_llm_pilot_001"
)
GOAL6_CONTENT_REVIEW_PLAN = GOAL3_PILOT_DIR / "content_review_plan.md"
GOAL3_METHOD_ID = "long_context_judgment_live_pilot_001_method"
GOAL3_EXPERIMENT_ID = "long_context_judgment_live_pilot_001"
GOAL7A_METHOD_ID = "chunked_source_grounding_live_pilot_001_method"
GOAL7A_EXPERIMENT_ID = "chunked_source_grounding_live_pilot_001"
LIVE_PILOT_RUN_ID = "long_context_judgment_live_pilot_001_run"
LIVE_PILOT_ARTIFACT_ID = "long_context_judgment_live_pilot_001_artifact"
LIVE_PILOT_EVALUATION_ID = "long_context_judgment_live_pilot_001_eval"
LIVE_PILOT_CONTENT_REVIEW_EVALUATION_ID = (
    "long_context_judgment_live_pilot_001_manual_content_review"
)
LIVE_PILOT_NOTE_ID = "long_context_judgment_live_pilot_001_note"
LIVE_PILOT_SOURCE_REF_PREFIX = "raw_corpora_sha256:"
LIVE_PILOT_POST_RUN_EXPORTS = {
    "run_record.live_pilot_001.json",
    "artifact_envelope.live_pilot_001.json",
    "evaluation_record.live_pilot_001.json",
    "research_note.live_pilot_001.json",
}
LIVE_PILOT_CONTENT_REVIEW_EXPORT = "evaluation_record.live_pilot_001_manual_content_review.json"
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


def live_pilot_records():
    run_id = "long_context_judgment_live_pilot_001_run"
    artifact_id = "long_context_judgment_live_pilot_001_artifact"
    evaluation_id = "long_context_judgment_live_pilot_001_eval"
    source_ref = "raw_corpora_sha256:example_source_segment"
    return [
        {
            "protocol_version": "qf-v3-protocol-0.1",
            "schema_name": "RunRecord",
            "schema_version": CURRENT_SCHEMA_VERSION,
            "run_record": {
                "run_id": run_id,
                "lab_id": "long_context_judgment",
                "experiment_id": GOAL3_EXPERIMENT_ID,
                "method_id": GOAL3_METHOD_ID,
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
                "method_id": GOAL3_METHOD_ID,
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
                    "provider_id": "deepseek_api",
                    "model_id": "deepseek-v4-flash",
                    "prompt_template_sha256": PROMPT_TEMPLATE_SHA256,
                    "config_sha256": CONFIG_SHA256,
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
                "evaluator_id": "manual_boundary_review_v0",
                "evaluator_type": "manual_boundary_review",
                "benchmark_pack_id": "text_judgment_v0",
                "score": 1.0,
                "pass_fail": "pass",
                "failure_tags": [],
                "comments": (
                    "Boundary review only: raw source, provider payloads, prompts with source "
                    "text, traces, and secrets are not committed; output remains proposal-only."
                ),
            },
        },
        {
            "protocol_version": "qf-v3-protocol-0.1",
            "schema_name": "ResearchNote",
            "schema_version": CURRENT_SCHEMA_VERSION,
            "research_note": {
                "note_id": "long_context_judgment_live_pilot_001_note",
                "lab_id": "long_context_judgment",
                "experiment_ids": [GOAL3_EXPERIMENT_ID],
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


def manual_content_review_evaluation_record():
    return {
        "protocol_version": "qf-v3-protocol-0.1",
        "schema_name": "EvaluationRecord",
        "schema_version": CURRENT_SCHEMA_VERSION,
        "evaluation": {
            "evaluation_id": "long_context_judgment_live_pilot_001_content_review_eval",
            "lab_id": "long_context_judgment",
            "target_id": LIVE_PILOT_ARTIFACT_ID,
            "target_type": "artifact",
            "evaluator_id": "manual_content_review_v0",
            "evaluator_type": "manual_content_review",
            "benchmark_pack_id": "text_judgment_v0",
            "score": 0.5,
            "pass_fail": "fail",
            "failure_tags": ["weak_source_grounding", "too_generic"],
            "comments": (
                "Manual content review only; does not validate trading correctness, product "
                "readiness, strategy evidence, financial advice, live-trading authority, "
                "graduation, or architecture."
            ),
        },
    }


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


def test_protocol_v012_supports_proposal_only_live_pilot_records():
    for record in live_pilot_records():
        validate_record(record)


def test_protocol_v012_supports_manual_content_review_evaluation_records():
    record = manual_content_review_evaluation_record()
    validate_record(record)
    assert record["evaluation"]["target_id"] == LIVE_PILOT_ARTIFACT_ID
    assert record["evaluation"]["evaluator_type"] == "manual_content_review"


def test_protocol_v012_rejects_content_review_specific_fields():
    record = manual_content_review_evaluation_record()
    record["evaluation"]["content_review_payload"] = {
        "source_grounding": "not part of protocol v0.1.2"
    }

    with pytest.raises(ValidationError):
        validate_record(record)


def test_protocol_v012_rejects_fixture_live_semantic_mismatches():
    [run_record, *_] = live_pilot_records()

    fixture_with_live_polarity = json.loads(json.dumps(run_record))
    fixture_with_live_polarity["run_record"].update(
        {
            "run_kind": "scaffold_fixture",
            "outcome_polarity": "proposal_only",
            "status": "fixture_recorded",
        }
    )
    with pytest.raises(ValidationError):
        validate_record(fixture_with_live_polarity)

    live_with_fixture_polarity = json.loads(json.dumps(run_record))
    live_with_fixture_polarity["run_record"].update(
        {
            "run_kind": "live_llm_pilot",
            "outcome_polarity": "positive_fixture",
            "status": "live_recorded",
        }
    )
    with pytest.raises(ValidationError):
        validate_record(live_with_fixture_polarity)

    live_with_fixture_status = json.loads(json.dumps(run_record))
    live_with_fixture_status["run_record"].update(
        {
            "run_kind": "live_llm_pilot",
            "outcome_polarity": "proposal_only",
            "status": "fixture_recorded",
        }
    )
    with pytest.raises(ValidationError):
        validate_record(live_with_fixture_status)


def test_protocol_v012_keeps_schema_inventory_tiny_and_documented():
    schema_dir = ROOT / "packages" / "qf_v3_protocol" / "src" / "qf_v3_protocol" / "schemas"
    assert {path.name for path in schema_dir.glob("*.schema.json")} == PROTOCOL_SCHEMA_NAMES

    protocol_current = (ROOT / "PROTOCOL_CURRENT.md").read_text()
    graduation = (ROOT / "GRADUATION_LEDGER.md").read_text()
    adr = ROOT / "docs" / "adr" / "0001-allow-proposal-only-live-pilot-records.md"
    assert adr.exists()
    adr_text = adr.read_text()
    assert "proposal-only live LLM pilot" in adr_text
    assert "This is not a graduation." in adr_text
    assert "This does not add live trace, prompt, model-call, graph, product, strategy" in adr_text
    assert "Current schema version: `0.1.2`" in protocol_current
    assert "0.1.1 adds proposal-only live pilot record support" in protocol_current
    assert "0.1.2 adds `manual_content_review` as an `EvaluationRecord` evaluator type" in (
        protocol_current
    )
    assert "No new protocol object type is added by schema 0.1.2." in protocol_current
    assert "No other schema is part of protocol v0.1." in protocol_current
    assert "No graduated items." in graduation
    adr_0002 = ROOT / "docs" / "adr" / "0002-add-manual-content-review-evaluator.md"
    assert adr_0002.exists()
    adr_0002_text = adr_0002.read_text()
    assert "Add `manual_content_review` to `EvaluationRecord.evaluator_type`." in (
        adr_0002_text
    )
    assert "No new protocol object." in adr_0002_text
    assert "No LLM judge." in adr_0002_text
    assert "No validation claim." in adr_0002_text
    assert "No graduation." in adr_0002_text


def test_synthesis_can_import_live_exports_without_reading_planning(tmp_path):
    root = tmp_path / "repo"
    export_dir = root / "labs" / "long_context_judgment" / "EXPORTS"
    planning_dir = root / "labs" / "long_context_judgment" / "PLANNING"
    export_dir.mkdir(parents=True)
    planning_dir.mkdir(parents=True)
    (root / "PORTFOLIO_CURRENT.md").write_text("test root\n")
    (root / "pyproject.toml").write_text("[project]\nname = 'tmp'\n")
    (export_dir / "run_record.live_pilot_001.json").write_text(
        json.dumps(live_pilot_records()[0], indent=2) + "\n"
    )
    (planning_dir / "run_record.live_pilot_001.json").write_text(
        json.dumps(live_pilot_records()[0], indent=2) + "\n"
    )

    summary = synthesize_exports(root=root)
    assert summary["record_count"] == 1
    assert summary["outcome_polarities"] == ["proposal_only"]
    assert summary["statuses"] == ["live_recorded"]
    assert summary["labs"] == {"long_context_judgment"}
    assert "fixture records only" not in summary["disclaimer"]


def test_raw_corpora_boundary_keeps_source_material_local_only():
    assert (ROOT / "raw_corpora" / "README.md").exists()

    ignored_paths = [
        "raw_corpora/trader_source_corpus/example.txt",
        "raw_corpora/selected/live_llm_pilot_001/source.txt",
    ]
    for path in ignored_paths:
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


def test_active_benchmark_packs_validate_and_preserve_v2_refs():
    paths = active_benchmark_paths(ROOT)
    assert len(paths) == 3
    assert {path.stem for path in paths} == {
        "source_grounding_v0",
        "text_judgment_v0",
        "visual_deictic_v0",
    }
    for path in paths:
        record = load_json(path)
        validate_record(record)
        benchmark = record["benchmark_pack"]
        assert benchmark["v2_lesson_refs"]
        assert benchmark["metadata_safety"] == {
            "raw_source_material_included": False,
            "private_or_provider_payload_included": False,
            "synthetic_or_placeholder_only": True,
        }


def test_future_candidate_packs_are_not_active():
    future_paths = sorted((ROOT / "benchmarks" / "future_candidates").glob("*"))
    assert {path.stem for path in future_paths} == {
        "formula_missing_v0",
        "judgment_artifact_seed_v0",
    }
    assert all(path.suffix == ".md" for path in future_paths)


def test_all_lab_exports_validate_and_include_positive_and_negative_fixtures():
    export_paths = lab_export_paths(ROOT)
    expected_labs = {
        "chunked_source_grounding",
        "long_context_judgment",
        "visual_deictic_understanding",
    }
    assert {path.parents[1].name for path in export_paths} == expected_labs
    fixture_paths = {path for path in export_paths if path.name == "fixture_records.json"}
    assert len(fixture_paths) == 3
    live_export_dir = ROOT / "labs" / "long_context_judgment" / "EXPORTS"
    assert {path.name for path in live_export_dir.glob("*.live_pilot_001.json")} == (
        LIVE_PILOT_POST_RUN_EXPORTS
    )
    for path in export_paths:
        records = list(iter_records(path))
        assert records
        for record in records:
            validate_record(record)
        if path.name != "fixture_records.json":
            continue
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
    old_names = {
        "source_grounding",
        "review_state",
        "product_fitness",
        "validation_scope",
        "retirement_state",
    }
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
        assert old_names.isdisjoint(posture)
        assert forbidden_statuses.isdisjoint(posture.values())


def test_run_records_link_required_protocol_ids():
    method_ids = {record["method_card"]["method_id"] for record in records_by_schema("MethodCard")}
    planning_method_ids = {
        load_json(GOAL3_PILOT_DIR / "method_card.proposed.json")["method_card"]["method_id"]
    }
    experiment_ids = {
        record["experiment_card"]["experiment_id"] for record in records_by_schema("ExperimentCard")
    }
    planning_experiment_ids = {
        load_json(GOAL3_PILOT_DIR / "experiment_card.proposed.json")["experiment_card"][
            "experiment_id"
        ]
    }
    artifact_ids = {
        record["artifact"]["artifact_id"] for record in records_by_schema("ArtifactEnvelope")
    }
    evaluation_ids = {
        record["evaluation"]["evaluation_id"]
        for record in records_by_schema("EvaluationRecord")
    }
    benchmark_ids = {
        load_json(path)["benchmark_pack"]["benchmark_id"] for path in active_benchmark_paths(ROOT)
    }

    for record in records_by_schema("RunRecord"):
        run = record["run_record"]
        if run["run_kind"] == "live_llm_pilot":
            assert run["method_id"] in planning_method_ids
            assert run["experiment_id"] in planning_experiment_ids
        else:
            assert run["method_id"] in method_ids
            assert run["experiment_id"] in experiment_ids
        assert run["benchmark_pack_id"] in benchmark_ids
        assert run["source_refs"]
        assert set(run["artifact_ids"]).issubset(artifact_ids)
        assert set(run["evaluation_ids"]).issubset(evaluation_ids)


def test_research_notes_and_llm_judge_placeholders_are_bounded():
    notes = records_by_schema("ResearchNote")
    assert notes
    for record in notes:
        note = record["research_note"]
        disclaimer = record["research_note"]["evidence_disclaimer"]
        if note["note_id"] == LIVE_PILOT_NOTE_ID:
            assert disclaimer == LIVE_EVIDENCE_DISCLAIMER
        else:
            assert disclaimer == FIXTURE_EVIDENCE_DISCLAIMER

    llm_placeholder_evals = [
        record["evaluation"]
        for record in records_by_schema("EvaluationRecord")
        if record["evaluation"]["evaluator_type"] == "llm_judge_placeholder"
    ]
    assert llm_placeholder_evals
    for evaluation in llm_placeholder_evals:
        assert evaluation["placeholder_disclaimer"] == (
            "No live LLM judge was called. This is a scaffold fixture only."
        )


def test_synthesis_imports_exports_and_writes_only_under_generated():
    before = {
        path: path.read_text()
        for path in active_benchmark_paths(ROOT) + lab_export_paths(ROOT)
    }
    summary = synthesize_exports(root=ROOT)
    assert summary["record_count"] == sum(1 for _ in all_lab_export_records())
    assert summary["labs"] == {
        "chunked_source_grounding",
        "long_context_judgment",
        "visual_deictic_understanding",
    }
    assert (ROOT / "generated" / "synthesis_summary.json").exists()
    assert (ROOT / "generated" / "synthesis_summary.md").exists()
    after = {
        path: path.read_text()
        for path in active_benchmark_paths(ROOT) + lab_export_paths(ROOT)
    }
    assert after == before


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
        "Counts are scaffold inspection aids only; they are not method authority, graduation "
        "evidence, or portfolio decisions."
    )
    generated_markdown = (ROOT / "generated" / "synthesis_summary.md").read_text()
    assert summary["ordering_note"] in generated_markdown
    assert summary["metrics_note"] in generated_markdown


def test_generated_summaries_are_ignored_by_default():
    gitignore = (ROOT / ".gitignore").read_text()
    assert "generated/*.json" in gitignore
    assert "generated/*.md" in gitignore
    assert "!generated/README.md" in gitignore
    assert (ROOT / "generated" / "README.md").exists()


def test_goal3_live_pilot_planning_packet_is_contained_and_current():
    required_files = {
        "admission.md",
        "method_card.proposed.json",
        "experiment_card.proposed.json",
        "evaluator_plan.md",
        "source_privacy_boundary.md",
        "prompt_config_recording_plan.md",
        "stop_condition.md",
        "run_admission_update.md",
        "prompt_template.live_pilot_001.md",
        "content_review_plan.md",
    }
    assert GOAL3_PILOT_DIR.exists()
    assert {path.name for path in GOAL3_PILOT_DIR.iterdir() if path.is_file()} == required_files

    method_card = load_json(GOAL3_PILOT_DIR / "method_card.proposed.json")
    experiment_card = load_json(GOAL3_PILOT_DIR / "experiment_card.proposed.json")
    validate_record(method_card)
    validate_record(experiment_card)
    assert method_card["schema_name"] == "MethodCard"
    assert method_card["method_card"]["method_id"] == GOAL3_METHOD_ID
    assert experiment_card["schema_name"] == "ExperimentCard"
    assert experiment_card["experiment_card"]["experiment_id"] == GOAL3_EXPERIMENT_ID
    assert experiment_card["experiment_card"]["method_ids"] == [GOAL3_METHOD_ID]

    planning_records = [method_card, experiment_card]
    assert {record["schema_name"] for record in planning_records} == {
        "MethodCard",
        "ExperimentCard",
    }
    forbidden_live_record_schemas = {
        "RunRecord",
        "ArtifactEnvelope",
        "EvaluationRecord",
        "ResearchNote",
    }
    assert forbidden_live_record_schemas.isdisjoint(
        {record["schema_name"] for record in planning_records}
    )
    assert "EXPORTS" not in GOAL3_PILOT_DIR.parts
    assert all("PLANNING" not in path.parts for path in lab_export_paths(ROOT))

    admission = (GOAL3_PILOT_DIR / "admission.md").read_text()
    for required_heading in [
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
        assert required_heading in admission
    for required_guardrail in [
        "This is a proposed live LLM pilot planning record.",
        "The separate `run_admission_update.md` authorized exactly one tiny live LLM pilot run.",
        "The planning packet is still not research evidence",
        "No method success is claimed.",
        "not a synthesis export",
    ]:
        assert required_guardrail in admission

    assert all("PLANNING" not in path.parts for path in lab_export_paths(ROOT))

    portfolio = (ROOT / "PORTFOLIO_CURRENT.md").read_text()
    lab_registry = (ROOT / "LAB_REGISTRY.md").read_text()
    assert GOAL3_EXPERIMENT_ID in portfolio
    assert GOAL3_EXPERIMENT_ID in lab_registry
    assert "not in `EXPORTS/`" in lab_registry


def test_goal4_live_pilot_run_admission_update_preserves_admitted_scope():
    update_path = GOAL3_PILOT_DIR / "run_admission_update.md"
    prompt_template_path = GOAL3_PILOT_DIR / "prompt_template.live_pilot_001.md"
    update = update_path.read_text()
    prompt_template = prompt_template_path.read_text()

    assert (
        "This admission update authorized exactly one tiny live LLM pilot run under "
        "the stated scope."
        in update
    )
    for required in [
        "Provider: DeepSeek API",
        "API format: OpenAI-compatible chat completions",
        "Base URL: `https://api.deepseek.com`",
        "Model: `deepseek-v4-flash`",
        "Reasoning/thinking mode: non-thinking",
        "Benchmark pack: `text_judgment_v0`",
        "Lab: `labs/long_context_judgment`",
        "Purpose: containment/protocol proof, not breakthrough quality.",
        "Budget cap: `$3` hard maximum.",
        "No retries unless the call fails before producing output.",
        "`DEEPSEEK_API_KEY`",
        "If `deepseek-v4-flash` is unavailable in the account, stop and report.",
        "Do not silently substitute `deepseek-v4-pro`, `deepseek-chat`, "
        "`deepseek-reasoner`, or any other model.",
        "Outputs from this experiment are proposals until evaluated.",
    ]:
        assert required in update

    assert "thinking" in update
    assert '"type": "disabled"' in update
    assert "tools disabled" in update
    assert "one approved source scope" in update
    assert "one prompt/template version" in update
    assert "one model configuration" in update
    assert "one model-call batch" in update
    assert "No private/raw source material or provider payloads are committed." in update
    assert "No validation, product authority, strategy evidence, financial advice" in update
    assert "live-trading authority, or architecture." in update

    recorded_prompt_hash = re.search(r"Prompt template SHA-256: `([0-9a-f]{64})`", update)
    assert recorded_prompt_hash
    assert recorded_prompt_hash.group(1) == sha256_file(prompt_template_path)
    assert "Prompt Template" in prompt_template
    assert "{{APPROVED_SOURCE_TEXT}}" in prompt_template
    assert "No raw source text is committed in this template." in prompt_template

    config_record = extract_json_block(update, "Canonical Model Config")
    recorded_config_hash = re.search(r"Config SHA-256: `([0-9a-f]{64})`", update)
    assert recorded_config_hash
    assert recorded_config_hash.group(1) == canonical_json_hash(config_record)
    assert config_record == {
        "api_format": "openai_compatible_chat_completions",
        "base_url": "https://api.deepseek.com",
        "context_window_provider_limit": "1M",
        "max_input_tokens": 12000,
        "max_output_tokens": 1200,
        "model_id": "deepseek-v4-flash",
        "provider_id": "deepseek_api",
        "sampling": {
            "frequency_penalty": None,
            "presence_penalty": None,
            "temperature": None,
            "top_p": None,
        },
        "stream": False,
        "thinking": {"type": "disabled"},
        "tool_routing": "none",
    }

    for expected_path in [
        "provider_payloads/live_llm_pilot_001/",
        "model_traces/live_llm_pilot_001/",
        "prompt_traces/live_llm_pilot_001/",
    ]:
        assert expected_path in update

    for expected_export in LIVE_PILOT_POST_RUN_EXPORTS:
        assert f"labs/long_context_judgment/EXPORTS/{expected_export}" in update

    summary = synthesize_exports(root=ROOT)
    assert summary["record_count"] == 32
    assert GOAL3_METHOD_ID in summary["methods"]
    assert summary["outcome_polarities"] == [
        "negative_fixture",
        "positive_fixture",
        "proposal_only",
    ]
    assert summary["statuses"] == ["fixture_recorded", "live_recorded"]

    graduation = (ROOT / "GRADUATION_LEDGER.md").read_text()
    assert "No graduated items." in graduation
    assert "first Goal 5 proposal-only live pilot export set does not affect graduation status" in (
        graduation
    )

    readme = (ROOT / "README.md").read_text()
    portfolio = (ROOT / "PORTFOLIO_CURRENT.md").read_text()
    lab_registry = (ROOT / "LAB_REGISTRY.md").read_text()
    for currentness_doc in [readme, portfolio, lab_registry]:
        assert "run_admission_update.md" in currentness_doc
        assert "no live LLM call has been made" not in currentness_doc.lower()
        assert "No live LLM experiment has run." not in currentness_doc
    assert "one admitted tiny live LLM pilot export set" in portfolio


def test_goal5_live_pilot_export_set_is_protocol_valid_and_bounded():
    export_dir = ROOT / "labs" / "long_context_judgment" / "EXPORTS"
    live_exports = {path.name: load_json(path) for path in export_dir.glob("*.live_pilot_001.json")}
    assert set(live_exports) == LIVE_PILOT_POST_RUN_EXPORTS
    for record in live_exports.values():
        validate_record(record)

    run = live_exports["run_record.live_pilot_001.json"]
    artifact = live_exports["artifact_envelope.live_pilot_001.json"]
    evaluation = live_exports["evaluation_record.live_pilot_001.json"]
    note = live_exports["research_note.live_pilot_001.json"]

    assert run["schema_name"] == "RunRecord"
    assert run["schema_version"] == CURRENT_SCHEMA_VERSION
    run_record = run["run_record"]
    assert run_record == {
        "run_id": LIVE_PILOT_RUN_ID,
        "lab_id": "long_context_judgment",
        "experiment_id": GOAL3_EXPERIMENT_ID,
        "method_id": GOAL3_METHOD_ID,
        "benchmark_pack_id": "text_judgment_v0",
        "source_refs": run_record["source_refs"],
        "artifact_ids": [LIVE_PILOT_ARTIFACT_ID],
        "evaluation_ids": [LIVE_PILOT_EVALUATION_ID],
        "run_kind": "live_llm_pilot",
        "outcome_polarity": "proposal_only",
        "status": "live_recorded",
    }
    assert len(run_record["source_refs"]) == 1
    assert run_record["source_refs"][0].startswith(LIVE_PILOT_SOURCE_REF_PREFIX)

    artifact_payload = artifact["artifact"]["payload"]
    assert artifact["artifact"]["artifact_id"] == LIVE_PILOT_ARTIFACT_ID
    assert artifact["artifact"]["artifact_type"] == "judgment_principle_proposal"
    assert artifact["artifact"]["run_id"] == LIVE_PILOT_RUN_ID
    assert artifact["artifact"]["source_refs"] == run_record["source_refs"]
    assert artifact["artifact"]["posture"] == {
        "grounding_status": "source_linked",
        "review_status": "self_checked",
        "readiness_status": "study_candidate",
        "validation_status": "none",
        "lifecycle_status": "active",
    }
    assert "proposal_only_not_evaluated" in artifact["artifact"]["blockers"]
    assert artifact_payload["outcome_polarity"] == "proposal_only"
    assert artifact_payload["proposal_only"] is True
    assert artifact_payload["provider_id"] == "deepseek_api"
    assert artifact_payload["base_url"] == "https://api.deepseek.com"
    assert artifact_payload["model_id"] == "deepseek-v4-flash"
    assert artifact_payload["thinking"] == {"type": "disabled"}
    assert artifact_payload["stream"] is False
    assert artifact_payload["prompt_template_sha256"] == PROMPT_TEMPLATE_SHA256
    assert artifact_payload["config_sha256"] == CONFIG_SHA256
    assert artifact_payload["source_metadata"]["source_ref"] == run_record["source_refs"][0]
    assert artifact_payload["source_metadata"]["excerpt_word_count"] >= 300
    assert artifact_payload["source_metadata"]["excerpt_word_count"] <= 1000
    assert artifact_payload["cost_metadata"]["budget_cap_usd"] == 3.0
    assert artifact_payload["cost_metadata"]["estimated_cost_usd"] <= 3.0
    assert artifact_payload["raw_source_text_committed"] is False
    assert artifact_payload["raw_provider_payload_committed"] is False
    assert artifact_payload["raw_prompt_trace_committed"] is False
    assert artifact_payload["secrets_committed"] is False
    assert "raw_source_text" not in artifact_payload
    assert "provider_payload" not in artifact_payload
    assert "api_key" not in json.dumps(artifact_payload).lower()

    assert evaluation["evaluation"]["evaluation_id"] == LIVE_PILOT_EVALUATION_ID
    assert evaluation["evaluation"]["target_id"] == LIVE_PILOT_ARTIFACT_ID
    assert evaluation["evaluation"]["evaluator_type"] == "manual_boundary_review"
    assert evaluation["evaluation"]["pass_fail"] == "pass"
    assert "method quality was not evaluated" in evaluation["evaluation"]["comments"]

    research_note = note["research_note"]
    assert research_note["note_id"] == LIVE_PILOT_NOTE_ID
    assert research_note["experiment_ids"] == [GOAL3_EXPERIMENT_ID]
    assert research_note["benchmark_pack_ids"] == ["text_judgment_v0"]
    assert research_note["evidence_disclaimer"] == LIVE_EVIDENCE_DISCLAIMER
    assert any("No method success is claimed" in item for item in research_note["what_failed"])

    combined_committed = "\n".join(
        path.read_text()
        for path in [
            export_dir / name
            for name in sorted(LIVE_PILOT_POST_RUN_EXPORTS)
        ]
    )
    for forbidden in [
        "BEGIN RAW SOURCE",
        "DEEPSEEK_API_KEY",
        "sk-",
        "\"api_key\"",
        "\"provider_payload\"",
    ]:
        assert forbidden not in combined_committed


def test_goal6_content_review_plan_is_planning_only_and_calibrates_evaluators():
    export_dir = ROOT / "labs" / "long_context_judgment" / "EXPORTS"
    plan = GOAL6_CONTENT_REVIEW_PLAN.read_text()
    live_export_names = {path.name for path in export_dir.glob("*.live_pilot_001.json")}
    protocol_schema_names = {
        path.name
        for path in (
            ROOT / "packages" / "qf_v3_protocol" / "src" / "qf_v3_protocol" / "schemas"
        ).glob("*.schema.json")
    }

    assert live_export_names == LIVE_PILOT_POST_RUN_EXPORTS
    assert (export_dir / LIVE_PILOT_CONTENT_REVIEW_EXPORT).exists()
    assert protocol_schema_names == PROTOCOL_SCHEMA_NAMES

    for required in [
        "Status: Goal 6 content-review planning record",
        "Do not call an LLM.",
        "Do not run another model.",
        "Do not create new live-run records.",
        "Goal 6C-B creates exactly one `manual_content_review` EvaluationRecord.",
        "Do not graduate anything.",
        (
            "Do not commit raw model output, raw provider payload, raw prompt trace, "
            "raw source text, or secrets."
        ),
        "labs/long_context_judgment/EXPORTS/artifact_envelope.live_pilot_001.json",
        "model_traces/live_llm_pilot_001/model_output.txt",
        "provider_payloads/live_llm_pilot_001/response.json",
        "source-grounding review",
        "usefulness review",
        "hallucination / unsupported-claim review",
        "abstraction-quality review",
        "negative-result value",
        "manual_content_review",
        "Schema 0.1.2 adds protocol support for `manual_content_review`.",
        "The next experiment should improve evaluator quality before running a second method.",
    ]:
        assert required in plan

    assert (
        "EvaluationRecord can now honestly represent a completed manual content review"
        in plan
    )
    assert "Goal 6C-A did not create the content-review export." in plan
    assert "Goal 6C-B is the separately authorized content-review export task." in plan
    assert "raw_source_text" not in plan
    assert "DEEPSEEK_API_KEY" not in plan
    assert "financial advice" in plan
    assert "architecture" in plan


def test_goal6c_b_manual_content_review_export_is_single_bounded_and_current():
    export_dir = ROOT / "labs" / "long_context_judgment" / "EXPORTS"
    content_review_path = export_dir / LIVE_PILOT_CONTENT_REVIEW_EXPORT
    assert content_review_path.exists()

    record = load_json(content_review_path)
    validate_record(record)
    assert record["schema_name"] == "EvaluationRecord"
    assert record["schema_version"] == CURRENT_SCHEMA_VERSION

    evaluation = record["evaluation"]
    assert evaluation["evaluation_id"] == LIVE_PILOT_CONTENT_REVIEW_EVALUATION_ID
    assert evaluation["lab_id"] == "long_context_judgment"
    assert evaluation["target_id"] == LIVE_PILOT_ARTIFACT_ID
    assert evaluation["target_type"] == "artifact"
    assert evaluation["evaluator_id"] == "manual_content_review_live_pilot_001"
    assert evaluation["evaluator_type"] == "manual_content_review"
    assert evaluation["benchmark_pack_id"] == "text_judgment_v0"
    assert evaluation["score"] == pytest.approx(0.74)
    assert evaluation["pass_fail"] == "pass"
    assert evaluation["failure_tags"] == [
        "missing_context",
        "over_abstracted_teacher_intent",
    ]

    comments = evaluation["comments"]
    for required in [
        "Manual content review only",
        "source grounding",
        "research usefulness",
        "hallucination / unsupported claims",
        "abstraction quality",
        "negative-result value",
        (
            "not validation, product evidence, strategy evidence, financial advice, "
            "live-trading authority, graduation, or architecture"
        ),
    ]:
        assert required in comments
    assert "raw source text and raw model output are not committed" in comments.lower()

    combined_committed = "\n".join(
        path.read_text()
        for path in [
            content_review_path,
            ROOT / "PORTFOLIO_CURRENT.md",
            ROOT / "LAB_REGISTRY.md",
        ]
    )
    for forbidden in [
        "BEGIN RAW SOURCE",
        "DEEPSEEK_API_KEY",
        "sk-",
        "\"api_key\"",
        "\"provider_payload\"",
        "raw_source_text",
        "raw_model_output",
    ]:
        assert forbidden not in combined_committed

    manual_content_reviews = [
        record["evaluation"]
        for record in records_by_schema("EvaluationRecord")
        if record["evaluation"]["evaluator_type"] == "manual_content_review"
    ]
    assert [review["evaluation_id"] for review in manual_content_reviews] == [
        LIVE_PILOT_CONTENT_REVIEW_EVALUATION_ID
    ]
    assert not list(export_dir.glob("run_record.*manual_content_review*.json"))
    assert not list(export_dir.glob("artifact_envelope.*manual_content_review*.json"))
    assert not list(export_dir.glob("research_note.*manual_content_review*.json"))

    portfolio = (ROOT / "PORTFOLIO_CURRENT.md").read_text()
    lab_registry = (ROOT / "LAB_REGISTRY.md").read_text()
    assert LIVE_PILOT_CONTENT_REVIEW_EXPORT in portfolio
    assert LIVE_PILOT_CONTENT_REVIEW_EXPORT in lab_registry
    assert "one manual content-review EvaluationRecord" in portfolio
    assert "one manual content-review EvaluationRecord" in lab_registry
    assert "generated synthesis metrics" not in portfolio.lower()

    graduation = (ROOT / "GRADUATION_LEDGER.md").read_text()
    assert "No graduated items." in graduation


def test_goal7a_chunked_source_grounding_planning_packet_is_contained_and_current():
    required_files = {
        "admission.md",
        "method_card.proposed.json",
        "experiment_card.proposed.json",
        "evaluator_plan.md",
        "source_privacy_boundary.md",
        "prompt_template.live_pilot_001.md",
        "run_admission_update.md",
        "stop_condition.md",
    }
    assert GOAL7A_PILOT_DIR.exists()
    assert {path.name for path in GOAL7A_PILOT_DIR.iterdir() if path.is_file()} == (
        required_files
    )

    method_card = load_json(GOAL7A_PILOT_DIR / "method_card.proposed.json")
    experiment_card = load_json(GOAL7A_PILOT_DIR / "experiment_card.proposed.json")
    validate_record(method_card)
    validate_record(experiment_card)
    assert method_card["schema_name"] == "MethodCard"
    assert method_card["schema_version"] == CURRENT_SCHEMA_VERSION
    assert method_card["method_card"]["method_id"] == GOAL7A_METHOD_ID
    assert method_card["method_card"]["lab_id"] == "chunked_source_grounding"
    assert method_card["method_card"]["method_family"] == (
        "chunked_source_grounded_llm_reader_proposed"
    )
    assert "chunked_source_grounding_proposal" in method_card["method_card"][
        "intended_outputs"
    ]
    assert "not a completed run" in method_card["method_card"]["non_goals"]
    assert "not architecture or graduation evidence" in method_card["method_card"]["non_goals"]

    assert experiment_card["schema_name"] == "ExperimentCard"
    assert experiment_card["schema_version"] == CURRENT_SCHEMA_VERSION
    experiment = experiment_card["experiment_card"]
    assert experiment["experiment_id"] == GOAL7A_EXPERIMENT_ID
    assert experiment["lab_id"] == "chunked_source_grounding"
    assert experiment["benchmark_pack_ids"] == ["text_judgment_v0"]
    assert experiment["method_ids"] == [GOAL7A_METHOD_ID]
    assert experiment["expected_artifact_types"] == [
        "chunked_source_grounding_proposal"
    ]
    assert "same source excerpt" in experiment["hypothesis"]
    assert "long_context_judgment_live_pilot_001" in experiment["evaluation_plan"]

    planning_records = [method_card, experiment_card]
    forbidden_live_record_schemas = {
        "RunRecord",
        "ArtifactEnvelope",
        "EvaluationRecord",
        "ResearchNote",
    }
    assert forbidden_live_record_schemas.isdisjoint(
        {record["schema_name"] for record in planning_records}
    )
    assert "EXPORTS" not in GOAL7A_PILOT_DIR.parts
    assert all("PLANNING" not in path.parts for path in lab_export_paths(ROOT))
    assert not list(
        (ROOT / "labs" / "chunked_source_grounding" / "EXPORTS").glob(
            "*.live_pilot_001.json"
        )
    )

    admission = (GOAL7A_PILOT_DIR / "admission.md").read_text()
    for required_heading in [
        "Hardening / Cleanup Discipline",
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
        assert required_heading in admission
    for required_guardrail in [
        "This is a proposed live LLM pilot planning record.",
        "This is planning/admission only. No LLM call has been made.",
        "Do not add around stale structure. Rework, replace, delete, or archive it.",
        "The planning packet is not research evidence",
        "not a synthesis export",
        "No method success is claimed.",
        "No RunRecord, ArtifactEnvelope, EvaluationRecord, or ResearchNote exists for this pilot.",
    ]:
        assert required_guardrail in admission

    evaluator_plan = (GOAL7A_PILOT_DIR / "evaluator_plan.md").read_text()
    for required in [
        "schema_check",
        "manual_boundary_review",
        "manual_content_review",
        "source grounding",
        "research usefulness",
        "comparison value against `long_context_judgment`",
    ]:
        assert required in evaluator_plan

    source_boundary = (GOAL7A_PILOT_DIR / "source_privacy_boundary.md").read_text()
    for required in [
        "raw_corpora_sha256:d8392c58c3b740eb",
        "raw_corpora/selected/live_llm_pilot_001/source.txt",
        "raw_corpora/trader_source_corpus/transcripts/how-to-use-market-profile-start-now-trading-tutorials.txt",
        "Do not commit raw source text.",
        "same approved excerpt as `long_context_judgment_live_pilot_001`",
    ]:
        assert required in source_boundary

    update = (GOAL7A_PILOT_DIR / "run_admission_update.md").read_text()
    prompt_template_path = GOAL7A_PILOT_DIR / "prompt_template.live_pilot_001.md"
    prompt_template = prompt_template_path.read_text()
    for required in [
        (
            "This admission update defines the executable preflight scope for exactly "
            "one future tiny live LLM pilot run."
        ),
        (
            "It does not by itself authorize execution. Execution requires a separate "
            "Goal 7B instruction."
        ),
        "Provider: DeepSeek API",
        "API format: OpenAI-compatible chat completions",
        "Base URL: `https://api.deepseek.com`",
        "Model: `deepseek-v4-flash`",
        "Reasoning/thinking mode: non-thinking",
        "Benchmark pack: `text_judgment_v0`",
        "Lab: `labs/chunked_source_grounding`",
        "Budget cap: `$3` hard maximum.",
        "No retries unless the call fails before producing output.",
        "Do not silently substitute `deepseek-v4-pro`, `deepseek-chat`, "
        "`deepseek-reasoner`, or any other model.",
        "Outputs from this experiment are proposals until evaluated.",
        "No private/raw source material or provider payloads are committed.",
    ]:
        assert required in update
    assert "thinking" in update
    assert '"type": "disabled"' in update
    assert "one model-call batch" in update
    assert "same approved excerpt as `long_context_judgment_live_pilot_001`" in update
    assert "authorizes exactly one tiny live LLM pilot run" not in update

    recorded_prompt_hash = re.search(r"Prompt template SHA-256: `([0-9a-f]{64})`", update)
    assert recorded_prompt_hash
    assert recorded_prompt_hash.group(1) == sha256_file(prompt_template_path)
    assert "Prompt Template" in prompt_template
    assert "{{APPROVED_SOURCE_TEXT}}" in prompt_template
    assert "No raw source text is committed in this template." in prompt_template

    config_record = extract_json_block(update, "Canonical Model Config")
    recorded_config_hash = re.search(r"Config SHA-256: `([0-9a-f]{64})`", update)
    assert recorded_config_hash
    assert recorded_config_hash.group(1) == canonical_json_hash(config_record)
    assert config_record == {
        "api_format": "openai_compatible_chat_completions",
        "base_url": "https://api.deepseek.com",
        "context_window_provider_limit": "1M",
        "max_input_tokens": 12000,
        "max_output_tokens": 1200,
        "model_id": "deepseek-v4-flash",
        "provider_id": "deepseek_api",
        "sampling": {
            "frequency_penalty": None,
            "presence_penalty": None,
            "temperature": None,
            "top_p": None,
        },
        "stream": False,
        "thinking": {"type": "disabled"},
        "tool_routing": "none",
    }

    for forbidden in [
        "BEGIN RAW SOURCE",
        "DEEPSEEK_API_KEY=",
        "sk-",
        "\"api_key\"",
        "\"provider_payload\"",
    ]:
        combined = "\n".join(path.read_text() for path in GOAL7A_PILOT_DIR.iterdir())
        assert forbidden not in combined

    summary = synthesize_exports(root=ROOT)
    assert summary["record_count"] == 32
    assert GOAL7A_METHOD_ID not in summary["methods"]

    readme = (ROOT / "README.md").read_text()
    portfolio = (ROOT / "PORTFOLIO_CURRENT.md").read_text()
    lab_registry = (ROOT / "LAB_REGISTRY.md").read_text()
    for currentness_doc in [readme, portfolio, lab_registry]:
        assert GOAL7A_EXPERIMENT_ID in currentness_doc
        assert "generated synthesis metrics" not in currentness_doc.lower()
    assert "fixture exports plus Goal 7A planning packet" in portfolio
    assert "fixture exports plus Goal 7A planning packet" in lab_registry
    assert "No graduated items." in (ROOT / "GRADUATION_LEDGER.md").read_text()


def test_authority_docs_preserve_scaffold_boundaries():
    readme = (ROOT / "README.md").read_text()
    lifecycle = (ROOT / "docs" / "research-lifecycle.md").read_text()
    llm_model = (ROOT / "docs" / "llm-experimentation-model.md").read_text()
    portfolio = (ROOT / "PORTFOLIO_CURRENT.md").read_text()
    graduation = (ROOT / "GRADUATION_LEDGER.md").read_text()
    admission = (ROOT / "docs" / "live-llm-experiment-admission.md").read_text()

    architecture_rule = (
        "No new experiment becomes architecture.\n"
        "It becomes records first.\n"
        "Architecture changes only after repeated evidence and explicit ADR."
    )
    assert architecture_rule in readme
    assert architecture_rule in lifecycle
    assert "Future live experiments must pass" in readme
    assert "Future labs may experiment" in llm_model
    assert "Scaffold milestone-one fixture records are not real research evidence." in portfolio
    assert "one admitted tiny live LLM pilot export set" in portfolio
    assert "## Active federation labs" in portfolio
    assert "Milestone-one active labs" not in portfolio
    assert "generated synthesis metrics" not in portfolio.lower()
    assert "Current phase: `milestone-2-live-pilot-recorded`" in graduation
    assert "Current milestone: `scaffold-v0.1`" not in graduation
    assert "Current phase: `milestone-2-live-pilot-recorded`" in admission
    assert "Current milestone: scaffold-v0.1" not in admission
    assert "No graduated items." in graduation
    assert "## Current Non-Graduation Rule" in graduation
    assert "Nothing can graduate during scaffold milestone one." not in graduation
    assert "A proposal-only live pilot export set is not graduation evidence by itself." in (
        graduation
    )
    assert (
        "The Goal 3 live pilot planning packet does not affect graduation status."
        in graduation
    )
    assert "first Goal 5 proposal-only live pilot export set does not affect graduation status" in (
        graduation
    )
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


def test_currentness_authority_surface_does_not_creep():
    build_prompt = (ROOT / "docs" / "build-prompts" / "scaffold-milestone-one.md").read_text()
    lifecycle = (ROOT / "docs" / "research-lifecycle.md").read_text()

    assert not (ROOT / "MILESTONE_GUIDE.md").exists()
    assert "MILESTONE_GUIDE.md" not in build_prompt
    assert "Milestone 2" in lifecycle
    assert "Tiny Live LLM Pilot" in lifecycle


def test_agent_guides_encode_v3_operating_boundaries():
    root_agents = (ROOT / "AGENTS.md").read_text()
    protocol_agents = (ROOT / "packages" / "qf_v3_protocol" / "AGENTS.md").read_text()
    synthesis_agents = (ROOT / "packages" / "qf_v3_synthesis" / "AGENTS.md").read_text()
    labs_agents = (ROOT / "labs" / "AGENTS.md").read_text()
    benchmarks_agents = (ROOT / "benchmarks" / "AGENTS.md").read_text()
    docs_agents = (ROOT / "docs" / "AGENTS.md").read_text()

    architecture_rule = (
        "No new experiment becomes architecture.\n"
        "It becomes records first.\n"
        "Architecture changes only after repeated evidence and explicit ADR."
    )
    assert (
        "V3 is a federated LLM-methodology research portfolio for discovering how messy "
        "trader source material can become useful trading intelligence."
    ) in root_agents
    assert architecture_rule in root_agents
    assert (
        "Evidence records, benchmark results, evaluations, and graduation decisions" in root_agents
    )
    assert "V3 must not become an append-only repo." in root_agents
    for required in [
        "Before adding new files, check whether an existing file, schema, test, prompt, "
        "planning pattern, or fixture should be reused, edited, generalized, deleted, "
        "or archived.",
        "Do not create a new script, helper, doc, test, or protocol field merely "
        "because this is a new method.",
        "reuse existing protocol records",
        "adapt existing lab planning structure",
        "add only the minimum new files needed for the new lab's distinct method",
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
    assert "Nothing graduates during scaffold milestone one." in root_agents
    assert "Before finalizing work, check:" in root_agents
    assert "Before changing files, agents must read:" in root_agents
    assert "every `AGENTS.md` on the path to each file they will touch" in root_agents
    assert "Agent guides consulted:" in root_agents
    assert "Python is truth" not in root_agents

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
    assert "explicit comparative evaluation path" in synthesis_agents

    assert "Labs are playgrounds for methodological exploration." in labs_agents
    assert "Do not turn a lab method into shared architecture." in labs_agents
    assert (
        "Before adding files for a new lab method, reuse existing protocol records and "
        "adapt existing lab planning structure where possible."
        in labs_agents
    )
    for required in [
        "`LAB_CARD.md`",
        "`RESEARCH_QUESTION.md`",
        "method description",
        "run or export records",
        "evaluation notes",
        "negative-result notes",
    ]:
        assert required in labs_agents
    assert (
        "Do not create live LLM runs until the live LLM experiment admission checklist "
        "is satisfied."
        in labs_agents
    )

    assert "Benchmark packs are metadata-safe test harnesses." in benchmarks_agents
    assert "Every active benchmark pack must include `v2_lesson_refs`." in benchmarks_agents
    for required in [
        "what capability it tests",
        "what failure mode it preserves",
        "why it is metadata-safe",
        "what would make it stale",
        "what evaluation surface will consume it",
    ]:
        assert required in benchmarks_agents

    assert (
        "Docs should clarify current direction, not accumulate contradictory history."
        in docs_agents
    )
    assert "Generated synthesis summaries must not be copied into docs as authority." in docs_agents
    assert "Milestone-one constraints are phase-local." in docs_agents
    assert "Superseded by:" in docs_agents
    assert "Status: historical / archived / no longer current" in docs_agents
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
