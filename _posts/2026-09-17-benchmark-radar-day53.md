---
title: "Benchmark Radar Day 53: Word Senses, Stablecoins, and Ride-Hailing Agents"
date: 2026-09-17
permalink: /posts/2026/09/benchmark-radar-day53/
tags:
  - AI
  - Benchmarks
  - Daily Snapshot
---

Day fifty-three of Benchmark Radar. The daily scan published 666 records and recommended 261 of them, led by a corrected word-sense benchmark, a stablecoin stress arena, and a ride-hailing agent test. Scoreboard: 229 stars, 36 forks.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar is live.** Track new AI benchmarks, datasets, and leaderboards every day: [open the dashboard](https://benchmark-radar.org/) or [star it on GitHub](https://github.com/ktwu01/benchmark-radar). Read the paper: [arXiv:2609.11115](https://arxiv.org/abs/2609.11115). Query the data: [Hugging Face dataset](https://huggingface.co/datasets/ktwu01/benchmark-radar).

The run fetched 1,467 items across sources, kept 666 after deduplication and scoring, and flagged 261 as recommended.

lexEN replaces disputed word-sense labels with a human-adjudicated correction layer: 211 labels changed and 56 removed. Its SenseBench harness exposes item-level results across 57 models and 192 runs.

StableEval Arena asks agents to diagnose stablecoin stress and forecast departures from a one-dollar price over a hidden seven-day horizon, using historical replay that keeps future information out of the test.

RideWay scores ride-hailing agents on efficiency only after they finish the task, discounting successful runs for extra tool calls and extra turns with the user.

Why this matters.

A benchmark that fixes its own labels, a test that blocks future leakage, and a score that charges for wasted steps: all three keep the test's own flaws out of the score. That is the kind of release the radar exists to surface.

Issues addressed

- daily snapshot: 1,467 fetched, 666 published, 261 recommended
- scoreboard: 229 of 1,000 stars, 36 forks

Day fifty-four: more fresh benchmarks, including a benchmark that catches coding agents claiming work they did not finish.

> Want to follow Benchmark Radar? [Star the repo on GitHub](https://github.com/ktwu01/benchmark-radar) for daily updates, or [open the live dashboard](https://benchmark-radar.org/) to explore the scans. Read the paper: [arXiv:2609.11115](https://arxiv.org/abs/2609.11115).
