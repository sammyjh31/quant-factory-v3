# Preliminary Method Comparison: Long-Context vs Chunked Source Grounding

Status: preliminary / non-authoritative comparison note

This note is not a synthesis export, not a protocol object, and not portfolio authority.

Only tiny pilots exist. No method has graduated. No winner is declared. No product, strategy, validation, financial-advice, live-trading, or architecture claim is made.

## Why this file exists

Existing currentness docs could not own this comparison without becoming a running results ledger. `PORTFOLIO_CURRENT.md` and `LAB_REGISTRY.md` route status; they should not accumulate method-comparison prose. `qf-v3-synthesis` is read-only and generated outputs are non-authoritative. This local planning note records one bounded comparison inside the active `chunked_source_grounding` lab because the comparison was triggered by the chunked pilot sequence against the prior long-context baseline.

## Compared Records

This note compares only:

- `long_context_judgment_live_pilot_001`
- `chunked_source_grounding_live_pilot_001` (bounded negative result: oversized Flash output contract)
- `chunked_source_grounding_live_pilot_002` (narrowed Pro contract variant)
- `chunked_source_grounding_live_pilot_003` (source-span precision refinement)
- `chunked_source_grounding_live_pilot_004` (second-source source-span precision repeat)
- `chunked_source_grounding_live_pilot_005` (direct locator emission candidate)
- `chunked_source_grounding_live_pilot_006` (line-range-first locator contract)
- `long_context_judgment_live_pilot_002` (grounded long-context variant; split result: strong abstraction, failed locators, contract overflow)

Per-pilot scores, failure tags, and review details live in the export records, including the manual content reviews and the strict span/locator/line-range review records for pilots 003 through 006.

## Comparison Axes

| Axis | Long-context pilot 001 | Chunked Flash pilot 001 | Chunked Pro pilot 002 | Chunked Pro pilot 003 | Chunked Pro pilot 004 | Chunked locator pilot 005 | Chunked line-range-first pilot 006 | Grounded long-context pilot 002 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| source grounding | Mostly specific span hints, but still affected by `missing_context`. | Not content-reviewable because truncation blocked source-grounding review. | Source-linked at a claim level; caveat: `broad_segment_refs` rather than canonical offsets. | Source-linked at tighter span-hint level for reviewed claims; strict review supplied canonical line/offset/hash locators after the fact. | Source-linked on a second excerpt; strict review supplied canonical line/offset/hash locators after the fact and found one overclaimed exactness case. | Line ranges were useful support regions; character offsets and quote hashes were not evidence-valid support handles. | Line ranges were support-valid; local offsets and quote hashes were computable after validation. | Claims were faithful with real support in the source, but all four emitted line ranges failed strict support validation; strict review supplied corrected locators after the fact. |
| source-span precision | Useful hints, but not designed as a span-precision contract. | Not reviewable as a completed artifact. | Broad segment refs made the artifact reviewable but imprecise. | Improved over pilot 002 under strict review. | Repeated the source-span precision pattern beyond the first source under strict review. | Direct locator emission was promising only at the line-range level. | Line-range-first improved locator precision under strict review. | Severe regression: 0/4 support-valid versus pilot 006's 3/3 on the same source; three `exact` labels were overclaimed. |
| research usefulness | Useful as a broader judgment-abstraction baseline. | Useful as negative-result value for output-contract sizing. | Useful for testing whether narrowed chunked contracts can produce reviewable source-grounded artifacts. | Useful as the first positive refinement signal for chunked source-span precision. | Useful as repeatability evidence for the source-span precision variant, not as graduation evidence. | Useful negative/partial result: it isolates locator granularity as the next bottleneck rather than parseability. | Useful positive method signal: ask the model for line ranges; let local review/tooling compute offsets and quote hashes after validation. | Useful split signal: strongest abstraction in the portfolio so far paired with failed locators and a contract overflow; isolates locator assignment as a candidate for its own pass. |
| hallucination / unsupported claims | Separated promotional or unsupported claims reasonably, with caveats. | Not reviewable as a completed artifact. | Unsupported-claim report did not add unsupported material, but the zero-count report is not comprehensive proof. | No unsupported-claim report was needed for the narrow claims reviewed; this is not comprehensive hallucination filtering. | Unsupported-claim report flagged overstatement risks without adding them as claims; still not comprehensive hallucination filtering. | Unsupported-claim handling was not the main bottleneck; locator correctness was. | Unsupported-claim handling was not the main bottleneck; locator-contract responsibility improved. | Unsupported-claim reports flagged real specification gaps without adding material; claim faithfulness held even where locators failed. |
| abstraction quality | Stronger broader judgment abstraction, with `over_abstracted_teacher_intent` caveat. | No reliable abstraction result because the artifact failed structurally. | `limited_abstraction` is expected because the narrowed contract avoided broad judgment commentary. | `limited_abstraction` remains; source-span precision came at the cost of broader teaching synthesis. | `limited_abstraction` repeats as the main tradeoff; precision improves inspectability but does not recover broad teaching logic. | Abstraction remained intentionally out of scope; locator reliability was the tested variable. | Abstraction remained intentionally out of scope; the run tested locator workflow, not broader judgment recovery. | Strongest yet: conditional logic preserved, principles cited supporting claims and self-declared limitations; caveat: `limited_breadth` (two principles, partial excerpt coverage). |
| negative-result value | Revealed missing-context and teacher-intent compression issues. | High negative-result value: the Flash contract was too broad for the configured cap. | Shows that narrowing the output contract can trade breadth for structural completion. | Shows the narrowed contract can be refined for tighter support labels while preserving parseability. | Shows that source-span precision did repeat under strict review in pilots 003/004. | Shows that line ranges work better than char offsets for direct locator emission; quote hashes computed from inaccurate offsets are not support-valid. | Confirms the pilot 005 lesson by removing the weak model-facing char-offset/hash responsibility from the contract. | High: contract overflow at the admitted cap echoes chunked pilot 001; identifies grounded-but-mislocated as a failure mode distinct from hallucination; records cap pressure as a confound. |
| output-contract fit | Fit was acceptable for a compact long-context proposal. | Poor fit: output contract exceeded the admitted Flash output budget. | Better fit: smaller contract produced parseable reviewable output. | Good fit: source-span precision contract remained parseable and reviewable. | Good fit on a second source: complete parseable JSON and reviewable support labels. | Good parseability, weak locator granularity: the next bottleneck is reliable locator granularity, not model parseability. | Good fit: line-range-only locator output stayed parseable and reviewable. | Poor fit: finish_reason=length at 1600 tokens; as-emitted JSON unparseable, though all five sections completed and truncation hit only the final note string. |
| comparison value for future method design | Baseline for broader judgment extraction. | Warning that chunked/source-grounded prompts can fail from contract size before method quality is testable. | Baseline for complete chunked Pro source-grounding under a narrow contract. | Candidate method variant to repeat before broader claims. | Repeatability signal for source-span precision, with open questions about offsets, stricter review, and whether a grounded long-context variant can preserve breadth. | Points toward a line-range-first locator contract rather than asking the model for canonical character offsets and quote-hash-ready spans in one step. | Shows local offset/hash computation after line-range validation is the stronger workflow, with remaining questions about repeatability, calibration, and long-context grounding comparison. | Suggests abstraction and locator pointing may not coexist in one single-pass contract at this budget; motivates a cap-relieved repeat to remove the confound before concluding a two-pass split is required. |

## Locator Thread Decision Review

Goal 13A: decision review / thread pause note

Decision: pause the chunked locator thread as a provisional method lesson.

This is a provisional pause, not graduation.

For chunked source-grounding, the strongest current locator pattern is: ask the model for line ranges; compute offsets and quote hashes locally after line-range validation.

### What the thread tested

The thread tested whether chunked/source-grounded LLM contracts could move from broad source-grounded claims toward reviewable source locator behavior. It moved through Flash output-contract failure, Pro narrowed source-grounding, source-span precision, second-source repetition, direct line/char locator emission, and finally a line-range-first locator contract planned at `labs/chunked_source_grounding/PLANNING/line_range_locator_contract_001/`.

### What the thread learned

Line-range-first is the strongest locator contract in this thread so far. The model should propose source line ranges; local review/tooling should validate those ranges and only then compute character offsets and quote hashes. This avoids asking the model to emit brittle character offsets or cryptographic hashes, while still giving reviewers support-valid regions.

### What repeated across sources

Source-span precision improved on pilot 003 and repeated on pilot 004 under strict review. The broader pattern is that narrower chunked contracts can preserve parseability and make source support more inspectable, but they still trade away broader judgment abstraction.

### What failed

The oversized Flash contract failed structurally. Direct line+char offset locator emission only partially improved the workflow: line ranges were useful, but model-proposed character offsets were not evidence-valid and quote hashes computed from those offsets were not support-valid.

### What remains unresolved

Line-range-first has not been repeated on a third source. Manual line-range review has not been calibrated across reviewers. Chunked source-grounding has not yet been compared against a stricter grounded long-context variant that tries to preserve broader judgment abstraction while requiring source-linked support. All pilots in this comparison used one model family (DeepSeek V4 Flash/Pro), so whether the line-range-first lesson is model-general or a DeepSeek contract-fit artifact is untested.

### What should not be done next

Do not activate the recursive contextual meaning loop yet.

Do not create graph infrastructure.

Do not promote line-range-first to architecture.

Do not create a protocol field for line ranges yet.

Do not run another chunked pilot unless the new evidence need is explicit.

### Candidate next forks

1. Pause the chunked locator thread as a provisional method lesson.
2. Repeat line-range-first on a third source excerpt.
3. Compare against a stricter grounded long-context variant.
4. Calibrate manual line-range review reliability.
5. Activate another methodology thread later, such as recursive contextual meaning loop.
6. Repeat line-range-first once under a different model family to test whether the locator lesson is model-general.

### Recommended next fork

The recommended next fork is to pause the chunked locator thread and plan a stricter grounded long-context variant.

Comparison question:

```text
Can long-context preserve broader judgment abstraction while adopting the source-grounding / line-range discipline learned from chunked_source_grounding?
```

This remains a lab-local method experiment. It is not validation, product evidence, strategy evidence, financial advice, live-trading authority, graduation, or architecture.

## Grounded Long-Context Decision Review

Goal 13D: decision review for the Goal 13C grounded long-context run

Decision: the comparison question is answered "split, and confounded" — plan one cap-relieved repeat to remove the confound before treating the split as a method truth.

This is a provisional decision, not graduation.

### What the run tested

`long_context_judgment_live_pilot_002` ran the Goal 13B grounded long-context contract on the same second-source excerpt as chunked pilots 004 through 006: judgment principle proposals layered on top of the line-range-first locator discipline, DeepSeek V4 Pro, 1600-token output cap.

### What the run learned

The two halves of the comparison question came apart cleanly:

* **Abstraction half: preserved.** Both judgment principles kept the source's conditional logic, cited their supporting claims, and self-declared limitations — the strongest abstraction quality in the portfolio so far, without the `over_abstracted_teacher_intent` caveat of pilot 001 or the `limited_abstraction` tradeoff of the chunked thread.
* **Grounding half: failed.** Strict review under the pilot 006 rubric found zero of four emitted line ranges support-valid (pilot 006: three of three on the same source). Three were labeled `exact` anyway. All four claims have real support in the excerpt — the failure mode is grounded-but-mislocated, which is distinct from hallucination.
* **Contract fit: failed.** The combined contract overflowed the cap (`finish_reason=length`); the as-emitted JSON did not parse, though all five sections completed before the cut.

### What is confounded

The model emitted everything against a hard output ceiling. Budget pressure, not the abstraction workload itself, may explain part or all of the locator regression. The current evidence cannot distinguish "abstraction degrades locator pointing" from "cap pressure degrades locator pointing."

### What should not be done next

Do not conclude that single-pass grounded long-context is dead before the confound is removed.

Do not re-run the same contract at the same cap.

Do not promote the two-pass split to a method commitment without the disambiguating run.

Do not start the cross-model repeat or third-source repeat before the grounded thread reaches a clean stopping point; an unresolved confound is exactly the kind of explicit evidence need that justifies one more run in this thread.

### Candidate next forks

1. Cap-relieved repeat: same grounded contract, larger output cap (new admission update), to disambiguate cap pressure from abstraction workload.
2. Two-pass split: abstraction pass first, then a separate locator-assignment pass over the produced claims.
3. Cross-model repeat of line-range-first (fork 6 of the Goal 13A review) to test model generality.
4. Third-source repeat of line-range-first.
5. Activate the recursive contextual meaning loop thread.

### Recommended next fork

Fork 1: plan a cap-relieved grounded long-context repeat (Goal 14A planning packet, `long_context_judgment` pilot 003). It is the cheapest run that converts the 13C split result from confounded to interpretable, and its outcome decides between fork 2 and continuing single-pass work. Forks 3 and 4 remain queued behind it as the graduation-horizon evidence for line-range-first.

This remains a lab-local method experiment. It is not validation, product evidence, strategy evidence, financial advice, live-trading authority, graduation, or architecture.
