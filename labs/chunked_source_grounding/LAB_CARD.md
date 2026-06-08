# Lab Card: chunked_source_grounding

Status: active live-pilot lab

This lab explores chunked source-span readers for messy trader educational text.

## Current Evidence State

- scaffold fixture exports exist for protocol shape only
- proposal-only live export records and manual reviews exist under `EXPORTS/`
- one bounded negative result showed that an oversized Flash output contract can truncate before content review
- narrowed Pro source-grounding runs produced complete parseable artifacts under proposal-only boundaries
- the source-span precision repeat generalized to a second-source excerpt with caveats
- strict source-span re-review records now add canonical offsets, line ranges, and quote hashes for pilots 003 and 004 without changing protocol
- the source-span locator candidate pilot has produced a proposal-only export set with model-proposed locator coordinates and locally computed quote hashes, pending strict manual locator review

current details live in protocol export records and the comparison note:

```text
labs/chunked_source_grounding/PLANNING/comparisons/live_pilot_method_comparison_001.md
```

## Current Active Research Thread

Goal 11C source-span locator candidate pilot has produced a proposal-only export set, based on the completed Goal 11A locator contract plan (the source-span locator output contract plan): whether a model call can emit canonical line-range and character-offset locator candidates directly so local review can compute quote hashes instead of reconstructing support after the fact.

The next proposed step is Goal 11D manual strict locator review. That review should judge whether the model-proposed coordinates actually point to the right source spans and whether the locally computed quote hashes support the intended claims.

The current comparison note records the second-source source-span precision repeat as proposal-only evidence. It does not validate the method, declare a winner, graduate anything, or create architecture.

The current comparison surface is:

```text
labs/chunked_source_grounding/PLANNING/comparisons/live_pilot_method_comparison_001.md
```

## Current Boundaries

- live outputs are proposal-only, not source truth
- no validation, product authority, strategy evidence, financial advice, live-trading authority, graduation, or architecture
- future live runs require live LLM admission and an explicit execution instruction
