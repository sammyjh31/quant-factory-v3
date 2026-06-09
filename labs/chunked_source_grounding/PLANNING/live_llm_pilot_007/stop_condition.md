# Chunked Source Grounding Live Pilot 007 Stop Condition

Status: Goal 15A planning/admission record
Historical status: pre-run admission record; current run status is owned by `labs/chunked_source_grounding/EXPORTS/run_record.live_pilot_007.json`.

Goal 15A stops after admission packet creation and verification.

Goal 15B must stop before any model call if:

* the selected third-source excerpt is missing or its SHA-256 does not match `1d5e041e35b40b84526e1353277667c21f9b5a822fc2d8bc47b22a91b5c1ea31`,
* the source file is not ignored by git, or is staged or tracked,
* `DEEPSEEK_API_KEY` is absent from the environment,
* `deepseek-v4-pro` is unavailable, or the request would use any other model,
* the run would exceed the `$3` budget cap,
* thinking cannot be enabled, streaming cannot be disabled, or tool routing cannot be disabled,
* the output cap cannot be set to `12000` tokens,
* the output contract expands beyond the four approved pilot 006 sections,
* the prompt asks the model to emit character offsets or quote hashes,
* line-range locator candidates cannot be evaluated,
* trace storage would commit raw source text, provider payloads, raw prompts, model output, reasoning content, private notes, account identifiers, or secrets,
* the run attempts to fall back to the full corpus path,
* or any post-run record would claim validation, product authority, strategy evidence, financial advice, live-trading authority, graduation, or architecture.

No retry is allowed unless the provider call fails before producing output.
