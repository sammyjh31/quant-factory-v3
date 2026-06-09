# Chunked Source Grounding Live Pilot 007 Admission Packet

Status: Goal 15A proposed planning packet
Historical status: pre-run admission record; current run status is owned by `labs/chunked_source_grounding/EXPORTS/run_record.live_pilot_007.json`.
Lab: `chunked_source_grounding`
Experiment: `chunked_source_grounding_live_pilot_007`

This is a proposed live LLM pilot planning record, not a completed run, not research evidence, and not a synthesis export. Execution requires a separately authorized Goal 15B instruction; the operator's milestone-4 goal directive supplies it for this evidence chain.

This packet contains no protocol records and claims no method success.

The Goal 13A decision review listed a third-source repeat of line-range-first as a candidate fork; the milestone-4 graduation question makes that evidence need explicit, which is the condition the decision review set for another chunked pilot.

## Hardening / Cleanup Discipline And Delta From Pilot 006

This packet reuses the pilot 006 line-range-first pattern and changes three declared variables:

1. **Third source excerpt** (the source-generality test). New operator-authorized selection under the milestone-4 directive: a 950-word teaching segment on volatility-regime assessment, environment definition, and tool selection, from a different author and topic than sources one and two. The origin transcript is unpunctuated-ASR-degraded in places — deliberately messier than the second source, which is north-star-relevant difficulty, recorded honestly as a known confound for any failure attribution.
2. **Deterministic local wrapping recorded as part of selection.** The origin transcript has no line structure (single line). The excerpt was wrapped locally at 50 characters via Python `textwrap.wrap` before hashing; line ranges refer to the wrapped excerpt. This is local pre-segmentation, consistent with the line-range-first lesson that segmentation and verification are local responsibilities, and it is part of the recorded selection procedure, not a model responsibility.
3. **Thinking enabled with a reasoning-aware 12000-token cap** — the portfolio's current operator-directed configuration, validated in long-context pilot 004. Pilot 006 ran thinking-off at a 900 cap; the config delta is declared and the cross-config comparison value (006 vs 007) is part of the design.

The contract itself — line-range locator candidates only, no model-emitted offsets or hashes, same four sections and entry caps — is unchanged from pilot 006 (template body identical except ids, source ref, and source ordinal).

## Admission Checklist Coverage

* **Benchmark pack**: `text_judgment_v0`, same `v2_lesson_refs` (`weak_source_grounding`, `report_only_confusion`) and metadata safety as pilot 006. Added known difficulty: ASR degradation (missing punctuation, transcription garbles) may make paraphrase fidelity and locator review harder; added failure modes from recent pilots: grounded-but-mislocated ranges, overclaimed exactness, entry-cap overflow under thinking mode, reasoning consuming the output cap.
* **MethodCard / ExperimentCard**: `method_card.proposed.json` (`chunked_source_grounding_live_pilot_007_method`), `experiment_card.proposed.json` (`chunked_source_grounding_live_pilot_007`). The experiment asks: does the line-range-first locator contract repeat on a third, messier source under the thinking-enabled configuration? Result that would change future behavior: a support-valid repeat completes the source-generality evidence item for the line-range-first graduation nomination; a failure either blocks the nomination or narrows it with an ASR-quality boundary condition, depending on failure mode.
* **Evaluator plan**: `evaluator_plan.md` in this packet — same three evaluators, pilot 006 strict rubric, plus entry-cap and reasoning/content token recording.
* **Source/privacy boundary**: `source_privacy_boundary.md` in this packet.
* **Prompt/template hash plan**: `prompt_template.live_pilot_007.md`, SHA-256 `ad8f12fb0fa35015b99e88ed5667738e31f93308425f18f65c154c098b41c655`.
* **Model/config recording plan**: locked in `run_admission_update.md` in this packet.
* **Output artifact types**: `chunked_source_line_range_locator_candidate_proposal`, same four sections and exclusions as pilot 006.
* **Negative-result value**: failure modes separate cleanly — parse failure indicts the config, invalid line numbers indict wrapping or line arithmetic, mislocated-but-grounded claims indict locator pointing, and ASR-garble-driven failures indict source quality — each sharpening the graduation ADR's boundary conditions.
* **Stop condition**: `stop_condition.md` in this packet.
* **Budget/secrets**: `$3` hard cap; `DEEPSEEK_API_KEY` name only; ignored trace paths only.
* **Proposal-only statement**: Outputs from this experiment are proposals until evaluated. They do not create source truth, role support, data truth, validation, strategy evidence, financial advice, product authority, live-trading authority, or architecture.
