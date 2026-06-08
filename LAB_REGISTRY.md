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
scaffold fixture exports plus one admitted proposal-only chunked/source-grounded live pilot export set plus one failure-focused manual content-review EvaluationRecord, plus one admitted DeepSeek V4 Pro chunked/source-grounded live pilot export set and one DeepSeek V4 Pro manual content-review EvaluationRecord, plus one admitted DeepSeek V4 Pro source-span precision live pilot export set and one DeepSeek V4 Pro source-span precision manual content-review EvaluationRecord
```

Proposed planning packets:

```text
labs/chunked_source_grounding/PLANNING/live_llm_pilot_001/
labs/chunked_source_grounding/PLANNING/live_llm_pilot_002/
labs/chunked_source_grounding/PLANNING/live_llm_pilot_003/
labs/chunked_source_grounding/PLANNING/live_llm_pilot_004/
```

Planning experiment ids:

```text
chunked_source_grounding_live_pilot_001
chunked_source_grounding_live_pilot_002
chunked_source_grounding_live_pilot_003
chunked_source_grounding_live_pilot_004
```

The proposed MethodCard and ExperimentCard planning records are not in `EXPORTS/`, are not imported by synthesis, and are not live-run evidence. The second packet defined the preflight scope for a DeepSeek V4 Pro rerun with a smaller output contract. The third packet defined the source-span precision scope for the DeepSeek V4 Pro pilot 003 run. The fourth packet defines the second-source source-span precision scope for `chunked_source_grounding_live_pilot_004`; no model call or export records exist for that pilot yet.

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

The Pro/narrow-contract planning packet lives at:

```text
labs/chunked_source_grounding/PLANNING/live_llm_pilot_002/
```

Goal 7E executed the admitted `chunked_source_grounding_live_pilot_002` one-call scope and created one admitted DeepSeek V4 Pro chunked/source-grounded live pilot export set:

```text
labs/chunked_source_grounding/EXPORTS/run_record.live_pilot_002.json
labs/chunked_source_grounding/EXPORTS/artifact_envelope.live_pilot_002.json
labs/chunked_source_grounding/EXPORTS/evaluation_record.live_pilot_002.json
labs/chunked_source_grounding/EXPORTS/evaluation_record.live_pilot_002_manual_content_review.json
labs/chunked_source_grounding/EXPORTS/research_note.live_pilot_002.json
```

The Pro run produced complete parseable JSON under the smaller output contract. The manual content review passed with caveats: the artifact was content-reviewable and source-linked at a claim level, while segment refs remained broad and the narrowed contract limited broader abstraction. It creates no protocol change, no synthesis feature, no graduation status, and no method-quality conclusion beyond this proposal-only manual review.

The source-span precision planning packet lives at:

```text
labs/chunked_source_grounding/PLANNING/live_llm_pilot_003/
```

Goal 8C executed the admitted `chunked_source_grounding_live_pilot_003` one-call scope and created one admitted DeepSeek V4 Pro source-span precision live pilot export set:

```text
labs/chunked_source_grounding/EXPORTS/run_record.live_pilot_003.json
labs/chunked_source_grounding/EXPORTS/artifact_envelope.live_pilot_003.json
labs/chunked_source_grounding/EXPORTS/evaluation_record.live_pilot_003.json
labs/chunked_source_grounding/EXPORTS/research_note.live_pilot_003.json
labs/chunked_source_grounding/EXPORTS/evaluation_record.live_pilot_003_manual_content_review.json
```

The source-span precision run produced complete parseable JSON under the narrowed output contract and kept raw source, prompt, provider response, and model output in ignored local traces. The manual content review passed with caveats: source-span precision improved relative to pilot 002, exact/approximate labels were warranted for the reviewed claims, and the artifact still lacks canonical offsets and broader abstraction. It creates no protocol change, no synthesis feature, no graduation status, and no method-quality conclusion beyond this proposal-only manual review.

The second-source source-span precision planning packet lives at:

```text
labs/chunked_source_grounding/PLANNING/live_llm_pilot_004/
```

Goal 9A created a planning/admission packet for `chunked_source_grounding_live_pilot_004` using an operator-approved second-source excerpt. It is planning structure only: no LLM call, no export records, no research evidence, no synthesis import, no graduation status, and no architecture.

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

Labs export protocol-valid records appropriate to their current phase. Scaffold fixtures, proposal-only live runs, manual reviews, and future experiment records must remain clearly labeled and must not claim protocol authority, graduation, validation, product evidence, strategy evidence, financial advice, live-trading authority, or architecture.

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
