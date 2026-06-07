# Stop Condition

Status: proposed planning document

This is a proposed live LLM pilot planning record. It is not a completed run, not research evidence, and not a synthesis export.

No LLM call has been made. No output artifact has been produced. No evaluation result exists. No method success is claimed.

---

## Future Run Stop Condition

The future live pilot must stop after:

* one approved source scope,
* one approved model configuration,
* one approved prompt/template version,
* and one model-call batch.

Any source, prompt, model, evaluator, or budget change requires a separate admission update before another live call.

---

## Failure Stop Conditions

Stop immediately if:

* the source/privacy boundary cannot be preserved,
* prompt or trace storage would commit raw/private material,
* required provider/model/config metadata cannot be recorded,
* the output cannot be represented as expected ArtifactEnvelope types,
* or review finds the output is not useful for judging long-context method viability.

---

## Planning Stop Condition

This Goal 3 planning packet is complete when the proposed MethodCard and ExperimentCard validate, the admission checklist is present, and tests prove the packet is not in `EXPORTS/` and is ignored by synthesis.

## Preflight Stop Condition

The Goal 4 live-run preflight is complete when `run_admission_update.md` records the provider/model, prompt/template hash, config hash, budget, source scope, trace boundary, secret boundary, post-run export paths, and exact one-run stop condition without creating live-run exports.
