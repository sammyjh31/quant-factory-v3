# Source-Span Review Rubric

Status: planning rubric

This rubric makes `manual_content_review` stricter for source-span precision.

## Labels

### exact

Use `exact` only when one contiguous local source span directly supports the claim without stitching multiple distant snippets together.

Required support:

- source ref,
- line range,
- character offset range,
- quote hash,
- reviewer note that the claim does not add meaning beyond the span.

### approximate

Use `approximate` when the claim is supported but paraphrased, compressed, or assembled from nearby source context.

Approximate support may still be useful, but it is not exact.

### broad

Use `broad` when the model gives a segment-level pointer or a wide source area that helps locate the idea but does not identify a precise support span.

`broad_segment_refs` should be used when broad labels are a repeated method limitation.

### missing

Use `missing` when the reviewer cannot identify a source span that supports the claim.

`weak_source_span_precision` should be used if missing or weak support affects the artifact's review value.

## Overclaimed Exactness

Use the phrase overclaimed exactness for the human-readable review caveat.

Mark `overclaimed_exactness` when the model labels support as `exact` but review shows one of these conditions:

- support is stitched from multiple non-contiguous snippets,
- support omits a necessary qualifier,
- support changes likelihood into certainty,
- support relies on surrounding context not included in the claimed span,
- support is broad or approximate rather than exact.

## Canonical Offsets Missing

Use `canonical_offsets_missing` when the artifact remains reviewable but lacks line ranges, character offsets, or quote hashes.

This tag should not mean the artifact failed. It means the review cannot yet make strong source-span precision claims.

## Repeatability

Use `source_span_precision_repeated` only when a later source repeats the positive review pattern from an earlier source without copying its assumptions.

For pilots 003 and 004, repeatability should be judged against:

- parseability,
- source-link reviewability,
- exact/approximate/broad/missing label quality,
- unsupported-claim handling,
- whether canonical offsets remain missing.
