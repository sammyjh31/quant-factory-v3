# Chunked Source Grounding Live Pilot 003 Admission Packet

Status: Goal 8B proposed planning packet
Historical status: pre-run admission record; current run status is owned by `labs/chunked_source_grounding/EXPORTS/run_record.live_pilot_003.json`.
Lab: `chunked_source_grounding`
Experiment: `chunked_source_grounding_live_pilot_003`

This is a proposed live LLM pilot planning record. It is not a completed run, not research evidence, and not a synthesis export.

This packet was created before execution as planning/admission only.

The planning packet is not research evidence, not a synthesis export, and not a method success claim. No method success is claimed.

This pre-run planning packet itself contains no RunRecord, ArtifactEnvelope, EvaluationRecord, or ResearchNote.

Goal 7G found broad_segment_refs and limited_abstraction caveats.

---

## Hardening / Cleanup Discipline

Do not add around stale structure. Rework, replace, delete, or archive it.

This packet reuses the existing `live_llm_pilot_002` planning pattern because Goal 8B needs a comparable pre-run admission shape.

It does not blindly copy pilot 002 assumptions. Pilot 002 produced complete parseable JSON under the narrowed contract, but the manual content review recorded broad segment references and limited abstraction. Goal 8B narrows the next question to source-span precision.

This packet adds only the files needed for a distinct source-span precision method variant. It does not add scripts, shared helpers, protocol fields, synthesis features, benchmark packs, authority docs, or graduation claims.

---

## Active Benchmark Pack

Benchmark pack: `text_judgment_v0`

Known difficulty:

```text
Chunked source-grounding can produce reviewable claim-level support while leaving span references too broad for precise grounding review.
```

Known failure modes:

* broad segment refs,
* approximate span hints pretending to be exact,
* over-tight source hints that omit necessary context,
* unsupported claims hidden inside metadata-safe paraphrase,
* loses broader judgment abstraction,
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
labs/chunked_source_grounding/PLANNING/live_llm_pilot_003/method_card.proposed.json
```

Method id:

```text
chunked_source_grounding_live_pilot_003_method
```

This proposed MethodCard is protocol-valid planning structure only. It is not in `EXPORTS/` and is not imported by synthesis.

---

## ExperimentCard

Proposed ExperimentCard:

```text
labs/chunked_source_grounding/PLANNING/live_llm_pilot_003/experiment_card.proposed.json
```

Experiment id:

```text
chunked_source_grounding_live_pilot_003
```

The experiment asks:

```text
Can a chunked/source-grounded LLM method improve source-span precision from broad segment references to tighter source-span hints while keeping the narrowed output contract complete and parseable?
```

Result that would change future behavior:

```text
If the run produces complete parseable output with honest exact/approximate/broad/missing span labels, V3 can compare whether tighter source-span precision improves chunked source grounding without re-expanding the output contract. If it fails, V3 should treat the result as evidence about span-policy design before another live call.
```

---

## Evaluator Plan

Evaluator plan:

```text
labs/chunked_source_grounding/PLANNING/live_llm_pilot_003/evaluator_plan.md
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
labs/chunked_source_grounding/PLANNING/live_llm_pilot_003/source_privacy_boundary.md
```

The live pilot must use the same approved excerpt/hash as the long-context pilot, Flash chunked pilot, and Pro narrowed-contract pilot. Raw source material, provider payloads, private notes, raw prompts containing source text, and model traces must remain outside git unless a later explicit policy allows them.

---

## Prompt / Template Hash Plan

Prompt/template path:

```text
labs/chunked_source_grounding/PLANNING/live_llm_pilot_003/prompt_template.live_pilot_003.md
```

The run admission update records the committed prompt template path and SHA-256 before execution.

Do not re-expand the output contract.

Do not add broad judgment abstraction notes.

Do not add full comparison commentary.

Do not ask for a product-like study card.

Do not add strategy, validation, trading advice, or playbook content.

---

## Model / Config Recording Plan

Provider/model/config details are locked only in:

```text
labs/chunked_source_grounding/PLANNING/live_llm_pilot_003/run_admission_update.md
```

Goal 8B does not call the provider.

---

## Output Artifact Types

Expected post-run artifact type:

* `chunked_source_span_precision_proposal`

Expected output sections:

* source-linked claim table,
* tighter source-span support hints,
* unsupported-claim report,
* brief method-failure notes.

Not requested in this run:

* broad judgment abstraction notes,
* full comparison commentary,
* product-like study card,
* strategy or validation content,
* trading advice,
* playbook content.

---

## Negative-Result Value

This pilot remains useful if it fails because it can record whether tighter source-span hints:

* still collapse to broad segment refs,
* make the output incomplete or unparsable,
* create false precision,
* preserve source grounding but lose useful abstraction,
* hide unsupported claims,
* or require a canonical segmenting policy before another live call.

---

## Stop Condition

Stop condition:

```text
labs/chunked_source_grounding/PLANNING/live_llm_pilot_003/stop_condition.md
```

Goal 8B stops at planning/admission validation. Goal 8C, if separately authorized, should stop after one approved source scope and one approved model configuration.

---

## Budget / Secrets Handling

Budget is authorized only by the run admission update.

Before execution, the run admission update must continue to record:

* approved spend ceiling,
* provider/model id,
* prompt/template path and hash,
* config hash,
* required secret environment variable names,
* trace/log storage boundaries,
* and exact stop conditions.

Secrets must be environment-only and must never be committed.

---

## Proposal-Only Statement

This packet is a proposed live LLM pilot planning record.

It is not a completed run, not research evidence, not a synthesis export, not validation, not product evidence, not strategy evidence, not financial advice, not live-trading authority, not graduation, and not architecture.
