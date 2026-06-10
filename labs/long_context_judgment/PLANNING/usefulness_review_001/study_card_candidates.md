# Usefulness Review 001: Study Card Candidates

Status: milestone-5 paired experiment — operator usefulness review (planning material, not exports)
Lab: `long_context_judgment`
Derived from: `long_context_judgment_live_pilot_004` (proposal-only artifact; strict review found 8/9 locators support-valid)

This is the portfolio's first downstream-usefulness probe: the question is not whether these cards are well-grounded (the strict review already answered that) but whether they are **useful to the operator as trading-study material**. No model call is involved; the operator's review form is the instrument.

These cards are proposals. They are not validation, product evidence, strategy evidence, financial advice, live-trading authority, graduation, or architecture.

Locator handles refer to the second source excerpt (`raw_corpora_sha256:9f9e143429f5842a`, the pharm box-trades excerpt, local path `raw_corpora/selected/source_span_precision_repeat_001/source.txt`). All handles below were validated by the pilot 004 strict review.

---

## Card 1 — Failed breakout raises opposite-break continuation odds

**Principle.** When a consolidation range (box) exhibits a failed breakout ("look above and fail"), the likelihood of a subsequent break in the opposite direction *with continuation* is elevated — especially when the failure is followed by a clean backtest of the boundary and a strong response.

**Conditions the source attaches.** The box must already have existed when the failure happened (a box drawn after the fact does not qualify); the ideal sequence is fail → backtest → strong sell response; real instances range from clean backtests to immediate rips or stalls, so this is a read, not a mechanical rule.

**Why the source says it works.** Trapped breakout participants are forced to liquidate, adding their pressure to the range participants' — which is why the break is "generally much stronger."

**Known limitations (self-declared by the extraction).** Compresses clean-vs-choppy failure modes into one principle; omits intra-box price action and volume profile context; "strong response" is subjective.

**Source support.** Scenario walkthrough and liquidation logic: lines 45–86 (offsets 1759–3343, span sha `6047c2f3…245c9e`); look-below symmetry: lines 88–89 (corrected by strict review); not-always-clean caveat: lines 89–99 (offsets 3392–3728).

---

## Card 2 — Boundary trading is a default; failure entries are the preference; review before live

**Principle.** The general rule in a box is sell the top, buy the bottom — but not mechanically; the higher-conviction entry is the *failure* of a boundary. When applying any newly learned range concept, review closed charts after market close (did it work? why / why not?) before trading it live, because new-concept fixation makes traders see the pattern everywhere and force entries.

**Conditions the source attaches.** The boundary rule is explicitly "a general rule," not an automatic signal; the failure preference is the teacher's personal style; the post-close review practice is framed as personal practice, not doctrine.

**Known limitations.** Blends an entry preference with a learning discipline; doesn't quantify what counts as a boundary "failure" or define review rigor.

**Source support.** Boundary rule and failure preference: lines 33–43 (offsets 1285–1730, span sha `72a787…146560`); new-concept fixation warning: lines 108–127 (offsets 3990–4630); post-close review method: lines 128–137 (offsets 4630–4905).

---

## Card 3 — Draw the obvious box; nuance is the last 10%

**Principle.** Constructing a box should prioritize capturing a clear, obvious range of consolidated price action. Wick-vs-body decisions, volume profile overlays, and market-structure tweaks can refine it, but a plain, clear range already delivers ~90% of the utility.

**Conditions the source attaches.** The 90% figure is the teacher's anecdotal estimate, not a measurement; the nuance layer presumes existing market-structure understanding.

**Known limitations.** May understate cases with extreme wicking; says nothing about timeframe selection or instrument differences.

**Source support.** Box definition: lines 12–18 (offsets 478–709, span sha `fc261f…00595f` — the span independently accepted by two pilots' strict reviews); drawing guidance and the 90% remark: lines 19–30 (offsets 709–1215, span sha `23984c…beacfd`).
