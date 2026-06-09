# Graduation Ledger

Status: portfolio graduation authority  
Current phase: `milestone-4-first-graduation-candidate`

One method pattern has graduated (GRAD-0001, by explicit operator decision and ADR 0003). No other methods, labs, schemas, artifacts, product surfaces, research claims, evaluators, or architectures have graduated.

Planning packets, run admission updates, proposal-only live export sets, manual reviews, comparison notes, strict reviews, locator-thread decision reviews, and research plans do not affect graduation status by themselves.

---

## Current Graduation State

```text
One graduated item: GRAD-0001.
```

### GRAD-0001: line-range-first source locator workflow

* Decided: 2026-06-09, operator decision under the milestone-4 goal directive.
* Owning ADR: `docs/adr/0003-graduate-line-range-first-locator-workflow.md`
* Evidence thread: `labs/chunked_source_grounding/PLANNING/comparisons/live_pilot_method_comparison_001.md` (Milestone-4 Evidence Thread section).
* What graduated: the locator division of labor — models propose line-range locator candidates only; local tooling validates ranges before acceptance; character offsets and quote hashes are computed locally only from validated spans; line structure is a recorded local responsibility; emitted locator confidence is not an acceptance signal.
* What did not graduate: any prompt, model, provider, configuration, lab, artifact type, schema change, benchmark, abstraction method, evaluation calibration, autonomous loop, product surface, or strategy claim.
* Recorded limitations: single model family (DeepSeek V4) evidence; single reviewer lineage pending judge calibration; small-n repeated evidence (three positive runs plus reviewer-side computations across three sources, with three recorded negative results).

---

## Meaning Of Graduation

Graduation means that a method, schema, artifact type, evaluator, lab pattern, or product surface has enough repeated evidence to become part of a hardened future architecture.

Graduation is a portfolio-level decision, not a lab-level decision.

---

## Current Non-Graduation Rule

No item other than GRAD-0001 has graduated in the current portfolio phase.

Fixture records are not evidence.

A proposal-only live pilot export set is not graduation evidence by itself.

Generated synthesis summaries are not evidence.

Currentness docs are not evidence.

---

## Future Graduation Requirements

Future graduation will require at minimum:

* repeated evidence across runs,
* relevant benchmark coverage,
* evaluation records,
* negative-result analysis,
* known failure modes,
* cross-lab comparison when applicable,
* explicit ADR,
* and a clear statement of what is and is not graduating.

GRAD-0001 is the precedent for this shape: evidence thread in the owning comparison note, decision and boundaries in the ADR, status here.
