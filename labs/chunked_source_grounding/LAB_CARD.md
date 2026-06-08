# Lab Card: chunked_source_grounding

Status: active live-pilot lab

This lab explores chunked source-span readers for messy trader educational text.

## Current Evidence State

- scaffold fixture exports exist for protocol shape only
- proposal-only live export records and manual reviews exist under `EXPORTS/`
- one bounded negative result showed that an oversized Flash output contract can truncate before content review
- narrowed Pro source-grounding runs produced complete parseable artifacts under proposal-only boundaries
- the source-span precision repeat generalized to a second-source excerpt with caveats
- source-span evaluator planning now targets canonical offsets, line ranges, and quote hashes before another model call

current details live in protocol export records and the comparison note:

```text
labs/chunked_source_grounding/PLANNING/comparisons/live_pilot_method_comparison_001.md
```

## Current Active Research Thread

The active thread is source-span evaluator planning: whether stricter manual review can replace broad segment refs with canonical offsets, line ranges, and quote hashes for existing source-span precision pilots.

The current comparison note records the second-source source-span precision repeat as proposal-only evidence. It does not validate the method, declare a winner, graduate anything, or create architecture.

The current evaluator plan is:

```text
labs/chunked_source_grounding/PLANNING/source_span_evaluator_001/
```

## Current Boundaries

- live outputs are proposal-only, not source truth
- no validation, product authority, strategy evidence, financial advice, live-trading authority, graduation, or architecture
- future live runs require live LLM admission and an explicit execution instruction
