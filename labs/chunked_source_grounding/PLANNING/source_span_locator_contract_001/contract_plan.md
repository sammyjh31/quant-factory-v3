# Goal 11A Source-Span Locator Contract Plan

Status: planning only

This is Goal 11A source-span locator output contract planning for `chunked_source_grounding`.

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

Goal 10C found that source-span precision improved and repeated under strict manual review, but the model artifacts still do not emit canonical line/offset locator candidates directly. Goal 11A plans a narrow output contract that asks the model to produce locator candidates that local review can use to compute quote hashes.

Research question:

```text
Can the model emit canonical locator candidates directly instead of producing broad source-span hints that manual reviewers must reconstruct afterward?
```

## Candidate Locator Fields

Each locator candidate should include:

- `source_ref`
- `candidate_line_start`
- `candidate_line_end`
- `candidate_char_start`
- `candidate_char_end`
- `locator_confidence`
- `locator_label: exact | approximate | broad | missing`

These fields are lab-local artifact payload fields for a future proposal-only artifact. They are not protocol fields in Goal 11A.

The model should not emit quote hashes. The local runner/reviewer computes quote hashes from the exact local source spans selected by the candidate line ranges and character offsets.

Future committed records may include metadata-safe computed quote hashes after local computation, but they must not treat model-generated hash strings as source truth.

## Relationship To Claims

Every source-linked claim must have at least one locator candidate. This means every claim must have at least one locator candidate.

Each locator candidate must have one claim id. This means every locator candidate must have one claim id.

Rule: unsupported claims must explain why no valid locator exists instead of inventing a locator candidate.

Composite claims should be split before assigning `exact`. If a claim needs multiple nearby spans, the model should mark the locator as `approximate` or split the claim.

## Narrow Output Contract

The future artifact should request only:

1. source-linked claim table,
2. locator candidate table,
3. unsupported-claim report,
4. brief method-failure notes.

Do not add broad judgment abstraction notes. Do not add comparison commentary. Do not add product-like study card fields. Do not ask for strategy, validation, trading advice, or playbook content.

## Protocol Fit

Existing `ArtifactEnvelope.payload` can honestly hold locator candidates and locally computed quote hashes as lab-local proposal payload data because the ArtifactEnvelope schema allows additional payload properties and already requires `outcome_polarity`.

No protocol change is needed for Goal 11A; no protocol change is part of this planning packet.

Do not change `ArtifactEnvelope` schema.

If a future execution step proves existing records cannot honestly represent locator candidates, stop and report before changing protocol.
