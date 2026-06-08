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

The Flash chunked run was a bounded negative result. Its content review failed because the output contract was too large for the admitted Flash run and produced `output_contract_too_large`, `incomplete_json`, and truncation failure evidence.

The Pro run is a method/config variant with a narrowed output contract, not a replacement for the Flash result. It produced complete parseable JSON and passed manual content review with caveats.

The source-span precision run is a refinement of the Pro narrowed-contract variant, not a replacement for pilot 002. It produced complete parseable JSON, passed manual content review with score `0.88`, and recorded `source_span_precision_improved`, `content_review_passed_with_caveats`, and `limited_abstraction`.

The second-source source-span precision repeat tests whether the pilot 003 pattern generalizes beyond the first source. It produced complete parseable JSON, passed manual content review with score `0.86`, and recorded `source_span_precision_repeated`, `content_review_passed_with_caveats`, `broad_segment_refs`, and `limited_abstraction`.

## Comparison Axes

| Axis | Long-context pilot 001 | Chunked Flash pilot 001 | Chunked Pro pilot 002 | Chunked Pro pilot 003 | Chunked Pro pilot 004 |
| --- | --- | --- | --- | --- | --- |
| source grounding | Mostly specific span hints, but still affected by `missing_context`. | Not content-reviewable because truncation blocked source-grounding review. | Source-linked at a claim level; caveat: `broad_segment_refs` rather than canonical offsets. | Source-linked at tighter span-hint level for reviewed claims; exact/approximate labels were warranted. | Source-linked on a second excerpt; exact/approximate labels were warranted, with `broad_segment_refs` still present. |
| source-span precision | Useful hints, but not designed as a span-precision contract. | Not reviewable as a completed artifact. | Broad segment refs made the artifact reviewable but imprecise. | Improved over pilot 002; still lacks canonical offsets. | Repeated the source-span precision pattern beyond the first source; still lacks canonical offsets. |
| research usefulness | Useful as a broader judgment-abstraction baseline. | Useful as negative-result value for output-contract sizing. | Useful for testing whether narrowed chunked contracts can produce reviewable source-grounded artifacts. | Useful as the first positive refinement signal for chunked source-span precision. | Useful as repeatability evidence for the source-span precision variant, not as graduation evidence. |
| hallucination / unsupported claims | Separated promotional or unsupported claims reasonably, with caveats. | Not reviewable as a completed artifact. | Unsupported-claim report did not add unsupported material, but the zero-count report is not comprehensive proof. | No unsupported-claim report was needed for the narrow claims reviewed; this is not comprehensive hallucination filtering. | Unsupported-claim report flagged overstatement risks without adding them as claims; still not comprehensive hallucination filtering. |
| abstraction quality | Stronger broader judgment abstraction, with `over_abstracted_teacher_intent` caveat. | No reliable abstraction result because the artifact failed structurally. | `limited_abstraction` is expected because the narrowed contract avoided broad judgment commentary. | `limited_abstraction` remains; source-span precision came at the cost of broader teaching synthesis. | `limited_abstraction` repeats as the main tradeoff; precision improves inspectability but does not recover broad teaching logic. |
| negative-result value | Revealed missing-context and teacher-intent compression issues. | High negative-result value: the Flash contract was too broad for the configured cap. | Shows that narrowing the output contract can trade breadth for structural completion. | Shows the narrowed contract can be refined for tighter support labels while preserving parseability. | Shows the repeat still needs canonical offsets or a stricter evaluator before stronger claims. |
| output-contract fit | Fit was acceptable for a compact long-context proposal. | Poor fit: output contract exceeded the admitted Flash output budget. | Better fit: smaller contract produced parseable reviewable output. | Good fit: source-span precision contract remained parseable and reviewable. | Good fit on a second source: complete parseable JSON and reviewable support labels. |
| comparison value for future method design | Baseline for broader judgment extraction. | Warning that chunked/source-grounded prompts can fail from contract size before method quality is testable. | Baseline for complete chunked Pro source-grounding under a narrow contract. | Candidate method variant to repeat before broader claims. | Repeatability signal for source-span precision, with open questions about offsets, stricter review, and whether a grounded long-context variant can preserve breadth. |

## Preliminary Read

Long-context preserved broader judgment abstraction better than the chunked variants, but its review caveats matter: `missing_context` and `over_abstracted_teacher_intent` show that broad abstraction can compress source intent too aggressively.

Chunked Flash should not be treated as method-quality evidence against chunked/source-grounded reading. It is a clean failure record for output-contract fit.

Chunked Pro with the narrowed contract preserved content-reviewability and claim-level grounding better than the Flash attempt. It also lost broader judgment abstraction by design. That tradeoff is useful: the narrower method made source grounding inspectable, but it did not try to recover the richer teaching logic that the long-context method attempted.

Chunked Pro source-span precision improved over pilot 002. The manual content review found that exact/approximate labels were warranted for reviewed claims, while the artifact still lacks canonical offsets and retains limited broader abstraction.

The second-source source-span precision repeat passed manual content review with caveats. The strongest finding is repeatability: source-span precision repeated on a different source excerpt while preserving parseability and support-label reviewability. The main unresolved tradeoff also repeated: the method still uses broad segment refs rather than canonical offsets and intentionally sacrifices broader judgment abstraction.

## Next Research Direction

Use this comparison note to choose the next bounded research fork.

The source-span precision repeat supports one narrow conclusion: the pilot 003 pattern generalized to a second source excerpt as a proposal-only, manually reviewed method signal. It does not validate the method, graduate it, or prove trading usefulness.

Reasonable next forks include a stricter evaluator for canonical offsets, a third-source repeat, or a grounded long-context variant that tests whether broader judgment abstraction can keep stronger source-span discipline. This note does not choose any direction as architecture.
