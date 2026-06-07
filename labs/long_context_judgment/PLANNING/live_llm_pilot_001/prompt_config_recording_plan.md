# Prompt / Config Recording Plan

Status: proposed planning document

This is a proposed live LLM pilot planning record. It is not a completed run, not research evidence, and not a synthesis export.

No LLM call has been made. No output artifact has been produced. No evaluation result exists. No method success is claimed.

---

## Prompt / Template Hash Plan

Before any live call, the run admission update must record:

* prompt/template file path or construction method,
* prompt/template hash,
* system prompt hash,
* tool instruction hash if tools are used,
* confirmation that committed prompt text contains no private/raw source material and no secrets.

Prompt text containing raw source material must remain local-only or ignored.

---

## Model / Config Recording Plan

No provider or model is selected in this planning packet.

Before any live call, the run admission update must record:

* provider id,
* model id,
* sampling settings,
* context/token settings,
* tool routing,
* config hash,
* required environment variable names without values.

Config records must not include secrets.

---

## Trace Boundary

Raw model traces and provider payloads must not be committed unless a later explicit policy allows them.

Any future trace storage location must be named in the admission update before execution.
