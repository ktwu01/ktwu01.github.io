import subprocess
import sys
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
LINTER = REPO_ROOT / "scripts" / "lint_blog_format.py"
FIXTURES = REPO_ROOT / "tests" / "fixtures"


class ChinesePermalinkLintTests(unittest.TestCase):
    def run_linter(self, fixture_name):
        return subprocess.run(
            [sys.executable, str(LINTER)],
            cwd=FIXTURES / fixture_name,
            capture_output=True,
            text=True,
            check=False,
        )

    def test_rejects_cn_filename_without_chinese_permalink(self):
        result = self.run_linter("cn_permalink_without_language_marker")

        self.assertNotEqual(result.returncode, 0)
        self.assertIn(
            "-cn.md post must use a /zh/ permalink",
            result.stdout,
        )

    def test_accepts_zh_permalink(self):
        result = self.run_linter("cn_permalink_valid")

        self.assertEqual(result.returncode, 0, result.stdout)

    def test_rejects_legacy_cn_suffix_permalink(self):
        result = self.run_linter("cn_permalink_legacy_suffix")

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("-cn.md post must use a /zh/ permalink", result.stdout)


if __name__ == "__main__":
    unittest.main()
