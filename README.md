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

## Living Monet theme

The site uses a procedural, animated water-garden background adapted from the
Tacite `/test11` concept. It draws brush marks directly in WebGL; there is no
painting image, video download, or additional runtime dependency. Existing
content, typography, navigation, media, and page layouts are preserved.

`assets/css/monet.css` owns the shared palette and reading surfaces, including
the existing dark theme. `assets/js/monet/index.js` initializes the decorative
canvas supplied by `_includes/monet-background.html`. Both shared layouts use
it; standalone reports, slide decks, and the talk map also include the theme,
with their surface overrides in `assets/css/monet-standalone.css`.

The painting pauses in hidden tabs, becomes still with reduced motion enabled,
and uses fewer brush marks on phones. A CSS color field remains when JavaScript
or WebGL is unavailable. Print layouts hide the background.

## Media Coverage

**All listings in `/media/` (`_pages/media.md`) are the source of truth for media coverage.** Preserve the complete archive, including press, video, and other mentions, when changing the homepage presentation. Add or update coverage there first.

The homepage is a curated view of the `featured_media` front matter in that same file, rendered by `_includes/home-media.html`. Its coverflow presentation lives in `assets/css/home-media.css` and `assets/js/home-media.js`; it must not replace or remove archive listings. Keep each highlight consistent with its archive entry.

The image-led coverflow styling and motion are adapted from [AmberLJC’s news deck](https://github.com/AmberLJC/AmberLJC.github.io/commit/6e229f2fb045ba154b46190b62b018b383e50ec4), including its screenshot panels, floating outlet badges, 3D positioning, arrow controls, pagination dots, and automatic sliding. Local adaptations add theme colors, an explicit pause button, and reduced-motion support. Screenshots, publisher images, and outlet marks are stored in `images/media/`; their source links and descriptions remain in `_pages/media.md`.

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
