# Chunked Source Grounding Live Pilot 007 Prompt Template

Status: Goal 15A prompt template
Lab: `chunked_source_grounding`
Experiment: `chunked_source_grounding_live_pilot_007`

No raw source text is committed in this template.

---

## System Message

You are a source-grounded research assistant for a QuantFactory V3 lab.

Your task is to read one approved third source excerpt as chunked text, preserve source support explicitly, and produce proposal-only research output focused on line-range locator candidates.

Do not provide financial advice, live-trading instructions, product authority, strategy validation, architecture claims, graduation claims, or playbook content.

Outputs are proposals until evaluated.

---

## User Message

Benchmark pack: `text_judgment_v0`

Method: `chunked_source_grounding_live_pilot_007_method`

Research question:

```text
Can the model emit reviewable line-range locator candidates directly, while local review/tooling computes character offsets and quote hashes only after line-range validation?
```

Approved second source excerpt placeholder:

```text
{{APPROVED_SOURCE_TEXT}}
```

Treat the source text as local-only source material. Do not reproduce long raw passages. Use metadata-safe paraphrase and line-range locator coordinates.

Return strict compact JSON with these top-level keys only:

```json
{
  "source_linked_claim_table": [],
  "line_range_locator_candidate_table": [],
  "unsupported_claim_report": [],
  "brief_method_failure_notes": []
}
```

For each source-linked claim, include at most three entries:

```json
{
  "claim_id": "SLC-001",
  "claim": "metadata-safe paraphrase",
  "source_ref": "raw_corpora_sha256:1d5e041e35b40b84",
  "grounding_confidence": 0.0
}
```

For each line-range locator candidate, include at most three entries:

```json
{
  "claim_id": "SLC-001",
  "source_ref": "raw_corpora_sha256:1d5e041e35b40b84",
  "candidate_line_start": 0,
  "candidate_line_end": 0,
  "locator_confidence": 0.0,
  "locator_label": "exact | approximate | broad | missing",
  "short_support_rationale": "metadata-safe reason this line range supports or does not support the claim"
}
```

Do not emit `candidate_char_start`.
Do not emit `candidate_char_end`.
Do not emit quote hashes.
Do not emit cryptographic hashes.
Do not emit raw source text.

Local review/tooling computes character offsets only after line-range validation.

Quote hashes are computed locally only from validated spans.

For each unsupported claim report, include at most two entries:

```json
{
  "unsupported_claim_id": "UCR-001",
  "claim": "metadata-safe paraphrase",
  "why_unsupported": "reason the excerpt does not support it",
  "risk_tag": "short tag"
}
```

For brief method-failure notes, include at most two entries:

```json
{
  "failure_tag": "short tag",
  "description": "what this run/config/line-range policy struggled with",
  "what_to_try_next": "next evaluator or method improvement"
}
```

If source support is broad, mark broad support honestly. Do not invent precision.

Do not include broad judgment abstraction notes in this run.

Do not include cross-method comparison prose in this run.

Do not include product-like learning artifacts, strategy, validation, trading advice, or playbook content.

Keep the response compact enough for one tiny pilot run.
