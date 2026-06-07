# Stop Condition

Status: proposed planning document

This is a proposed live LLM pilot planning record. It is not a completed run, not research evidence, and not a synthesis export.

The authorized Goal 5 live run has completed one model-call batch and produced proposal-only export records. No method success is claimed.

---

## Run Stop Condition

The authorized live pilot stopped after:

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

The Goal 4 live-run preflight completed when `run_admission_update.md` recorded the provider/model, prompt/template hash, config hash, budget, source scope, trace boundary, secret boundary, post-run export paths, and exact one-run stop condition without creating live-run exports.

## Goal 5 Stop Condition

Goal 5 is complete when exactly one live model-call batch has produced proposal-only export records, stale pre-run currentness text has been replaced, synthesis imports the records from `EXPORTS/`, and no graduation or architecture claim has been created.
