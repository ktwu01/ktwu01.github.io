---
title: "Benchmark Radar Day 68: Video Tests Without the Video"
date: 2026-10-02
permalink: /posts/2026/10/benchmark-radar-day68/
tags:
  - AI
  - Benchmarks
---

Day sixty-eight of Benchmark Radar. The daily scan published 668 records and recommended 244, led by Video-Index, a meta-benchmark that audits whether video tests require video understanding. Scoreboard: 272 stars, 45 forks.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar is live.** Track new AI benchmarks, datasets, and leaderboards every day: [open the dashboard](https://benchmark-radar.org/) or [star it on GitHub](https://github.com/ktwu01/benchmark-radar). Read the paper: [arXiv:2609.11115](https://arxiv.org/abs/2609.11115). Query the data: [Hugging Face dataset](https://huggingface.co/datasets/ktwu01/benchmark-radar).

The run fetched 1,424 items, kept 668, and recommended 244.

Video-Index audits whether video tests actually require video understanding. Its five-level attack pyramid tests increasingly informative shortcuts. The authors report that frame-blind attackers approach full-video accuracy on 35 audited benchmarks, and that shuffled frames retain a median 96% of full accuracy.

Finding the Right Fit studies 66 agent configurations and treats the language model and its execution harness, the software that supplies tools and manages actions, as one evaluated system. It reports model-rank reversals across harnesses and tasks.

Scores That Hold, Benchmarks That Leak audits public brain-tumor magnetic resonance imaging classification corpora. It checks test independence at three levels (duplicate images, repeated patients, and acquisition sources) and measures how each kind of leakage affects reported performance.

Why this matters.

If frame-blind attackers reach near-full accuracy, the score describes the shortcut and not the video. Three audits in one day ask the same question of different fields.

Issues addressed

- daily snapshot: 1,424 fetched, 668 published, 244 recommended
- scoreboard: 272 of 1,000 stars, 45 forks

Day sixty-nine: the scan continues, with the scoreboard at 272 stars.

> Want to follow Benchmark Radar? [Star the repo on GitHub](https://github.com/ktwu01/benchmark-radar) for daily updates, or [open the live dashboard](https://benchmark-radar.org/) to explore the scans. Read the paper: [arXiv:2609.11115](https://arxiv.org/abs/2609.11115).
