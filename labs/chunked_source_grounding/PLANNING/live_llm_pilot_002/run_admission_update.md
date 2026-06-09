# Chunked Source Grounding Live Pilot 002 Run Admission Update

Status: Goal 7D live-run admission update for completed proposal-only pilot 002
Historical status: pre-run admission record; current run status is owned by `labs/chunked_source_grounding/EXPORTS/run_record.live_pilot_002.json`.

This admission update defined the executable preflight scope for exactly one tiny live LLM pilot run.

It did not by itself authorize execution. Execution required a separate Goal 7E instruction.

Goal 7D itself did not execute the run. The separately authorized run now has proposal-only export records for `chunked_source_grounding_live_pilot_002`.

This update itself is not research evidence and not a synthesis export. It does not create a RunRecord, ArtifactEnvelope, EvaluationRecord, ResearchNote, generated synthesis claim, graduation status, or architecture.

---

## Authority Boundary

This update narrows the Goal 7D planning packet into one executable preflight scope for Goal 7E if separately authorized.

Outputs from this experiment are proposals until evaluated. They do not create source truth, role support, data truth, validation, strategy evidence, financial advice, product authority, live-trading authority, or architecture.

No validation, product authority, strategy evidence, financial advice, live-trading authority, or architecture is created by this admission update or by any future raw model output.

Do not add around stale structure. Rework, replace, delete, or archive it.

The Flash pilot 001 record remains a bounded negative result and is not overwritten by this Pro variant.

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

Purpose: test whether a stronger model plus a smaller output contract can produce a complete parseable source-grounding artifact on the same source and benchmark.

Research question:

```text
Can a chunked/source-grounded LLM method produce a complete parseable source-grounding artifact when using DeepSeek V4 Pro and a smaller output contract, and what does it preserve or lose compared with the long-context judgment pilot?
```

This pilot tests a deliberate new config variant, not a silent substitution or replacement for `chunked_source_grounding_live_pilot_001`.

---

## Run Scope

The defined run scope is:

* one tiny pilot,
* one approved source scope,
* one prompt/template version,
* one model configuration,
* one model-call batch.

No retries unless the call fails before producing output.

Any source, prompt, model, budget, evaluator, artifact type, output contract, chunking policy, or retry-policy change requires a separate admission update before another live call.

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
labs/chunked_source_grounding/PLANNING/live_llm_pilot_002/prompt_template.live_pilot_002.md
```

Prompt template SHA-256: `0c0701f1474f806c60cb3dcac6ed43a54dd19088475033e84af5565fb48342f4`

The prompt template contains placeholders only. It does not contain raw source text, private notes, provider payloads, or secrets.

System prompt source: the `System Message` section inside the same prompt template file.

Tool instruction hash: none. Tools are disabled.

Prompt traces that include source text must be stored only under ignored local paths.

The output contract is narrower than `live_llm_pilot_001`.

Removed from the Flash contract:

* broad judgment abstraction notes,
* full comparison commentary,
* open-ended expansion beyond the listed sections.

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

The max output cap remains intentionally small; this run tests whether the smaller output contract can fit inside the tiny pilot boundary.

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
provider_payloads/chunked_source_grounding_live_pilot_002/
model_traces/chunked_source_grounding_live_pilot_002/
prompt_traces/chunked_source_grounding_live_pilot_002/
```

These paths are covered by top-level ignored directories. They may hold raw request/response details only outside git.

Committed post-run records must contain metadata-safe summaries and protocol records only.

---

## Expected Post-Run Files

After the live run, and only after the live run, create protocol-valid records at:

```text
labs/chunked_source_grounding/EXPORTS/run_record.live_pilot_002.json
labs/chunked_source_grounding/EXPORTS/artifact_envelope.live_pilot_002.json
labs/chunked_source_grounding/EXPORTS/evaluation_record.live_pilot_002.json
labs/chunked_source_grounding/EXPORTS/research_note.live_pilot_002.json
```

Those files do not exist in Goal 7D because no model call has been made.

---

## Exact Stop Condition

Stop after one model-call batch produces output or after any pre-output provider failure that cannot be retried without changing scope.

Stop immediately if:

* `deepseek-v4-pro` is unavailable,
* `DEEPSEEK_API_KEY` is missing,
* the source excerpt cannot be matched to the same approved source identity as `long_context_judgment_live_pilot_001` and `chunked_source_grounding_live_pilot_001`,
* source/privacy boundaries cannot be preserved,
* raw source text or provider payloads would be committed,
* prompt/config hashes cannot be reproduced,
* the budget cap would be exceeded,
* the output cannot be represented as `chunked_source_grounding_proposal`,
* the output contract would expand back to the failed Flash pilot 001 section set,
* or the run would require any unapproved model, prompt, source, evaluator, tool, retry, protocol, or architecture substitution.

---

## Preflight Verification Required Before Call

Run these commands before any live call:

```bash
uv run pytest
uv run ruff check .
uv run qf-v3-validate
uv run qf-v3-synthesis
uv run qf-v3-validate labs/chunked_source_grounding/PLANNING/live_llm_pilot_002/method_card.proposed.json labs/chunked_source_grounding/PLANNING/live_llm_pilot_002/experiment_card.proposed.json
```

If any command fails, do not call the model.
