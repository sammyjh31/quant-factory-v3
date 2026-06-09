# Chunked Source Grounding Live Pilot 001 Admission Packet

Status: proposed planning packet
Historical status: pre-run admission record; current run status is owned by `labs/chunked_source_grounding/EXPORTS/run_record.live_pilot_001.json`.
Lab: `chunked_source_grounding`
Experiment: `chunked_source_grounding_live_pilot_001`

This is a proposed live LLM pilot planning record. It is not a completed run, not research evidence, and not a synthesis export.

This packet was created before execution as planning/admission only.

The planning packet is not research evidence, not a synthesis export, and not a method success claim. No method success is claimed.

This pre-run planning packet itself contains no RunRecord, ArtifactEnvelope, EvaluationRecord, or ResearchNote.

---

## Hardening / Cleanup Discipline

Do not add around stale structure. Rework, replace, delete, or archive it.

This packet reuses the existing lab planning pattern from `long_context_judgment` because Goal 7A needs a comparable pre-run admission shape.

This packet adds only the files needed for the distinct chunked/source-grounded method. It does not add scripts, shared helpers, protocol fields, synthesis features, benchmark packs, authority docs, or graduation claims.

The long-context packet remains the owner for the first pilot. This packet is local to `chunked_source_grounding`.

---

## Active Benchmark Pack

Benchmark pack: `text_judgment_v0`

Known difficulty:

```text
Chunked source-grounding can preserve exact support while losing broader source intent.
```

Known failure modes:

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
labs/chunked_source_grounding/PLANNING/live_llm_pilot_001/method_card.proposed.json
```

Method id:

```text
chunked_source_grounding_live_pilot_001_method
```

This proposed MethodCard is protocol-valid planning structure only. It is not in `EXPORTS/` and is not imported by synthesis.

---

## ExperimentCard

Proposed ExperimentCard:

```text
labs/chunked_source_grounding/PLANNING/live_llm_pilot_001/experiment_card.proposed.json
```

Experiment id:

```text
chunked_source_grounding_live_pilot_001
```

The experiment asks:

```text
Can a chunked/source-grounded LLM method preserve exact source grounding better than the long-context method, and what broader trading-judgment abstraction does it lose?
```

Result that would change future behavior:

```text
If the run preserves exact source support but loses broader judgment abstraction, V3 should compare chunked and long-context methods explicitly before adding more live calls. If it improves grounding without losing abstraction, V3 can consider a second chunked run or hybrid method. If it fails both grounding and abstraction, evaluator quality or prompt structure should be improved first.
```

---

## Evaluator Plan

Evaluator plan:

```text
labs/chunked_source_grounding/PLANNING/live_llm_pilot_001/evaluator_plan.md
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
labs/chunked_source_grounding/PLANNING/live_llm_pilot_001/source_privacy_boundary.md
```

The live pilot must use the same approved excerpt as `long_context_judgment_live_pilot_001`. Raw source material, provider payloads, private notes, raw prompts containing source text, and model traces must remain outside git unless a later explicit policy allows them.

---

## Prompt / Template Hash Plan

Prompt/template path:

```text
labs/chunked_source_grounding/PLANNING/live_llm_pilot_001/prompt_template.live_pilot_001.md
```

The run admission update records the committed prompt template path and SHA-256 before execution.

---

## Model / Config Recording Plan

Provider/model/config details are locked only in:

```text
labs/chunked_source_grounding/PLANNING/live_llm_pilot_001/run_admission_update.md
```

Goal 7A does not call the provider.

---

## Output Artifact Types

Expected post-run artifact type:

* `chunked_source_grounding_proposal`

Expected output sections:

* source-linked claim table,
* segment/span support notes,
* unsupported-claim report,
* judgment abstraction notes,
* method-failure notes.

---

## Negative-Result Value

This pilot remains useful if it fails because it can record whether chunked/source-grounded reading:

* preserves exact support while losing broader judgment,
* creates too many local claims without useful abstraction,
* misses unsupported promotional claims,
* needs a different chunk size or span policy,
* or requires evaluator calibration before another live call.

---

## Stop Condition

Stop condition:

```text
labs/chunked_source_grounding/PLANNING/live_llm_pilot_001/stop_condition.md
```

Goal 7A stops at planning/admission validation. Goal 7B, if separately authorized, should stop after one approved source scope and one approved model configuration.

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
