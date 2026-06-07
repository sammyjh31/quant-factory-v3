# ADR 0001: Allow Proposal-Only Live Pilot Records

Status: accepted

## Context

Goal 5 preflight found that the protocol could not honestly represent the first admitted live LLM pilot. `RunRecord` only allowed scaffold fixture semantics, `ArtifactEnvelope` only allowed fixture outcome polarity, and `ResearchNote` required a fixture-only disclaimer.

Calling a live DeepSeek run a scaffold fixture would create semantic drift: the records would validate syntactically while lying about their authority.

## Decision

Allow existing protocol v0.1 records to represent one admitted proposal-only live LLM pilot without mislabeling it as a scaffold fixture.

This patch keeps `protocol_version` as `qf-v3-protocol-0.1` and bumps `schema_version` to `0.1.1`.

The changed record support is limited to:

* `RunRecord` can represent `live_llm_pilot` with `proposal_only` and `live_recorded` or `live_failed`.
* `RunRecord` rejects fixture/live semantic mismatches.
* `ArtifactEnvelope` can carry `payload.outcome_polarity: proposal_only`.
* `EvaluationRecord` can use `manual_boundary_review`.
* `ResearchNote` uses `evidence_disclaimer` for both fixture and proposal-only live pilot notes.

## Non-Effects

This is not a graduation.

This is not a new product architecture.

This is not a live trading or strategy-validation surface.

This does not add live trace, prompt, model-call, graph, product, strategy, backtest, Playbook, execution, or graduation schemas.

This does not add `LiveExperimentAdmission` as a schema. The existing live LLM admission document remains the admission boundary.

This does not validate model output quality, source truth, trading utility, product readiness, financial advice, live-trading authority, or architecture.

## Consequences

The first live pilot can now create protocol-valid proposal-only records after the admitted model call.

Fixture records stay valid after migrating to `schema_version: 0.1.1` and `evidence_disclaimer`.

Synthesis can import future live exports from `EXPORTS/` without reading `PLANNING/`, while remaining generated and non-authoritative.
