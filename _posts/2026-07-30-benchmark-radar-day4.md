---
title: "Benchmark Radar Day 4: Historical Memory and Freshness Detection"
date: 2026-07-30
permalink: /posts/2026/07/benchmark-radar-day4/
tags:
  - AI
  - Benchmarks
  - History
  - Freshness
  - Agentic AI
---

The radar learned to remember. Day four added historical backfill, staleness detection, and an agentic taxonomy category.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

## What shipped

**simulate-history command.** A new CLI command backfills historical snapshots by simulating past collection runs. Four historical snapshots were generated to give the trend map actual data to display.

**Staleness banner.** The dashboard now shows a banner when data is older than expected. If the daily run fails or stalls, users see a warning instead of trusting stale numbers.

**Corpus totals by category.** The Today view now shows total distinct artifacts broken down by category (benchmarks, datasets, leaderboards, research). This gives an immediate sense of scale.

**Agentic taxonomy category.** A new "agentic" category was added to the taxonomy with matching retrieval keywords. Agent benchmarks were being classified into generic categories; now they have their own.

**Trend delta fixes.** Re-announced updates were excluded from trend deltas. A releases-only view was added. The arXiv keyword filter was tightened to focus on benchmark and dataset introductions.

**Record expansion fix.** When a record is expanded, the dashboard now shows new content instead of repeating the teaser text.

**Daily radar scheduling.** The radar was configured to run twice a day so a failed trigger gets a same-day retry.

## Why it matters

A radar without history is a daily newspaper. A radar with history is an atlas. The simulate-history command filled the gap between "we started yesterday" and "we have months of data," giving the trend map something real to show.

The staleness banner was equally important. If data is two days old, the dashboard should say so. Trust requires transparency about freshness.

The agentic taxonomy category reflected a real market shift: agent benchmarks (SWE-bench, WebArena, OSWorld) were growing fast enough to deserve their own classification.

## Issues addressed

- \#35, \#42, \#45: freshness banner, corpus totals, history backfill
- \#52: corpus totals visibility
- \#53: freshness fields
- \#55: trend delta fixes
- \#58: agentic taxonomy category

Day five: trend chart hover cards and the benchmark landscape report.
