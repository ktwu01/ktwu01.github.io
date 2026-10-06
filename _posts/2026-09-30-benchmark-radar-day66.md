---
title: "Benchmark Radar Day 66: Who Plays the User?"
date: 2026-09-30
permalink: /posts/2026/09/benchmark-radar-day66/
tags:
  - AI
  - Benchmarks
---

Day sixty-six of Benchmark Radar. The daily scan published 656 records and recommended 186, led by UserProxyBench, which tests whether the language model playing the user follows its private instructions. Scoreboard: 268 stars, 43 forks.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar is live.** Track new AI benchmarks, datasets, and leaderboards every day: [open the dashboard](https://benchmark-radar.org/) or [star it on GitHub](https://github.com/ktwu01/benchmark-radar). Read the paper: [arXiv:2609.11115](https://arxiv.org/abs/2609.11115). Query the data: [Hugging Face dataset](https://huggingface.co/datasets/ktwu01/benchmark-radar).

The run fetched 1,661 items, kept 656, and recommended 186.

UserProxyBench tests a hidden dependency in interactive agent benchmarks: whether the language model playing the user follows its private instructions. It adds a User Fidelity Score, holds the evaluated agent fixed, and varies only the simulated user across 375 enterprise tasks.

EnterpriseBench extends enterprise evaluation beyond static question answering into interactive decisions with missing information, uncertainty, feedback, and long-term trade-offs. It also reorganizes existing enterprise and financial question-answering datasets into one foundational suite.

CTE-Bench evaluates whether a coding model can predict how changing code or stored state will alter a running service several calls later. It isolates this state-tracking ability from action selection by asking for future behavior after an intervention, not for an edit.

Why this matters.

When one model plays the user, a weak simulated user can lower or raise the score of the agent under test. UserProxyBench measures that effect directly.

Issues addressed

- daily snapshot: 1,661 fetched, 656 published, 186 recommended
- scoreboard: 268 of 1,000 stars, 43 forks

Day sixty-seven: the scan continues, with the scoreboard at 268 stars.

> Want to follow Benchmark Radar? [Star the repo on GitHub](https://github.com/ktwu01/benchmark-radar) for daily updates, or [open the live dashboard](https://benchmark-radar.org/) to explore the scans. Read the paper: [arXiv:2609.11115](https://arxiv.org/abs/2609.11115).
