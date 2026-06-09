from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CURRENT_PHASE = "milestone-3-method-comparison-recorded"
ROUTER_LEDGER_PATTERNS = (
    r"labs/[^\s`]+/EXPORTS/(?:run_record|artifact_envelope|evaluation_record|research_note)"
    r"\.live_pilot_\d+\.json",
    r"evaluation_record\.live_pilot_\d+_manual_content_review\.json",
    r"manual content review (?:failed|passed) for pilot \d+",
    r"chunked_source_grounding_live_pilot_00[1-5]",
)



def test_repo_governance_contracts_live_outside_scaffold_contract_file():
    scaffold_contracts = (ROOT / "tests" / "test_scaffold_contracts.py").read_text()

    for moved_test in [
        "def test_authority_docs_preserve_scaffold_boundaries",
        "def test_currentness_authority_surface_does_not_creep",
        "def test_agent_guides_encode_v3_operating_boundaries",
        "def test_lab_cards_match_current_live_pilot_posture_without_stale_fixture_language",
        "def test_active_lab_research_questions_match_current_phase_without_fixture_only_claims",
        "def test_lab_readmes_and_package_metadata_match_current_phase_language",
        "def test_agent_checklists_prevent_append_only_drift_and_random_experiments",
        "def test_recursive_contextual_meaning_plan_remains_future_only",
    ]:
        assert moved_test not in scaffold_contracts

    assert len(scaffold_contracts.splitlines()) < 5700


def assert_currentness_router_not_ledger(text: str):
    assert "generated synthesis metrics" not in text.lower()
    assert "provider_payload" not in text
    assert "raw_source_text" not in text
    assert "raw_model_output" not in text
    for pattern in ROUTER_LEDGER_PATTERNS:
        assert not re.search(pattern, text), pattern


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
    assert "## Candidate LLM Methods" in llm_model
    assert "Labs may experiment" in llm_model
    assert "Future labs may experiment" not in llm_model
    assert "Scaffold fixture records are not real research evidence." in portfolio
    assert "one tiny method-comparison loop on `text_judgment_v0`" in portfolio
    assert "live_pilot_method_comparison_001.md" in portfolio
    assert "## Active federation labs" in portfolio
    assert "Milestone-one active labs" not in portfolio
    assert "generated synthesis metrics" not in portfolio.lower()
    assert f"Current phase: `{CURRENT_PHASE}`" in graduation
    assert "Current phase: `milestone-2-live-pilot-recorded`" not in graduation
    assert "Current milestone: `scaffold-v0.1`" not in graduation
    assert f"Current phase: `{CURRENT_PHASE}`" in admission
    assert "Current phase: `milestone-2-live-pilot-recorded`" not in admission
    assert "Current milestone: scaffold-v0.1" not in admission
    assert "No graduated items." in graduation
    assert "## Current Non-Graduation Rule" in graduation
    assert "Nothing can graduate during scaffold milestone one." not in graduation
    assert "A proposal-only live pilot export set is not graduation evidence by itself." in (
        graduation
    )
    assert (
        "Planning packets, run admission updates, proposal-only live export sets, "
        "manual reviews, comparison notes, strict reviews, locator-thread decision "
        "reviews, and research plans do not affect graduation status by themselves."
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
    assert "Superseded by:" in build_prompt
    assert "README.md" in build_prompt
    assert "PORTFOLIO_CURRENT.md" in build_prompt
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


def test_active_lab_research_questions_match_current_phase_without_fixture_only_claims():
    long_context_question = (
        ROOT / "labs" / "long_context_judgment" / "RESEARCH_QUESTION.md"
    ).read_text()
    chunked_question = (
        ROOT / "labs" / "chunked_source_grounding" / "RESEARCH_QUESTION.md"
    ).read_text()
    visual_question = (
        ROOT / "labs" / "visual_deictic_understanding" / "RESEARCH_QUESTION.md"
    ).read_text()

    for active_question in [long_context_question, chunked_question]:
        assert "fixture records only" not in active_question
        assert "No real method result exists yet." not in active_question
        assert "proposal-only live pilot records" in active_question
        assert (
            "do not create validation, product authority, strategy evidence, financial "
            "advice, live-trading authority, graduation, or architecture"
        ) in active_question

    assert "fixture records only" in visual_question
    assert "No real method result exists yet." in visual_question


def test_lab_readmes_and_package_metadata_match_current_phase_language():
    synthesis_pyproject = (
        ROOT / "packages" / "qf_v3_synthesis" / "pyproject.toml"
    ).read_text()
    long_context_readme = (
        ROOT / "labs" / "long_context_judgment" / "README.md"
    ).read_text()
    chunked_readme = (
        ROOT / "labs" / "chunked_source_grounding" / "README.md"
    ).read_text()
    visual_readme = (
        ROOT / "labs" / "visual_deictic_understanding" / "README.md"
    ).read_text()

    assert "protocol export records" in synthesis_pyproject
    assert "scaffold fixture records" not in synthesis_pyproject

    for active_readme in [long_context_readme, chunked_readme]:
        assert "Status: active live-pilot lab" in active_readme
        assert "proposal-only live export records" in active_readme
        assert "This lab contains scaffold fixture records only." not in active_readme
        assert "It does not run live LLM calls" not in active_readme
        assert "future live runs require live LLM admission" in active_readme
        assert (
            "no validation, product authority, strategy evidence, financial advice, "
            "live-trading authority, graduation, or architecture"
        ) in active_readme

    assert "Status: scaffold fixture exports only" in visual_readme
    assert "no live visual/deictic pilot has been admitted or run yet" in visual_readme
    assert "future live visual/deictic runs require live LLM admission" in visual_readme
    assert "It does not run live LLM calls" not in visual_readme


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
