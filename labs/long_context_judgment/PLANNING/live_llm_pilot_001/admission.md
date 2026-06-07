# Live LLM Pilot 001 Admission Packet

Status: proposed planning packet  
Lab: `long_context_judgment`  
Experiment: `long_context_judgment_live_pilot_001`

This is a proposed live LLM pilot planning record. It is not a completed run, not research evidence, and not a synthesis export.

No LLM call has been made. No output artifact has been produced. No evaluation result exists. No method success is claimed.

This packet prepares a future admission decision only. It does not authorize execution by itself.

---

## Active Benchmark Pack

Benchmark pack: `text_judgment_v0`

Known difficulty:

```text
Long-form trader language can preserve intent while losing exact source boundaries.
```

Known failure modes:

* over-abstracts teacher intent,
* weakens source grounding,
* turns fixture output into evidence.

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
labs/long_context_judgment/PLANNING/live_llm_pilot_001/method_card.proposed.json
```

Method id:

```text
long_context_judgment_live_pilot_001_method
```

This proposed MethodCard is protocol-valid planning structure only. It is not in `EXPORTS/` and is not imported by synthesis.

---

## ExperimentCard

Proposed ExperimentCard:

```text
labs/long_context_judgment/PLANNING/live_llm_pilot_001/experiment_card.proposed.json
```

Experiment id:

```text
long_context_judgment_live_pilot_001
```

The experiment asks:

```text
Can a long-context LLM method extract reusable trading judgment from messy trader text without losing grounding?
```

Result that would change future behavior:

```text
If the run produces source-linked judgment proposals while preserving unsupported-claim visibility, V3 can consider a second controlled long-context run or a comparison against chunked source-grounding. If it over-abstracts or loses grounding, the negative result should steer the next milestone toward chunked or hybrid methods before more long-context runs.
```

---

## Evaluator Plan

Evaluator plan:

```text
labs/long_context_judgment/PLANNING/live_llm_pilot_001/evaluator_plan.md
```

Planned evaluator types:

* `schema_check`
* `human_placeholder`

No evaluator has run. No evaluation result exists.

---

## Source / Privacy Boundary

Source/privacy boundary:

```text
labs/long_context_judgment/PLANNING/live_llm_pilot_001/source_privacy_boundary.md
```

The live pilot may use one controlled messy trader text source scope. Raw source material, provider payloads, private notes, raw prompts containing source text, and model traces must remain outside git unless a later explicit policy allows them.

---

## Prompt / Template Hash Plan

Prompt/template hash plan:

```text
labs/long_context_judgment/PLANNING/live_llm_pilot_001/prompt_config_recording_plan.md
```

The future run must record hashes for the prompt template, system prompt, and any tool instructions before execution.

---

## Model / Config Recording Plan

Model/config recording plan:

```text
labs/long_context_judgment/PLANNING/live_llm_pilot_001/prompt_config_recording_plan.md
```

No provider or model is selected in this planning packet. A future run admission update must record provider id, model id, sampling settings, context settings, tool routing, and config hash before any LLM call.

---

## Output Artifact Types

Expected post-run artifact types:

* `judgment_principle_proposal`
* `source_grounded_claim`
* `unsupported_claim_report`

No ArtifactEnvelope exists for this pilot yet.

---

## Negative-Result Value

This pilot remains useful if it fails because it can record whether long-context reading:

* loses exact source grounding,
* over-abstracts trader intent,
* hides unsupported claims,
* needs chunked source spans before abstraction,
* or requires a different evaluator before comparison work.

---

## Stop Condition

Stop condition:

```text
labs/long_context_judgment/PLANNING/live_llm_pilot_001/stop_condition.md
```

The future live pilot should stop after one approved source scope and one approved model configuration. Prompt, source, or model changes require a separate admission update before another live call.

---

## Budget / Secrets Handling

No budget is authorized by this planning packet.

Before execution, a future admission update must record:

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
