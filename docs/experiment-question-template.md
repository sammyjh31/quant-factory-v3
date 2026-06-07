# Experiment Question Template

Every serious future experiment should answer these questions before it runs.

---

## Research Question

What are we trying to learn?

---

## Hypothesis

What do we expect this method to do better or worse?

---

## Competing Methods

What are we comparing?

If there is only one method, what baseline or failure case is it being compared against?

---

## Benchmark Pack

Which benchmark pack tests this question?

Why is that pack appropriate?

---

## Expected Artifacts

What should the method produce?

Examples:

- judgment principle proposal,
- source-grounded claim,
- visual binding candidate,
- contradiction pair,
- formula candidate,
- unsupported claim report,
- study card candidate.

---

## Evaluators

How will we judge:

- grounding,
- usefulness,
- hallucination,
- abstraction quality,
- contradiction handling,
- failure value?

---

## Negative Result Value

If this fails, what do we learn?

---

## Stop Condition

When do we stop instead of iterating forever?

---

## Graduation Implication

What would this result make us trust more, trust less, or test next?

---

## Architecture Rule

```text
No new experiment becomes architecture.
It becomes records first.
Architecture changes only after repeated evidence and explicit ADR.
```
