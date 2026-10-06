---
title: "Benchmark Radar Day 61: Partial Credit That Rewards Fake Progress"
date: 2026-09-25
permalink: /posts/2026/09/benchmark-radar-day61/
tags:
  - AI
  - Benchmarks
---

Day sixty-one of Benchmark Radar. The daily scan published 450 records and recommended 198, led by PartHackBench, which tests whether partial-credit scorers reward misleading progress in long-running tool agents. Scoreboard: 252 stars, 41 forks.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar is live.** Track new AI benchmarks, datasets, and leaderboards every day: [open the dashboard](https://benchmark-radar.org/) or [star it on GitHub](https://github.com/ktwu01/benchmark-radar). Read the paper: [arXiv:2609.11115](https://arxiv.org/abs/2609.11115). Query the data: [Hugging Face dataset](https://huggingface.co/datasets/ktwu01/benchmark-radar).

The run fetched 1,128 items, kept 450, and recommended 198.

PartHackBench compares honest and adversarial trajectories only after a private certifier establishes that both have equal current-state progress and equal agent attribution. That isolates score inflation from genuine task advancement.

DynBench generates fresh Knowledge Graph Question Answering datasets automatically as the underlying knowledge changes, which addresses static-test obsolescence and possible memorization. BRIE does the same for clinical records, so refreshable evaluation shows up twice in one day.

SWE-Prometheus extends coding-agent evaluation beyond fixing a supplied issue. An agent receives a repository snapshot and an open-ended governance objective, then has to identify risks, prioritize interventions, and verify its changes.

Why this matters.

A partial-credit score is only useful if it moves when the work moves. PartHackBench measures whether it moves for the wrong reasons.

Issues addressed

- daily snapshot: 1,128 fetched, 450 published, 198 recommended
- scoreboard: 252 of 1,000 stars, 41 forks

Day sixty-two: the scan continues, with the scoreboard at 252 stars.

> Want to follow Benchmark Radar? [Star the repo on GitHub](https://github.com/ktwu01/benchmark-radar) for daily updates, or [open the live dashboard](https://benchmark-radar.org/) to explore the scans. Read the paper: [arXiv:2609.11115](https://arxiv.org/abs/2609.11115).
