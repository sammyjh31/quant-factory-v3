# Portfolio Current

Status: scaffold currentness router  
Current milestone: `scaffold-v0.1`  
Protocol version: `qf-v3-protocol-0.1`

This file owns the current portfolio posture. It does not own lab results, method success claims, generated synthesis claims, or graduation decisions.

---

## Current Portfolio Purpose

QuantFactory V3 is a federated LLM-methodology research portfolio.

The current milestone builds the scaffold required for future LLM experiments:

- protocol schemas,
- benchmark manifests,
- lab fixture exports,
- validation,
- read-only synthesis,
- and currentness docs.

The scaffold exists so future live LLM experiments can be measured, compared, and contained.

---

## Active Labs

Milestone-one active labs:

1. `long_context_judgment`
   - Parent question: How can long-context LLM methods extract reusable trading judgment from messy trader text?

2. `chunked_source_grounding`
   - Parent question: How can chunked/source-span LLM methods preserve grounding while still supporting useful abstraction?

3. `visual_deictic_understanding`
   - Parent question: How can multimodal or vision-language LLM workflows bind transcript/deictic language to visual chart context?

These labs currently contain fixture records only.

---

## Active Benchmark Packs

Milestone-one active benchmark packs:

1. `text_judgment_v0`
2. `source_grounding_v0`
3. `visual_deictic_v0`

Future candidate benchmark topics are listed under `benchmarks/future_candidates/` but are not active benchmark packs.

---

## Evidence Status

There is no real research evidence in scaffold milestone one.

Current lab records are fixtures for protocol validation only.

They exist to prove that labs can publish comparable records and that synthesis can import those records read-only.

---

## Current Architecture Rule

```text
No new experiment becomes architecture.
It becomes records first.
Architecture changes only after repeated evidence and explicit ADR.
```

---

## Live LLM Experiment Status

No live LLM experiments run during scaffold milestone one.

Future live LLM experiments must pass the admission checklist in:

```text
docs/live-llm-experiment-admission.md
```

---

## Synthesis Status

Synthesis is read-only.

It may import and summarize fixture records, but it does not:

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
