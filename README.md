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

The purpose of this repository is to create the first V3 federation scaffold.

The scaffold does not try to answer the research questions yet. It creates the measurement and comparison harness needed before live LLM experiments begin.

Milestone one proves that independent labs can publish comparable fixture records through a shared protocol, and that synthesis can read those records without becoming authority.

Future milestones will add real LLM method runs, model comparisons, source-grounding evaluations, multimodal experiments, graph-building experiments, product-output experiments, and cross-lab graduation reviews.

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

Only two installable packages exist in milestone one:

* `qf_v3_protocol`
* `qf_v3_synthesis`

Labs are intentionally not installable packages yet. They are isolated research workspaces that export fixture records through the protocol.

---

## Current Phase

Current phase: `milestone-2-live-pilot-recorded`

The scaffold baseline is accepted. Milestone 2 now has one admitted tiny live LLM pilot export set recorded under `labs/long_context_judgment/EXPORTS/`, plus one admitted proposal-only chunked/source-grounded live pilot export set, one failure-focused manual content-review EvaluationRecord, one admitted DeepSeek V4 Pro chunked/source-grounded live pilot export set, and one DeepSeek V4 Pro manual content-review EvaluationRecord recorded under `labs/chunked_source_grounding/EXPORTS/`.

The live export set is proposal-only. It is not validation, product evidence, strategy evidence, financial advice, live-trading authority, graduation, or architecture.

Milestone one was not a limitation on V3’s ambition. It created the first safety and comparison harness.

The accepted scaffold contains:

* shared protocol schemas,
* metadata-safe benchmark packs,
* three starter lab skeletons,
* positive and negative fixture records,
* validation tools,
* read-only synthesis,
* currentness docs,
* and tests proving the scaffold boundaries.

Current live-pilot planning packets live under:

```text
labs/long_context_judgment/PLANNING/live_llm_pilot_001/
labs/chunked_source_grounding/PLANNING/live_llm_pilot_001/
labs/chunked_source_grounding/PLANNING/live_llm_pilot_002/
labs/chunked_source_grounding/PLANNING/live_llm_pilot_003/
```

The first packet includes `run_admission_update.md`, which authorized exactly one tiny live LLM pilot run under the stated scope. The first chunked-source packet defined the preflight scope for `chunked_source_grounding_live_pilot_001`, which has now produced proposal-only export records and a failure-focused manual content-review EvaluationRecord. The second chunked-source packet defined the preflight scope for `chunked_source_grounding_live_pilot_002`, which has now produced one admitted DeepSeek V4 Pro chunked/source-grounded live pilot export set under the smaller output contract and one DeepSeek V4 Pro manual content-review EvaluationRecord at `labs/chunked_source_grounding/EXPORTS/evaluation_record.live_pilot_002_manual_content_review.json`. The third chunked-source packet defines the Goal 8B source-span precision planning scope for `chunked_source_grounding_live_pilot_003`; it has not executed a model call and does not authorize execution without a separate Goal 8C instruction. Planning packets are not in `EXPORTS/`, are not imported by synthesis, and are not research evidence.

The purpose of these live pilots is to prove that real model calls can be recorded, evaluated at the boundary, compared later, and contained without turning output into truth.

See:

* `PORTFOLIO_CURRENT.md`
* `docs/llm-experimentation-model.md`
* `docs/research-lifecycle.md`
* `docs/live-llm-experiment-admission.md`

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

Expected day-one commands:

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
