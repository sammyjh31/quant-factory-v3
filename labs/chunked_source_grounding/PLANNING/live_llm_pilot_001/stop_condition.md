# Chunked Source Grounding Live Pilot 001 Stop Condition

Status: Goal 7A planning/admission record
Historical status: pre-run admission record; current run status is owned by `labs/chunked_source_grounding/EXPORTS/run_record.live_pilot_001.json`.

Goal 7A stops after creating the planning/admission packet and validating the proposed MethodCard and ExperimentCard.

No LLM call is made in Goal 7A.

Goal 7B, if separately authorized, must stop after one model-call batch produces output or after any pre-output provider failure that cannot be retried without changing scope.

Stop immediately if:

* `deepseek-v4-flash` is unavailable,
* `DEEPSEEK_API_KEY` is missing,
* the source excerpt cannot be matched to the same approved source identity as `long_context_judgment_live_pilot_001`,
* source/privacy boundaries cannot be preserved,
* raw source text or provider payloads would be committed,
* prompt/config hashes cannot be reproduced,
* the `$3` budget cap would be exceeded,
* the output cannot be represented as `chunked_source_grounding_proposal`,
* or the run would require any unapproved model, prompt, source, evaluator, tool, retry, protocol, or architecture substitution.
