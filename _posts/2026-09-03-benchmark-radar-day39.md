---
title: "Benchmark Radar Day 39: The Daily Brief Gets a Home"
date: 2026-09-03
permalink: /posts/2026/09/benchmark-radar-day39/
tags:
  - AI
  - Benchmarks
  - Blog
  - Open Source
  - Data
  - Plain English
---

Day thirty-nine of Benchmark Radar. The daily brief now has a landing page, a full archive, and a feed of its own, and the dashboard navigation got short enough to scan. Scoreboard: 144 stars, 27 forks.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar is live.** Track new AI benchmarks, datasets, and leaderboards every day: [open the dashboard](https://benchmark-radar.org/) or [star it on GitHub](https://github.com/ktwu01/benchmark-radar).

A landing page is the first page of a section. An archive is the complete set of past pages. A feed is a machine-readable list readers subscribe to. A chrome is the shared header, navigation, and footer that appears around every page.

PR #521 publishes the blog at `/blog/`. Each collection day gets a page, the newest thirty appear on the landing page, the archive lists every day, and a separate feed serves subscribers. Three kinds of day are labelled: a daily brief when a briefing was stored, a no-material-change note when nothing moved enough, and an evidence summary for the early snapshots written before briefings existed. Nothing here calls a model or the network, so a rebuild is byte-identical.

PR #525 simplifies the dashboard chrome. The menu now reads Today, CLI, Leaderboard, Trends; Explore and Rubric are hidden from the menu bar but stay published at their own URLs, and the header keeps the star count while dropping the fork and issue bubbles.

PR #519 reduces the CLI setup to one command, `npx skills add ktwu01/benchmark-radar`. The second step a reader used to copy and relay is gone, and the Skill now owns setup end to end, checking the CLI, repairing it if needed, and reporting what it ran.

PR #526 extracts the blog chrome from the same source as the dashboard, so blog pages carry the same navigation, language toggle, and badges, and an untranslated English body stays visible when the chrome switches to Chinese.

Why this matters.

The most readable thing the project produces is now also the most reachable thing. A daily record with a landing page, an archive, and a feed is a record search engines can crawl and readers can subscribe to, without a model call in the build.

A quieter dashboard is a faster decision. Fewer menu items and fewer badge numbers leave the eye on the data, and the hidden routes keep working for the people who already know them.

Issues addressed

- daily brief blog at `/blog/` with archive and RSS feed
- #512: dashboard navigation and badges simplified
- #519: CLI setup reduced to one install command
- #526: blog pages match the dashboard chrome
- scoreboard: 144 of 1,000 stars, 27 forks

Day forty: a publishing network most radars ignore, and a benchmark brought back by its exact name.

> Want to follow Benchmark Radar? [Star the repo on GitHub](https://github.com/ktwu01/benchmark-radar) for daily updates, or [open the live dashboard](https://benchmark-radar.org/) to explore the scans. Read the paper: [arXiv:2609.11115](https://arxiv.org/abs/2609.11115).