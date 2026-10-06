---
title: "Benchmark Radar Day 71: Passing the Test You Trained On"
date: 2026-10-05
permalink: /posts/2026/10/benchmark-radar-day71/
tags:
  - AI
  - Benchmarks
---

Day seventy-one of Benchmark Radar. The daily scan published 560 records and recommended 273, led by "Passing the Test You Trained On," a study of 15 prompt-injection detectors. Scoreboard: 279 stars, 45 forks.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar is live.** Track new AI benchmarks, datasets, and leaderboards every day: [open the dashboard](https://benchmark-radar.org/) or [star it on GitHub](https://github.com/ktwu01/benchmark-radar). Read the paper: [arXiv:2609.11115](https://arxiv.org/abs/2609.11115). Query the data: [Hugging Face dataset](https://huggingface.co/datasets/ktwu01/benchmark-radar).

The run fetched 1,275 items, kept 560, and recommended 273.

"Passing the Test You Trained On" evaluates 15 prompt-injection detectors on benign and injected outputs reconstructed from real agent benchmark tool calls. Detector rankings transferred poorly across benchmarks: the best detector on the public BIPIA benchmark caught only 2% of AgentDojo injections at the study's setting.

The milipoint-runs release rebuilds a radar dataset's evaluation splits after finding that shuffled, overlapping windows let most test examples share frames with training examples. Holding out complete recording runs reduced the reported PointMLP identification accuracy from about 94% to 37 to 39%.

OpenGameEval runs programming agents in reproducible, stateful Roblox Studio sessions. It scores executable checks on both the edited scene and simulated play, and it separates observation tools from editing tools so exploration behavior can be measured apart from final task completion.

Why this matters.

A detector that tops one benchmark and catches 2% on another has learned the benchmark. The day's second study, 94% falling to 37 to 39%, points the same way.

Issues addressed

- daily snapshot: 1,275 fetched, 560 published, 273 recommended
- scoreboard: 279 of 1,000 stars, 45 forks

Day seventy-two: the scan continues, with the scoreboard at 279 stars and 45 forks.

> Want to follow Benchmark Radar? [Star the repo on GitHub](https://github.com/ktwu01/benchmark-radar) for daily updates, or [open the live dashboard](https://benchmark-radar.org/) to explore the scans. Read the paper: [arXiv:2609.11115](https://arxiv.org/abs/2609.11115).
