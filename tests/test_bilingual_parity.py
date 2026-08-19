import importlib.util
import tempfile
import unittest
from pathlib import Path

import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

SPEC = importlib.util.spec_from_file_location(
    "check_bilingual_parity",
    Path(__file__).resolve().parents[1] / "scripts" / "check_bilingual_parity.py",
)
PARITY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(PARITY)

AUTHOR_EN = "> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)"
AUTHOR_ZH = "> 作者：[Koutian Wu](https://www.linkedin.com/in/ktwu01/)；[GitHub: ktwu01](https://github.com/ktwu01/)"


def make_pair(root, en_body, zh_body):
    en = Path(root) / "2026-01-01-example.md"
    zh = Path(root) / "2026-01-01-example-zh.md"
    en.write_text(
        "---\ntitle: Example\npermalink: /posts/2026/01/example/\n---\n"
        f"A hook.\n\n{AUTHOR_EN}\n\n{en_body}\n",
        encoding="utf-8",
    )
    zh.write_text(
        "---\ntitle: 例子\npermalink: /zh/posts/2026/01/example/\n---\n"
        f"这是钩子。\n\n{AUTHOR_ZH}\n\n{zh_body}\n",
        encoding="utf-8",
    )
    return en, zh


class StructuralParityTests(unittest.TestCase):
    def issues(self, root):
        posts, _skipped = PARITY.load_posts(Path(root))
        grouped, _stale = PARITY.pair_issues(posts, {})
        return grouped

    def test_identical_structure_passes(self):
        with tempfile.TemporaryDirectory() as root:
            body = "## Section\n\nSome text with [a link](https://example.com).\n\n"
            en, zh = make_pair(root, body, body)
            self.assertEqual(self.issues(root), {})

    def test_translated_text_is_not_compared(self):
        with tempfile.TemporaryDirectory() as root:
            en_body = (
                "## What Ships\n\nUse [the docs](https://docs.example.org).\n\n"
                "```python\nprint('hi')\n```\n"
            )
            zh_body = (
                "## 今日交付\n\n参见[文档](https://docs.example.org)。\n\n"
                "```python\nprint('hi')\n```\n"
            )
            make_pair(root, en_body, zh_body)
            self.assertEqual(self.issues(root), {})

    def test_dropped_link_is_caught(self):
        with tempfile.TemporaryDirectory() as root:
            en_body = "See [docs](https://docs.example.org) and [blog](https://blog.example.org)."
            zh_body = "参见[文档](https://docs.example.org)。"
            make_pair(root, en_body, zh_body)
            grouped = self.issues(root)
            self.assertIn("/posts/2026/01/example/", grouped)
            self.assertTrue(
                any("links" in issue and "blog.example.org" in issue
                    for issue in grouped["/posts/2026/01/example/"]["issues"])
            )

    def test_dropped_image_is_caught(self):
        with tempfile.TemporaryDirectory() as root:
            en_body = "![Chart](/images/chart.png) and text."
            zh_body = "正文。"
            make_pair(root, en_body, zh_body)
            grouped = self.issues(root)
            self.assertTrue(
                any("images" in issue
                    for issue in grouped["/posts/2026/01/example/"]["issues"])
            )

    def test_dropped_heading_is_caught(self):
        with tempfile.TemporaryDirectory() as root:
            en_body = "## One\n\ntext.\n\n## Two\n\nmore.\n"
            zh_body = "## 一\n\n正文。\n"
            make_pair(root, en_body, zh_body)
            grouped = self.issues(root)
            self.assertTrue(
                any("headings" in issue
                    for issue in grouped["/posts/2026/01/example/"]["issues"])
            )

    def test_dropped_equation_is_caught(self):
        with tempfile.TemporaryDirectory() as root:
            en_body = "Text $$E=mc^2$$ more $$a=b$$."
            zh_body = "正文 $$E=mc^2$$。"
            make_pair(root, en_body, zh_body)
            grouped = self.issues(root)
            self.assertTrue(
                any("math" in issue
                    for issue in grouped["/posts/2026/01/example/"]["issues"])
            )

    def test_dropped_table_is_caught(self):
        with tempfile.TemporaryDirectory() as root:
            en_body = "|A|B|\n|---|---|\n|1|2|\n"
            zh_body = "|A|B|\n|---|---|\n"
            make_pair(root, en_body, zh_body)
            grouped = self.issues(root)
            self.assertTrue(
                any("tables" in issue
                    for issue in grouped["/posts/2026/01/example/"]["issues"])
            )

    def test_dropped_code_fence_is_caught(self):
        with tempfile.TemporaryDirectory() as root:
            en_body = "```bash\necho hi\n```\n"
            zh_body = "正文。\n"
            make_pair(root, en_body, zh_body)
            grouped = self.issues(root)
            self.assertTrue(
                any("code" in issue
                    for issue in grouped["/posts/2026/01/example/"]["issues"])
            )

    def test_favicon_link_cards_resolve_to_target_domain(self):
        with tempfile.TemporaryDirectory() as root:
            card = (
                "[\n\n![](https://t0.gstatic.com/faviconV2?url=https://example.org/&client=BARD"
                "&type=FAVICON&size=256)\n\nOpens in a new window](https://example.org/doc)"
            )
            en_body = "See [the doc](https://example.org/doc)."
            zh_body = f"参见{card}。"
            make_pair(root, en_body, zh_body)
            self.assertEqual(self.issues(root), {})

    def test_lamda_decorative_image_is_ignored(self):
        with tempfile.TemporaryDirectory() as root:
            en_body = "Text."
            zh_body = (
                "正文。\n\n"
                "![logo](https://www.gstatic.com/lamda/images/immersives/"
                "google_logo_icon_2380fba942c84387f09cf.svg)\n"
            )
            make_pair(root, en_body, zh_body)
            self.assertEqual(self.issues(root), {})

    def test_baseline_allows_listed_issue_type(self):
        with tempfile.TemporaryDirectory() as root:
            en_body = "Text."
            zh_body = "正文。[link](https://extra.example.org)。"
            make_pair(root, en_body, zh_body)
            posts, _skipped = PARITY.load_posts(Path(root))
            baseline = {"/posts/2026/01/example/": ["links"]}
            grouped, stale = PARITY.pair_issues(posts, baseline)
            self.assertEqual(grouped, {})
            self.assertEqual(stale, [])

    def test_stale_baseline_entry_is_reported(self):
        with tempfile.TemporaryDirectory() as root:
            en_body = "Text."
            zh_body = "正文。"
            make_pair(root, en_body, zh_body)
            posts, _skipped = PARITY.load_posts(Path(root))
            baseline = {"/posts/2026/01/example/": ["links"]}
            grouped, stale = PARITY.pair_issues(posts, baseline)
            self.assertEqual(grouped, {})
            self.assertEqual(stale, ["/posts/2026/01/example/"])

    def test_baseline_does_not_cover_other_issue_types(self):
        with tempfile.TemporaryDirectory() as root:
            en_body = "## One\n\n## Two\n\nText."
            zh_body = "## 一\n\n正文。\n\n[link](https://extra.example.org)。"
            make_pair(root, en_body, zh_body)
            posts, _skipped = PARITY.load_posts(Path(root))
            baseline = {"/posts/2026/01/example/": ["links"]}
            grouped, _stale = PARITY.pair_issues(posts, baseline)
            issues = grouped["/posts/2026/01/example/"]["issues"]
            self.assertTrue(any("headings" in issue for issue in issues))
            self.assertFalse(any("links" in issue for issue in issues))


if __name__ == "__main__":
    unittest.main()