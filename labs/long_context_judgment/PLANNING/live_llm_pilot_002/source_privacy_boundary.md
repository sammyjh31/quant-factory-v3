# Long Context Judgment Live Pilot 002 Source Privacy Boundary

Status: Goal 13B planning/admission record

This pilot must use the same selected second-source excerpt as chunked_source_grounding pilots 004, 005, and 006: the operator-approved excerpt selected from the local pharm box-trades transcript. Reusing this excerpt is deliberate: it makes locator quality directly comparable across the chunked and grounded long-context method families.

Canonical source ref:

```text
raw_corpora_sha256:9f9e143429f5842a
```

Full selected excerpt SHA-256: `9f9e143429f5842a9c03c95b1f7705d85fb664cf795c30919a582fa66b16fbb5`

Selected excerpt word count: `945`

Selected local operator path:

```text
raw_corpora/selected/source_span_precision_repeat_001/source.txt
```

Recorded local source origin:

```text
raw_corpora/trader_source_corpus/pharm/box trades_999923657.txt
```

The selected local path is the only approved source scope for Goal 13C if execution is separately authorized.

A larger-source repeat that actually stresses the long-context window is a future fork and requires its own admission packet; this pilot tests the grounded contract, not context length.

Do not fall back to the full corpus path.

Do not commit raw source text.

Do not commit private notes, raw prompts containing source text, model traces, provider payloads, account identifiers, or secrets.

Committed records may include only metadata-safe identifiers, source refs, hashes, counts, line ranges, locator labels, locator confidence, computed character offset ranges after validation, computed quote hashes after validation, and proposal-only summaries.

Character offsets are computed locally only after line-range validation.

Quote hashes are computed locally only from validated spans.

Computed hashes are local metadata, not model output.

No source material becomes product authority, strategy evidence, financial advice, live-trading authority, graduation, or architecture.
