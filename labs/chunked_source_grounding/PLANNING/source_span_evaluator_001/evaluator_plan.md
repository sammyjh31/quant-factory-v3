# Goal 10A Source-Span Evaluator Plan

Status: planning only

This is Goal 10A source-span evaluator planning for `chunked_source_grounding`.

Do not call an LLM.
Do not run another model.
Do not create EXPORTS records.
Do not create a live-run admission packet.
Do not create MethodCard or ExperimentCard records.
Do not create RunRecord, ArtifactEnvelope, EvaluationRecord, or ResearchNote records.
Do not change protocol.
Do not add synthesis features.
Do not add shared scripts/helpers.
Do not add new benchmark packs.
Do not graduate anything.

## Purpose

Goal 9D found that source-span precision repeated on a second source excerpt, but both reviewed source-span precision pilots still lack canonical offsets and rely on broad segment refs. Goal 10A plans a stricter evaluator/review method before any further model calls.

Research question:

```text
How can manual_content_review become stricter about source-span precision without changing protocol yet?
```

## Evaluation Target

The first strict re-review should target pilots 003 and 004:

- `chunked_source_grounding_live_pilot_003`
- `chunked_source_grounding_live_pilot_004`

The re-review should inspect existing proposal-only artifacts, local ignored source files, local ignored prompt/model traces if needed, and existing manual content-review records.

## Canonical Source-Span Precision

canonical source-span precision means that each model-proposed support hint can be checked against a local source locator that includes:

1. source ref,
2. line ranges,
3. character offsets,
4. quote hashes,
5. reviewer judgment for `exact`, `approximate`, `broad`, or `missing`.

Line ranges provide human inspectability. Character offsets provide stricter reproducibility. Quote hashes allow a committed review to refer to a span without committing raw source text.

## Evaluator Type

Existing `manual_content_review` can honestly represent this stricter review if the EvaluationRecord comments state that it is a stricter source-span re-review and include metadata-safe findings only.

The existing EvaluationRecord can hold the stricter review result unless repeated reviews prove that structured source-span fields are needed.

No new `evaluator_type` is needed for Goal 10A.

## Failure Tags

Reuse or add locally as supported by review:

- `broad_segment_refs`
- `weak_source_span_precision`
- `overclaimed_exactness`
- `canonical_offsets_missing`
- `source_span_precision_repeated`
- `content_review_passed_with_caveats`

These are EvaluationRecord failure tags, not protocol fields.

## Future Protocol Trigger

A future protocol change may be warranted only after repeated reviews show that source-span evidence needs structured fields that cannot be represented safely in existing `EvaluationRecord` comments, `failure_tags`, or artifact payload metadata.

Possible future candidates:

- canonical source locator object,
- source-span evidence table,
- quote-hash field,
- canonical offset range field.

None are added in Goal 10A.

## Next Live-Run Trigger

The next live model run becomes worthwhile only if stricter review shows what the model should change, such as:

- split composite claims before assigning exact support,
- return line-range candidates,
- return quote-hash candidates,
- avoid exact labels when support spans are stitched from multiple snippets,
- preserve broader abstraction only after grounding passes.
