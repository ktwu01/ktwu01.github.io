---
title: "Benchmark Radar Day 2: Cumulative Trends and Artifact Deduplication"
date: 2026-07-28
permalink: /posts/2026/07/benchmark-radar-day2/
tags:
  - AI
  - Benchmarks
  - Data Quality
  - Deduplication
---

The radar gained memory. Day two added trend maps that span time, plus a fix for benchmarks showing up under many names.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar is live.** Track new AI benchmarks, datasets, and leaderboards every day: [open the dashboard](https://ktwu01.github.io/benchmark-radar/) or [star it on GitHub](https://github.com/ktwu01/benchmark-radar).

Hi, Koutian here. Today the radar stopped being a daily snapshot and started keeping a longer story. Two changes did that.

The trend map now shows how benchmark counts move over time. Before, you only saw today. Now each kind of item (benchmarks, datasets, leaderboards, and research papers) gets its own line on the chart. You can watch the field grow instead of guessing.

The alias resolver fixes a quiet problem. The same benchmark often appears under different names across sources. The system now links those names together, so one artifact counts once. That keeps the totals honest.

We also folded the Explorer view into the main radar. There were two screens doing the same job, so we made them one. The priority scoring got retuned too, so a genuinely new benchmark is not buried under re-announced updates. The evidence pipeline now pulls from more sources, and we cleaned up some clutter on the page (the masthead, the Trends section, and the Sources panel). The Sources panel is no longer pinned, and the repo badges are now clickable links instead of plain text.

Why this matters.

A benchmark radar lives or dies on deduplication. Without it, one benchmark shows up ten times under ten names and every count is wrong. Our resolver matches on exact identifiers, not fuzzy title guesses, so it stays precise.

The trend map was the first proof this project is not just a daily scanner. It is becoming a record of how the AI benchmark world changes month to month.

Issues addressed:
- #29: radar UX and coverage fixes
- #33: resolve radar issues
- #46: resolve artifact aliases across snapshots
- duplicate detection via exact identifiers
- priority scoring recalibration

Day three: scan date filter fixes and linkable rubric dialogs.

> Want to follow Benchmark Radar? [Star the repo on GitHub](https://github.com/ktwu01/benchmark-radar) for daily updates, or [open the live dashboard](https://ktwu01.github.io/benchmark-radar/) to explore the scans.
