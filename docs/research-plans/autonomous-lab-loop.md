# Autonomous Lab Loop

Status: future method plan
Origin: operator direction — evolve V3 toward labs that run their own research loops, with agents testing hypotheses against the portfolio's parent questions
Current state: not active lab, not protocol, not architecture, not current milestone, not export evidence, not graduation
Candidate future shape: per-lab agent loops, not a new lab

This document preserves a future V3 orchestration plan. It is not current portfolio authority and does not change the active portfolio work.

Gating plan: [llm-judge-calibration-study](llm-judge-calibration-study.md). No level of loop autonomy beyond drafting activates until that study produces a delegation map.

---

## 1. One-Sentence Thesis

Can an agent execute the already-documented lab lifecycle — plan, admit, run, evaluate, recommend the next fork — concurrently across labs, producing packets and reviews of operator quality, without violating the federation's containment rules?

---

## 2. Why This Plan Exists

The seven live pilots to date have been a human-paced rehearsal of a loop that is already fully documented:

```text
research question -> admission packet -> run admission update -> (separately authorized) live run
-> export records -> manual + strict review -> comparison note -> decision review -> next fork
```

Every stage of that loop exists as an explicit file convention: admission packets under `PLANNING/`, the checklist in `docs/live-llm-experiment-admission.md`, evaluator plans, stop conditions, export records, and decision reviews like Goal 13A. Agents can execute a documented lifecycle; they cannot execute an implicit one. V3 has spent its first milestones making the lifecycle explicit, which is precisely the prerequisite for automating it.

The long-term operator intent is a federation where each lab pursues its parent research question simultaneously, in a learning loop: hypotheses are proposed, admitted, run, evaluated, and folded back into the next hypothesis — with the human moving from doing every step to governing the gates.

This plan exists so that intent is recorded inside V3's governance instead of living outside it, and so the path there is incremental and measurable rather than a leap.

---

## 3. The Autonomy Ladder

Autonomy increases one rung at a time, per lab, with explicit operator promotion between rungs. A lab can sit at a different rung than its neighbors.

### L0 — Operator-executed (current state)

The operator (with agent assistance in-session) performs every stage. All seven pilots to date are L0.

### L1 — Agent-drafted, human-everything-else

The agent drafts admission packets, prompt templates, and run admission updates from the lab's open forks. The operator reviews and edits every packet, authorizes execution, performs all reviews, and writes decision reviews.

Entry requirement: the live-pilot packet template exists (`docs/agent-checklists/live-pilot-packet-template.md`).

Exit evidence: agent-drafted packets repeatedly pass operator review with only minor edits.

### L2 — Agent-run, judge-assisted, human-gated

The agent drafts packets, the operator approves admission and budget, the agent executes the run and produces export records, a calibrated LLM judge performs first-pass review on its `delegable` and `assistive` axes, and the operator reviews everything the judge flags plus a fixed spot-check fraction of what it passes.

Entry requirement: the calibration study's delegation map exists and at least one review axis is `delegable`.

Exit evidence: judge-passed, human-spot-checked artifacts show no missed failures across multiple pilots.

### L3 — Concurrent lab loops, human at the gates

Multiple labs run L2 loops simultaneously. Each loop iterates within a budget envelope and stop conditions approved in advance. The operator's recurring touchpoints shrink to: admission/budget approval per iteration batch, judge-flag review, decision reviews at fork points, and all portfolio-level authority.

Entry requirement: at least one lab has completed multiple L2 iterations cleanly, and cross-lab budget accounting exists.

There is no L4 in this plan. The gates below never automate.

---

## 4. Permanent Human Gates

These remain human-only at every rung, by design, because they are exactly the authority surfaces the federation exists to protect:

* graduation decisions and the `GRADUATION_LEDGER.md`,
* ADRs and any protocol or schema change,
* currentness docs (`PORTFOLIO_CURRENT.md`, `LAB_REGISTRY.md`, `PROTOCOL_CURRENT.md`, `README.md`),
* source-scope and privacy-boundary approval for any new source material,
* budget ceilings and secrets,
* activating a new lab or a new methodology thread,
* and promotion of any lab up this ladder.

An autonomous loop is the maximum-drift scenario V3's rules were written against: a system that generates records, evaluates them itself, and quietly accumulates authority. The evidence ladder (`fixture -> proposed run -> evaluated run -> repeated evidence -> graduation candidate -> ADR-approved architecture`) applies to loop outputs with no shortcuts: nothing a loop produces rises above `evaluated run` without human review, and nothing reaches architecture without an ADR.

---

## 5. Loop Mechanics (per lab, per iteration)

One iteration of a lab loop is one bounded pilot cycle:

1. **Fork selection.** Read the lab's open candidate forks from its decision reviews and comparison notes. Select the highest-value fork that has an explicit evidence need. If no fork has an explicit evidence need, stop and report — do not invent work.
2. **Packet drafting.** Instantiate the packet template for the selected fork. Reuse prior packet structure; state what the new pilot deliberately does not copy from its predecessors.
3. **Admission gate.** Human approval at L1/L2; batch approval at L3.
4. **Execution.** One tiny run under the locked config, stop conditions, and budget. No retries except provider failure before output, exactly as current pilots.
5. **Records.** Proposal-only export records, same shapes as today.
6. **Evaluation.** Mechanical checks first (line-range validation, offsets, hashes), then judge axes per the delegation map, then human review per rung.
7. **Fold-back.** Update the lab's comparison note with the new row, append candidate forks, and draft (not decide) the next-fork recommendation. Decision reviews remain human.

Iteration invariants:

* every iteration is one packet, one run, one export set — no batching of model calls inside an iteration,
* every iteration has a stop condition written before execution,
* a loop halts after any iteration whose review finds a containment violation, and stays halted until a human restarts it,
* and a loop never modifies another lab's files, shared packages, benchmarks, or protocol.

---

## 6. What "Learning" Means Here

The loop's learning is the portfolio's existing learning mechanism, executed faster: negative results steer the next fork; repeated positive signals motivate repeat-on-new-source pilots; repeated evidence across sources and labs accumulates toward graduation nominations that humans decide.

The loop does not get memory beyond the records. Lessons live in comparison notes, decision reviews, and export records — exactly where they live now — so that an iteration's reasoning is always reconstructible from committed artifacts. No hidden state, no agent-private scratch memory that outlives an iteration, no "the loop knows" claims.

---

## 7. Failure Modes

### Authority laundering

The loop cites its own prior outputs as evidence that its method works.

Mitigation: the evidence ladder applies unchanged; judge and human review label evidence stage explicitly; synthesis stays read-only.

### Packet cargo-culting

Agent-drafted packets copy predecessor packets' words without their reasoning, hollowing out admission into ritual.

Mitigation: every packet must state what it deliberately does not copy from its predecessor and why; human packet review at L1 specifically grades this.

### Evaluation drift

The judge's standards drift from the human's over time as artifacts change shape.

Mitigation: the delegation map is per-judge-config and provisional; recalibrate when artifact types change; spot-check fraction never reaches zero.

### Runaway spend

Concurrent loops multiply small budgets into large ones.

Mitigation: per-iteration hard caps as today (`$3`-scale), per-lab envelopes, and a portfolio ceiling approved per batch; loops halt, never borrow.

### Fork churn

The loop endlessly generates plausible next pilots, accumulating planning packets faster than evidence.

Mitigation: fork selection requires an explicit evidence need recorded in a decision review; "no eligible fork" is a stop state, not a prompt to invent one.

### Doc sprawl

Each iteration adds files; the repo becomes append-only by automation.

Mitigation: the loop runs the existing stale-direction cleanup checklist as part of fold-back; superseded planning material is archived or reworked per `AGENTS.md` §4.

---

## 8. Activation Criteria

Begin L1 for a single lab only when:

1. the operator intentionally chooses a first lab (the natural candidate is whichever lab owns the next open fork after Goal 13B/13C closes),
2. the packet template checklist exists and matches current packet conventions,
3. and the operator commits to reviewing L1 drafts against the cargo-culting failure mode, not just for correctness.

Begin L2 only when the calibration study (see gating plan) yields at least one `delegable` axis and the mechanical locator checks are implemented as local tooling.

Begin L3 only after multiple clean L2 iterations in one lab and explicit operator decision.

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
* authorize any agent to run a live pilot,
* promote any lab to any rung,
* graduate anything,
* supersede active portfolio work.

---

## 10. Open Questions

* Should fork selection at L3 be able to propose cross-lab comparison pilots, or must those always originate from a human decision review?
* What is the right spot-check fraction at L2, and should it decay with clean history or stay fixed?
* How should concurrent loops share the raw-corpora source-selection process, which is currently operator-approved per excerpt?
* Does the loop need its own protocol record type eventually (iteration record), or are existing RunRecord/ResearchNote shapes enough?
* What scheduling substrate runs the loops (operator-started sessions, scheduled agents, or something else), and does that choice affect containment?
* When a loop halts on a containment violation, what is the minimum human investigation before restart?
