# Portfolio Current

Status: portfolio currentness router
Current phase: `milestone-4-first-graduation-candidate`
Protocol version: `qf-v3-protocol-0.1`

This file owns the current portfolio posture. It routes agents to current evidence surfaces, but it does not own lab results, method success claims, generated synthesis claims, or graduation decisions.

---

## Current Portfolio Purpose

QuantFactory V3 is a federated LLM-methodology research portfolio.

The scaffold baseline has been accepted, and the portfolio has moved into method-comparison work. Detailed pilot-level evidence lives in protocol export records and lab-local comparison notes.

Milestone 4 goal, set by operator decision, is complete: line-range-first source grounding went through the full evidence ladder to an ADR-approved graduation decision (GRAD-0001, ADR 0003) — the first graduation in the portfolio's history. The evidence items were the grounded long-context comparison (pilots 003/004), the thinking-enabled configuration repeat, and the third-source repeat (chunked pilot 007), with negative results recorded along the way.

The current local comparison note is:

```text
labs/chunked_source_grounding/PLANNING/comparisons/live_pilot_method_comparison_001.md
```

The scaffold exists so live LLM experiments can be measured, compared, and contained.

---

## Active federation labs

Active federation labs:

1. `long_context_judgment`
   - Parent question: How can long-context LLM methods extract reusable trading judgment from messy trader text?
   - Current state: active live-pilot lab with four proposal-only live pilots including the milestone-4 grounded-variant evidence runs.

2. `chunked_source_grounding`
   - Parent question: How can chunked/source-span LLM methods preserve grounding while still supporting useful abstraction?
   - Current state: active live-pilot lab with seven proposal-only live pilots; the locator thread's method lesson graduated as GRAD-0001.

3. `visual_deictic_understanding`
   - Parent question: How can multimodal or vision-language LLM workflows bind transcript/deictic language to visual chart context?
   - Current state: scaffold fixture exports only.

---

## Active Benchmark Packs

Active benchmark packs:

1. `text_judgment_v0`
2. `source_grounding_v0`
3. `visual_deictic_v0`

Future candidate benchmark topics are listed under `benchmarks/future_candidates/` but are not active benchmark packs.

---

## Current Evidence Posture

Scaffold fixture records are not real research evidence.

Proposal-only live pilot records exist across two labs, including bounded negative results, manual and strict reviews, and one completed method-comparison loop. Pilot-level findings live in export records and the owning comparison note; currentness docs intentionally do not repeat them.

These records are proposal-only research records. They are not validation, product evidence, strategy evidence, financial advice, live-trading authority, graduation, or architecture.

Future live LLM experiments must pass the admission checklist in:

```text
docs/live-llm-experiment-admission.md
```

---

## Current Architecture Rule

```text
No new experiment becomes architecture.
It becomes records first.
Architecture changes only after repeated evidence and explicit ADR.
```

---

## Synthesis Status

Synthesis is read-only.

It may import and summarize export records, but it does not:

* mutate lab files,
* mutate benchmark files,
* mutate protocol schemas,
* mutate currentness docs,
* declare winning methods,
* graduate methods,
* or become authority.

Generated synthesis outputs are ignored by default.

---

## Graduation Status

One method pattern has graduated: GRAD-0001, the line-range-first source locator workflow, by operator decision and ADR 0003. Nothing else has graduated.

See:

```text
GRADUATION_LEDGER.md
docs/adr/0003-graduate-line-range-first-locator-workflow.md
```

---

## Next Recommended Research Direction

Milestone 4 is complete: the milestone-4 evidence thread (long-context pilots 003/004, chunked pilot 007) and the GRAD-0001 graduation decision are recorded. The owning comparison note is:

```text
labs/chunked_source_grounding/PLANNING/comparisons/live_pilot_method_comparison_001.md
```

Candidate next directions, in recorded priority order, all requiring operator selection:

1. Cross-model-family repeat of line-range-first — the explicit limitation recorded in ADR 0003 and the highest-value robustness check on GRAD-0001.
2. The LLM-judge calibration study (`docs/research-plans/llm-judge-calibration-study.md`) — the ground-truth inventory has grown to fifteen human evaluation records, and calibration gates the autonomous-lab-loop plan.
3. A downstream-usefulness experiment — the first "useful for what?" question now that locator trust exists.
4. The recursive contextual meaning loop plan, which can now build on graduated locator discipline.

Future method plans for LLM-judge calibration and an autonomous lab loop are recorded under `docs/research-plans/`. They are future plans only, not active labs, and do not change current portfolio work.
