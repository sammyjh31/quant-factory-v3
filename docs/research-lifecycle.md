# Research Lifecycle

This document describes how V3 research should progress from scaffold to live experiments to eventual graduation.

---

## Milestone 1 — Scaffold

Purpose:

```text
Build the measurement and comparison harness.
```

Milestone one creates:

* protocol schemas,
* benchmark manifests,
* lab fixture exports,
* validation tooling,
* read-only synthesis,
* currentness docs,
* and tests.

Milestone one does not produce real research evidence.

Fixture records are protocol-validation examples only.

---

## Milestone 2 — Tiny Live LLM Pilot

Purpose:

```text
Run one small live LLM experiment through the admission gate.
```

A milestone-two pilot should use:

* one lab,
* one active benchmark pack,
* one MethodCard,
* one ExperimentCard,
* one evaluator plan,
* one controlled source scope,
* one clear stop condition.

The goal is not to get a breakthrough. The goal is to prove that real LLM runs can be recorded, evaluated, and contained.

---

## Milestone 3 — Method Comparison

Purpose:

```text
Compare two or more methods on the same benchmark pack.
```

Example:

* long-context reader vs chunked source-grounding reader.

---

## Milestone 4 — Evaluator Comparison

Purpose:

```text
Compare evaluator types.
```

Examples:

* schema checks,
* code checks,
* human review,
* LLM judge,
* pairwise comparison.

Evaluator weakness is expected and should be recorded.

---

## Milestone 5 — Cross-Pack Repeat

Purpose:

```text
Run the same method across multiple benchmark packs.
```

This tests whether a method generalizes or only works on one kind of source.

---

## Milestone 6 — Cross-Lab Synthesis

Purpose:

```text
Compare lessons across labs.
```

Synthesis can identify patterns, failures, and possible reusable methods.

Synthesis does not graduate anything by itself.

---

## Milestone 7 — Graduation Review

Purpose:

```text
Decide whether something should harden toward V4.
```

Graduation requires repeated evidence and explicit ADR.

---

## Permanent Rule

```text
No new experiment becomes architecture.
It becomes records first.
Architecture changes only after repeated evidence and explicit ADR.
```
