# Chunked Source Grounding Live Pilot 004 Stop Condition

Status: Goal 9A planning/admission record
Historical status: pre-run admission record; current run status is owned by `labs/chunked_source_grounding/EXPORTS/run_record.live_pilot_004.json`.

Goal 9A stops after creating the planning/admission packet and validating the proposed MethodCard and ExperimentCard.

No LLM call is made in Goal 9A.

Goal 9B, if separately authorized, must stop after one model-call batch produces output or after any pre-output provider failure that cannot be retried without changing scope.

Stop immediately if:

* the selected second-source excerpt is missing,
* source file is not ignored by git,
* source file is staged or tracked,
* the source hash does not match `raw_corpora_sha256:9f9e143429f5842a`,
* the run attempts to fall back to the full corpus path,
* `deepseek-v4-pro` is unavailable,
* `DEEPSEEK_API_KEY` is missing,
* source/privacy boundaries cannot be preserved,
* raw source text or provider payloads would be committed,
* prompt/config hashes cannot be reproduced,
* the `$3` budget cap would be exceeded,
* the output cannot be represented as `chunked_source_span_precision_proposal`,
* the output contract expands beyond source-span precision,
* source-span precision cannot be evaluated,
* the run asks for broad judgment abstraction notes, full comparison commentary, a product-like study card, strategy, validation, trading advice, or playbook content,
* or the run would require any unapproved model, prompt, source, evaluator, tool, retry, protocol, synthesis, or architecture substitution.
