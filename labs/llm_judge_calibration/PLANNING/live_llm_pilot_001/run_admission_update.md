# LLM Judge Calibration Live Pilot 001 Run Admission Update

Status: Goal 16A live-run admission update for pilot 001
Historical status: pre-run admission record; current run status is owned by `labs/llm_judge_calibration/EXPORTS/run_record.live_pilot_001.json`.

Defines the executable preflight scope for one admitted judge-trial batch. Execution requires the separately given Goal 16B instruction; the operator's milestone-5 directive supplies it.

Outputs from this experiment are proposals until evaluated. They do not create source truth, role support, data truth, validation, strategy evidence, financial advice, product authority, live-trading authority, or architecture.

Existing human EvaluationRecords remain review authority and are not modified by this study.

## Provider, Model, Scope

Provider: DeepSeek API; OpenAI-compatible chat completions; base URL `https://api.deepseek.com`; model `deepseek-v4-pro`; thinking enabled (`thinking: {"type": "enabled"}`); stream and tools disabled; no model substitution. One admitted batch of exactly the 17 pre-registered trials (15 trials plus 2 self-consistency duplicates); a call that fails before producing output may be retried once; a call that produces output is final; more than 3 terminal failures stops the batch.

Source scope: the three previously approved excerpts and eleven pilots' local traces listed in `source_privacy_boundary.md`. No new source material.

Prompt template: `labs/llm_judge_calibration/PLANNING/live_llm_pilot_001/prompt_template.live_pilot_001.md`
Prompt template SHA-256: `df384c9162574d5a286790a78a2e9d56be58019af609c52f8e76f0a29ade383e`
Placeholders only; assembled prompts (which contain source and artifact text) exist only under ignored trace paths. The harness asserts the blinding rule before each call.

## Canonical Model Config

```json
{
  "api_format": "openai_compatible_chat_completions",
  "base_url": "https://api.deepseek.com",
  "context_window_provider_limit": "1M",
  "max_input_tokens": 12000,
  "max_output_tokens": 8000,
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

Config SHA-256: `8adecc066d879a1f7e45971178f84d33c35d5f52e58a0b3f1c060745a420b8ca`

The 8000-token cap is sized for reasoning plus the small JSON verdict, per the pilot 003 thinking-cap lesson. Record reasoning and content tokens per trial.

## Budget, Secrets, Traces, Expected Files

Budget cap `$3` hard maximum for the whole batch; secret name `DEEPSEEK_API_KEY` (value never committed). Ignored trace paths: `provider_payloads/llm_judge_calibration_live_pilot_001/`, `model_traces/llm_judge_calibration_live_pilot_001/`, `prompt_traces/llm_judge_calibration_live_pilot_001/`.

Expected post-run files under `labs/llm_judge_calibration/EXPORTS/`: `run_record.live_pilot_001.json`, `artifact_envelope.live_pilot_001.json`, `evaluation_record.live_pilot_001.json`, `research_note.live_pilot_001.json`. Expected artifact type: `judge_agreement_delegation_map_proposal`. All records proposal-only; no raw source, artifact text, judge prose, payloads, or secrets committed.
