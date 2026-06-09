# Long Context Judgment Live Pilot 003 Admission Packet

Status: Goal 14A proposed planning packet
Lab: `long_context_judgment`
Experiment: `long_context_judgment_live_pilot_003`

This is a proposed live LLM pilot planning record. It is not a completed run, not research evidence, and not a synthesis export. Execution requires a separately authorized Goal 14B instruction; the operator's milestone-4 goal directive supplies that authorization for this evidence chain.

This packet contains no RunRecord, ArtifactEnvelope, EvaluationRecord, or ResearchNote. No method success is claimed.

The Goal 13D decision review recommended a cap-relieved grounded long-context repeat to remove the output-cap confound. Goal 14A is that packet.

---

## Hardening / Cleanup Discipline And Delta From Pilot 002

This packet reuses the pilot 002 planning pattern and changes exactly two variables; everything not listed below is identical to the pilot 002 packet and is owned by the corresponding pilot 002 file where referenced.

Deltas:

1. **Output cap raised from `1600` to `4000` tokens** — the cap-relieved repeat the Goal 13D review recommended. The output contract itself is unchanged (verified byte-identical message body to pilot 002's template).
2. **Thinking enabled** — recorded as `thinking: {"type": "enabled"}`, by explicit operator direction for the milestone-4 evidence chain. Hypothesized to specifically improve line-range pointing, which is exactly what failed in pilot 002.

Attribution limit, stated up front: because both the cap and the thinking mode change, a success cannot be attributed to either variable alone. For the milestone-4 graduation question this is acceptable: the decision-relevant question is whether any grounded long-context configuration can produce support-valid locators with preserved abstraction, not which variable fixes it. A failure remains attributable: if locators still fail with a relieved cap and thinking enabled, single-pass grounded long-context is disconfirmed much more strongly.

## Active Benchmark Pack

Benchmark pack: `text_judgment_v0` — same difficulty, failure modes, `v2_lesson_refs` (`weak_source_grounding`, `report_only_confusion`), and metadata-safety status as recorded in the pilot 002 admission packet, plus one pilot-002-derived failure mode: grounded-but-mislocated line ranges with overclaimed exactness.

## MethodCard / ExperimentCard

* `labs/long_context_judgment/PLANNING/live_llm_pilot_003/method_card.proposed.json` (`long_context_judgment_live_pilot_003_method`)
* `labs/long_context_judgment/PLANNING/live_llm_pilot_003/experiment_card.proposed.json` (`long_context_judgment_live_pilot_003`)

The experiment asks:

```text
With the output cap relieved and thinking enabled, can the grounded long-context contract produce support-valid line-range locators while preserving the abstraction quality pilot 002 demonstrated?
```

Result that would change future behavior:

```text
If locators become support-valid with abstraction preserved, grounded long-context becomes supporting cross-method evidence for the line-range-first graduation nomination. If locators still fail, the single-pass grounded variant is disconfirmed without the cap confound, and the two-pass split becomes the lab's recommended direction.
```

## Evaluator Plan

Same three evaluators and review questions as `labs/long_context_judgment/PLANNING/live_llm_pilot_002/evaluator_plan.md`, with comparison value preserved against pilots 001, 002, and chunked 006. Strict review reuses the pilot 006 rubric and labels (`exact | approximate | broad | missing`, `overclaimed_exactness`).

## Source / Privacy Boundary

Identical to `labs/long_context_judgment/PLANNING/live_llm_pilot_002/source_privacy_boundary.md`: same selected second-source excerpt (`raw_corpora_sha256:9f9e143429f5842a`, 945 words, 140 lines), same local-only path rules, same prohibition on falling back to the full corpus path. Keeping the source fixed makes pilot 003 a one-source-change-free comparison against pilots 002 and 006.

## Prompt / Template Hash Plan

Prompt/template: `labs/long_context_judgment/PLANNING/live_llm_pilot_003/prompt_template.live_pilot_003.md` (SHA-256 `1ad7a5625086b952cc4f10de0c2dae10281293d6e162a8a9f13c9c0d80db393a`). Message body verified byte-identical to pilot 002's contract; only header/ids differ.

## Model / Config Recording Plan

Locked in `labs/long_context_judgment/PLANNING/live_llm_pilot_003/run_admission_update.md`.

## Output Artifact Types

Expected post-run artifact type: `grounded_long_context_judgment_proposal`, same five sections and same exclusions as pilot 002.

## Negative-Result Value

If this pilot fails it cleanly disconfirms single-pass grounded long-context without the cap confound, records whether thinking changes locator pointing, and steers the lab toward a two-pass split — all of which sharpen the graduation ADR's known-failure-modes section.

## Stop Condition

`labs/long_context_judgment/PLANNING/live_llm_pilot_003/stop_condition.md`. Goal 14A stops at packet verification; Goal 14B stops after one approved call.

## Budget / Secrets Handling

Budget cap `$3` hard maximum; secret name `DEEPSEEK_API_KEY` (name documented, value never committed); traces only under ignored local paths.

## Proposal-Only Statement

Outputs from this experiment are proposals until evaluated. They do not create source truth, role support, data truth, validation, strategy evidence, financial advice, product authority, live-trading authority, or architecture.
