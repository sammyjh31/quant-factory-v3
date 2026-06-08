# Chunked Source Grounding Live Pilot 005 Admission Packet

Status: Goal 11B proposed planning packet
Lab: `chunked_source_grounding`
Experiment: `chunked_source_grounding_live_pilot_005`

This is a proposed live LLM pilot planning record. It is not a completed run, not research evidence, and not a synthesis export.

This is planning/admission only. No LLM call has been made.

The planning packet is not research evidence, not a synthesis export, and not a method success claim. No method success is claimed.

No RunRecord, ArtifactEnvelope, EvaluationRecord, or ResearchNote exists for this pilot.

Goal 11A planned a source-span locator output contract. Goal 11B turns that plan into a contained live-run admission packet without executing the run.

---

## Hardening / Cleanup Discipline

Do not add around stale structure. Rework, replace, delete, or archive it.

This packet reuses the existing live pilot planning pattern because Goal 11B needs a comparable pre-run admission shape for a source-span locator candidate pilot.

It does not blindly copy pilot 004 assumptions. Pilot 004 used source-span support hints and strict review reconstructed locators after the fact. Goal 11B narrows the prompt to source-linked claims plus locator candidates.

This packet adds only the files needed for a distinct live-run admission packet. It does not add scripts, shared helpers, protocol fields, synthesis features, benchmark packs, authority docs, or graduation claims.

## Goal 11A Cleanup

Goal 11B first clarifies the Goal 11A contract:

* the model emits line/offset locator candidates;
* local runner/reviewer computes quote hashes from selected local source spans;
* committed records may include metadata-safe computed quote hashes but not raw source text.

Do not ask the model to emit quote hashes.

## Active Benchmark Pack

Benchmark pack: `text_judgment_v0`

Known difficulty:

```text
The model may still provide broad support hints instead of canonical line ranges and character offsets.
```

Known failure modes:

* broad support labels disguised as exact source spans,
* line ranges and character offsets disagree,
* locator confidence overstates source precision,
* unsupported claims hidden inside metadata-safe paraphrase,
* false precision from local spans that omit required context,
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
labs/chunked_source_grounding/PLANNING/live_llm_pilot_005/method_card.proposed.json
```

Method id:

```text
chunked_source_grounding_live_pilot_005_method
```

This proposed MethodCard is protocol-valid planning structure only. It is not in `EXPORTS/` and is not imported by synthesis.

## ExperimentCard

Proposed ExperimentCard:

```text
labs/chunked_source_grounding/PLANNING/live_llm_pilot_005/experiment_card.proposed.json
```

Experiment id:

```text
chunked_source_grounding_live_pilot_005
```

The experiment asks:

```text
Can the model emit canonical locator candidates directly -- line ranges and character offsets -- so local review can compute quote hashes from the proposed spans instead of reconstructing support after the fact?
```

Result that would change future behavior:

```text
If the run produces complete parseable output with usable line ranges, character offsets, and honest locator labels, V3 can compare direct locator-candidate output against reviewer-reconstructed locators from pilots 003 and 004. If it fails, V3 should treat the result as evidence about locator-contract brittleness before another live call.
```

## Evaluator Plan

Evaluator plan:

```text
labs/chunked_source_grounding/PLANNING/live_llm_pilot_005/evaluator_plan.md
```

Planned evaluator types:

* `schema_check`
* `manual_boundary_review`
* `manual_content_review`

The planning packet does not create an EvaluationRecord.

## Source / Privacy Boundary

Source/privacy boundary:

```text
labs/chunked_source_grounding/PLANNING/live_llm_pilot_005/source_privacy_boundary.md
```

The live pilot must use the same approved source as pilot 004 unless a later admission update changes scope. Raw source material, provider payloads, private notes, raw prompts containing source text, and model traces must remain outside git unless a later explicit policy allows them.

Do not fall back to the full corpus path.

## Prompt / Template Hash Plan

Prompt/template path:

```text
labs/chunked_source_grounding/PLANNING/live_llm_pilot_005/prompt_template.live_pilot_005.md
```

The run admission update records the committed prompt template path and SHA-256 before execution.

Keep the output contract narrow:

* source-linked claim table,
* locator candidate table,
* unsupported-claim report,
* brief method-failure notes.

Do not ask the model to emit quote hashes.

Do not add broad judgment abstraction notes.

Do not add full comparison commentary.

Do not ask for a product-like study card.

Do not add strategy, validation, trading advice, or playbook content.

## Model / Config Recording Plan

Provider/model/config details are locked only in:

```text
labs/chunked_source_grounding/PLANNING/live_llm_pilot_005/run_admission_update.md
```

Goal 11B does not call the provider.

## Output Artifact Types

Expected post-run artifact type:

* `chunked_source_span_locator_candidate_proposal`

Expected output sections:

* source-linked claim table,
* locator candidate table,
* unsupported-claim report,
* brief method-failure notes.

Not requested in this run:

* broad judgment abstraction notes,
* full comparison commentary,
* product-like study card,
* strategy or validation content,
* trading advice,
* playbook content.

## Negative-Result Value

This pilot remains useful if it fails because it can record whether direct locator candidates:

* reduce reviewer reconstruction work,
* remain too broad to compute useful quote hashes,
* produce disagreeing line ranges and character offsets,
* create false precision,
* preserve source grounding but lose useful abstraction,
* hide unsupported claims,
* or require local pre-segmentation before another live call.

## Stop Condition

Stop condition:

```text
labs/chunked_source_grounding/PLANNING/live_llm_pilot_005/stop_condition.md
```

Goal 11B stops at planning/admission validation. Goal 11C, if separately authorized, should stop after one approved source scope and one approved model configuration.

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

## Proposal-Only Statement

Any future output from this pilot is proposal-only until evaluated. It is not source truth, validation, product authority, strategy evidence, financial advice, live-trading authority, graduation, or architecture.
