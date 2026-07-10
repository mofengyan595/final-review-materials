from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SKILL_ROOT = REPO_ROOT / "final-review-materials"
AUDIT_SCRIPT = SKILL_ROOT / "scripts" / "audit_source_coverage.py"
FIXTURES = Path(__file__).resolve().parent / "fixtures"


class SourceCoverageTest(unittest.TestCase):
    def run_audit(self, fixture: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [
                sys.executable,
                str(AUDIT_SCRIPT),
                str(FIXTURES / fixture),
                "--strict",
            ],
            text=True,
            capture_output=True,
            check=False,
        )

    def test_complete_project_passes_strict_audit(self) -> None:
        result = self.run_audit("complete")

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("Source coverage audit passed.", result.stdout)

    def test_missing_source_unit_fails_audit(self) -> None:
        result = self.run_audit("missing-unit")

        self.assertEqual(result.returncode, 1)
        self.assertIn("coverage has 1 unique unit(s), expected 2", result.stdout)

    def test_wrong_page_id_fails_even_when_row_count_matches(self) -> None:
        result = self.run_audit("wrong-page-id")

        self.assertEqual(result.returncode, 1)
        self.assertIn("missing page/slide unit_id(s): 2", result.stdout)
        self.assertIn("unexpected page/slide unit_id(s): 3", result.stdout)


if __name__ == "__main__":
    unittest.main()
