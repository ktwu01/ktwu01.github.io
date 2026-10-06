---
title: "Benchmark Radar Day 63: A Quiet Sunday and a Scorer Fix"
date: 2026-09-27
permalink: /posts/2026/09/benchmark-radar-day63/
tags:
  - AI
  - Benchmarks
---

Day sixty-three of Benchmark Radar. The daily scan published 314 records and recommended 106, led by the Kalyvox Voice Benchmark 2026, which scores one voice agent across 240 controlled calls. Scoreboard: 257 stars, 41 forks.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar is live.** Track new AI benchmarks, datasets, and leaderboards every day: [open the dashboard](https://benchmark-radar.org/) or [star it on GitHub](https://github.com/ktwu01/benchmark-radar). Read the paper: [arXiv:2609.11115](https://arxiv.org/abs/2609.11115). Query the data: [Hugging Face dataset](https://huggingface.co/datasets/ktwu01/benchmark-radar).

The run fetched 1,006 items, kept 314, and recommended 106.

The Kalyvox Voice Benchmark 2026 evaluates one voice agent through 240 controlled French and English calls across 12 scenario families. It reports interaction-level measures: response latency, intent accuracy, task completion, call transfer, appointment booking, and fallback handling, rather than relying on transcript quality.

The updated full-text extraction pipeline keeps its original frozen scorer and adds an aligned scorer that corrects three identified defects, including comparisons of temperatures reported in kelvin without conversion. The archive also retains provenance spans that link each extracted value to its source text.

The agent-eval-platform runs each support-agent trial in an isolated Kubernetes job, measures pass^k reliability (whether repeated attempts produce a success), and injects failures to test recovery on the tau-bench banking task.

Why this matters.

The scorer fix shows the cost of a frozen metric: three defects stayed in the numbers until a second scorer was added beside the first.

Issues addressed

- daily snapshot: 1,006 fetched, 314 published, 106 recommended
- scoreboard: 257 of 1,000 stars, 41 forks

Day sixty-four: the weekday scan resumes.

> Want to follow Benchmark Radar? [Star the repo on GitHub](https://github.com/ktwu01/benchmark-radar) for daily updates, or [open the live dashboard](https://benchmark-radar.org/) to explore the scans. Read the paper: [arXiv:2609.11115](https://arxiv.org/abs/2609.11115).
