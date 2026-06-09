# Long Context Judgment Live Pilot 002 Admission Packet

Status: Goal 13B proposed planning packet
Lab: `long_context_judgment`
Experiment: `long_context_judgment_live_pilot_002`

This is a proposed live LLM pilot planning record. It is not a completed run, not research evidence, and not a synthesis export.

This packet was created before execution as planning/admission only. Execution requires a separately authorized Goal 13C instruction.

The planning packet is not research evidence, not a synthesis export, and not a method success claim. No method success is claimed.

This pre-run planning packet itself contains no RunRecord, ArtifactEnvelope, EvaluationRecord, or ResearchNote.

The Goal 13A locator-thread decision review paused the chunked locator thread and recommended planning a stricter grounded long-context variant. Goal 13B turns that recommendation into a contained live-run admission packet without executing the run.

The owning comparison note is:

```text
labs/chunked_source_grounding/PLANNING/comparisons/live_pilot_method_comparison_001.md
```

---

## Hardening / Cleanup Discipline

Do not add around stale structure. Rework, replace, delete, or archive it.

This packet reuses the existing live pilot planning pattern because Goal 13B needs a comparable pre-run admission shape for a grounded long-context pilot.

It does not blindly copy pilot 001 assumptions. Pilot 001 asked for span hints with no locator contract; Goal 13B requires a line-range locator candidate for every source-linked claim, adopting the line-range-first lesson from the chunked_source_grounding Goal 13A decision review.

It does not blindly copy chunked pilot 006 assumptions either. Pilot 006 excluded broad judgment abstraction; Goal 13B deliberately reintroduces judgment principle proposals on top of the locator discipline, because recovering abstraction breadth is the variable under test.

This packet adds only the files needed for a distinct live-run admission packet. It does not add scripts, shared helpers, protocol fields, synthesis features, benchmark packs, authority docs, or graduation claims.

## Comparison Question Reuse

Goal 13B tests the comparison question recorded in the Goal 13A decision review:

```text
Can long-context preserve broader judgment abstraction while adopting the source-grounding / line-range discipline learned from chunked_source_grounding?
```

The locator policy is reused from the line-range-first lesson:

* the model emits line-range locator candidates only,
* do not ask the model to emit character offsets,
* do not ask the model to emit quote hashes,
* local review/tooling computes character offsets only after line-range validation,
* quote hashes are computed locally only from validated spans.

## Active Benchmark Pack

Benchmark pack: `text_judgment_v0`

Known difficulty:

```text
Long-form trader language can preserve intent while losing exact source boundaries, and grounding pressure can flatten broader judgment back into narrow claims.
```

Known failure modes:

* over-abstracts teacher intent,
* abstraction reverts to generic advice under grounding pressure,
* limited_abstraction repeats despite the reintroduced principle contract,
* broad line ranges disguised as exact support,
* invalid line numbers,
* judgment principles cite claims that do not actually support them,
* locator confidence overstates source precision,
* unsupported claims hidden inside metadata-safe paraphrase,
* combined contract exceeds the output cap before method quality is testable,
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
labs/long_context_judgment/PLANNING/live_llm_pilot_002/method_card.proposed.json
```

Method id:

```text
long_context_judgment_live_pilot_002_method
```

This proposed MethodCard is protocol-valid planning structure only. It is not in `EXPORTS/` and is not imported by synthesis.

## ExperimentCard

Proposed ExperimentCard:

```text
labs/long_context_judgment/PLANNING/live_llm_pilot_002/experiment_card.proposed.json
```

Experiment id:

```text
long_context_judgment_live_pilot_002
```

The experiment asks:

```text
Can a grounded long-context contract preserve broader judgment abstraction while requiring line-range source support for every source-linked claim?
```

Result that would change future behavior:

```text
If the run produces judgment principle proposals that preserve conditional logic and cite support-valid line ranges, V3 has its first signal that grounding discipline and abstraction breadth are compatible in one contract, and can plan a repeat on a second source. If abstraction reverts to generic advice, locator quality degrades versus pilot 006, or the contract fails structurally, the negative result should steer future work toward two-pass or recursive reading methods instead of single-pass grounded long-context contracts.
```

## Evaluator Plan

Evaluator plan:

```text
labs/long_context_judgment/PLANNING/live_llm_pilot_002/evaluator_plan.md
```

Planned evaluator types:

* `schema_check`
* `manual_boundary_review`
* `manual_content_review`

The planning packet does not create an EvaluationRecord.

## Source / Privacy Boundary

Source/privacy boundary:

```text
labs/long_context_judgment/PLANNING/live_llm_pilot_002/source_privacy_boundary.md
```

The live pilot must use the same selected second-source excerpt as chunked_source_grounding pilots 004, 005, and 006, so that locator quality is directly comparable across methods. Raw source material, provider payloads, private notes, raw prompts containing source text, and model traces must remain outside git unless a later explicit policy allows them.

Do not fall back to the full corpus path.

## Prompt / Template Hash Plan

Prompt/template path:

```text
labs/long_context_judgment/PLANNING/live_llm_pilot_002/prompt_template.live_pilot_002.md
```

The run admission update records the committed prompt template path and SHA-256 before execution.

Keep the output contract bounded:

* judgment principle proposal table,
* source-linked claim table,
* line-range locator candidate table,
* unsupported-claim report,
* brief method-failure notes.

Do not ask the model to emit character offsets.

Do not ask the model to emit quote hashes.

Do not add full comparison commentary.

Do not ask for a product-like study card.

Do not add strategy, validation, trading advice, or playbook content.

## Model / Config Recording Plan

Provider/model/config details are locked only in:

```text
labs/long_context_judgment/PLANNING/live_llm_pilot_002/run_admission_update.md
```

Goal 13B does not call the provider.

## Output Artifact Types

Expected post-run artifact type:

* `grounded_long_context_judgment_proposal`

Expected output sections:

* judgment principle proposal table,
* source-linked claim table,
* line-range locator candidate table,
* unsupported-claim report,
* brief method-failure notes.

Not requested in this run:

* character offsets,
* quote hashes,
* full comparison commentary,
* product-like study card,
* strategy or validation content,
* trading advice,
* playbook content.

## Negative-Result Value

This pilot remains useful if it fails because it can record whether a grounded long-context contract:

* flattens broader judgment back into narrow claims,
* reverts abstraction to generic advice under grounding pressure,
* produces principles whose cited claims do not support them,
* degrades line-range locator quality relative to pilot 006,
* exceeds the output cap before method quality is testable,
* hides unsupported claims,
* or shows that abstraction breadth and grounding discipline need a two-pass or recursive method rather than one contract.

## Stop Condition

Stop condition:

```text
labs/long_context_judgment/PLANNING/live_llm_pilot_002/stop_condition.md
```

Goal 13B stops at planning/admission validation. Goal 13C, if separately authorized, should stop after one approved source scope and one approved model configuration.

## Budget / Secrets Handling

Budget cap: `$3` hard maximum.

Required secret name:

```text
DEEPSEEK_API_KEY
```

The secret name may be documented. The secret value must never be committed.

## Proposal-Only Statement

Outputs from this experiment are proposals until evaluated. They do not create source truth, role support, data truth, validation, strategy evidence, financial advice, product authority, live-trading authority, or architecture.
