# Source Locator Boundary

Status: planning only

The approved source scope remains metadata-safe and local.

Source reference:

```text
raw_corpora_sha256:9f9e143429f5842a
```

Local ignored source path:

```text
raw_corpora/selected/source_span_precision_repeat_001/source.txt
```

The source text stays ignored/local; no raw source text is committed.

## Responsibility Split

The model may propose line ranges.

Local review and local tooling must:

- validate candidate line ranges against local ignored source;
- compute character offsets only after the line range is accepted;
- compute quote hashes locally only from validated line ranges and offsets;
- mark hashes as computed locally, not model-generated.

The model must not emit quote hashes, cryptographic hashes, raw source text, or canonical character offsets.

## Why This Boundary Exists

Pilot 005 showed that mechanically computable hashes do not prove semantic support when the offsets are not evidence-valid. The line-range-first contract keeps the model's role at proposal level and keeps cryptographic or canonical support handles local.
