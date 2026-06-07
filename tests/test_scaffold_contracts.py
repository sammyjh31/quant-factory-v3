from __future__ import annotations

import inspect
import json
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
GOAL3_PILOT_DIR = (
    ROOT / "labs" / "long_context_judgment" / "PLANNING" / "live_llm_pilot_001"
)
GOAL3_METHOD_ID = "long_context_judgment_live_pilot_001_method"
GOAL3_EXPERIMENT_ID = "long_context_judgment_live_pilot_001"


def load_json(path: Path):
    return json.loads(path.read_text())


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
    assert len(export_paths) == 3
    expected_labs = {
        "chunked_source_grounding",
        "long_context_judgment",
        "visual_deictic_understanding",
    }
    assert {path.parents[1].name for path in export_paths} == expected_labs
    for path in export_paths:
        records = list(iter_records(path))
        assert records
        for record in records:
            validate_record(record)
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
    experiment_ids = {
        record["experiment_card"]["experiment_id"] for record in records_by_schema("ExperimentCard")
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
        disclaimer = record["research_note"]["scaffold_disclaimer"]
        assert disclaimer == (
            "This is a scaffold fixture for protocol validation, not real research evidence."
        )

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
        "No LLM call has been made.",
        "No output artifact has been produced.",
        "No evaluation result exists.",
        "No method success is claimed.",
        "not a synthesis export",
    ]:
        assert required_guardrail in admission

    summary = synthesize_exports(root=ROOT)
    assert summary["record_count"] == 27
    assert GOAL3_METHOD_ID not in summary["methods"]

    portfolio = (ROOT / "PORTFOLIO_CURRENT.md").read_text()
    lab_registry = (ROOT / "LAB_REGISTRY.md").read_text()
    assert GOAL3_EXPERIMENT_ID in portfolio
    assert GOAL3_EXPERIMENT_ID in lab_registry
    assert "No live LLM experiment has run." in portfolio
    assert "not in `EXPORTS/`" in lab_registry


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
    assert "future live LLM runs" in readme
    assert "Future labs may experiment" in llm_model
    assert "There is no real research evidence in scaffold milestone one." in portfolio
    assert "generated synthesis metrics" not in portfolio.lower()
    assert "No graduated items." in graduation
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
        "read-only with respect to labs, benchmarks, protocol schemas, and currentness docs"
        in synthesis_agents
    )
    assert "Generated outputs are non-authoritative and ignored by default." in synthesis_agents
    assert "Synthesis must not imply a winner through ordering" in synthesis_agents
    assert "explicit comparative evaluation path" in synthesis_agents

    assert "Labs are playgrounds for methodological exploration." in labs_agents
    assert "Do not turn a lab method into shared architecture." in labs_agents
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
        "why this does not require shared architecture yet",
        "why this does not require protocol changes yet",
    ]:
        assert required in new_experiment
