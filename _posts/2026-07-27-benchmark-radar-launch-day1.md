---
title: "Benchmark Radar Day 1: Building the Cumulative Dashboard MVP"
date: 2026-07-27
permalink: /posts/2026/07/benchmark-radar-launch-day1/
tags:
  - AI
  - Benchmarks
  - Open Source
  - Launch
---

Day one of Benchmark Radar. The project went from zero to a running cumulative dashboard in a single day.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

The first day covered every layer of the system: CI/CD pipeline, data persistence, the Today dashboard MVP, attention signal processing, and arXiv RSS fallback. Twenty commits landed in a single push.

## What shipped

**Infrastructure.** The GitHub Actions workflow was established with actions/checkout, upload/download-artifact, and setup-python bumped to their latest major versions. pytest was widened from `<9` to `<10` to keep pace with upstream.

**Cumulative dashboard MVP.** The core idea: persist daily snapshots outside the protected `main` branch so they accumulate over time. Each snapshot captures the full scored corpus, not just a summary.

**Attention signal fixes.** Duplicate signals were removed and detail rendering was corrected so the dashboard actually reflected what the pipeline collected.

**arXiv RSS fallback.** When the primary arXiv search endpoint fails, the system falls back to the RSS feed. This matters because arXiv search is rate-limited and unreliable at scale.

**Today dashboard.** The overview was compacted, cleaned up, and simplified. The goal was a page you could scan in thirty seconds.

## Why it matters

The hardest part of building a radar is not collecting data; it is making yesterday's data still mean something tomorrow. Persistence was the first commitment: every daily scan produces a record that future runs can compare against. Without that, the radar would forget everything overnight.

The arXiv fallback was also a foundational decision. Primary endpoints fail. RSS feeds are lower-fidelity but more resilient. Having both from day one meant the daily run would not break when arXiv rate-limited the crawler.

## Issues addressed

- \#4, \#5, \#1, \#2, \#3: dependency bumps
- \#10: cumulative radar dashboard MVP
- \#11: persist snapshots outside protected main
- \#13: attention signal details and duplicates
- \#14: compact Today overview
- \#16: clean up Today dashboard UI
- \#17: ignore local development artifacts
- \#18: simplify Today dashboard
- \#21: main snapshot source of truth
- \#22: fall back to arXiv RSS

Tomorrow: cumulative trend maps, UI cleanup, and evidence source expansion.
