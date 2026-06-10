# LLM Judge Calibration Live Pilot 001 Stop Condition

Status: Goal 16A planning/admission record
Historical status: pre-run admission record; current run status is owned by `labs/llm_judge_calibration/EXPORTS/run_record.live_pilot_001.json`.

Goal 16A stops after admission packet creation and verification.

Goal 16B must stop before any judge call if:

* any of the three approved source excerpts or any required local trace is missing,
* a blinding assertion fails (the assembled prompt contains ground-truth verdict material),
* `DEEPSEEK_API_KEY` is absent,
* `deepseek-v4-pro` is unavailable, or the request would use any other model,
* the batch would exceed the `$3` cap,
* thinking cannot be enabled, streaming cannot be disabled, or tool routing cannot be disabled,
* the trial set deviates from the pre-registered 17 trials,
* the delegation thresholds have not been committed before the first call,
* trace storage would commit raw source text, artifact text, judge outputs, provider payloads, or secrets,
* or any post-run record would claim review authority, validation, product authority, strategy evidence, financial advice, live-trading authority, graduation, or architecture.

Mid-batch: a provider call that fails before producing output may be retried once; a call that produces output is final. If more than 3 of 17 calls fail terminally, stop the batch and record a bounded negative.

After the batch: stop. Analysis and export-record creation use local data only; no further model calls under this admission.
