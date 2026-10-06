---
title: "Benchmark Radar Day 69: Per-Example Predictions, Not Just Scores"
date: 2026-10-03
permalink: /posts/2026/10/benchmark-radar-day69/
tags:
  - AI
  - Benchmarks
---

Day sixty-nine of Benchmark Radar. The daily scan published 577 records and recommended 174, led by an updated retinal benchmark audit that publishes image-level manifests and per-image predictions. Scoreboard: 275 stars, 45 forks.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar is live.** Track new AI benchmarks, datasets, and leaderboards every day: [open the dashboard](https://benchmark-radar.org/) or [star it on GitHub](https://github.com/ktwu01/benchmark-radar). Read the paper: [arXiv:2609.11115](https://arxiv.org/abs/2609.11115). Query the data: [Hugging Face dataset](https://huggingface.co/datasets/ktwu01/benchmark-radar).

The run fetched 1,318 items, kept 577, and recommended 174.

The updated retinal benchmark audit provides image-level manifests for patient-grouped, source-matched, and leave-one-source-out evaluations, plus per-image predictions and adjudication of 335 possible cross-label duplicates.

The Jeff/Gemma4 multimodal package evaluates six complete checkpoints under frozen designs. It publishes per-example predictions, confidence and calibration measurements, graphics-processing-unit latency and memory, and paired drift after quantization lowers numerical precision.

The transformation-based Object Constraint Language benchmark changes model representations through deterministic, meaning-preserving operations such as identifier renaming and association reification. It tests whether performance survives a change of representation while the requested constraint keeps the same meaning.

Why this matters.

A published prediction per example lets a reader recompute the headline number and look at the cases behind it.

Issues addressed

- daily snapshot: 1,318 fetched, 577 published, 174 recommended
- scoreboard: 275 of 1,000 stars, 45 forks

Day seventy: the scan continues, with the scoreboard at 275 stars.

> Want to follow Benchmark Radar? [Star the repo on GitHub](https://github.com/ktwu01/benchmark-radar) for daily updates, or [open the live dashboard](https://benchmark-radar.org/) to explore the scans. Read the paper: [arXiv:2609.11115](https://arxiv.org/abs/2609.11115).
