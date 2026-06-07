from __future__ import annotations

import argparse
from pathlib import Path

from qf_v3_synthesis import synthesize_exports


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Import V3 scaffold lab exports read-only.")
    parser.add_argument("--root", type=Path, default=Path.cwd(), help="Repository root.")
    args = parser.parse_args(argv)
    summary = synthesize_exports(root=args.root)
    print(
        "qf-v3-synthesis: OK "
        f"({summary['record_count']} fixture records across {len(summary['labs'])} labs)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
