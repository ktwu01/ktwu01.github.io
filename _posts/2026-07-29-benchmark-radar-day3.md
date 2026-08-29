---
title: "Benchmark Radar Day 3: Linkable Rubric Dialogs and Filter Fixes"
date: 2026-07-29
permalink: /posts/2026/07/benchmark-radar-day3/
tags:
  - AI
  - Benchmarks
  - UX
  - URL Routing
---

A small day with two precise fixes that made the radar shareable.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar is live.** Track new AI benchmarks, datasets, and leaderboards every day: [open the dashboard](https://benchmark-radar.org/) or [star it on GitHub](https://github.com/ktwu01/benchmark-radar).

Hi, Koutian here. Today was quiet, but the two fixes made the tool much easier to share with other people.

The scan date filter used to snap back to the old date after you picked a new one. We fixed it so the filter stays where you put it.

The rubric dialog now opens from a URL. A rubric is the set of rules we use to score each benchmark. You can now send someone a link that lands straight on a specific rubric, which is handy in a chat or a paper. A new test guards that linking so it does not break later.

We also fixed the record expansion display, which was not rendering right, and the trend map, which now shows the full set of data instead of a slice.

Why this matters.

Linkability sounds small, but it changes how you use a tool. When you can send a URL to one benchmark's rubric, the radar becomes something you cite, not just something you visit once.

The filter fix is about trust. If you pick a date and it reverts, you stop trusting the controls. Tiny fixes like this are how trust is built.

Issues addressed:
- #48: scan date filter and rubric link
- rubric dialog linkable via URL hashtag
- record expansion state rendering
- trend map full corpus representation

Day four: history backfill, freshness banners, and the agentic taxonomy.

> Want to follow Benchmark Radar? [Star the repo on GitHub](https://github.com/ktwu01/benchmark-radar) for daily updates, or [open the live dashboard](https://benchmark-radar.org/) to explore the scans.
