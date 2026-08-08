import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
MASTHEAD = REPO_ROOT / "_includes" / "masthead.html"
NAVIGATION_STYLES = REPO_ROOT / "_sass" / "layout" / "_navigation.scss"


class MastheadIssueButtonTests(unittest.TestCase):
    def test_issue_button_links_to_the_new_issue_form(self):
        template = MASTHEAD.read_text(encoding="utf-8")

        self.assertIn(
            'href="https://github.com/ktwu01/ktwu01.github.io/issues/new"',
            template,
        )
        self.assertIn('target="_blank"', template)
        self.assertIn('rel="noopener noreferrer"', template)
        self.assertIn(
            'aria-label="Report an issue on GitHub (opens in a new tab)"',
            template,
        )

    def test_issue_button_sits_next_to_the_theme_toggle_and_can_overflow(self):
        template = MASTHEAD.read_text(encoding="utf-8")

        issue_position = template.index('masthead__menu-item masthead__issue-link"')
        theme_position = template.index('id="theme-toggle"')
        self.assertLess(issue_position, theme_position)
        self.assertNotIn("masthead__issue-link persist", template)

    def test_issue_button_has_compact_navigation_styles(self):
        styles = NAVIGATION_STYLES.read_text(encoding="utf-8")

        self.assertIn(".masthead__issue-link", styles)
        self.assertIn("display: inline-flex;", styles)
        self.assertIn(
            "border-color: var(--global-masthead-link-color-hover);",
            styles,
        )
        self.assertIn("@media (max-width: $small)", styles)
        self.assertRegex(
            styles,
            r"(?s)@media \(max-width: \$small\).*?span\s*\{\s*display: none;",
        )


if __name__ == "__main__":
    unittest.main()
