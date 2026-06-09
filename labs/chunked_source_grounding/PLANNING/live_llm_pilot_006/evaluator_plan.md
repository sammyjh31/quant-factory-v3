# Chunked Source Grounding Live Pilot 006 Evaluator Plan

Status: Goal 12B planning/admission record

This plan defines evaluator intent only. It does not create an EvaluationRecord and does not call an LLM.

---

## Planned Evaluators

Planned post-run evaluator types:

* `schema_check`
* `manual_boundary_review`
* `manual_content_review`

`schema_check` validates record shape only.

`manual_boundary_review` checks containment, proposal-only status, selected-source boundaries, trace boundaries, model/config adherence, line-range-only output boundaries, and non-authority language. It does not evaluate method quality.

`manual_content_review` may be used after a run to judge whether line-range locator candidates support source-linked claims, whether the proposed line range directly supports the claim, whether local review can compute character offsets and a computed quote hash after accepting the line range, whether locator labels are honest, whether unsupported claims are handled, and whether the line-range-first contract reduces reconstruction work compared with pilot 005.

The locator labels for review are:

```text
exact | approximate | broad | missing
```

The review should preserve comparison value against `chunked_source_grounding_live_pilot_005`.

---

## Line-Range Review Question

The expected line-range review question is:

```text
Can direct line-range locator candidates produce reviewable support regions before local tooling computes any character offsets or computed quote hash handles?
```

Review should treat honest `broad` and `missing` labels as more useful than false precision.

Use `overclaimed_exactness` when the model labels a candidate as `exact` but local review shows it is approximate, broad, missing, or unsupported.

There is no new evaluator type in Goal 12B.

No evaluator may create validation, product evidence, strategy evidence, financial advice, live-trading authority, graduation, or architecture.
