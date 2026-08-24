---
title: "Benchmark Radar Day 27: Paging Today, Halving a Title, and Naming 21 Benchmarks Right"
date: 2026-08-22
permalink: /posts/2026/08/benchmark-radar-day27/
tags:
  - AI
  - Benchmarks
  - Today View
  - Pagination
  - i18n
  - SEO
---

Day twenty-seven of Benchmark Radar. We made the Today list load a page at a time, cut a title in half, and taught 21 benchmarks to show their real names.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

Pagination means showing a long list in pages instead of all at once. A bootstrap payload is the small file the page loads first to appear quickly. SEO is how search engines find and describe a site.

PR #315 pages the Today list. Before, the first paint tried to render every observation, so your browser fetched and drew the whole day. Now it paints 20 cards, then watches a sentinel below the list. When you scroll near the bottom it loads the next 20 in place, so an expanded card stays open and the rank keeps counting across pages. A status line reads loaded of total, like 20 of 136, plus scroll for more. The legend was trimmed to 136 normal and 9 attention plus the sort note; the raw total that repeated the same number is gone. The export badge, its dialog, and the client-side CSV builder are gone too; requests for the full dataset now point to the contact sheet.

PR #317 gives the saturation view a left-to-right entrance. The running-best line draws itself from left to right, and each point fades up as the line passes its date. Points that still hold the best value as of their date stay fully emphasized; the others recede behind the line until you hover or focus them. Membership comes from one shared per-date best collapse, scoped to the line's own comparable group, and it only runs when a line is actually drawn. The entrance is presentational, but the emphasis rule is data-driven.

PR #319 halves the leaderboard title. It was 48px and pushed the ranking and the chart down. Now it is `clamp(1.25rem, 2vw, 1.5rem)`, about half that, so the first screen belongs to the ranking again. The blue (i) info toggle no longer floats hundreds of pixels away; the title and its toggle now sit in one flex row that wraps on narrow screens.

PR #320 adds a header row and bars to the ranking. Before, the five rows had no labels, so you had to guess that the number on the left was rank and the number on the right was count. Now a row reads Rank, Benchmark, Model cards. Each row also draws a horizontal bar sized against the largest count on screen, so the gap between GPQA Diamond at 26 and AIME at 17 is visible at a glance. The heavy bordered, all-caps SHOW ALL control was replaced with a lighter disclosure that toggles between the top 5 and all 79.

PR #321 translates the benchmark detail panel. Section headings like Identity, Publisher, Modality, Openness, Size, and Code and Data licence, plus every not established placeholder, now go through `t()` with a real `zh` entry. Before, only Released had a Chinese translation and the rest fell back to English, so the panel showed mixed languages. The panel now reads fully in Chinese when you choose Chinese.

PR #323 closes #262. Twenty-one of the 76 score-dense `llm-stats` benchmarks showed publisher not established only because the `llm-stats` API carries no provenance, yet each has an exact-name OpenCompass record in the same crawl that already holds paper, repo, dataset, publisher, and release date. Those 21 are now linked as equivalent groups in `data/external/identity.yml`, and the loader lets the `llm-stats` record display its reviewed peer's identity. The other records stay unlinked until a second anchor appears.

PR #328 fixes the bootstrap. PR #327 had replaced the first paint with a compact bootstrap payload to make the site load fast and to lazy-load the full 34MB dataset for trends and all-date views. But `dashboard_bootstrap()` also stripped `benchmark_score_progression` out of that first payload, claiming the history is only used with the full data. It is not. The leaderboard's Scores over time panel reads exactly that block, so it showed No benchmark in this registry has a score read from a document yet on every visit. Now the bootstrap ships the progression again, and `stateNeedsFullData()` still only upgrades to `radar.json` for trends, the map, and historical Today views, never for the leaderboard.

PR #327 also lands the first-load and adoption work: pagination with a durable sentinel, durable contact and rubric links, earned star and share prompts, and citation metadata with a public downstream use-case template in the docs.

PR #325 adds the mechanical SEO layer from #236. A generated `sitemap.xml` covers every indexable view, plus `robots.txt`, per-page titles and meta descriptions that differ, Open Graph and `twitter:image` tags, canonical URLs, and JSON-LD structured data as `Dataset` for the corpus and `WebSite` with `SearchAction`. No new content or query targeting was added; this is the plumbing that lets crawlers read what was already there.

Why this matters.

Paging keeps the Today view usable when a day is dense. Rendering 136 cards at once is not more informative, it is slower to become usable. Twenty at a time with a sentinel keeps your scroll position and your open card while you ask for more.

Naming 21 benchmarks right fixes the identity layer where it counts. A publisher not established badge that is only missing because one API is silent is not a gap to display, it is a link we had not drawn. Linking exact-name pairs from a second source that already holds the paper and repo lets the record speak with the right provenance.

The title, bar, and translation work is about reading without guessing. A halved title gives the first screen back to the data. Bars make a 26 versus 17 gap visible without comparing two numbers in your head. A fully translated detail panel means the language toggle actually toggles the whole page.

Issues addressed

- #311: Today list pages 20 at a time with in-place loading
- #312: saturation line draws left to right with data-driven emphasis
- #313: leaderboard title halved and its info toggle anchored
- #314: ranking gains columns, bars, and a lighter disclosure
- #316: benchmark detail panel fully translated to Chinese
- #262: 21 `llm-stats` identities resolved via OpenCompass equivalents
- #236: generated sitemap, `robots.txt`, canonicals, and structured data
- #322: bootstrap first paint with lazy full data, pagination, and citation metadata
- #328: leaderboard Scores over time restored in the bootstrap

Day twenty-eight: one source of truth for the data, and one `h1` for the page.
