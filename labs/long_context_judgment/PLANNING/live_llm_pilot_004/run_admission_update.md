# Long Context Judgment Live Pilot 004 Run Admission Update

Status: Goal 14C live-run admission update for pilot 004

Defines the executable preflight scope for exactly one tiny live LLM pilot run. Execution requires the separately given Goal 14D instruction; the operator's milestone-4 goal directive supplies it for this evidence chain.

Outputs from this experiment are proposals until evaluated. They do not create source truth, role support, data truth, validation, strategy evidence, financial advice, product authority, live-trading authority, or architecture.

Pilots 002 and 003 remain completed bounded results and are not overwritten.

## Provider, Model, Scope

Provider: DeepSeek API; OpenAI-compatible chat completions; base URL `https://api.deepseek.com`; model `deepseek-v4-pro`; thinking enabled (`thinking: {"type": "enabled"}`); stream and tools disabled; no model substitution. One pilot, one source scope, one template version, one config, one call batch; no retries unless the call fails before producing output; any change requires a new admission update.

Source scope: identical to pilots 002/003 — `raw_corpora_sha256:9f9e143429f5842a`, excerpt SHA-256 `9f9e143429f5842a9c03c95b1f7705d85fb664cf795c30919a582fa66b16fbb5`, 945 words, local path `raw_corpora/selected/source_span_precision_repeat_001/source.txt`, local-only/ignored, no corpus fallback.

Prompt template: `labs/long_context_judgment/PLANNING/live_llm_pilot_004/prompt_template.live_pilot_004.md`, SHA-256 `162b8ab50f960183776d48ff4d2032fb7d022a1e537137d247f8d0bd8c409c5e`, body byte-identical to pilots 002/003; placeholders only; same exclusions (no model-emitted offsets/hashes).

## Canonical Model Config

```json
{
  "api_format": "openai_compatible_chat_completions",
  "base_url": "https://api.deepseek.com",
  "context_window_provider_limit": "1M",
  "max_input_tokens": 12000,
  "max_output_tokens": 12000,
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
    "type": "enabled"
  },
  "tool_routing": "none"
}
```

Config SHA-256 (compact-sorted serialization): `3e90c8b504372ad6e23be3258ad1c06a243cf60bec54de521c1cd332ffca4243`

The 12000-token cap is sized from the pilot 003 reasoning trace (~4000 reasoning tokens, unfinished) plus the ~1600-token contract observed in pilot 002, with margin. Record reasoning and content tokens separately post-run.

## Budget, Secrets, Traces, Expected Files

Budget cap `$3` hard maximum; secret name `DEEPSEEK_API_KEY` (value never committed). Ignored trace paths: `provider_payloads/long_context_judgment_live_pilot_004/`, `model_traces/long_context_judgment_live_pilot_004/`, `prompt_traces/long_context_judgment_live_pilot_004/`.

Expected post-run files under `labs/long_context_judgment/EXPORTS/`: `run_record.live_pilot_004.json`, `artifact_envelope.live_pilot_004.json`, `evaluation_record.live_pilot_004.json`, `evaluation_record.live_pilot_004_manual_content_review.json`, `evaluation_record.live_pilot_004_strict_line_range_review.json`, `research_note.live_pilot_004.json`. Expected artifact type: `grounded_long_context_judgment_proposal`. All records proposal-only; no raw source, traces, payloads, or secrets committed.
