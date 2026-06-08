# Lab Registry

Status: lab currentness router  
Current phase: `milestone-2-live-pilot-recorded`

This file lists labs and their parent research questions. It does not claim that any method works.

---

## Active Scaffold Labs

### `long_context_judgment`

Path:

```text
labs/long_context_judgment/
```

Parent research question:

```text
How can long-context LLM methods extract reusable trading judgment from messy trader text?
```

Current state:

```text
scaffold fixture exports plus one admitted proposal-only live pilot export set and one manual content-review EvaluationRecord
```

Required fixture posture:

* one positive fixture run,
* one negative fixture run,
* protocol-valid fixture artifacts,
* evaluation records,
* research note with scaffold disclaimer.

Proposed planning packet:

```text
labs/long_context_judgment/PLANNING/live_llm_pilot_001/
```

Planning experiment id:

```text
long_context_judgment_live_pilot_001
```

The proposed MethodCard and ExperimentCard planning records are not in `EXPORTS/`, are not imported by synthesis, and are not live-run evidence.

Run admission update:

```text
labs/long_context_judgment/PLANNING/live_llm_pilot_001/run_admission_update.md
```

The run admission update authorized exactly one tiny live LLM pilot run under the stated scope. The update itself did not create RunRecord, ArtifactEnvelope, EvaluationRecord, or ResearchNote records.

The authorized live pilot has now produced one proposal-only export set and one manual content-review EvaluationRecord:

```text
labs/long_context_judgment/EXPORTS/run_record.live_pilot_001.json
labs/long_context_judgment/EXPORTS/artifact_envelope.live_pilot_001.json
labs/long_context_judgment/EXPORTS/evaluation_record.live_pilot_001.json
labs/long_context_judgment/EXPORTS/evaluation_record.live_pilot_001_manual_content_review.json
labs/long_context_judgment/EXPORTS/research_note.live_pilot_001.json
```

The live export set and manual content-review EvaluationRecord are proposal-only and do not create validation, product evidence, strategy evidence, financial advice, live-trading authority, graduation, or architecture.

---

### `chunked_source_grounding`

Path:

```text
labs/chunked_source_grounding/
```

Parent research question:

```text
How can chunked/source-span LLM methods preserve source grounding while still supporting useful abstraction?
```

Current state:

```text
scaffold fixture exports plus one admitted proposal-only chunked/source-grounded live pilot export set plus one failure-focused manual content-review EvaluationRecord
```

Proposed planning packet:

```text
labs/chunked_source_grounding/PLANNING/live_llm_pilot_001/
```

Planning experiment id:

```text
chunked_source_grounding_live_pilot_001
```

The proposed MethodCard and ExperimentCard planning records are not in `EXPORTS/`, are not imported by synthesis, and are not live-run evidence.

Run admission update:

```text
labs/chunked_source_grounding/PLANNING/live_llm_pilot_001/run_admission_update.md
```

The run admission update defined the executable preflight scope for exactly one future live LLM pilot run under the stated scope. Goal 7B executed that admitted one-call scope and created one proposal-only export set.

The authorized live pilot has now produced one proposal-only export set and one failure-focused manual content-review EvaluationRecord:

```text
labs/chunked_source_grounding/EXPORTS/run_record.live_pilot_001.json
labs/chunked_source_grounding/EXPORTS/artifact_envelope.live_pilot_001.json
labs/chunked_source_grounding/EXPORTS/evaluation_record.live_pilot_001.json
labs/chunked_source_grounding/EXPORTS/evaluation_record.live_pilot_001_manual_content_review.json
labs/chunked_source_grounding/EXPORTS/research_note.live_pilot_001.json
```

The live export set is proposal-only comparison work against `long_context_judgment_live_pilot_001` and does not create validation, product evidence, strategy evidence, financial advice, live-trading authority, graduation, or architecture. The model output reached the configured output-token cap before complete JSON parsing. The manual content review records that as a failure of this admitted Flash run/config/output contract, not a global method-quality conclusion.

---

### `visual_deictic_understanding`

Path:

```text
labs/visual_deictic_understanding/
```

Parent research question:

```text
How can multimodal or vision-language LLM workflows bind transcript/deictic language to visual chart context?
```

Current state:

```text
scaffold fixture exports only
```

---

## Lab Independence Rule

Labs may use different internal methods, assumptions, prompts, models, dependencies, and artifact formats in future milestones.

During scaffold, labs export only protocol fixture records.

Labs do not define protocol authority.

Labs do not graduate methods.

Labs do not define portfolio architecture.

---

## Shared Code Rule

Labs should not share lab-runtime code in milestone one.

Shared code is limited to protocol validation and read-only synthesis.

Future shared lab helper code requires:

1. repeated use across at least two labs,
2. clear evidence that duplication is harmful,
3. an ADR,
4. and no expansion of protocol authority by accident.
