---
title: "Benchmark Radar Day 67: The Date in the System Prompt Moves the Score"
date: 2026-10-01
permalink: /posts/2026/10/benchmark-radar-day67/
tags:
  - AI
  - Benchmarks
---

Day sixty-seven of Benchmark Radar. The daily scan published 688 records and recommended 289, led by "Dating the Model," a study showing that a hidden current-date line changes measured performance. Scoreboard: 268 stars, 45 forks.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar is live.** Track new AI benchmarks, datasets, and leaderboards every day: [open the dashboard](https://benchmark-radar.org/) or [star it on GitHub](https://github.com/ktwu01/benchmark-radar). Read the paper: [arXiv:2609.11115](https://arxiv.org/abs/2609.11115). Query the data: [Hugging Face dataset](https://huggingface.co/datasets/ktwu01/benchmark-radar).

The run fetched 1,490 items, kept 688, and recommended 289.

"Dating the Model" reports that hidden current-date text injected into system prompts changed measured performance across nine large language models and six datasets, with shifts of up to 14% on mathematics tasks. Model rankings changed as well, while the user prompts stayed otherwise identical.

EngramBench is built around capability overlap without solution overlap: its learning and test tasks require related skills but avoid highly similar solutions. It has 30 learning tasks and 13 unseen tasks, meant to separate reusable skill development from copying earlier code.

Argus benchmarks confidence estimates for computer-use agents that turn vision-language model predictions into graphical interface clicks. It compares 27 methods across four open-weight agents and four datasets, plus eight methods across three closed-source vendors.

Why this matters.

Two models compared on different dates, under different hidden prompts, may not be compared at all.

Issues addressed

- daily snapshot: 1,490 fetched, 688 published, 289 recommended
- scoreboard: 268 of 1,000 stars, 45 forks

Day sixty-eight: the scan continues, with the scoreboard at 268 stars and 45 forks.

> Want to follow Benchmark Radar? [Star the repo on GitHub](https://github.com/ktwu01/benchmark-radar) for daily updates, or [open the live dashboard](https://benchmark-radar.org/) to explore the scans. Read the paper: [arXiv:2609.11115](https://arxiv.org/abs/2609.11115).
