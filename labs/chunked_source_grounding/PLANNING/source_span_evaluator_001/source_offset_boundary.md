# Source Offset Boundary

Status: local source-boundary planning

This plan defines metadata-safe source-span review for local ignored source files.

## Source Scope

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

Both source files are local-only raw source material. Do not commit raw source text.

## Canonical Locator

For stricter source-span review, each reviewed support hint should be mapped locally to:

```text
source_ref
line range
character offset start
character offset end
quote hash
```

The committed review may mention line range, character offset, quote hash, and source ref. It must not copy the raw source text.

## Line Range

Line ranges are human-review aids. They should use the local ignored source file line numbering after normalizing only line endings.

Line ranges should not be treated as source truth if the source file changes. The source ref and quote hash must accompany them.

## Character Offset

Character offsets are stricter than broad segment refs. They should be computed against the exact local ignored source file bytes decoded as text for review.

Offsets should be recorded as local review metadata only unless a later protocol change creates a formal field.

## Quote Hash

Quote hashes should be generated from the exact local source span text selected during review.

Recommended local format:

```text
quote_sha256:<first_16_hex_chars>
```

Quote hashes allow later local reproduction without committing raw source text.

## Local-Only Materials

The reviewer may inspect:

- ignored source files,
- ignored model traces,
- ignored prompt traces,
- ignored provider response metadata.

The committed review must not include raw source text, raw model output, raw prompt traces, provider payloads, private notes, API keys, or secrets.
