# Lab Registry

Status: lab currentness router  
Current phase: `milestone-3-method-comparison-recorded`

This file lists labs, parent research questions, and phase-appropriate export status. It does not claim that any method works.

---

## Active Federation Labs

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
active live-pilot lab with scaffold fixtures, proposal-only live export records, and manual review records
```

Details live in the lab's `EXPORTS/` and `PLANNING/` directories.

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
active live-pilot lab with scaffold fixtures, proposal-only live export records, manual review records, one second-source source-span precision repeat, and one strict locator review showing useful line ranges but inaccurate char offsets; Goal 12B live-run admission planning is complete and the next proposed step is Goal 12C execution of the admitted line-range-first locator pilot
```

Current details live in protocol export records and the lab-local comparison note:

```text
labs/chunked_source_grounding/PLANNING/comparisons/live_pilot_method_comparison_001.md
```

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

Labs export protocol-valid records appropriate to their current phase. Scaffold fixtures, proposal-only live runs, manual reviews, and future experiment records must remain clearly labeled and must not claim protocol authority, graduation, validation, product evidence, strategy evidence, financial advice, live-trading authority, or architecture.

Labs do not define protocol authority.

Labs do not graduate methods.

Labs do not define portfolio architecture.

---

## Shared Code Rule

Labs should not share lab-runtime code in milestone one.

Shared code is limited to protocol validation and read-only synthesis.

Future shared lab helper code requires:

* repeated need across labs,
* evidence that duplication is harming comparison,
* a minimal shared abstraction,
* and explicit architecture approval.
