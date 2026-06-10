# Lab Card: llm_judge_calibration

Status: active live-pilot lab (milestone 5)

This lab measures whether an LLM judge can reproduce the operator-lineage manual content-review and strict line-range-review verdicts on the portfolio's existing live-pilot artifacts. Its output is a per-axis delegation map (delegable / assistive / not delegable), the explicit gate for the autonomous-lab-loop plan.

Activated from `docs/research-plans/llm-judge-calibration-study.md` by operator decision (milestone-5 directive).

## Current Evidence State

- scaffold fixtures, a pre-registered admission packet, and proposal-only live export records from blinded judge-agreement trials
- ground truth: 15 committed human evaluation records across 11 pilots in two labs
- judge trials and agreement results live in export records, not in this lab card

## Current Boundaries

- judge outputs are proposal-only; they are never review authority and never overwrite human EvaluationRecords
- agreement results are committed as lab artifacts (delegation-map proposals), not as new evaluator types; protocol v0.1 is unchanged
- no validation, product authority, strategy evidence, financial advice, live-trading authority, graduation, or architecture
- future live runs require live LLM admission and an explicit execution instruction
