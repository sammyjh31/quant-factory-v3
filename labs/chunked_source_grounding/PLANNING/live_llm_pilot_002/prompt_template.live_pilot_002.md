# Chunked Source Grounding Live Pilot 002 Prompt Template

Status: Goal 7D prompt template
Lab: `chunked_source_grounding`
Experiment: `chunked_source_grounding_live_pilot_002`

No raw source text is committed in this template.

---

## System Message

You are a source-grounded research assistant for a QuantFactory V3 lab.

Your task is to read one approved trader-education source excerpt as chunked text, preserve source support explicitly, and produce proposal-only research output.

Do not provide financial advice, live-trading instructions, product authority, strategy validation, architecture claims, or graduation claims.

Outputs are proposals until evaluated.

---

## User Message

Benchmark pack: `text_judgment_v0`

Method: `chunked_source_grounding_live_pilot_002_method`

Research question:

```text
Can a chunked/source-grounded LLM method produce a complete parseable source-grounding artifact when using DeepSeek V4 Pro and a smaller output contract, and what does it preserve or lose compared with the long-context judgment pilot?
```

Approved source text placeholder:

```text
{{APPROVED_SOURCE_TEXT}}
```

Treat the source text as local-only source material. Do not reproduce long raw passages. Use short span hints only when needed to identify support.

Return strict compact JSON with these top-level keys only:

```json
{
  "source_linked_claim_table": [],
  "segment_span_support_notes": [],
  "unsupported_claim_report": [],
  "brief_method_failure_notes": []
}
```

For each source-linked claim, include at most three entries:

```json
{
  "claim_id": "SLC-001",
  "claim": "metadata-safe paraphrase",
  "segment_id": "segment label or approximate location",
  "source_span_hint": "short support hint, not raw transcript reproduction",
  "grounding_confidence": 0.0
}
```

For each segment/span support note, include at most three entries:

```json
{
  "support_note_id": "SSN-001",
  "segment_id": "segment label or approximate location",
  "support_quality": "specific | broad | weak | missing",
  "why_it_matters": "how this affects source-grounding review"
}
```

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
  "description": "what this run/config/output contract struggled with",
  "what_to_try_next": "next evaluator or method improvement"
}
```

Do not include broad judgment abstraction notes in this run.

Do not include cross-method comparison prose in this run.

Keep the response compact enough for one tiny pilot run.
