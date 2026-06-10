# Portfolio Current

Status: portfolio currentness router
Current phase: `milestone-5-evaluation-calibration`
Protocol version: `qf-v3-protocol-0.1`

This file owns the current portfolio posture. It routes agents to current evidence surfaces, but it does not own lab results, method success claims, generated synthesis claims, or graduation decisions.

---

## Current Portfolio Purpose

QuantFactory V3 is a federated LLM-methodology research portfolio.

The scaffold baseline has been accepted, and the portfolio has moved into method-comparison work. Detailed pilot-level evidence lives in protocol export records and lab-local comparison notes.

Milestone 4 goal, set by operator decision, is complete: line-range-first source grounding went through the full evidence ladder to an ADR-approved graduation decision (GRAD-0001, ADR 0003) — the first graduation in the portfolio's history. The evidence items were the grounded long-context comparison (pilots 003/004), the thinking-enabled configuration repeat, and the third-source repeat (chunked pilot 007), with negative results recorded along the way.

The current local comparison note is:

```text
labs/chunked_source_grounding/PLANNING/comparisons/live_pilot_method_comparison_001.md
```

The scaffold exists so live LLM experiments can be measured, compared, and contained.

---

## Active federation labs

Active federation labs:

1. `long_context_judgment`
   - Parent question: How can long-context LLM methods extract reusable trading judgment from messy trader text?
   - Current state: active live-pilot lab with four proposal-only live pilots including the milestone-4 grounded-variant evidence runs.

2. `chunked_source_grounding`
   - Parent question: How can chunked/source-span LLM methods preserve grounding while still supporting useful abstraction?
   - Current state: active live-pilot lab with seven proposal-only live pilots; the locator thread's method lesson graduated as GRAD-0001.

3. `llm_judge_calibration`
   - Parent question: Can an LLM judge reproduce operator-lineage review verdicts on existing live-pilot artifacts, and on which review axes?
   - Current state: active live-pilot lab (milestone 5) with a pre-registered blinded judge-agreement study.

4. `visual_deictic_understanding`
   - Parent question: How can multimodal or vision-language LLM workflows bind transcript/deictic language to visual chart context?
   - Current state: scaffold fixture exports only.

---

## Active Benchmark Packs

Active benchmark packs:

1. `text_judgment_v0`
2. `source_grounding_v0`
3. `visual_deictic_v0`

Future candidate benchmark topics are listed under `benchmarks/future_candidates/` but are not active benchmark packs.

---

## Current Evidence Posture

Scaffold fixture records are not real research evidence.

Proposal-only live pilot records exist across two labs, including bounded negative results, manual and strict reviews, and one completed method-comparison loop. Pilot-level findings live in export records and the owning comparison note; currentness docs intentionally do not repeat them.

These records are proposal-only research records. They are not validation, product evidence, strategy evidence, financial advice, live-trading authority, graduation, or architecture.

Future live LLM experiments must pass the admission checklist in:

```text
docs/live-llm-experiment-admission.md
```

---

## Current Architecture Rule

```text
No new experiment becomes architecture.
It becomes records first.
Architecture changes only after repeated evidence and explicit ADR.
```

---

## Synthesis Status

Synthesis is read-only.

It may import and summarize export records, but it does not:

* mutate lab files,
* mutate benchmark files,
* mutate protocol schemas,
* mutate currentness docs,
* declare winning methods,
* graduate methods,
* or become authority.

Generated synthesis outputs are ignored by default.

---

## Graduation Status

One method pattern has graduated: GRAD-0001, the line-range-first source locator workflow, by operator decision and ADR 0003. Nothing else has graduated.

See:

```text
GRADUATION_LEDGER.md
docs/adr/0003-graduate-line-range-first-locator-workflow.md
```

---

## Next Recommended Research Direction

Milestone 4 is complete: the milestone-4 evidence thread (long-context pilots 003/004, chunked pilot 007) and the GRAD-0001 graduation decision are recorded. The owning comparison note is:

```text
labs/chunked_source_grounding/PLANNING/comparisons/live_pilot_method_comparison_001.md
```

Milestone 5 (evaluation calibration, operator-selected) has run its first batch: the `llm_judge_calibration` lab completed the pre-registered 17-trial blinded judge-agreement study. Both review axes landed at `assistive` under the pre-registered thresholds, with zero sycophancy on four negative controls and stable self-consistency. Details are owned by `labs/llm_judge_calibration/EXPORTS/`.

Open items, in recorded priority order:

1. Operator usefulness review — the paired downstream experiment awaits the operator's answers at `labs/long_context_judgment/PLANNING/usefulness_review_001/operator_review_form.md`; those answers become the portfolio's first downstream-usefulness ground truth.
2. A pre-registered follow-up judge trial set restricted to GRAD-0001-pattern artifacts — the first batch's post-hoc observation (4/4 verdict match, score gaps <= 0.05 on line-range-anchored trials) needs its own pre-registration before any delegable claim.
3. Rubric policy fixes surfaced by the study: encode truncation-handling policy explicitly so judge and human apply the same rule.
4. Cross-model-family repeat of line-range-first — the explicit limitation recorded in ADR 0003 (blocked on a second provider key or a local model).
5. The recursive contextual meaning loop plan, building on graduated locator discipline.

The autonomous-lab-loop plan under `docs/research-plans/` remains a future plan gated on calibration results; `assistive` does not satisfy its L2 entry requirement.
