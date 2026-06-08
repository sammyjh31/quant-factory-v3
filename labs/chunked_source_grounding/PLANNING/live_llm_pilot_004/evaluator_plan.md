# Chunked Source Grounding Live Pilot 004 Evaluator Plan

Status: Goal 9A planning/admission record

This plan defines evaluator intent only. It does not create an EvaluationRecord and does not call an LLM.

---

## Planned Evaluators

Planned post-run evaluator types:

* `schema_check`
* `manual_boundary_review`
* `manual_content_review`

`schema_check` validates record shape only.

`manual_boundary_review` checks containment, proposal-only status, selected-source boundaries, trace boundaries, model/config adherence, and non-authority language. It does not evaluate method quality.

`manual_content_review` may be used after a run to judge source-span precision, source grounding, hallucination / unsupported claims, parseability, output-contract fit, negative-result value, repeatability value against `chunked_source_grounding_live_pilot_003`, and comparison value against the first approved source excerpt.

The support hint quality labels for review are:

```text
exact | approximate | broad | missing
```

The review should preserve repeatability value against `chunked_source_grounding_live_pilot_003`.

The review should preserve comparison value against the first approved source excerpt.

---

## Precision Review Question

The expected precision question is:

```text
Can the source-span precision variant remain complete and honest on a second source excerpt while marking broad or missing support honestly?
```

Review should treat honest `broad` and `missing` labels as more useful than false precision.

No evaluator may create validation, product evidence, strategy evidence, financial advice, live-trading authority, graduation, or architecture.
