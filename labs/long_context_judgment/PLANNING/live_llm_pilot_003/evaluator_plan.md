# Long Context Judgment Live Pilot 003 Evaluator Plan

Status: Goal 14A planning/admission record

Same evaluator set, review questions, labels, and failure-tag vocabulary as `labs/long_context_judgment/PLANNING/live_llm_pilot_002/evaluator_plan.md`: `schema_check`, `manual_boundary_review`, and `manual_content_review` (abstraction half against pilots 001/002; strict line-range half under the pilot 006 rubric).

Pilot-003-specific review additions:

* Record whether locator pointing changed relative to pilot 002's 0/4 support-valid result now that cap pressure is removed and thinking is enabled.
* Record completion-token headroom: whether the contract finished naturally below the 4000-token cap (`finish_reason=stop`), which retroactively confirms or weakens the pilot 002 cap-pressure confound.
* Use `unsupported_principle_link` when a judgment principle cites a supporting claim that does not support it, and `overclaimed_exactness` per the pilot 006 rubric.

This plan defines evaluator intent only; it creates no EvaluationRecord and calls no LLM. No evaluator may create validation, product evidence, strategy evidence, financial advice, live-trading authority, graduation, or architecture.
