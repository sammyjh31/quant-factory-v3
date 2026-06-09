# Evaluator Plan

Status: planning only

The future review should reuse `manual_content_review`. It should not add a new evaluator type.

## Review Target

The future target artifact should be an `ArtifactEnvelope` containing lab-local line-range locator candidates in `payload`.

## Review Axes

Manual review should judge:

- line-number validity;
- source-ref consistency;
- whether the proposed range supports the claim;
- whether the range is narrow enough to reduce reviewer reconstruction;
- whether the support rationale overclaims the source;
- whether local offsets and quote hashes can be computed after accepting the line range.

## Locator Labels

Use these label rules:

- exact if the line range directly supports the claim;
- approximate if nearby lines support the claim but the range is not exact;
- broad if the range points to a general region only;
- missing if no support exists.

The review may tag `overclaimed_exactness` if a model labels a broad or approximate range as exact.

## Evaluation Boundary

This review would not validate trading usefulness, product readiness, strategy quality, or architecture. It would only evaluate whether line-range locator candidates improve the source-span workflow.

There is no new evaluator type in Goal 12A.
