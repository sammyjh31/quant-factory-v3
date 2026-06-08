# Portfolio Current

Status: portfolio currentness router
Current phase: `milestone-3-method-comparison-recorded`
Protocol version: `qf-v3-protocol-0.1`

This file owns the current portfolio posture. It routes agents to current evidence surfaces, but it does not own lab results, method success claims, generated synthesis claims, or graduation decisions.

---

## Current Portfolio Purpose

QuantFactory V3 is a federated LLM-methodology research portfolio.

The scaffold baseline has been accepted. The portfolio has completed one tiny method-comparison loop on `text_judgment_v0`, plus a second-source source-span precision repeat inside the active chunked/source-grounded lab.

Detailed pilot-level evidence lives in protocol export records and lab-local comparison notes.

The current local comparison note is:

```text
labs/chunked_source_grounding/PLANNING/comparisons/live_pilot_method_comparison_001.md
```

The scaffold exists so live LLM experiments can be measured, compared, and contained. Goal 11D manual strict locator review is complete. The next proposed step is Goal 11E comparison-note update.

---

## Active federation labs

Active federation labs:

1. `long_context_judgment`
   - Parent question: How can long-context LLM methods extract reusable trading judgment from messy trader text?
   - Current state: active live-pilot lab with proposal-only export records and manual review records.

2. `chunked_source_grounding`
   - Parent question: How can chunked/source-span LLM methods preserve grounding while still supporting useful abstraction?
   - Current state: active live-pilot lab with proposal-only export records, manual reviews, a bounded negative Flash result, a Pro narrowed-contract result, a second-source source-span precision repeat, strict source-span re-review records, and one strict locator review showing useful line ranges but inaccurate char offsets.

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

The portfolio has completed one tiny method-comparison loop on `text_judgment_v0`.

Current preliminary read:

- long-context preserved broader judgment abstraction with missing-context and teacher-intent compression caveats;
- chunked/source-grounded methods have one bounded negative Flash result and later Pro results showing better parseability under narrower contracts;
- source-span precision pattern repeated beyond the first source, while strict source-span re-review with canonical offsets found one overclaimed exactness caveat and broad segment refs / limited abstraction remain open tradeoffs.
- the source-span locator candidate pilot produced proposal-only locator coordinates and locally computed quote hashes; strict manual locator review found useful line ranges but inaccurate char offsets, so computed quote hashes were mechanically valid but not evidence-valid support handles.

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

Goal 11D manual strict locator review is complete. The next proposed step is Goal 11E comparison-note update.

The owning comparison note is:

```text
labs/chunked_source_grounding/PLANNING/comparisons/live_pilot_method_comparison_001.md
```

The completed Goal 11A locator contract plan (the source-span locator output contract plan) and the completed Goal 11B admission packet define the recorded source-span locator candidate pilot. Goal 11D found that direct locator emission partly improves review because line ranges are useful, but char offsets are not yet accurate enough for canonical quote-hash support. Goal 11E should update the local comparison note without creating validation, graduation, or architecture.
