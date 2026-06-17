#!/usr/bin/env python3
"""Create a LaTeX review-project skeleton from the bundled template."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path


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
        "figures",
        "sections",
        "build",
        "logs",
    ]:
        (output_dir / name).mkdir(parents=True, exist_ok=True)


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
    print(f"Created review project at {output_dir}")
    print(f"Template: {main_tex}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
