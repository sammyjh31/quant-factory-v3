# Chunked Source Grounding Live Pilot 005 Evaluator Plan

Status: Goal 11B planning/admission record

This plan defines evaluator intent only. It does not create an EvaluationRecord and does not call an LLM.

---

## Planned Evaluators

Planned post-run evaluator types:

* `schema_check`
* `manual_boundary_review`
* `manual_content_review`

`schema_check` validates record shape only.

`manual_boundary_review` checks containment, proposal-only status, selected-source boundaries, trace boundaries, model/config adherence, and non-authority language. It does not evaluate method quality.

`manual_content_review` may be used after a run to judge whether line/offset locator candidates directly support source-linked claims, whether local review can compute a quote hash from each proposed span, whether locator labels are honest, whether unsupported claims are handled, and whether the locator-candidate contract reduces reconstruction work compared with pilots 003 and 004.

The locator labels for review are:

```text
exact | approximate | broad | missing
```

The review should preserve comparison value against `chunked_source_grounding_live_pilot_003` and `chunked_source_grounding_live_pilot_004`.

---

## Locator Review Question

The expected locator review question is:

```text
Can direct line/offset locator candidates produce metadata-safe computed quote hash handles without relying on reviewer reconstruction from broad segment hints?
```

Review should treat honest `broad` and `missing` labels as more useful than false precision.

Use `overclaimed_exactness` when the model labels a candidate as `exact` but local review shows it is approximate, broad, missing, or unsupported.

No evaluator may create validation, product evidence, strategy evidence, financial advice, live-trading authority, graduation, or architecture.
