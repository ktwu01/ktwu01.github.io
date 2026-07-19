import importlib.util
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
LINTER = REPO_ROOT / "scripts" / "lint_blog_format.py"
FIXTURES = REPO_ROOT / "tests" / "fixtures"

SPEC = importlib.util.spec_from_file_location("blog_lint", LINTER)
BLOG_LINT = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(BLOG_LINT)


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


class LocalImageLintTests(unittest.TestCase):
    def test_accepts_existing_root_relative_jpeg(self):
        with tempfile.TemporaryDirectory() as root:
            image = Path(root) / "images" / "example.jpeg"
            image.parent.mkdir()
            image.write_bytes(b"\xff\xd8\xff\xe0valid-jpeg-test")

            issues = BLOG_LINT.check_local_images(
                "![Example](/images/example.jpeg)", root
            )

        self.assertEqual(issues, [])

    def test_rejects_missing_or_relative_local_image(self):
        with tempfile.TemporaryDirectory() as root:
            missing = BLOG_LINT.check_local_images(
                "![Missing](/images/missing.png)", root
            )
            relative = BLOG_LINT.check_local_images(
                "![Relative](images/example.png)", root
            )

        self.assertIn("Local image does not exist", missing[0])
        self.assertIn("must start with /images/", relative[0])

    def test_rejects_corrupt_jpeg(self):
        with tempfile.TemporaryDirectory() as root:
            image = Path(root) / "images" / "corrupt.jpeg"
            image.parent.mkdir()
            image.write_bytes(b"not-a-jpeg")

            issues = BLOG_LINT.check_local_images(
                "![Corrupt](/images/corrupt.jpeg)", root
            )

        self.assertIn("does not match its extension", issues[0])


if __name__ == "__main__":
    unittest.main()
