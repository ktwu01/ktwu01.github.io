import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
INCLUDE = REPO_ROOT / "_includes" / "language-switcher.html"
LAYOUT = REPO_ROOT / "_layouts" / "single.html"
PAGE_STYLES = REPO_ROOT / "_sass" / "layout" / "_page.scss"
JEKYLL_CONFIG = REPO_ROOT / "_config.yml"


class LanguageSwitcherTemplateTests(unittest.TestCase):
    def test_include_renders_accessible_language_variants(self):
        template = INCLUDE.read_text(encoding="utf-8")

        self.assertIn("site.data.language_links[page.url]", template)
        self.assertIn('aria-label="Language versions"', template)
        self.assertIn("language_entry.variants", template)
        self.assertIn("variant.url | relative_url", template)
        self.assertIn('hreflang="{{ variant.language }}"', template)
        self.assertIn("{{ variant.label }}", template)

    def test_layout_places_switcher_before_article_body(self):
        layout = LAYOUT.read_text(encoding="utf-8")

        include_position = layout.index("{% include language-switcher.html %}")
        content_position = layout.index("{{ content }}")
        self.assertLess(include_position, content_position)

    def test_page_styles_include_language_switcher(self):
        styles = PAGE_STYLES.read_text(encoding="utf-8")

        self.assertIn(".page__language-switcher", styles)

    def test_jekyll_excludes_linter_fixture_posts(self):
        config = JEKYLL_CONFIG.read_text(encoding="utf-8")

        self.assertRegex(config, r"(?m)^  - tests$")


if __name__ == "__main__":
    unittest.main()
