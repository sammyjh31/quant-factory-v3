# LLM Judge Calibration Live Pilot 001 Admission Packet

Status: Goal 16A proposed planning packet
Historical status: pre-run admission record; current run status is owned by `labs/llm_judge_calibration/EXPORTS/run_record.live_pilot_001.json`.
Lab: `llm_judge_calibration`
Experiment: `llm_judge_calibration_live_pilot_001`

This is a proposed live LLM pilot planning record, not a completed run, not research evidence, and not a synthesis export. Execution requires a separately authorized Goal 16B instruction; the operator's milestone-5 directive supplies it.

This packet contains no protocol records and claims no method success.

This packet activates `docs/research-plans/llm-judge-calibration-study.md` per its activation criteria: operator selection (milestone-5 directive), an admission packet, blinding and rubric written before any judge call (this packet), judge config locked in the run admission update, and lab-local work with no protocol changes.

## Hardening / Cleanup Discipline

This packet instantiates the canonical live-pilot packet template for a new lab rather than copying another lab's method assumptions. What it deliberately does not copy: the reading-method contracts of the other labs (this lab reviews artifacts, it does not read trader sources for extraction), and the one-source-scope shape (this study's "source scope" is the fixed set of eleven existing pilots' local traces plus their three approved source excerpts — no new source material is approved by this packet).

## Admission Checklist Coverage

* **Benchmark pack**: `text_judgment_v0` (every ground-truth artifact was produced under it). Known difficulty: judge sycophancy on plausible-looking artifacts. Known failure modes: verdict leakage, rubric drift, sycophantic agreement, judge self-inconsistency, small-sample overconfidence. `v2_lesson_refs`: `report_only_confusion`, `weak_source_grounding`. Metadata safety: the pack contains placeholder identifiers only.
* **MethodCard / ExperimentCard**: `method_card.proposed.json` (`llm_judge_calibration_live_pilot_001_method`), `experiment_card.proposed.json` (`llm_judge_calibration_live_pilot_001`). Research question: can a blinded LLM judge reproduce the operator-lineage review verdicts, and on which axes? Result that would change future behavior: any `delegable` axis enables judge-first review with human spot-checks and unblocks the autonomous-lab-loop entry criteria; a fully `not_delegable` result records that evaluation scaling needs better mechanical checks or tighter rubrics before any loop automation.
* **Evaluator plan**: `evaluator_plan.md` — pre-registered blinding, fixed 17-trial set, agreement metrics, and delegation thresholds, written before any call.
* **Source/privacy boundary**: `source_privacy_boundary.md`.
* **Prompt/template hash plan**: `prompt_template.live_pilot_001.md`, SHA-256 `df384c9162574d5a286790a78a2e9d56be58019af609c52f8e76f0a29ade383e`.
* **Model/config recording plan**: locked in `run_admission_update.md`.
* **Output artifact types**: `judge_agreement_delegation_map_proposal` — the per-axis agreement table and delegation map. Judge verdicts themselves stay in ignored local traces; only metadata-safe agreement statistics are committed.
* **Negative-result value**: a judge that fails calibration is decision-relevant evidence that review cannot yet be delegated; per-axis failures localize what to fix (rubric, mechanical checks, or judge model).
* **Stop condition**: `stop_condition.md`.
* **Budget/secrets**: `$3` hard cap for the whole 17-call batch; `DEEPSEEK_API_KEY` name only; ignored trace paths only.
* **Proposal-only statement**: Outputs from this experiment are proposals until evaluated. They do not create source truth, role support, data truth, validation, strategy evidence, financial advice, product authority, live-trading authority, or architecture.
