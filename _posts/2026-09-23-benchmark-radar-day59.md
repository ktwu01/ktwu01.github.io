---
title: "Benchmark Radar Day 59: Hidden Duplicates and Agents That Collide"
date: 2026-09-23
permalink: /posts/2026/09/benchmark-radar-day59/
tags:
  - AI
  - Benchmarks
  - Coding Agents
  - Chemistry
---

Day fifty-nine of Benchmark Radar. The daily scan published 510 records and recommended 211, led by a molecular audit that finds hidden duplicates across train and test splits and a benchmark for coding agents whose patches break when merged. Scoreboard: 249 stars, 41 forks.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar is live.** Track new AI benchmarks, datasets, and leaderboards every day: [open the dashboard](https://benchmark-radar.org/) or [star it on GitHub](https://github.com/ktwu01/benchmark-radar). Read the paper: [arXiv:2609.11115](https://arxiv.org/abs/2609.11115). Query the data: [Hugging Face dataset](https://huggingface.co/datasets/ktwu01/benchmark-radar).

The run fetched 1,177 items, kept 510, and recommended 211.

A new audit of B3DB, a blood-brain barrier dataset, shows that common 2D molecular formats map different 3D arrangements (stereoisomers) to the same input. Molecules that look separate in the split can be effective duplicates, inflating test scores. The audit compares standard deduplication with representation-aware curation across 7,807 records.

"Trains but Doesn't Learn" introduces a ten-stage benchmark for agents that fine-tune and deliver models under a budget, human approval, and reproducibility rules, aimed at runs where training loss falls but the model does not improve.

The stale benchmark tests each of two coding agents' patches alone and then merged, counting failures caused only by the combination.

Why this matters.

All three expose a score that looks fine and is not: a test set that secretly overlaps training data, a falling loss that hides a model that did not improve, two passing patches that fail together. Catching that gap is what a benchmark is for.

Issues addressed

- daily snapshot: 1,177 fetched, 510 published, 211 recommended
- ingest health: OpenReview, Semantic Scholar, and Brave returned errors; the other sources carried the run
- scoreboard: 249 of 1,000 stars, 41 forks

Day sixty: the scoreboard crosses 250 stars.

> Want to follow Benchmark Radar? [Star the repo on GitHub](https://github.com/ktwu01/benchmark-radar) for daily updates, or [open the live dashboard](https://benchmark-radar.org/) to explore the scans. Read the paper: [arXiv:2609.11115](https://arxiv.org/abs/2609.11115).
