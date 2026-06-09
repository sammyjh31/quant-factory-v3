# Long Context Judgment Live Pilot 003 Source Privacy Boundary

Status: Goal 14A planning/admission record

Identical boundary to `labs/long_context_judgment/PLANNING/live_llm_pilot_002/source_privacy_boundary.md`, restated minimally so this packet stands alone:

* Approved source scope: the same operator-approved second-source excerpt from the local pharm box-trades transcript used by pilots 002 and chunked 004-006.
* Canonical source ref: `raw_corpora_sha256:9f9e143429f5842a`; full excerpt SHA-256 `9f9e143429f5842a9c03c95b1f7705d85fb664cf795c30919a582fa66b16fbb5`; word count `945`; 140 lines.
* Selected local operator path: `raw_corpora/selected/source_span_precision_repeat_001/source.txt` (origin: `raw_corpora/trader_source_corpus/pharm/box trades_999923657.txt`).
* Do not fall back to the full corpus path. Do not commit raw source text, private notes, raw prompts containing source text, model traces, provider payloads, account identifiers, or secrets.
* Committed records may include only metadata-safe identifiers, refs, hashes, counts, line ranges, locator labels and confidence, offsets and quote hashes computed locally after line-range validation, and proposal-only summaries.

No source material becomes product authority, strategy evidence, financial advice, live-trading authority, graduation, or architecture.
