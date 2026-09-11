---
title: "Benchmark Radar Day 42: The Recent-Releases Ranking Reaches the Dashboard"
date: 2026-09-06
permalink: /posts/2026/09/benchmark-radar-day42/
tags:
  - AI
  - Benchmarks
  - Ranking
  - Dashboard
  - UI
  - Plain English
---

Day forty-two of Benchmark Radar. The ranking engine for recent releases moves from backend to the dashboard, and the daily radar snapshot captures the first full week of ranked cohorts. Scoreboard: 165 stars, 29 forks.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar is live.** Track new AI benchmarks, datasets, and leaderboards every day: [open the dashboard](https://benchmark-radar.org/) or [star it on GitHub](https://github.com/ktwu01/benchmark-radar).

A cohort is a set of releases grouped by when they were published. A window is the span of days a release must land in to count. The ranking engine evaluates seven-, thirty-, and ninety-day windows with the data contract validated at ingest.

PR #531 phase two wires the ranking engine into the dashboard. The Today page now shows a ranked feed of recent releases grouped by cohort window, with each entry displaying its benchmark identity, normalized score, test protocol, and evidence link. Releases without enough durable signal show a `limited_signals` badge instead of a rank number. The seven-day cohort updates daily, the thirty-day cohort weekly, and the ninety-day cohort monthly.

PR #562 adds a protocol column to the ranked feed so readers can see exactly which measurement rules produced each score. PR #563 fixes a hydration mismatch where the cohort label rendered differently on server and client. PR #556 (from Day 41) brought the sunblaze-ucb organization into the discovery registry, and today's scan picked up their first benchmark.

Why this matters.

A ranking that lives only in a database is a promise. Putting it on the dashboard makes the rules visible: readers can see which cohort a release belongs to, which protocol measured its score, and whether it earned a rank or a `limited_signals` label.

The cohort structure turns a flat list into a timeline. A benchmark that appeared in the seven-day window but not the thirty-day window tells a different story than one that persists across all three.

Issues addressed

- #530: data contract and ranking engine for recent releases, phase two (dashboard integration)
- #562: protocol column in ranked feed
- #563: hydration fix for cohort labels
- scoreboard: 165 of 1,000 stars, 29 forks

Day forty-three: paper preparation intensifies — source counts, figure data, and the audit pipeline freeze for the arXiv submission.

> Want to follow Benchmark Radar? [Star the repo on GitHub](https://github.com/ktwu01/benchmark-radar) for daily updates, or [open the live dashboard](https://benchmark-radar.org/) to explore the scans.