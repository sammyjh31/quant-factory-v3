# Future Blockers And Mitigations

This document names likely V3 failure modes before they occur.

---

## Fixture Theater

Risk:

```text
The scaffold passes tests but teaches nothing.
```

Mitigation:

```text
Milestone two should run one tiny live LLM pilot, not ten labs.
```

---

## Evaluator Weakness

Risk:

```text
LLM judges or weak evaluators produce confident nonsense.
```

Mitigation:

```text
Add evaluator calibration later: human spot checks, known-bad fixtures, pairwise comparisons, and evaluator failure tags.
```

---

## Schema Churn

Risk:

```text
Real experiments expose missing protocol fields.
```

Mitigation:

```text
Allow lab-local payloads and notes. Require ADRs for protocol changes.
```

---

## Thin Benchmarks

Risk:

```text
Metadata-only benchmark packs do not stress methods enough.
```

Mitigation:

```text
Add small synthetic or redacted benchmark cases before raw corpus migration.
```

---

## Generated Synthesis Becoming Authority

Risk:

```text
Generated summaries become a new truth ledger.
```

Mitigation:

```text
Generated outputs are ignored by default, stamped non-authoritative, and never copied into currentness docs.
```

---

## Shared Helper Creep

Risk:

```text
Labs start sharing runtime code and become a monolith.
```

Mitigation:

```text
No shared lab runtime without an ADR and repeated use across at least two labs.
```

---

## Experiment Sprawl

Risk:

```text
Too many weak experiments create noise.
```

Mitigation:

```text
Every experiment must state what result would change future behavior.
```
