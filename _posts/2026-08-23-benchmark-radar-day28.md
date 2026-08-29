---
title: "Benchmark Radar Day 28: One Source of Truth, One H1, and a Citation You Can Copy"
date: 2026-08-23
permalink: /posts/2026/08/benchmark-radar-day28/
tags:
  - AI
  - Benchmarks
  - Data Plumbing
  - i18n
  - SEO
  - Citation
---

Day twenty-eight of Benchmark Radar. We removed a second copy of the data, made the page say one thing to crawlers, and gave the work a citable name.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar is live.** Track new AI benchmarks, datasets, and leaderboards every day: [open the dashboard](https://benchmark-radar.org/) or [star it on GitHub](https://github.com/ktwu01/benchmark-radar).

A source of truth is the one file you regenerate from, instead of keeping two copies that can drift. `h1` is the page's main heading; crawlers expect exactly one. `i18n` means internationalization, showing the interface in another language. A citation is the reference you paste into a paper to credit the work.

PR #337 removes the derived shards. `site/data/benchmark-index.json` and 1,148 files in `site/data/benchmarks/` are produced by `benchmark-radar normalize-external` from the committed crawl CSVs, `data/leaderboard_snapshots.yml`, and `data/external/identity.yml`. They were committed as well, so the repo carried two versions of the same catalog. Regenerating on `main` rewrote 50 shards that had already drifted. Now they are gitignored and built in CI. A fresh checkout builds them before anything that reads them, and the model registry refuses to write if the shards are missing. Copying the data is no longer copying the truth.

PR #329 polishes the docs. Both READMEs move the language switch to the top-right above the title and use a plain label, `[中文](README.zh-CN.md)` and `[English](README.md)`, instead of a filename-style link. Both gain an Acknowledgements section crediting `llm-stats` as the frontier-score data source, because the AIME 2025 chart is built on `llm-stats.com` data. Both gain a BibTeX block at the end, `Wu 2026`, pointing at `CITATION.cff` for machine-readable metadata. The homepage's support card now mentions citing the work, and a Cite button lives in the header so the reference is one click away.

PR #331 adds 26 missing `zh` entries and fixes SEO. Every `t()` call site was audited against the `zh` dictionary; zero misses remain. The misses covered `not scored`, `not recorded`, related-record labels, benchmark-detail loading and error strings, saturation bound text, the adoption-ranking explainer, badge tooltips, pagination, and the star, fork, and issue badges. For SEO, the page now has a single `h1`, Today's radar. The leaderboard, map, trends, and error-state headings are now `h2` with the same visual style. Crawlers used to see four competing `h1` titles across hidden views. `og:title` now matches the document title, and internal links were fixed so the analyzer score rose to 85.

PR #335 updates citation metadata to `v0.8.0`. `CITATION.cff` moves from `v0.3.0` to `v0.8.0` and records the release date.

PR #331 and PR #337 also changed the plumbing order in CI. `benchmark-radar classify` and the shard generation now run earlier, so a derived asset never reads a stale input. That matches how a reader already uses the site: the small bootstrap first, the full dataset only when needed.

Why this matters.

A repo with two copies of the same catalog will drift by construction, and it just did, by 50 shards. The fix is not to commit more carefully, it is to commit only the source, the crawl CSVs and the identity files, and to generate the rest on every checkout and every CI run. One source of truth means a rebuild from `main` says the same thing as the last publish.

One `h1` and consistent `og:title` means crawlers hear one title for the page, not four. A page that shows one view at a time should also declare one heading at a time. The same logic applies to translations: 26 remaining English strings under the Chinese locale means the language toggle pretended to switch but left pieces behind. Filling them makes the toggle do what its label says.

A citable reference turns use into credit. The `llm-stats` acknowledgement gives credit where the scores came from, and the `CITATION.cff` plus BibTeX plus header Cite button gives credit where the radar itself is reused.

Issues addressed

- #329: README language links top-right, `llm-stats` acknowledgement, BibTeX and homepage Cite button
- #331: 26 missing `zh` entries, single `h1`, matching `og:title`, internal links, analyzer score 85
- `v0.8.0` citation metadata in `CITATION.cff`
- derived `site/data/benchmarks/` shards untracked, generated in CI, built before consumers
- shard generation and classification ordered before reads in CI

Day twenty-nine: releases before updates, scores on a 0 to 100 scale, and a nav state you can see.

> Want to follow Benchmark Radar? [Star the repo on GitHub](https://github.com/ktwu01/benchmark-radar) for daily updates, or [open the live dashboard](https://benchmark-radar.org/) to explore the scans.
