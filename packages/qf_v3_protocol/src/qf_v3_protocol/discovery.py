from __future__ import annotations

from pathlib import Path


def repo_root(start: Path | None = None) -> Path:
    current = (start or Path.cwd()).resolve()
    for candidate in (current, *current.parents):
        if (
            (candidate / "PORTFOLIO_CURRENT.md").exists()
            and (candidate / "pyproject.toml").exists()
        ):
            return candidate
    raise RuntimeError(f"Could not find repo root from {current}")


def active_benchmark_paths(root: Path | None = None) -> list[Path]:
    base = repo_root(root) / "benchmarks" / "active"
    return sorted(base.glob("*.json"))


def valid_example_paths(root: Path | None = None) -> list[Path]:
    base = repo_root(root) / "packages" / "qf_v3_protocol" / "examples" / "valid"
    return sorted(base.glob("*.json"))


def invalid_example_paths(root: Path | None = None) -> list[Path]:
    base = repo_root(root) / "packages" / "qf_v3_protocol" / "examples" / "invalid"
    return sorted(base.glob("*.json"))


def lab_export_paths(root: Path | None = None) -> list[Path]:
    base = repo_root(root) / "labs"
    return sorted(base.glob("*/EXPORTS/*.json"))


def default_validation_paths(root: Path | None = None) -> list[Path]:
    current_root = repo_root(root)
    return [
        *valid_example_paths(current_root),
        *active_benchmark_paths(current_root),
        *lab_export_paths(current_root),
    ]
