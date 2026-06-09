# QuantFactory V3 Federation

QuantFactory V3 is a federated LLM-methodology research portfolio for discovering how messy trader source material can become useful trading intelligence.

V3 is not one monolithic product repo. It is a research federation: independent labs explore different methods, while a tiny shared protocol lets their results be compared, synthesized, challenged, and eventually graduated.

The long-term goal is to discover how large bodies of trader education, transcripts, videos, examples, notes, charts, and related market context can be transformed into useful downstream artifacts, including but not limited to:

- reusable trading judgment,
- source-grounded study material,
- concept maps and contradiction maps,
- visual/deictic understanding,
- formula and data requirement recovery,
- source-native strategy candidates,
- cross-source research hypotheses,
- historically audited playbook candidates,
- operator review and calibration artifacts,
- and eventually hardened V4 product surfaces.

V3 is a laboratory. V4 will inherit only the methods, schemas, artifacts, evaluations, and product directions that survive repeated evidence across the V3 research federation.

---

## Core Principle

```text
Many methods explore independently.
Every method reports comparably.
Nothing becomes architecture until it has repeated evidence and an explicit decision.
```

Labs may be methodologically weird. Exports must be boring.

---

## Why This Repo Exists

The purpose of this repository is to maintain the V3 federation harness: independent labs, a tiny shared protocol, benchmark packs, live-experiment admission guardrails, read-only synthesis, currentness routing, and tests.

The original milestone-one scaffold did not try to answer the research questions. It created the measurement and comparison harness needed before live LLM experiments could begin.

Current work uses that harness for proposal-only live pilots, manual reviews, method comparisons, and bounded research planning without turning any single experiment into architecture.

Future milestones will add broader LLM method runs, model comparisons, source-grounding evaluations, multimodal experiments, graph-building experiments, product-output experiments, and cross-lab graduation reviews.

---

## Research Questions V3 Is Designed To Explore

V3 is organized around methodological questions, not product guesses.

Examples:

* How can LLMs extract reusable trading judgment from messy trader text?
* How can LLMs preserve exact source grounding while still producing useful abstraction?
* How can LLMs combine transcripts, captions, chart frames, and deictic language into grounded visual understanding?
* How can LLMs recover formulas, parameters, and data requirements from trader education?
* How can LLMs discover stable concepts across noisy, inconsistent trading sources?
* How can LLMs preserve and reason over contradictions between trader sources?
* How can source-ingested material become research tasks, strategy hypotheses, playbook candidates, or judgment artifacts?
* Which ingestion and extraction methods work best for which downstream use?
* How can the research system learn from failures without turning them into hidden authority?

---

## Federation Shape

This repo starts as one workspace:

```text
quantfactory-v3-federation/
  packages/qf_v3_protocol/
  packages/qf_v3_synthesis/
  benchmarks/
  labs/
  docs/
  generated/
  tests/
```

Only two installable shared packages exist today:

* `qf_v3_protocol`
* `qf_v3_synthesis`

Labs are intentionally not installable packages yet. They are isolated research workspaces that export protocol-valid export records appropriate to their current phase.

---

## Current Phase

Current phase: `milestone-4-first-graduation-candidate`

The scaffold baseline is accepted, and the portfolio has moved from isolated live-pilot recording into method-comparison work. README owns the project purpose, commands, and routing. It does not own pilot-level evidence or method conclusions.

Current status is routed through:

* `PORTFOLIO_CURRENT.md`
* `LAB_REGISTRY.md`
* `labs/chunked_source_grounding/PLANNING/comparisons/live_pilot_method_comparison_001.md`
* `docs/llm-experimentation-model.md`
* `docs/research-lifecycle.md`
* `docs/live-llm-experiment-admission.md`

The current next proposed research step is owned by `PORTFOLIO_CURRENT.md`.

The live records are proposal-only. They are not validation, product evidence, strategy evidence, financial advice, live-trading authority, graduation, or architecture.

Milestone one was not a limitation on V3’s ambition. It created the first safety and comparison harness.

Live-pilot planning packets remain under each lab's `PLANNING/` directory. Planning packets are not in `EXPORTS/`, are not imported by synthesis, and are not research evidence.

---

## Fixture Records Are Not Evidence

Milestone-one lab records are fixtures for protocol validation.

They are not real research evidence. They do not prove that a method works. They do not validate a product direction. They do not create architecture.

Future live experiments must pass the live LLM experiment admission checklist before running.

---

## Architecture Rule

```text
No new experiment becomes architecture.
It becomes records first.
Architecture changes only after repeated evidence and explicit ADR.
```

This rule exists to keep V3 exploratory without recreating V2-style drift.

---

## Commands

Common verification commands:

```bash
uv run pytest
uv run ruff check .
uv run qf-v3-validate
uv run qf-v3-synthesis
```

---

## Generated Outputs

Generated synthesis outputs are ignored by default and non-authoritative.

Synthesis may summarize export records, but it does not mutate labs, declare winners, graduate methods, or become portfolio authority.

---

## V2 Relationship

V2 is used as benchmark memory and failure memory, not inherited architecture.

V2 contributes lessons such as:

* weak source grounding,
* report-only confusion,
* visual/deictic blockers,
* formula/data blockers,
* generated artifact drift,
* authority/documentation drift,
* and the danger of turning temporary experiment paths into permanent architecture.

V3 does not import V2’s process model as doctrine.
