# Live Pilot Packet Template

Status: agent checklist / packet template
Derived from: `labs/long_context_judgment/PLANNING/live_llm_pilot_001/`, `labs/chunked_source_grounding/PLANNING/live_llm_pilot_006/`, and `labs/long_context_judgment/PLANNING/live_llm_pilot_002/`

This checklist standardizes the file set and required content of a live LLM pilot planning packet so that drafting a new packet costs minutes, not a rediscovery of conventions. It does not replace `docs/live-llm-experiment-admission.md`; every packet must still satisfy that checklist. It does not authorize execution; execution always requires a separate explicit instruction.

A template instantiation is planning structure only. It is not research evidence, not a synthesis export, and not a method success claim.

---

## Canonical Packet Location And Naming

```text
labs/<lab_id>/PLANNING/live_llm_pilot_NNN/
```

* `NNN` continues the lab's own pilot numbering.
* Experiment id: `<lab_id>_live_pilot_NNN`
* Method id: `<lab_id>_live_pilot_NNN_method`
* Goal label: use the next portfolio goal letter for planning (packet) vs execution (separately authorized run).

## Canonical File Set

Every packet contains exactly these eight files unless the admission doc explains why one is absent or extra:

```text
admission.md
evaluator_plan.md
experiment_card.proposed.json
method_card.proposed.json
prompt_template.live_pilot_NNN.md
run_admission_update.md
source_privacy_boundary.md
stop_condition.md
```

---

## Per-File Required Content

### admission.md

* Status line with goal label; lab; experiment id.
* Proposal-only framing: not a completed run, not evidence, not a synthesis export; execution requires a separately authorized goal.
* **Hardening / cleanup discipline section**: what existing packet pattern is reused, and — required — what this pilot deliberately does *not* copy from its predecessors and why. A packet that cannot state its delta should not exist.
* All twelve admission checklist items, each either resolved inline or pointing at the packet file that owns it: benchmark pack (with known difficulty, failure modes, `v2_lesson_refs`, metadata safety), MethodCard, ExperimentCard (with the result-that-would-change-future-behavior statement), evaluator plan, source/privacy boundary, prompt/template hash plan, model/config recording plan, output artifact types (requested and explicitly not requested), negative-result value, stop condition, budget/secrets, proposal-only statement.

### method_card.proposed.json / experiment_card.proposed.json

* Protocol-valid records (`protocol_version`, `schema_name`, current `schema_version`).
* Mirror the field structure of the most recent accepted packet's cards.
* `known_risks` first entry: "This is a proposed live LLM pilot planning record, not a completed run."
* `non_goals` include: not evidence, not a synthesis export, not strategy validation, not product authority, not architecture or graduation evidence.
* Run `uv run qf-v3-validate` (or the test suite) to confirm the proposed cards stay schema-valid.

### prompt_template.live_pilot_NNN.md

* Placeholders only (`{{APPROVED_SOURCE_TEXT}}`, `{{APPROVED_SOURCE_REF}}`); never raw source text, private notes, or secrets.
* System Message section + User Message section with a strict JSON output contract: top-level keys, per-key entry caps, and per-entry field shapes.
* Locator policy when source grounding is in scope: line ranges only; never ask the model for character offsets or quote hashes; local tooling computes those after line-range validation.
* Explicit exclusion list (no strategy, validation, trading advice, playbook content, product-like artifacts).

### evaluator_plan.md

* Planned evaluator types from the current protocol enum (`schema_check`, `manual_boundary_review`, `manual_content_review`).
* What each evaluator does and does not measure.
* The review question, expected failure tags, and which prior pilots the review must preserve comparison value against.

### source_privacy_boundary.md

* Approved source scope with canonical source ref, full excerpt SHA-256, word count, selected local path, and recorded origin path.
* Local-only/ignored rules for raw source, prompts containing source, traces, payloads.
* What committed records may contain (metadata-safe identifiers only).

### run_admission_update.md

* Provider, base URL, exact model id, thinking mode, tool routing, and the no-silent-substitution rule.
* Run scope: one pilot, one source scope, one prompt version, one config, one model-call batch; no retries unless the call fails before producing output; any change requires a new admission update.
* Committed prompt template path + SHA-256; canonical model config JSON + SHA-256; input/output token caps with the reason for the output cap.
* Budget hard cap; secret env var name (never value); allowed ignored trace paths; expected post-run export file paths and artifact type.

### stop_condition.md

* Planning goal stops at packet creation and verification.
* Pre-call abort list for the execution goal: missing source, untracked-source violations, missing secret, unavailable model, budget breach, config deviations, contract expansion, trace-commit risks, authority-claim risks.
* The no-retry rule.

---

## After Instantiation

* Verify with `uv run pytest` and `uv run qf-v3-validate`.
* Update the currentness doc that owns the next-step claim (`PORTFOLIO_CURRENT.md`) if this packet is the portfolio's proposed next step; do not duplicate packet detail there.
* Check the stale-direction cleanup checklist: does this packet supersede an older planning packet, fixture, or claim? If so, mark or rework it.
* Do not create export records, evaluation records, or comparison-note rows from a packet. Those exist only after a separately authorized run.
