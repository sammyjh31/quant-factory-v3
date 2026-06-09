# Chunked Source Grounding Live Pilot 006 Stop Condition

Status: Goal 12B planning/admission record

Goal 12B stops after admission packet creation and verification.

Goal 12C, if separately authorized, must stop before any model call if:

* the selected second-source excerpt is missing,
* the source file is not ignored by git,
* the source file is staged or tracked,
* `DEEPSEEK_API_KEY` is absent from the environment,
* `deepseek-v4-pro` is unavailable,
* the run would exceed the `$3` budget cap,
* the request would use a model other than `deepseek-v4-pro`,
* thinking cannot be disabled,
* streaming cannot be disabled,
* tool routing cannot be disabled,
* the output contract expands beyond line-range locator candidates,
* the prompt asks the model to emit character offsets,
* the prompt asks the model to emit quote hashes,
* line-range locator candidates cannot be evaluated,
* trace storage would commit raw source text, provider payloads, raw prompts, model output, private notes, account identifiers, or secrets,
* the run attempts to fall back to the full corpus path,
* or any post-run record would claim validation, product authority, strategy evidence, financial advice, live-trading authority, graduation, or architecture.

No retry is allowed unless the provider call fails before producing output.
