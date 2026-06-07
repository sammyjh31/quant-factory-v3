# AGENTS.md - Benchmarks

Benchmark packs are metadata-safe test harnesses.

They preserve source-reference structure, known difficulties, known failure modes, and V2 lesson refs.

They are not raw source truth.

Do not commit raw private source text, private notes, provider payloads, prompts, secrets, model traces, or unapproved V2 corpus material.

Every active benchmark pack must include `v2_lesson_refs`.

If a benchmark pack becomes stale, update it directly or move it out of `active/`.

## Active Benchmark Quality Rules

Every active benchmark should make clear:

* what capability it tests,
* what failure mode it preserves,
* why it is metadata-safe,
* what would make it stale,
* what evaluation surface will consume it.

Benchmark packs that cannot answer these questions should remain future candidates, not active packs.
