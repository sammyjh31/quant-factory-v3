# Portfolio Current

Status: portfolio currentness router
Current phase: `milestone-2-live-pilot-recorded`
Protocol version: `qf-v3-protocol-0.1`

This file owns the current portfolio posture. It routes agents to the current evidence surfaces, but it does not own lab results, method success claims, generated synthesis claims, or graduation decisions.

---

## Current Portfolio Purpose

QuantFactory V3 is a federated LLM-methodology research portfolio.

The scaffold baseline has been accepted. The portfolio now has one tiny method-comparison loop on `text_judgment_v0`, using the same source excerpt across:

- `long_context_judgment_live_pilot_001`
- `chunked_source_grounding_live_pilot_001`
- `chunked_source_grounding_live_pilot_002`
- `chunked_source_grounding_live_pilot_003`

`chunked_source_grounding_live_pilot_003` produced one admitted DeepSeek V4 Pro source-span precision live pilot export set and one DeepSeek V4 Pro source-span precision manual content-review EvaluationRecord.

A second-source source-span precision repeat is now planned as `chunked_source_grounding_live_pilot_004`; no model call, export records, research evidence, generated synthesis claim, graduation status, or architecture exists for that repeat.

The accepted scaffold contains protocol schemas, benchmark manifests, lab fixture exports, validation, read-only synthesis, currentness docs, and tests proving the boundaries.

The scaffold exists so live LLM experiments can be measured, compared, and contained.

---

## Active federation labs

Active scaffold-origin labs:

1. `long_context_judgment`
   - Parent question: How can long-context LLM methods extract reusable trading judgment from messy trader text?
   - Current state: scaffold fixture exports plus one admitted proposal-only live pilot export set and one manual content-review EvaluationRecord for `long_context_judgment_live_pilot_001`

2. `chunked_source_grounding`
   - Parent question: How can chunked/source-span LLM methods preserve grounding while still supporting useful abstraction?
   - Current state: scaffold fixture exports plus one admitted proposal-only chunked/source-grounded live pilot export set and one failure-focused manual content-review EvaluationRecord for `chunked_source_grounding_live_pilot_001`; one admitted DeepSeek V4 Pro chunked/source-grounded live pilot export set and one DeepSeek V4 Pro manual content-review EvaluationRecord for `chunked_source_grounding_live_pilot_002`; one admitted DeepSeek V4 Pro source-span precision live pilot export set and one DeepSeek V4 Pro source-span precision manual content-review EvaluationRecord for `chunked_source_grounding_live_pilot_003`

3. `visual_deictic_understanding`
   - Parent question: How can multimodal or vision-language LLM workflows bind transcript/deictic language to visual chart context?
   - Current state: scaffold fixture exports only

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

The local comparison note is:

```text
labs/chunked_source_grounding/PLANNING/comparisons/live_pilot_method_comparison_001.md
```

Current preliminary read:

- long-context preserved broader judgment abstraction but had missing-context / teacher-intent compression caveats;
- chunked Flash is a bounded negative result for output-contract size / incomplete JSON;
- chunked Pro with the narrowed contract produced reviewable claim-level source grounding, with broad segment refs and limited abstraction;
- chunked Pro source-span precision improved over pilot 002, with warranted exact/approximate labels for reviewed claims, while still lacking canonical offsets and broader abstraction.

The current records include one manual content-review EvaluationRecord for the long-context pilot, one failure-focused manual content-review EvaluationRecord for the chunked Flash pilot, one DeepSeek V4 Pro manual content-review EvaluationRecord for the chunked Pro pilot, and one DeepSeek V4 Pro source-span precision manual content-review EvaluationRecord.

These records are proposal-only research records. They are not validation, product evidence, strategy evidence, financial advice, live-trading authority, graduation, or architecture.

The current source-span precision planning packets are:

```text
labs/chunked_source_grounding/PLANNING/live_llm_pilot_003/
labs/chunked_source_grounding/PLANNING/live_llm_pilot_004/
```

Pilot 003 narrowed the chunked Pro question to tighter source-span hints and honest exact/approximate/broad/missing support labels. The corresponding manual content review passed with caveats: source-span precision improved relative to pilot 002, exact/approximate labels were warranted for the reviewed claims, and the artifact still lacks canonical offsets and broader abstraction. Pilot 004 plans a second-source repeat of that source-span precision contract. Planning packets remain planning structure only. They are not in `EXPORTS/`, are not imported by synthesis, and do not authorize future execution by themselves.

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

Execute the admitted `chunked_source_grounding_live_pilot_004` second-source source-span precision repeat only after a separate Goal 9B instruction.

That next execution must stay within the admitted source, prompt, model, budget, and trace boundaries; create only proposal-only protocol records if the run succeeds; avoid declaring a winner; avoid copying generated summaries; and avoid product, strategy, validation, financial-advice, live-trading, graduation, or architecture claims.
