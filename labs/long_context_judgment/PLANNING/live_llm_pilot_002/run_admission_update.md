# Long Context Judgment Live Pilot 002 Run Admission Update

Status: Goal 13B live-run admission update for pilot 002

This admission update defines the executable preflight scope for exactly one tiny live LLM pilot run.

It does not by itself authorize execution. Execution requires a separate Goal 13C instruction.

Goal 13B itself does not execute the run. No export records exist for `long_context_judgment_live_pilot_002`.

This update itself is not research evidence and not a synthesis export. It does not create a RunRecord, ArtifactEnvelope, EvaluationRecord, ResearchNote, generated synthesis claim, graduation status, or architecture.

---

## Authority Boundary

This update narrows the Goal 13B planning packet into one executable preflight scope for Goal 13C if separately authorized.

Outputs from this experiment are proposals until evaluated. They do not create source truth, role support, data truth, validation, strategy evidence, financial advice, product authority, live-trading authority, or architecture.

No validation, product authority, strategy evidence, financial advice, live-trading authority, or architecture is created by this admission update or by any future raw model output.

Do not add around stale structure. Rework, replace, delete, or archive it.

Pilot 001 remains the completed ungrounded long-context baseline and is not overwritten by this grounded variant. Chunked pilot 006 remains the completed line-range-first locator attempt and is not overwritten either.

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

Lab: `labs/long_context_judgment`

Benchmark pack: `text_judgment_v0`

Purpose: test whether a grounded long-context contract can preserve broader judgment abstraction while requiring a line-range locator candidate for every source-linked claim, adopting the line-range-first lesson from the chunked_source_grounding Goal 13A decision review.

Research question:

```text
Can a grounded long-context contract preserve broader judgment abstraction while requiring line-range source support for every source-linked claim?
```

This pilot tests a deliberate grounded variant of the long-context method family, not a replacement for `long_context_judgment_live_pilot_001` or `chunked_source_grounding_live_pilot_006`.

---

## Run Scope

The defined run scope is:

* one tiny pilot,
* one approved source scope,
* one prompt/template version,
* one model configuration,
* one model-call batch.

No retries unless the call fails before producing output.

Any source, prompt, model, budget, evaluator, artifact type, output contract, locator policy, or retry-policy change requires a separate admission update before another live call.

---

## Source Scope

Approved source scope:

```text
same selected second-source excerpt as chunked_source_grounding pilots 004, 005, and 006: operator-approved excerpt from the local pharm box-trades transcript
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
labs/long_context_judgment/PLANNING/live_llm_pilot_002/prompt_template.live_pilot_002.md
```

Prompt template SHA-256: `74f8e89a2e25942a2be20170fd6bb0c1e414d4216a18003915ea0214abc29024`

The prompt template contains placeholders only. It does not contain raw source text, private notes, provider payloads, or secrets.

System prompt source: the `System Message` section inside the same prompt template file.

Tool instruction hash: none. Tools are disabled.

Prompt traces that include source text must be stored only under ignored local paths.

The output contract is the grounded long-context contract from the Goal 13B admission packet.

It keeps:

* judgment principle proposal table,
* source-linked claim table,
* line-range locator candidate table,
* unsupported-claim report,
* brief method-failure notes.

It excludes:

* model-emitted character offsets,
* model-emitted quote hashes,
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
  "max_output_tokens": 1600,
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

Config SHA-256: `416028f9496cefee6284e6fed96440f8fef182afe878743ba3081f8733f951cb`

Sampling settings: provider defaults, with no temperature, top-p, presence-penalty, or frequency-penalty override.

Context/token settings: cap the runtime input below `12000` tokens and output below `1600` tokens even though the provider documents a larger context window.

The max output cap is larger than pilot 006's `900` because the grounded contract adds the judgment principle proposal table; the entry caps in the prompt template bound the expansion. If the contract cannot fit in `1600` output tokens, that is itself a recordable negative result echoing the chunked pilot 001 contract-size failure.

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
provider_payloads/long_context_judgment_live_pilot_002/
model_traces/long_context_judgment_live_pilot_002/
prompt_traces/long_context_judgment_live_pilot_002/
```

These paths are covered by top-level ignored directories. They may hold raw request/response details only outside git.

Committed post-run records must contain metadata-safe summaries and protocol records only.

---

## Expected Post-Run Files

After the live run, and only after the live run, create protocol-valid records at:

```text
labs/long_context_judgment/EXPORTS/run_record.live_pilot_002.json
labs/long_context_judgment/EXPORTS/artifact_envelope.live_pilot_002.json
labs/long_context_judgment/EXPORTS/evaluation_record.live_pilot_002.json
labs/long_context_judgment/EXPORTS/research_note.live_pilot_002.json
```

The expected artifact type is:

```text
grounded_long_context_judgment_proposal
```

These records must be proposal-only and non-authoritative. They must not include raw source text, private notes, secrets, raw provider payloads, prompt traces, or model traces.
