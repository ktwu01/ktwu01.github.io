---
title: "Benchmark Radar Day 6: Hacker News Integration and Scheduled Reliability"
date: 2026-08-01
permalink: /posts/2026/08/benchmark-radar-day6/
tags:
  - AI
  - Benchmarks
  - Hacker News
  - Reliability
  - RSS
---

The radar now watches Hacker News. Day six added community attention signals and hardened the daily schedule.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar is live.** Track new AI benchmarks, datasets, and leaderboards every day: [open the dashboard](https://ktwu01.github.io/benchmark-radar/) or [star it on GitHub](https://github.com/ktwu01/benchmark-radar).

Hi, Koutian here. Today the radar started listening to what practitioners talk about, not just what researchers publish.

The radar now pulls benchmark discussions from Hacker News (HN, a big tech news site). When a benchmark gets discussed there, it means working engineers are paying attention, not just academics. That is our first community-sourced signal.

The HN collector keeps its output bounded. One viral thread cannot flood the daily snapshot. We also made the arXiv RSS feed tougher: entries with broken metadata are skipped instead of crashing the pipeline. On weekends and holidays, arXiv often returns nothing, so the radar now finishes cleanly on an empty day instead of failing.

PR #75 fixed reliability in the scheduled workflow, including fallback handling and error recovery. We added the landscape report figures to the docs and bumped the GitHub App token action from 2.2.2 to 3.2.0.

Why this matters.

Hacker News is where people discuss what they actually use. Adding HN let the radar catch a benchmark gaining real-world traction, not just citations. It is the first time the system listens to the community.

The arXiv hardening matters just as much. A daily run that dies on a quiet Sunday is a run you stop trusting. Surviving empty days and bad RSS means the schedule can run on its own.

Issues addressed:
- #70: GitHub App token bump
- #71: landscape report figures
- #73: hide duplicate report tables
- #75: scheduled radar reliability
- #76: Hacker News collector integration
- arXiv RSS document filtering
- empty arXiv day handling

Day seven: model card adoption leaderboard and registry expansion.

> Want to follow Benchmark Radar? [Star the repo on GitHub](https://github.com/ktwu01/benchmark-radar) for daily updates, or [open the live dashboard](https://ktwu01.github.io/benchmark-radar/) to explore the scans.
