# Chunked Source Grounding Live Pilot 001 Evaluator Plan

Status: Goal 7A planning/admission record

This plan defines evaluator intent only. It does not create an EvaluationRecord and does not call an LLM.

---

## Planned Evaluators

Planned post-run evaluator types:

* `schema_check`
* `manual_boundary_review`
* `manual_content_review`

`schema_check` validates record shape only.

`manual_boundary_review` checks containment, proposal-only status, source/privacy boundaries, trace boundaries, and non-authority language. It does not evaluate method quality.

`manual_content_review` may be used after a run to judge source grounding, research usefulness, hallucination / unsupported claims, abstraction quality, negative-result value, and comparison value against `long_context_judgment`.

---

## Comparison Value

The review should compare this method against `long_context_judgment_live_pilot_001` on the same source ref and benchmark pack.

The expected comparison question is:

```text
Does chunked/source-grounded reading preserve exact support better, and what broader trading-judgment abstraction does it lose?
```

No evaluator may create validation, product evidence, strategy evidence, financial advice, live-trading authority, graduation, or architecture.
