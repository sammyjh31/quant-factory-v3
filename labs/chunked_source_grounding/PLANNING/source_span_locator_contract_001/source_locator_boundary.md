# Source Locator Boundary

Status: planning only

This file defines the metadata-safe boundary for future locator-candidate artifacts.

## Source Scope

The first future locator-candidate pilot should reuse the same approved source scope unless a separate admission update changes it.

Pilot 003 source:

```text
source_ref: raw_corpora_sha256:d8392c58c3b740eb
local source path: raw_corpora/selected/live_llm_pilot_001/source.txt
```

Pilot 004 source:

```text
source_ref: raw_corpora_sha256:9f9e143429f5842a
local source path: raw_corpora/selected/source_span_precision_repeat_001/source.txt
```

These source files are local-only. The source text stays ignored/local, and no raw source text is committed.

## Metadata-Safe Locator Candidates

Committed future records may include metadata-safe locator candidates:

- source ref,
- line start and line end,
- character offset start and character offset end,
- locally computed quote hash,
- locator label,
- locator confidence.

Committed future records must not include raw source text, raw model traces, raw prompt traces, provider payloads, private notes, API keys, or secrets.

## Quote Hash Boundary

The model should not emit quote hashes.

Quote hashes should be computed locally after the model response from the exact local source span selected by the candidate offsets.

A computed quote hash is not source truth by itself. It is a reproducibility handle for local review.

If line ranges, offsets, and locally computed quote hash disagree, the future review should mark the locator candidate as approximate, broad, missing, or failed according to the review evidence.
