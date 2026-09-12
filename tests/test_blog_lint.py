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

    def test_forbidden_phrase_flagged_in_prose(self):
        hits = BLOG_LINT.check_forbidden_phrases("\u8bf4\u7684\u662f A \u800c\u4e0d\u662f B\u3002")

        self.assertEqual(len(hits), 1)
        self.assertEqual(hits[0][1], "\u800c\u4e0d\u662f")
        self.assertIn("AI slop", hits[0][2])

    def test_all_negation_variants_flagged(self):
        variants = [
            "\u8bf4\u7684\u662f A \u800c\u4e0d\u662f B\u3002",
            "\u57fa\u4e8e\u76f4\u89c9\u800c\u975e\u6570\u636e\u3002",
            "\u771f\u6b63\u7684\u74f6\u9888\u4e0d\u662f\u65f6\u95f4\uff0c\u800c\u662f\u6ce8\u610f\u529b\u3002",
            "\u90a3\u4e0d\u662f\u9053\u6b49\uff0c\u662f\u901a\u544a\u3002",
            "\u8fd9\u4e0d\u662f\u66b4\u529b\u7edf\u8ba1\u800c\u662f\u63a8\u7406\u3002",
        ]
        for text in variants:
            with self.subTest(text=text):
                self.assertTrue(BLOG_LINT.check_forbidden_phrases(text))

    def test_cross_clause_negation_is_not_flagged(self):
        """"\u4e0d\u662f X \u662f Y" spanning two clauses is ordinary prose."""
        for text in [
            "\u4ed6\u95ee\u7684\u4e0d\u662f\u8fd9\u4e2a\u9886\u57df\u662f\u4ec0\u4e48\u3002",
            "\u8fd9\u4e0d\u662f\u6211\u60f3\u8981\u7684\u7ed3\u679c\u3002",
        ]:
            with self.subTest(text=text):
                self.assertEqual(BLOG_LINT.check_forbidden_phrases(text), [])

    def test_throat_clearing_flagged_only_at_opening_positions(self):
        body = (
            "---\ntitle: 'x'\n---\n"
            "\u5148\u8bf4\u7ed3\u8bba\uff1a\u8fd9\u662f\u91cd\u70b9\u3002\n\n"
            "## \u5c0f\u8282\n\n"
            "\u8bf4\u4e00\u4ef6\u771f\u4e8b\u3002\n"
        )
        lines = [hit[0] for hit in BLOG_LINT.check_forbidden_phrases(body)]

        self.assertEqual(lines, [4, 8])

    def test_throat_clearing_ignored_mid_paragraph(self):
        text = "\u7b2c\u4e00\u53e5\u6b63\u5e38\u3002\n\u7b80\u5355\u8bf4\u8fd9\u6ca1\u95ee\u9898\u3002"

        self.assertEqual(BLOG_LINT.check_forbidden_phrases(text), [])

    def test_forbidden_phrase_ignored_inside_code_fence(self):
        fenced = "```\ngrep \u800c\u4e0d\u662f file\n```"

        self.assertEqual(BLOG_LINT.check_forbidden_phrases(fenced), [])

    def test_forbidden_phrase_policy_is_prospective(self):
        post = (
            "---\ntitle: 'x'\npermalink: /zh/posts/2026/09/x/\n---\n"
            "\u8bf4\u7684\u662f A \u800c\u4e0d\u662f B\u3002\n"
        )
        start = BLOG_LINT.POSITIVE_PHRASING_POLICY_START

        self.assertTrue(BLOG_LINT.follows_positive_phrasing_policy(f"{start}-x-zh.md"))
        self.assertFalse(BLOG_LINT.follows_positive_phrasing_policy("2026-01-01-x-zh.md"))

        flagged = BLOG_LINT.check_file_content(post, f"_posts/{start}-x-zh.md")
        legacy = BLOG_LINT.check_file_content(post, "_posts/2026-01-01-x-zh.md")

        self.assertTrue(any("AI slop" in issue for issue in flagged))
        self.assertFalse(any("AI slop" in issue for issue in legacy))


if __name__ == "__main__":
    unittest.main()
