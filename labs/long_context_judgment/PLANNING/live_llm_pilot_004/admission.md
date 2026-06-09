# Long Context Judgment Live Pilot 004 Admission Packet

Status: Goal 14C proposed planning packet
Historical status: pre-run admission record; current run status is owned by `labs/long_context_judgment/EXPORTS/run_record.live_pilot_004.json`.
Lab: `long_context_judgment`
Experiment: `long_context_judgment_live_pilot_004`

This is a proposed live LLM pilot planning record, not a completed run, not research evidence, and not a synthesis export. Execution requires a separately authorized Goal 14D instruction; the operator's milestone-4 goal directive supplies it for this evidence chain.

This packet contains no protocol records and claims no method success.

## Hardening / Cleanup Discipline And Delta From Pilot 003

Pilot 003 established that the provider counts reasoning tokens against `max_tokens`, returning empty content at a 4000-token cap. This packet changes exactly one variable against pilot 003:

1. **Output cap raised from `4000` to `12000` tokens**, sized for reasoning plus the full contract per the pilot 003 research note. Thinking stays enabled (operator direction); the contract stays byte-identical (verified) to pilots 002/003.

Everything else — research question, source scope, evaluators, privacy boundary, exclusions — is owned by the pilot 003 packet files and carries over unchanged.

## Admission Checklist Coverage

* **Benchmark pack**: `text_judgment_v0`, same difficulty/failure modes/`v2_lesson_refs`/metadata safety as pilots 002/003, plus the pilot 003 lesson: reasoning shares the output budget.
* **MethodCard / ExperimentCard**: `method_card.proposed.json` (`long_context_judgment_live_pilot_004_method`), `experiment_card.proposed.json` (`long_context_judgment_live_pilot_004`). The experiment asks the pilot 003 question with a viable cap: with reasoning headroom, can the grounded contract produce support-valid line-range locators while preserving pilot 002's abstraction quality? Result that would change future behavior: support-valid locators with preserved abstraction make grounded long-context supporting cross-method evidence for the line-range-first graduation nomination; another locator failure with no cap pressure and thinking enabled disconfirms the single-pass grounded variant and steers the lab to a two-pass split.
* **Evaluator plan**: same three evaluators and pilot-003 additions (`labs/long_context_judgment/PLANNING/live_llm_pilot_003/evaluator_plan.md`); strict review under the pilot 006 rubric; comparison value preserved against pilots 002, 003, and chunked 006.
* **Source/privacy boundary**: identical to `labs/long_context_judgment/PLANNING/live_llm_pilot_003/source_privacy_boundary.md` (same second-source excerpt `raw_corpora_sha256:9f9e143429f5842a`, 945 words, 140 lines, local-only, no corpus fallback).
* **Prompt/template hash plan**: `prompt_template.live_pilot_004.md`, SHA-256 `162b8ab50f960183776d48ff4d2032fb7d022a1e537137d247f8d0bd8c409c5e`, body byte-identical to pilots 002/003.
* **Model/config recording plan**: locked in `run_admission_update.md` in this packet.
* **Output artifact types**: `grounded_long_context_judgment_proposal`, same five sections, same exclusions (no model-emitted offsets or hashes).
* **Negative-result value**: a locator failure here is the clean disconfirmation pilot 002 could not provide (no cap pressure, thinking enabled); an empty-content repeat at 12000 tokens would mark thinking mode itself as unfit for this contract.
* **Stop condition**: `stop_condition.md` in this packet.
* **Budget/secrets**: `$3` hard cap; `DEEPSEEK_API_KEY` name only; ignored trace paths only.
* **Proposal-only statement**: Outputs from this experiment are proposals until evaluated. They do not create source truth, role support, data truth, validation, strategy evidence, financial advice, product authority, live-trading authority, or architecture.
