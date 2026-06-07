# Live LLM Pilot 001 Run Admission Update

Status: Milestone 2 live-run admission update used for one completed proposal-only pilot

This admission update authorized exactly one tiny live LLM pilot run under the stated scope.

This update itself is not research evidence and not a synthesis export. The authorized run has now produced one proposal-only export set under `labs/long_context_judgment/EXPORTS/`. No method success is claimed.

---

## Authority Boundary

This update narrows the Goal 3 planning packet into one executable preflight scope. It does not create a RunRecord, ArtifactEnvelope, EvaluationRecord, or ResearchNote.

Outputs from this experiment are proposals until evaluated. They do not create source truth, role support, data truth, validation, strategy evidence, financial advice, product authority, live-trading authority, or architecture.

No validation, product authority, strategy evidence, financial advice, live-trading authority, or architecture is created by this admission update or by any future raw model output.

---

## Provider And Model

Provider: DeepSeek API

API format: OpenAI-compatible chat completions

Base URL: `https://api.deepseek.com`

Model: `deepseek-v4-flash`

Reasoning/thinking mode: non-thinking, recorded as `thinking: {"type": "disabled"}`.

Tool routing: tools disabled; no retrieval tools, browser tools, code tools, or file tools are authorized for this first pilot.

Provider docs checked for this admission update:

* `https://api-docs.deepseek.com/`
* `https://api-docs.deepseek.com/quick_start/pricing`
* `https://api-docs.deepseek.com/guides/thinking_mode`

If `deepseek-v4-flash` is unavailable in the account, stop and report. Do not silently substitute `deepseek-v4-pro`, `deepseek-chat`, `deepseek-reasoner`, or any other model.

---

## Lab, Benchmark, And Purpose

Lab: `labs/long_context_judgment`

Benchmark pack: `text_judgment_v0`

Purpose: containment/protocol proof, not breakthrough quality.

Research question:

```text
Can a long-context LLM method extract reusable trading judgment from messy trader text without losing grounding?
```

This pilot tests whether the V3 live-run harness can move from admission, to one provider call, to protocol records without turning output into truth.

---

## Run Scope

The authorized run scope is:

* one tiny pilot,
* one approved source scope,
* one prompt/template version,
* one model configuration,
* one model-call batch.

No retries unless the call fails before producing output.

Any source, prompt, model, budget, evaluator, artifact type, or retry-policy change requires a separate admission update before another live call.

---

## Source Scope

Approved source scope:

```text
source_text_judgment_placeholder from benchmark pack text_judgment_v0, replaced at runtime by one operator-approved messy trader text excerpt kept outside git.
```

The source text must stay local-only or ignored. The committed record may include source scope identifiers, source span hints, and metadata-safe summaries, but not raw private source text unless a later explicit policy allows it.

No private/raw source material or provider payloads are committed.

---

## Prompt Template

Prompt/template path:

```text
labs/long_context_judgment/PLANNING/live_llm_pilot_001/prompt_template.live_pilot_001.md
```

Prompt template SHA-256: `b842070956374c17ddd6d966c069c28ad4ff22dd753b20370c72cb03df79dae6`

The prompt template contains placeholders only. It does not contain raw source text, private notes, provider payloads, or secrets.

System prompt source: the `System Message` section inside the same prompt template file.

Tool instruction hash: none. Tools are disabled.

Prompt traces that include source text must be stored only under ignored local paths.

---

## Canonical Model Config

```json
{
  "api_format": "openai_compatible_chat_completions",
  "base_url": "https://api.deepseek.com",
  "context_window_provider_limit": "1M",
  "max_input_tokens": 12000,
  "max_output_tokens": 1200,
  "model_id": "deepseek-v4-flash",
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

Config SHA-256: `390729eba63d8b3ae2364631bb98b4ab2b218683cd069ba1c84778d26f2cdfac`

Sampling settings: provider defaults, with no temperature, top-p, presence-penalty, or frequency-penalty override.

Context/token settings: cap the runtime input below `12000` tokens and output below `1200` tokens even though the provider documents a larger context window.

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
provider_payloads/live_llm_pilot_001/
model_traces/live_llm_pilot_001/
prompt_traces/live_llm_pilot_001/
```

These paths are covered by top-level ignored directories. They may hold raw request/response details only outside git.

Committed post-run records must contain metadata-safe summaries and protocol records only.

---

## Expected Post-Run Files

After the live run, and only after the live run, create protocol-valid records at:

```text
labs/long_context_judgment/EXPORTS/run_record.live_pilot_001.json
labs/long_context_judgment/EXPORTS/artifact_envelope.live_pilot_001.json
labs/long_context_judgment/EXPORTS/evaluation_record.live_pilot_001.json
labs/long_context_judgment/EXPORTS/research_note.live_pilot_001.json
```

Those files now exist because the authorized run has completed. They remain proposal-only export records.

---

## Exact Stop Condition

Stop after one model-call batch produces output or after any pre-output provider failure that cannot be retried without changing scope.

Stop immediately if:

* `deepseek-v4-flash` is unavailable,
* `DEEPSEEK_API_KEY` is missing,
* source/privacy boundaries cannot be preserved,
* raw source text or provider payloads would be committed,
* prompt/config hashes cannot be reproduced,
* the budget cap would be exceeded,
* the output cannot be represented as expected ArtifactEnvelope types,
* or the run would require any unapproved model, prompt, source, evaluator, tool, or retry substitution.

---

## Preflight Verification Required Before Call

Run these commands before any live call:

```bash
uv run pytest
uv run ruff check .
uv run qf-v3-validate
uv run qf-v3-synthesis
uv run qf-v3-validate labs/long_context_judgment/PLANNING/live_llm_pilot_001/method_card.proposed.json labs/long_context_judgment/PLANNING/live_llm_pilot_001/experiment_card.proposed.json
```

If any command fails, do not call the model.
