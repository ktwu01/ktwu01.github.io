---
title: "Benchmark Radar Day 48: Reader-First Dashboard — Homepage, Benchmark Pages, and Plain-English Scores"
date: 2026-09-12
permalink: /posts/2026/09/benchmark-radar-day48/
tags:
  - AI
  - Benchmarks
  - UX
  - SEO
  - Documentation
  - Plain English
---

Day forty-eight of Benchmark Radar. The dashboard gets a reader-first pass: the homepage banner keeps its words but drops its pixels, benchmark pages answer what readers actually search for, and an About page tells the project's story on the site. Scoreboard: 185 stars, 30 forks.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar is live.** Track new AI benchmarks, datasets, and leaderboards every day: [open the dashboard](https://benchmark-radar.org/) or [star it on GitHub](https://github.com/ktwu01/benchmark-radar). Read the paper: [arXiv:2609.11115](https://arxiv.org/abs/2609.11115).

The About page lands and the citation page becomes Publications, the label researchers actually look for. The path stays `/cite/`, so existing links keep working while the menu speaks the reader's word.

Benchmark pages stop being stubs. Each page now names the artifacts the benchmark has and adds sections in the reader's own words: what it is, artifact links, scores on record, citing sources, and sibling benchmarks in the same capability. Sections with no data are dropped, so a page never promises an artifact the catalog does not hold.

The homepage banner shrinks to a visually hidden heading: screen readers and crawlers still get the subject, while readers see results one screen earlier. The menu bar drops the circled info marks, moves Blog and About to the footer, and keeps the tool row for tools. The priority score shows three signals instead of five: the number, the bar, and the rubric link.

Daily briefs say the day once. The hero no longer repeats the eyebrow, the date line, the fixed tag row, and a clipped lede above the full text. Blog cards become a title plus what the day found, with the kind pill and date column gone.

PR #618 puts the paper citation inside every query payload (`data.citation` with APA, BibTeX, and the cite key) and into `site/llms.txt`, with tests tying all five BibTeX surfaces to `citation.py`. PR #619 adds a model-card SOP (scores move with cards, agents self-identify) and splits AGENTS.md into reference guides. PR #621 marks the name as Benchmark Radar™ with a contributors copyright line.

Why this matters.

Searchers type a benchmark name plus paper, dataset, code, leaderboard, or results. Pages built around those words meet the query where it starts. The About page gives arrivals from search a place to learn why the project exists, with links back into the catalog so it never dead-ends.

Issues addressed

- #606: relative first-party feed links resolved against the feed URL
- #609: structured-data warning fixed, benchmark pages dated individually
- #612: Publications aliases consolidate onto /cite/, sitemap lastmod covered
- #618: paper citation inside query payload and llms.txt
- #619: model-card SOP, AGENTS.md split into reference guides
- #621: Benchmark Radar™ name and contributors copyright line
- scoreboard: 185 of 1,000 stars, 30 forks

Day forty-nine: the README names who uses the radar, with a researchers-by-institution strip and a fresh WeChat group code.

> Want to follow Benchmark Radar? [Star the repo on GitHub](https://github.com/ktwu01/benchmark-radar) for daily updates, or [open the live dashboard](https://benchmark-radar.org/) to explore the scans. Read the paper: [arXiv:2609.11115](https://arxiv.org/abs/2609.11115).
