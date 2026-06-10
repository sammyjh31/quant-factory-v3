# LLM Judge Calibration Live Pilot 001 Source Privacy Boundary

Status: Goal 16A planning/admission record

This study approves no new source material. Its inputs are the three previously operator-approved source excerpts and the eleven existing pilots' local output traces:

* `raw_corpora/selected/live_llm_pilot_001/source.txt` (first source, used by long_context 001 and chunked 001-003),
* `raw_corpora/selected/source_span_precision_repeat_001/source.txt` (second source, `raw_corpora_sha256:9f9e143429f5842a`),
* `raw_corpora/selected/third_source_line_range_001/source.txt` (third source, `raw_corpora_sha256:1d5e041e35b40b84`),
* local ignored traces under `model_traces/*` for the eleven pilots.

The harness reads each pilot's committed ArtifactEnvelope only to resolve its source path and source ref; envelope metadata is never placed in judge prompts (blinding rule).

Judge prompts contain source text and artifact text and therefore must exist only under ignored local paths (`prompt_traces/llm_judge_calibration_live_pilot_001/`). Judge raw outputs and provider payloads stay under ignored local paths.

Committed records may include only metadata-safe agreement statistics, counts, delegation labels, trial identifiers, hashes, and proposal-only summaries. No raw source text, no artifact claim text, no judge verdict prose containing source quotes, no provider payloads, no secrets.

No source material becomes product authority, strategy evidence, financial advice, live-trading authority, graduation, or architecture.
