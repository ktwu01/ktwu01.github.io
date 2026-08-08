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
- `scripts/check_blog.py`: regenerates derived blog data locally; runs as a check in CI.

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

GitHub Actions runs the blog linter and tests on push, and builds and deploys
the site to GitHub Pages on pushes to `main`.

## Blog Posts

Source filenames:

- English: `_posts/YYYY-MM-DD-topic-slug.md`
- Chinese: `_posts/YYYY-MM-DD-topic-slug-zh.md`

Public permalinks, where a translation pair shares one `YYYY/MM/topic-slug`
(never add `-en`, `-cn`, or `-zh` to a permalink):

- English: `/posts/YYYY/MM/topic-slug/`
- Chinese: `/zh/posts/YYYY/MM/topic-slug/`

Author notes and language navigation are generated, never hand-written. Run
this once after you finish editing posts, not once per post (each run rewrites
all of `_posts/`):

```bash
python3 scripts/check_blog.py --fix
```

Do not run the linter or tests yourself. CI runs them on push and will tell you
what to fix.

## Contact

Email: `ktwugoat@gmail.com`

---

© 2026 Koutian Wu.
