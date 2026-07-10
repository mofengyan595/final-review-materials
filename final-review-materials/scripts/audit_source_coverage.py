#!/usr/bin/env python3
"""Audit source-unit coverage and lecture-example mapping for a review project."""

from __future__ import annotations

import argparse
import csv
from collections import Counter, defaultdict
from pathlib import Path


INVENTORY_HEADERS = {
    "source_file",
    "source_type",
    "coverage_mode",
    "unit_count",
    "read_status",
    "example_scan_status",
    "notes",
}
COVERAGE_HEADERS = {
    "source_file",
    "unit_id",
    "unit_type",
    "knowledge_point_id",
    "extracted_items",
    "output_location",
    "status",
    "uncertainty",
}
EXAMPLE_HEADERS = {
    "example_id",
    "source_file",
    "unit_id",
    "example_type",
    "knowledge_point_id",
    "stem_status",
    "media_status",
    "answer_source",
    "output_location",
    "status",
    "uncertainty",
}

ALLOWED_COVERAGE_MODES = {"page", "item", "reference"}
ALLOWED_READ_STATUSES = {"pending", "complete", "partial", "unreadable"}
ALLOWED_SCAN_STATUSES = {"pending", "complete", "partial", "not-applicable"}
ALLOWED_COVERAGE_STATUSES = {"mapped", "merged", "non-content", "needs-review"}
ALLOWED_EXAMPLE_STATUSES = {"mapped", "merged", "needs-review"}
ALLOWED_STEM_STATUSES = {"complete", "partial", "unreadable"}
ALLOWED_MEDIA_STATUSES = {"not-needed", "preserved", "redrawn", "needs-review"}
ALLOWED_ANSWER_SOURCES = {
    "teacher",
    "source",
    "derived",
    "missing",
    "conflict",
    "needs-review",
}


class Audit:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def error(self, message: str) -> None:
        self.errors.append(message)

    def warning(self, message: str) -> None:
        self.warnings.append(message)


def load_csv(path: Path, required: set[str], audit: Audit) -> list[dict[str, str]]:
    if not path.exists():
        audit.error(f"missing file: {path}")
        return []

    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        headers = set(reader.fieldnames or [])
        missing = sorted(required - headers)
        if missing:
            audit.error(f"{path.name}: missing columns: {', '.join(missing)}")
            return []

        rows: list[dict[str, str]] = []
        for row_number, row in enumerate(reader, start=2):
            normalized = {key: (value or "").strip() for key, value in row.items()}
            if not any(normalized.values()):
                continue
            normalized["_row"] = str(row_number)
            rows.append(normalized)
        return rows


def require_value(
    row: dict[str, str], field: str, label: str, audit: Audit
) -> bool:
    if row.get(field, ""):
        return True
    audit.error(f"{label}: {field} is empty")
    return False


def parse_positive_count(value: str, label: str, audit: Audit) -> int | None:
    try:
        count = int(value)
    except ValueError:
        audit.error(f"{label}: unit_count must be a positive integer")
        return None
    if count <= 0:
        audit.error(f"{label}: unit_count must be greater than zero")
        return None
    return count


def audit_inventory(
    rows: list[dict[str, str]], audit: Audit
) -> tuple[dict[str, dict[str, str]], dict[str, int]]:
    if not rows:
        audit.error("source-inventory.csv: no source rows")
        return {}, {}

    sources: dict[str, dict[str, str]] = {}
    expected_counts: dict[str, int] = {}

    for row in rows:
        label = f"source-inventory.csv row {row['_row']}"
        source = row["source_file"]
        if not require_value(row, "source_file", label, audit):
            continue
        if source in sources:
            audit.error(f"{label}: duplicate source_file: {source}")
            continue

        mode = row["coverage_mode"]
        read_status = row["read_status"]
        scan_status = row["example_scan_status"]
        require_value(row, "source_type", label, audit)

        if mode not in ALLOWED_COVERAGE_MODES:
            audit.error(f"{label}: invalid coverage_mode: {mode or '<empty>'}")
        if read_status not in ALLOWED_READ_STATUSES:
            audit.error(f"{label}: invalid read_status: {read_status or '<empty>'}")
        if scan_status not in ALLOWED_SCAN_STATUSES:
            audit.error(
                f"{label}: invalid example_scan_status: {scan_status or '<empty>'}"
            )

        if mode in {"page", "item"}:
            count = parse_positive_count(row["unit_count"], label, audit)
            if count is not None:
                expected_counts[source] = count
        elif row["unit_count"]:
            parse_positive_count(row["unit_count"], label, audit)

        if read_status in {"pending", "partial", "unreadable"}:
            audit.warning(f"{source}: read_status is {read_status}")
        if scan_status in {"pending", "partial"}:
            audit.warning(f"{source}: example_scan_status is {scan_status}")
        if scan_status == "not-applicable" and not row["notes"]:
            audit.warning(f"{source}: explain why example scanning is not applicable")

        sources[source] = row

    return sources, expected_counts


def audit_coverage(
    rows: list[dict[str, str]],
    sources: dict[str, dict[str, str]],
    expected_counts: dict[str, int],
    audit: Audit,
) -> set[tuple[str, str]]:
    seen_units: set[tuple[str, str]] = set()
    counts: Counter[str] = Counter()
    unit_ids: dict[str, set[str]] = defaultdict(set)

    for row in rows:
        label = f"source-coverage.csv row {row['_row']}"
        source = row["source_file"]
        unit_id = row["unit_id"]
        status = row["status"]

        require_value(row, "source_file", label, audit)
        require_value(row, "unit_id", label, audit)
        require_value(row, "unit_type", label, audit)

        if source and source not in sources:
            audit.error(f"{label}: source not found in inventory: {source}")
        key = (source, unit_id)
        if source and unit_id:
            if key in seen_units:
                audit.error(f"{label}: duplicate source unit: {source} / {unit_id}")
            seen_units.add(key)
            counts[source] += 1
            unit_ids[source].add(unit_id)

        if status not in ALLOWED_COVERAGE_STATUSES:
            audit.error(f"{label}: invalid status: {status or '<empty>'}")
            continue

        if status in {"mapped", "merged"}:
            require_value(row, "knowledge_point_id", label, audit)
            require_value(row, "extracted_items", label, audit)
            require_value(row, "output_location", label, audit)
        elif status == "non-content":
            if not row["extracted_items"] and not row["uncertainty"]:
                audit.error(f"{label}: justify non-content classification")
        elif status == "needs-review":
            require_value(row, "uncertainty", label, audit)
            audit.warning(f"{source} / {unit_id}: coverage needs review")

    for source, expected in expected_counts.items():
        actual = counts[source]
        if actual != expected:
            audit.error(
                f"{source}: coverage has {actual} unique unit(s), expected {expected}"
            )
        if sources[source]["coverage_mode"] == "page":
            expected_ids = {str(index) for index in range(1, expected + 1)}
            missing_ids = sorted(expected_ids - unit_ids[source], key=int)
            unexpected_ids = sorted(unit_ids[source] - expected_ids)
            if missing_ids:
                audit.error(
                    f"{source}: missing page/slide unit_id(s): {', '.join(missing_ids)}"
                )
            if unexpected_ids:
                audit.error(
                    f"{source}: unexpected page/slide unit_id(s): "
                    f"{', '.join(unexpected_ids)}"
                )

    return seen_units


def audit_examples(
    rows: list[dict[str, str]],
    sources: dict[str, dict[str, str]],
    seen_units: set[tuple[str, str]],
    audit: Audit,
) -> None:
    seen_ids: set[str] = set()

    for row in rows:
        label = f"example-catalog.csv row {row['_row']}"
        example_id = row["example_id"]
        source = row["source_file"]
        unit_id = row["unit_id"]
        status = row["status"]

        require_value(row, "example_id", label, audit)
        require_value(row, "source_file", label, audit)
        require_value(row, "unit_id", label, audit)
        require_value(row, "example_type", label, audit)

        if example_id:
            if example_id in seen_ids:
                audit.error(f"{label}: duplicate example_id: {example_id}")
            seen_ids.add(example_id)

        if source and source not in sources:
            audit.error(f"{label}: source not found in inventory: {source}")
        elif source and sources[source]["coverage_mode"] != "reference":
            if (source, unit_id) not in seen_units:
                audit.error(
                    f"{label}: source unit missing from coverage matrix: {source} / {unit_id}"
                )

        if row["stem_status"] not in ALLOWED_STEM_STATUSES:
            audit.error(
                f"{label}: invalid stem_status: {row['stem_status'] or '<empty>'}"
            )
        if row["media_status"] not in ALLOWED_MEDIA_STATUSES:
            audit.error(
                f"{label}: invalid media_status: {row['media_status'] or '<empty>'}"
            )
        if row["answer_source"] not in ALLOWED_ANSWER_SOURCES:
            audit.error(
                f"{label}: invalid answer_source: {row['answer_source'] or '<empty>'}"
            )
        if status not in ALLOWED_EXAMPLE_STATUSES:
            audit.error(f"{label}: invalid status: {status or '<empty>'}")
            continue

        if status in {"mapped", "merged"}:
            require_value(row, "knowledge_point_id", label, audit)
            require_value(row, "output_location", label, audit)
        if status == "mapped" and row["stem_status"] != "complete":
            audit.warning(f"{example_id}: mapped example stem is {row['stem_status']}")
        if row["media_status"] == "needs-review":
            audit.warning(f"{example_id}: example media needs review")
        if row["answer_source"] in {"missing", "conflict", "needs-review"}:
            audit.warning(f"{example_id}: answer source is {row['answer_source']}")
        if status == "needs-review":
            require_value(row, "uncertainty", label, audit)
            audit.warning(f"{example_id}: example mapping needs review")


def audit_course_map(path: Path, audit: Audit) -> None:
    if not path.exists():
        audit.error(f"missing file: {path}")
        return
    text = path.read_text(encoding="utf-8-sig", errors="replace").strip()
    if not text:
        audit.error("course-map.md: file is empty")
    if "Replace this line" in text or "Replace with a concept" in text:
        audit.warning("course-map.md: template placeholders remain")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Audit source coverage and lecture-example mapping."
    )
    parser.add_argument("project_dir", help="Review-project root containing coverage/")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Exit nonzero for unresolved warnings as well as structural errors",
    )
    args = parser.parse_args()

    project_dir = Path(args.project_dir).resolve()
    coverage_dir = project_dir / "coverage"
    audit = Audit()

    inventory_rows = load_csv(
        coverage_dir / "source-inventory.csv", INVENTORY_HEADERS, audit
    )
    coverage_rows = load_csv(
        coverage_dir / "source-coverage.csv", COVERAGE_HEADERS, audit
    )
    example_rows = load_csv(
        coverage_dir / "example-catalog.csv", EXAMPLE_HEADERS, audit
    )

    sources, expected_counts = audit_inventory(inventory_rows, audit)
    seen_units = audit_coverage(
        coverage_rows, sources, expected_counts, audit
    )
    audit_examples(example_rows, sources, seen_units, audit)
    audit_course_map(coverage_dir / "course-map.md", audit)

    print(
        "Coverage summary: "
        f"{len(inventory_rows)} source(s), "
        f"{len(coverage_rows)} unit(s), "
        f"{len(example_rows)} lecture example(s)"
    )
    for message in audit.errors:
        print(f"ERROR: {message}")
    for message in audit.warnings:
        print(f"WARNING: {message}")

    if audit.errors:
        print(f"Audit failed with {len(audit.errors)} error(s).")
        return 1
    if args.strict and audit.warnings:
        print(f"Strict audit failed with {len(audit.warnings)} unresolved warning(s).")
        return 1

    print("Source coverage audit passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
