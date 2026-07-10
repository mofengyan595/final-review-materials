#!/usr/bin/env python3
"""Create a LaTeX review-project skeleton from the bundled template."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path


WORKING_TEMPLATES = [
    "source-inventory.csv",
    "source-coverage.csv",
    "example-catalog.csv",
    "course-map.md",
]


def skill_root() -> Path:
    return Path(__file__).resolve().parents[1]


def copy_template(output_dir: Path, force: bool) -> Path:
    template = skill_root() / "assets" / "latex-template" / "main.tex"
    if not template.exists():
        raise FileNotFoundError(f"Template not found: {template}")

    output_dir.mkdir(parents=True, exist_ok=True)
    target = output_dir / "main.tex"
    if target.exists() and not force:
        raise FileExistsError(f"Refusing to overwrite existing file: {target}")
    shutil.copy2(template, target)
    return target


def create_dirs(output_dir: Path) -> None:
    for name in [
        "sources",
        "extracted",
        "coverage",
        "figures",
        "sections",
        "build",
        "logs",
    ]:
        (output_dir / name).mkdir(parents=True, exist_ok=True)


def copy_working_templates(output_dir: Path) -> list[Path]:
    template_dir = skill_root() / "assets" / "working-templates"
    coverage_dir = output_dir / "coverage"
    copied: list[Path] = []

    for name in WORKING_TEMPLATES:
        source = template_dir / name
        if not source.exists():
            raise FileNotFoundError(f"Working template not found: {source}")

        target = coverage_dir / name
        if target.exists():
            continue
        shutil.copy2(source, target)
        copied.append(target)

    return copied


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Initialize a final-review LaTeX project skeleton."
    )
    parser.add_argument("output_dir", help="Directory to create or update")
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite an existing main.tex",
    )
    args = parser.parse_args()

    output_dir = Path(args.output_dir).resolve()
    main_tex = copy_template(output_dir, args.force)
    create_dirs(output_dir)
    working_files = copy_working_templates(output_dir)
    print(f"Created review project at {output_dir}")
    print(f"Template: {main_tex}")
    for path in working_files:
        print(f"Working file: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
