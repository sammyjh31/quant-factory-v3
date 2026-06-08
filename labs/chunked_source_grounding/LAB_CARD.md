# Lab Card: chunked_source_grounding

Status: active live-pilot lab

This lab explores chunked source-span readers for messy trader educational text.

Current records:

- scaffold fixture exports for protocol shape only
- `chunked_source_grounding_live_pilot_001`: proposal-only DeepSeek V4 Flash live pilot on `text_judgment_v0`
- Flash pilot 001 records a bounded negative result: truncated output, incomplete JSON, and output contract too large
- manual boundary review passed for pilot 001
- manual content review failed for pilot 001 with score 0.2
- `chunked_source_grounding_live_pilot_002`: proposal-only DeepSeek V4 Pro live pilot with a narrower output contract
- Pro pilot 002 produced complete parseable JSON structurally
- manual content review remains pending for Goal 7F

Current boundaries:

- live outputs are proposal-only, not source truth
- no validation, product authority, strategy evidence, financial advice, live-trading authority, graduation, or architecture
- future live runs require live LLM admission and an explicit execution instruction
