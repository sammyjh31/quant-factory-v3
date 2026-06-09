# Chunked Source Grounding Live Pilot 006 Admission Packet

Status: Goal 12B proposed planning packet
Historical status: pre-run admission record; current run status is owned by `labs/chunked_source_grounding/EXPORTS/run_record.live_pilot_006.json`.
Lab: `chunked_source_grounding`
Experiment: `chunked_source_grounding_live_pilot_006`

This is a proposed live LLM pilot planning record. It is not a completed run, not research evidence, and not a synthesis export.

This packet was created before execution as planning/admission only.

The planning packet is not research evidence, not a synthesis export, and not a method success claim. No method success is claimed.

This pre-run planning packet itself contains no RunRecord, ArtifactEnvelope, EvaluationRecord, or ResearchNote.

Goal 12A planned a line-range-first locator contract. Goal 12B turns that plan into a contained live-run admission packet without executing the run.

---

## Hardening / Cleanup Discipline

Do not add around stale structure. Rework, replace, delete, or archive it.

This packet reuses the existing live pilot planning pattern because Goal 12B needs a comparable pre-run admission shape for a line-range-first locator pilot.

It does not blindly copy pilot 005 assumptions. Pilot 005 asked for line ranges and character offsets; Goal 12B narrows the prompt to source-linked claims plus line-range locator candidates only.

This packet adds only the files needed for a distinct live-run admission packet. It does not add scripts, shared helpers, protocol fields, synthesis features, benchmark packs, authority docs, or graduation claims.

## Goal 12A Contract Reuse

Goal 12B uses:

```text
labs/chunked_source_grounding/PLANNING/line_range_locator_contract_001/
```

The model emits line-range locator candidates only.

Do not ask the model to emit character offsets.

Do not ask the model to emit quote hashes.

local review/tooling computes character offsets only after line-range validation.

quote hashes are computed locally only from validated spans.

## Active Benchmark Pack

Benchmark pack: `text_judgment_v0`

Known difficulty:

```text
The model may still propose line ranges that are broad, nearby, or confidence-overstated rather than support-valid.
```

Known failure modes:

* broad line ranges disguised as exact support,
* invalid line numbers,
* source-linked claims without support-valid line ranges,
* locator confidence overstates source precision,
* unsupported claims hidden inside metadata-safe paraphrase,
* false precision if local offsets or hashes are computed before line-range validation,
* loses broader judgment abstraction,
* turns planning structure into evidence,
* falls back to a full corpus path instead of the selected excerpt.

V2 lesson refs:

* `weak_source_grounding`
* `report_only_confusion`

Metadata safety:

```text
The active benchmark pack contains placeholder identifiers only and does not include raw trader source text or V2 corpus material.
```

## MethodCard

Proposed MethodCard:

```text
labs/chunked_source_grounding/PLANNING/live_llm_pilot_006/method_card.proposed.json
```

Method id:

```text
chunked_source_grounding_live_pilot_006_method
```

This proposed MethodCard is protocol-valid planning structure only. It is not in `EXPORTS/` and is not imported by synthesis.

## ExperimentCard

Proposed ExperimentCard:

```text
labs/chunked_source_grounding/PLANNING/live_llm_pilot_006/experiment_card.proposed.json
```

Experiment id:

```text
chunked_source_grounding_live_pilot_006
```

The experiment asks:

```text
Can the model emit reviewable line-range locator candidates directly, while local review/tooling computes character offsets and quote hashes only after line-range validation?
```

Result that would change future behavior:

```text
If the run produces complete parseable output with useful line ranges and honest locator labels, V3 can compare line-range-first locator output against pilot 005's line-plus-offset attempt. If it fails, V3 should treat the result as evidence that direct locator emission needs a different segmentation or review policy before another live call.
```

## Evaluator Plan

Evaluator plan:

```text
labs/chunked_source_grounding/PLANNING/live_llm_pilot_006/evaluator_plan.md
```

Planned evaluator types:

* `schema_check`
* `manual_boundary_review`
* `manual_content_review`

The planning packet does not create an EvaluationRecord.

## Source / Privacy Boundary

Source/privacy boundary:

```text
labs/chunked_source_grounding/PLANNING/live_llm_pilot_006/source_privacy_boundary.md
```

The live pilot must use the same selected second-source excerpt as pilots 004 and 005 unless a later admission update changes scope. Raw source material, provider payloads, private notes, raw prompts containing source text, and model traces must remain outside git unless a later explicit policy allows them.

Do not fall back to the full corpus path.

## Prompt / Template Hash Plan

Prompt/template path:

```text
labs/chunked_source_grounding/PLANNING/live_llm_pilot_006/prompt_template.live_pilot_006.md
```

The run admission update records the committed prompt template path and SHA-256 before execution.

Keep the output contract narrow:

* source-linked claim table,
* line-range locator candidate table,
* unsupported-claim report,
* brief method-failure notes.

Do not ask the model to emit character offsets.

Do not ask the model to emit quote hashes.

Do not add broad judgment abstraction notes.

Do not add full comparison commentary.

Do not ask for a product-like study card.

Do not add strategy, validation, trading advice, or playbook content.

## Model / Config Recording Plan

Provider/model/config details are locked only in:

```text
labs/chunked_source_grounding/PLANNING/live_llm_pilot_006/run_admission_update.md
```

Goal 12B does not call the provider.

## Output Artifact Types

Expected post-run artifact type:

* `chunked_source_line_range_locator_candidate_proposal`

Expected output sections:

* source-linked claim table,
* line-range locator candidate table,
* unsupported-claim report,
* brief method-failure notes.

Not requested in this run:

* character offsets,
* quote hashes,
* broad judgment abstraction notes,
* full comparison commentary,
* product-like study card,
* strategy or validation content,
* trading advice,
* playbook content.

## Negative-Result Value

This pilot remains useful if it fails because it can record whether line-range-first locator candidates:

* reduce reviewer reconstruction work,
* remain too broad to compute useful offsets later,
* produce invalid line ranges,
* create false precision through confidence labels,
* preserve source grounding but lose useful abstraction,
* hide unsupported claims,
* or require local pre-segmentation before another live call.

## Stop Condition

Stop condition:

```text
labs/chunked_source_grounding/PLANNING/live_llm_pilot_006/stop_condition.md
```

Goal 12B stops at planning/admission validation. Goal 12C, if separately authorized, should stop after one approved source scope and one approved model configuration.

## Budget / Secrets Handling

Budget cap: `$3` hard maximum.

Required secret name:

```text
DEEPSEEK_API_KEY
```

The secret name may be documented. The secret value must never be committed.

## Proposal-Only Statement

Outputs from this experiment are proposals until evaluated. They do not create source truth, role support, data truth, validation, strategy evidence, financial advice, product authority, live-trading authority, or architecture.
