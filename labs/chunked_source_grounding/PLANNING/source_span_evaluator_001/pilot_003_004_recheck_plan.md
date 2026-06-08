# Pilot 003 / 004 Recheck Plan

Status: planning only

Goal 10B should perform a stricter manual re-review of:

- `chunked_source_grounding_live_pilot_003`
- `chunked_source_grounding_live_pilot_004`

Goal 10A does not perform that review.

## Inputs To Inspect Locally

Inspect existing committed records:

- pilot 003 ArtifactEnvelope,
- pilot 003 manual content-review EvaluationRecord,
- pilot 004 ArtifactEnvelope,
- pilot 004 manual content-review EvaluationRecord,
- current method comparison note.

Inspect ignored local material only as needed:

- pilot 003 source file,
- pilot 004 source file,
- pilot 003 model output trace,
- pilot 004 model output trace,
- prompt traces and provider metadata.

Do this without copying raw source text, without copying raw model output, and without committing raw traces.

## Recheck Steps

1. Build a local-only source locator table for each reviewed support hint.
2. Map each model support hint to source ref, line range, character offsets, and quote hash.
3. Compare existing support labels against canonical offsets.
   This means: compare existing support labels against canonical offsets before changing any review conclusion.
4. Mark each reviewed support hint as `exact`, `approximate`, `broad`, or `missing`.
5. Record any `overclaimed_exactness`, `broad_segment_refs`, `weak_source_span_precision`, or `canonical_offsets_missing`.
6. Compare pilot 003 and pilot 004 under the same rubric.
7. Decide whether the stricter review changes the current comparison note.

## Expected Output For Goal 10B

Goal 10B may create manual_content_review EvaluationRecord records only if the existing protocol can represent the stricter review honestly.

Possible target records:

- stricter manual re-review for pilot 003 artifact,
- stricter manual re-review for pilot 004 artifact.

No RunRecord, ArtifactEnvelope, ResearchNote, live-run admission packet, protocol change, or synthesis feature is implied by this plan.
