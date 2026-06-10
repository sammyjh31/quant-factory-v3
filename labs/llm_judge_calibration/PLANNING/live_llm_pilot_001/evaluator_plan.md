# LLM Judge Calibration Live Pilot 001 Evaluator Plan And Pre-Registration

Status: Goal 16A planning/admission record — pre-registered BEFORE any judge call

This file pre-registers the blinding procedure, trial set, agreement metrics, and delegation thresholds, per the calibration plan's rule that thresholds must be settled before trials so they cannot be fitted to observed results.

## Blinding Procedure

Judge inputs per trial are exactly: the numbered approved source excerpt for that pilot, the raw model output trace of that pilot, mechanically computed pre-check results, and the rubric in the committed prompt template. Judge inputs must never include: human EvaluationRecords, ArtifactEnvelope metadata (it encodes human strict-review counts), comparison notes, research notes, currentness docs, or any score/verdict text. The harness asserts the assembled prompt contains none of the strings `evaluation_record`, `strict review`, `score`, or any ground-truth verdict value before sending.

Mechanical pre-checks supplied to the judge (strict mode): for each locator candidate, the exact span text extracted at its proposed line range, plus a validity note if the range is out of bounds. Line extraction is local tooling work per GRAD-0001; the judge judges support, not arithmetic.

## Trial Set (fixed in advance)

Content-review trials (8), ground truth = the committed `*_manual_content_review` records:
long_context 001, 002, 003, 004; chunked 001, 002, 003, 004.
Negative controls within the set: chunked 001 (truncated, not reviewable) and long_context 003 (empty content) must be failed by the judge; passing either disqualifies the content axis at `delegable`.

Strict line-range trials (7), ground truth = the committed strict review records:
chunked 003, 004, 005, 006, 007; long_context 002, 004.
Negative controls: chunked 005 (model-emitted offsets/hashes not evidence-valid) and long_context 002 (0/4 support-valid) must not be scored as clean passes.

Self-consistency probes (2): duplicate judge calls on chunked 006 (strict) and long_context 004 (content). Verdict disagreement between duplicates caps the affected axis at `assistive`.

Total admitted batch: 17 judge calls, one batch, no per-trial retries unless a call fails before producing output.

## Agreement Metrics

Per trial: verdict agreement (pass/fail match), score agreement (|judge − human| ≤ 0.15), failure-tag overlap (any shared tag counts as overlap; full Jaccard reported), and for strict trials with parseable per-candidate ground truth (chunked 006, 007; long_context 002, 004): per-candidate `support_valid` match and strict-label match, plus `overclaimed_exactness` detection.

Report counts, not percentages alone. n is small and the records must say so.

## Pre-Registered Delegation Thresholds

Per axis (content; strict):

* `delegable`: verdict agreement on at least 7/8 content or 6/7 strict trials, AND all negative controls correctly failed/flagged, AND mean absolute score gap ≤ 0.15, AND self-consistency probe verdicts agree.
* `assistive`: verdict agreement on at least 5/8 content or 4/7 strict trials.
* `not_delegable`: below `assistive`, or sycophancy (a passed negative control) at any agreement level below `delegable` requirements.

A `delegable` result still means judge-first with human spot-checks, never judge-only; human review remains authority per the calibration plan.

## Boundaries

This plan creates no EvaluationRecord. Judge verdicts are local trial data summarized into a delegation-map artifact; they are never committed as EvaluationRecords (protocol v0.1 has no live-judge evaluator type and this study does not add one). No evaluator or judge may create validation, product evidence, strategy evidence, financial advice, live-trading authority, graduation, or architecture.
