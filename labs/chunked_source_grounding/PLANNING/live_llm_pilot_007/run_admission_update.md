# Chunked Source Grounding Live Pilot 007 Run Admission Update

Status: Goal 15A live-run admission update for pilot 007
Historical status: pre-run admission record; current run status is owned by `labs/chunked_source_grounding/EXPORTS/run_record.live_pilot_007.json`.

Defines the executable preflight scope for exactly one tiny live LLM pilot run. Execution requires the separately given Goal 15B instruction; the operator's milestone-4 goal directive supplies it for this evidence chain.

Outputs from this experiment are proposals until evaluated. They do not create source truth, role support, data truth, validation, strategy evidence, financial advice, product authority, live-trading authority, or architecture.

Pilot 006 remains the completed second-source line-range-first run and is not overwritten.

## Provider, Model, Scope

Provider: DeepSeek API; OpenAI-compatible chat completions; base URL `https://api.deepseek.com`; model `deepseek-v4-pro`; thinking enabled (`thinking: {"type": "enabled"}`); stream and tools disabled; no model substitution. One pilot, one source scope, one template version, one config, one call batch; no retries unless the call fails before producing output; any change requires a new admission update.

Source scope: the operator-authorized third source excerpt — `raw_corpora_sha256:1d5e041e35b40b84`, excerpt SHA-256 `1d5e041e35b40b84526e1353277667c21f9b5a822fc2d8bc47b22a91b5c1ea31`, 950 words, 106 wrapped lines, local path `raw_corpora/selected/third_source_line_range_001/source.txt` (origin: `raw_corpora/trader_source_corpus/transcripts/trading-strategy-part-2-tuesday-9th-december-2025-9-30pm-utc.txt`, words 1900-2850, wrapped locally at 50 characters). Local-only/ignored; no fallback to the full corpus path.

Prompt template: `labs/chunked_source_grounding/PLANNING/live_llm_pilot_007/prompt_template.live_pilot_007.md`
Prompt template SHA-256: `ad8f12fb0fa35015b99e88ed5667738e31f93308425f18f65c154c098b41c655`
Body identical to the pilot 006 contract except ids, source ref, and source ordinal; placeholders only; the four pilot 006 sections and exclusions unchanged (no model-emitted character offsets or quote hashes; local computation only after line-range validation).

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

Config SHA-256: `3e90c8b504372ad6e23be3258ad1c06a243cf60bec54de521c1cd332ffca4243`

Identical configuration to long-context pilot 004 (the portfolio's validated thinking-enabled configuration), giving a controlled cross-lab config repeat. Sampling: provider defaults. The 12000-token cap covers reasoning plus content; record both token counts post-run.

## Budget, Secrets, Traces, Expected Files

Budget cap `$3` hard maximum; secret name `DEEPSEEK_API_KEY` (value never committed). Ignored trace paths: `provider_payloads/chunked_source_grounding_live_pilot_007/`, `model_traces/chunked_source_grounding_live_pilot_007/`, `prompt_traces/chunked_source_grounding_live_pilot_007/`.

Expected post-run files under `labs/chunked_source_grounding/EXPORTS/`: `run_record.live_pilot_007.json`, `artifact_envelope.live_pilot_007.json`, `evaluation_record.live_pilot_007.json`, `evaluation_record.live_pilot_007_strict_line_range_review.json`, `research_note.live_pilot_007.json`. Expected artifact type: `chunked_source_line_range_locator_candidate_proposal`. All records proposal-only; no raw source, traces, payloads, or secrets committed.
