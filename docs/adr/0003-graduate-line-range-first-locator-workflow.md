# ADR 0003: Graduate The Line-Range-First Source Locator Workflow

Status: accepted
Decision date: 2026-06-09
Decision authority: operator (milestone-4 goal directive), recorded by the executing agent

## Context

QuantFactory V3's milestone 4 set one goal: take a single method through the full evidence ladder — fixture, proposed run, evaluated run, repeated evidence, graduation candidate, ADR — to the portfolio's first explicit graduation decision.

The candidate is the **line-range-first source locator workflow**, the method lesson that emerged from the chunked_source_grounding locator thread (pilots 001-006, Goal 13A decision review) and was then deliberately stressed across method families, sources, and configurations under the milestone-4 evidence thread.

Evidence inventory (all proposal-only export records with boundary, content, and strict line-range reviews):

* `chunked_source_grounding_live_pilot_006` — narrow line-range-first contract, second source, thinking off: 3/3 support-valid candidates under strict review.
* `chunked_source_grounding_live_pilot_007` — same contract, operator-authorized third source (ASR-degraded, deterministically wrapped), thinking on: 3/3 support-valid, all exact labels warranted, zero demotions, entry caps respected.
* `long_context_judgment_live_pilot_004` — broad grounded long-context contract adopting the locator discipline, second source, thinking on with reasoning-aware cap: 8/9 support-valid at finer claim granularity, with one accepted span byte-identical to pilot 006's independent acceptance.
* Strict reviews of `chunked_source_grounding_live_pilot_003`/`004` — reviewer-side line/offset/hash locator computation demonstrated on the first and second sources.
* Negative-result analysis: `chunked_source_grounding_live_pilot_005` (model-emitted character offsets and quote hashes are not evidence-valid), `long_context_judgment_live_pilot_002` (locator pointing collapses under output-cap pressure even when claims stay faithful), `long_context_judgment_live_pilot_003` (thinking-mode reasoning consumes content-sized caps entirely).

Cross-lab comparison exists (two labs, two contract families on the same source and rubric). Benchmark coverage is `text_judgment_v0`. Known failure modes are recorded in the evidence-thread section of the owning comparison note.

## Decision

Graduate the line-range-first source locator workflow as an approved V3 method pattern and a V4 inheritance candidate. The graduated pattern is exactly this division of labor:

1. Models propose **line-range locator candidates only**. Prompts must not ask models to emit character offsets, quote hashes, or any cryptographic locator handle.
2. **Local tooling validates** proposed line ranges against the source before acceptance; model-emitted ranges and labels are candidates, never accepted on trust.
3. **Character offsets and quote hashes are computed locally, only from validated spans.** Computed handles are local metadata, not model output.
4. **Line structure is a recorded local responsibility**: sources without native line structure are deterministically segmented (procedure, parameters, and post-wrap hash recorded) before any line coordinate is used.
5. **Emitted locator confidence is not an acceptance signal**; strict-review labels (`exact | approximate | broad | missing`) assigned during local validation are the usable signal.

Future V3 lab work that needs source locators should use this pattern by default; departures require their own recorded justification.

## What Does Not Graduate

No prompt template, model, provider, configuration, thinking mode, lab, artifact type, schema change, benchmark, abstraction method, claim-extraction quality bar, evaluation calibration, autonomous loop, product surface, or strategy claim graduates with this ADR. The pattern is a locator workflow, not a reading method.

## Known Limitations And Boundary Conditions

* **Single model family.** All live evidence is DeepSeek V4 (Flash/Pro). Model-family generality is untested; the operator chose thinking-mode variation over cross-vendor repeats for milestone 4. A cross-family repeat remains the highest-value future robustness check, and this graduation must be revisited if a different family fails the pattern.
* **Single reviewer lineage.** Strict reviews were executed by operator-directed agent review without cross-reviewer calibration; the LLM-judge calibration study (docs/research-plans/llm-judge-calibration-study.md) remains future work.
* **Small-n.** The repeated evidence is three positive runs plus reviewer-side computations across three sources; this clears the portfolio's first graduation bar, not a statistical one.
* Broad contracts under thinking mode ignored entry caps; thinking caps must be sized for reasoning plus contract; off-by-one boundary misses occur. These are operating conditions of the pattern, recorded in the evidence thread.

## Consequences

* `GRADUATION_LEDGER.md` records GRAD-0001 and stops claiming that nothing has graduated; its evidence discipline for non-graduated items is unchanged.
* The boundary-contract test asserting a permanently empty ledger is updated to assert the new ledger state, under this ADR.
* Protocol v0.1 is unchanged: no new protocol object or field is added by this graduation. A future LocatorRecord or line-range protocol field would require its own ADR and repeated cross-lab need.
* Proposal-only posture for pilot records is unchanged; graduation elevates the method pattern, not any individual record's evidence status.

## Non-Effects

No validation claim. No product authority. No strategy evidence. No financial advice. No live-trading authority. No new protocol object. No lab architecture change. No autonomous-loop activation.
