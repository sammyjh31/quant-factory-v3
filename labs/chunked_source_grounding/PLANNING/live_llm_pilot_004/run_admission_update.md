# Chunked Source Grounding Live Pilot 004 Run Admission Update

Status: Goal 9A live-run admission update for one future proposal-only pilot

This admission update defines the executable preflight scope for exactly one future tiny live LLM pilot run.

It does not by itself authorize execution. Execution requires a separate Goal 9B instruction.

Goal 9A does not execute the run. No LLM call has been made for `chunked_source_grounding_live_pilot_004`.

This update itself is not research evidence and not a synthesis export. It does not create a RunRecord, ArtifactEnvelope, EvaluationRecord, ResearchNote, generated synthesis claim, graduation status, or architecture.

---

## Authority Boundary

This update narrows the Goal 9A planning packet into one executable preflight scope for Goal 9B if separately authorized.

Outputs from this experiment are proposals until evaluated. They do not create source truth, role support, data truth, validation, strategy evidence, financial advice, product authority, live-trading authority, or architecture.

No validation, product authority, strategy evidence, financial advice, live-trading authority, or architecture is created by this admission update or by any future raw model output.

Do not add around stale structure. Rework, replace, delete, or archive it.

The source-span precision pilot 003 record remains the current completed source-span precision run and is not overwritten by this second-source repeat.

---

## Provider And Model

Provider: DeepSeek API

API format: OpenAI-compatible chat completions

Base URL: `https://api.deepseek.com`

Model: `deepseek-v4-pro`

Reasoning/thinking mode: non-thinking, recorded as `thinking: {"type": "disabled"}`.

Tool routing: tools disabled; no retrieval tools, browser tools, code tools, or file tools are authorized for this pilot.

If `deepseek-v4-pro` is unavailable in the account, stop and report. Do not silently substitute `deepseek-v4-flash`, `deepseek-chat`, `deepseek-reasoner`, or any other model.

---

## Lab, Benchmark, And Purpose

Lab: `labs/chunked_source_grounding`

Benchmark pack: `text_judgment_v0`

Purpose: test whether the source-span precision contract from pilot 003 repeats on a second operator-approved source excerpt while staying complete, parseable, source-linked, and reviewable.

Research question:

```text
Can the chunked/source-grounded source-span precision method that improved on pilot 003 generalize to a second source excerpt while staying complete, parseable, source-linked, and reviewable?
```

This pilot tests a deliberate second-source repeat, not a replacement for `chunked_source_grounding_live_pilot_003`.

---

## Run Scope

The defined run scope is:

* one tiny pilot,
* one approved source scope,
* one prompt/template version,
* one model configuration,
* one model-call batch.

No retries unless the call fails before producing output.

Any source, prompt, model, budget, evaluator, artifact type, output contract, span policy, chunking policy, or retry-policy change requires a separate admission update before another live call.

---

## Source Scope

Approved source scope:

```text
operator-approved second-source excerpt from the local pharm box-trades transcript
```

Canonical source ref:

```text
raw_corpora_sha256:9f9e143429f5842a
```

Full selected excerpt SHA-256: `9f9e143429f5842a9c03c95b1f7705d85fb664cf795c30919a582fa66b16fbb5`

Selected excerpt word count: `945`

Preferred local operator path:

```text
raw_corpora/selected/source_span_precision_repeat_001/source.txt
```

Recorded local source origin:

```text
raw_corpora/trader_source_corpus/pharm/box trades_999923657.txt
```

The source text must stay local-only or ignored. The committed record may include source scope identifiers, source span hints, support hint quality labels, and metadata-safe summaries, but not raw private source text unless a later explicit policy allows it.

No private/raw source material or provider payloads are committed.

Do not fall back to the full corpus path.

---

## Prompt Template

Prompt/template path:

```text
labs/chunked_source_grounding/PLANNING/live_llm_pilot_004/prompt_template.live_pilot_004.md
```

Prompt template SHA-256: `859d1271ca060f1a349b51101192c0cb0d395f3bbc401d35eb71c2a7316f3bfb`

The prompt template contains placeholders only. It does not contain raw source text, private notes, provider payloads, or secrets.

System prompt source: the `System Message` section inside the same prompt template file.

Tool instruction hash: none. Tools are disabled.

Prompt traces that include source text must be stored only under ignored local paths.

The output contract remains the source-span precision contract from pilot 003.

It keeps:

* source-linked claim table,
* tighter source-span support hints,
* unsupported-claim report,
* brief method-failure notes.

It excludes:

* broad judgment abstraction notes,
* full comparison commentary,
* product-like study cards,
* strategy or validation content,
* trading advice,
* playbook content.

---

## Canonical Model Config

```json
{
  "api_format": "openai_compatible_chat_completions",
  "base_url": "https://api.deepseek.com",
  "context_window_provider_limit": "1M",
  "max_input_tokens": 12000,
  "max_output_tokens": 1200,
  "model_id": "deepseek-v4-pro",
  "provider_id": "deepseek_api",
  "sampling": {
    "frequency_penalty": null,
    "presence_penalty": null,
    "temperature": null,
    "top_p": null
  },
  "stream": false,
  "thinking": {
    "type": "disabled"
  },
  "tool_routing": "none"
}
```

Config SHA-256: `a8a8daccf08254a827fd5d68203d41f56b25c295e14e4005f9671fd0bd46a9cb`

Sampling settings: provider defaults, with no temperature, top-p, presence-penalty, or frequency-penalty override.

Context/token settings: cap the runtime input below `12000` tokens and output below `1200` tokens even though the provider documents a larger context window.

The max output cap remains intentionally small; this run tests whether the pilot 003 source-span precision contract can repeat on a second source without expanding scope.

---

## Budget And Secrets

Budget cap: `$3` hard maximum.

The operator must stop before the call if the estimated request cost, account state, or provider pricing would make the run exceed the budget cap.

Required secret environment variable name:

```text
DEEPSEEK_API_KEY
```

Use `DEEPSEEK_API_KEY` only through environment variables; never commit secrets.

No API key, account id, request id, provider payload, prompt trace containing source text, or raw model trace may be committed.

---

## Trace And Log Storage

Allowed local-only or ignored trace paths:

```text
provider_payloads/chunked_source_grounding_live_pilot_004/
model_traces/chunked_source_grounding_live_pilot_004/
prompt_traces/chunked_source_grounding_live_pilot_004/
```

These paths are covered by top-level ignored directories. They may hold raw request/response details only outside git.

Committed post-run records must contain metadata-safe summaries and protocol records only.

---

## Expected Post-Run Files

After the live run, and only after the live run, create protocol-valid records at:

```text
labs/chunked_source_grounding/EXPORTS/run_record.live_pilot_004.json
labs/chunked_source_grounding/EXPORTS/artifact_envelope.live_pilot_004.json
labs/chunked_source_grounding/EXPORTS/evaluation_record.live_pilot_004.json
labs/chunked_source_grounding/EXPORTS/research_note.live_pilot_004.json
```

The expected artifact type is:

```text
chunked_source_span_precision_proposal
```

These records must be proposal-only and non-authoritative. They must not include raw source text, private notes, secrets, raw provider payloads, prompt traces, or model traces.
