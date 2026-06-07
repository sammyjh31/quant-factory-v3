# Protocol Current

Status: protocol currentness router  
Current protocol version: `qf-v3-protocol-0.1`
Current schema version: `0.1.1`

This file owns the current protocol version and schema inventory. It does not own lab results or method conclusions.

---

## Protocol Purpose

The protocol exists so independent research labs can report comparable records without sharing architecture.

The protocol defines what labs must export, not how labs must think.

---

## Protocol v0.1 Schemas

Protocol v0.1 includes:

1. `BenchmarkPack`
2. `SourceRef`
3. `MethodCard`
4. `ExperimentCard`
5. `RunRecord`
6. `ArtifactEnvelope`
7. `EvaluationRecord`
8. `ResearchNote`

No other schema is part of protocol v0.1.

Schema 0.1.1 adds proposal-only live pilot record support to existing record schemas. It does not add new protocol object types.

---

## Required Version Fields

Every protocol record must include:

```yaml
protocol_version: qf-v3-protocol-0.1
schema_name: ...
schema_version: 0.1.1
```

---

## Canonical Protocol Authority

The canonical protocol authority is the hand-authored JSON Schema Draft 2020-12 files under:

```text
packages/qf_v3_protocol/src/qf_v3_protocol/schemas/
```

Python validators are tooling. They do not supersede the schemas.

Examples are fixtures. They do not supersede the schemas.

Docs explain the protocol. They do not supersede the schemas.

---

## Strictness

Protocol schemas are strict by default.

Unknown top-level fields are forbidden.

Lab-specific content belongs only inside explicitly flexible fields such as `payload`, `notes`, or future extension fields.

This protects the protocol from silently becoming architecture.

---

## Protocol Change Rule

Protocol changes require an ADR.

A lab may propose protocol changes, but no single lab owns protocol authority.

Protocol fields should be added only after repeated evidence from fixture or live experiments shows they are needed.

ADR 0001 records the schema `0.1.1` readiness patch that lets existing records represent a proposal-only live LLM pilot without relabeling it as a scaffold fixture.

---

## Scaffold Limitation

Protocol v0.1 is intentionally small.

It does not include:

* live LLM trace schemas,
* prompt record schemas,
* model call schemas,
* graph schemas,
* product schemas,
* strategy schemas,
* graduation schemas,
* autonomous learning schemas.

These may be added later only after evidence and ADR.
