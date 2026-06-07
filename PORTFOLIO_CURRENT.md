# Portfolio Current

Status: scaffold currentness router  
Current phase: `milestone-2-live-pilot-recorded`
Protocol version: `qf-v3-protocol-0.1`

This file owns the current portfolio posture. It does not own lab results, method success claims, generated synthesis claims, or graduation decisions.

---

## Current Portfolio Purpose

QuantFactory V3 is a federated LLM-methodology research portfolio.

The scaffold baseline has been accepted. Milestone 2 now has one admitted tiny live LLM pilot export set recorded under `labs/long_context_judgment/EXPORTS/`.

The accepted scaffold contains:

- protocol schemas,
- benchmark manifests,
- lab fixture exports,
- validation,
- read-only synthesis,
- and currentness docs.

The scaffold exists so live LLM experiments can be measured, compared, and contained.

Current planning packet:

```text
labs/long_context_judgment/PLANNING/live_llm_pilot_001/
```

The base Goal 3 planning material is proposed planning structure only. It is not in `EXPORTS/`, is not imported by synthesis, and does not authorize execution by itself.

The packet now includes:

```text
labs/long_context_judgment/PLANNING/live_llm_pilot_001/run_admission_update.md
```

That update authorized exactly one tiny live LLM pilot run under the stated scope. The update itself did not create run evidence, generated synthesis claims, graduation status, or architecture.

The authorized run has produced one proposal-only live export set. The export set is not validation, product evidence, strategy evidence, financial advice, live-trading authority, graduation, or architecture.

---

## Active federation labs

Active scaffold-origin labs:

1. `long_context_judgment`
   - Parent question: How can long-context LLM methods extract reusable trading judgment from messy trader text?
   - Current state: scaffold fixture exports plus one admitted tiny live LLM pilot export set for `long_context_judgment_live_pilot_001`

2. `chunked_source_grounding`
   - Parent question: How can chunked/source-span LLM methods preserve grounding while still supporting useful abstraction?
   - Current state: scaffold fixture exports only

3. `visual_deictic_understanding`
   - Parent question: How can multimodal or vision-language LLM workflows bind transcript/deictic language to visual chart context?
   - Current state: scaffold fixture exports only

---

## Active Benchmark Packs

Milestone-one active benchmark packs:

1. `text_judgment_v0`
2. `source_grounding_v0`
3. `visual_deictic_v0`

Future candidate benchmark topics are listed under `benchmarks/future_candidates/` but are not active benchmark packs.

---

## Evidence Status

Scaffold milestone-one fixture records are not real research evidence.

Current scaffold-origin lab records remain fixtures for protocol validation only.

They exist to prove that labs can publish comparable records and that synthesis can import those records read-only.

The `long_context_judgment_live_pilot_001` planning packet and `run_admission_update.md` are not evidence and are not synthesis exports.

One admitted tiny live LLM pilot export set now exists for `long_context_judgment_live_pilot_001`. It is proposal-only. It is not validation, product evidence, strategy evidence, financial advice, live-trading authority, graduation, or architecture.

---

## Current Architecture Rule

```text
No new experiment becomes architecture.
It becomes records first.
Architecture changes only after repeated evidence and explicit ADR.
```

---

## Live LLM Experiment Status

The first admitted tiny live LLM pilot has run under:

```text
labs/long_context_judgment/PLANNING/live_llm_pilot_001/
```

The planning packet contains proposed MethodCard and ExperimentCard records only. Those planning records are not in `EXPORTS/` and are not imported by synthesis.

The current preflight update is:

```text
labs/long_context_judgment/PLANNING/live_llm_pilot_001/run_admission_update.md
```

It authorized exactly one tiny live LLM pilot run under the stated scope.

The proposal-only live export set is:

```text
labs/long_context_judgment/EXPORTS/run_record.live_pilot_001.json
labs/long_context_judgment/EXPORTS/artifact_envelope.live_pilot_001.json
labs/long_context_judgment/EXPORTS/evaluation_record.live_pilot_001.json
labs/long_context_judgment/EXPORTS/research_note.live_pilot_001.json
```

Future live LLM experiments must pass the admission checklist in:

```text
docs/live-llm-experiment-admission.md
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
