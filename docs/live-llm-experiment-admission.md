# Live LLM Experiment Admission

Status: live LLM experiment guardrail
Current phase: `milestone-4-first-graduation-recorded`

No live LLM experiment may run until it has satisfied this checklist.

Passing this checklist does not mean the method works. It only means the experiment is allowed to run under the V3 federation protocol.

---

## Required Checklist

A live LLM experiment must define:

1. Active benchmark pack
2. MethodCard
3. ExperimentCard
4. Evaluator plan
5. Source/privacy boundary
6. Prompt/template hash plan
7. Model/config recording plan
8. Output artifact types
9. Negative-result value
10. Stop condition
11. Budget/secrets handling
12. Proposal-only statement

---

## 1. Active Benchmark Pack

The experiment must name at least one active benchmark pack.

It must document:

- benchmark_pack_id,
- known difficulty,
- known failure modes,
- v2_lesson_refs,
- metadata safety status.

---

## 2. MethodCard

The experiment must have a MethodCard.

The MethodCard must document:

- method_id,
- lab_id,
- method family,
- intended inputs,
- intended outputs,
- known risks,
- non-goals.

---

## 3. ExperimentCard

The experiment must have an ExperimentCard.

The ExperimentCard must document:

- research question,
- hypothesis,
- benchmark pack,
- method ids,
- evaluation plan,
- expected artifact types.

It must state what result would change future behavior.

---

## 4. Evaluator Plan

The experiment must document:

- evaluator ids,
- evaluator types,
- what each evaluator measures,
- known evaluator limitations,
- expected failure tags.

If an LLM judge is used, the model/config must be recorded and the judge result must not be treated as final authority without calibration.

---

## 5. Source / Privacy Boundary

The experiment must document:

- source scope,
- whether raw source text is used,
- whether private notes are used,
- whether provider payloads are stored,
- whether prompts or traces include source text,
- what is committed to git,
- what is ignored or local-only.

Private notes, provider payloads, raw model traces, secrets, and raw source material must not be committed unless a later explicit policy allows it.

---

## 6. Prompt / Template Hash Plan

The experiment must document:

- prompt/template file or construction method,
- prompt/template hash plan,
- system prompt hash plan if applicable,
- tool instruction hash plan if applicable.

Prompt text may be committed only if it contains no private/raw source material and no secrets.

---

## 7. Model / Config Recording Plan

The experiment must document:

- provider id,
- model id,
- sampling settings,
- context/token settings,
- tool routing if applicable,
- config hash.

Config records must not include secrets.

---

## 8. Output Artifact Types

The experiment must define expected artifact types before running.

Examples:

- judgment_principle_proposal,
- source_grounded_claim,
- visual_deictic_binding_candidate,
- unsupported_claim_report,
- formula_candidate,
- contradiction_pair,
- study_card_candidate.

Outputs must use ArtifactEnvelope records.

---

## 9. Negative-Result Value

The experiment must state what will be learned if it fails.

Examples:

- method loses source grounding,
- method over-abstracts trader intent,
- method hallucinates visual objects,
- method cannot recover formulas,
- evaluator cannot detect unsupported claims.

---

## 10. Stop Condition

The experiment must define when to stop.

Examples:

- maximum runs,
- maximum budget,
- repeated failure pattern,
- grounding below threshold,
- no improvement over baseline,
- human review says output is not useful.

---

## 11. Budget / Secrets Handling

The experiment must document:

- expected model-call budget,
- environment variables required,
- secret names without values,
- trace/log storage,
- gitignore behavior.

Secrets must never be committed.

---

## 12. Proposal-Only Statement

Every live LLM experiment must include:

```text
Outputs from this experiment are proposals until evaluated. They do not create source truth, role support, data truth, validation, strategy evidence, financial advice, product authority, live-trading authority, or architecture.
```

---

## Future Schema Note

A later protocol version may replace this document with a formal LiveExperimentAdmission schema.

This guardrail was introduced in scaffold v0.1 and remains the required admission boundary until a formal schema replaces it.
