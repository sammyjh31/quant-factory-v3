# Chunked Source Grounding Live Pilot 001 Run Admission Update

Status: Goal 7A live-run admission update for one future proposal-only pilot

This admission update authorizes exactly one tiny live LLM pilot run under the stated scope.

Goal 7A does not execute the run. No LLM call has been made for `chunked_source_grounding_live_pilot_001`.

This update itself is not research evidence and not a synthesis export. It does not create a RunRecord, ArtifactEnvelope, EvaluationRecord, ResearchNote, generated synthesis claim, graduation status, or architecture.

---

## Authority Boundary

This update narrows the Goal 7A planning packet into one executable preflight scope for Goal 7B if separately authorized.

Outputs from this experiment are proposals until evaluated. They do not create source truth, role support, data truth, validation, strategy evidence, financial advice, product authority, live-trading authority, or architecture.

No validation, product authority, strategy evidence, financial advice, live-trading authority, or architecture is created by this admission update or by any future raw model output.

Do not add around stale structure. Rework, replace, delete, or archive it.

---

## Provider And Model

Provider: DeepSeek API

API format: OpenAI-compatible chat completions

Base URL: `https://api.deepseek.com`

Model: `deepseek-v4-flash`

Reasoning/thinking mode: non-thinking, recorded as `thinking: {"type": "disabled"}`.

Tool routing: tools disabled; no retrieval tools, browser tools, code tools, or file tools are authorized for this pilot.

If `deepseek-v4-flash` is unavailable in the account, stop and report. Do not silently substitute `deepseek-v4-pro`, `deepseek-chat`, `deepseek-reasoner`, or any other model.

---

## Lab, Benchmark, And Purpose

Lab: `labs/chunked_source_grounding`

Benchmark pack: `text_judgment_v0`

Purpose: method comparison against the first long-context pilot, not breakthrough quality.

Research question:

```text
Can a chunked/source-grounded LLM method preserve exact source grounding better than the long-context method, and what broader trading-judgment abstraction does it lose?
```

This pilot tests whether a chunked/source-grounded reader can produce comparable proposal records on the same source excerpt and benchmark without turning output into truth.

---

## Run Scope

The authorized run scope is:

* one tiny pilot,
* one approved source scope,
* one prompt/template version,
* one model configuration,
* one model-call batch.

No retries unless the call fails before producing output.

Any source, prompt, model, budget, evaluator, artifact type, chunking policy, or retry-policy change requires a separate admission update before another live call.

---

## Source Scope

Approved source scope:

```text
same approved excerpt as `long_context_judgment_live_pilot_001`
```

Canonical source ref:

```text
raw_corpora_sha256:d8392c58c3b740eb
```

Preferred local operator path:

```text
raw_corpora/selected/live_llm_pilot_001/source.txt
```

Recorded first-pilot source path scope:

```text
raw_corpora/trader_source_corpus/transcripts/how-to-use-market-profile-start-now-trading-tutorials.txt
```

The source text must stay local-only or ignored. The committed record may include source scope identifiers, source span hints, and metadata-safe summaries, but not raw private source text unless a later explicit policy allows it.

No private/raw source material or provider payloads are committed.

---

## Prompt Template

Prompt/template path:

```text
labs/chunked_source_grounding/PLANNING/live_llm_pilot_001/prompt_template.live_pilot_001.md
```

Prompt template SHA-256: `b6680a634ad38ad94b394d71425805c6b4d7bfc9217afad877711567f5556a35`

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
provider_payloads/chunked_source_grounding_live_pilot_001/
model_traces/chunked_source_grounding_live_pilot_001/
prompt_traces/chunked_source_grounding_live_pilot_001/
```

These paths are covered by top-level ignored directories. They may hold raw request/response details only outside git.

Committed post-run records must contain metadata-safe summaries and protocol records only.

---

## Expected Post-Run Files

After the live run, and only after the live run, create protocol-valid records at:

```text
labs/chunked_source_grounding/EXPORTS/run_record.live_pilot_001.json
labs/chunked_source_grounding/EXPORTS/artifact_envelope.live_pilot_001.json
labs/chunked_source_grounding/EXPORTS/evaluation_record.live_pilot_001.json
labs/chunked_source_grounding/EXPORTS/research_note.live_pilot_001.json
```

Those files do not exist in Goal 7A because no model call has been made.

---

## Exact Stop Condition

Stop after one model-call batch produces output or after any pre-output provider failure that cannot be retried without changing scope.

Stop immediately if:

* `deepseek-v4-flash` is unavailable,
* `DEEPSEEK_API_KEY` is missing,
* the source excerpt cannot be matched to the same approved source identity as `long_context_judgment_live_pilot_001`,
* source/privacy boundaries cannot be preserved,
* raw source text or provider payloads would be committed,
* prompt/config hashes cannot be reproduced,
* the budget cap would be exceeded,
* the output cannot be represented as `chunked_source_grounding_proposal`,
* or the run would require any unapproved model, prompt, source, evaluator, tool, retry, protocol, or architecture substitution.

---

## Preflight Verification Required Before Call

Run these commands before any live call:

```bash
uv run pytest
uv run ruff check .
uv run qf-v3-validate
uv run qf-v3-synthesis
uv run qf-v3-validate labs/chunked_source_grounding/PLANNING/live_llm_pilot_001/method_card.proposed.json labs/chunked_source_grounding/PLANNING/live_llm_pilot_001/experiment_card.proposed.json
```

If any command fails, do not call the model.
