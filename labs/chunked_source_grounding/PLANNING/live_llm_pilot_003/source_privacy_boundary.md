# Chunked Source Grounding Live Pilot 003 Source Privacy Boundary

Status: Goal 8B planning/admission record

This pilot must use the same approved excerpt as `long_context_judgment_live_pilot_001` and the same approved excerpt/hash as `chunked_source_grounding_live_pilot_002`.

Canonical source ref:

```text
raw_corpora_sha256:d8392c58c3b740eb
```

Preferred local operator path:

```text
raw_corpora/selected/live_llm_pilot_001/source.txt
```

Recorded first-pilot source path scope:

```text
raw_corpora/trader_source_corpus/transcripts/how-to-use-market-profile-start-now-trading-tutorials.txt
```

Goal 8C must stop before calling a model unless the source excerpt resolves to the same approved source identity used by `long_context_judgment_live_pilot_001`, `chunked_source_grounding_live_pilot_001`, and `chunked_source_grounding_live_pilot_002`.

Do not commit raw source text.

Do not commit private notes, raw prompts containing source text, model traces, provider payloads, account identifiers, or secrets.

Committed records may include only metadata-safe identifiers, source refs, hashes, counts, short span hints, support hint quality labels, and proposal-only summaries.

No source material becomes product authority, strategy evidence, financial advice, live-trading authority, graduation, or architecture.
