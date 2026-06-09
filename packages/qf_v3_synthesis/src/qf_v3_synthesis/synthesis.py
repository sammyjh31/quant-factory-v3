from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path
from typing import Any

from qf_v3_protocol.discovery import lab_export_paths, repo_root
from qf_v3_protocol.validation import validate_record


def synthesize_exports(root: Path | None = None) -> dict[str, Any]:
    current_root = repo_root(root)
    destination = current_root / "generated"
    destination.mkdir(parents=True, exist_ok=True)

    records = []
    for path in lab_export_paths(current_root):
        payload = json.loads(path.read_text())
        path_records = payload if isinstance(payload, list) else [payload]
        for record in path_records:
            validate_record(record)
            records.append(record)

    summary = _summarize(records)
    _write_json(destination / "synthesis_summary.json", summary)
    _write_markdown(destination / "synthesis_summary.md", summary)
    return summary


def _summarize(records: list[dict[str, Any]]) -> dict[str, Any]:
    by_schema: dict[str, int] = defaultdict(int)
    labs: set[str] = set()
    benchmarks: set[str] = set()
    methods: set[str] = set()
    polarities: set[str] = set()
    statuses: set[str] = set()

    for record in records:
        schema_name = record["schema_name"]
        by_schema[schema_name] += 1
        if schema_name == "RunRecord":
            run = record["run_record"]
            labs.add(run["lab_id"])
            benchmarks.add(run["benchmark_pack_id"])
            methods.add(run["method_id"])
            polarities.add(run["outcome_polarity"])
            statuses.add(run["status"])
        elif schema_name == "MethodCard":
            method = record["method_card"]
            labs.add(method["lab_id"])
            methods.add(method["method_id"])
        elif schema_name == "ExperimentCard":
            experiment = record["experiment_card"]
            labs.add(experiment["lab_id"])
            benchmarks.update(experiment["benchmark_pack_ids"])
            methods.update(experiment["method_ids"])

    return {
        "status": "non_authoritative_export_summary",
        "record_count": len(records),
        "schema_counts": dict(sorted(by_schema.items())),
        "labs": set(sorted(labs)),
        "benchmarks": sorted(benchmarks),
        "methods": sorted(methods),
        "outcome_polarities": sorted(polarities),
        "statuses": sorted(statuses),
        "disclaimer": (
            "Generated synthesis outputs summarize protocol export records and are not authority."
        ),
        "ordering_note": (
            "Lists and schema counts are sorted alphabetically by identifier for deterministic "
            "inspection only; ordering is not a ranking."
        ),
        "metrics_note": (
            "Counts are export inspection aids only; they are not method authority, graduation "
            "evidence, or portfolio decisions."
        ),
    }


def _write_json(path: Path, summary: dict[str, Any]) -> None:
    serializable = {
        key: sorted(value) if isinstance(value, set) else value for key, value in summary.items()
    }
    path.write_text(json.dumps(serializable, indent=2, sort_keys=True) + "\n")


def _write_markdown(path: Path, summary: dict[str, Any]) -> None:
    lines = [
        "# Synthesis Summary",
        "",
        "Status: generated non-authoritative export summary",
        "",
        summary["disclaimer"],
        "",
        summary["ordering_note"],
        "",
        summary["metrics_note"],
        "",
        f"Record count: {summary['record_count']}",
        "",
        "## Labs",
        "",
        *[f"- `{lab}`" for lab in sorted(summary["labs"])],
        "",
        "## Schema Counts",
        "",
        *[f"- `{schema}`: {count}" for schema, count in summary["schema_counts"].items()],
        "",
    ]
    path.write_text("\n".join(lines))
