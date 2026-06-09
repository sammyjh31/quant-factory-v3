# Prompt Delta Plan

Status: planning only

Goal 12A narrows the next chunked-source prompt from pilot 005's broad locator contract to line-range locator candidates only.

## Prompt Changes

The future prompt should ask the model to emit:

- claim id
- source reference
- starting line number
- ending line number
- locator confidence
- locator label
- short support rationale

Do not ask for `candidate_char_start`.
Do not ask for `candidate_char_end`.
Do not ask for quote hashes.
Do not ask for cryptographic hashes.
Do not ask for raw source text.
Do not add broad judgment abstraction notes.
Do not add comparison commentary.
Do not ask for strategy, validation, trading advice, or playbook content.

## Contract Shape

The model should produce compact JSON with a top-level list of line-range candidates. Each candidate should stay small enough for one tiny live-pilot call.

The prompt should make clear that locator labels are proposals. Local review decides whether the proposed line range is exact, approximate, broad, or missing.

## Expected Failure Modes

The narrowed prompt should make these failures visible:

- invalid line numbers;
- line ranges too broad for source-span precision;
- line ranges that point near the right concept but not to a supporting span;
- confidence that is higher than the support warrants;
- rationale that overstates what the source region proves.

No failure should be hidden by asking the model for hashes or offsets that local code cannot trust.
