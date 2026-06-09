# Portfolio Current

Status: portfolio currentness router
Current phase: `milestone-3-method-comparison-recorded`
Protocol version: `qf-v3-protocol-0.1`

This file owns the current portfolio posture. It routes agents to current evidence surfaces, but it does not own lab results, method success claims, generated synthesis claims, or graduation decisions.

---

## Current Portfolio Purpose

QuantFactory V3 is a federated LLM-methodology research portfolio.

The scaffold baseline has been accepted, and the portfolio has moved into method-comparison work. Detailed pilot-level evidence lives in protocol export records and lab-local comparison notes.

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
   - Current state: active live-pilot lab with proposal-only export records and manual review records.

2. `chunked_source_grounding`
   - Parent question: How can chunked/source-span LLM methods preserve grounding while still supporting useful abstraction?
   - Current state: active live-pilot lab with proposal-only export and review records; the locator thread is provisionally paused.

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

No methods, labs, schemas, artifacts, product surfaces, or research claims have graduated.

See:

```text
GRADUATION_LEDGER.md
```

---

## Next Recommended Research Direction

Goal 13A locator-thread decision review is complete; the chunked locator thread is provisionally paused as a method lesson. Goal 13B grounded long-context variant planning is drafted as a proposed admission packet at:

```text
labs/long_context_judgment/PLANNING/live_llm_pilot_002/
```

The packet is planning only. The next proposed step is operator review of that packet and, if approved, a separately authorized Goal 13C execution instruction.

The owning comparison note is:

```text
labs/chunked_source_grounding/PLANNING/comparisons/live_pilot_method_comparison_001.md
```

Future method plans for LLM-judge calibration and an autonomous lab loop are recorded under `docs/research-plans/`. They are future plans only, not active labs, and do not change current portfolio work.
