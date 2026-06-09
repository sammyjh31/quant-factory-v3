# Goal 12A Line-Range-First Locator Contract Plan

Status: planning only

This is Goal 12A line-range-first locator contract planning for the `chunked_source_grounding` lab.

No LLM call is authorized by this file. No live-run admission packet is created by Goal 12A.

## Purpose

Pilot 005 moved the bottleneck from parseability to locator granularity. The strict locator review found that line ranges worked, while character offsets and quote-hash support did not.

Goal 12A plans a narrower output contract:

```text
Can a chunked/source-grounded model emit useful line-range locator candidates while local review computes offsets and quote hashes only after line-range validation?
```

This is a planning artifact. It is not research evidence, not a synthesis export, not validation, not graduation, and not architecture.

## Pilot 005 Lesson

Character offsets did not provide support-valid spans in pilot 005. Quote hashes computed from bad offsets were mechanically valid but not support-valid.

The next contract should not rerun the broader pilot 005 locator contract unchanged. It should preserve what worked: line-range regions that helped reviewers reduce reconstruction.

## Line-Range Locator Candidate Fields

The future model prompt should ask for line-range locator candidates only.

Allowed model-emitted fields:

- `claim_id`
- `source_ref`
- `candidate_line_start`
- `candidate_line_end`
- `locator_confidence`
- `locator_label: exact | approximate | broad | missing`
- short support rationale

The model should not emit `candidate_char_start`.
The model should not emit `candidate_char_end`.
The model should not emit `quote_hash_candidate`.
The model should not emit cryptographic hashes.
The model should not emit raw source text.

## Local Postprocessing Boundary

Local review owns validation of candidate line ranges. Character offsets and quote hashes are downstream computed values only after line-range support has been accepted.

The model may propose a support region. It must not claim canonical offsets or source hashes.

## Protocol Fit

ArtifactEnvelope.payload can honestly hold line-range locator candidates as lab-local payload details.

No protocol change is needed for Goal 12A. The shared protocol does not need new fields for this planning step, and a future run can keep lab-specific locator details inside `ArtifactEnvelope.payload`.

## Non-Authority Boundary

This contract plan does not create product evidence, strategy evidence, financial advice, live-trading authority, validation, graduation, or architecture.
