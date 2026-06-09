# Long Context Judgment Live Pilot 002 Evaluator Plan

Status: Goal 13B planning/admission record

This plan defines evaluator intent only. It does not create an EvaluationRecord and does not call an LLM.

---

## Planned Evaluators

Planned post-run evaluator types:

* `schema_check`
* `manual_boundary_review`
* `manual_content_review`

`schema_check` validates record shape only.

`manual_boundary_review` checks containment, proposal-only status, selected-source boundaries, trace boundaries, model/config adherence, line-range-only locator boundaries, and non-authority language. It does not evaluate method quality.

`manual_content_review` may be used after a run to judge both halves of the comparison question:

1. **Abstraction half**, compared against `long_context_judgment_live_pilot_001`: do the judgment principle proposals preserve the trader's conditional logic, caveats, and failure conditions; do they avoid generic advice and `over_abstracted_teacher_intent`; do they recover breadth that the narrowed chunked contracts traded away as `limited_abstraction`?
2. **Grounding half**, compared against `chunked_source_grounding_live_pilot_006`: do source-linked claims have reviewable line-range locator candidates; does each proposed line range directly support its claim; can local review compute character offsets and a computed quote hash after accepting the line range; are locator labels honest; do the principles actually rest on their cited supporting claims?

The locator labels for review are:

```text
exact | approximate | broad | missing
```

Use `overclaimed_exactness` when the model labels a candidate as `exact` but local review shows it is approximate, broad, missing, or unsupported.

Use `unsupported_principle_link` review notes when a judgment principle cites a supporting claim that does not actually support it.

The review should preserve comparison value against both `long_context_judgment_live_pilot_001` and `chunked_source_grounding_live_pilot_006`.

---

## Grounded Abstraction Review Question

The expected content review question is:

```text
Did adding line-range grounding discipline preserve, weaken, or destroy the broader judgment abstraction that the long-context method family is supposed to provide?
```

Review should treat an honest negative answer as more useful than a generous positive one. Expected failure tags include:

* `over_abstracted_teacher_intent`
* `generic_advice`
* `limited_abstraction`
* `lost_conditionality`
* `overclaimed_exactness`
* `weak_source_grounding`
* `unsupported_claim`

There is no new evaluator type in Goal 13B.

No evaluator may create validation, product evidence, strategy evidence, financial advice, live-trading authority, graduation, or architecture.
