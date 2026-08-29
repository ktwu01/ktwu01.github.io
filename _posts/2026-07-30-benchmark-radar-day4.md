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

**Benchmark Radar is live.** Track new AI benchmarks, datasets, and leaderboards every day: [open the dashboard](https://benchmark-radar.org/) or [star it on GitHub](https://github.com/ktwu01/benchmark-radar).

Hi, Koutian here. Today the radar got a memory and a way to tell you when its data is stale.

We added a command called `simulate-history`. It backfills old snapshots by replaying past collection runs. We generated four historical snapshots so the trend map finally has real history to draw.

The dashboard now shows a banner when the data is older than expected. If the daily run fails or stalls, you see a warning instead of trusting numbers that are two days old.

The Today view now shows total distinct artifacts split by category (benchmarks, datasets, leaderboards, research). You get a sense of scale the moment you open it.

We added an "agentic" category to the taxonomy. Agent benchmarks (think SWE-bench, WebArena, OSWorld) were being lumped into generic buckets. Now they have their own home, with matching search keywords.

A few smaller fixes: re-announced updates no longer distort the trend deltas, we added a releases-only view, and we tightened the arXiv keyword filter to focus on new benchmark and dataset announcements. When you expand a record, it now shows fresh content instead of repeating the teaser. The radar now runs twice a day, so a failed trigger gets a retry the same day.

Why this matters.

A radar without history is a daily newspaper. A radar with history is an atlas you can flip through. The simulate-history command bridged "we started yesterday" and "we have months of data," giving the trend map something real.

The staleness banner matters just as much. If the data is two days old, the dashboard should say so out loud. Trust needs honesty about freshness.

The agentic category tracks a real shift: agent benchmarks are growing fast enough to deserve their own label.

Issues addressed:
- #35, #42, #45: freshness banner, corpus totals, history backfill
- #52: corpus totals visibility
- #53: freshness fields
- #55: trend delta fixes
- #58: agentic taxonomy category

Day five: trend chart hover cards and the benchmark landscape report.

> Want to follow Benchmark Radar? [Star the repo on GitHub](https://github.com/ktwu01/benchmark-radar) for daily updates, or [open the live dashboard](https://benchmark-radar.org/) to explore the scans.
