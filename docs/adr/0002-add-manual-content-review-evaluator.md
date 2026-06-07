# ADR 0002: Add Manual Content Review Evaluator

Status: accepted

## Context

Goal 6 planning found that the first live pilot can be contained and recorded, but content quality cannot yet be reviewed honestly as a completed evaluator record.

`manual_boundary_review` represents containment checks only. It should not be overloaded with source-grounding, usefulness, hallucination, unsupported-claim, or abstraction-quality judgment.

`schema_check` validates record shape only. `human_placeholder` and `llm_judge_placeholder` are placeholders, not completed reviews.

## Decision

Add `manual_content_review` to `EvaluationRecord.evaluator_type`.

This patch keeps `protocol_version` as `qf-v3-protocol-0.1` and bumps `schema_version` to `0.1.2`.

The change allows a future EvaluationRecord to represent completed human/manual review of proposal-only live pilot artifacts for:

* source grounding,
* research usefulness,
* hallucination or unsupported-claim handling,
* abstraction quality,
* and negative-result value.

## Non-Effects

No new protocol object.

No LLM judge.

No validation claim.

No product authority.

No strategy evidence.

No financial advice.

No live-trading authority.

No graduation.

No product, graph, backtest, Playbook, execution, or graduation schema.

No content-review export is created by this ADR.

This is not architecture approval beyond adding one evaluator enum value.

## Consequences

Future Goal 6C-B work can create one `manual_content_review` EvaluationRecord targeting the first live pilot artifact if explicitly authorized.

The existing manual boundary review remains the containment review for Goal 5.

Synthesis continues to import only records under `EXPORTS/` and remains generated and non-authoritative.
