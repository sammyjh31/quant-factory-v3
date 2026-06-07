# Local Raw Corpora

Status: local source-material boundary

This directory is the canonical local-only home for raw source material used by
QuantFactory V3 experiments.

Only this README is tracked. Everything else under `raw_corpora/` is ignored by
git.

## Layout

Use this layout for the current Desktop text corpus:

```text
raw_corpora/
  trader_source_corpus/
    ...
```

Use this layout for source material selected for an admitted experiment:

```text
raw_corpora/
  selected/
    live_llm_pilot_001/
      source.txt
      source_scope.local.json
```

`source.txt` is still raw source material. Selection means an operator approved
that local excerpt for one admitted experiment; it does not make the excerpt
safe to commit.

`source_scope.local.json` may store local-only reproducibility metadata such as:

- original local path,
- source id,
- source file hash,
- excerpt hash,
- selection note,
- character or segment offsets when available.

## Boundary

Raw trader text, transcripts, videos, private notes, provider payloads, prompt
traces containing source text, model traces, generated local manifests, and
selected experiment excerpts must not be committed.

Benchmark packs and lab exports may reference only metadata-safe source ids,
hashes, span ids, and summaries allowed by the active experiment admission
packet.

Local source material is not project authority, benchmark authority, research
evidence, product evidence, financial advice, strategy validation, or
architecture.

Before using a local source excerpt in a live LLM experiment, confirm:

1. the experiment admission packet defines the source/privacy boundary;
2. the selected source path remains ignored by git;
3. no raw source text, private notes, provider payloads, prompt traces
   containing source text, model traces, or secrets are staged;
4. committed records contain only metadata-safe source references.
