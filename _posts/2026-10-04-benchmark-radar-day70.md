---
title: "Benchmark Radar Day 70: Random Splits Overstate Performance"
date: 2026-10-04
permalink: /posts/2026/10/benchmark-radar-day70/
tags:
  - AI
  - Benchmarks
---

Day seventy of Benchmark Radar. The daily scan published 484 records and recommended 127, led by the 2026 Cryo-EM Benchmark Dataset, 12 protein structures deposited after every disclosed test set for MICA. Scoreboard: 278 stars, 45 forks.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar is live.** Track new AI benchmarks, datasets, and leaderboards every day: [open the dashboard](https://benchmark-radar.org/) or [star it on GitHub](https://github.com/ktwu01/benchmark-radar). Read the paper: [arXiv:2609.11115](https://arxiv.org/abs/2609.11115). Query the data: [Hugging Face dataset](https://huggingface.co/datasets/ktwu01/benchmark-radar).

The run fetched 1,213 items, kept 484, and recommended 127.

The 2026 Cryo-EM Benchmark Dataset provides 12 protein structures deposited after every test set disclosed for MICA, an artificial intelligence system that builds atomic models from cryogenic electron microscopy maps. The authors also screened the structures against MICA's disclosed training set at a 25% sequence-identity threshold.

Two releases show how random record-level splits can overstate performance when related observations cross between training and testing. The clearest case finds that a 1,030-record concrete-strength benchmark contains only 427 distinct mixtures, and 76.1% of its records share composition with another record.

The Presentation-Invariant Supplier Selection Benchmark changes only the order of supplier rows while holding the decision-relevant information constant. It combines six scenarios, four levels of conflict between objectives, three balanced orderings, and three open-weight language models, for 216 calls.

Why this matters.

A benchmark with 1,030 records and 427 distinct mixtures has fewer independent test cases than its size suggests. A random split counts the same mixture on both sides.

Issues addressed

- daily snapshot: 1,213 fetched, 484 published, 127 recommended
- scoreboard: 278 of 1,000 stars, 45 forks

Day seventy-one: the scan continues, with the scoreboard at 278 stars.

> Want to follow Benchmark Radar? [Star the repo on GitHub](https://github.com/ktwu01/benchmark-radar) for daily updates, or [open the live dashboard](https://benchmark-radar.org/) to explore the scans. Read the paper: [arXiv:2609.11115](https://arxiv.org/abs/2609.11115).
