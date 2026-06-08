# Chunked Source Grounding Live Pilot 003 Stop Condition

Status: Goal 8B planning/admission record

Goal 8B stops after creating the planning/admission packet and validating the proposed MethodCard and ExperimentCard.

No LLM call is made in Goal 8B.

Goal 8C, if separately authorized, must stop after one model-call batch produces output or after any pre-output provider failure that cannot be retried without changing scope.

Stop immediately if:

* `deepseek-v4-pro` is unavailable,
* `DEEPSEEK_API_KEY` is missing,
* the source excerpt cannot be matched to the same approved source identity as `long_context_judgment_live_pilot_001`, `chunked_source_grounding_live_pilot_001`, and `chunked_source_grounding_live_pilot_002`,
* source/privacy boundaries cannot be preserved,
* raw source text or provider payloads would be committed,
* prompt/config hashes cannot be reproduced,
* the `$3` budget cap would be exceeded,
* the output cannot be represented as `chunked_source_span_precision_proposal`,
* the output contract expands beyond source-span precision,
* source-span precision cannot be evaluated,
* the run asks for broad judgment abstraction notes, full comparison commentary, a product-like study card, strategy, validation, trading advice, or playbook content,
* or the run would require any unapproved model, prompt, source, evaluator, tool, retry, protocol, synthesis, or architecture substitution.
