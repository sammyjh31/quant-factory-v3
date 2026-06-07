# AGENTS.md

Status: agent operating guide  
Scope: entire `quantfactory-v3-federation` workspace

This file tells coding and research agents how to work in this repo without recreating V2-style drift.

QuantFactory V3 is a federated LLM-methodology research portfolio. Its purpose is to discover how messy trader source material can become useful trading intelligence through many independent labs, shared reporting, benchmark comparison, evaluation, and eventual graduation.

V3 is not a monolithic product repo.  
V3 is not a Python-script accumulation project.  
V3 is not a place where every new idea becomes permanent architecture.  
V3 is a laboratory whose outputs must be contained, comparable, and revisable.

Evidence records, benchmark results, evaluations, and graduation decisions are how the project learns. Code is just one tool. LLM methods are first-class research instruments.

---

## 0. Agent Guide Loading Rule

Before changing files, agents must read:

1. root `AGENTS.md`;
2. every `AGENTS.md` on the path to each file they will touch;
3. every `AGENTS.md` for any sibling subtree whose boundary they affect.

Known local `AGENTS.md` overlays:

* `packages/qf_v3_protocol/AGENTS.md`
* `packages/qf_v3_synthesis/AGENTS.md`
* `labs/AGENTS.md`
* `benchmarks/AGENTS.md`
* `docs/AGENTS.md`

Examples:

* Editing `packages/qf_v3_protocol/src/...` requires root `AGENTS.md` and `packages/qf_v3_protocol/AGENTS.md`.
* Editing `docs/...` requires root `AGENTS.md` and `docs/AGENTS.md`.
* Editing synthesis behavior that reads lab exports requires root `AGENTS.md`, `packages/qf_v3_synthesis/AGENTS.md`, and `labs/AGENTS.md`.

Agents should state the applied guide set in work notes or final summaries:

```text
Agent guides consulted: AGENTS.md, docs/AGENTS.md
```

If no local overlay applies, say that root `AGENTS.md` was the only guide consulted.

---

## 1. North Star

Always preserve this north star:

```text
V3 is a federated LLM-methodology research portfolio for discovering how messy trader source material can become useful trading intelligence.
```

The long-term project may explore:

* LLM-based source reading,
* long-context judgment extraction,
* chunked/source-grounded extraction,
* visual and deictic understanding,
* formula and data requirement recovery,
* contradiction mining,
* cross-source hypothesis discovery,
* source-native strategy candidates,
* study and judgment artifacts,
* operator calibration,
* historically audited playbook candidates,
* graph-based understanding,
* product prototypes,
* and eventually V4 product surfaces.

Milestone-one scaffold constraints are phase-local. They are not permanent philosophical limits on V3.

---

## 2. Core Operating Rules

### 2.1 Labs may be weird. Exports must be boring.

Inside labs, methods may be novel, exotic, model-heavy, speculative, and experimental.

At the federation boundary, every lab must export comparable records through the protocol.

Exploration belongs inside labs. Comparability belongs at the export boundary.

### 2.2 No experiment becomes architecture directly.

```text
No new experiment becomes architecture.
It becomes records first.
Architecture changes only after repeated evidence and explicit ADR.
```

A promising method should produce records, evaluations, research notes, and maybe a graduation nomination later. It should not immediately reshape the repo.

### 2.3 Evidence ladder

Agents must keep artifact authority aligned with this ladder:

```text
fixture -> proposed run -> evaluated run -> repeated evidence -> graduation candidate -> ADR-approved architecture
```

Lower ladder stages must not borrow language from higher stages.

* A fixture proves schema shape only.
* A proposed run records an idea or output before evaluation.
* An evaluated run has evaluator records but may still be weak, negative, or non-repeatable.
* Repeated evidence can motivate a graduation nomination.
* A graduation candidate is not architecture yet.
* ADR-approved architecture is the only stage that changes shared structure or doctrine.

### 2.4 V2 is failure memory, not architecture.

Use V2 for benchmark cases, failure patterns, and lessons.

Do not import V2's packet machinery, authority style, generated-ledger habits, default process model, or code-owns-all-truth framing.

V2's LLM-proposal-to-Python-review pattern is one method family. It is not V3 doctrine.

### 2.5 Scaffold records are fixtures, not evidence.

Milestone-one records are protocol fixtures. They are not real research results.

Do not cite fixture records as proof that a method works.

### 2.6 Synthesis is read-only.

Synthesis may import, validate, index, and summarize exports.

Synthesis must not:

* mutate lab files,
* mutate benchmark files,
* mutate protocol schemas,
* mutate currentness docs,
* declare winning methods,
* graduate anything,
* or become authority.

### 2.7 Live LLM experiments require admission.

No live LLM experiment may run until it satisfies:

```text
docs/live-llm-experiment-admission.md
```

Live LLM outputs are proposals until evaluated. They are not truth, architecture, product evidence, financial advice, or strategy validation.

---

## 3. How Agents Should Think

Do not default to "write a new Python script."

Before adding code, ask:

1. What research question does this serve?
2. Is this scaffold work, a lab method, a benchmark, a protocol change, a synthesis feature, or documentation?
3. Is there an existing file that should be modified instead of adding a new one?
4. Is anything now stale and should be deleted, archived, or rewritten?
5. Does this create evidence, or only a fixture?
6. Does this preserve lab independence?
7. Does this accidentally turn one lab's method into shared architecture?
8. Does this help future LLM methodology experiments become more measurable, comparable, or useful?

If the answer is unclear, stop and clarify in the work notes before adding files.

---

## 4. Addition, Deletion, and Archival Discipline

V3 must not become an append-only repo.

Hardening / cleanup discipline:

Before adding new files, check whether an existing file, schema, test, prompt, planning pattern, or fixture should be reused, edited, generalized, deleted, or archived.

Do not create a new script, helper, doc, test, or protocol field merely because this is a new method.

Prefer:

1. reuse existing protocol records,
2. adapt existing lab planning structure,
3. update stale text directly,
4. delete or archive superseded local planning material,
5. add only the minimum new files needed for the new lab's distinct method.

If a new file is added, explain why an existing file could not own that role.

If a prior hardening choice is now wrong or too narrow, rework it instead of layering another workaround on top.

When changing direction, do not simply add a new doc below old guidance.

Prefer this order:

1. **Rewrite** stale current guidance when it is still the correct file.
2. **Delete** obsolete scaffold artifacts if they are no longer needed.
3. **Archive** historical material only when it has learning value.
4. **Add** new files only when they introduce a distinct role.

Every change that adds a new direction should ask:

```text
What old direction, file, example, fixture, or claim is now superseded?
```

If something is superseded, mark it clearly or remove it.

Avoid leaving multiple competing "current" truths in the repo.

---

## 5. Currentness Discipline

Currentness docs route status. They should not become giant ledgers.

Use:

* `README.md` for project purpose and commands.
* `PORTFOLIO_CURRENT.md` for active protocol version, active labs, active benchmark packs, and current scaffold status.
* `PROTOCOL_CURRENT.md` for protocol version and schema inventory.
* `LAB_REGISTRY.md` for lab ids, parent questions, and fixture-export status.
* `GRADUATION_LEDGER.md` for graduation status only.

Do not duplicate generated synthesis metrics into currentness docs.

Do not append stale claims below newer claims. Replace stale text or mark it superseded.

If a milestone changes, update the currentness docs directly and remove or rewrite stale milestone language.

---

## 6. LLM Intelligence Is Central

V3 exists to study LLM-centered methods.

Agents should not treat LLMs as an afterthought or reduce V3 to a static schema repository.

The scaffold exists so future LLM experiments can be:

* recorded,
* evaluated,
* compared,
* repeated,
* criticized,
* and safely synthesized.

Future lab work should actively explore LLM methods such as:

* long-context reading,
* chunked/source-grounded reading,
* multi-agent disagreement,
* example-to-principle extraction,
* contradiction mining,
* formula recovery,
* visual/deictic grounding,
* cross-source synthesis,
* LLM judging,
* human/model comparison,
* and other novel methods.

But live LLM calls must wait until the admission checklist is satisfied.

---

## 7. Protocol Changes

The protocol is intentionally tiny.

Do not add protocol fields just because one lab wants them.

A protocol change requires:

1. a clear reason,
2. evidence from fixture or live runs,
3. impact on other labs,
4. backward compatibility notes,
5. an ADR.

Lab-specific detail belongs in `payload` or `notes` until repeated evidence proves it should become protocol.

---

## 8. Lab Work Rules

Labs are independent research workspaces.

A lab may invent its own internal method, prompt style, file layout, or model strategy, as long as it exports valid protocol records.

Labs must not:

* define protocol authority,
* graduate their own methods,
* mutate synthesis outputs,
* require other labs to share their architecture,
* or create shared runtime helpers without ADR.

If a lab changes direction, update its `LAB_CARD.md` and `RESEARCH_QUESTION.md`. Archive or remove stale fixtures rather than leaving contradictory current claims.

---

## 9. Benchmarks

Benchmark packs are metadata-safe scaffolds for testing methods.

They preserve failure modes and source-reference structure.

They must not contain raw private source material, provider payloads, secrets, raw prompts, or unapproved V2 corpus material.

Every active benchmark pack must include `v2_lesson_refs`.

Benchmark metadata is not source truth. It is a test harness.

---

## 10. Generated Outputs

Generated outputs are ignored by default and non-authoritative.

Do not copy generated summaries into currentness docs.

Generated files may help humans inspect the scaffold, but they do not decide what is true.

---

## 11. Graduation

Nothing graduates during scaffold milestone one.

Future graduation is portfolio-level, not lab-level.

Graduation requires repeated evidence, evaluations, negative-result analysis, benchmark coverage, known failure modes, and explicit ADR.

Until then, methods are experiments, not architecture.

---

## 12. Financial and Trading Boundary

This repo is not a live-trading system.

Scaffold and lab artifacts must not claim to provide:

* financial advice,
* live trading instructions,
* validated trading strategies,
* execution authority,
* playbook truth,
* broker actions,
* or guaranteed edge.

Future research may study strategy hypotheses and playbook candidates, but those require explicit future milestones and evaluation boundaries.

---

## 13. What Good Work Looks Like

Good work in this repo usually does one of these:

* makes LLM experiments more measurable,
* improves benchmark quality,
* improves source/provenance clarity,
* improves export comparability,
* records a useful failure mode,
* simplifies or deletes stale structure,
* clarifies currentness,
* prevents generated outputs from becoming authority,
* makes a future live LLM experiment safer,
* or prepares evidence for eventual V4 graduation.

Bad work usually does one of these:

* adds a new script without a research question,
* adds a new doc without removing stale guidance,
* creates a second source of current truth,
* treats fixtures as evidence,
* turns one lab's method into shared architecture,
* creates live LLM outputs without admission,
* hides failures,
* or expands scope without evaluation.

---

## 14. GitHub Update Hygiene

Before ending meaningful work, agents should review repository state and consider whether the repo should be updated.

Agents should:

* run `git status -sb`;
* inspect the relevant diff before staging;
* stage only files that belong to the completed work;
* avoid committing generated outputs, secrets, raw corpora, provider payloads, model traces, prompt traces, private notes, or unrelated user changes;
* run the relevant verification commands before claiming success;
* commit coherent completed work with a plain commit message;
* consider pushing the commit to `main` when the change is intended to update the current repo state and direct-main publication is appropriate.

Agents must not treat this as permission to publish unsafe or unclear work.

If the worktree is mixed, the change is unfinished, checks cannot run, or publication intent is unclear, agents should leave the repo uncommitted or unpushed and clearly report:

* what changed;
* what remains uncommitted;
* what verification did or did not run;
* what decision is needed before commit or push.

---

## 15. Before Finishing Any Change

Before finalizing work, check:

* Did I preserve the V3 north star?
* Did I keep scaffold limits phase-local?
* Did I avoid adding stale/duplicate authority?
* Did I delete or archive superseded material?
* Did I keep lab internals separate from protocol exports?
* Did I avoid making samples look like evidence?
* Did I keep generated outputs non-authoritative?
* Did I add tests for new structure?
* Did I update currentness docs only where they actually own the claim?

If not, fix that before finishing.
