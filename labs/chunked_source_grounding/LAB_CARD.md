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
- `labs/chunked_source_grounding/EXPORTS/evaluation_record.live_pilot_002_manual_content_review.json`: one DeepSeek V4 Pro manual content-review EvaluationRecord
- manual content review passed for pilot 002 with caveats: source-linked at a claim level, broad segment refs, limited abstraction
- `chunked_source_grounding_live_pilot_003`: proposal-only DeepSeek V4 Pro source-span precision live pilot
- source-span precision pilot 003 produced complete parseable JSON structurally
- `labs/chunked_source_grounding/EXPORTS/evaluation_record.live_pilot_003_manual_content_review.json`: one DeepSeek V4 Pro source-span precision manual content-review EvaluationRecord
- manual content review passed for pilot 003 with caveats: source-span precision improved, exact/approximate labels were warranted for reviewed claims, no canonical offsets, limited broader abstraction
- `chunked_source_grounding_live_pilot_004`: second-source source-span precision planning packet only
- `labs/chunked_source_grounding/PLANNING/live_llm_pilot_004/`: proposed MethodCard/ExperimentCard and admission scope for the second-source repeat
- pilot 004 has no model call, export records, manual review, research evidence, synthesis claim, graduation status, or architecture

Current boundaries:

- live outputs are proposal-only, not source truth
- no validation, product authority, strategy evidence, financial advice, live-trading authority, graduation, or architecture
- future live runs require live LLM admission and an explicit execution instruction
