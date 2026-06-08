# Chunked Source Grounding Live Pilot 002 Admission Packet

Status: Goal 7D proposed planning packet
Lab: `chunked_source_grounding`
Experiment: `chunked_source_grounding_live_pilot_002`

This is a proposed live LLM pilot planning record. It is not a completed run, not research evidence, and not a synthesis export.

This is planning/admission only. No LLM call has been made.

The planning packet is not research evidence, not a synthesis export, and not a method success claim. No method success is claimed.

No RunRecord, ArtifactEnvelope, EvaluationRecord, or ResearchNote exists for this pilot.

This packet does not replace the Flash pilot 001 record. Flash pilot 001 produced a bounded negative result: output truncated, incomplete JSON, and output_contract_too_large.

---

## Hardening / Cleanup Discipline

Do not add around stale structure. Rework, replace, delete, or archive it.

This packet reuses the existing `live_llm_pilot_001` planning pattern because Goal 7D needs a comparable pre-run admission shape.

It does not blindly copy the failed Flash output contract. The prompt is narrowed to source-linked claims, segment/span support notes, unsupported-claim reporting, and brief method-failure notes.

This packet adds only the files needed for a distinct Pro/narrow-contract method variant. It does not add scripts, shared helpers, protocol fields, synthesis features, benchmark packs, authority docs, or graduation claims.

---

## Active Benchmark Pack

Benchmark pack: `text_judgment_v0`

Known difficulty:

```text
Chunked source-grounding can preserve exact support while losing broader source intent.
```

Known failure modes:

* output contract too large for one tiny pilot,
* incomplete JSON,
* loses cross-segment judgment,
* becomes too literal to produce reusable abstraction,
* treats span proximity as source truth,
* turns planning structure into evidence.

V2 lesson refs:

* `weak_source_grounding`
* `report_only_confusion`

Metadata safety:

```text
The active benchmark pack contains placeholder identifiers only and does not include raw trader source text or V2 corpus material.
```

---

## MethodCard

Proposed MethodCard:

```text
labs/chunked_source_grounding/PLANNING/live_llm_pilot_002/method_card.proposed.json
```

Method id:

```text
chunked_source_grounding_live_pilot_002_method
```

This proposed MethodCard is protocol-valid planning structure only. It is not in `EXPORTS/` and is not imported by synthesis.

---

## ExperimentCard

Proposed ExperimentCard:

```text
labs/chunked_source_grounding/PLANNING/live_llm_pilot_002/experiment_card.proposed.json
```

Experiment id:

```text
chunked_source_grounding_live_pilot_002
```

The experiment asks:

```text
Can a chunked/source-grounded LLM method produce a complete parseable source-grounding artifact when using DeepSeek V4 Pro and a smaller output contract, and what does it preserve or lose compared with the long-context judgment pilot?
```

Result that would change future behavior:

```text
If the run produces complete parseable source-grounding records, V3 can compare it against the long-context pilot and the Flash failure. If it fails again, V3 should treat the failure as evidence about the method/output contract and review evaluator or prompt structure before another live call.
```

---

## Evaluator Plan

Evaluator plan:

```text
labs/chunked_source_grounding/PLANNING/live_llm_pilot_002/evaluator_plan.md
```

Planned evaluator types:

* `schema_check`
* `manual_boundary_review`
* `manual_content_review`

The planning packet does not create an EvaluationRecord.

---

## Source / Privacy Boundary

Source/privacy boundary:

```text
labs/chunked_source_grounding/PLANNING/live_llm_pilot_002/source_privacy_boundary.md
```

The live pilot must use the same approved excerpt/hash as the long-context pilot and Flash chunked pilot. Raw source material, provider payloads, private notes, raw prompts containing source text, and model traces must remain outside git unless a later explicit policy allows them.

---

## Prompt / Template Hash Plan

Prompt/template path:

```text
labs/chunked_source_grounding/PLANNING/live_llm_pilot_002/prompt_template.live_pilot_002.md
```

The run admission update records the committed prompt template path and SHA-256 before execution.

Do not request broad judgment abstraction notes in the same call.

Do not request full comparison commentary in the same call.

Do not request every useful section just because DeepSeek V4 Pro is stronger.

---

## Model / Config Recording Plan

Provider/model/config details are locked only in:

```text
labs/chunked_source_grounding/PLANNING/live_llm_pilot_002/run_admission_update.md
```

Goal 7D does not call the provider.

---

## Output Artifact Types

Expected post-run artifact type:

* `chunked_source_grounding_proposal`

Expected output sections:

* source-linked claim table,
* segment/span support notes,
* unsupported-claim report,
* brief method-failure notes.

Not requested in this run:

* broad judgment abstraction notes,
* full comparison commentary.

---

## Negative-Result Value

This pilot remains useful if it fails because it can record whether DeepSeek V4 Pro plus a smaller output contract:

* still cannot produce complete parseable output,
* preserves source support but loses broader judgment,
* creates too many local claims without useful abstraction,
* misses unsupported promotional claims,
* needs a different chunk size or span policy,
* or requires evaluator calibration before another live call.

---

## Stop Condition

Stop condition:

```text
labs/chunked_source_grounding/PLANNING/live_llm_pilot_002/stop_condition.md
```

Goal 7D stops at planning/admission validation. Goal 7E, if separately authorized, should stop after one approved source scope and one approved model configuration.

---

## Budget / Secrets Handling

Budget is authorized only by the run admission update.

Before execution, the run admission update must continue to record:

* approved spend ceiling,
* required environment variable names without values,
* trace/log storage location,
* gitignore behavior,
* and confirmation that secrets are not committed.

---

## Proposal-Only Statement

```text
Outputs from this experiment are proposals until evaluated. They do not create source truth, role support, data truth, validation, strategy evidence, financial advice, product authority, live-trading authority, or architecture.
```
