---
title: "Benchmark Radar Day 58: Fix the Source, Keep the Guard"
date: 2026-09-22
permalink: /posts/2026/09/benchmark-radar-day58/
tags:
  - AI
  - Benchmarks
  - Data Quality
  - Hugging Face
---

Day fifty-eight of Benchmark Radar. Two fixes clear yesterday's stop without loosening the check that caused it: Zenodo file batches collapse to one finding, and copied Hugging Face template text no longer passes as a description. Scoreboard: 246 stars, 41 forks.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar is live.** Track new AI benchmarks, datasets, and leaderboards every day: [open the dashboard](https://benchmark-radar.org/) or [star it on GitHub](https://github.com/ktwu01/benchmark-radar). Read the paper: [arXiv:2609.11115](https://arxiv.org/abs/2609.11115). Query the data: [Hugging Face dataset](https://huggingface.co/datasets/ktwu01/benchmark-radar).

PR #680 collapses batch deposits. When one creator list and one description repeat across many Zenodo records, the radar keeps the earliest record and notes how many files it stands for. Both conditions are required: a shared description alone could merge two groups who happen to use the same words, and a shared creator list alone could merge a lab's genuinely separate deposits.

PR #679 handles a second copy problem on Hugging Face. Leaderboard templates ship a filled-in one-line description, and duplicating a template copies it verbatim, so three leaderboards were about to publish "Duplicate this leaderboard to initialize your own!" as their own description. The fix drops known template lines and, more durably, clears a one-line card that an earlier owner published first, so the next new template needs no manual list entry.

A manual rerun and the scheduled run both succeeded. The snapshot published 410 records and recommended 163, including Curation-Bench for data-selection agents, XYEval for agents that should question a user's proposed fix, and VibeMemBench for coding memory across 111 targets.

Why this matters.

The easy fix was to relax the guard. The durable fix was to teach the source stage what a copy looks like. The guard in the pipeline is untouched and still fails hard, so the next unknown copy pattern will stop the run again before it reaches readers.

Issues addressed

- #680: one finding per Zenodo batch deposit
- #679: Hugging Face template descriptions no longer published as a repo's own
- daily snapshot: 1,140 fetched, 410 published, 163 recommended
- scoreboard: 246 of 1,000 stars, 41 forks

Day fifty-nine: the daily radar keeps scanning, now with both copy patterns handled at the source.

> Want to follow Benchmark Radar? [Star the repo on GitHub](https://github.com/ktwu01/benchmark-radar) for daily updates, or [open the live dashboard](https://benchmark-radar.org/) to explore the scans. Read the paper: [arXiv:2609.11115](https://arxiv.org/abs/2609.11115).
