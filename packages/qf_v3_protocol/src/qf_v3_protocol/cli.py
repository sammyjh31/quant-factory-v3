from __future__ import annotations

import argparse
from pathlib import Path

from qf_v3_protocol.discovery import (
    default_validation_paths,
    invalid_example_paths,
    repo_root,
)
from qf_v3_protocol.validation import ValidationError, validate_path


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Validate QuantFactory V3 protocol records.")
    parser.add_argument("paths", nargs="*", type=Path, help="JSON files to validate.")
    parser.add_argument(
        "--expect-invalid",
        action="store_true",
        help="Require supplied records to fail validation.",
    )
    parser.add_argument(
        "--include-invalid-examples",
        action="store_true",
        help="Also verify packaged invalid examples fail validation.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    root = repo_root(Path.cwd())
    paths = args.paths or default_validation_paths(root)
    try:
        if args.expect_invalid:
            _validate_expected_invalid(paths)
        else:
            _validate_expected_valid(paths)
            if args.include_invalid_examples or not args.paths:
                _validate_expected_invalid(invalid_example_paths(root))
    except ValidationError as error:
        print(f"qf-v3-validate: FAIL: {error}")
        return 1
    print(f"qf-v3-validate: OK ({len(paths)} path(s) validated)")
    return 0


def _validate_expected_valid(paths: list[Path]) -> None:
    for path in paths:
        validate_path(path)


def _validate_expected_invalid(paths: list[Path]) -> None:
    for path in paths:
        try:
            validate_path(path)
        except ValidationError:
            continue
        raise ValidationError(f"Expected invalid fixture to fail validation: {path}")


if __name__ == "__main__":
    raise SystemExit(main())
