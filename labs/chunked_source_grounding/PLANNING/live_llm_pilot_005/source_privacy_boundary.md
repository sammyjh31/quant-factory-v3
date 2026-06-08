# Chunked Source Grounding Live Pilot 005 Source Privacy Boundary

Status: Goal 11B planning/admission record

This pilot must use the same approved source as `chunked_source_grounding_live_pilot_004`: the operator-approved second-source excerpt selected from the local pharm box-trades transcript.

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

The selected local path is the only approved source scope for Goal 11C if execution is separately authorized.

Do not fall back to the full corpus path.

Do not commit raw source text.

Do not commit private notes, raw prompts containing source text, model traces, provider payloads, account identifiers, or secrets.

Committed records may include only metadata-safe identifiers, source refs, hashes, counts, line ranges, character offset ranges, computed quote hashes, locator labels, locator confidence, and proposal-only summaries.

Quote hashes are computed locally after the model response from the exact selected local source spans. The model should emit locator coordinates, not cryptographic hashes.

No source material becomes product authority, strategy evidence, financial advice, live-trading authority, graduation, or architecture.
