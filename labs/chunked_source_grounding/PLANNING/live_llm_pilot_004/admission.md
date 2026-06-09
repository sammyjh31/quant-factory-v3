# Chunked Source Grounding Live Pilot 004 Admission Packet

Status: Goal 9A proposed planning packet
Historical status: pre-run admission record; current run status is owned by `labs/chunked_source_grounding/EXPORTS/run_record.live_pilot_004.json`.
Lab: `chunked_source_grounding`
Experiment: `chunked_source_grounding_live_pilot_004`

This is a proposed live LLM pilot planning record. It is not a completed run, not research evidence, and not a synthesis export.

This packet was created before execution as planning/admission only.

The planning packet is not research evidence, not a synthesis export, and not a method success claim. No method success is claimed.

This pre-run planning packet itself contains no RunRecord, ArtifactEnvelope, EvaluationRecord, or ResearchNote.

Goal 8E found source-span precision improved on pilot 003 but still needs a second-source repeat.

---

## Hardening / Cleanup Discipline

Do not add around stale structure. Rework, replace, delete, or archive it.

This packet reuses the existing `live_llm_pilot_003` planning pattern because Goal 9A needs a comparable pre-run admission shape for a second source.

It does not blindly copy pilot 003 assumptions. Pilot 003 used the first approved source excerpt and passed manual content review with caveats. Goal 9A keeps the source-span precision contract and changes only the approved source scope.

This packet adds only the files needed for a distinct second-source repeat. It does not add scripts, shared helpers, protocol fields, synthesis features, benchmark packs, authority docs, or graduation claims.

---

## Active Benchmark Pack

Benchmark pack: `text_judgment_v0`

Known difficulty:

```text
Source-span precision may improve on one source excerpt while failing to repeat on a different messy trader transcript.
```

Known failure modes:

* source selection bias,
* broad support labels disguised as exact source spans,
* over-tight source hints that omit necessary context,
* unsupported claims hidden inside metadata-safe paraphrase,
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

---

## MethodCard

Proposed MethodCard:

```text
labs/chunked_source_grounding/PLANNING/live_llm_pilot_004/method_card.proposed.json
```

Method id:

```text
chunked_source_grounding_live_pilot_004_method
```

This proposed MethodCard is protocol-valid planning structure only. It is not in `EXPORTS/` and is not imported by synthesis.

---

## ExperimentCard

Proposed ExperimentCard:

```text
labs/chunked_source_grounding/PLANNING/live_llm_pilot_004/experiment_card.proposed.json
```

Experiment id:

```text
chunked_source_grounding_live_pilot_004
```

The experiment asks:

```text
Can the chunked/source-grounded source-span precision method that improved on pilot 003 generalize to a second source excerpt while staying complete, parseable, source-linked, and reviewable?
```

Result that would change future behavior:

```text
If the run produces complete parseable output with honest exact/approximate/broad/missing span labels on the second source, V3 can treat pilot 003's source-span precision improvement as repeatable enough for a preliminary comparison note. If it fails, V3 should treat the result as evidence about source selection, span-policy brittleness, or contract limits before another live call.
```

---

## Evaluator Plan

Evaluator plan:

```text
labs/chunked_source_grounding/PLANNING/live_llm_pilot_004/evaluator_plan.md
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
labs/chunked_source_grounding/PLANNING/live_llm_pilot_004/source_privacy_boundary.md
```

The live pilot must use the operator-approved second-source excerpt at the selected local path. Raw source material, provider payloads, private notes, raw prompts containing source text, and model traces must remain outside git unless a later explicit policy allows them.

Do not fall back to the full corpus path.

---

## Prompt / Template Hash Plan

Prompt/template path:

```text
labs/chunked_source_grounding/PLANNING/live_llm_pilot_004/prompt_template.live_pilot_004.md
```

The run admission update records the committed prompt template path and SHA-256 before execution.

Keep the pilot 003 source-span precision contract.

Do not re-expand the output contract.

Do not add broad judgment abstraction notes.

Do not add full comparison commentary.

Do not ask for a product-like study card.

Do not add strategy, validation, trading advice, or playbook content.

---

## Model / Config Recording Plan

Provider/model/config details are locked only in:

```text
labs/chunked_source_grounding/PLANNING/live_llm_pilot_004/run_admission_update.md
```

Goal 9A does not call the provider.

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

This pilot remains useful if it fails because it can record whether source-span precision:

* repeats on a second source,
* still collapses to broad support labels,
* makes the output incomplete or unparsable,
* creates false precision,
* preserves source grounding but loses useful abstraction,
* hides unsupported claims,
* or requires a canonical segmenting policy before another live call.

---

## Stop Condition

Stop condition:

```text
labs/chunked_source_grounding/PLANNING/live_llm_pilot_004/stop_condition.md
```

Goal 9A stops at planning/admission validation. Goal 9B, if separately authorized, should stop after one approved source scope and one approved model configuration.

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

Any future output from this pilot is proposal-only until evaluated. It is not source truth, validation, product authority, strategy evidence, financial advice, live-trading authority, graduation, or architecture.
