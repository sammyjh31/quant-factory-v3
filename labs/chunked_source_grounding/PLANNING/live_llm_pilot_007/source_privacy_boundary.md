# Chunked Source Grounding Live Pilot 007 Source Privacy Boundary

Status: Goal 15A planning/admission record

This pilot must use the operator-authorized third source excerpt selected under the milestone-4 directive.

Canonical source ref:

```text
raw_corpora_sha256:1d5e041e35b40b84
```

Full selected excerpt SHA-256: `1d5e041e35b40b84526e1353277667c21f9b5a822fc2d8bc47b22a91b5c1ea31`

Selected excerpt word count: `950`

Selected excerpt line count: `106`

Selected local operator path:

```text
raw_corpora/selected/third_source_line_range_001/source.txt
```

Recorded local source origin:

```text
raw_corpora/trader_source_corpus/transcripts/trading-strategy-part-2-tuesday-9th-december-2025-9-30pm-utc.txt
```

Recorded selection procedure: a 950-word teaching segment (volatility-regime assessment, environment definition, tool selection) was taken from the origin transcript at a recorded word offset (words 1900-2850 of the whitespace-split origin), wrapped locally at 50 characters via Python `textwrap.wrap` to create line structure (the origin file is a single unwrapped line), and hashed. Line ranges in this pilot refer to the wrapped excerpt.

The selected local path is the only approved source scope for Goal 15B.

Do not fall back to the full corpus path. Do not commit raw source text, private notes, raw prompts containing source text, model traces, reasoning traces, provider payloads, account identifiers, or secrets.

Committed records may include only metadata-safe identifiers, refs, hashes, counts, line ranges, locator labels and confidence, offsets and quote hashes computed locally after line-range validation, and proposal-only summaries.

No source material becomes product authority, strategy evidence, financial advice, live-trading authority, graduation, or architecture.
