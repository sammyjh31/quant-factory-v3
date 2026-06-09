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
GOAL7D_PILOT_DIR = (
    ROOT / "labs" / "chunked_source_grounding" / "PLANNING" / "live_llm_pilot_002"
)
GOAL8B_PILOT_DIR = (
    ROOT / "labs" / "chunked_source_grounding" / "PLANNING" / "live_llm_pilot_003"
)
GOAL9A_PILOT_DIR = (
    ROOT / "labs" / "chunked_source_grounding" / "PLANNING" / "live_llm_pilot_004"
)
GOAL10A_EVALUATOR_DIR = (
    ROOT / "labs" / "chunked_source_grounding" / "PLANNING" / "source_span_evaluator_001"
)
GOAL11A_LOCATOR_CONTRACT_DIR = (
    ROOT
    / "labs"
    / "chunked_source_grounding"
    / "PLANNING"
    / "source_span_locator_contract_001"
)
GOAL11B_PILOT_DIR = (
    ROOT / "labs" / "chunked_source_grounding" / "PLANNING" / "live_llm_pilot_005"
)
GOAL9A_SOURCE_PATH = (
    ROOT / "raw_corpora" / "selected" / "source_span_precision_repeat_001" / "source.txt"
)
GOAL7G_COMPARISON_NOTE = (
    ROOT
    / "labs"
    / "chunked_source_grounding"
    / "PLANNING"
    / "comparisons"
    / "live_pilot_method_comparison_001.md"
)
GOAL6_CONTENT_REVIEW_PLAN = GOAL3_PILOT_DIR / "content_review_plan.md"
GOAL3_METHOD_ID = "long_context_judgment_live_pilot_001_method"
GOAL3_EXPERIMENT_ID = "long_context_judgment_live_pilot_001"
GOAL7A_METHOD_ID = "chunked_source_grounding_live_pilot_001_method"
GOAL7A_EXPERIMENT_ID = "chunked_source_grounding_live_pilot_001"
GOAL7D_METHOD_ID = "chunked_source_grounding_live_pilot_002_method"
GOAL7D_EXPERIMENT_ID = "chunked_source_grounding_live_pilot_002"
GOAL8B_METHOD_ID = "chunked_source_grounding_live_pilot_003_method"
GOAL8B_EXPERIMENT_ID = "chunked_source_grounding_live_pilot_003"
GOAL9A_METHOD_ID = "chunked_source_grounding_live_pilot_004_method"
GOAL9A_EXPERIMENT_ID = "chunked_source_grounding_live_pilot_004"
GOAL11B_METHOD_ID = "chunked_source_grounding_live_pilot_005_method"
GOAL11B_EXPERIMENT_ID = "chunked_source_grounding_live_pilot_005"
CHUNKED_PRO_LIVE_PILOT_RUN_ID = "chunked_source_grounding_live_pilot_002_run"
CHUNKED_PRO_LIVE_PILOT_ARTIFACT_ID = (
    "chunked_source_grounding_live_pilot_002_artifact"
)
CHUNKED_PRO_LIVE_PILOT_EVALUATION_ID = "chunked_source_grounding_live_pilot_002_eval"
CHUNKED_PRO_LIVE_PILOT_CONTENT_REVIEW_EVALUATION_ID = (
    "chunked_source_grounding_live_pilot_002_manual_content_review"
)
CHUNKED_PRO_LIVE_PILOT_NOTE_ID = "chunked_source_grounding_live_pilot_002_note"
CHUNKED_SPAN_LIVE_PILOT_RUN_ID = "chunked_source_grounding_live_pilot_003_run"
CHUNKED_SPAN_LIVE_PILOT_ARTIFACT_ID = (
    "chunked_source_grounding_live_pilot_003_artifact"
)
CHUNKED_SPAN_LIVE_PILOT_EVALUATION_ID = "chunked_source_grounding_live_pilot_003_eval"
CHUNKED_SPAN_LIVE_PILOT_CONTENT_REVIEW_EVALUATION_ID = (
    "chunked_source_grounding_live_pilot_003_manual_content_review"
)
CHUNKED_SPAN_LIVE_PILOT_NOTE_ID = "chunked_source_grounding_live_pilot_003_note"
CHUNKED_SPAN_REPEAT_LIVE_PILOT_RUN_ID = (
    "chunked_source_grounding_live_pilot_004_run"
)
CHUNKED_SPAN_REPEAT_LIVE_PILOT_ARTIFACT_ID = (
    "chunked_source_grounding_live_pilot_004_artifact"
)
CHUNKED_SPAN_REPEAT_LIVE_PILOT_EVALUATION_ID = (
    "chunked_source_grounding_live_pilot_004_eval"
)
CHUNKED_SPAN_REPEAT_LIVE_PILOT_NOTE_ID = (
    "chunked_source_grounding_live_pilot_004_note"
)
CHUNKED_LOCATOR_LIVE_PILOT_RUN_ID = (
    "chunked_source_grounding_live_pilot_005_run"
)
CHUNKED_LOCATOR_LIVE_PILOT_ARTIFACT_ID = (
    "chunked_source_grounding_live_pilot_005_artifact"
)
CHUNKED_LOCATOR_LIVE_PILOT_EVALUATION_ID = (
    "chunked_source_grounding_live_pilot_005_eval"
)
CHUNKED_LOCATOR_LIVE_PILOT_NOTE_ID = (
    "chunked_source_grounding_live_pilot_005_note"
)
LIVE_PILOT_RUN_ID = "long_context_judgment_live_pilot_001_run"
LIVE_PILOT_ARTIFACT_ID = "long_context_judgment_live_pilot_001_artifact"
LIVE_PILOT_EVALUATION_ID = "long_context_judgment_live_pilot_001_eval"
LIVE_PILOT_CONTENT_REVIEW_EVALUATION_ID = (
    "long_context_judgment_live_pilot_001_manual_content_review"
)
LIVE_PILOT_NOTE_ID = "long_context_judgment_live_pilot_001_note"
LIVE_PILOT_SOURCE_REF_PREFIX = "raw_corpora_sha256:"
CHUNKED_LIVE_PILOT_RUN_ID = "chunked_source_grounding_live_pilot_001_run"
CHUNKED_LIVE_PILOT_ARTIFACT_ID = "chunked_source_grounding_live_pilot_001_artifact"
CHUNKED_LIVE_PILOT_EVALUATION_ID = "chunked_source_grounding_live_pilot_001_eval"
CHUNKED_LIVE_PILOT_CONTENT_REVIEW_EVALUATION_ID = (
    "chunked_source_grounding_live_pilot_001_manual_content_review"
)
CHUNKED_LIVE_PILOT_NOTE_ID = "chunked_source_grounding_live_pilot_001_note"
CHUNKED_SPAN_REPEAT_LIVE_PILOT_CONTENT_REVIEW_EVALUATION_ID = (
    "chunked_source_grounding_live_pilot_004_manual_content_review"
)
CHUNKED_SPAN_STRICT_REVIEW_003_EVALUATION_ID = (
    "chunked_source_grounding_live_pilot_003_strict_span_review"
)
CHUNKED_SPAN_STRICT_REVIEW_004_EVALUATION_ID = (
    "chunked_source_grounding_live_pilot_004_strict_span_review"
)
CHUNKED_LOCATOR_STRICT_REVIEW_005_EVALUATION_ID = (
    "chunked_source_grounding_live_pilot_005_strict_locator_review"
)
CHUNKED_SPAN_STRICT_REVIEW_003_EXPORT = (
    "evaluation_record.live_pilot_003_strict_span_review.json"
)
CHUNKED_SPAN_STRICT_REVIEW_004_EXPORT = (
    "evaluation_record.live_pilot_004_strict_span_review.json"
)
CHUNKED_LOCATOR_STRICT_REVIEW_005_EXPORT = (
    "evaluation_record.live_pilot_005_strict_locator_review.json"
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

CURRENT_PHASE = "milestone-3-method-comparison-recorded"
CURRENT_NEXT_STEP = "Goal 12A planning for a line-range-first locator contract"
ROUTER_LEDGER_PATTERNS = (
    r"labs/[^\s`]+/EXPORTS/(?:run_record|artifact_envelope|evaluation_record|research_note)"
    r"\.live_pilot_\d+\.json",
    r"evaluation_record\.live_pilot_\d+_manual_content_review\.json",
    r"manual content review (?:failed|passed) for pilot \d+",
    r"chunked_source_grounding_live_pilot_00[1-5]",
)


def assert_currentness_router_not_ledger(text: str):
    assert "generated synthesis metrics" not in text.lower()
    assert "provider_payload" not in text
    assert "raw_source_text" not in text
    assert "raw_model_output" not in text
    for pattern in ROUTER_LEDGER_PATTERNS:
        assert not re.search(pattern, text), pattern


def live_pilot_export_names(pilot_number: str) -> set[str]:
    return {
        f"run_record.live_pilot_{pilot_number}.json",
        f"artifact_envelope.live_pilot_{pilot_number}.json",
        f"evaluation_record.live_pilot_{pilot_number}.json",
        f"research_note.live_pilot_{pilot_number}.json",
    }


def manual_content_review_export_name(pilot_number: str) -> str:
    return f"evaluation_record.live_pilot_{pilot_number}_manual_content_review.json"


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
        live_pilot_export_names("001")
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
        load_json(GOAL3_PILOT_DIR / "method_card.proposed.json")["method_card"]["method_id"],
        load_json(GOAL7A_PILOT_DIR / "method_card.proposed.json")["method_card"][
            "method_id"
        ],
        load_json(GOAL7D_PILOT_DIR / "method_card.proposed.json")["method_card"][
            "method_id"
        ],
        load_json(GOAL8B_PILOT_DIR / "method_card.proposed.json")["method_card"][
            "method_id"
        ],
        load_json(GOAL9A_PILOT_DIR / "method_card.proposed.json")["method_card"][
            "method_id"
        ],
        load_json(GOAL11B_PILOT_DIR / "method_card.proposed.json")["method_card"][
            "method_id"
        ],
    }
    experiment_ids = {
        record["experiment_card"]["experiment_id"] for record in records_by_schema("ExperimentCard")
    }
    planning_experiment_ids = {
        load_json(GOAL3_PILOT_DIR / "experiment_card.proposed.json")["experiment_card"][
            "experiment_id"
        ],
        load_json(GOAL7A_PILOT_DIR / "experiment_card.proposed.json")["experiment_card"][
            "experiment_id"
        ],
        load_json(GOAL7D_PILOT_DIR / "experiment_card.proposed.json")[
            "experiment_card"
        ]["experiment_id"],
        load_json(GOAL8B_PILOT_DIR / "experiment_card.proposed.json")[
            "experiment_card"
        ]["experiment_id"],
        load_json(GOAL9A_PILOT_DIR / "experiment_card.proposed.json")[
            "experiment_card"
        ]["experiment_id"],
        load_json(GOAL11B_PILOT_DIR / "experiment_card.proposed.json")[
            "experiment_card"
        ]["experiment_id"],
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
        if note["note_id"] in {
            LIVE_PILOT_NOTE_ID,
            CHUNKED_LIVE_PILOT_NOTE_ID,
            CHUNKED_PRO_LIVE_PILOT_NOTE_ID,
            CHUNKED_SPAN_LIVE_PILOT_NOTE_ID,
            CHUNKED_SPAN_REPEAT_LIVE_PILOT_NOTE_ID,
            CHUNKED_LOCATOR_LIVE_PILOT_NOTE_ID,
        }:
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
    assert "long_context_judgment" in portfolio
    assert "long_context_judgment" in lab_registry
    assert "proposal-only" in portfolio
    assert "proposal-only" in lab_registry


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

    for expected_export in live_pilot_export_names("001"):
        assert f"labs/long_context_judgment/EXPORTS/{expected_export}" in update

    summary = synthesize_exports(root=ROOT)
    assert summary["record_count"] == sum(1 for _ in all_lab_export_records())
    assert GOAL3_METHOD_ID in summary["methods"]
    assert summary["outcome_polarities"] == [
        "negative_fixture",
        "positive_fixture",
        "proposal_only",
    ]
    assert summary["statuses"] == ["fixture_recorded", "live_recorded"]

    graduation = (ROOT / "GRADUATION_LEDGER.md").read_text()
    assert "No graduated items." in graduation
    assert "proposal-only live export sets, manual reviews, comparison notes" in (
        graduation
    )

    readme = (ROOT / "README.md").read_text()
    portfolio = (ROOT / "PORTFOLIO_CURRENT.md").read_text()
    lab_registry = (ROOT / "LAB_REGISTRY.md").read_text()
    for currentness_doc in [readme, lab_registry]:
        assert "proposal-only" in currentness_doc
        assert "no live LLM call has been made" not in currentness_doc.lower()
        assert "No live LLM experiment has run." not in currentness_doc
    assert "run_admission_update.md" not in portfolio
    assert "no live LLM call has been made" not in portfolio.lower()
    assert "No live LLM experiment has run." not in portfolio
    assert "one tiny method-comparison loop on `text_judgment_v0`" in portfolio


def test_goal5_live_pilot_export_set_is_protocol_valid_and_bounded():
    export_dir = ROOT / "labs" / "long_context_judgment" / "EXPORTS"
    live_exports = {path.name: load_json(path) for path in export_dir.glob("*.live_pilot_001.json")}
    assert set(live_exports) == live_pilot_export_names("001")
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
            for name in sorted(live_pilot_export_names("001"))
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

    assert live_export_names == live_pilot_export_names("001")
    assert (export_dir / manual_content_review_export_name("001")).exists()
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
    content_review_path = export_dir / manual_content_review_export_name("001")
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
    assert LIVE_PILOT_CONTENT_REVIEW_EVALUATION_ID in [
        review["evaluation_id"] for review in manual_content_reviews
    ]
    assert not list(export_dir.glob("run_record.*manual_content_review*.json"))
    assert not list(export_dir.glob("artifact_envelope.*manual_content_review*.json"))
    assert not list(export_dir.glob("research_note.*manual_content_review*.json"))

    portfolio = (ROOT / "PORTFOLIO_CURRENT.md").read_text()
    lab_registry = (ROOT / "LAB_REGISTRY.md").read_text()
    assert "manual reviews" in portfolio
    assert "manual review records" in lab_registry
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
    assert summary["record_count"] == sum(1 for _ in all_lab_export_records())

    readme = (ROOT / "README.md").read_text()
    portfolio = (ROOT / "PORTFOLIO_CURRENT.md").read_text()
    lab_registry = (ROOT / "LAB_REGISTRY.md").read_text()
    for currentness_doc in [readme, portfolio, lab_registry]:
        assert "chunked_source_grounding" in currentness_doc
        assert "proposal-only" in currentness_doc
        assert "generated synthesis metrics" not in currentness_doc.lower()
    assert "No graduated items." in (ROOT / "GRADUATION_LEDGER.md").read_text()


def test_goal7b_chunked_source_grounding_live_export_set_is_protocol_valid_and_bounded():
    export_dir = ROOT / "labs" / "chunked_source_grounding" / "EXPORTS"
    live_exports = {path.name: load_json(path) for path in export_dir.glob("*.live_pilot_001.json")}
    assert set(live_exports) == live_pilot_export_names("001")
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
        "run_id": CHUNKED_LIVE_PILOT_RUN_ID,
        "lab_id": "chunked_source_grounding",
        "experiment_id": GOAL7A_EXPERIMENT_ID,
        "method_id": GOAL7A_METHOD_ID,
        "benchmark_pack_id": "text_judgment_v0",
        "source_refs": ["raw_corpora_sha256:d8392c58c3b740eb"],
        "artifact_ids": [CHUNKED_LIVE_PILOT_ARTIFACT_ID],
        "evaluation_ids": [CHUNKED_LIVE_PILOT_EVALUATION_ID],
        "run_kind": "live_llm_pilot",
        "outcome_polarity": "proposal_only",
        "status": "live_recorded",
    }

    artifact_payload = artifact["artifact"]["payload"]
    assert artifact["artifact"]["artifact_id"] == CHUNKED_LIVE_PILOT_ARTIFACT_ID
    assert artifact["artifact"]["artifact_type"] == "chunked_source_grounding_proposal"
    assert artifact["artifact"]["lab_id"] == "chunked_source_grounding"
    assert artifact["artifact"]["method_id"] == GOAL7A_METHOD_ID
    assert artifact["artifact"]["run_id"] == CHUNKED_LIVE_PILOT_RUN_ID
    assert artifact["artifact"]["source_refs"] == run_record["source_refs"]
    assert artifact["artifact"]["posture"] == {
        "grounding_status": "source_linked",
        "review_status": "self_checked",
        "readiness_status": "study_candidate",
        "validation_status": "none",
        "lifecycle_status": "active",
    }
    assert "proposal_only_not_evaluated" in artifact["artifact"]["blockers"]
    assert "content_review_not_yet_completed" in artifact["artifact"]["blockers"]
    assert artifact_payload["outcome_polarity"] == "proposal_only"
    assert artifact_payload["proposal_only"] is True
    assert artifact_payload["provider_id"] == "deepseek_api"
    assert artifact_payload["base_url"] == "https://api.deepseek.com"
    assert artifact_payload["model_id"] == "deepseek-v4-flash"
    assert artifact_payload["requested_model_id"] == "deepseek-v4-flash"
    assert artifact_payload["thinking"] == {"type": "disabled"}
    assert artifact_payload["stream"] is False
    assert artifact_payload["prompt_template_sha256"] == sha256_file(
        GOAL7A_PILOT_DIR / "prompt_template.live_pilot_001.md"
    )
    assert artifact_payload["config_sha256"] == CONFIG_SHA256
    assert artifact_payload["source_metadata"] == {
        "source_ref": "raw_corpora_sha256:d8392c58c3b740eb",
        "source_scope": (
            "same operator-approved ignored local trader education transcript excerpt "
            "used by long_context_judgment_live_pilot_001"
        ),
        "source_path_scope": (
            "raw_corpora/trader_source_corpus/transcripts/"
            "how-to-use-market-profile-start-now-trading-tutorials.txt"
        ),
        "source_file_sha256": (
            "dca704a5010abf9b56498a325702c895fd6ab2ae7815b26021b20f8f89dcdd95"
        ),
        "source_file_word_count": 8849,
        "excerpt_sha256": (
            "d8392c58c3b740eb87efd9488fd72da35ef3d09f6a4ee766a9816f672d9b03ee"
        ),
        "excerpt_word_count": 650,
        "raw_source_text_committed": False,
    }
    assert artifact_payload["cost_metadata"]["budget_cap_usd"] == 3.0
    assert artifact_payload["cost_metadata"]["estimated_cost_usd"] <= 3.0
    assert artifact_payload["raw_source_text_committed"] is False
    assert artifact_payload["raw_provider_payload_committed"] is False
    assert artifact_payload["raw_prompt_trace_committed"] is False
    assert artifact_payload["raw_model_trace_committed"] is False
    assert artifact_payload["secrets_committed"] is False
    assert "raw_source_text" not in artifact_payload
    assert "provider_payload" not in artifact_payload
    assert "api_key" not in json.dumps(artifact_payload).lower()

    model_output_metadata = artifact_payload["model_output_metadata"]
    assert model_output_metadata["parsed_json_success"] is False
    assert model_output_metadata["finish_reason"] == "length"
    assert model_output_metadata["model_output_truncated"] is True
    assert set(model_output_metadata["expected_top_level_keys_detected"]) == {
        "source_linked_claim_table",
        "segment_span_support_notes",
        "unsupported_claim_report",
        "judgment_abstraction_notes",
        "method_failure_notes",
    }
    assert "did not parse as complete JSON" in model_output_metadata["sanitized_output_summary"]

    assert evaluation["evaluation"]["evaluation_id"] == CHUNKED_LIVE_PILOT_EVALUATION_ID
    assert evaluation["evaluation"]["target_id"] == CHUNKED_LIVE_PILOT_ARTIFACT_ID
    assert evaluation["evaluation"]["evaluator_type"] == "manual_boundary_review"
    assert evaluation["evaluation"]["pass_fail"] == "pass"
    assert "method quality was not evaluated" in evaluation["evaluation"]["comments"]

    research_note = note["research_note"]
    assert research_note["note_id"] == CHUNKED_LIVE_PILOT_NOTE_ID
    assert research_note["experiment_ids"] == [GOAL7A_EXPERIMENT_ID]
    assert research_note["benchmark_pack_ids"] == ["text_judgment_v0"]
    assert research_note["evidence_disclaimer"] == LIVE_EVIDENCE_DISCLAIMER
    assert any("No method success is claimed" in item for item in research_note["what_failed"])
    assert any(
        "long_context_judgment_live_pilot_001" in item
        for item in research_note["reusable_by_other_labs"]
    )

    combined_committed = "\n".join(
        path.read_text()
        for path in [
            export_dir / name
            for name in sorted(live_pilot_export_names("001"))
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

    portfolio = (ROOT / "PORTFOLIO_CURRENT.md").read_text()
    lab_registry = (ROOT / "LAB_REGISTRY.md").read_text()
    readme = (ROOT / "README.md").read_text()
    for currentness_doc in [portfolio, lab_registry, readme]:
        assert "proposal-only" in currentness_doc
        assert "generated synthesis metrics" not in currentness_doc.lower()
    assert "No graduated items." in (ROOT / "GRADUATION_LEDGER.md").read_text()


def test_goal7c_chunked_flash_manual_content_review_records_truncated_failure_only():
    export_dir = ROOT / "labs" / "chunked_source_grounding" / "EXPORTS"
    content_review_path = export_dir / manual_content_review_export_name("001")
    assert content_review_path.exists()

    record = load_json(content_review_path)
    validate_record(record)
    assert record["schema_name"] == "EvaluationRecord"
    assert record["schema_version"] == CURRENT_SCHEMA_VERSION

    evaluation = record["evaluation"]
    assert evaluation["evaluation_id"] == CHUNKED_LIVE_PILOT_CONTENT_REVIEW_EVALUATION_ID
    assert evaluation["lab_id"] == "chunked_source_grounding"
    assert evaluation["target_id"] == CHUNKED_LIVE_PILOT_ARTIFACT_ID
    assert evaluation["target_type"] == "artifact"
    assert evaluation["evaluator_id"] == "manual_content_review_live_pilot_001"
    assert evaluation["evaluator_type"] == "manual_content_review"
    assert evaluation["benchmark_pack_id"] == "text_judgment_v0"
    assert evaluation["score"] == pytest.approx(0.2)
    assert evaluation["pass_fail"] == "fail"
    assert evaluation["failure_tags"] == [
        "model_output_truncated",
        "incomplete_json",
        "output_contract_too_large",
        "content_review_blocked",
    ]

    comments = evaluation["comments"]
    for required in [
        "Manual content review only",
        "content-reviewable",
        "truncation blocks source-grounding review",
        "prompt/output contract asked for too much",
        "partial output is usable only as failure evidence",
        "not a global judgment on chunked/source-grounded reading",
        (
            "not validation, product evidence, strategy evidence, financial advice, "
            "live-trading authority, graduation, or architecture"
        ),
    ]:
        assert required in comments
    assert "raw source text and raw model output are not committed" in comments.lower()

    manual_content_reviews = [
        record["evaluation"]
        for record in records_by_schema("EvaluationRecord")
        if record["evaluation"]["evaluator_type"] == "manual_content_review"
    ]
    assert sorted(review["evaluation_id"] for review in manual_content_reviews) == [
        CHUNKED_LIVE_PILOT_CONTENT_REVIEW_EVALUATION_ID,
        CHUNKED_PRO_LIVE_PILOT_CONTENT_REVIEW_EVALUATION_ID,
        CHUNKED_SPAN_LIVE_PILOT_CONTENT_REVIEW_EVALUATION_ID,
        CHUNKED_SPAN_STRICT_REVIEW_003_EVALUATION_ID,
        CHUNKED_SPAN_REPEAT_LIVE_PILOT_CONTENT_REVIEW_EVALUATION_ID,
        CHUNKED_SPAN_STRICT_REVIEW_004_EVALUATION_ID,
        CHUNKED_LOCATOR_STRICT_REVIEW_005_EVALUATION_ID,
        LIVE_PILOT_CONTENT_REVIEW_EVALUATION_ID,
    ]
    assert not list(export_dir.glob("run_record.*manual_content_review*.json"))
    assert not list(export_dir.glob("artifact_envelope.*manual_content_review*.json"))
    assert not list(export_dir.glob("research_note.*manual_content_review*.json"))

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

    portfolio = (ROOT / "PORTFOLIO_CURRENT.md").read_text()
    lab_registry = (ROOT / "LAB_REGISTRY.md").read_text()
    assert "bounded negative" in portfolio
    assert "chunked_source_grounding" in lab_registry
    assert "generated synthesis metrics" not in portfolio.lower()
    assert "No graduated items." in (ROOT / "GRADUATION_LEDGER.md").read_text()


def test_goal7d_deepseek_v4_pro_rerun_planning_packet_is_contained_and_narrower():
    required_files = {
        "admission.md",
        "method_card.proposed.json",
        "experiment_card.proposed.json",
        "evaluator_plan.md",
        "source_privacy_boundary.md",
        "prompt_template.live_pilot_002.md",
        "run_admission_update.md",
        "stop_condition.md",
    }
    assert GOAL7D_PILOT_DIR.exists()
    assert {path.name for path in GOAL7D_PILOT_DIR.iterdir() if path.is_file()} == (
        required_files
    )

    method_card = load_json(GOAL7D_PILOT_DIR / "method_card.proposed.json")
    experiment_card = load_json(GOAL7D_PILOT_DIR / "experiment_card.proposed.json")
    validate_record(method_card)
    validate_record(experiment_card)

    assert method_card["schema_name"] == "MethodCard"
    assert method_card["schema_version"] == CURRENT_SCHEMA_VERSION
    method = method_card["method_card"]
    assert method["method_id"] == GOAL7D_METHOD_ID
    assert method["lab_id"] == "chunked_source_grounding"
    assert method["method_family"] == "chunked_source_grounded_llm_reader_proposed"
    assert "chunked_source_grounding_proposal" in method["intended_outputs"]
    assert "source-linked claim table" in method["intended_outputs"]
    assert "unsupported-claim report" in method["intended_outputs"]
    assert "brief method-failure notes" in method["intended_outputs"]
    assert "judgment abstraction notes" not in method["intended_outputs"]
    assert "Flash pilot 001 failed structurally" in " ".join(method["known_risks"])
    assert "not a completed run" in method["non_goals"]
    assert "not architecture or graduation evidence" in method["non_goals"]

    assert experiment_card["schema_name"] == "ExperimentCard"
    assert experiment_card["schema_version"] == CURRENT_SCHEMA_VERSION
    experiment = experiment_card["experiment_card"]
    assert experiment["experiment_id"] == GOAL7D_EXPERIMENT_ID
    assert experiment["lab_id"] == "chunked_source_grounding"
    assert experiment["benchmark_pack_ids"] == ["text_judgment_v0"]
    assert experiment["method_ids"] == [GOAL7D_METHOD_ID]
    assert experiment["expected_artifact_types"] == ["chunked_source_grounding_proposal"]
    assert "DeepSeek V4 Pro" in experiment["research_question"]
    assert "smaller output contract" in experiment["research_question"]
    assert "same source excerpt" in experiment["hypothesis"]
    assert "output_contract_too_large" in experiment["hypothesis"]
    assert "long_context_judgment_live_pilot_001" in experiment["evaluation_plan"]
    assert "chunked_source_grounding_live_pilot_001" in experiment["evaluation_plan"]

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
    assert "EXPORTS" not in GOAL7D_PILOT_DIR.parts
    assert all("PLANNING" not in path.parts for path in lab_export_paths(ROOT))

    admission = (GOAL7D_PILOT_DIR / "admission.md").read_text()
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
        "This is planning/admission only. No LLM call has been made.",
        "Do not add around stale structure. Rework, replace, delete, or archive it.",
        "does not replace the Flash pilot 001 record",
        "Flash pilot 001 produced a bounded negative result",
        "No RunRecord, ArtifactEnvelope, EvaluationRecord, or ResearchNote exists for this pilot.",
        "Do not request broad judgment abstraction notes in the same call.",
        "Do not request full comparison commentary in the same call.",
    ]:
        assert required_guardrail in admission

    evaluator_plan = (GOAL7D_PILOT_DIR / "evaluator_plan.md").read_text()
    for required in [
        "schema_check",
        "manual_boundary_review",
        "manual_content_review",
        "source grounding",
        "hallucination / unsupported claims",
        "negative-result value",
        "comparison value against `long_context_judgment_live_pilot_001`",
        "comparison value against `chunked_source_grounding_live_pilot_001`",
    ]:
        assert required in evaluator_plan

    source_boundary = (GOAL7D_PILOT_DIR / "source_privacy_boundary.md").read_text()
    for required in [
        "raw_corpora_sha256:d8392c58c3b740eb",
        "raw_corpora/selected/live_llm_pilot_001/source.txt",
        "raw_corpora/trader_source_corpus/transcripts/how-to-use-market-profile-start-now-trading-tutorials.txt",
        "Do not commit raw source text.",
        "same approved excerpt as `long_context_judgment_live_pilot_001`",
        "same approved excerpt/hash as `chunked_source_grounding_live_pilot_001`",
    ]:
        assert required in source_boundary

    update = (GOAL7D_PILOT_DIR / "run_admission_update.md").read_text()
    prompt_template_path = GOAL7D_PILOT_DIR / "prompt_template.live_pilot_002.md"
    prompt_template = prompt_template_path.read_text()
    for required in [
        (
            "This admission update defines the executable preflight scope for exactly "
            "one future tiny live LLM pilot run."
        ),
        (
            "It does not by itself authorize execution. Execution requires a separate "
            "Goal 7E instruction."
        ),
        "Provider: DeepSeek API",
        "API format: OpenAI-compatible chat completions",
        "Base URL: `https://api.deepseek.com`",
        "Model: `deepseek-v4-pro`",
        "Reasoning/thinking mode: non-thinking",
        "Benchmark pack: `text_judgment_v0`",
        "Lab: `labs/chunked_source_grounding`",
        "Budget cap: `$3` hard maximum.",
        "No retries unless the call fails before producing output.",
        "Do not silently substitute `deepseek-v4-flash`, `deepseek-chat`, "
        "`deepseek-reasoner`, or any other model.",
        "Outputs from this experiment are proposals until evaluated.",
        "No private/raw source material or provider payloads are committed.",
        "The output contract is narrower than `live_llm_pilot_001`.",
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
    assert "source_linked_claim_table" in prompt_template
    assert "segment_span_support_notes" in prompt_template
    assert "unsupported_claim_report" in prompt_template
    assert "brief_method_failure_notes" in prompt_template
    assert "judgment_abstraction_notes" not in prompt_template
    assert "full comparison commentary" not in prompt_template

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
        "model_id": "deepseek-v4-pro",
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

    stop_condition = (GOAL7D_PILOT_DIR / "stop_condition.md").read_text()
    assert "`deepseek-v4-pro` is unavailable" in stop_condition
    assert (
        "any unapproved model, prompt, source, evaluator, tool, retry, protocol, or "
        "architecture substitution"
    ) in stop_condition

    combined = "\n".join(path.read_text() for path in GOAL7D_PILOT_DIR.iterdir())
    for forbidden in [
        "BEGIN RAW SOURCE",
        "DEEPSEEK_API_KEY=",
        "sk-",
        "\"api_key\"",
        "\"provider_payload\"",
    ]:
        assert forbidden not in combined

    summary = synthesize_exports(root=ROOT)
    assert summary["record_count"] == sum(1 for _ in all_lab_export_records())

    readme = (ROOT / "README.md").read_text()
    portfolio = (ROOT / "PORTFOLIO_CURRENT.md").read_text()
    lab_registry = (ROOT / "LAB_REGISTRY.md").read_text()
    for currentness_doc in [readme, lab_registry]:
        assert "chunked_source_grounding" in currentness_doc
        assert "generated synthesis metrics" not in currentness_doc.lower()
    assert "live_llm_pilot_002" not in portfolio
    assert "generated synthesis metrics" not in portfolio.lower()
    assert "No graduated items." in (ROOT / "GRADUATION_LEDGER.md").read_text()


def test_goal7e_deepseek_v4_pro_live_export_set_is_protocol_valid_and_bounded():
    export_dir = ROOT / "labs" / "chunked_source_grounding" / "EXPORTS"
    live_exports = {path.name: load_json(path) for path in export_dir.glob("*.live_pilot_002.json")}
    assert set(live_exports) == live_pilot_export_names("002")
    for record in live_exports.values():
        validate_record(record)

    run = live_exports["run_record.live_pilot_002.json"]
    artifact = live_exports["artifact_envelope.live_pilot_002.json"]
    evaluation = live_exports["evaluation_record.live_pilot_002.json"]
    note = live_exports["research_note.live_pilot_002.json"]

    assert run["schema_name"] == "RunRecord"
    assert run["schema_version"] == CURRENT_SCHEMA_VERSION
    run_record = run["run_record"]
    assert run_record == {
        "run_id": CHUNKED_PRO_LIVE_PILOT_RUN_ID,
        "lab_id": "chunked_source_grounding",
        "experiment_id": GOAL7D_EXPERIMENT_ID,
        "method_id": GOAL7D_METHOD_ID,
        "benchmark_pack_id": "text_judgment_v0",
        "source_refs": ["raw_corpora_sha256:d8392c58c3b740eb"],
        "artifact_ids": [CHUNKED_PRO_LIVE_PILOT_ARTIFACT_ID],
        "evaluation_ids": [CHUNKED_PRO_LIVE_PILOT_EVALUATION_ID],
        "run_kind": "live_llm_pilot",
        "outcome_polarity": "proposal_only",
        "status": "live_recorded",
    }

    artifact_payload = artifact["artifact"]["payload"]
    assert artifact["artifact"]["artifact_id"] == CHUNKED_PRO_LIVE_PILOT_ARTIFACT_ID
    assert artifact["artifact"]["artifact_type"] == "chunked_source_grounding_proposal"
    assert artifact["artifact"]["lab_id"] == "chunked_source_grounding"
    assert artifact["artifact"]["method_id"] == GOAL7D_METHOD_ID
    assert artifact["artifact"]["run_id"] == CHUNKED_PRO_LIVE_PILOT_RUN_ID
    assert artifact["artifact"]["source_refs"] == run_record["source_refs"]
    assert artifact["artifact"]["posture"]["grounding_status"] == "source_linked"
    assert artifact["artifact"]["posture"]["review_status"] == "self_checked"
    assert artifact["artifact"]["posture"]["validation_status"] == "none"
    assert "proposal_only_not_evaluated" in artifact["artifact"]["blockers"]
    assert "content_review_not_yet_completed" in artifact["artifact"]["blockers"]

    assert artifact_payload["outcome_polarity"] == "proposal_only"
    assert artifact_payload["proposal_only"] is True
    assert artifact_payload["provider_id"] == "deepseek_api"
    assert artifact_payload["api_format"] == "openai_compatible_chat_completions"
    assert artifact_payload["base_url"] == "https://api.deepseek.com"
    assert artifact_payload["model_id"] == "deepseek-v4-pro"
    assert artifact_payload["requested_model_id"] == "deepseek-v4-pro"
    assert artifact_payload["thinking"] == {"type": "disabled"}
    assert artifact_payload["stream"] is False
    assert artifact_payload["tool_routing"] == "none"
    assert artifact_payload["prompt_template_path"] == (
        "labs/chunked_source_grounding/PLANNING/live_llm_pilot_002/"
        "prompt_template.live_pilot_002.md"
    )
    assert artifact_payload["prompt_template_sha256"] == sha256_file(
        GOAL7D_PILOT_DIR / "prompt_template.live_pilot_002.md"
    )
    assert artifact_payload["config_sha256"] == canonical_json_hash(
        extract_json_block(
            (GOAL7D_PILOT_DIR / "run_admission_update.md").read_text(),
            "Canonical Model Config",
        )
    )
    assert artifact_payload["source_metadata"]["source_ref"] == (
        "raw_corpora_sha256:d8392c58c3b740eb"
    )
    assert artifact_payload["source_metadata"]["excerpt_sha256"] == (
        "d8392c58c3b740eb87efd9488fd72da35ef3d09f6a4ee766a9816f672d9b03ee"
    )
    assert artifact_payload["source_metadata"]["excerpt_word_count"] == 650
    assert artifact_payload["source_metadata"]["raw_source_text_committed"] is False
    assert artifact_payload["source_metadata"]["source_path_scope"] in {
        "raw_corpora/selected/live_llm_pilot_001/source.txt",
        (
            "raw_corpora/trader_source_corpus/transcripts/"
            "how-to-use-market-profile-start-now-trading-tutorials.txt"
        ),
    }

    assert artifact_payload["token_metadata"]["prompt_tokens"] > 0
    assert artifact_payload["token_metadata"]["completion_tokens"] > 0
    assert artifact_payload["token_metadata"]["total_tokens"] == (
        artifact_payload["token_metadata"]["prompt_tokens"]
        + artifact_payload["token_metadata"]["completion_tokens"]
    )
    assert artifact_payload["cost_metadata"]["budget_cap_usd"] == 3.0
    assert artifact_payload["cost_metadata"]["estimated_cost_usd"] <= 3.0
    assert "billing authority" in artifact_payload["cost_metadata"]["pricing_basis"]

    output_metadata = artifact_payload["model_output_metadata"]
    assert len(output_metadata["raw_model_output_sha256"]) == 64
    assert len(output_metadata["raw_response_sha256"]) == 64
    assert output_metadata["finish_reason"] in {"stop", "length"}
    assert output_metadata["model_output_truncated"] is (
        output_metadata["finish_reason"] == "length"
    )
    assert set(output_metadata["expected_top_level_keys"]) == {
        "source_linked_claim_table",
        "segment_span_support_notes",
        "unsupported_claim_report",
        "brief_method_failure_notes",
    }
    assert set(output_metadata["expected_top_level_keys_detected"]).issubset(
        set(output_metadata["expected_top_level_keys"])
    )
    if output_metadata["parsed_json_success"]:
        assert set(output_metadata["expected_top_level_keys_detected"]) == set(
            output_metadata["expected_top_level_keys"]
        )
        assert output_metadata["missing_expected_top_level_keys"] == []
    else:
        assert output_metadata["missing_expected_top_level_keys"] or output_metadata[
            "model_output_truncated"
        ]

    trace_boundary = artifact_payload["trace_storage_boundary"]
    assert trace_boundary == {
        "provider_request_trace": (
            "provider_payloads/chunked_source_grounding_live_pilot_002/request.json"
        ),
        "provider_response_trace": (
            "provider_payloads/chunked_source_grounding_live_pilot_002/response.json"
        ),
        "prompt_trace": "prompt_traces/chunked_source_grounding_live_pilot_002/prompt.txt",
        "model_output_trace": (
            "model_traces/chunked_source_grounding_live_pilot_002/model_output.txt"
        ),
        "traces_committed": False,
    }
    assert artifact_payload["raw_source_text_committed"] is False
    assert artifact_payload["raw_provider_payload_committed"] is False
    assert artifact_payload["raw_prompt_trace_committed"] is False
    assert artifact_payload["raw_model_trace_committed"] is False
    assert artifact_payload["secrets_committed"] is False

    assert evaluation["evaluation"]["evaluation_id"] == CHUNKED_PRO_LIVE_PILOT_EVALUATION_ID
    assert evaluation["evaluation"]["target_id"] == CHUNKED_PRO_LIVE_PILOT_ARTIFACT_ID
    assert evaluation["evaluation"]["evaluator_type"] == "manual_boundary_review"
    assert evaluation["evaluation"]["pass_fail"] == "pass"
    assert "method quality was not evaluated" in evaluation["evaluation"]["comments"]

    research_note = note["research_note"]
    assert research_note["note_id"] == CHUNKED_PRO_LIVE_PILOT_NOTE_ID
    assert research_note["experiment_ids"] == [GOAL7D_EXPERIMENT_ID]
    assert research_note["benchmark_pack_ids"] == ["text_judgment_v0"]
    assert research_note["evidence_disclaimer"] == LIVE_EVIDENCE_DISCLAIMER
    assert any("DeepSeek V4 Pro" in item for item in research_note["what_worked"])
    assert any(
        "chunked_source_grounding_live_pilot_001" in item
        for item in research_note["reusable_by_other_labs"]
    )

    combined_committed = "\n".join(
        path.read_text()
        for path in [
            export_dir / name
            for name in sorted(live_pilot_export_names("002"))
        ]
    )
    for forbidden in [
        "BEGIN RAW SOURCE",
        "DEEPSEEK_API_KEY",
        "sk-",
        "\"api_key\"",
        "\"provider_payload\"",
        "{{APPROVED_SOURCE_TEXT}}",
    ]:
        assert forbidden not in combined_committed

    portfolio = (ROOT / "PORTFOLIO_CURRENT.md").read_text()
    lab_registry = (ROOT / "LAB_REGISTRY.md").read_text()
    readme = (ROOT / "README.md").read_text()
    for currentness_doc in [portfolio, lab_registry, readme]:
        assert "chunked_source_grounding" in currentness_doc
        assert "generated synthesis metrics" not in currentness_doc.lower()
    assert "No graduated items." in (ROOT / "GRADUATION_LEDGER.md").read_text()


def test_goal7f_chunked_pro_manual_content_review_records_grounding_result_only():
    export_dir = ROOT / "labs" / "chunked_source_grounding" / "EXPORTS"
    content_review_path = export_dir / manual_content_review_export_name("002")
    assert content_review_path.exists()

    record = load_json(content_review_path)
    validate_record(record)
    assert record["schema_name"] == "EvaluationRecord"
    assert record["schema_version"] == CURRENT_SCHEMA_VERSION

    evaluation = record["evaluation"]
    assert evaluation["evaluation_id"] == CHUNKED_PRO_LIVE_PILOT_CONTENT_REVIEW_EVALUATION_ID
    assert evaluation["lab_id"] == "chunked_source_grounding"
    assert evaluation["target_id"] == CHUNKED_PRO_LIVE_PILOT_ARTIFACT_ID
    assert evaluation["target_type"] == "artifact"
    assert evaluation["evaluator_id"] == "manual_content_review_live_pilot_002"
    assert evaluation["evaluator_type"] == "manual_content_review"
    assert evaluation["benchmark_pack_id"] == "text_judgment_v0"
    assert evaluation["score"] == pytest.approx(0.82)
    assert evaluation["pass_fail"] == "pass"
    assert evaluation["failure_tags"] == [
        "missing_context",
        "broad_segment_refs",
        "limited_abstraction",
    ]

    comments = evaluation["comments"]
    for required in [
        "Manual content review only",
        "source grounding",
        "research usefulness",
        "hallucination / unsupported claims",
        "abstraction quality",
        "negative-result value",
        "comparison value against long_context_judgment_live_pilot_001",
        "comparison value against chunked_source_grounding_live_pilot_001",
        "content-reviewable",
        "complete parseable JSON",
        "source-linked claims match the approved excerpt",
        "failure note correctly identifies the excerpt boundary",
        "segment refs are broad labels rather than canonical offsets",
        "narrowed contract intentionally gives limited broader judgment abstraction",
        (
            "not validation, product evidence, strategy evidence, financial advice, "
            "live-trading authority, graduation, or architecture"
        ),
    ]:
        assert required in comments
    assert "raw source text and raw model output are not committed" in comments.lower()

    manual_content_reviews = [
        record["evaluation"]
        for record in records_by_schema("EvaluationRecord")
        if record["evaluation"]["evaluator_type"] == "manual_content_review"
    ]
    assert sorted(review["evaluation_id"] for review in manual_content_reviews) == [
        CHUNKED_LIVE_PILOT_CONTENT_REVIEW_EVALUATION_ID,
        CHUNKED_PRO_LIVE_PILOT_CONTENT_REVIEW_EVALUATION_ID,
        CHUNKED_SPAN_LIVE_PILOT_CONTENT_REVIEW_EVALUATION_ID,
        CHUNKED_SPAN_STRICT_REVIEW_003_EVALUATION_ID,
        CHUNKED_SPAN_REPEAT_LIVE_PILOT_CONTENT_REVIEW_EVALUATION_ID,
        CHUNKED_SPAN_STRICT_REVIEW_004_EVALUATION_ID,
        CHUNKED_LOCATOR_STRICT_REVIEW_005_EVALUATION_ID,
        LIVE_PILOT_CONTENT_REVIEW_EVALUATION_ID,
    ]
    assert not list(export_dir.glob("run_record.*manual_content_review*.json"))
    assert not list(export_dir.glob("artifact_envelope.*manual_content_review*.json"))
    assert not list(export_dir.glob("research_note.*manual_content_review*.json"))

    combined_committed = "\n".join(
        path.read_text()
        for path in [
            content_review_path,
            ROOT / "PORTFOLIO_CURRENT.md",
            ROOT / "LAB_REGISTRY.md",
            ROOT / "README.md",
            ROOT / "labs" / "chunked_source_grounding" / "LAB_CARD.md",
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
        "{{APPROVED_SOURCE_TEXT}}",
    ]:
        assert forbidden not in combined_committed

    portfolio = (ROOT / "PORTFOLIO_CURRENT.md").read_text()
    lab_registry = (ROOT / "LAB_REGISTRY.md").read_text()
    lab_card = (ROOT / "labs" / "chunked_source_grounding" / "LAB_CARD.md").read_text()
    for currentness_doc in [lab_registry, lab_card]:
        assert "manual review" in currentness_doc.lower()
        assert "manual content review remains" not in currentness_doc
        assert "generated synthesis metrics" not in currentness_doc.lower()
    assert "manual reviews" in portfolio
    assert manual_content_review_export_name("002") not in portfolio
    assert "generated synthesis metrics" not in portfolio.lower()
    assert "No graduated items." in (ROOT / "GRADUATION_LEDGER.md").read_text()


def test_goal8e_comparison_note_includes_source_span_precision_without_authority():
    lab_registry = (ROOT / "LAB_REGISTRY.md").read_text()
    assert "During scaffold, labs export only protocol fixture records." not in lab_registry
    assert (
        "Labs export protocol-valid records appropriate to their current phase. "
        "Scaffold fixtures, proposal-only live runs, manual reviews, and future "
        "experiment records must remain clearly labeled and must not claim protocol "
        "authority, graduation, validation, product evidence, strategy evidence, "
        "financial advice, live-trading authority, or architecture."
    ) in lab_registry

    assert GOAL7G_COMPARISON_NOTE.exists()
    assert GOAL7G_COMPARISON_NOTE.parts[-4:] == (
        "chunked_source_grounding",
        "PLANNING",
        "comparisons",
        "live_pilot_method_comparison_001.md",
    )
    assert "EXPORTS" not in GOAL7G_COMPARISON_NOTE.parts

    note = GOAL7G_COMPARISON_NOTE.read_text()
    for required in [
        "# Preliminary Method Comparison: Long-Context vs Chunked Source Grounding",
        "Status: preliminary / non-authoritative comparison note",
        "This note is not a synthesis export, not a protocol object, and not portfolio authority.",
        "Only tiny pilots exist.",
        "No method has graduated.",
        "No winner is declared.",
        (
            "No product, strategy, validation, financial-advice, live-trading, or "
            "architecture claim is made."
        ),
        "Why this file exists",
        "Existing currentness docs could not own this comparison",
        "long_context_judgment_live_pilot_001",
        "chunked_source_grounding_live_pilot_001",
        "chunked_source_grounding_live_pilot_002",
        "chunked_source_grounding_live_pilot_003",
        "chunked_source_grounding_live_pilot_004",
        "The Flash chunked run was a bounded negative result.",
        (
            "The Pro run is a method/config variant with a narrowed output contract, "
            "not a replacement for the Flash result."
        ),
        (
            "The source-span precision run is a refinement of the Pro narrowed-contract "
            "variant, not a replacement for pilot 002."
        ),
        (
            "The second-source source-span precision repeat tests whether the pilot 003 "
            "pattern generalizes beyond the first source."
        ),
        "source grounding",
        "source-span precision",
        "research usefulness",
        "hallucination / unsupported claims",
        "abstraction quality",
        "negative-result value",
        "output-contract fit",
        "comparison value for future method design",
        "missing_context",
        "over_abstracted_teacher_intent",
        "output_contract_too_large",
        "incomplete_json",
        "broad_segment_refs",
        "source_span_precision_improved",
        "source_span_precision_repeated",
        "content_review_passed_with_caveats",
        "exact/approximate labels were warranted",
        "score `0.86`",
        "limited_abstraction",
        "chunked_source_grounding_live_pilot_005",
        "Line-range locator candidates are useful",
        "char-offset and quote-hash candidate workflow is not yet reliable",
        "Next Research Direction",
        "Goal 12A",
        "line-range-first locator contract",
    ]:
        assert required in note

    for forbidden in [
        "# Preliminary Method Comparison: Live Pilot 001",
        "The tentative next step is to improve source-span precision for chunked Pro",
        "A later comparison can test whether canonical span IDs",
        "The leading next research direction is to repeat source-span precision",
        "The leading next bounded fork is Goal 11A",
        "BEGIN RAW SOURCE",
        "DEEPSEEK_API_KEY",
        "sk-",
        "\"api_key\"",
        "\"provider_payload\"",
        "raw_source_text",
        "raw_model_output",
        "{{APPROVED_SOURCE_TEXT}}",
        "wins",
        "validated trading",
        "generated synthesis metrics",
    ]:
        assert forbidden not in note

    portfolio = (ROOT / "PORTFOLIO_CURRENT.md").read_text()
    readme = (ROOT / "README.md").read_text()
    assert "live_pilot_method_comparison_001.md" in portfolio
    assert "chunked_source_grounding_live_pilot_003" not in portfolio
    assert "chunked_source_grounding_live_pilot_004" not in portfolio
    assert "Goal 8E" not in portfolio
    assert "live_pilot_method_comparison_001.md" in readme
    for currentness_doc in [portfolio, readme]:
        assert "generated synthesis metrics" not in currentness_doc.lower()

    assert all("comparisons" not in path.parts for path in lab_export_paths(ROOT))
    assert synthesize_exports(root=ROOT)["record_count"] == sum(
        1 for _ in all_lab_export_records()
    )
    assert "No graduated items." in (ROOT / "GRADUATION_LEDGER.md").read_text()


def test_portfolio_current_is_router_not_live_export_ledger():
    portfolio = (ROOT / "PORTFOLIO_CURRENT.md").read_text()

    for required_heading in [
        "Current phase: `milestone-3-method-comparison-recorded`",
        "## Current Portfolio Purpose",
        "## Active federation labs",
        "## Active Benchmark Packs",
        "## Current Evidence Posture",
        "## Current Architecture Rule",
        "## Synthesis Status",
        "## Graduation Status",
        "## Next Recommended Research Direction",
    ]:
        assert required_heading in portfolio

    for required in [
        "The portfolio has completed one tiny method-comparison loop on `text_judgment_v0`.",
        "labs/chunked_source_grounding/PLANNING/comparisons/live_pilot_method_comparison_001.md",
        (
            "Detailed pilot-level evidence lives in protocol export records and "
            "lab-local comparison notes."
        ),
        "source-span precision pattern repeated beyond the first source",
        (
            "These records are proposal-only research records. They are not validation, "
            "product evidence, strategy evidence, financial advice, live-trading "
            "authority, graduation, or architecture."
        ),
        (
            "Goal 11E comparison-note update is complete. The next proposed step is "
            f"{CURRENT_NEXT_STEP}."
        ),
    ]:
        assert required in portfolio

    for removed_ledger_text in [
        "## Live LLM Experiment Status",
        "The proposal-only live export set and manual content-review EvaluationRecord are:",
        "The chunked/source-grounded proposal-only live export set is:",
        "The DeepSeek V4 Pro proposal-only live export set is:",
    ]:
        assert removed_ledger_text not in portfolio

    assert_currentness_router_not_ledger(portfolio)


def test_goal10a_source_span_evaluator_planning_packet_is_contained():
    required_files = {
        "evaluator_plan.md",
        "source_offset_boundary.md",
        "review_rubric.md",
        "pilot_003_004_recheck_plan.md",
        "non_effects.md",
    }
    assert GOAL10A_EVALUATOR_DIR.exists()
    assert {path.name for path in GOAL10A_EVALUATOR_DIR.iterdir() if path.is_file()} == (
        required_files
    )
    assert "EXPORTS" not in GOAL10A_EVALUATOR_DIR.parts
    assert all("PLANNING" not in path.parts for path in lab_export_paths(ROOT))

    forbidden_planning_files = {
        "admission.md",
        "method_card.proposed.json",
        "experiment_card.proposed.json",
        "run_admission_update.md",
        "prompt_template.live_pilot_005.md",
    }
    assert forbidden_planning_files.isdisjoint(
        {path.name for path in GOAL10A_EVALUATOR_DIR.iterdir() if path.is_file()}
    )
    assert not list(
        (ROOT / "labs" / "chunked_source_grounding" / "EXPORTS").glob(
            "*source_span_evaluator_001*"
        )
    )

    evaluator_plan = (GOAL10A_EVALUATOR_DIR / "evaluator_plan.md").read_text()
    for required in [
        "Goal 10A source-span evaluator planning",
        "planning only",
        "Do not call an LLM.",
        "Do not run another model.",
        "Do not create EXPORTS records.",
        "manual_content_review",
        "canonical source-span precision",
        "line ranges",
        "character offsets",
        "quote hashes",
        "pilots 003 and 004",
        "existing EvaluationRecord can hold",
        "future protocol change",
    ]:
        assert required in evaluator_plan

    source_boundary = (GOAL10A_EVALUATOR_DIR / "source_offset_boundary.md").read_text()
    for required in [
        "raw_corpora_sha256:d8392c58c3b740eb",
        "raw_corpora_sha256:9f9e143429f5842a",
        "raw_corpora/selected/live_llm_pilot_001/source.txt",
        "raw_corpora/selected/source_span_precision_repeat_001/source.txt",
        "line range",
        "character offset",
        "quote hash",
        "Do not commit raw source text.",
        "local-only",
    ]:
        assert required in source_boundary

    rubric = (GOAL10A_EVALUATOR_DIR / "review_rubric.md").read_text()
    for required in [
        "exact",
        "approximate",
        "broad",
        "missing",
        "overclaimed exactness",
        "broad_segment_refs",
        "weak_source_span_precision",
        "overclaimed_exactness",
        "canonical_offsets_missing",
        "source_span_precision_repeated",
    ]:
        assert required in rubric

    recheck_plan = (
        GOAL10A_EVALUATOR_DIR / "pilot_003_004_recheck_plan.md"
    ).read_text()
    for required in [
        "chunked_source_grounding_live_pilot_003",
        "chunked_source_grounding_live_pilot_004",
        "manual re-review",
        "without copying raw source text",
        "without copying raw model output",
        "compare existing support labels against canonical offsets",
        "Goal 10B",
    ]:
        assert required in recheck_plan

    non_effects = (GOAL10A_EVALUATOR_DIR / "non_effects.md").read_text()
    for required in [
        "No LLM call has been made.",
        "No model has been run.",
        "No EXPORTS records are created.",
        "No protocol change is made.",
        "No synthesis feature is added.",
        "No benchmark pack is added.",
        "No graduation occurs.",
        (
            "not validation, product evidence, strategy evidence, financial advice, "
            "live-trading authority, or architecture"
        ),
    ]:
        assert required in non_effects

    combined = "\n".join(path.read_text() for path in GOAL10A_EVALUATOR_DIR.iterdir())
    for forbidden in [
        "BEGIN RAW SOURCE",
        "DEEPSEEK_API_KEY",
        "sk-",
        "\"api_key\"",
        "\"provider_payload\"",
        "{{APPROVED_SOURCE_TEXT}}",
    ]:
        assert forbidden not in combined

    protocol_schema_names = {
        path.name
        for path in (
            ROOT / "packages" / "qf_v3_protocol" / "src" / "qf_v3_protocol" / "schemas"
        ).glob("*.schema.json")
    }
    assert protocol_schema_names == PROTOCOL_SCHEMA_NAMES
    assert synthesize_exports(root=ROOT)["record_count"] == sum(
        1 for _ in all_lab_export_records()
    )

    portfolio = (ROOT / "PORTFOLIO_CURRENT.md").read_text()
    lab_card = (ROOT / "labs" / "chunked_source_grounding" / "LAB_CARD.md").read_text()
    assert "Current phase: `milestone-3-method-comparison-recorded`" in portfolio
    assert "Current phase: `milestone-2-live-pilot-recorded`" not in portfolio
    assert "canonical offsets" in portfolio
    assert "line-range-first locator contract" in lab_card
    for currentness_doc in [portfolio, lab_card]:
        assert "generated synthesis metrics" not in currentness_doc.lower()
        assert "run_record.live_pilot_005" not in currentness_doc
        assert "No graduated items." not in currentness_doc


def test_goal10b_strict_span_manual_reviews_are_protocol_records_only():
    export_dir = ROOT / "labs" / "chunked_source_grounding" / "EXPORTS"
    strict_review_paths = {
        "003": export_dir / CHUNKED_SPAN_STRICT_REVIEW_003_EXPORT,
        "004": export_dir / CHUNKED_SPAN_STRICT_REVIEW_004_EXPORT,
    }

    for path in strict_review_paths.values():
        assert path.exists()
        record = load_json(path)
        validate_record(record)
        assert record["protocol_version"] == "qf-v3-protocol-0.1"
        assert record["schema_name"] == "EvaluationRecord"
        assert record["schema_version"] == CURRENT_SCHEMA_VERSION
        assert record["evaluation"]["lab_id"] == "chunked_source_grounding"
        assert record["evaluation"]["target_type"] == "artifact"
        assert record["evaluation"]["evaluator_type"] == "manual_content_review"
        assert record["evaluation"]["benchmark_pack_id"] == "text_judgment_v0"
        assert "strict source-span re-review" in record["evaluation"]["comments"]
        assert "line_range_count=" in record["evaluation"]["comments"]
        assert "character_offset_count=" in record["evaluation"]["comments"]
        assert "quote_hash_count=" in record["evaluation"]["comments"]
        assert "quote_sha256=" in record["evaluation"]["comments"]
        assert "zero-based character offsets" in record["evaluation"]["comments"]
        assert "Raw source text and raw model output are not committed." in (
            record["evaluation"]["comments"]
        )
        assert (
            "not validation, product evidence, strategy evidence, financial advice, "
            "live-trading authority, graduation, or architecture"
        ) in record["evaluation"]["comments"]

    pilot_003 = load_json(strict_review_paths["003"])["evaluation"]
    assert pilot_003["evaluation_id"] == CHUNKED_SPAN_STRICT_REVIEW_003_EVALUATION_ID
    assert pilot_003["target_id"] == CHUNKED_SPAN_LIVE_PILOT_ARTIFACT_ID
    assert pilot_003["evaluator_id"] == "manual_content_review_strict_span_pilot_003"
    assert pilot_003["score"] == pytest.approx(0.88)
    assert pilot_003["pass_fail"] == "pass"
    assert pilot_003["failure_tags"] == [
        "source_span_precision_improved",
        "content_review_passed_with_caveats",
        "broad_segment_refs",
    ]
    for required in [
        "reviewed_hint_count=5",
        "exact_count=3",
        "approximate_count=2",
        "broad_count=0",
        "missing_count=0",
        "overclaimed_exactness_count=0",
        "canonical_offsets_missing=false_for_strict_review",
        "original_artifact_canonical_offsets_missing=true",
        "SLC-001 source_ref=raw_corpora_sha256:d8392c58c3b740eb",
        "SLC-002 source_ref=raw_corpora_sha256:d8392c58c3b740eb",
        "SLC-003 source_ref=raw_corpora_sha256:d8392c58c3b740eb",
        "TSH-001 source_ref=raw_corpora_sha256:d8392c58c3b740eb",
        "TSH-002 source_ref=raw_corpora_sha256:d8392c58c3b740eb",
    ]:
        assert required in pilot_003["comments"]

    pilot_004 = load_json(strict_review_paths["004"])["evaluation"]
    assert pilot_004["evaluation_id"] == CHUNKED_SPAN_STRICT_REVIEW_004_EVALUATION_ID
    assert pilot_004["target_id"] == CHUNKED_SPAN_REPEAT_LIVE_PILOT_ARTIFACT_ID
    assert pilot_004["evaluator_id"] == "manual_content_review_strict_span_pilot_004"
    assert pilot_004["score"] == pytest.approx(0.82)
    assert pilot_004["pass_fail"] == "pass"
    assert pilot_004["failure_tags"] == [
        "source_span_precision_repeated",
        "source_span_precision_improved",
        "content_review_passed_with_caveats",
        "broad_segment_refs",
        "overclaimed_exactness",
    ]
    for required in [
        "reviewed_hint_count=6",
        "exact_count=4",
        "approximate_count=2",
        "broad_count=0",
        "missing_count=0",
        "overclaimed_exactness_count=1",
        "canonical_offsets_missing=false_for_strict_review",
        "original_artifact_canonical_offsets_missing=true",
        "source-span precision repeated under stricter review",
        "SLC-001 source_ref=raw_corpora_sha256:9f9e143429f5842a",
        "SLC-002 source_ref=raw_corpora_sha256:9f9e143429f5842a",
        "SLC-003 source_ref=raw_corpora_sha256:9f9e143429f5842a",
        "TSH-001 source_ref=raw_corpora_sha256:9f9e143429f5842a",
        "TSH-002 source_ref=raw_corpora_sha256:9f9e143429f5842a",
        "TSH-003 source_ref=raw_corpora_sha256:9f9e143429f5842a",
    ]:
        assert required in pilot_004["comments"]

    strict_review_text = "\n".join(path.read_text() for path in strict_review_paths.values())
    for forbidden in [
        "BEGIN RAW SOURCE",
        "DEEPSEEK_API_KEY",
        "sk-",
        "\"api_key\"",
        "\"provider_payload\"",
        "{{APPROVED_SOURCE_TEXT}}",
    ]:
        assert forbidden not in strict_review_text
    assert not list(export_dir.glob("run_record.*strict_span_review*.json"))
    assert not list(export_dir.glob("artifact_envelope.*strict_span_review*.json"))
    assert not list(export_dir.glob("research_note.*strict_span_review*.json"))

    protocol_schema_names = {
        path.name
        for path in (
            ROOT / "packages" / "qf_v3_protocol" / "src" / "qf_v3_protocol" / "schemas"
        ).glob("*.schema.json")
    }
    assert protocol_schema_names == PROTOCOL_SCHEMA_NAMES
    assert synthesize_exports(root=ROOT)["record_count"] == sum(
        1 for _ in all_lab_export_records()
    )

    manual_content_reviews = [
        record["evaluation"]
        for record in records_by_schema("EvaluationRecord")
        if record["evaluation"]["evaluator_type"] == "manual_content_review"
    ]
    assert sorted(review["evaluation_id"] for review in manual_content_reviews) == [
        CHUNKED_LIVE_PILOT_CONTENT_REVIEW_EVALUATION_ID,
        CHUNKED_PRO_LIVE_PILOT_CONTENT_REVIEW_EVALUATION_ID,
        CHUNKED_SPAN_LIVE_PILOT_CONTENT_REVIEW_EVALUATION_ID,
        CHUNKED_SPAN_STRICT_REVIEW_003_EVALUATION_ID,
        CHUNKED_SPAN_REPEAT_LIVE_PILOT_CONTENT_REVIEW_EVALUATION_ID,
        CHUNKED_SPAN_STRICT_REVIEW_004_EVALUATION_ID,
        CHUNKED_LOCATOR_STRICT_REVIEW_005_EVALUATION_ID,
        LIVE_PILOT_CONTENT_REVIEW_EVALUATION_ID,
    ]

    portfolio = (ROOT / "PORTFOLIO_CURRENT.md").read_text()
    lab_card = (ROOT / "labs" / "chunked_source_grounding" / "LAB_CARD.md").read_text()
    for currentness_doc in [portfolio, lab_card]:
        assert "Goal 11E comparison-note update is complete" in currentness_doc
        assert "Goal 12A" in currentness_doc
        assert "line-range-first locator contract" in currentness_doc
        assert "generated synthesis metrics" not in currentness_doc.lower()
    assert "The current next step is evaluator planning" not in portfolio
    assert "The active thread is source-span evaluator planning" not in lab_card
    assert "current next step is comparison-note compression" not in portfolio
    assert "The active thread is Goal 10C comparison-note compression" not in lab_card
    assert "No graduated items." in (ROOT / "GRADUATION_LEDGER.md").read_text()


def test_goal10c_comparison_note_compresses_strict_span_review_findings():
    comparisons_dir = (
        ROOT / "labs" / "chunked_source_grounding" / "PLANNING" / "comparisons"
    )
    comparison_files = sorted(path.name for path in comparisons_dir.glob("*.md"))
    assert comparison_files == ["live_pilot_method_comparison_001.md"]

    note = GOAL7G_COMPARISON_NOTE.read_text()
    for required in [
        "strict source-span re-review findings",
        "chunked_source_grounding_live_pilot_003_strict_span_review",
        "chunked_source_grounding_live_pilot_004_strict_span_review",
        "pilot 003 strict-span review",
        "score `0.88`",
        "reviewed hints `5`",
        "exact `3`",
        "approximate `2`",
        "broad `0`",
        "missing `0`",
        "quote hashes `5`",
        "overclaimed exactness `0`",
        "pilot 004 strict-span review",
        "score `0.82`",
        "reviewed hints `6`",
        "exact `4`",
        "approximate `2`",
        "quote hashes `6`",
        "overclaimed exactness `1`",
        "one model-labeled exact case was better treated as approximate",
        "source-span precision improvement repeated under stricter review",
        "the original model artifact did not emit canonical locators",
        (
            "reviewers could map the support hints to canonical line ranges, "
            "character offsets, and quote hashes"
        ),
        "broad_segment_refs",
        "limited_abstraction",
        "source-span locator candidate pilot 005",
        "Direct locator emission improved only partially",
        "line-range-first locator contract",
        "local review computes offsets/hashes only after line-range validation",
    ]:
        assert required in note

    for stale_or_forbidden in [
        "Use this comparison note to choose the next bounded research fork.",
        (
            "Reasonable next forks include a stricter evaluator for canonical offsets, "
            "a third-source repeat, or a grounded long-context variant"
        ),
        "still needs canonical offsets or a stricter evaluator before stronger claims",
        "The leading next bounded fork is Goal 11A",
        "A third-source repeat is the leading next fork",
        "BEGIN RAW SOURCE",
        "DEEPSEEK_API_KEY",
        "sk-",
        "\"api_key\"",
        "\"provider_payload\"",
        "raw_source_text",
        "raw_model_output",
        "{{APPROVED_SOURCE_TEXT}}",
        "wins",
        "validated trading",
        "generated synthesis metrics",
    ]:
        assert stale_or_forbidden not in note

    assert all("comparisons" not in path.parts for path in lab_export_paths(ROOT))
    assert not list(
        (ROOT / "labs" / "chunked_source_grounding" / "EXPORTS").glob(
            "*locator_output_contract*"
        )
    )
    assert synthesize_exports(root=ROOT)["record_count"] == sum(
        1 for _ in all_lab_export_records()
    )

    portfolio = (ROOT / "PORTFOLIO_CURRENT.md").read_text()
    lab_card = (ROOT / "labs" / "chunked_source_grounding" / "LAB_CARD.md").read_text()
    for currentness_doc in [portfolio, lab_card]:
        assert "source-span locator candidate pilot" in currentness_doc
        assert "Goal 11E comparison-note update is complete" in currentness_doc
        assert "Goal 12A" in currentness_doc
        assert "line-range-first locator contract" in currentness_doc
        assert "generated synthesis metrics" not in currentness_doc.lower()
    assert "current next step is comparison-note compression" not in portfolio
    assert "The active thread is Goal 10C comparison-note compression" not in lab_card
    assert "No graduated items." in (ROOT / "GRADUATION_LEDGER.md").read_text()


def test_goal11a_source_span_locator_contract_planning_packet_is_contained():
    required_files = {
        "contract_plan.md",
        "prompt_delta_plan.md",
        "evaluator_plan.md",
        "source_locator_boundary.md",
        "pilot_003_004_lessons.md",
        "non_effects.md",
    }
    assert GOAL11A_LOCATOR_CONTRACT_DIR.exists()
    assert {
        path.name for path in GOAL11A_LOCATOR_CONTRACT_DIR.iterdir() if path.is_file()
    } == required_files
    assert "EXPORTS" not in GOAL11A_LOCATOR_CONTRACT_DIR.parts
    assert all("PLANNING" not in path.parts for path in lab_export_paths(ROOT))

    forbidden_planning_files = {
        "admission.md",
        "method_card.proposed.json",
        "experiment_card.proposed.json",
        "run_admission_update.md",
        "prompt_template.live_pilot_005.md",
    }
    assert forbidden_planning_files.isdisjoint(
        {path.name for path in GOAL11A_LOCATOR_CONTRACT_DIR.iterdir() if path.is_file()}
    )
    assert not list(
        (ROOT / "labs" / "chunked_source_grounding" / "EXPORTS").glob(
            "*source_span_locator_contract_001*"
        )
    )

    contract_plan = (GOAL11A_LOCATOR_CONTRACT_DIR / "contract_plan.md").read_text()
    for required in [
        "Goal 11A source-span locator output contract planning",
        "planning only",
        "Can the model emit canonical locator candidates directly",
        "source_ref",
        "candidate_line_start",
        "candidate_line_end",
        "candidate_char_start",
        "candidate_char_end",
        "locator_confidence",
        "locator_label: exact | approximate | broad | missing",
        "The model should not emit quote hashes.",
        "The local runner/reviewer computes quote hashes",
        "committed records may include metadata-safe computed quote hashes",
        "every claim must have at least one locator candidate",
        "every locator candidate must have one claim id",
        "unsupported claims must explain why no valid locator exists",
        "source-linked claim table",
        "locator candidate table",
        "unsupported-claim report",
        "brief method-failure notes",
        "ArtifactEnvelope.payload",
        "no protocol change",
    ]:
        assert required in contract_plan

    prompt_delta = (GOAL11A_LOCATOR_CONTRACT_DIR / "prompt_delta_plan.md").read_text()
    for required in [
        "Do not add broad judgment abstraction notes.",
        "Do not add comparison commentary.",
        "Do not add product-like study card fields.",
        "Do not ask for strategy, validation, trading advice, or playbook content.",
        "line-range candidates",
        "character-offset candidates",
        "Do not ask the model to emit quote hashes.",
        "Local runner/reviewer computes quote hashes",
    ]:
        assert required in prompt_delta
    for forbidden in [
        "quote-hash candidates",
        "quote_hash_candidate",
    ]:
        assert forbidden not in contract_plan
        assert forbidden not in prompt_delta

    evaluator_plan = (GOAL11A_LOCATOR_CONTRACT_DIR / "evaluator_plan.md").read_text()
    for required in [
        "manual_content_review",
        "exact if line/offset and locally computed quote hash directly support the claim",
        "approximate if support is local but not exact",
        "broad if support points to a general region only",
        "missing if no source support is found",
        "overclaimed_exactness",
        "no new evaluator type",
    ]:
        assert required in evaluator_plan

    boundary = (GOAL11A_LOCATOR_CONTRACT_DIR / "source_locator_boundary.md").read_text()
    for required in [
        "metadata-safe",
        "source text stays ignored/local",
        "no raw source text is committed",
        "raw_corpora_sha256:d8392c58c3b740eb",
        "raw_corpora_sha256:9f9e143429f5842a",
        "raw_corpora/selected/live_llm_pilot_001/source.txt",
        "raw_corpora/selected/source_span_precision_repeat_001/source.txt",
        "The model should not emit quote hashes.",
        "Quote hashes should be computed locally after the model response",
    ]:
        assert required in boundary

    lessons = (GOAL11A_LOCATOR_CONTRACT_DIR / "pilot_003_004_lessons.md").read_text()
    for required in [
        "pilots 003/004 emitted support hints",
        "strict reviewers reconstructed canonical locators after the fact",
        "Goal 11 should test whether the model can emit locator candidates directly",
        "chunked_source_grounding_live_pilot_003_strict_span_review",
        "chunked_source_grounding_live_pilot_004_strict_span_review",
        "one model-labeled exact case was better treated as approximate",
    ]:
        assert required in lessons

    non_effects = (GOAL11A_LOCATOR_CONTRACT_DIR / "non_effects.md").read_text()
    for required in [
        "No LLM call has been made.",
        "No model has been run.",
        "No EXPORTS records are created.",
        "No RunRecord, ArtifactEnvelope, EvaluationRecord, or ResearchNote is created.",
        "No protocol change is made.",
        "No synthesis feature is added.",
        "No shared script or helper is added.",
        "No benchmark pack is added.",
        "No graduation occurs.",
    ]:
        assert required in non_effects

    combined = "\n".join(path.read_text() for path in GOAL11A_LOCATOR_CONTRACT_DIR.iterdir())
    for forbidden in [
        "BEGIN RAW SOURCE",
        "DEEPSEEK_API_KEY",
        "sk-",
        "\"api_key\"",
        "\"provider_payload\"",
        "{{APPROVED_SOURCE_TEXT}}",
        "validated trading",
    ]:
        assert forbidden not in combined

    protocol_schema_names = {
        path.name
        for path in (
            ROOT / "packages" / "qf_v3_protocol" / "src" / "qf_v3_protocol" / "schemas"
        ).glob("*.schema.json")
    }
    assert protocol_schema_names == PROTOCOL_SCHEMA_NAMES
    assert synthesize_exports(root=ROOT)["record_count"] == sum(
        1 for _ in all_lab_export_records()
    )

    portfolio = (ROOT / "PORTFOLIO_CURRENT.md").read_text()
    lab_card = (ROOT / "labs" / "chunked_source_grounding" / "LAB_CARD.md").read_text()
    for currentness_doc in [portfolio, lab_card]:
        assert "source-span locator candidate pilot" in currentness_doc
        assert "Goal 11E comparison-note update is complete" in currentness_doc
        assert "Goal 12A" in currentness_doc
        assert "line-range-first locator contract" in currentness_doc
        assert "generated synthesis metrics" not in currentness_doc.lower()
        assert "run_record.live_pilot_005" not in currentness_doc
    assert "No graduated items." in (ROOT / "GRADUATION_LEDGER.md").read_text()


def test_goal11b_source_span_locator_live_admission_packet_is_contained_and_current():
    required_files = {
        "admission.md",
        "method_card.proposed.json",
        "experiment_card.proposed.json",
        "evaluator_plan.md",
        "source_privacy_boundary.md",
        "prompt_template.live_pilot_005.md",
        "run_admission_update.md",
        "stop_condition.md",
    }
    assert GOAL9A_SOURCE_PATH.exists()
    source_text = GOAL9A_SOURCE_PATH.read_text()
    source_word_count = len(source_text.split())
    source_hash = sha256_file(GOAL9A_SOURCE_PATH)
    source_ref = f"raw_corpora_sha256:{source_hash[:16]}"

    assert GOAL11B_PILOT_DIR.exists()
    assert {path.name for path in GOAL11B_PILOT_DIR.iterdir() if path.is_file()} == (
        required_files
    )

    method_card = load_json(GOAL11B_PILOT_DIR / "method_card.proposed.json")
    experiment_card = load_json(GOAL11B_PILOT_DIR / "experiment_card.proposed.json")
    validate_record(method_card)
    validate_record(experiment_card)

    method = method_card["method_card"]
    assert method_card["schema_name"] == "MethodCard"
    assert method_card["schema_version"] == CURRENT_SCHEMA_VERSION
    assert method["method_id"] == GOAL11B_METHOD_ID
    assert method["lab_id"] == "chunked_source_grounding"
    assert method["method_family"] == "chunked_source_grounded_llm_reader_proposed"
    assert "same approved source as pilot 004" in " ".join(method["intended_inputs"])
    assert "line/offset locator candidates" in " ".join(method["intended_outputs"])
    assert "locally computed quote hashes" in " ".join(method["intended_outputs"])
    assert "broad judgment abstraction notes" not in method["intended_outputs"]
    assert "cryptographic hashes" in " ".join(method["known_risks"])
    assert "not a completed run" in method["non_goals"]
    assert "not architecture or graduation evidence" in method["non_goals"]

    experiment = experiment_card["experiment_card"]
    assert experiment_card["schema_name"] == "ExperimentCard"
    assert experiment_card["schema_version"] == CURRENT_SCHEMA_VERSION
    assert experiment["experiment_id"] == GOAL11B_EXPERIMENT_ID
    assert experiment["lab_id"] == "chunked_source_grounding"
    assert experiment["benchmark_pack_ids"] == ["text_judgment_v0"]
    assert experiment["method_ids"] == [GOAL11B_METHOD_ID]
    assert experiment["expected_artifact_types"] == [
        "chunked_source_span_locator_candidate_proposal"
    ]
    assert "canonical locator candidates directly" in experiment["research_question"]
    assert "local review can compute quote hashes" in experiment["research_question"]

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
    assert "EXPORTS" not in GOAL11B_PILOT_DIR.parts
    assert all("PLANNING" not in path.parts for path in lab_export_paths(ROOT))

    admission = (GOAL11B_PILOT_DIR / "admission.md").read_text()
    for required_heading in [
        "Hardening / Cleanup Discipline",
        "Goal 11A Cleanup",
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
        "This is planning/admission only. No LLM call has been made.",
        "No RunRecord, ArtifactEnvelope, EvaluationRecord, or ResearchNote exists for this pilot.",
        "Do not ask the model to emit quote hashes.",
        "local runner/reviewer computes quote hashes",
        "Do not add broad judgment abstraction notes.",
        "Do not add full comparison commentary.",
        "Do not ask for a product-like study card.",
        "Do not add strategy, validation, trading advice, or playbook content.",
    ]:
        assert required_guardrail in admission

    evaluator_plan = (GOAL11B_PILOT_DIR / "evaluator_plan.md").read_text()
    for required in [
        "schema_check",
        "manual_boundary_review",
        "manual_content_review",
        "line/offset locator candidates",
        "exact | approximate | broad | missing",
        "computed quote hash",
        "overclaimed_exactness",
    ]:
        assert required in evaluator_plan

    source_boundary = (GOAL11B_PILOT_DIR / "source_privacy_boundary.md").read_text()
    for required in [
        source_ref,
        f"Full selected excerpt SHA-256: `{source_hash}`",
        f"Selected excerpt word count: `{source_word_count}`",
        "raw_corpora/selected/source_span_precision_repeat_001/source.txt",
        "raw_corpora/trader_source_corpus/pharm/box trades_999923657.txt",
        "same approved source as `chunked_source_grounding_live_pilot_004`",
        "Do not commit raw source text.",
        "Do not fall back to the full corpus path.",
        "Quote hashes are computed locally after the model response",
    ]:
        assert required in source_boundary

    update = (GOAL11B_PILOT_DIR / "run_admission_update.md").read_text()
    prompt_template_path = GOAL11B_PILOT_DIR / "prompt_template.live_pilot_005.md"
    prompt_template = prompt_template_path.read_text()
    for required in [
        (
            "This admission update defines the executable preflight scope for exactly "
            "one future tiny live LLM pilot run."
        ),
        (
            "It does not by itself authorize execution. Execution requires a separate "
            "Goal 11C instruction."
        ),
        "Provider: DeepSeek API",
        "API format: OpenAI-compatible chat completions",
        "Base URL: `https://api.deepseek.com`",
        "Model: `deepseek-v4-pro`",
        "Reasoning/thinking mode: non-thinking",
        "Tool routing: tools disabled",
        "Benchmark pack: `text_judgment_v0`",
        "Lab: `labs/chunked_source_grounding`",
        "Budget cap: `$3` hard maximum.",
        "No retries unless the call fails before producing output.",
        "Do not silently substitute `deepseek-v4-flash`, `deepseek-chat`, "
        "`deepseek-reasoner`, or any other model.",
        "Outputs from this experiment are proposals until evaluated.",
        "No private/raw source material or provider payloads are committed.",
        "Do not ask the model to emit quote hashes.",
        "Local runner/reviewer computes quote hashes",
        source_ref,
        f"Selected excerpt word count: `{source_word_count}`",
    ]:
        assert required in update
    assert "thinking" in update
    assert '"type": "disabled"' in update
    assert "one model-call batch" in update
    assert "Do not fall back to the full corpus path." in update
    assert "authorizes exactly one tiny live LLM pilot run" not in update

    recorded_prompt_hash = re.search(r"Prompt template SHA-256: `([0-9a-f]{64})`", update)
    assert recorded_prompt_hash
    assert recorded_prompt_hash.group(1) == sha256_file(prompt_template_path)
    assert "Prompt Template" in prompt_template
    assert "{{APPROVED_SOURCE_TEXT}}" in prompt_template
    assert "No raw source text is committed in this template." in prompt_template
    assert "source_linked_claim_table" in prompt_template
    assert "locator_candidate_table" in prompt_template
    assert "unsupported_claim_report" in prompt_template
    assert "brief_method_failure_notes" in prompt_template
    for required_field in [
        "claim_id",
        "source_ref",
        "candidate_line_start",
        "candidate_line_end",
        "candidate_char_start",
        "candidate_char_end",
        "locator_confidence",
        "locator_label",
        "exact | approximate | broad | missing",
    ]:
        assert required_field in prompt_template
    assert "Do not emit quote hashes." in prompt_template
    assert "Local runner/reviewer computes quote hashes" in prompt_template
    assert "quote_hash_candidate" not in prompt_template
    assert "judgment_abstraction_notes" not in prompt_template
    assert "full comparison commentary" not in prompt_template
    assert "study card" not in prompt_template.lower()

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
        "model_id": "deepseek-v4-pro",
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

    stop_condition = (GOAL11B_PILOT_DIR / "stop_condition.md").read_text()
    for required in [
        "selected pilot 004 source excerpt is missing",
        "source file is not ignored by git",
        "source file is staged or tracked",
        "`deepseek-v4-pro` is unavailable",
        "the output contract expands beyond locator candidates",
        "the prompt asks the model to emit quote hashes",
        "the run attempts to fall back to the full corpus path",
    ]:
        assert required in stop_condition

    combined = "\n".join(path.read_text() for path in GOAL11B_PILOT_DIR.iterdir())
    for forbidden in [
        "BEGIN RAW SOURCE",
        "DEEPSEEK_API_KEY=",
        "sk-",
        "\"api_key\"",
        "\"provider_payload\"",
        "quote_hash_candidate",
    ]:
        assert forbidden not in combined

    summary = synthesize_exports(root=ROOT)
    assert summary["record_count"] == sum(1 for _ in all_lab_export_records())
    assert all("PLANNING" not in path.parts for path in lab_export_paths(ROOT))

    portfolio = (ROOT / "PORTFOLIO_CURRENT.md").read_text()
    lab_card = (ROOT / "labs" / "chunked_source_grounding" / "LAB_CARD.md").read_text()
    for currentness_doc in [portfolio, lab_card]:
        assert "Goal 11E comparison-note update is complete" in currentness_doc
        assert "Goal 12A" in currentness_doc
        assert "line-range-first locator contract" in currentness_doc
        assert "generated synthesis metrics" not in currentness_doc.lower()
        assert "run_record.live_pilot_005" not in currentness_doc
    assert "current next step is Goal 11A" not in portfolio
    assert "The active thread is Goal 11A" not in lab_card
    assert "current bounded planning packet is Goal 11B" not in portfolio
    assert "The active thread is Goal 11B live-run admission planning" not in lab_card
    assert "quote-hash candidates" not in portfolio
    assert "No graduated items." in (ROOT / "GRADUATION_LEDGER.md").read_text()


def test_goal11c_source_span_locator_live_export_set_is_protocol_valid_and_bounded():
    export_dir = ROOT / "labs" / "chunked_source_grounding" / "EXPORTS"
    live_exports = {
        path.name: load_json(path) for path in export_dir.glob("*.live_pilot_005.json")
    }
    assert set(live_exports) == live_pilot_export_names("005")
    for record in live_exports.values():
        validate_record(record)

    run = live_exports["run_record.live_pilot_005.json"]
    artifact = live_exports["artifact_envelope.live_pilot_005.json"]
    evaluation = live_exports["evaluation_record.live_pilot_005.json"]
    note = live_exports["research_note.live_pilot_005.json"]

    source_hash = sha256_file(GOAL9A_SOURCE_PATH)
    source_ref = f"raw_corpora_sha256:{source_hash[:16]}"
    prompt_template_path = GOAL11B_PILOT_DIR / "prompt_template.live_pilot_005.md"

    assert run["schema_name"] == "RunRecord"
    assert run["schema_version"] == CURRENT_SCHEMA_VERSION
    assert run["run_record"] == {
        "run_id": CHUNKED_LOCATOR_LIVE_PILOT_RUN_ID,
        "lab_id": "chunked_source_grounding",
        "experiment_id": GOAL11B_EXPERIMENT_ID,
        "method_id": GOAL11B_METHOD_ID,
        "benchmark_pack_id": "text_judgment_v0",
        "source_refs": [source_ref],
        "artifact_ids": [CHUNKED_LOCATOR_LIVE_PILOT_ARTIFACT_ID],
        "evaluation_ids": [CHUNKED_LOCATOR_LIVE_PILOT_EVALUATION_ID],
        "run_kind": "live_llm_pilot",
        "outcome_polarity": "proposal_only",
        "status": "live_recorded",
    }

    artifact_body = artifact["artifact"]
    artifact_payload = artifact_body["payload"]
    assert artifact_body["artifact_id"] == CHUNKED_LOCATOR_LIVE_PILOT_ARTIFACT_ID
    assert artifact_body["artifact_type"] == (
        "chunked_source_span_locator_candidate_proposal"
    )
    assert artifact_body["lab_id"] == "chunked_source_grounding"
    assert artifact_body["method_id"] == GOAL11B_METHOD_ID
    assert artifact_body["run_id"] == CHUNKED_LOCATOR_LIVE_PILOT_RUN_ID
    assert artifact_body["source_refs"] == [source_ref]
    assert artifact_body["posture"] == {
        "grounding_status": "source_linked",
        "review_status": "self_checked",
        "readiness_status": "study_candidate",
        "validation_status": "none",
        "lifecycle_status": "active",
    }
    for blocker in [
        "proposal_only_not_evaluated",
        "manual_strict_locator_review_not_yet_completed",
        "raw_output_local_only",
    ]:
        assert blocker in artifact_body["blockers"]

    assert artifact_payload["outcome_polarity"] == "proposal_only"
    assert artifact_payload["proposal_only"] is True
    assert artifact_payload["provider_id"] == "deepseek_api"
    assert artifact_payload["api_format"] == "openai_compatible_chat_completions"
    assert artifact_payload["base_url"] == "https://api.deepseek.com"
    assert artifact_payload["model_id"] == "deepseek-v4-pro"
    assert artifact_payload["requested_model_id"] == "deepseek-v4-pro"
    assert artifact_payload["thinking"] == {"type": "disabled"}
    assert artifact_payload["stream"] is False
    assert artifact_payload["tool_routing"] == "none"
    assert artifact_payload["prompt_template_path"] == (
        "labs/chunked_source_grounding/PLANNING/live_llm_pilot_005/"
        "prompt_template.live_pilot_005.md"
    )
    assert artifact_payload["prompt_template_sha256"] == sha256_file(prompt_template_path)
    assert artifact_payload["config_sha256"] == (
        "a8a8daccf08254a827fd5d68203d41f56b25c295e14e4005f9671fd0bd46a9cb"
    )
    assert artifact_payload["source_metadata"] == {
        "source_ref": source_ref,
        "source_scope": (
            "operator-approved second-source excerpt from the local pharm box-trades "
            "transcript"
        ),
        "source_path_scope": (
            "raw_corpora/selected/source_span_precision_repeat_001/source.txt"
        ),
        "source_origin_scope": (
            "raw_corpora/trader_source_corpus/pharm/box trades_999923657.txt"
        ),
        "source_file_sha256": source_hash,
        "source_file_word_count": 945,
        "excerpt_sha256": source_hash,
        "excerpt_word_count": 945,
        "raw_source_text_committed": False,
    }
    assert artifact_payload["cost_metadata"]["budget_cap_usd"] == 3.0
    assert artifact_payload["cost_metadata"]["estimated_cost_usd"] <= 3.0
    assert artifact_payload["raw_source_text_committed"] is False
    assert artifact_payload["raw_provider_payload_committed"] is False
    assert artifact_payload["raw_prompt_trace_committed"] is False
    assert artifact_payload["raw_model_trace_committed"] is False
    assert artifact_payload["secrets_committed"] is False
    assert "raw_source_text" not in artifact_payload
    assert "provider_payload" not in artifact_payload
    assert "api_key" not in json.dumps(artifact_payload).lower()

    model_output_metadata = artifact_payload["model_output_metadata"]
    assert model_output_metadata["parsed_json_success"] is True
    assert model_output_metadata["finish_reason"] == "stop"
    assert model_output_metadata["model_output_truncated"] is False
    assert model_output_metadata["expected_top_level_keys"] == [
        "source_linked_claim_table",
        "locator_candidate_table",
        "unsupported_claim_report",
        "brief_method_failure_notes",
    ]
    assert model_output_metadata["missing_expected_top_level_keys"] == []
    assert model_output_metadata["locator_candidate_count"] >= 1
    assert model_output_metadata["model_emitted_locator_coordinates"] is True

    locator_metadata = artifact_payload["locator_candidate_metadata"]
    assert locator_metadata["local_quote_hash_computation_attempted"] is True
    assert locator_metadata["quote_hashes_computed_by"] == (
        "local_runner_from_candidate_offsets"
    )
    assert locator_metadata["model_asked_to_emit_quote_hashes"] is False
    assert locator_metadata["model_emitted_quote_hashes_ignored"] in {False, True}
    assert locator_metadata["computed_quote_hash_count"] >= 1
    assert locator_metadata["computed_quote_hash_count"] <= (
        model_output_metadata["locator_candidate_count"]
    )
    for item in locator_metadata["computed_quote_hashes"]:
        assert item["claim_id"]
        assert item["source_ref"] == source_ref
        assert re.fullmatch(r"[0-9a-f]{64}", item["quote_sha256"])
        assert item["quote_hash_computed_locally"] is True
        assert item["quote_text_committed"] is False

    assert evaluation["evaluation"]["evaluation_id"] == (
        CHUNKED_LOCATOR_LIVE_PILOT_EVALUATION_ID
    )
    assert evaluation["evaluation"]["target_id"] == CHUNKED_LOCATOR_LIVE_PILOT_ARTIFACT_ID
    assert evaluation["evaluation"]["evaluator_type"] == "manual_boundary_review"
    assert evaluation["evaluation"]["pass_fail"] == "pass"
    for required in [
        "method quality was not evaluated",
        "prompt asked for line/offset locator candidates, not quote hashes",
        "quote hashes were computed locally where offsets were usable",
        (
            "raw source text, provider payloads, prompt traces, model traces, and "
            "secrets are not committed"
        ),
    ]:
        assert required in evaluation["evaluation"]["comments"]

    research_note = note["research_note"]
    assert research_note["note_id"] == CHUNKED_LOCATOR_LIVE_PILOT_NOTE_ID
    assert research_note["experiment_ids"] == [GOAL11B_EXPERIMENT_ID]
    assert research_note["benchmark_pack_ids"] == ["text_judgment_v0"]
    assert research_note["evidence_disclaimer"] == LIVE_EVIDENCE_DISCLAIMER
    assert any(
        "No method success is claimed" in item for item in research_note["what_failed"]
    )
    assert any("Goal 11D" in item for item in research_note["do_not_repeat"])

    combined_committed = "\n".join(
        (export_dir / name).read_text()
        for name in sorted(live_pilot_export_names("005"))
    )
    for forbidden in [
        "BEGIN RAW SOURCE",
        "DEEPSEEK_API_KEY",
        "sk-",
        "\"api_key\"",
        "\"provider_payload\"",
        "{{APPROVED_SOURCE_TEXT}}",
    ]:
        assert forbidden not in combined_committed

    portfolio = (ROOT / "PORTFOLIO_CURRENT.md").read_text()
    lab_card = (ROOT / "labs" / "chunked_source_grounding" / "LAB_CARD.md").read_text()
    lab_registry = (ROOT / "LAB_REGISTRY.md").read_text()
    for currentness_doc in [portfolio, lab_card, lab_registry]:
        assert "Goal 11E comparison-note update is complete" in currentness_doc
        assert "Goal 12A" in currentness_doc
        assert "line-range-first locator contract" in currentness_doc
        assert "proposal-only" in currentness_doc
        assert "generated synthesis metrics" not in currentness_doc.lower()
        assert "run_record.live_pilot_005" not in currentness_doc
    assert (
        "Goal 11B admission planning is complete. The next proposed step is Goal 11C"
        not in portfolio
    )
    assert "No graduated items." in (ROOT / "GRADUATION_LEDGER.md").read_text()


def test_goal11d_strict_locator_review_records_coordinate_failure_only():
    export_dir = ROOT / "labs" / "chunked_source_grounding" / "EXPORTS"
    review_path = export_dir / CHUNKED_LOCATOR_STRICT_REVIEW_005_EXPORT
    assert review_path.exists()

    record = load_json(review_path)
    validate_record(record)
    assert record["protocol_version"] == "qf-v3-protocol-0.1"
    assert record["schema_name"] == "EvaluationRecord"
    assert record["schema_version"] == CURRENT_SCHEMA_VERSION

    evaluation = record["evaluation"]
    assert evaluation["evaluation_id"] == CHUNKED_LOCATOR_STRICT_REVIEW_005_EVALUATION_ID
    assert evaluation["lab_id"] == "chunked_source_grounding"
    assert evaluation["target_id"] == CHUNKED_LOCATOR_LIVE_PILOT_ARTIFACT_ID
    assert evaluation["target_type"] == "artifact"
    assert evaluation["evaluator_id"] == "manual_content_review_strict_locator_pilot_005"
    assert evaluation["evaluator_type"] == "manual_content_review"
    assert evaluation["benchmark_pack_id"] == "text_judgment_v0"
    assert evaluation["score"] == pytest.approx(0.58)
    assert evaluation["pass_fail"] == "fail"
    assert evaluation["failure_tags"] == [
        "line_ranges_valid",
        "quote_hashes_computed_locally",
        "source_span_locator_improved",
        "char_offsets_inaccurate",
        "quote_hashes_not_evidence_valid",
        "canonical_locator_candidates_failed",
    ]

    comments = evaluation["comments"]
    for required in [
        "Manual strict locator review only",
        "reviewed_locator_candidate_count=3",
        "line_range_valid_count=3",
        "char_offset_syntax_valid_count=3",
        "char_offset_support_valid_count=0",
        "quote_hash_count=3",
        "quote_hash_support_valid_count=0",
        "exact_count=0",
        "approximate_count=2",
        "broad_count=1",
        "missing_count=0",
        "overclaimed_exactness_count=0",
        "direct_locator_emission_improved_over_reconstruction=partial",
        "line ranges reduced reviewer reconstruction",
        "character offsets did not align with the intended supporting spans",
        "computed quote hashes are mechanically valid but not evidence-valid support handles",
        "SLC-001 source_ref=raw_corpora_sha256:9f9e143429f5842a",
        "SLC-002 source_ref=raw_corpora_sha256:9f9e143429f5842a",
        "SLC-003 source_ref=raw_corpora_sha256:9f9e143429f5842a",
        "raw source text and raw model output are not committed",
        (
            "not validation, product evidence, strategy evidence, financial advice, "
            "live-trading authority, graduation, or architecture"
        ),
    ]:
        assert required in comments
    for quote_hash in [
        "aa1c4a4d9123c3edc6181631661dab1a136e98db5ac3eb5763f5689b66d46a33",
        "5f0e1de0ae75a0815f9b3b33ec8ac3a145dfddf0d1e61a8010e3e7b676cfa577",
        "b68bd9fe88e732e44a1ba2176db1f86ef0ab7a4789a58bf619ab4021c03a0023",
    ]:
        assert quote_hash in comments

    review_text = review_path.read_text()
    for forbidden in [
        "BEGIN RAW SOURCE",
        "DEEPSEEK_API_KEY",
        "sk-",
        "\"api_key\"",
        "\"provider_payload\"",
        "{{APPROVED_SOURCE_TEXT}}",
        "raw_source_text",
        "raw_model_output",
    ]:
        assert forbidden not in review_text
    assert not list(export_dir.glob("run_record.*strict_locator_review*.json"))
    assert not list(export_dir.glob("artifact_envelope.*strict_locator_review*.json"))
    assert not list(export_dir.glob("research_note.*strict_locator_review*.json"))

    manual_content_reviews = [
        review["evaluation"]["evaluation_id"]
        for review in records_by_schema("EvaluationRecord")
        if review["evaluation"]["evaluator_type"] == "manual_content_review"
    ]
    assert CHUNKED_LOCATOR_STRICT_REVIEW_005_EVALUATION_ID in manual_content_reviews

    portfolio = (ROOT / "PORTFOLIO_CURRENT.md").read_text()
    lab_card = (ROOT / "labs" / "chunked_source_grounding" / "LAB_CARD.md").read_text()
    lab_registry = (ROOT / "LAB_REGISTRY.md").read_text()
    for currentness_doc in [portfolio, lab_card, lab_registry]:
        assert "Goal 11E comparison-note update is complete" in currentness_doc
        assert "Goal 12A" in currentness_doc
        assert "line-range-first locator contract" in currentness_doc
        assert "char offsets" in currentness_doc
        assert "proposal-only" in currentness_doc
        assert "generated synthesis metrics" not in currentness_doc.lower()
        assert "run_record.live_pilot_005" not in currentness_doc
    assert "The next proposed step is Goal 11D manual strict locator review" not in (
        portfolio
    )
    assert "No graduated items." in (ROOT / "GRADUATION_LEDGER.md").read_text()


def test_goal11e_comparison_note_records_locator_findings_and_next_fork():
    note = GOAL7G_COMPARISON_NOTE.read_text()

    for required in [
        "chunked_source_grounding_live_pilot_005",
        "chunked_source_grounding_live_pilot_005_strict_locator_review",
        "score `0.58`",
        "pass_fail `fail`",
        "locator candidates reviewed `3`",
        "line ranges `3/3` valid and reviewer-useful",
        "char offsets `3/3` syntactically valid but `0/3` evidence-valid",
        "quote hashes `3` computed locally and mechanically valid but not support-valid",
        "labels: exact `0`, approximate `2`, broad `1`, missing `0`",
        "overclaimed exactness `0`",
        "direct locator emission improved only partially over pilots 003/004",
        "Line-range locator candidates are useful",
        "char-offset and quote-hash candidate workflow is not yet reliable",
        "source-span precision did repeat under strict review in pilots 003/004",
        "direct locator emission is promising only at the line-range level",
        "the next bottleneck is reliable locator granularity, not model parseability",
        "Goal 12A",
        "line-range-first locator contract",
        (
            "model emits line ranges and local review computes offsets/hashes only "
            "after line-range validation"
        ),
    ]:
        assert required in note

    for stale_or_forbidden in [
        "model artifacts do not yet emit canonical line/offset locator candidates",
        "The bounded fork from this comparison is now the completed Goal 11A",
        "Goal 11B admission planning is complete",
        "Goal 11C execution of the admitted source-span locator candidate pilot",
        "whether a future model call can emit canonical locator candidates directly",
        (
            "The admitted future contract should test line-range candidates and "
            "character-offset candidates"
        ),
        "method wins",
        "validated trading",
        "generated synthesis metrics",
        "BEGIN RAW SOURCE",
        "DEEPSEEK_API_KEY",
        "sk-",
        "\"api_key\"",
        "\"provider_payload\"",
        "raw_source_text",
        "raw_model_output",
        "{{APPROVED_SOURCE_TEXT}}",
    ]:
        assert stale_or_forbidden not in note

    portfolio = (ROOT / "PORTFOLIO_CURRENT.md").read_text()
    lab_card = (ROOT / "labs" / "chunked_source_grounding" / "LAB_CARD.md").read_text()
    lab_registry = (ROOT / "LAB_REGISTRY.md").read_text()
    for currentness_doc in [portfolio, lab_card, lab_registry]:
        assert "Goal 11E comparison-note update is complete" in currentness_doc
        assert "Goal 12A" in currentness_doc
        assert "line-range-first locator contract" in currentness_doc
        assert "proposal-only" in currentness_doc
        assert "generated synthesis metrics" not in currentness_doc.lower()
        assert "run_record.live_pilot_005" not in currentness_doc

    assert "The next proposed step is Goal 11E comparison-note update" not in portfolio
    assert all("comparisons" not in path.parts for path in lab_export_paths(ROOT))
    assert synthesize_exports(root=ROOT)["record_count"] == sum(
        1 for _ in all_lab_export_records()
    )
    assert "No graduated items." in (ROOT / "GRADUATION_LEDGER.md").read_text()


def test_goal9e_currentness_docs_are_compressed_routers_not_ledgers():
    readme = (ROOT / "README.md").read_text()
    portfolio = (ROOT / "PORTFOLIO_CURRENT.md").read_text()
    lab_registry = (ROOT / "LAB_REGISTRY.md").read_text()
    graduation = (ROOT / "GRADUATION_LEDGER.md").read_text()
    root_agents = (ROOT / "AGENTS.md").read_text()
    chunked_card = (ROOT / "labs" / "chunked_source_grounding" / "LAB_CARD.md").read_text()

    assert "protocol-valid export records appropriate to their current phase" in readme
    assert f"Current phase: `{CURRENT_PHASE}`" in readme
    assert "Current phase: `milestone-2-live-pilot-recorded`" not in readme
    assert "Goal 12A" in readme
    assert "PORTFOLIO_CURRENT.md" in readme
    assert "LAB_REGISTRY.md" in readme
    assert "live_pilot_method_comparison_001.md" in readme
    assert "export fixture records through the protocol" not in readme
    assert "Only two installable packages exist in milestone one" not in readme

    assert "## Active Federation Labs" in lab_registry
    assert "## Active Scaffold Labs" not in lab_registry
    assert (
        "Labs export protocol-valid records appropriate to their current phase." in
        lab_registry
    )

    assert "phase-appropriate export status" in root_agents
    assert "fixture-export status" not in root_agents

    assert "The Goal 3 live pilot planning packet does not affect graduation status." not in (
        graduation
    )
    assert (
        "Planning packets, run admission updates, proposal-only live export sets, "
        "manual reviews, comparison notes, and research plans do not affect graduation "
        "status by themselves."
    ) in graduation
    assert "No graduated items." in graduation

    for required in [
        "## Current Evidence State",
        "## Current Active Research Thread",
        "live_pilot_method_comparison_001.md",
        "line-range-first locator contract",
        "proposal-only",
    ]:
        assert required in chunked_card
    assert "Current records:" not in chunked_card
    for ledgerish_card_text in [
        "one bounded negative result",
        "narrowed Pro source-grounding runs",
        "strict source-span re-review records now add",
        "for pilots 003 and 004",
    ]:
        assert ledgerish_card_text not in chunked_card

    compressed_docs = [readme, portfolio, lab_registry, chunked_card]
    for doc in compressed_docs:
        assert_currentness_router_not_ledger(doc)
        assert "manual content review has not been completed" not in doc
        assert "no model call or export records exist" not in doc


def test_goal8b_source_span_precision_planning_packet_is_contained_and_current():
    required_files = {
        "admission.md",
        "method_card.proposed.json",
        "experiment_card.proposed.json",
        "evaluator_plan.md",
        "source_privacy_boundary.md",
        "prompt_template.live_pilot_003.md",
        "run_admission_update.md",
        "stop_condition.md",
    }
    assert GOAL8B_PILOT_DIR.exists()
    assert {path.name for path in GOAL8B_PILOT_DIR.iterdir() if path.is_file()} == (
        required_files
    )

    method_card = load_json(GOAL8B_PILOT_DIR / "method_card.proposed.json")
    experiment_card = load_json(GOAL8B_PILOT_DIR / "experiment_card.proposed.json")
    validate_record(method_card)
    validate_record(experiment_card)

    method = method_card["method_card"]
    assert method_card["schema_name"] == "MethodCard"
    assert method_card["schema_version"] == CURRENT_SCHEMA_VERSION
    assert method["method_id"] == GOAL8B_METHOD_ID
    assert method["lab_id"] == "chunked_source_grounding"
    assert method["method_family"] == "chunked_source_grounded_llm_reader_proposed"
    assert "chunked_source_span_precision_proposal" in method["intended_outputs"]
    assert "tighter source-span support hints" in method["intended_outputs"]
    assert "support hint precision labels" in method["intended_outputs"]
    assert "broader judgment abstraction notes" not in method["intended_outputs"]
    assert "broad_segment_refs" in " ".join(method["known_risks"])
    assert "not a completed run" in method["non_goals"]
    assert "not architecture or graduation evidence" in method["non_goals"]

    experiment = experiment_card["experiment_card"]
    assert experiment_card["schema_name"] == "ExperimentCard"
    assert experiment_card["schema_version"] == CURRENT_SCHEMA_VERSION
    assert experiment["experiment_id"] == GOAL8B_EXPERIMENT_ID
    assert experiment["lab_id"] == "chunked_source_grounding"
    assert experiment["benchmark_pack_ids"] == ["text_judgment_v0"]
    assert experiment["method_ids"] == [GOAL8B_METHOD_ID]
    assert experiment["expected_artifact_types"] == [
        "chunked_source_span_precision_proposal"
    ]
    assert "source-span precision" in experiment["research_question"]
    assert "broad segment references to tighter source-span hints" in (
        experiment["research_question"]
    )
    assert "same source excerpt" in experiment["hypothesis"]
    assert "narrowed output contract" in experiment["hypothesis"]

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
    assert "EXPORTS" not in GOAL8B_PILOT_DIR.parts
    assert all("PLANNING" not in path.parts for path in lab_export_paths(ROOT))

    admission = (GOAL8B_PILOT_DIR / "admission.md").read_text()
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
        "This is planning/admission only. No LLM call has been made.",
        "Do not add around stale structure. Rework, replace, delete, or archive it.",
        "Goal 7G found broad_segment_refs and limited_abstraction caveats.",
        "No RunRecord, ArtifactEnvelope, EvaluationRecord, or ResearchNote exists for this pilot.",
        "Do not re-expand the output contract.",
        "Do not add broad judgment abstraction notes.",
        "Do not add full comparison commentary.",
        "Do not ask for a product-like study card.",
    ]:
        assert required_guardrail in admission

    evaluator_plan = (GOAL8B_PILOT_DIR / "evaluator_plan.md").read_text()
    for required in [
        "schema_check",
        "manual_boundary_review",
        "manual_content_review",
        "source-span precision",
        "exact | approximate | broad | missing",
        "comparison value against `chunked_source_grounding_live_pilot_002`",
        "comparison value against `long_context_judgment_live_pilot_001`",
    ]:
        assert required in evaluator_plan

    source_boundary = (GOAL8B_PILOT_DIR / "source_privacy_boundary.md").read_text()
    for required in [
        "raw_corpora_sha256:d8392c58c3b740eb",
        "raw_corpora/selected/live_llm_pilot_001/source.txt",
        "raw_corpora/trader_source_corpus/transcripts/how-to-use-market-profile-start-now-trading-tutorials.txt",
        "Do not commit raw source text.",
        "same approved excerpt as `long_context_judgment_live_pilot_001`",
        "same approved excerpt/hash as `chunked_source_grounding_live_pilot_002`",
    ]:
        assert required in source_boundary

    update = (GOAL8B_PILOT_DIR / "run_admission_update.md").read_text()
    prompt_template_path = GOAL8B_PILOT_DIR / "prompt_template.live_pilot_003.md"
    prompt_template = prompt_template_path.read_text()
    for required in [
        (
            "This admission update defines the executable preflight scope for exactly "
            "one future tiny live LLM pilot run."
        ),
        (
            "It does not by itself authorize execution. Execution requires a separate "
            "Goal 8C instruction."
        ),
        "Provider: DeepSeek API",
        "API format: OpenAI-compatible chat completions",
        "Base URL: `https://api.deepseek.com`",
        "Model: `deepseek-v4-pro`",
        "Reasoning/thinking mode: non-thinking",
        "Benchmark pack: `text_judgment_v0`",
        "Lab: `labs/chunked_source_grounding`",
        "Budget cap: `$3` hard maximum.",
        "No retries unless the call fails before producing output.",
        "Do not silently substitute `deepseek-v4-flash`, `deepseek-chat`, "
        "`deepseek-reasoner`, or any other model.",
        "Outputs from this experiment are proposals until evaluated.",
        "No private/raw source material or provider payloads are committed.",
        "The output contract remains narrow.",
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
    assert "source_linked_claim_table" in prompt_template
    assert "tighter_source_span_support_hints" in prompt_template
    assert "unsupported_claim_report" in prompt_template
    assert "brief_method_failure_notes" in prompt_template
    assert "support_hint_quality" in prompt_template
    assert "exact | approximate | broad | missing" in prompt_template
    assert "mark broad support honestly" in prompt_template
    assert "judgment_abstraction_notes" not in prompt_template
    assert "full comparison commentary" not in prompt_template
    assert "study card" not in prompt_template.lower()

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
        "model_id": "deepseek-v4-pro",
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

    stop_condition = (GOAL8B_PILOT_DIR / "stop_condition.md").read_text()
    assert "`deepseek-v4-pro` is unavailable" in stop_condition
    assert "the output contract expands beyond source-span precision" in stop_condition
    assert "source-span precision cannot be evaluated" in stop_condition

    combined = "\n".join(path.read_text() for path in GOAL8B_PILOT_DIR.iterdir())
    for forbidden in [
        "BEGIN RAW SOURCE",
        "DEEPSEEK_API_KEY=",
        "sk-",
        "\"api_key\"",
        "\"provider_payload\"",
    ]:
        assert forbidden not in combined

    summary = synthesize_exports(root=ROOT)
    assert summary["record_count"] == sum(1 for _ in all_lab_export_records())

    readme = (ROOT / "README.md").read_text()
    portfolio = (ROOT / "PORTFOLIO_CURRENT.md").read_text()
    lab_registry = (ROOT / "LAB_REGISTRY.md").read_text()
    for currentness_doc in [portfolio, lab_registry]:
        assert "source-span precision" in currentness_doc
        assert "generated synthesis metrics" not in currentness_doc.lower()
    assert_currentness_router_not_ledger(readme)
    assert "No graduated items." in (ROOT / "GRADUATION_LEDGER.md").read_text()


def test_goal9a_second_source_span_precision_repeat_planning_packet_is_contained_and_current():
    required_files = {
        "admission.md",
        "method_card.proposed.json",
        "experiment_card.proposed.json",
        "evaluator_plan.md",
        "source_privacy_boundary.md",
        "prompt_template.live_pilot_004.md",
        "run_admission_update.md",
        "stop_condition.md",
    }
    assert GOAL9A_SOURCE_PATH.exists()
    source_text = GOAL9A_SOURCE_PATH.read_text()
    source_word_count = len(source_text.split())
    source_hash = sha256_file(GOAL9A_SOURCE_PATH)
    source_ref = f"raw_corpora_sha256:{source_hash[:16]}"
    assert 300 <= source_word_count <= 1000

    ignore_result = subprocess.run(
        ["git", "check-ignore", "raw_corpora/selected/source_span_precision_repeat_001/source.txt"],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    tracked_result = subprocess.run(
        ["git", "ls-files", "raw_corpora/selected/source_span_precision_repeat_001/source.txt"],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    assert ignore_result.returncode == 0
    assert tracked_result.stdout.strip() == ""

    assert GOAL9A_PILOT_DIR.exists()
    assert {path.name for path in GOAL9A_PILOT_DIR.iterdir() if path.is_file()} == (
        required_files
    )

    method_card = load_json(GOAL9A_PILOT_DIR / "method_card.proposed.json")
    experiment_card = load_json(GOAL9A_PILOT_DIR / "experiment_card.proposed.json")
    validate_record(method_card)
    validate_record(experiment_card)

    method = method_card["method_card"]
    assert method_card["schema_name"] == "MethodCard"
    assert method_card["schema_version"] == CURRENT_SCHEMA_VERSION
    assert method["method_id"] == GOAL9A_METHOD_ID
    assert method["lab_id"] == "chunked_source_grounding"
    assert method["method_family"] == "chunked_source_grounded_llm_reader_proposed"
    assert "second operator-approved source excerpt" in " ".join(method["intended_inputs"])
    assert "chunked_source_span_precision_proposal" in method["intended_outputs"]
    assert "source-linked claim table" in method["intended_outputs"]
    assert "tighter source-span support hints" in method["intended_outputs"]
    assert "support hint precision labels" in method["intended_outputs"]
    assert "broader judgment abstraction notes" not in method["intended_outputs"]
    known_risks = " ".join(method["known_risks"]).lower()
    assert "second source" in known_risks
    assert "repeatability" in known_risks
    assert "source selection" in known_risks
    assert "false precision" in known_risks
    assert "limited abstraction" in known_risks
    assert "not a completed run" in method["non_goals"]
    assert "not architecture or graduation evidence" in method["non_goals"]

    experiment = experiment_card["experiment_card"]
    assert experiment_card["schema_name"] == "ExperimentCard"
    assert experiment_card["schema_version"] == CURRENT_SCHEMA_VERSION
    assert experiment["experiment_id"] == GOAL9A_EXPERIMENT_ID
    assert experiment["lab_id"] == "chunked_source_grounding"
    assert experiment["benchmark_pack_ids"] == ["text_judgment_v0"]
    assert experiment["method_ids"] == [GOAL9A_METHOD_ID]
    assert experiment["expected_artifact_types"] == [
        "chunked_source_span_precision_proposal"
    ]
    assert "second source excerpt" in experiment["research_question"]
    assert "generalize" in experiment["research_question"]
    assert "pilot 003" in experiment["hypothesis"]
    assert "second source" in experiment["hypothesis"]

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
    assert "EXPORTS" not in GOAL9A_PILOT_DIR.parts
    assert all("PLANNING" not in path.parts for path in lab_export_paths(ROOT))

    admission = (GOAL9A_PILOT_DIR / "admission.md").read_text()
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
        "This is planning/admission only. No LLM call has been made.",
        (
            "Goal 8E found source-span precision improved on pilot 003 but still "
            "needs a second-source repeat."
        ),
        "No RunRecord, ArtifactEnvelope, EvaluationRecord, or ResearchNote exists for this pilot.",
        "Do not fall back to the full corpus path.",
        "Do not add broad judgment abstraction notes.",
        "Do not add full comparison commentary.",
        "Do not ask for a product-like study card.",
    ]:
        assert required_guardrail in admission

    evaluator_plan = (GOAL9A_PILOT_DIR / "evaluator_plan.md").read_text()
    for required in [
        "schema_check",
        "manual_boundary_review",
        "manual_content_review",
        "source-span precision",
        "exact | approximate | broad | missing",
        "repeatability value against `chunked_source_grounding_live_pilot_003`",
        "comparison value against the first approved source excerpt",
    ]:
        assert required in evaluator_plan

    source_boundary = (GOAL9A_PILOT_DIR / "source_privacy_boundary.md").read_text()
    for required in [
        source_ref,
        f"Full selected excerpt SHA-256: `{source_hash}`",
        f"Selected excerpt word count: `{source_word_count}`",
        "raw_corpora/selected/source_span_precision_repeat_001/source.txt",
        "raw_corpora/trader_source_corpus/pharm/box trades_999923657.txt",
        "operator-approved second-source excerpt",
        "Do not commit raw source text.",
        "Do not fall back to the full corpus path.",
    ]:
        assert required in source_boundary

    update = (GOAL9A_PILOT_DIR / "run_admission_update.md").read_text()
    prompt_template_path = GOAL9A_PILOT_DIR / "prompt_template.live_pilot_004.md"
    prompt_template = prompt_template_path.read_text()
    for required in [
        (
            "This admission update defines the executable preflight scope for exactly "
            "one future tiny live LLM pilot run."
        ),
        (
            "It does not by itself authorize execution. Execution requires a separate "
            "Goal 9B instruction."
        ),
        "Provider: DeepSeek API",
        "API format: OpenAI-compatible chat completions",
        "Base URL: `https://api.deepseek.com`",
        "Model: `deepseek-v4-pro`",
        "Reasoning/thinking mode: non-thinking",
        "Benchmark pack: `text_judgment_v0`",
        "Lab: `labs/chunked_source_grounding`",
        "Budget cap: `$3` hard maximum.",
        "No retries unless the call fails before producing output.",
        "Do not silently substitute `deepseek-v4-flash`, `deepseek-chat`, "
        "`deepseek-reasoner`, or any other model.",
        "Outputs from this experiment are proposals until evaluated.",
        "No private/raw source material or provider payloads are committed.",
        "The output contract remains the source-span precision contract from pilot 003.",
        source_ref,
        f"Selected excerpt word count: `{source_word_count}`",
    ]:
        assert required in update
    assert "thinking" in update
    assert '"type": "disabled"' in update
    assert "one model-call batch" in update
    assert "Do not fall back to the full corpus path." in update
    assert "authorizes exactly one tiny live LLM pilot run" not in update

    recorded_prompt_hash = re.search(r"Prompt template SHA-256: `([0-9a-f]{64})`", update)
    assert recorded_prompt_hash
    assert recorded_prompt_hash.group(1) == sha256_file(prompt_template_path)
    assert "Prompt Template" in prompt_template
    assert "{{APPROVED_SOURCE_TEXT}}" in prompt_template
    assert "No raw source text is committed in this template." in prompt_template
    assert "second source excerpt" in prompt_template
    assert "source_linked_claim_table" in prompt_template
    assert "tighter_source_span_support_hints" in prompt_template
    assert "unsupported_claim_report" in prompt_template
    assert "brief_method_failure_notes" in prompt_template
    assert "support_hint_quality" in prompt_template
    assert "exact | approximate | broad | missing" in prompt_template
    assert "mark broad support honestly" in prompt_template
    assert "judgment_abstraction_notes" not in prompt_template
    assert "full comparison commentary" not in prompt_template
    assert "study card" not in prompt_template.lower()

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
        "model_id": "deepseek-v4-pro",
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

    stop_condition = (GOAL9A_PILOT_DIR / "stop_condition.md").read_text()
    for required in [
        "selected second-source excerpt is missing",
        "source file is not ignored by git",
        "source file is staged or tracked",
        "`deepseek-v4-pro` is unavailable",
        "the output contract expands beyond source-span precision",
        "source-span precision cannot be evaluated",
        "the run attempts to fall back to the full corpus path",
    ]:
        assert required in stop_condition

    combined = "\n".join(path.read_text() for path in GOAL9A_PILOT_DIR.iterdir())
    for forbidden in [
        "BEGIN RAW SOURCE",
        "DEEPSEEK_API_KEY=",
        "sk-",
        "\"api_key\"",
        "\"provider_payload\"",
    ]:
        assert forbidden not in combined

    summary = synthesize_exports(root=ROOT)
    assert summary["record_count"] == sum(1 for _ in all_lab_export_records())
    assert all("PLANNING" not in path.parts for path in lab_export_paths(ROOT))

    readme = (ROOT / "README.md").read_text()
    portfolio = (ROOT / "PORTFOLIO_CURRENT.md").read_text()
    lab_registry = (ROOT / "LAB_REGISTRY.md").read_text()
    lab_card = (ROOT / "labs" / "chunked_source_grounding" / "LAB_CARD.md").read_text()
    for currentness_doc in [portfolio, lab_registry]:
        assert "second-source" in currentness_doc
        assert "source-span precision" in currentness_doc
        assert "generated synthesis metrics" not in currentness_doc.lower()
    for router_doc in [readme, lab_card]:
        assert_currentness_router_not_ledger(router_doc)
    assert "No graduated items." in (ROOT / "GRADUATION_LEDGER.md").read_text()


def test_goal8c_source_span_precision_live_export_set_is_protocol_valid_and_bounded():
    export_dir = ROOT / "labs" / "chunked_source_grounding" / "EXPORTS"
    live_exports = {path.name: load_json(path) for path in export_dir.glob("*.live_pilot_003.json")}
    assert set(live_exports) == live_pilot_export_names("003")
    for record in live_exports.values():
        validate_record(record)

    run = live_exports["run_record.live_pilot_003.json"]
    artifact = live_exports["artifact_envelope.live_pilot_003.json"]
    evaluation = live_exports["evaluation_record.live_pilot_003.json"]
    note = live_exports["research_note.live_pilot_003.json"]

    assert run["schema_name"] == "RunRecord"
    assert run["schema_version"] == CURRENT_SCHEMA_VERSION
    run_record = run["run_record"]
    assert run_record == {
        "run_id": CHUNKED_SPAN_LIVE_PILOT_RUN_ID,
        "lab_id": "chunked_source_grounding",
        "experiment_id": GOAL8B_EXPERIMENT_ID,
        "method_id": GOAL8B_METHOD_ID,
        "benchmark_pack_id": "text_judgment_v0",
        "source_refs": ["raw_corpora_sha256:d8392c58c3b740eb"],
        "artifact_ids": [CHUNKED_SPAN_LIVE_PILOT_ARTIFACT_ID],
        "evaluation_ids": [CHUNKED_SPAN_LIVE_PILOT_EVALUATION_ID],
        "run_kind": "live_llm_pilot",
        "outcome_polarity": "proposal_only",
        "status": "live_recorded",
    }

    artifact_payload = artifact["artifact"]["payload"]
    assert artifact["artifact"]["artifact_id"] == CHUNKED_SPAN_LIVE_PILOT_ARTIFACT_ID
    assert artifact["artifact"]["artifact_type"] == "chunked_source_span_precision_proposal"
    assert artifact["artifact"]["lab_id"] == "chunked_source_grounding"
    assert artifact["artifact"]["method_id"] == GOAL8B_METHOD_ID
    assert artifact["artifact"]["run_id"] == CHUNKED_SPAN_LIVE_PILOT_RUN_ID
    assert artifact["artifact"]["source_refs"] == run_record["source_refs"]
    assert artifact["artifact"]["posture"]["grounding_status"] == "source_linked"
    assert artifact["artifact"]["posture"]["review_status"] == "self_checked"
    assert artifact["artifact"]["posture"]["validation_status"] == "none"
    assert "proposal_only_not_evaluated" in artifact["artifact"]["blockers"]
    assert "content_review_not_yet_completed" in artifact["artifact"]["blockers"]

    assert artifact_payload["outcome_polarity"] == "proposal_only"
    assert artifact_payload["proposal_only"] is True
    assert artifact_payload["provider_id"] == "deepseek_api"
    assert artifact_payload["api_format"] == "openai_compatible_chat_completions"
    assert artifact_payload["base_url"] == "https://api.deepseek.com"
    assert artifact_payload["model_id"] == "deepseek-v4-pro"
    assert artifact_payload["requested_model_id"] == "deepseek-v4-pro"
    assert artifact_payload["thinking"] == {"type": "disabled"}
    assert artifact_payload["stream"] is False
    assert artifact_payload["tool_routing"] == "none"
    assert artifact_payload["prompt_template_path"] == (
        "labs/chunked_source_grounding/PLANNING/live_llm_pilot_003/"
        "prompt_template.live_pilot_003.md"
    )
    assert artifact_payload["prompt_template_sha256"] == sha256_file(
        GOAL8B_PILOT_DIR / "prompt_template.live_pilot_003.md"
    )
    assert artifact_payload["config_sha256"] == canonical_json_hash(
        extract_json_block(
            (GOAL8B_PILOT_DIR / "run_admission_update.md").read_text(),
            "Canonical Model Config",
        )
    )
    assert artifact_payload["source_metadata"]["source_ref"] == (
        "raw_corpora_sha256:d8392c58c3b740eb"
    )
    assert artifact_payload["source_metadata"]["excerpt_sha256"] == (
        "d8392c58c3b740eb87efd9488fd72da35ef3d09f6a4ee766a9816f672d9b03ee"
    )
    assert artifact_payload["source_metadata"]["excerpt_word_count"] == 650
    assert artifact_payload["source_metadata"]["raw_source_text_committed"] is False
    assert artifact_payload["source_metadata"]["source_path_scope"] == (
        "raw_corpora/selected/live_llm_pilot_001/source.txt"
    )

    assert artifact_payload["token_metadata"]["prompt_tokens"] > 0
    assert artifact_payload["token_metadata"]["completion_tokens"] > 0
    assert artifact_payload["token_metadata"]["total_tokens"] == (
        artifact_payload["token_metadata"]["prompt_tokens"]
        + artifact_payload["token_metadata"]["completion_tokens"]
    )
    assert artifact_payload["cost_metadata"]["budget_cap_usd"] == 3.0
    assert artifact_payload["cost_metadata"]["estimated_cost_usd"] <= 3.0
    assert "billing authority" in artifact_payload["cost_metadata"]["pricing_basis"]

    output_metadata = artifact_payload["model_output_metadata"]
    assert len(output_metadata["raw_model_output_sha256"]) == 64
    assert len(output_metadata["raw_response_sha256"]) == 64
    assert output_metadata["finish_reason"] in {"stop", "length"}
    assert output_metadata["model_output_truncated"] is (
        output_metadata["finish_reason"] == "length"
    )
    assert output_metadata["artifact_type"] == "chunked_source_span_precision_proposal"
    assert set(output_metadata["expected_top_level_keys"]) == {
        "source_linked_claim_table",
        "tighter_source_span_support_hints",
        "unsupported_claim_report",
        "brief_method_failure_notes",
    }
    assert set(output_metadata["expected_top_level_keys_detected"]).issubset(
        set(output_metadata["expected_top_level_keys"])
    )
    if output_metadata["parsed_json_success"]:
        assert set(output_metadata["expected_top_level_keys_detected"]) == set(
            output_metadata["expected_top_level_keys"]
        )
        assert output_metadata["missing_expected_top_level_keys"] == []
        assert "source_span_hint_quality_counts" in output_metadata
        assert set(output_metadata["source_span_hint_quality_counts"]).issubset(
            {"exact", "approximate", "broad", "missing"}
        )
    else:
        assert output_metadata["missing_expected_top_level_keys"] or output_metadata[
            "model_output_truncated"
        ]

    trace_boundary = artifact_payload["trace_storage_boundary"]
    assert trace_boundary == {
        "provider_request_trace": (
            "provider_payloads/chunked_source_grounding_live_pilot_003/request.json"
        ),
        "provider_response_trace": (
            "provider_payloads/chunked_source_grounding_live_pilot_003/response.json"
        ),
        "prompt_trace": "prompt_traces/chunked_source_grounding_live_pilot_003/prompt.txt",
        "model_output_trace": (
            "model_traces/chunked_source_grounding_live_pilot_003/model_output.txt"
        ),
        "traces_committed": False,
    }
    assert artifact_payload["raw_source_text_committed"] is False
    assert artifact_payload["raw_provider_payload_committed"] is False
    assert artifact_payload["raw_prompt_trace_committed"] is False
    assert artifact_payload["raw_model_trace_committed"] is False
    assert artifact_payload["secrets_committed"] is False

    assert evaluation["evaluation"]["evaluation_id"] == CHUNKED_SPAN_LIVE_PILOT_EVALUATION_ID
    assert evaluation["evaluation"]["target_id"] == CHUNKED_SPAN_LIVE_PILOT_ARTIFACT_ID
    assert evaluation["evaluation"]["evaluator_type"] == "manual_boundary_review"
    assert evaluation["evaluation"]["pass_fail"] == "pass"
    assert "method quality was not evaluated" in evaluation["evaluation"]["comments"]

    research_note = note["research_note"]
    assert research_note["note_id"] == CHUNKED_SPAN_LIVE_PILOT_NOTE_ID
    assert research_note["experiment_ids"] == [GOAL8B_EXPERIMENT_ID]
    assert research_note["benchmark_pack_ids"] == ["text_judgment_v0"]
    assert research_note["evidence_disclaimer"] == LIVE_EVIDENCE_DISCLAIMER
    assert any("source-span precision" in item for item in research_note["what_worked"])
    assert any("Goal 8D" in item for item in research_note["do_not_repeat"])

    combined_committed = "\n".join(
        path.read_text()
        for path in [
            export_dir / name
            for name in sorted(live_pilot_export_names("003"))
        ]
    )
    for forbidden in [
        "BEGIN RAW SOURCE",
        "DEEPSEEK_API_KEY",
        "sk-",
        "\"api_key\"",
        "\"provider_payload\"",
        "{{APPROVED_SOURCE_TEXT}}",
    ]:
        assert forbidden not in combined_committed
    assert "study card" not in combined_committed.lower()
    assert "validated trading" not in combined_committed.lower()

    portfolio = (ROOT / "PORTFOLIO_CURRENT.md").read_text()
    lab_registry = (ROOT / "LAB_REGISTRY.md").read_text()
    readme = (ROOT / "README.md").read_text()
    for currentness_doc in [portfolio, lab_registry]:
        assert "source-span precision" in currentness_doc
        assert "Goal 8C instruction" not in currentness_doc
        assert "generated synthesis metrics" not in currentness_doc.lower()
    assert_currentness_router_not_ledger(readme)
    assert "No graduated items." in (ROOT / "GRADUATION_LEDGER.md").read_text()


def test_goal9b_second_source_span_precision_live_export_set_is_protocol_valid_and_bounded():
    export_dir = ROOT / "labs" / "chunked_source_grounding" / "EXPORTS"
    live_exports = {
        path.name: load_json(path) for path in export_dir.glob("*.live_pilot_004.json")
    }
    assert set(live_exports) == live_pilot_export_names("004")
    for record in live_exports.values():
        validate_record(record)

    source_hash = sha256_file(GOAL9A_SOURCE_PATH)
    source_ref = f"raw_corpora_sha256:{source_hash[:16]}"
    source_word_count = len(GOAL9A_SOURCE_PATH.read_text().split())

    run = live_exports["run_record.live_pilot_004.json"]
    artifact = live_exports["artifact_envelope.live_pilot_004.json"]
    evaluation = live_exports["evaluation_record.live_pilot_004.json"]
    note = live_exports["research_note.live_pilot_004.json"]

    assert run["schema_name"] == "RunRecord"
    assert run["schema_version"] == CURRENT_SCHEMA_VERSION
    run_record = run["run_record"]
    assert run_record == {
        "run_id": CHUNKED_SPAN_REPEAT_LIVE_PILOT_RUN_ID,
        "lab_id": "chunked_source_grounding",
        "experiment_id": GOAL9A_EXPERIMENT_ID,
        "method_id": GOAL9A_METHOD_ID,
        "benchmark_pack_id": "text_judgment_v0",
        "source_refs": [source_ref],
        "artifact_ids": [CHUNKED_SPAN_REPEAT_LIVE_PILOT_ARTIFACT_ID],
        "evaluation_ids": [CHUNKED_SPAN_REPEAT_LIVE_PILOT_EVALUATION_ID],
        "run_kind": "live_llm_pilot",
        "outcome_polarity": "proposal_only",
        "status": "live_recorded",
    }

    artifact_payload = artifact["artifact"]["payload"]
    assert artifact["artifact"]["artifact_id"] == (
        CHUNKED_SPAN_REPEAT_LIVE_PILOT_ARTIFACT_ID
    )
    assert artifact["artifact"]["artifact_type"] == (
        "chunked_source_span_precision_proposal"
    )
    assert artifact["artifact"]["lab_id"] == "chunked_source_grounding"
    assert artifact["artifact"]["method_id"] == GOAL9A_METHOD_ID
    assert artifact["artifact"]["run_id"] == CHUNKED_SPAN_REPEAT_LIVE_PILOT_RUN_ID
    assert artifact["artifact"]["source_refs"] == run_record["source_refs"]
    assert artifact["artifact"]["posture"]["grounding_status"] == "source_linked"
    assert artifact["artifact"]["posture"]["review_status"] == "self_checked"
    assert artifact["artifact"]["posture"]["validation_status"] == "none"
    assert "proposal_only_not_evaluated" in artifact["artifact"]["blockers"]
    assert "content_review_not_yet_completed" in artifact["artifact"]["blockers"]

    assert artifact_payload["outcome_polarity"] == "proposal_only"
    assert artifact_payload["proposal_only"] is True
    assert artifact_payload["provider_id"] == "deepseek_api"
    assert artifact_payload["api_format"] == "openai_compatible_chat_completions"
    assert artifact_payload["base_url"] == "https://api.deepseek.com"
    assert artifact_payload["model_id"] == "deepseek-v4-pro"
    assert artifact_payload["requested_model_id"] == "deepseek-v4-pro"
    assert artifact_payload["thinking"] == {"type": "disabled"}
    assert artifact_payload["stream"] is False
    assert artifact_payload["tool_routing"] == "none"
    assert artifact_payload["prompt_template_path"] == (
        "labs/chunked_source_grounding/PLANNING/live_llm_pilot_004/"
        "prompt_template.live_pilot_004.md"
    )
    assert artifact_payload["prompt_template_sha256"] == sha256_file(
        GOAL9A_PILOT_DIR / "prompt_template.live_pilot_004.md"
    )
    assert artifact_payload["config_sha256"] == canonical_json_hash(
        extract_json_block(
            (GOAL9A_PILOT_DIR / "run_admission_update.md").read_text(),
            "Canonical Model Config",
        )
    )
    assert artifact_payload["source_metadata"]["source_ref"] == source_ref
    assert artifact_payload["source_metadata"]["excerpt_sha256"] == source_hash
    assert artifact_payload["source_metadata"]["excerpt_word_count"] == source_word_count
    assert artifact_payload["source_metadata"]["source_path_scope"] == (
        "raw_corpora/selected/source_span_precision_repeat_001/source.txt"
    )
    assert artifact_payload["source_metadata"]["source_origin_scope"] == (
        "raw_corpora/trader_source_corpus/pharm/box trades_999923657.txt"
    )
    assert artifact_payload["source_metadata"]["raw_source_text_committed"] is False

    assert artifact_payload["token_metadata"]["prompt_tokens"] > 0
    assert artifact_payload["token_metadata"]["completion_tokens"] > 0
    assert artifact_payload["token_metadata"]["total_tokens"] == (
        artifact_payload["token_metadata"]["prompt_tokens"]
        + artifact_payload["token_metadata"]["completion_tokens"]
    )
    assert artifact_payload["cost_metadata"]["budget_cap_usd"] == 3.0
    assert artifact_payload["cost_metadata"]["estimated_cost_usd"] <= 3.0
    assert "billing authority" in artifact_payload["cost_metadata"]["pricing_basis"]

    output_metadata = artifact_payload["model_output_metadata"]
    assert output_metadata["artifact_type"] == "chunked_source_span_precision_proposal"
    assert len(output_metadata["raw_model_output_sha256"]) == 64
    assert len(output_metadata["raw_response_sha256"]) == 64
    assert output_metadata["finish_reason"] in {"stop", "length"}
    assert output_metadata["model_output_truncated"] is (
        output_metadata["finish_reason"] == "length"
    )
    assert set(output_metadata["expected_top_level_keys"]) == {
        "source_linked_claim_table",
        "tighter_source_span_support_hints",
        "unsupported_claim_report",
        "brief_method_failure_notes",
    }
    assert set(output_metadata["expected_top_level_keys_detected"]).issubset(
        set(output_metadata["expected_top_level_keys"])
    )
    if output_metadata["parsed_json_success"]:
        assert set(output_metadata["expected_top_level_keys_detected"]) == set(
            output_metadata["expected_top_level_keys"]
        )
        assert output_metadata["missing_expected_top_level_keys"] == []
        assert "source_span_hint_quality_counts" in output_metadata
        assert set(output_metadata["source_span_hint_quality_counts"]).issubset(
            {"exact", "approximate", "broad", "missing"}
        )
    else:
        assert output_metadata["missing_expected_top_level_keys"] or output_metadata[
            "model_output_truncated"
        ]

    trace_boundary = artifact_payload["trace_storage_boundary"]
    assert trace_boundary == {
        "provider_request_trace": (
            "provider_payloads/chunked_source_grounding_live_pilot_004/request.json"
        ),
        "provider_response_trace": (
            "provider_payloads/chunked_source_grounding_live_pilot_004/response.json"
        ),
        "prompt_trace": "prompt_traces/chunked_source_grounding_live_pilot_004/prompt.txt",
        "model_output_trace": (
            "model_traces/chunked_source_grounding_live_pilot_004/model_output.txt"
        ),
        "traces_committed": False,
    }
    assert artifact_payload["raw_source_text_committed"] is False
    assert artifact_payload["raw_provider_payload_committed"] is False
    assert artifact_payload["raw_prompt_trace_committed"] is False
    assert artifact_payload["raw_model_trace_committed"] is False
    assert artifact_payload["secrets_committed"] is False

    assert evaluation["evaluation"]["evaluation_id"] == (
        CHUNKED_SPAN_REPEAT_LIVE_PILOT_EVALUATION_ID
    )
    assert evaluation["evaluation"]["target_id"] == (
        CHUNKED_SPAN_REPEAT_LIVE_PILOT_ARTIFACT_ID
    )
    assert evaluation["evaluation"]["evaluator_type"] == "manual_boundary_review"
    assert evaluation["evaluation"]["pass_fail"] == "pass"
    assert "second-source" in evaluation["evaluation"]["comments"]
    assert "method quality was not evaluated" in evaluation["evaluation"]["comments"]

    research_note = note["research_note"]
    assert research_note["note_id"] == CHUNKED_SPAN_REPEAT_LIVE_PILOT_NOTE_ID
    assert research_note["experiment_ids"] == [GOAL9A_EXPERIMENT_ID]
    assert research_note["benchmark_pack_ids"] == ["text_judgment_v0"]
    assert research_note["evidence_disclaimer"] == LIVE_EVIDENCE_DISCLAIMER
    assert any("second-source" in item for item in research_note["what_worked"])
    assert any("Goal 9C" in item for item in research_note["do_not_repeat"])

    combined_committed = "\n".join(
        path.read_text()
        for path in [
            export_dir / name
            for name in sorted(live_pilot_export_names("004"))
        ]
    )
    for forbidden in [
        "BEGIN RAW SOURCE",
        "DEEPSEEK_API_KEY",
        "sk-",
        "\"api_key\"",
        "\"provider_payload\"",
        "{{APPROVED_SOURCE_TEXT}}",
    ]:
        assert forbidden not in combined_committed
    assert "study card" not in combined_committed.lower()
    assert "validated trading" not in combined_committed.lower()

    portfolio = (ROOT / "PORTFOLIO_CURRENT.md").read_text()
    lab_registry = (ROOT / "LAB_REGISTRY.md").read_text()
    readme = (ROOT / "README.md").read_text()
    lab_card = (ROOT / "labs" / "chunked_source_grounding" / "LAB_CARD.md").read_text()
    for currentness_doc in [portfolio, lab_registry]:
        assert "second-source" in currentness_doc
        assert "source-span precision" in currentness_doc
        assert "no model call or export records exist for that pilot yet" not in (
            currentness_doc
        )
        assert "generated synthesis metrics" not in currentness_doc.lower()
    for router_doc in [readme, lab_card]:
        assert_currentness_router_not_ledger(router_doc)
    assert "No graduated items." in (ROOT / "GRADUATION_LEDGER.md").read_text()


def test_goal9c_second_source_span_precision_content_review_is_bounded():
    export_dir = ROOT / "labs" / "chunked_source_grounding" / "EXPORTS"
    content_review_path = (
        export_dir / manual_content_review_export_name("004")
    )
    assert content_review_path.exists()

    record = load_json(content_review_path)
    validate_record(record)
    assert record["schema_name"] == "EvaluationRecord"
    assert record["schema_version"] == CURRENT_SCHEMA_VERSION

    evaluation = record["evaluation"]
    assert (
        evaluation["evaluation_id"]
        == CHUNKED_SPAN_REPEAT_LIVE_PILOT_CONTENT_REVIEW_EVALUATION_ID
    )
    assert evaluation["lab_id"] == "chunked_source_grounding"
    assert evaluation["target_id"] == CHUNKED_SPAN_REPEAT_LIVE_PILOT_ARTIFACT_ID
    assert evaluation["target_type"] == "artifact"
    assert evaluation["evaluator_id"] == "manual_content_review_live_pilot_004"
    assert evaluation["evaluator_type"] == "manual_content_review"
    assert evaluation["benchmark_pack_id"] == "text_judgment_v0"
    assert evaluation["score"] == pytest.approx(0.86)
    assert evaluation["pass_fail"] == "pass"
    assert evaluation["failure_tags"] == [
        "source_span_precision_repeated",
        "content_review_passed_with_caveats",
        "broad_segment_refs",
        "limited_abstraction",
    ]

    comments = evaluation["comments"]
    for required in [
        "Manual content review only",
        "source grounding",
        "source-span precision",
        "exact/approximate/broad/missing labels",
        "research usefulness",
        "hallucination / unsupported claims",
        "abstraction quality",
        "negative-result value",
        "repeatability value against chunked_source_grounding_live_pilot_003",
        "comparison value against long_context_judgment_live_pilot_001",
        "comparison value against chunked_source_grounding_live_pilot_001",
        "comparison value against chunked_source_grounding_live_pilot_002",
        "comparison value against chunked_source_grounding_live_pilot_003",
        "source-span precision repeated on a second source excerpt",
        "complete parseable JSON",
        "exact labels are warranted for direct source phrasing",
        "the approximate label is warranted for the composite span",
        "unsupported-claim report flags overstatement risks without adding them as claims",
        "still uses broad segment refs rather than canonical offsets",
        "limited broader judgment abstraction",
        "raw source text and raw model output are not committed",
        (
            "not validation, product evidence, strategy evidence, financial advice, "
            "live-trading authority, graduation, or architecture"
        ),
    ]:
        assert required in comments

    manual_content_reviews = [
        record["evaluation"]
        for record in records_by_schema("EvaluationRecord")
        if record["evaluation"]["evaluator_type"] == "manual_content_review"
    ]
    assert sorted(review["evaluation_id"] for review in manual_content_reviews) == [
        CHUNKED_LIVE_PILOT_CONTENT_REVIEW_EVALUATION_ID,
        CHUNKED_PRO_LIVE_PILOT_CONTENT_REVIEW_EVALUATION_ID,
        CHUNKED_SPAN_LIVE_PILOT_CONTENT_REVIEW_EVALUATION_ID,
        CHUNKED_SPAN_STRICT_REVIEW_003_EVALUATION_ID,
        CHUNKED_SPAN_REPEAT_LIVE_PILOT_CONTENT_REVIEW_EVALUATION_ID,
        CHUNKED_SPAN_STRICT_REVIEW_004_EVALUATION_ID,
        CHUNKED_LOCATOR_STRICT_REVIEW_005_EVALUATION_ID,
        LIVE_PILOT_CONTENT_REVIEW_EVALUATION_ID,
    ]
    assert not list(export_dir.glob("run_record.*manual_content_review*.json"))
    assert not list(export_dir.glob("artifact_envelope.*manual_content_review*.json"))
    assert not list(export_dir.glob("research_note.*manual_content_review*.json"))

    combined_committed = "\n".join(
        path.read_text()
        for path in [
            content_review_path,
            ROOT / "PORTFOLIO_CURRENT.md",
            ROOT / "LAB_REGISTRY.md",
            ROOT / "README.md",
            ROOT / "labs" / "chunked_source_grounding" / "LAB_CARD.md",
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
        "{{APPROVED_SOURCE_TEXT}}",
    ]:
        assert forbidden not in combined_committed

    portfolio = (ROOT / "PORTFOLIO_CURRENT.md").read_text()
    lab_registry = (ROOT / "LAB_REGISTRY.md").read_text()
    readme = (ROOT / "README.md").read_text()
    lab_card = (ROOT / "labs" / "chunked_source_grounding" / "LAB_CARD.md").read_text()
    for currentness_doc in [lab_registry]:
        assert "second-source" in currentness_doc
        assert "source-span precision" in currentness_doc
        assert "manual review" in currentness_doc.lower()
        assert "manual content review has not been completed for pilot 004 yet" not in (
            currentness_doc
        )
        assert "generated synthesis metrics" not in currentness_doc.lower()
    for router_doc in [readme, lab_card]:
        assert_currentness_router_not_ledger(router_doc)
    assert "second-source source-span precision repeat" in portfolio
    assert manual_content_review_export_name("004") not in portfolio
    assert "Goal 9C" not in portfolio
    assert "generated synthesis metrics" not in portfolio.lower()
    assert "No graduated items." in (ROOT / "GRADUATION_LEDGER.md").read_text()


def test_goal8d_source_span_precision_manual_content_review_records_precision_result_only():
    export_dir = ROOT / "labs" / "chunked_source_grounding" / "EXPORTS"
    content_review_path = export_dir / manual_content_review_export_name("003")
    assert content_review_path.exists()

    record = load_json(content_review_path)
    validate_record(record)
    assert record["schema_name"] == "EvaluationRecord"
    assert record["schema_version"] == CURRENT_SCHEMA_VERSION

    evaluation = record["evaluation"]
    assert evaluation["evaluation_id"] == CHUNKED_SPAN_LIVE_PILOT_CONTENT_REVIEW_EVALUATION_ID
    assert evaluation["lab_id"] == "chunked_source_grounding"
    assert evaluation["target_id"] == CHUNKED_SPAN_LIVE_PILOT_ARTIFACT_ID
    assert evaluation["target_type"] == "artifact"
    assert evaluation["evaluator_id"] == "manual_content_review_live_pilot_003"
    assert evaluation["evaluator_type"] == "manual_content_review"
    assert evaluation["benchmark_pack_id"] == "text_judgment_v0"
    assert evaluation["score"] == pytest.approx(0.88)
    assert evaluation["pass_fail"] == "pass"
    assert evaluation["failure_tags"] == [
        "source_span_precision_improved",
        "content_review_passed_with_caveats",
        "limited_abstraction",
    ]

    comments = evaluation["comments"]
    for required in [
        "Manual content review only",
        "source grounding",
        "source-span precision",
        "exact/approximate labels are warranted",
        "research usefulness",
        "hallucination / unsupported claims",
        "abstraction quality",
        "negative-result value",
        "comparison value against long_context_judgment_live_pilot_001",
        "comparison value against chunked_source_grounding_live_pilot_001",
        "comparison value against chunked_source_grounding_live_pilot_002",
        "source-span precision improved relative to chunked_source_grounding_live_pilot_002",
        "complete parseable JSON",
        "exact labels are supported by direct source phrasing",
        "approximate labels are honestly marked",
        "no unsupported-claim report was needed for the narrow claims reviewed",
        "still lacks canonical offsets",
        "limited broader judgment abstraction",
        (
            "not validation, product evidence, strategy evidence, financial advice, "
            "live-trading authority, graduation, or architecture"
        ),
    ]:
        assert required in comments
    assert "raw source text and raw model output are not committed" in comments.lower()

    manual_content_reviews = [
        record["evaluation"]
        for record in records_by_schema("EvaluationRecord")
        if record["evaluation"]["evaluator_type"] == "manual_content_review"
    ]
    assert sorted(review["evaluation_id"] for review in manual_content_reviews) == [
        CHUNKED_LIVE_PILOT_CONTENT_REVIEW_EVALUATION_ID,
        CHUNKED_PRO_LIVE_PILOT_CONTENT_REVIEW_EVALUATION_ID,
        CHUNKED_SPAN_LIVE_PILOT_CONTENT_REVIEW_EVALUATION_ID,
        CHUNKED_SPAN_STRICT_REVIEW_003_EVALUATION_ID,
        CHUNKED_SPAN_REPEAT_LIVE_PILOT_CONTENT_REVIEW_EVALUATION_ID,
        CHUNKED_SPAN_STRICT_REVIEW_004_EVALUATION_ID,
        CHUNKED_LOCATOR_STRICT_REVIEW_005_EVALUATION_ID,
        LIVE_PILOT_CONTENT_REVIEW_EVALUATION_ID,
    ]
    assert not list(export_dir.glob("run_record.*manual_content_review*.json"))
    assert not list(export_dir.glob("artifact_envelope.*manual_content_review*.json"))
    assert not list(export_dir.glob("research_note.*manual_content_review*.json"))

    combined_committed = "\n".join(
        path.read_text()
        for path in [
            content_review_path,
            ROOT / "PORTFOLIO_CURRENT.md",
            ROOT / "LAB_REGISTRY.md",
            ROOT / "README.md",
            ROOT / "labs" / "chunked_source_grounding" / "LAB_CARD.md",
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
        "{{APPROVED_SOURCE_TEXT}}",
    ]:
        assert forbidden not in combined_committed

    portfolio = (ROOT / "PORTFOLIO_CURRENT.md").read_text()
    lab_registry = (ROOT / "LAB_REGISTRY.md").read_text()
    readme = (ROOT / "README.md").read_text()
    lab_card = (ROOT / "labs" / "chunked_source_grounding" / "LAB_CARD.md").read_text()
    for currentness_doc in [lab_registry]:
        assert "source-span precision" in currentness_doc
        assert "manual review" in currentness_doc.lower()
        assert "manual content review is still required" not in currentness_doc
        assert "generated synthesis metrics" not in currentness_doc.lower()
    for router_doc in [readme, lab_card]:
        assert_currentness_router_not_ledger(router_doc)
    assert "source-span precision" in portfolio
    assert manual_content_review_export_name("003") not in portfolio
    assert "Goal 8D" not in portfolio
    assert "generated synthesis metrics" not in portfolio.lower()
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
    assert "Scaffold fixture records are not real research evidence." in portfolio
    assert "one tiny method-comparison loop on `text_judgment_v0`" in portfolio
    assert "live_pilot_method_comparison_001.md" in portfolio
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
        "Planning packets, run admission updates, proposal-only live export sets, "
        "manual reviews, comparison notes, and research plans do not affect graduation "
        "status by themselves."
        in graduation
    )
    assert "first Goal 5 proposal-only live pilot export set" not in graduation
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
    assert "Nothing graduates during scaffold milestone one." not in root_agents
    for required in [
        (
            "No item graduates merely because a scaffold fixture, planning packet, "
            "proposal-only live run, manual review, or generated synthesis summary exists."
        ),
        "Future graduation is portfolio-level, not lab-level.",
        (
            "Graduation requires repeated evidence, evaluations, negative-result analysis, "
            "benchmark coverage, known failure modes, cross-lab comparison when applicable, "
            "and explicit ADR."
        ),
        "Until then, methods are experiments, not architecture.",
    ]:
        assert required in root_agents
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
    assert "phase-appropriate export status" in root_agents
    assert "fixture-export status" not in root_agents

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


def test_lab_cards_match_current_live_pilot_posture_without_stale_fixture_language():
    long_context_card = (ROOT / "labs" / "long_context_judgment" / "LAB_CARD.md").read_text()
    chunked_card = (ROOT / "labs" / "chunked_source_grounding" / "LAB_CARD.md").read_text()
    visual_card = (
        ROOT / "labs" / "visual_deictic_understanding" / "LAB_CARD.md"
    ).read_text()

    for active_card in [long_context_card, chunked_card]:
        assert "Status: scaffold fixture exports only" not in active_card
        assert "During scaffold milestone one" not in active_card
        assert "- no live LLM calls" not in active_card
        assert "proposal-only" in active_card
        assert (
            "no validation, product authority, strategy evidence, financial advice, "
            "live-trading authority, graduation, or architecture"
        ) in active_card
        assert (
            "future live runs require live LLM admission and an explicit execution instruction"
            in active_card
        )

    for required in [
        "Status: active live-pilot lab",
        "`long_context_judgment_live_pilot_001`",
        "DeepSeek V4 Flash",
        "manual boundary review passed",
        "manual content review passed with caveats",
    ]:
        assert required in long_context_card

    for required in [
        "Status: active live-pilot lab",
        "## Current Evidence State",
        "## Current Active Research Thread",
        "live_pilot_method_comparison_001.md",
        "line-range-first locator contract",
        "current details live in protocol export records and the comparison note",
    ]:
        assert required in chunked_card
    for removed_ledger_text in [
        "Current records:",
        "one bounded negative result",
        "narrowed Pro source-grounding runs",
        "source-span precision repeat generalized",
        "for pilots 003 and 004",
        "manual content review failed for pilot 001 with score 0.2",
        "manual content review passed for pilot 002 with caveats",
        "manual content review passed for pilot 003 with caveats",
        "manual content review passed for pilot 004 with caveats",
        "evaluation_record.live_pilot_004_manual_content_review.json",
    ]:
        assert removed_ledger_text not in chunked_card

    assert "Status: scaffold fixture exports only" in visual_card
    assert "During scaffold milestone one" not in visual_card
    assert "- no live LLM calls" not in visual_card
    assert "no live visual/deictic pilot has been admitted or run yet" in visual_card
    assert (
        "future live visual/deictic runs require live LLM admission and an explicit "
        "execution instruction"
    ) in visual_card
    assert (
        "no validation, product authority, strategy evidence, financial advice, "
        "live-trading authority, graduation, or architecture"
    ) in visual_card


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
        "active Goal 9 work",
        "supersede active Goal 9 work",
        "Current state: active",
        "Status: active",
        "is protocol authority",
        "is export evidence",
        "graduation evidence",
    ]:
        assert forbidden not in plan
