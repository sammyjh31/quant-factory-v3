# LLM Judge Calibration Study

Status: future method plan
Origin: operator direction to make evaluation automatable before any lab loop is automated
Current state: not active lab, not protocol, not architecture, not current milestone, not export evidence, not graduation
Candidate future lab: `labs/llm_judge_calibration/`

This document preserves a future V3 methodology plan. It is not current portfolio authority and does not change the active portfolio work.

Related plan: [autonomous-lab-loop](autonomous-lab-loop.md). That plan's activation is explicitly gated on this study's results.

---

## 1. One-Sentence Thesis

Can an LLM judge reproduce the operator's manual content-review and strict locator-review verdicts on the existing live-pilot artifacts well enough to be trusted as a calibrated first-pass evaluator in future experiments?

---

## 2. Why This Plan Exists

Every live pilot so far has been evaluated by operator manual review. That is correct for a young portfolio, but it makes evaluation the bottleneck for everything the portfolio wants to become: more pilots, method comparisons, repeated-evidence accumulation, and any future autonomous lab loop.

The admission checklist already anticipates this:

```text
If an LLM judge is used, the model/config must be recorded and the judge result must not be treated as final authority without calibration.
```

This study is that calibration. It is also independently valuable even if no lab loop is ever automated, because it measures how reliable manual review itself is — the Goal 13A decision review lists uncalibrated manual line-range review as an unresolved item.

The study is unusually cheap because the ground truth already exists.

---

## 3. Ground Truth Inventory

The completed human evaluation records as of this plan:

Manual content reviews (`manual_content_review`):

```text
labs/long_context_judgment/EXPORTS/evaluation_record.live_pilot_001_manual_content_review.json
labs/chunked_source_grounding/EXPORTS/evaluation_record.live_pilot_001_manual_content_review.json
labs/chunked_source_grounding/EXPORTS/evaluation_record.live_pilot_002_manual_content_review.json
labs/chunked_source_grounding/EXPORTS/evaluation_record.live_pilot_003_manual_content_review.json
labs/chunked_source_grounding/EXPORTS/evaluation_record.live_pilot_004_manual_content_review.json
```

Strict span/locator/line-range reviews:

```text
labs/chunked_source_grounding/EXPORTS/evaluation_record.live_pilot_003_strict_span_review.json
labs/chunked_source_grounding/EXPORTS/evaluation_record.live_pilot_004_strict_span_review.json
labs/chunked_source_grounding/EXPORTS/evaluation_record.live_pilot_005_strict_locator_review.json
labs/chunked_source_grounding/EXPORTS/evaluation_record.live_pilot_006_strict_line_range_review.json
```

That is nine human evaluation records across seven pilots and two labs. Future pilots (such as `long_context_judgment_live_pilot_002`) add to this inventory as their reviews complete.

This inventory is small. The study must report agreement honestly at this sample size and must not claim statistical authority from nine records.

---

## 4. Study Design

### 4.1 Blinded judge re-review

For each reviewed artifact, an LLM judge receives:

* the committed ArtifactEnvelope content,
* the approved source excerpt (under the same privacy boundary as the original pilot),
* the same review rubric and failure-tag vocabulary the human review used,
* and nothing else.

The judge must not see the human EvaluationRecord, the comparison note, the research notes, or any text that reveals the human verdict. Leakage of the human verdict into the judge prompt invalidates the trial.

The judge produces the same record shape the human produced: per-axis scores, pass/fail status, failure tags, and review comments.

### 4.2 Mechanical pre-checks are separate

Line-range validity, character-offset computation, and quote-hash computation are mechanical operations, not judgment. They should be computed by local tooling before the judge runs, and the judge should receive their results as inputs.

The study measures judgment agreement, not the judge's ability to count lines. Conflating the two would understate or overstate the judge in ways that do not transfer.

### 4.3 Agreement measurement

For each artifact, compare judge output to the human record on:

* verdict agreement (pass/fail or accept/reject per reviewed item),
* per-axis score agreement (within a stated tolerance),
* failure-tag overlap (which tags the judge found, missed, or invented),
* locator-label agreement for strict reviews (`exact | approximate | broad | missing`),
* and `overclaimed_exactness` detection specifically, since that is the failure the strict reviews exist to catch.

Report results as a per-axis agreement table, not a single headline number. A judge may be trustworthy on parseability and locator labels but untrustworthy on abstraction quality; the per-axis result is the decision-relevant output.

### 4.4 Judge variance probe

Run the judge more than once on at least one artifact (varying prompt phrasing or judge model) to record self-consistency. A judge that disagrees with itself cannot be calibrated against anyone.

---

## 5. What The Results Decide

The output of this study is a delegation map: for each review axis, one of:

```text
delegable        - judge agreement high; judge may run as first-pass evaluator, human spot-checks
assistive        - judge useful as a pre-screen, human verdict still required
not delegable    - judge unreliable on this axis; remains human-only
```

The delegation map is the explicit input to the autonomous-lab-loop plan's activation criteria. Without it, any automated loop is grading its own homework with an unmeasured grader.

A negative result is valuable: if the judge cannot reproduce human verdicts on any axis, the portfolio learns that scaling evaluation requires either better mechanical checks, tighter rubrics, or accepting the human bottleneck.

---

## 6. Method Boundaries

* Judge outputs are EvaluationRecord proposals at most; protocol v0.1 has no live LLM-judge evaluator type, so representing a live judge in committed records requires its own small ADR (the `manual_content_review` ADR 0002 is the precedent shape).
* The judge never reviews its own lab's method outputs in the same run that produced them.
* Judge prompts containing source text follow the same trace and privacy boundaries as pilot prompts: ignored local paths only.
* Judge results do not graduate anything, do not declare winners, and do not change currentness docs.
* Human review remains the authority during and after this study; calibration changes who runs first, not who decides.

---

## 7. Failure Modes

### Verdict leakage

The judge sees text that encodes the human verdict and parrots it.

Mitigation: blinded inputs assembled from ArtifactEnvelope and source excerpt only; leakage check before each trial.

### Sycophantic agreement

The judge passes everything because artifacts look plausible.

Mitigation: include the known-negative artifacts (chunked pilot 001's structural failure, pilot 005's invalid offsets) — a judge that passes those is disqualified on that axis.

### Rubric drift

The judge is scored against a rubric that differs from what the human actually applied.

Mitigation: reconstruct the rubric from the original evaluator plans and review records before any judge call; record the rubric hash.

### Small-sample overconfidence

Nine records produce a tidy-looking agreement table that does not generalize.

Mitigation: report counts, not percentages alone; mark every delegation-map entry as provisional until repeated on later pilots' reviews.

### Judge-model monoculture

Calibrating one judge model and treating the result as true of LLM judges generally.

Mitigation: record judge model/config per trial; treat the delegation map as per-judge-config.

---

## 8. Activation Criteria

Open `labs/llm_judge_calibration/` (or run this as a contained study inside an existing lab with an explicit admission packet) only when:

1. the operator intentionally chooses to start calibration work,
2. the study has an admission packet satisfying `docs/live-llm-experiment-admission.md`,
3. the blinding procedure and rubric reconstruction are written before any judge call,
4. judge model, config, and budget are locked in a run admission update,
5. and the work can remain lab-local without protocol changes (judge records stay proposal-only until an ADR defines their committed representation).

---

## 9. Non-Effects

This plan does not:

* create a new lab,
* change protocol,
* change synthesis,
* change benchmarks,
* create current milestone work,
* create export records,
* create evidence,
* declare any review axis delegable,
* authorize any autonomous loop,
* graduate anything,
* supersede active portfolio work.

---

## 10. Open Questions

* Should the first judge trial use the same model family as the pilots (DeepSeek V4) or a deliberately different family to avoid shared blind spots?
* How should per-axis tolerance be set for score agreement before trials begin, so the threshold is not fitted to the observed results?
* Can strict locator review be made fully mechanical (validated line ranges plus computed offsets), removing the judge from that axis entirely?
* How many human-reviewed artifacts are enough to mark an axis `delegable` rather than `assistive`?
* Should disagreements between judge and human trigger a second human review, and does that re-review change the recorded ground truth?
