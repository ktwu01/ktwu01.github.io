import importlib.util
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPT = REPO_ROOT / "scripts" / "generate_language_links.py"


def load_module():
    spec = importlib.util.spec_from_file_location("language_links", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class LanguageLinkTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.module = load_module()
        cls.Post = cls.module.Post

    def post(self, name, permalink):
        return self.Post(Path(name), permalink)

    def test_builds_links_in_both_directions(self):
        posts = [
            self.post("2026-07-19-topic.md", "/posts/2026/07/topic/"),
            self.post("2026-07-19-topic-cn.md", "/zh/posts/2026/07/topic/"),
        ]

        links = self.module.build_language_links(posts)

        self.assertEqual(
            links["/posts/2026/07/topic/"]["variants"],
            [
                {
                    "language": "zh",
                    "label": "中文",
                    "url": "/zh/posts/2026/07/topic/",
                }
            ],
        )
        self.assertEqual(
            links["/zh/posts/2026/07/topic/"]["variants"],
            [
                {
                    "language": "en",
                    "label": "English",
                    "url": "/posts/2026/07/topic/",
                }
            ],
        )

    def test_monolingual_post_has_no_generated_entry(self):
        posts = [self.post("2026-07-19-topic.md", "/posts/2026/07/topic/")]

        self.assertEqual(self.module.build_language_links(posts), {})

    def test_rejects_day_segment_and_public_language_suffix(self):
        day_path = self.module.validate_post_url(
            Path("2026-07-19-topic.md"), "/posts/2026/07/19/topic/"
        )
        suffix = self.module.validate_post_url(
            Path("2026-07-19-topic-cn.md"), "/zh/posts/2026/07/topic-cn/"
        )

        self.assertTrue(any("canonical" in issue for issue in day_path))
        self.assertTrue(any("language suffix" in issue for issue in suffix))

    def test_rejects_chinese_source_marker_outside_zh(self):
        issues = self.module.validate_post_url(
            Path("2026-07-19-topic-cn.md"), "/posts/2026/07/topic/"
        )

        self.assertTrue(any("must use a /zh/" in issue for issue in issues))

    def test_rejects_filename_date_mismatch_and_invalid_month(self):
        mismatch = self.module.validate_post_url(
            Path("2026-07-19-topic.md"), "/posts/2025/07/topic/"
        )
        month = self.module.validate_post_url(
            Path("2026-07-19-topic.md"), "/posts/2026/13/topic/"
        )

        self.assertTrue(any("date" in issue for issue in mismatch))
        self.assertTrue(any("month" in issue for issue in month))

    def test_rejects_duplicate_language_variant(self):
        posts = [
            self.post("2026-07-19-one.md", "/posts/2026/07/topic/"),
            self.post("2026-07-19-two.md", "/posts/2026/07/topic/"),
        ]

        issues = self.module.validate_posts(posts)

        self.assertTrue(any("duplicate en variant" in issue for issue in issues))

    def test_rejects_filename_pair_with_mismatched_public_slugs(self):
        posts = [
            self.post("2026-07-19-topic.md", "/posts/2026/07/topic/"),
            self.post(
                "2026-07-19-topic-cn.md", "/zh/posts/2026/07/different-topic/"
            ),
        ]

        issues = self.module.validate_posts(posts)

        self.assertTrue(any("mismatched bilingual paths" in issue for issue in issues))

    def test_json_is_deterministic(self):
        posts = [
            self.post("2026-07-19-topic.md", "/posts/2026/07/topic/"),
            self.post("2026-07-19-topic-cn.md", "/zh/posts/2026/07/topic/"),
        ]

        forward = self.module.render_json(
            self.module.build_language_links(posts)
        )
        reverse = self.module.render_json(
            self.module.build_language_links(list(reversed(posts)))
        )

        self.assertEqual(forward, reverse)
        self.assertTrue(forward.endswith("\n"))

    def test_check_mode_rejects_stale_output(self):
        with tempfile.TemporaryDirectory() as root:
            root_path = Path(root)
            posts_dir = root_path / "_posts"
            posts_dir.mkdir()
            for name, permalink in (
                ("2026-07-19-topic.md", "/posts/2026/07/topic/"),
                ("2026-07-19-topic-cn.md", "/zh/posts/2026/07/topic/"),
            ):
                (posts_dir / name).write_text(
                    f"---\npermalink: {permalink}\n---\nBody\n", encoding="utf-8"
                )
            output = root_path / "language_links.json"
            output.write_text("{}\n", encoding="utf-8")

            result = subprocess.run(
                [
                    sys.executable,
                    str(SCRIPT),
                    "--check",
                    "--posts-dir",
                    str(posts_dir),
                    "--output",
                    str(output),
                ],
                capture_output=True,
                text=True,
                check=False,
            )

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("stale", result.stdout.lower())


if __name__ == "__main__":
    unittest.main()
