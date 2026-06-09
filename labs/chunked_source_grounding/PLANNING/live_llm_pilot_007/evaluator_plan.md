# Chunked Source Grounding Live Pilot 007 Evaluator Plan

Status: Goal 15A planning/admission record

Same evaluator set and rubric as `labs/chunked_source_grounding/PLANNING/live_llm_pilot_006/evaluator_plan.md`: `schema_check`, `manual_boundary_review`, and `manual_content_review` including the strict line-range review with labels `exact | approximate | broad | missing`, `overclaimed_exactness` for unwarranted exact labels, and local offset/quote-hash computation only after line-range validation.

Pilot-007-specific review additions:

* Record reasoning tokens and content tokens separately (thinking-enabled configuration).
* Record entry-cap adherence (at most three source-linked claims, three locator candidates, two unsupported-claim entries, two failure notes per the pilot 006 contract).
* Record whether ASR degradation (missing punctuation, garbled words) affected claim faithfulness or locator review difficulty, as boundary-condition evidence for the graduation ADR.
* Preserve comparison value against pilot 006 (same contract, second source, thinking-off) and long-context pilot 004 (different contract, second source, thinking-on).

This plan defines evaluator intent only; it creates no EvaluationRecord and calls no LLM. No evaluator may create validation, product evidence, strategy evidence, financial advice, live-trading authority, graduation, or architecture.
