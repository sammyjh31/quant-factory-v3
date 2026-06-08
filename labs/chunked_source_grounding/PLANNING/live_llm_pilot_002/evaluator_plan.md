# Chunked Source Grounding Live Pilot 002 Evaluator Plan

Status: Goal 7D planning/admission record

This plan defines evaluator intent only. It does not create an EvaluationRecord and does not call an LLM.

---

## Planned Evaluators

Planned post-run evaluator types:

* `schema_check`
* `manual_boundary_review`
* `manual_content_review`

`schema_check` validates record shape only.

`manual_boundary_review` checks containment, proposal-only status, source/privacy boundaries, trace boundaries, model/config adherence, and non-authority language. It does not evaluate method quality.

`manual_content_review` may be used after a run to judge source grounding, research usefulness, hallucination / unsupported claims, parseability, negative-result value, and comparison value against `long_context_judgment_live_pilot_001` and `chunked_source_grounding_live_pilot_001`.

The review should preserve comparison value against `long_context_judgment_live_pilot_001`.

The review should preserve comparison value against `chunked_source_grounding_live_pilot_001`.

---

## Comparison Value

The review should compare this planned Pro/narrow-contract variant against:

* `long_context_judgment_live_pilot_001`
* `chunked_source_grounding_live_pilot_001`

The expected comparison question is:

```text
Can the Pro/narrow-contract chunked method produce complete parseable source-grounding records, and what does it preserve or lose relative to long-context judgment and the failed Flash contract?
```

No evaluator may create validation, product evidence, strategy evidence, financial advice, live-trading authority, graduation, or architecture.
