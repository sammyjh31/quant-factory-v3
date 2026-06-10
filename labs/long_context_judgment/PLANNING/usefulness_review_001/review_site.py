"""Local review site for usefulness_review_001.

Serves a single-page review app on http://127.0.0.1:8923 — a plain-English
dashboard of the milestone results, the three study-card candidates with their
source passages (read live from the local ignored source file; never embedded
in this committed script), and the operator review form. Answers are saved to
operator_answers.json in this directory.

Run:  python3 labs/long_context_judgment/PLANNING/usefulness_review_001/review_site.py

This is an operator review instrument for the usefulness_review_001 experiment.
It is planning tooling, not a lab method, not evidence, and not architecture.
"""
import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
SOURCE = ROOT / "raw_corpora/selected/source_span_precision_repeat_001/source.txt"
ANSWERS = HERE / "operator_answers.json"
JUDGE_ENVELOPE = ROOT / "labs/llm_judge_calibration/EXPORTS/artifact_envelope.live_pilot_001.json"

CARDS = [
    {
        "id": "card1",
        "title": "Card 1 — Failed breakout raises the odds of an opposite break with continuation",
        "principle": "When a box (consolidation range) shows a failed breakout — price looks above the box and fails back inside — a later break in the OTHER direction is more likely to run with continuation, especially after a clean backtest of the boundary and a strong response.",
        "conditions": "The box must already exist when the failure happens (drawing it after the fact doesn't count). Ideal sequence: fail, backtest, strong sell response. Real cases are messy: sometimes a clean backtest, sometimes an instant rip, sometimes a stall. It's a read, not a mechanical rule.",
        "why": "Trapped breakout buyers are forced to puke their longs, and their selling stacks on top of the range participants' selling — that's why the move is 'generally much stronger.'",
        "limitations": "Squashes clean-vs-choppy failure modes into one idea; skips intra-box price action and volume profile nuance; 'strong response' is subjective.",
        "supports": [
            {"label": "Scenario walkthrough + trapped-longs logic", "start": 45, "end": 86},
            {"label": "Look-below symmetry", "start": 88, "end": 89},
            {"label": "Not-always-clean caveat", "start": 89, "end": 99},
        ],
    },
    {
        "id": "card2",
        "title": "Card 2 — Boundary trading is a default; failure entries are the preference; review before live",
        "principle": "General rule in a box: sell the top, buy the bottom — but never mechanically. The higher-conviction entry is the FAILURE of a boundary. And when you learn any new range concept, review closed charts after the session (did it work? why / why not?) before trading it live.",
        "conditions": "The boundary rule is explicitly 'a general rule,' not a signal. The failure preference is the teacher's personal style. The post-close review habit is framed as personal practice, not doctrine.",
        "why": "New-concept fixation makes traders see the pattern everywhere and force entries — 'you'll get short every one-minute failed breakout and just get chopped up.'",
        "limitations": "Blends an entry preference with a learning discipline; doesn't define what counts as a boundary 'failure' or how rigorous the review should be.",
        "supports": [
            {"label": "Boundary rule + failure preference", "start": 33, "end": 43},
            {"label": "New-concept fixation warning", "start": 108, "end": 127},
            {"label": "Post-close review method", "start": 128, "end": 137},
        ],
    },
    {
        "id": "card3",
        "title": "Card 3 — Draw the obvious box; nuance is the last 10%",
        "principle": "When drawing a box, capture the clear, obvious range of consolidated price action. Wick-vs-body choices, volume profile overlays, and market-structure tweaks refine it — but the plain, clear range already gets you ~90% of the value.",
        "conditions": "The 90% figure is the teacher's gut estimate, not a measurement. The nuance layer assumes you already understand market structure.",
        "why": "The box is just 'a range of consolidation that precedes trend' — its power is in being obvious, not precise.",
        "limitations": "May understate cases with extreme wicks; says nothing about timeframes or instrument differences.",
        "supports": [
            {"label": "Box definition", "start": 12, "end": 18},
            {"label": "Drawing guidance + the 90% remark", "start": 19, "end": 30},
        ],
    },
]

PAGE = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>QuantFactory V3 — Review &amp; Answer</title>
<style>
  :root { --bg:#0f1117; --panel:#181b24; --panel2:#1f2330; --text:#e8eaf0; --dim:#9aa3b5;
          --accent:#5eead4; --accent2:#818cf8; --good:#4ade80; --bad:#f87171; --warn:#fbbf24; }
  * { box-sizing:border-box; }
  body { margin:0; background:var(--bg); color:var(--text);
         font:16px/1.6 -apple-system, "Segoe UI", Helvetica, Arial, sans-serif; }
  .wrap { max-width:880px; margin:0 auto; padding:24px 20px 120px; }
  h1 { font-size:26px; margin:18px 0 4px; }
  h2 { font-size:20px; margin:36px 0 10px; color:var(--accent); }
  h3 { font-size:17px; margin:22px 0 8px; }
  p.sub { color:var(--dim); margin-top:0; }
  .tabs { display:flex; gap:8px; margin:22px 0 8px; flex-wrap:wrap; position:sticky; top:0;
          background:var(--bg); padding:12px 0; z-index:5; }
  .tab { padding:9px 16px; border-radius:99px; background:var(--panel); color:var(--dim);
         cursor:pointer; border:1px solid #2a2f3e; font-size:14.5px; }
  .tab.active { background:var(--accent); color:#06241f; font-weight:600; border-color:var(--accent); }
  section { display:none; } section.active { display:block; }
  .card { background:var(--panel); border:1px solid #262b3a; border-radius:14px; padding:18px 20px; margin:14px 0; }
  .stat-row { display:grid; grid-template-columns:repeat(auto-fit,minmax(180px,1fr)); gap:12px; margin:14px 0; }
  .stat { background:var(--panel2); border-radius:12px; padding:14px; text-align:center; }
  .stat .n { font-size:26px; font-weight:700; color:var(--accent); }
  .stat .l { font-size:12.5px; color:var(--dim); }
  .arc { display:flex; align-items:center; gap:10px; flex-wrap:wrap; font-size:15px; }
  .arc .step { background:var(--panel2); padding:8px 14px; border-radius:10px; }
  .arc .arrow { color:var(--dim); }
  .pill { display:inline-block; padding:2px 10px; border-radius:99px; font-size:12.5px; font-weight:600; }
  .pill.good { background:#14351f; color:var(--good); } .pill.bad { background:#3a1717; color:var(--bad); }
  .pill.warn { background:#382c10; color:var(--warn); }
  table { width:100%; border-collapse:collapse; font-size:14px; margin:10px 0; }
  th, td { text-align:left; padding:8px 10px; border-bottom:1px solid #262b3a; }
  th { color:var(--dim); font-weight:600; }
  details { background:var(--panel2); border-radius:10px; padding:10px 14px; margin:10px 0; }
  summary { cursor:pointer; color:var(--accent2); font-weight:600; font-size:14.5px; }
  pre.src { white-space:pre-wrap; font:13.5px/1.55 ui-monospace, Menlo, monospace; color:#cdd6e4;
            background:#12141c; border-radius:8px; padding:12px; margin:10px 0 2px; }
  .q { margin:16px 0 6px; font-weight:600; }
  .opts { display:flex; gap:8px; flex-wrap:wrap; }
  .opt { padding:8px 14px; border-radius:10px; border:1px solid #2c3245; background:var(--panel2);
         cursor:pointer; font-size:14.5px; color:var(--dim); }
  .opt.sel { background:var(--accent2); border-color:var(--accent2); color:#fff; font-weight:600; }
  textarea, input[type=text] { width:100%; background:#12141c; border:1px solid #2c3245; color:var(--text);
         border-radius:10px; padding:10px 12px; font:14.5px/1.5 inherit; margin-top:6px; }
  textarea { min-height:64px; resize:vertical; }
  .savebar { position:fixed; bottom:0; left:0; right:0; background:#12141cee; backdrop-filter:blur(6px);
             border-top:1px solid #262b3a; padding:12px 20px; display:flex; gap:14px; align-items:center;
             justify-content:center; z-index:10; }
  button.save { background:var(--accent); color:#06241f; font-weight:700; font-size:16px; border:0;
                padding:12px 34px; border-radius:12px; cursor:pointer; }
  #savestatus { color:var(--dim); font-size:14px; }
  .field-label { color:var(--dim); font-size:13.5px; margin-top:10px; }
  .why { color:var(--dim); font-size:14px; border-left:3px solid #2c3245; padding-left:12px; margin:8px 0; }
  .kicker { font-size:12.5px; letter-spacing:1.4px; text-transform:uppercase; color:var(--accent2); }
</style>
</head>
<body>
<div class="wrap">
  <div class="kicker">QuantFactory V3 · Milestone 5</div>
  <h1>Today's results, and the part only you can do</h1>
  <p class="sub">Three tabs: what happened (2-min read) → how the AI judge did → the study cards with your review form. Your answers save straight into the repo.</p>

  <div class="tabs">
    <div class="tab active" data-t="t1">1 · What happened</div>
    <div class="tab" data-t="t2">2 · Judge results</div>
    <div class="tab" data-t="t3">3 · Study cards + your review</div>
  </div>

  <section id="t1" class="active">
    <div class="card">
      <h3>The one-paragraph version</h3>
      <p>Your project's first <b>graduated method</b> now exists: when an AI reads trader material, it should point at <i>line ranges</i> in the source, and local code — not the AI — verifies them and computes the precise coordinates. That rule survived testing across two labs, three sources, and two model configurations, so it's now official architecture (GRAD-0001). Today we also measured whether an AI judge can take over the reviewing work I've been doing by hand. Answer: <b>it can help, but can't yet be trusted alone</b>. And finally — the bit that needs you — we turned real pilot output into three trading study cards, and your verdict on them is the project's first measurement of whether any of this is actually <i>useful</i>.</p>
    </div>
    <div class="stat-row">
      <div class="stat"><div class="n">13</div><div class="l">live model runs recorded (total)</div></div>
      <div class="stat"><div class="n">GRAD-0001</div><div class="l">first graduated method</div></div>
      <div class="stat"><div class="n">~$0.16</div><div class="l">total model spend today</div></div>
      <div class="stat"><div class="n">43 ✓</div><div class="l">boundary tests passing</div></div>
    </div>
    <div class="card">
      <h3>The locator story in one line</h3>
      <div class="arc">
        <div class="step">Broad contract, tight budget<br><span class="pill bad">0 / 4 locators right</span></div>
        <div class="arrow">→ give it room to think →</div>
        <div class="step">Same contract, thinking on<br><span class="pill good">8 / 9 right</span></div>
        <div class="arrow">→ new, messier source →</div>
        <div class="step">Third source<br><span class="pill good">3 / 3 perfect</span></div>
      </div>
      <p class="why">Translation: the AI wasn't bad at citing sources — it was being squeezed. With a budget sized for reasoning plus output, citations became near-perfect, even on an ugly unpunctuated transcript.</p>
    </div>
    <div class="card">
      <h3>What's still open</h3>
      <p>① Your study-card review (tab 3). ② A follow-up judge test on only the new-style artifacts — early signs say it might be fully trustable there. ③ Testing the graduated method on a non-DeepSeek model when you have a second API key. ④ The recursive deep-reading method, parked until you want it.</p>
    </div>
  </section>

  <section id="t2">
    <div class="card">
      <h3>What we tested</h3>
      <p>I re-ran <b>15 of my own past reviews</b> through a blinded AI judge — it saw the artifact, the source, and the rubric, but never my verdicts. Then we compared. Rules of the game (agreement bars, trick questions, repeat-tests) were locked in <i>before</i> the first call so the results couldn't be massaged.</p>
      <div class="stat-row">
        <div class="stat"><div class="n">10 / 15</div><div class="l">verdicts matched mine</div></div>
        <div class="stat"><div class="n">4 / 4</div><div class="l">trick questions caught<br>(it failed every junk artifact)</div></div>
        <div class="stat"><div class="n">2 / 2</div><div class="l">repeat-tests consistent</div></div>
        <div class="stat"><div class="n pill warn" style="font-size:18px">ASSISTIVE</div><div class="l">official rating, both axes:<br>useful pre-screener, human still decides</div></div>
      </div>
      <p class="why"><b>The interesting part:</b> on artifacts that follow the new graduated citation format, the judge agreed with me 4-for-4 with near-identical scores (one was 0.80 vs my 0.80, exactly). Every disagreement was either an old-format artifact it had no anchors for, or the judge being <i>stricter</i> than me — never sloppier. Stricter-but-assistive is the safe failure direction.</p>
    </div>
    <div class="card">
      <h3>All 17 trials</h3>
      <div id="trials"></div>
    </div>
  </section>

  <section id="t3">
    <div class="card">
      <p style="margin:6px 0"><b>How to do this:</b> read each card (they came from a real pilot run on the box-trades video transcript — every claim was verified against the source line-by-line). Click open the source passages if you want to compare. Then tap your answers. Gut reactions are exactly what's wanted. Hit <b>Save</b> at the bottom whenever — you can come back and edit.</p>
    </div>
    <div id="cards"></div>
    <div class="card">
      <h2 style="margin-top:6px">Overall verdict</h2>
      <div class="q">5. Is this card format right for studying — principle + conditions + limits + source lines?</div>
      <div class="opts" data-k="q5_format">
        <div class="opt" data-v="this format works">This format works</div>
        <div class="opt" data-v="flashcard Q&A">Flashcard Q&amp;A</div>
        <div class="opt" data-v="checklist">Checklist</div>
        <div class="opt" data-v="annotated transcript">Annotated transcript</div>
        <div class="opt" data-v="chart-annotated examples">Chart-annotated examples</div>
      </div>
      <div class="field-label">Or describe what you'd rather have:</div>
      <input type="text" data-k="q5_other" placeholder="optional — your ideal format">

      <div class="q">6. Scale check: a full course transcript (~15k words) would yield ~50 cards like these. Useful study asset, or noise?</div>
      <div class="opts" data-k="q6_volume">
        <div class="opt" data-v="useful asset">Useful asset</div>
        <div class="opt" data-v="noise">Noise</div>
        <div class="opt" data-v="depends">Depends (say below)</div>
      </div>
      <input type="text" data-k="q6_note" placeholder="optional — depends on what?">

      <div class="q">7. The north-star question: after reading these, are you closer to "this pipeline could make something I'd use weekly" — or not? What artifact do you actually want it to produce?</div>
      <div class="opts" data-k="q7_closer">
        <div class="opt" data-v="closer">Closer</div>
        <div class="opt" data-v="not the right artifact">Not the right artifact</div>
        <div class="opt" data-v="unsure">Unsure</div>
      </div>
      <textarea data-k="q7_want" placeholder="what would you actually want — be greedy, this steers the next milestone"></textarea>
    </div>
  </section>
</div>

<div class="savebar">
  <button class="save" onclick="save()">Save my answers</button>
  <span id="savestatus"></span>
</div>

<script>
const state = { answers: {} };

document.querySelectorAll('.tab').forEach(t => t.onclick = () => {
  document.querySelectorAll('.tab').forEach(x => x.classList.remove('active'));
  document.querySelectorAll('section').forEach(x => x.classList.remove('active'));
  t.classList.add('active');
  document.getElementById(t.dataset.t).classList.add('active');
});

function optRow(key, opts) {
  return `<div class="opts" data-k="${key}">` +
    opts.map(o => `<div class="opt" data-v="${o[0]}">${o[1]}</div>`).join('') + `</div>`;
}

function cardHtml(c) {
  const sup = c.supports.map(s =>
    `<details><summary>${s.label} — source lines ${s.start}–${s.end}</summary><pre class="src">${s.text}</pre></details>`).join('');
  return `<div class="card">
    <h3>${c.title}</h3>
    <p><b>${c.principle}</b></p>
    <div class="why"><b>Conditions:</b> ${c.conditions}</div>
    <div class="why"><b>Why it works (per the source):</b> ${c.why}</div>
    <div class="why"><b>Honest limits:</b> ${c.limitations}</div>
    ${sup}
    <div class="q">1. Keep this card?</div>
    ${optRow(c.id + '_keep', [["yes","Yes"],["no","No"],["rework","Only if reworked"]])}
    <div class="q">2. Would you act on it — something you'd check on a chart this week?</div>
    ${optRow(c.id + '_act', [["yes","Yes"],["vaguely","Vaguely"],["no","No"]])}
    <div class="q">3. What did the card lose that the source taught? <span style="color:var(--dim);font-weight:400">(one line is fine)</span></div>
    <input type="text" data-k="${c.id}_missing" placeholder="optional">
    <div class="q">4. The source citations (line ranges) — would you ever click through?</div>
    ${optRow(c.id + '_locator', [["useful","Useful"],["dead weight","Dead weight"],["auditing only","Only for auditing"]])}
  </div>`;
}

function renderTrials(rows) {
  let h = '<table><tr><th>Trial</th><th>My verdict</th><th>Judge</th><th>Match</th><th>Note</th></tr>';
  for (const r of rows) {
    const m = r.verdict_match ? '<span class="pill good">match</span>' : '<span class="pill bad">differs</span>';
    const note = r.negative_control ? 'trick question ✓' : (r.self_consistency_probe ? 'repeat-test' : (r.note || (r.per_candidate || '')));
    h += `<tr><td>${r.trial}</td><td>${r.human}</td><td>${r.judge}</td><td>${m}</td><td style="color:var(--dim)">${note}</td></tr>`;
  }
  document.getElementById('trials').innerHTML = h + '</table>';
}

function wire() {
  document.querySelectorAll('.opts').forEach(row => {
    row.querySelectorAll('.opt').forEach(o => o.onclick = () => {
      row.querySelectorAll('.opt').forEach(x => x.classList.remove('sel'));
      o.classList.add('sel');
      state.answers[row.dataset.k] = o.dataset.v;
    });
  });
  document.querySelectorAll('input[type=text],textarea').forEach(el => {
    el.oninput = () => { state.answers[el.dataset.k] = el.value; };
  });
}

function prefill(saved) {
  Object.assign(state.answers, saved);
  for (const [k, v] of Object.entries(saved)) {
    const row = document.querySelector(`.opts[data-k="${k}"]`);
    if (row) row.querySelectorAll('.opt').forEach(o => { if (o.dataset.v === v) o.classList.add('sel'); });
    const el = document.querySelector(`[data-k="${k}"]:not(.opts)`);
    if (el && 'value' in el) el.value = v;
  }
}

async function save() {
  const res = await fetch('/api/save', { method: 'POST', headers: {'Content-Type':'application/json'},
                                         body: JSON.stringify(state.answers) });
  document.getElementById('savestatus').textContent =
    res.ok ? 'Saved ✓ (' + new Date().toLocaleTimeString() + ') — edit any time and save again'
           : 'Save failed — is the server still running?';
}

(async () => {
  const d = await (await fetch('/api/data')).json();
  document.getElementById('cards').innerHTML = d.cards.map(cardHtml).join('');
  renderTrials(d.trials);
  wire();
  if (d.saved) prefill(d.saved);
})();
</script>
</body>
</html>
"""


def build_data():
    lines = SOURCE.read_text(encoding="utf-8").splitlines()
    cards = []
    for c in CARDS:
        c2 = dict(c)
        c2["supports"] = [
            {**s, "text": "\n".join(f"{i:4} {lines[i-1]}" for i in range(s["start"], min(s["end"], len(lines)) + 1))}
            for s in c["supports"]
        ]
        cards.append(c2)
    trials = json.loads(JUDGE_ENVELOPE.read_text())["artifact"]["payload"]["trial_table"]
    saved = json.loads(ANSWERS.read_text()) if ANSWERS.exists() else None
    return {"cards": cards, "trials": trials, "saved": saved}


class Handler(BaseHTTPRequestHandler):
    def _send(self, code, body, ctype):
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path == "/api/data":
            self._send(200, json.dumps(build_data()).encode(), "application/json")
        else:
            self._send(200, PAGE.encode(), "text/html; charset=utf-8")

    def do_POST(self):
        if self.path != "/api/save":
            return self._send(404, b"{}", "application/json")
        n = int(self.headers.get("Content-Length", 0))
        answers = json.loads(self.rfile.read(n) or b"{}")
        ANSWERS.write_text(json.dumps(answers, indent=2) + "\n", encoding="utf-8")
        self._send(200, b'{"ok": true}', "application/json")

    def log_message(self, *args):  # quiet
        pass


if __name__ == "__main__":
    print("Review site running: http://127.0.0.1:8923  (Ctrl-C to stop)")
    HTTPServer(("127.0.0.1", 8923), Handler).serve_forever()
