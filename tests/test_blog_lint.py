import importlib.util
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
LINTER = REPO_ROOT / "scripts" / "lint_blog_format.py"
AUTHOR_GENERATOR = REPO_ROOT / "scripts" / "generate_author_notes.py"
FIXTURES = REPO_ROOT / "tests" / "fixtures"

SPEC = importlib.util.spec_from_file_location("blog_lint", LINTER)
BLOG_LINT = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(BLOG_LINT)

AUTHOR_SPEC = importlib.util.spec_from_file_location(
    "author_notes", AUTHOR_GENERATOR
)
AUTHOR_NOTES = importlib.util.module_from_spec(AUTHOR_SPEC)
AUTHOR_SPEC.loader.exec_module(AUTHOR_NOTES)


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

    def test_rejects_noncanonical_chinese_permalink_before_2026(self):
        with tempfile.TemporaryDirectory() as root:
            post = Path(root) / "2024-01-01-example-cn.md"
            post.write_text(
                "---\n"
                "title: Example\n"
                "permalink: /posts/2024/01/example-cn/\n"
                "---\n"
                "A hook.\n\n"
                f"{AUTHOR_NOTES.AUTHOR_NOTES['zh']}\n",
                encoding="utf-8",
            )

            issues = BLOG_LINT.check_file(post)

        self.assertTrue(any("must use a /zh/" in issue for issue in issues))


class AuthorNoteTests(unittest.TestCase):
    def post(self, permalink, body):
        return (
            "---\n"
            "title: Example\n"
            f"permalink: {permalink}\n"
            "---\n"
            f"{body}"
        )

    def test_inserts_localized_note_after_hook(self):
        content = self.post(
            "/zh/posts/2026/07/example/",
            "这是钩子。\n\n正文。\n",
        )

        rendered = AUTHOR_NOTES.render_post(content)
        lines = AUTHOR_NOTES.logical_body_lines(rendered)

        self.assertEqual(lines[0], "这是钩子。")
        self.assertEqual(lines[1], AUTHOR_NOTES.AUTHOR_NOTES["zh"])
        self.assertEqual(lines[2], "正文。")

    def test_explicit_language_overrides_legacy_permalink(self):
        content = (
            "---\n"
            "title: Example\n"
            "lang: zh-CN\n"
            "permalink: /posts/2026/07/example/\n"
            "---\n"
            "这是钩子。\n\n正文。\n"
        )

        rendered = AUTHOR_NOTES.render_post(content)

        self.assertEqual(
            AUTHOR_NOTES.logical_body_lines(rendered)[1],
            AUTHOR_NOTES.AUTHOR_NOTES["zh"],
        )

    def test_rejects_ambiguous_chinese_body_on_legacy_permalink(self):
        chinese_body = "这是需要显式语言标记的中文正文。" * 30
        content = self.post(
            "/posts/2026/07/example/",
            f"这是钩子。\n\n{chinese_body}\n",
        )

        with self.assertRaisesRegex(ValueError, "likely Chinese content"):
            AUTHOR_NOTES.render_post(content)
        self.assertTrue(
            any(
                "Likely Chinese content" in issue
                for issue in BLOG_LINT.check_file_content(content)
            )
        )

    def test_replaces_duplicates_and_wrong_language_idempotently(self):
        english_note = AUTHOR_NOTES.AUTHOR_NOTES["en"]
        content = self.post(
            "/zh/posts/2026/07/example/",
            f"这是钩子。\n\n{english_note}\n\n正文。\n\n{english_note}\n",
        )

        rendered = AUTHOR_NOTES.render_post(content)

        self.assertEqual(
            AUTHOR_NOTES.logical_body_lines(rendered).count(
                AUTHOR_NOTES.AUTHOR_NOTES["zh"]
            ),
            1,
        )
        self.assertNotIn(english_note, rendered)
        self.assertEqual(AUTHOR_NOTES.render_post(rendered), rendered)

    def test_refuses_to_discard_trailing_author_content(self):
        canonical = AUTHOR_NOTES.AUTHOR_NOTES["en"]
        content = self.post(
            "/posts/2026/07/example/",
            f"A hook.\n\n{canonical} 290 stars\n\nBody.\n",
        )

        with self.assertRaisesRegex(ValueError, "refusing to discard"):
            AUTHOR_NOTES.render_post(content)

    def test_keeps_continued_blockquote_attached_to_note(self):
        canonical = AUTHOR_NOTES.AUTHOR_NOTES["en"]
        content = self.post(
            "/posts/2026/07/example/",
            f"A hook.\n\n{canonical}\n>\n> Project details.\n",
        )

        rendered = AUTHOR_NOTES.render_post(content)

        self.assertIn(f"{canonical}\n>\n> Project details.", rendered)
        self.assertNotIn(f"{canonical}\n\n>", rendered)
        self.assertEqual(AUTHOR_NOTES.render_post(rendered), rendered)

    def test_separates_unrelated_blockquote_after_note(self):
        canonical = AUTHOR_NOTES.AUTHOR_NOTES["en"]
        content = self.post(
            "/posts/2026/07/example/",
            f"A hook.\n\n{canonical}\n> Research metadata.\n",
        )

        rendered = AUTHOR_NOTES.render_post(content)

        self.assertIn(f"{canonical}\n\n> Research metadata.", rendered)
        self.assertEqual(AUTHOR_NOTES.render_post(rendered), rendered)

    def test_skips_front_matter_without_language_signal(self):
        content = "---\ntitle: Notes\n---\nA hook.\n"

        self.assertEqual(AUTHOR_NOTES.render_post(content), content)

    def test_preserves_disclaimer_before_hook_and_note(self):
        disclaimer = (
            "> **THIS IS A FAKE BLOG.** This content is fabricated."
        )
        content = self.post(
            "/posts/2026/07/example/",
            f"{disclaimer}\n\nA hook.\n\nBody.\n",
        )

        rendered = AUTHOR_NOTES.render_post(content)
        lines = AUTHOR_NOTES.logical_body_lines(rendered)

        self.assertEqual(
            lines,
            [
                disclaimer,
                "A hook.",
                AUTHOR_NOTES.AUTHOR_NOTES["en"],
                "Body.",
            ],
        )
        self.assertEqual(BLOG_LINT.check_file_content(rendered), [])

    def test_linter_rejects_noncanonical_or_duplicate_note(self):
        canonical = AUTHOR_NOTES.AUTHOR_NOTES["en"]
        noncanonical = canonical + " extra"
        content = self.post(
            "/posts/2026/07/example/",
            f"A hook.\n\n{noncanonical}\n\nBody.\n",
        )

        issues = BLOG_LINT.check_file_content(content)

        self.assertTrue(any("not the canonical" in issue for issue in issues))

        duplicate = self.post(
            "/posts/2026/07/example/",
            f"A hook.\n\n{canonical}\n\nBody.\n\n{canonical}\n",
        )
        issues = BLOG_LINT.check_file_content(duplicate)
        self.assertTrue(any("exactly one" in issue for issue in issues))


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
