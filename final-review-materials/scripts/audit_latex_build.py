#!/usr/bin/env python3
"""Scan a LaTeX build log for problems that need manual review."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


CHECKS = [
    ("fatal", re.compile(r"^\ufeff?! .+", re.MULTILINE)),
    ("undefined-reference", re.compile(r"undefined references?", re.IGNORECASE)),
    ("rerun", re.compile(r"Rerun to get (cross-references|outlines) right", re.IGNORECASE)),
    ("missing-character", re.compile(r"Missing character:", re.IGNORECASE)),
    ("overfull-hbox", re.compile(r"Overfull \\hbox", re.IGNORECASE)),
    ("overfull-vbox", re.compile(r"Overfull \\vbox", re.IGNORECASE)),
    ("font-warning", re.compile(r"LaTeX Font Warning:", re.IGNORECASE)),
]


def scan_log(log_text: str) -> dict[str, list[str]]:
    results: dict[str, list[str]] = {}
    for name, pattern in CHECKS:
        matches = [
            match.group(0).replace("\ufeff", "").strip()
            for match in pattern.finditer(log_text)
        ]
        if matches:
            results[name] = matches
    return results


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Scan a LaTeX .log file for build and layout warnings."
    )
    parser.add_argument("log_file", help="Path to a LaTeX .log file")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Exit nonzero when any issue is found",
    )
    args = parser.parse_args()

    log_path = Path(args.log_file).resolve()
    if not log_path.exists():
        raise FileNotFoundError(f"Log file not found: {log_path}")

    issues = scan_log(log_path.read_text(encoding="utf-8", errors="replace"))
    if not issues:
        print("No common LaTeX log issues found.")
        return 0

    print(f"Found {sum(len(v) for v in issues.values())} LaTeX log issue(s):")
    for name, matches in issues.items():
        print(f"\n[{name}] {len(matches)}")
        for line in matches[:10]:
            print(f"- {line}")
        if len(matches) > 10:
            print(f"- ... {len(matches) - 10} more")

    return 1 if args.strict else 0


if __name__ == "__main__":
    raise SystemExit(main())
