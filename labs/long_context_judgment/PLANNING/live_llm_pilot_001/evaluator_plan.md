# Evaluator Plan

Status: proposed planning document

This is a proposed live LLM pilot planning record. It is not a completed run, not research evidence, and not a synthesis export.

The authorized Goal 5 live run now has a boundary-only EvaluationRecord under `labs/long_context_judgment/EXPORTS/`. No method success is claimed.

---

## Evaluators

### `schema_check`

Purpose:

```text
Confirm that post-run records validate against protocol schemas.
```

Limits:

```text
Schema validity proves shape only. It does not prove method quality, source truth, trading value, or strategy validity.
```

### `manual_boundary_review`

Purpose:

```text
Review that raw source text, provider payloads, prompt traces, model traces, and secrets were not committed, and that the output remains proposal-only.
```

Limits:

```text
Manual boundary review is not a method-quality review, source-truth review, or trading-validity review.
```

---

## Planned Failure Tags

* `weak_source_grounding`
* `over_abstracted_teacher_intent`
* `unsupported_claim`
* `ambiguous_source_span`
* `not_useful_for_judgment_reuse`

---

## Excluded Evaluators

No `llm_judge_placeholder` is planned for the first live pilot. Adding an LLM judge requires a separate admission update with model/config recording and calibration limits.
