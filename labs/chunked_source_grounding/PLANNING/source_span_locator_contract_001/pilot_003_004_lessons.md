# Pilot 003 / 004 Lessons

Status: planning only

Goal 11A reuses the lesson from pilots 003 and 004 instead of creating a new method family.

## What Pilots 003 And 004 Did

pilots 003/004 emitted support hints rather than canonical locator candidates.

The support hints were reviewable and useful, but the model artifacts did not emit line ranges, character offsets, or quote hashes directly.

## What Goal 10B Added

The strict reviewers reconstructed canonical locators after the fact; strict reviewers reconstructed canonical locators after the fact is the key Goal 10B lesson.

The strict review records were:

- `chunked_source_grounding_live_pilot_003_strict_span_review`
- `chunked_source_grounding_live_pilot_004_strict_span_review`

Pilot 003 strict review found `exact=3`, `approximate=2`, `broad=0`, `missing=0`, and `overclaimed_exactness=0`.

Pilot 004 strict review found `exact=4`, `approximate=2`, `broad=0`, `missing=0`, and `overclaimed_exactness=1`.

The pilot 004 caveat matters: one model-labeled exact case was better treated as approximate because it compressed a composite local span.

## Goal 11 Lesson

Goal 11 should test whether the model can emit locator candidates directly.

The next contract should not ask for another broad repeat. It should ask whether direct locator candidates reduce reviewer reconstruction work while preserving proposal-only boundaries.

If the model still emits broad segment refs, that becomes useful negative-result evidence for the contract.
