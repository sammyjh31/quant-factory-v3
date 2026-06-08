# Preliminary Method Comparison: Long-Context vs Chunked Source Grounding

Status: preliminary / non-authoritative comparison note

This note is not a synthesis export, not a protocol object, and not portfolio authority.

Only tiny pilots exist. No method has graduated. No winner is declared. No product, strategy, validation, financial-advice, live-trading, or architecture claim is made.

## Why this file exists

Existing currentness docs could not own this comparison without becoming a running results ledger. `PORTFOLIO_CURRENT.md` and `LAB_REGISTRY.md` route status; they should not accumulate method-comparison prose. `qf-v3-synthesis` is read-only and generated outputs are non-authoritative. This local planning note records one bounded comparison inside the active `chunked_source_grounding` lab because the comparison was triggered by the chunked pilot sequence against the prior long-context baseline.

## Compared Records

This note compares only:

- `long_context_judgment_live_pilot_001`
- `chunked_source_grounding_live_pilot_001`
- `chunked_source_grounding_live_pilot_002`
- `chunked_source_grounding_live_pilot_003`
- `chunked_source_grounding_live_pilot_004`
- `chunked_source_grounding_live_pilot_005`

The Flash chunked run was a bounded negative result. Its content review failed because the output contract was too large for the admitted Flash run and produced `output_contract_too_large`, `incomplete_json`, and truncation failure evidence.

The Pro run is a method/config variant with a narrowed output contract, not a replacement for the Flash result. It produced complete parseable JSON and passed manual content review with caveats.

The source-span precision run is a refinement of the Pro narrowed-contract variant, not a replacement for pilot 002. It produced complete parseable JSON, passed manual content review with score `0.88`, and recorded `source_span_precision_improved`, `content_review_passed_with_caveats`, and `limited_abstraction`.

The second-source source-span precision repeat tests whether the pilot 003 pattern generalizes beyond the first source. It produced complete parseable JSON, passed manual content review with score `0.86`, and recorded `source_span_precision_repeated`, `content_review_passed_with_caveats`, `broad_segment_refs`, and `limited_abstraction`.

Goal 10B added strict source-span re-review findings for the two source-span precision pilots:

- `chunked_source_grounding_live_pilot_003_strict_span_review`
- `chunked_source_grounding_live_pilot_004_strict_span_review`

The pilot 003 strict-span review passed with score `0.88`: reviewed hints `5`, exact `3`, approximate `2`, broad `0`, missing `0`, quote hashes `5`, and overclaimed exactness `0`. It supports the earlier source-span precision improvement conclusion while preserving the caveat that the original model artifact did not emit canonical locators.

The pilot 004 strict-span review passed with score `0.82`: reviewed hints `6`, exact `4`, approximate `2`, broad `0`, missing `0`, quote hashes `6`, and overclaimed exactness `1`. It supports the second-source repeat conclusion, but one model-labeled exact case was better treated as approximate because it compressed a composite local span.

The source-span locator candidate pilot 005 tested direct locator emission rather than reviewer reconstruction. Its strict locator review, `chunked_source_grounding_live_pilot_005_strict_locator_review`, recorded score `0.58`, pass_fail `fail`, locator candidates reviewed `3`, line ranges `3/3` valid and reviewer-useful, char offsets `3/3` syntactically valid but `0/3` evidence-valid, quote hashes `3` computed locally and mechanically valid but not support-valid, labels: exact `0`, approximate `2`, broad `1`, missing `0`, and overclaimed exactness `0`. Direct locator emission improved only partially over pilots 003/004.

## Comparison Axes

| Axis | Long-context pilot 001 | Chunked Flash pilot 001 | Chunked Pro pilot 002 | Chunked Pro pilot 003 | Chunked Pro pilot 004 | Chunked locator pilot 005 |
| --- | --- | --- | --- | --- | --- | --- |
| source grounding | Mostly specific span hints, but still affected by `missing_context`. | Not content-reviewable because truncation blocked source-grounding review. | Source-linked at a claim level; caveat: `broad_segment_refs` rather than canonical offsets. | Source-linked at tighter span-hint level for reviewed claims; strict review supplied canonical line/offset/hash locators after the fact. | Source-linked on a second excerpt; strict review supplied canonical line/offset/hash locators after the fact and found one overclaimed exactness case. | Line ranges were useful support regions; character offsets and quote hashes were not evidence-valid support handles. |
| source-span precision | Useful hints, but not designed as a span-precision contract. | Not reviewable as a completed artifact. | Broad segment refs made the artifact reviewable but imprecise. | Improved over pilot 002; strict review found exact `3`, approximate `2`, broad `0`, missing `0`. | Repeated the source-span precision pattern beyond the first source; strict review found exact `4`, approximate `2`, broad `0`, missing `0`. | Direct locator emission is promising only at the line-range level; strict review found exact `0`, approximate `2`, broad `1`, missing `0`. |
| research usefulness | Useful as a broader judgment-abstraction baseline. | Useful as negative-result value for output-contract sizing. | Useful for testing whether narrowed chunked contracts can produce reviewable source-grounded artifacts. | Useful as the first positive refinement signal for chunked source-span precision. | Useful as repeatability evidence for the source-span precision variant, not as graduation evidence. | Useful negative/partial result: it isolates locator granularity as the next bottleneck rather than parseability. |
| hallucination / unsupported claims | Separated promotional or unsupported claims reasonably, with caveats. | Not reviewable as a completed artifact. | Unsupported-claim report did not add unsupported material, but the zero-count report is not comprehensive proof. | No unsupported-claim report was needed for the narrow claims reviewed; this is not comprehensive hallucination filtering. | Unsupported-claim report flagged overstatement risks without adding them as claims; still not comprehensive hallucination filtering. | Unsupported-claim handling was not the main bottleneck; locator correctness was. |
| abstraction quality | Stronger broader judgment abstraction, with `over_abstracted_teacher_intent` caveat. | No reliable abstraction result because the artifact failed structurally. | `limited_abstraction` is expected because the narrowed contract avoided broad judgment commentary. | `limited_abstraction` remains; source-span precision came at the cost of broader teaching synthesis. | `limited_abstraction` repeats as the main tradeoff; precision improves inspectability but does not recover broad teaching logic. | Abstraction remained intentionally out of scope; locator reliability was the tested variable. |
| negative-result value | Revealed missing-context and teacher-intent compression issues. | High negative-result value: the Flash contract was too broad for the configured cap. | Shows that narrowing the output contract can trade breadth for structural completion. | Shows the narrowed contract can be refined for tighter support labels while preserving parseability. | Shows that source-span precision did repeat under strict review in pilots 003/004. | Shows that line ranges work better than char offsets for direct locator emission; quote hashes computed from inaccurate offsets are not support-valid. |
| output-contract fit | Fit was acceptable for a compact long-context proposal. | Poor fit: output contract exceeded the admitted Flash output budget. | Better fit: smaller contract produced parseable reviewable output. | Good fit: source-span precision contract remained parseable and reviewable. | Good fit on a second source: complete parseable JSON and reviewable support labels. | Good parseability, weak locator granularity: the next bottleneck is reliable locator granularity, not model parseability. |
| comparison value for future method design | Baseline for broader judgment extraction. | Warning that chunked/source-grounded prompts can fail from contract size before method quality is testable. | Baseline for complete chunked Pro source-grounding under a narrow contract. | Candidate method variant to repeat before broader claims. | Repeatability signal for source-span precision, with open questions about offsets, stricter review, and whether a grounded long-context variant can preserve breadth. | Points toward a line-range-first locator contract rather than asking the model for canonical character offsets and quote-hash-ready spans in one step. |

## Preliminary Read

Long-context preserved broader judgment abstraction better than the chunked variants, but its review caveats matter: `missing_context` and `over_abstracted_teacher_intent` show that broad abstraction can compress source intent too aggressively.

Chunked Flash should not be treated as method-quality evidence against chunked/source-grounded reading. It is a clean failure record for output-contract fit.

Chunked Pro with the narrowed contract preserved content-reviewability and claim-level grounding better than the Flash attempt. It also lost broader judgment abstraction by design. That tradeoff is useful: the narrower method made source grounding inspectable, but it did not try to recover the richer teaching logic that the long-context method attempted.

Chunked Pro source-span precision improved over pilot 002. The manual content review found that exact/approximate labels were warranted for reviewed claims, and the strict review later showed reviewers could map the support hints to canonical line ranges, character offsets, and quote hashes.

The second-source source-span precision repeat passed manual content review with caveats, then survived strict source-span re-review. The strongest finding is repeatability: source-span precision improvement repeated under stricter review on a different source excerpt while preserving parseability and support-label reviewability.

The source-span locator candidate pilot shifted the bottleneck again. Goal 11C showed that a model can emit locator coordinates and local code can compute quote hashes from those coordinates. Goal 11D showed the sharper limitation: line ranges `3/3` were valid and reviewer-useful, but char offsets were only syntactically valid and `0/3` evidence-valid. The resulting quote hashes were mechanically computable but not support-valid.

Line-range locator candidates are useful; the char-offset and quote-hash candidate workflow is not yet reliable. Source-span precision did repeat under strict review in pilots 003/004, and pilot 005 shows direct locator emission is promising only at the line-range level. The next bottleneck is reliable locator granularity, not model parseability.

## Next Research Direction

The source-span precision repeat supports one narrow conclusion: the pilot 003 pattern generalized to a second source excerpt as a proposal-only, manually reviewed method signal, and the pattern survived strict source-span re-review. It does not validate the method, graduate it, or prove trading usefulness.

The source-span locator candidate pilot supports a second narrow conclusion: direct locator emission improved only partially over pilots 003/004. It reduced reviewer reconstruction when the model emitted usable line ranges, but it failed as a canonical character-offset and quote-hash-support workflow.

The leading next step is Goal 12A: plan a line-range-first locator contract, where the model emits line ranges and local review computes offsets/hashes only after line-range validation. The contract should not ask the model to produce quote hashes and should not treat character offsets as reliable until local review has validated the line-range support.

This remains a lab-local method experiment. It is not validation, product evidence, strategy evidence, financial advice, live-trading authority, graduation, or architecture.
