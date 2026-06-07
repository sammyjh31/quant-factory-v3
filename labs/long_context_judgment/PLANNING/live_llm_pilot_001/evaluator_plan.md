# Evaluator Plan

Status: proposed planning document

This is a proposed live LLM pilot planning record. It is not a completed run, not research evidence, and not a synthesis export.

No LLM call has been made. No output artifact has been produced. No evaluation result exists. No method success is claimed.

---

## Planned Evaluators

### `schema_check`

Purpose:

```text
Confirm that any future post-run records validate against protocol schemas.
```

Limits:

```text
Schema validity proves shape only. It does not prove method quality, source truth, trading value, or strategy validity.
```

### `human_placeholder`

Purpose:

```text
Review future output artifacts for source grounding, teacher-intent preservation, unsupported claims, and over-abstraction.
```

Limits:

```text
Human placeholder review is a planned evaluation surface. It is not an evaluation result until a separately approved live run produces artifacts.
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
