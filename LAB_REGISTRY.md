# Lab Registry

Status: lab currentness router  
Current milestone: `scaffold-v0.1`

This file lists labs and their parent research questions. It does not claim that any method works.

---

## Active Scaffold Labs

### `long_context_judgment`

Path:

```text
labs/long_context_judgment/
```

Parent research question:

```text
How can long-context LLM methods extract reusable trading judgment from messy trader text?
```

Current state:

```text
scaffold fixture exports only
```

Required fixture posture:

* one positive fixture run,
* one negative fixture run,
* protocol-valid fixture artifacts,
* evaluation records,
* research note with scaffold disclaimer.

---

### `chunked_source_grounding`

Path:

```text
labs/chunked_source_grounding/
```

Parent research question:

```text
How can chunked/source-span LLM methods preserve source grounding while still supporting useful abstraction?
```

Current state:

```text
scaffold fixture exports only
```

---

### `visual_deictic_understanding`

Path:

```text
labs/visual_deictic_understanding/
```

Parent research question:

```text
How can multimodal or vision-language LLM workflows bind transcript/deictic language to visual chart context?
```

Current state:

```text
scaffold fixture exports only
```

---

## Lab Independence Rule

Labs may use different internal methods, assumptions, prompts, models, dependencies, and artifact formats in future milestones.

During scaffold, labs export only protocol fixture records.

Labs do not define protocol authority.

Labs do not graduate methods.

Labs do not define portfolio architecture.

---

## Shared Code Rule

Labs should not share lab-runtime code in milestone one.

Shared code is limited to protocol validation and read-only synthesis.

Future shared lab helper code requires:

1. repeated use across at least two labs,
2. clear evidence that duplication is harmful,
3. an ADR,
4. and no expansion of protocol authority by accident.
