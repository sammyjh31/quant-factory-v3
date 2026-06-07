# Source / Privacy Boundary

Status: proposed planning document

This is a proposed live LLM pilot planning record. It is not a completed run, not research evidence, and not a synthesis export.

No LLM call has been made. No output artifact has been produced. No evaluation result exists. No method success is claimed.

---

## Source Scope

The future live pilot may use one controlled messy trader text source scope associated with `text_judgment_v0`.

The committed planning packet contains metadata only. It does not include raw source text, private notes, provider payloads, prompt traces, model traces, secrets, or raw V2 corpus material.

---

## Git Boundary

Allowed in git:

* protocol-valid proposed MethodCard and ExperimentCard planning records,
* admission checklist,
* run admission update,
* metadata-safe prompt template with placeholders only,
* evaluator plan,
* source/privacy boundary,
* prompt/config recording plan,
* stop condition.

Not allowed in git:

* raw source text,
* private notes,
* provider payloads,
* raw model traces,
* prompt traces containing source text,
* secrets,
* generated synthesis summaries.

---

## Local-Only Materials

If source text is used in a future run, it must remain in a local or ignored path until a later explicit policy allows committing it.

This planning packet does not choose or store the raw source material.
