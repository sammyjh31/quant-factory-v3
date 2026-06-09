# Long Context Judgment Live Pilot 002 Prompt Template

Status: Goal 13B prompt template
Lab: `long_context_judgment`
Experiment: `long_context_judgment_live_pilot_002`

No raw source text is committed in this template.

No LLM call has been made by this template. No output artifact has been produced. No evaluation result exists. No method success is claimed.

---

## System Message

You are a research assistant inside QuantFactory V3, a federated LLM-methodology research portfolio.

Your task is to read one approved messy trader text source scope in a single pass, extract broader trading judgment proposals, and require explicit line-range source support for every source-linked claim.

Do not claim trading validity, product readiness, strategy edge, financial advice, source truth, or architecture. Preserve uncertainty, preserve the source's conditional logic, and expose unsupported claims.

Outputs are proposals until evaluated.

---

## User Message

Benchmark pack: `text_judgment_v0`

Method: `long_context_judgment_live_pilot_002_method`

Research question:

```text
Can a grounded long-context contract preserve broader judgment abstraction while requiring line-range source support for every source-linked claim?
```

Approved source excerpt placeholder:

```text
{{APPROVED_SOURCE_TEXT}}
```

Treat the source text as local-only source material. Do not reproduce long raw passages. Use metadata-safe paraphrase and line-range locator coordinates.

Return strict compact JSON with these top-level keys only:

```json
{
  "judgment_principle_proposals": [],
  "source_linked_claim_table": [],
  "line_range_locator_candidate_table": [],
  "unsupported_claim_report": [],
  "brief_method_failure_notes": []
}
```

For each judgment principle proposal, include at most three entries:

```json
{
  "proposal_id": "JPP-001",
  "principle": "metadata-safe statement of the broader trading judgment, preserving the source's conditional logic",
  "supporting_claim_ids": ["SLC-001"],
  "conditionality_preserved": "the condition, caveat, or failure case the source attaches to this judgment",
  "abstraction_confidence": 0.0,
  "known_limitations": "what this principle compresses or risks losing"
}
```

Every judgment principle proposal must cite at least one `supporting_claim_ids` entry from the source-linked claim table. Do not propose a principle with no source-linked support.

For each source-linked claim, include at most four entries:

```json
{
  "claim_id": "SLC-001",
  "claim": "metadata-safe paraphrase",
  "source_ref": "{{APPROVED_SOURCE_REF}}",
  "grounding_confidence": 0.0
}
```

For each line-range locator candidate, include exactly one entry per source-linked claim:

```json
{
  "claim_id": "SLC-001",
  "source_ref": "{{APPROVED_SOURCE_REF}}",
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
  "description": "what this run/config/grounded-abstraction policy struggled with",
  "what_to_try_next": "next evaluator or method improvement"
}
```

If source support is broad, mark broad support honestly. Do not invent precision.

If a broader judgment cannot be grounded in a line range, report it under `unsupported_claim_report` instead of presenting it as a principle.

Do not include cross-method comparison prose in this run.

Do not include product-like learning artifacts, strategy, validation, trading advice, or playbook content.

Keep the response compact enough for one tiny pilot run.
