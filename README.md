# Koutian Wu

This repository hosts the source for my personal academic website:

https://koutian.is-a.dev

The site is built with Jekyll and the [Academic Pages template](https://github.com/academicpages/academicpages.github.io).

## Site Structure

- `_pages/`: top-level website pages.
- `_posts/`: blog posts and essays.
- `_portfolio/`: portfolio/project entries.
- `_publications/`: publication entries.
- `_talks/`: talk entries.
- `images/`: site images and portfolio assets.
- `scripts/lint_blog_format.py`: blog-post format linter used by CI.

Standalone demos and one-off HTML artifacts should not live at the repository root. Put them in dedicated static repos and link to their GitHub Pages URLs instead.

Current standalone pages:

- [Claude Code Demo](https://koutian.is-a.dev/claude-code-demo/) -> [`ktwu01/claude-code-demo`](https://github.com/ktwu01/claude-code-demo)
- [ESM Leaderboard](https://koutian.is-a.dev/esm-leaderboard/) -> [`ktwu01/esm-leaderboard`](https://github.com/ktwu01/esm-leaderboard)
- [JCJ AI Comms Demo](https://koutian.is-a.dev/jcj-ai-comms-demo/) -> [`ktwu01/jcj-ai-comms-demo`](https://github.com/ktwu01/jcj-ai-comms-demo)
- [Rain Window](https://koutian.is-a.dev/rain-window/) -> [`ktwu01/rain-window`](https://github.com/ktwu01/rain-window)

## Local Development

Install Ruby and Bundler, then run:

```bash
git clone https://github.com/ktwu01/ktwu01.github.io.git
cd ktwu01.github.io
bundle install
bundle exec jekyll serve
```

Open `http://localhost:4000`.

Run the blog linter before pushing post changes:

```bash
python3 scripts/lint_blog_format.py
```

GitHub Actions builds and deploys the site to GitHub Pages on pushes to `main`.

## Contact

Email: `ktwugoat@gmail.com`

---

© 2026 Koutian Wu.
