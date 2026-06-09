# Long Context Judgment Live Pilot 003 Run Admission Update

Status: Goal 14A live-run admission update for pilot 003
Historical status: pre-run admission record; current run status is owned by `labs/long_context_judgment/EXPORTS/run_record.live_pilot_003.json`.

This admission update defines the executable preflight scope for exactly one tiny live LLM pilot run. Execution requires the separately given Goal 14B instruction; the operator's milestone-4 goal directive supplies it for this evidence chain.

This update is not research evidence and not a synthesis export. It creates no protocol records.

Outputs from this experiment are proposals until evaluated. They do not create source truth, role support, data truth, validation, strategy evidence, financial advice, product authority, live-trading authority, or architecture.

Pilot 002 remains the completed cap-constrained grounded attempt and is not overwritten by this cap-relieved repeat.

---

## Provider And Model

Provider: DeepSeek API. API format: OpenAI-compatible chat completions. Base URL: `https://api.deepseek.com`. Model: `deepseek-v4-pro`.

Reasoning/thinking mode: **enabled**, recorded as `thinking: {"type": "enabled"}`, by explicit operator direction. This is the first thinking-enabled run in the portfolio; record reasoning-token usage in the export metadata.

Tool routing: tools disabled. If `deepseek-v4-pro` is unavailable, stop and report; do not substitute any other model.

## Run Scope

One tiny pilot, one approved source scope, one prompt/template version, one model configuration, one model-call batch. No retries unless the call fails before producing output. Any change requires a new admission update.

## Source Scope

Same as pilot 002: `raw_corpora_sha256:9f9e143429f5842a`, excerpt SHA-256 `9f9e143429f5842a9c03c95b1f7705d85fb664cf795c30919a582fa66b16fbb5`, 945 words, local path `raw_corpora/selected/source_span_precision_repeat_001/source.txt`. Local-only/ignored; no fallback to the full corpus path.

## Prompt Template

Path: `labs/long_context_judgment/PLANNING/live_llm_pilot_003/prompt_template.live_pilot_003.md`
Prompt template SHA-256: `1ad7a5625086b952cc4f10de0c2dae10281293d6e162a8a9f13c9c0d80db393a`
Message body verified byte-identical to the pilot 002 contract; placeholders only; no raw source text or secrets. System prompt source: the `System Message` section of the same file. The contract keeps the five pilot 002 sections and all pilot 002 exclusions, including no model-emitted character offsets or quote hashes.

## Canonical Model Config

```json
{
  "api_format": "openai_compatible_chat_completions",
  "base_url": "https://api.deepseek.com",
  "context_window_provider_limit": "1M",
  "max_input_tokens": 12000,
  "max_output_tokens": 4000,
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

Config SHA-256: `9b1194ff8121ba8dbdb2afcab0c58b7b54aa5e566ef352fad160a8903745d1b9`

Sampling: provider defaults. The 4000-token cap covers the full completion including any reasoning tokens the provider counts against it; if the contract still truncates, that is a recordable negative result.

## Budget And Secrets

Budget cap `$3` hard maximum. Required secret env var name: `DEEPSEEK_API_KEY` (value never committed). No payloads, traces, request ids, or account identifiers committed.

## Trace And Log Storage

Ignored local paths only:

```text
provider_payloads/long_context_judgment_live_pilot_003/
model_traces/long_context_judgment_live_pilot_003/
prompt_traces/long_context_judgment_live_pilot_003/
```

## Expected Post-Run Files

```text
labs/long_context_judgment/EXPORTS/run_record.live_pilot_003.json
labs/long_context_judgment/EXPORTS/artifact_envelope.live_pilot_003.json
labs/long_context_judgment/EXPORTS/evaluation_record.live_pilot_003.json
labs/long_context_judgment/EXPORTS/evaluation_record.live_pilot_003_manual_content_review.json
labs/long_context_judgment/EXPORTS/evaluation_record.live_pilot_003_strict_line_range_review.json
labs/long_context_judgment/EXPORTS/research_note.live_pilot_003.json
```

Expected artifact type: `grounded_long_context_judgment_proposal`. All records proposal-only and non-authoritative; no raw source text, traces, payloads, or secrets committed.
