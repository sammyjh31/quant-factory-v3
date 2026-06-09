# Scaffold Milestone One Build Prompt

Status: historical build brief / implementation prompt.
Superseded by: README.md, PORTFOLIO_CURRENT.md, PROTOCOL_CURRENT.md, LAB_REGISTRY.md, GRADUATION_LEDGER.md, AGENTS.md overlays, and docs/live-llm-experiment-admission.md.
This file is not project authority. Current authority lives in README.md, PORTFOLIO_CURRENT.md, PROTOCOL_CURRENT.md, LAB_REGISTRY.md, GRADUATION_LEDGER.md, AGENTS.md overlays, and the named docs listed by README.md.

---

```text
Create the scaffold implementation for the existing workspace repo `quantfactory-v3-federation`.

This is scaffold milestone one only.

The authority/currentness docs have already been created and reviewed. Respect their directional framing. Do not rewrite them into permanent prohibition lists. If a required doc is missing a required section, update it carefully while preserving the positive V3 mission:

V3 is a federated LLM-methodology research portfolio for discovering how messy trader source material can become useful trading intelligence.

Milestone one builds the measurement and comparison harness before live LLM experiments begin.

Do not implement live LLM calls, product UI, graph infrastructure, strategy generation, backtesting, Playbook, execution, real V2 corpus migration, autonomous learning, or graduation logic.

Goal:
Build a V3 research federation scaffold for future LLM-methodology experiments. The scaffold should prove that independent labs can publish comparable, source-linked, evaluated, posture-bounded fixture records through a tiny shared protocol, and that read-only synthesis can import those records without becoming authority.

Core rules:
- Labs may be methodologically weird. Exports must be boring.
- Scaffold records are fixtures, not evidence.
- Synthesis imports and summarizes; it does not mutate, graduate, or become authority.
- No new experiment becomes architecture. It becomes records first. Architecture changes only after repeated evidence and explicit ADR.
- No live LLM experiment may run until it has passed the live LLM experiment admission checklist.
- Milestone-one constraints are phase-local scaffold posture, not permanent V3 doctrine.
- Future live LLM calls, product prototypes, graph work, strategy research, playbook research, and learning loops are legitimate future research directions after the scaffold harness exists.

Use:
- Python 3.11+
- uv workspace
- pytest
- ruff
- jsonschema
- JSON Schema Draft 2020-12

Workspace layout:
Create or preserve:

- README.md
- PORTFOLIO_CURRENT.md
- PROTOCOL_CURRENT.md
- LAB_REGISTRY.md
- GRADUATION_LEDGER.md
- pyproject.toml
- .gitignore

- docs/project-thesis.md
- docs/research-lifecycle.md
- docs/llm-experimentation-model.md
- docs/live-llm-experiment-admission.md
- docs/v2-benchmark-memory.md
- docs/future-blockers-and-mitigations.md
- docs/experiment-question-template.md
- docs/build-prompts/scaffold-milestone-one.md

- packages/qf_v3_protocol/
- packages/qf_v3_synthesis/

- benchmarks/active/
- benchmarks/future_candidates/

- labs/

- generated/README.md

- tests/

Installable packages:
Only create installable packages for:

- packages/qf_v3_protocol
- packages/qf_v3_synthesis

Do not make labs installable packages.
Do not create shared lab-runtime code.
Do not create a root examples/ directory.

Use:

- packages/qf_v3_protocol/examples/valid/ for valid protocol examples.
- packages/qf_v3_protocol/examples/invalid/ for invalid protocol examples.
- labs/<lab>/EXPORTS/ for lab fixture records.

Protocol v0.1:
Hand-author JSON Schema Draft 2020-12 schemas for exactly these protocol objects:

- BenchmarkPack
- SourceRef
- MethodCard
- ExperimentCard
- RunRecord
- ArtifactEnvelope
- EvaluationRecord
- ResearchNote

Do not add protocol schemas for:

- LearningEvent
- GraduationCandidate
- GraphNode
- ProductSurface
- LiveExperimentAdmission
- LLMTrace
- PromptRecord
- ModelCall
- BacktestRecord
- StrategyRecord
- PlaybookRecord

Every exported protocol record must include:

- protocol_version: qf-v3-protocol-0.1
- schema_name
- schema_version: 0.1.0

Schemas should be strict by default:

- forbid unknown top-level fields
- forbid unknown required object fields
- use additionalProperties: false where practical
- allow lab-specific content only inside explicit payload or notes fields

JSON Schema files should live under:

packages/qf_v3_protocol/src/qf_v3_protocol/schemas/

Protocol examples should live under:

packages/qf_v3_protocol/examples/valid/
packages/qf_v3_protocol/examples/invalid/

Protocol validation:
Implement qf_v3_protocol as boring tooling only.

It should provide:

- schema loading
- record validation
- helpful validation errors
- a CLI entrypoint, preferably `qf-v3-validate`
- no live LLM calls
- no product logic
- no lab-specific runtime logic

Canonical protocol authority:
The hand-authored JSON Schema files are canonical.
Python validators are tooling.
Docs explain the protocol.
Examples are fixtures.
No Python model should supersede the schemas.

Protocol object minimums:

1. BenchmarkPack

Required fields:

- protocol_version
- schema_name
- schema_version
- benchmark_pack

benchmark_pack must include:

- benchmark_id
- title
- purpose
- source_refs
- known_difficulty
- known_failure_modes
- v2_lesson_refs
- suggested_evaluators
- metadata_safety
- notes

metadata_safety must include:

- raw_source_material_included
- private_or_provider_payload_included
- synthetic_or_placeholder_only

Every active benchmark pack must include at least one v2_lesson_ref.

Benchmark metadata must not contain raw source text, private notes, provider payloads, prompts, secrets, model traces, or raw V2 corpus material.

2. SourceRef

Required fields:

- protocol_version
- schema_name
- schema_version
- source_ref

source_ref must include:

- source_id
- source_type
- source_version_hash
- segment_refs
- metadata_safety

Each segment_ref must include:

- segment_id
- span_type
- start
- end
- quote_hash

SourceRef does not mean the source is true. It only records source identity and lineage metadata.

3. MethodCard

Required fields:

- protocol_version
- schema_name
- schema_version
- method_card

method_card must include:

- method_id
- lab_id
- parent_question
- method_family
- intended_inputs
- intended_outputs
- known_risks
- non_goals

MethodCard must not claim that a method is canonical, graduated, validated, product-ready, or architecture.

4. ExperimentCard

Required fields:

- protocol_version
- schema_name
- schema_version
- experiment_card

experiment_card must include:

- experiment_id
- lab_id
- research_question
- hypothesis
- benchmark_pack_ids
- method_ids
- evaluation_plan
- expected_artifact_types

ExperimentCard should state the methodological question being tested, not a product claim.

5. RunRecord

Required fields:

- protocol_version
- schema_name
- schema_version
- run_record

run_record must include:

- run_id
- lab_id
- experiment_id
- method_id
- benchmark_pack_id
- source_refs
- artifact_ids
- evaluation_ids
- run_kind
- outcome_polarity
- status

Allowed outcome_polarity values in scaffold:

- positive_fixture
- negative_fixture

Do not call fixture records real research runs.

6. ArtifactEnvelope

Required fields:

- protocol_version
- schema_name
- schema_version
- artifact

artifact must include:

- artifact_id
- artifact_type
- lab_id
- method_id
- run_id
- source_refs
- posture
- blockers
- summary
- payload

posture must use exactly these final facet names:

- grounding_status
- review_status
- readiness_status
- validation_status
- lifecycle_status

Allowed grounding_status:

- none
- source_linked
- source_grounded
- disputed

Allowed review_status:

- unreviewed
- self_checked
- model_judged
- human_reviewed
- rejected

Allowed readiness_status:

- unknown
- study_candidate
- research_candidate
- formalization_candidate

Allowed validation_status:

- none
- benchmark_eval

Allowed lifecycle_status:

- active
- blocked
- superseded
- retired

Do not use old posture names such as:

- source_grounding
- review_state
- product_fitness
- validation_scope
- retirement_state

Do not use statuses such as:

- validated
- historically_audited
- production_ready
- strategy_ready
- playbook_ready

7. EvaluationRecord

Required fields:

- protocol_version
- schema_name
- schema_version
- evaluation

evaluation must include:

- evaluation_id
- lab_id
- target_id
- target_type
- evaluator_id
- evaluator_type
- benchmark_pack_id
- score
- pass_fail
- failure_tags
- comments

Allowed evaluator_type values in scaffold:

- fixture_assertion
- schema_check
- human_placeholder
- llm_judge_placeholder

If evaluator_type is llm_judge_placeholder, require:

placeholder_disclaimer: "No live LLM judge was called. This is a scaffold fixture only."

No actual LLM judge calls are allowed in scaffold.

8. ResearchNote

Required fields:

- protocol_version
- schema_name
- schema_version
- research_note

research_note must include:

- note_id
- lab_id
- experiment_ids
- benchmark_pack_ids
- summary
- what_worked
- what_failed
- negative_results
- reusable_by_other_labs
- do_not_repeat
- scaffold_disclaimer

scaffold_disclaimer must include this exact sentence:

"This is a scaffold fixture for protocol validation, not real research evidence."

Benchmark packs:
Create exactly three active metadata-safe benchmark pack manifests under benchmarks/active/:

- text_judgment_v0
- source_grounding_v0
- visual_deictic_v0

Create future-candidate notes, not active packs, under benchmarks/future_candidates/ for:

- formula_missing_v0
- judgment_artifact_seed_v0

Future candidate packs must not be treated as active benchmark packs.

Each active benchmark pack must include:

- benchmark_id
- title
- purpose
- source_refs
- known_difficulty
- known_failure_modes
- v2_lesson_refs
- suggested_evaluators
- metadata_safety
- notes

Every active benchmark pack must have at least one v2_lesson_ref.

Suggested v2_lesson_refs examples:

- weak_source_grounding
- report_only_confusion
- visual_deictic_blocker
- weak_temporal_alignment
- formula_missing_blocker
- generated_artifact_drift
- authority_drift

Active benchmark packs must be metadata-safe:
They must not include raw source text, private notes, provider payloads, prompts, secrets, model traces, or raw V2 corpus material.

Labs:
Create exactly three scaffold labs:

- labs/long_context_judgment
- labs/chunked_source_grounding
- labs/visual_deictic_understanding

Each lab must include:

- README.md
- LAB_CARD.md
- RESEARCH_QUESTION.md
- METHOD_CARDS/
- EXPERIMENTS/
- RUNS/
- ARTIFACTS/
- EVALS/
- EXPORTS/

Each lab must export fixture records, not real research evidence:

- one MethodCard
- one ExperimentCard
- one positive fixture RunRecord
- one negative fixture RunRecord
- one positive fixture ArtifactEnvelope
- one negative fixture ArtifactEnvelope
- EvaluationRecords covering fixture artifacts/runs
- one ResearchNote with what worked, what failed, reusable lessons, do-not-repeat notes, and the scaffold disclaimer

Use outcome_polarity:

- positive_fixture
- negative_fixture

Every lab should make clear in README.md and fixture ResearchNote that the records are scaffold fixtures for protocol validation, not real research evidence.

Starter lab purposes:

1. labs/long_context_judgment

Parent research question:
How can long-context LLM methods extract reusable trading judgment from messy trader text?

Positive fixture:
A long-context method preserves teacher intent and produces a useful study candidate.

Negative fixture:
A long-context method over-abstracts and weakens exact source grounding.

2. labs/chunked_source_grounding

Parent research question:
How can chunked/source-span LLM methods preserve source grounding while still supporting useful abstraction?

Positive fixture:
A chunked method produces a stronger source-linked claim table.

Negative fixture:
A chunked method preserves citation but loses broader trading judgment.

3. labs/visual_deictic_understanding

Parent research question:
How can multimodal or vision-language LLM workflows bind transcript/deictic language to visual chart context?

Positive fixture:
A method binds a deictic phrase to a frame/segment placeholder.

Negative fixture:
A method hallucinates or misaligns a chart object reference.

Synthesis:
Implement qf_v3_synthesis as a read-only importer.

It should:

- discover lab EXPORTS
- validate records with qf_v3_protocol
- index by lab, benchmark, method, outcome_polarity, status
- write generated summaries only under generated/
- optionally print a concise summary to stdout
- never mutate labs, benchmarks, protocol schemas, currentness docs, registry docs, or lab records
- never declare graduation or winning methods
- never describe fixture records as real research evidence

Synthesis generated outputs:
Commit generated/README.md only.
Ignore generated/*.json and generated/*.md by default, except generated/README.md.
generated/README.md must state that generated synthesis outputs are reproducible, ignored by default, and non-authoritative.

Suggested generated outputs:

- generated/synthesis_summary.json
- generated/synthesis_summary.md

These files should be ignored by default.

Currentness and authority docs:
Preserve or create the authority docs with positive V3 mission framing.

README.md owns:

- repo purpose
- scaffold scope
- commands
- non-goals as milestone-one phase-local constraints
- where to read currentness docs
- statement that V3 is a federated LLM-methodology research portfolio

PORTFOLIO_CURRENT.md owns:

- active protocol version
- active labs
- active benchmark packs
- scaffold status
- statement that no real research evidence exists yet

PROTOCOL_CURRENT.md owns:

- protocol version
- schema inventory
- schema authority statement
- compatibility rules

LAB_REGISTRY.md owns:

- lab ids
- parent questions
- active/inactive status
- fixture-export status only

GRADUATION_LEDGER.md owns:

- graduation status

During scaffold it must state:

No methods, schemas, labs, artifacts, product surfaces, or claims have graduated.

Docs:
Ensure these docs exist and preserve the positive V3 direction:

- docs/project-thesis.md
- docs/research-lifecycle.md
- docs/llm-experimentation-model.md
- docs/live-llm-experiment-admission.md
- docs/v2-benchmark-memory.md
- docs/future-blockers-and-mitigations.md
- docs/experiment-question-template.md

docs/project-thesis.md must explain:

- V3 is a federated LLM-methodology research portfolio.
- V3 explores how messy trader source material can become useful trading intelligence.
- V3 is not one fixed pipeline.
- V3 supports methodological pluralism.
- Products are downstream possibilities, not starting assumptions.
- V4 inherits only what V3 proves useful.

docs/research-lifecycle.md must define the intended progression:

- Scaffold
- Tiny live LLM pilot
- Method comparison
- Evaluator comparison
- Cross-pack repeat
- Cross-lab synthesis
- Graduation review

docs/llm-experimentation-model.md must explain:

- V3’s primary purpose is methodological LLM experimentation.
- Scaffold phase does not run live LLMs.
- Future LLM runs must record model id, prompt/template hash, parameters, source scope, artifacts, evaluator ids, failures, and research notes.
- LLM outputs are proposals until evaluated.
- No hidden “the system learned” claims.
- Negative LLM results are first-class.
- Scaffold fixture records are not research evidence.

docs/live-llm-experiment-admission.md must define the checklist required before any future live LLM experiment can run.

It must require:

- active benchmark pack
- MethodCard
- ExperimentCard
- evaluator plan
- source/privacy boundary
- prompt/template hash plan
- model/config recording plan
- output artifact types
- negative-result value
- stop condition
- budget/secrets handling
- proposal-only statement

Until a formal LiveExperimentAdmission schema exists, each future live experiment must include an admission checklist document beside its ExperimentCard.

docs/v2-benchmark-memory.md must explain:

- V2 is benchmark memory and failure memory, not architecture.
- V2 may contribute failure cases and benchmark lessons.
- V2 does not contribute canonical architecture, packet machinery, currentness machinery, product doctrine, shared lab runtime, default ingestion model, default extraction model, or universal LLM-to-Python law.

docs/future-blockers-and-mitigations.md must cover:

- fixture theater
- evaluator weakness
- schema churn
- benchmark packs too thin
- generated synthesis becoming truth
- shared helper creep
- experiment sprawl

docs/experiment-question-template.md must require future experiments to state:

- research question
- hypothesis
- competing methods
- benchmark pack
- expected artifacts
- evaluators
- negative result value
- stop condition
- graduation implication

Documentation stance:
Write README.md and docs as positive directional authority, not permanent prohibition lists.

They should say V3 is a federated LLM-methodology research portfolio designed to discover how messy trader source material can become useful trading intelligence.

They should say milestone one is only the scaffold harness for future live LLM experiments.

They should not imply that V3 is permanently avoiding live LLM calls, product prototypes, graphs, strategy research, playbook research, or learning loops.

Those are future research directions. They are simply not part of scaffold milestone one.

ADR:
Do not build a full ADR system yet unless trivial.
If adding an ADR stub, create docs/adr/README.md only.
No architecture decisions beyond scaffold setup should be recorded as graduated decisions.

Tooling:
Use uv workspace with Python 3.11+.

Root pyproject.toml should include:

- workspace members for packages/qf_v3_protocol and packages/qf_v3_synthesis
- dev dependencies for pytest, ruff, jsonschema, PyYAML if YAML fixture loading is used
- console scripts:
  - qf-v3-validate
  - qf-v3-synthesis

Keep tooling boring and replaceable.

Day-one commands:

- uv run pytest
- uv run ruff check .
- uv run qf-v3-validate
- uv run qf-v3-synthesis

Security and privacy:
.gitignore should exclude:

- generated/*.json
- generated/*.md
- raw source corpora
- private notes
- provider payloads
- model traces
- prompt traces containing source text
- secrets
- .env files
- caches
- virtual environments

Commit generated/README.md only.

Do not commit secrets, API keys, raw V2 source material, private notes, provider payloads, raw model traces, or prompts containing private/raw source material.

Tests:
Add tests proving:

- protocol valid examples validate
- invalid examples fail
- protocol examples live only under packages/qf_v3_protocol/examples/
- no root examples/ directory exists
- active benchmark packs validate
- exactly three active benchmark packs exist
- future candidate packs are not active
- each active benchmark pack has v2_lesson_refs
- each active benchmark pack is metadata-safe
- all lab EXPORTS validate
- each lab has at least one positive fixture and one negative fixture
- every ArtifactEnvelope uses the final posture facet names
- no old posture facet names appear
- every RunRecord links method, experiment, benchmark, source refs, artifact ids, and evaluation ids
- ResearchNotes include scaffold fixture disclaimers
- llm_judge_placeholder records require placeholder_disclaimer
- synthesis imports all valid exports
- synthesis writes only under generated/
- synthesis is read-only outside generated/
- generated summaries are ignored by default
- GRADUATION_LEDGER.md has no graduated entries
- docs/live-llm-experiment-admission.md exists and contains all required checklist headings
- README.md and docs/research-lifecycle.md include the architecture rule:
  "No new experiment becomes architecture. It becomes records first. Architecture changes only after repeated evidence and explicit ADR."
- README.md and docs/llm-experimentation-model.md make clear that V3’s future includes live LLM methodology experiments after scaffold
- currentness docs do not claim fixture records are real research evidence
- PORTFOLIO_CURRENT.md does not duplicate generated synthesis metrics

Non-goals for scaffold milestone one:
Do not implement live LLM calls.
Do not implement product UI.
Do not build graph infrastructure.
Do not build strategy generation, backtesting, Playbook, execution, or validated trading claims.
Do not migrate V2 architecture.
Do not treat V2 as protocol authority.
Do not make labs installable packages.
Do not create shared lab-runtime helpers.
Do not graduate anything.
Use V2 only as metadata-safe benchmark/failure-memory inspiration.

Definition of done:
- uv run pytest passes
- uv run ruff check . passes
- uv run qf-v3-validate succeeds
- uv run qf-v3-synthesis succeeds
- all validation fixtures behave as expected
- all three labs export positive and negative fixture records
- synthesis imports them read-only
- generated summaries are ignored by default
- active benchmark packs preserve V2 lesson refs without raw/private/provider material
- currentness docs clearly state that scaffold records are fixtures rather than real research evidence
- docs preserve V3’s positive long-term mission as a federated LLM-methodology research portfolio
- GRADUATION_LEDGER.md remains empty/stubbed
```
