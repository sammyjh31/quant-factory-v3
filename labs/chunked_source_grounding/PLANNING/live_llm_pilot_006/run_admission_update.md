# Chunked Source Grounding Live Pilot 006 Run Admission Update

Status: Goal 12B live-run admission update for pilot 006

This admission update defines the executable preflight scope for exactly one tiny live LLM pilot run.

It does not by itself authorize execution. Execution requires a separate Goal 12C instruction.

Goal 12B did not execute the run or create export records for `chunked_source_grounding_live_pilot_006`.

This update itself is not research evidence and not a synthesis export. It does not create a RunRecord, ArtifactEnvelope, EvaluationRecord, ResearchNote, generated synthesis claim, graduation status, or architecture.

---

## Authority Boundary

This update narrows the Goal 12B planning packet into one executable preflight scope for Goal 12C if separately authorized.

Outputs from this experiment are proposals until evaluated. They do not create source truth, role support, data truth, validation, strategy evidence, financial advice, product authority, live-trading authority, or architecture.

No validation, product authority, strategy evidence, financial advice, live-trading authority, or architecture is created by this admission update or by any future raw model output.

Do not add around stale structure. Rework, replace, delete, or archive it.

Pilot 005 remains the completed line-plus-offset locator attempt and is not overwritten by this line-range-first pilot.

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

Purpose: test whether a line-range-first locator contract can make the model emit reviewable line-range support regions directly, while local review/tooling computes character offsets and quote hashes only after line-range validation.

Research question:

```text
Can the model emit reviewable line-range locator candidates directly, while local review/tooling computes character offsets and quote hashes only after line-range validation?
```

This pilot tests a deliberate line-range-first variant, not a replacement for `chunked_source_grounding_live_pilot_005`.

---

## Run Scope

The defined run scope is:

* one tiny pilot,
* one approved source scope,
* one prompt/template version,
* one model configuration,
* one model-call batch.

No retries unless the call fails before producing output.

Any source, prompt, model, budget, evaluator, artifact type, output contract, locator policy, chunking policy, or retry-policy change requires a separate admission update before another live call.

---

## Source Scope

Approved source scope:

```text
same selected second-source excerpt as pilots 004 and 005: operator-approved excerpt from the local pharm box-trades transcript
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

The source text must stay local-only or ignored. The committed record may include source scope identifiers, line ranges, locator labels, locator confidence, computed character offsets after validation, computed quote hashes after validation, and metadata-safe summaries, but not raw private source text unless a later explicit policy allows it.

No private/raw source material or provider payloads are committed.

Do not fall back to the full corpus path.

---

## Prompt Template

Prompt/template path:

```text
labs/chunked_source_grounding/PLANNING/live_llm_pilot_006/prompt_template.live_pilot_006.md
```

Prompt template SHA-256: `4a3695f0af9dbf2013fd304bd571f4ec14f4b860ab683fad44cc9782b5a4467b`

The prompt template contains placeholders only. It does not contain raw source text, private notes, provider payloads, or secrets.

System prompt source: the `System Message` section inside the same prompt template file.

Tool instruction hash: none. Tools are disabled.

Prompt traces that include source text must be stored only under ignored local paths.

The output contract is the line-range-first locator contract from Goal 12A.

It keeps:

* source-linked claim table,
* line-range locator candidate table,
* unsupported-claim report,
* brief method-failure notes.

It excludes:

* model-emitted character offsets,
* model-emitted quote hashes,
* broad judgment abstraction notes,
* full comparison commentary,
* product-like study cards,
* strategy or validation content,
* trading advice,
* playbook content.

Do not ask the model to emit `candidate_char_start`.

Do not ask the model to emit `candidate_char_end`.

Do not ask the model to emit quote hashes.

Local review/tooling computes character offsets only after line-range validation.

Quote hashes are computed locally only from validated spans.

---

## Canonical Model Config

```json
{
  "api_format": "openai_compatible_chat_completions",
  "base_url": "https://api.deepseek.com",
  "context_window_provider_limit": "1M",
  "max_input_tokens": 12000,
  "max_output_tokens": 900,
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

Config SHA-256: `3a1ed6ce1e3ecc5dc24cc3838e400676997b62c6a22081a6d0d220b2615f21e7`

Sampling settings: provider defaults, with no temperature, top-p, presence-penalty, or frequency-penalty override.

Context/token settings: cap the runtime input below `12000` tokens and output below `900` tokens even though the provider documents a larger context window.

The max output cap is intentionally smaller than pilot 005; this run tests whether the line-range-first contract fits without expanding into character offsets or broader judgment abstraction.

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
provider_payloads/chunked_source_grounding_live_pilot_006/
model_traces/chunked_source_grounding_live_pilot_006/
prompt_traces/chunked_source_grounding_live_pilot_006/
```

These paths are covered by top-level ignored directories. They may hold raw request/response details only outside git.

Committed post-run records must contain metadata-safe summaries and protocol records only.

---

## Expected Post-Run Files

After the live run, and only after the live run, create protocol-valid records at:

```text
labs/chunked_source_grounding/EXPORTS/run_record.live_pilot_006.json
labs/chunked_source_grounding/EXPORTS/artifact_envelope.live_pilot_006.json
labs/chunked_source_grounding/EXPORTS/evaluation_record.live_pilot_006.json
labs/chunked_source_grounding/EXPORTS/research_note.live_pilot_006.json
```

The expected artifact type is:

```text
chunked_source_line_range_locator_candidate_proposal
```

These records must be proposal-only and non-authoritative. They must not include raw source text, private notes, secrets, raw provider payloads, prompt traces, or model traces.
