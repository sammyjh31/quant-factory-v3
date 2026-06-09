# Long Context Judgment Live Pilot 004 Evaluator Plan

Status: Goal 14C planning/admission record

Same evaluator set, review questions, labels, and failure-tag vocabulary as `labs/long_context_judgment/PLANNING/live_llm_pilot_003/evaluator_plan.md`: `schema_check`, `manual_boundary_review`, and `manual_content_review` (abstraction half against pilots 001/002; strict line-range half under the pilot 006 rubric with local offsets and quote hashes computed only after line-range validation).

Pilot-004-specific review additions:

* Record reasoning tokens and content tokens separately; record whether the contract finished naturally (`finish_reason=stop`).
* Record entry-cap adherence explicitly: the contract allows at most three principles, four claims, one locator per claim, and two unsupported-claim entries.
* Compare locator support validity against pilot 002's 0/4 and chunked pilot 006's 3/3 on the same source.

This plan defines evaluator intent only; it creates no EvaluationRecord and calls no LLM. No evaluator may create validation, product evidence, strategy evidence, financial advice, live-trading authority, graduation, or architecture.
