# Prompt Delta Plan

Status: planning only

This plan describes how a future prompt should differ from the pilot 003/004 source-span precision prompt.

## Delta

The next prompt should ask the model for locator candidates directly rather than broad source-span hints.

The model should emit:

- line-range candidates,
- character-offset candidates,
- quote-hash candidates,
- locator confidence,
- locator label.

The model should not rely only on segment labels such as `opening segment` or `drawing boxes segment`.

## Narrow Sections

The prompt should request exactly these output sections:

1. source-linked claim table,
2. locator candidate table,
3. unsupported-claim report,
4. brief method-failure notes.

Do not add broad judgment abstraction notes.
Do not add comparison commentary.
Do not add product-like study card fields.
Do not ask for strategy, validation, trading advice, or playbook content.

## Claim Discipline

The prompt should require one claim id for every locator candidate.

The prompt should require at least one locator candidate for every claim unless the claim is marked unsupported.

The prompt should tell the model to mark composite support as `approximate` unless one contiguous source span directly supports the claim.

The prompt should tell the model to use `missing` when no source support exists.
