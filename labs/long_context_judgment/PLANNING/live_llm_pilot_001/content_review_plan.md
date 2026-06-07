# Live LLM Pilot 001 Content Review Plan

Status: Goal 6 content-review planning record

This is a planning document for content-review and evaluator-calibration work after the first admitted live LLM pilot, with the Goal 6C-B export boundary recorded.

Do not call an LLM.
Do not run another model.
Do not create new live-run records.
Goal 6C-B creates exactly one `manual_content_review` EvaluationRecord.
Do not graduate anything.
Do not commit raw model output, raw provider payload, raw prompt trace, raw source text, or secrets.

This plan does not claim that the first live pilot produced useful trading judgment. It plans how to evaluate that question without turning proposal output into validation, financial advice, live-trading authority, product evidence, or architecture.

Scope: source-grounding review, usefulness review, hallucination / unsupported-claim review, abstraction-quality review, and negative-result value.

---

## Review Target

Target artifact:

```text
labs/long_context_judgment/EXPORTS/artifact_envelope.live_pilot_001.json
```

Target run:

```text
long_context_judgment_live_pilot_001_run
```

Target source ref:

```text
raw_corpora_sha256:d8392c58c3b740eb
```

Local ignored traces available for reviewer inspection:

```text
model_traces/live_llm_pilot_001/model_output.txt
provider_payloads/live_llm_pilot_001/response.json
prompt_traces/live_llm_pilot_001/prompt.txt
```

Those traces are local-only inspection material. They are not authority, not exports, and not material to copy into currentness docs.

Committed record metadata says the model returned:

* two judgment-principle proposal items,
* four source-grounded claim items,
* two unsupported-claim report items,
* and two method-failure note items.

These counts are inspection metadata only. They do not imply quality.

---

## Source-Grounding Review

The next reviewer should inspect the ignored model output and source excerpt locally and answer:

* Does each proposed principle have a source-span hint specific enough for a human to find the supporting passage?
* Does each source-grounded claim preserve the source meaning, or does it change the teacher's intent?
* Does the model expose uncertainty when the source is vague?
* Does the model avoid claiming source truth beyond the excerpt?
* Which claims cannot be checked without a more exact span or quote policy?

Expected failure tags:

* `ambiguous_source_span`
* `weak_source_grounding`
* `source_meaning_shift`
* `unsupported_claim`

---

## Usefulness Review

The next reviewer should judge usefulness as research utility only, not trading validity.

Review questions:

* Would a human researcher understand what judgment principle the model is proposing?
* Is the proposal reusable as a study or review candidate?
* Is it too generic to help future method comparison?
* Does it preserve enough context to compare long-context reading against chunked/source-grounded reading later?
* Does it identify what a future evaluator should check?

Do not score profitability, edge, live-market actionability, trade setup quality, or strategy validity.

Expected failure tags:

* `too_generic`
* `weak_research_utility`
* `missing_context`
* `not_useful_for_judgment_reuse`

---

## Hallucination / Unsupported-Claim Review

The next reviewer should inspect whether the model separates supported and unsupported material.

Review questions:

* Are unsupported-claim reports actually unsupported by the source excerpt?
* Did the model miss any major unsupported claim in its own output?
* Did it introduce trading instructions, product claims, validation claims, financial advice, or architecture claims?
* Did it describe an inference as a source-grounded fact?
* Did it preserve uncertainty around interpretation?

Expected failure tags:

* `unsupported_claim`
* `missed_unsupported_claim`
* `overclaimed_grounding`
* `authority_leak`

---

## Abstraction-Quality Review

The next reviewer should inspect whether the model abstracted the source into a useful principle without flattening it.

Review questions:

* Does the abstraction keep the trader's conditional logic?
* Does it preserve relevant context, caveats, and failure conditions?
* Does it over-compress the source into generic trading advice?
* Does it preserve the distinction between market observation, process advice, and strategy claim?
* Would the abstraction help compare long-context reading with a more source-grounded method?

Expected failure tags:

* `over_abstracted_teacher_intent`
* `lost_conditionality`
* `generic_advice`
* `category_blur`

---

## Evaluator Representation Decision

Schema 0.1.2 adds protocol support for `manual_content_review`.

EvaluationRecord can now honestly represent a completed manual content review for this pilot after a separately authorized content-review export task.

Reason:

* `manual_boundary_review` is already used for containment checks and should not be overloaded with content-quality judgment.
* `schema_check` validates record shape only.
* `human_placeholder` is a placeholder evaluator type, not a completed manual review.
* `llm_judge_placeholder` is explicitly not a live judge and is not appropriate for Goal 6.

The protocol change was adding `manual_content_review` to the existing EvaluationRecord `evaluator_type` enum. No new protocol object is needed for the next step unless repeated runs prove the current EvaluationRecord shape cannot carry the needed review comments, score, pass/fail status, and failure tags.

Goal 6C-A did not create the content-review export.

Goal 6C-B is the separately authorized content-review export task.

The authorized content-review export task preserves these boundaries:

1. inspect ignored local model/source materials without committing raw text or traces,
2. create exactly one `manual_content_review` EvaluationRecord as authorized,
3. keep the review proposal-only and non-authoritative,
4. avoid creating any new RunRecord, ArtifactEnvelope, ResearchNote, protocol object, or graduation claim.

---

## Negative-Result Value

A weak or failed content review is still useful if it shows:

* long-context output loses exact grounding,
* unsupported-claim reports are too shallow,
* the prompt encourages generic advice,
* the artifact needs exact quote-span policy before review,
* or the evaluator cannot distinguish quality levels consistently.

A negative result should steer the next milestone toward evaluator quality, not toward more live calls.

---

## Next Experiment Decision

The next experiment should improve evaluator quality before running a second method.

Rationale:

* Goal 5 proved the harness can contain a live call.
* The current bottleneck is judging whether the output is useful.
* More model calls would create more proposal records without a reliable content-review path.
* Manual review should come before an LLM judge because one live pilot is too early to delegate evaluation to another model.

Current sequence:

```text
Goal 6C-A: add protocol support for one manual content-review evaluator.
Goal 6C-B: export exactly one manual content-review EvaluationRecord.
Goal 7: decide whether to run a second method or improve evaluator calibration further.
```

No single content review should create validation, graduation, product authority, strategy evidence, financial advice, live-trading authority, or architecture.
