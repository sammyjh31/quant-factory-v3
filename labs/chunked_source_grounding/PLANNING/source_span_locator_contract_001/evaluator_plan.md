# Evaluator Plan

Status: planning only

Goal 11A does not create an EvaluationRecord. It plans how a future manual review should judge locator candidates.

## Evaluator Type

Use the existing `manual_content_review` evaluator type for a future strict locator review.

No new evaluator type is needed; no new evaluator type is introduced.

Do not create a second evaluator framework.

## Review Labels

Use exact if line/offset and locally computed quote hash directly support the claim.

Use approximate if support is local but not exact.

Use broad if support points to a general region only.

Use missing if no source support is found.

Use `overclaimed_exactness` when the model labels a candidate as `exact` but review shows it is approximate, broad, or missing.

## Review Questions

For each locator candidate, the reviewer should ask:

- Does the source ref match the approved local source?
- Do line start and line end identify the same local span as the character offsets?
- Does the locally computed quote hash match the local span selected by the offsets?
- Does the locator label match the strict source-span rubric?
- Does the claim add meaning that is not present in the located span?

The future manual review can remain metadata-safe by committing counts, labels, line ranges, offsets, and quote hashes without committing raw source text.
