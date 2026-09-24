---
title: "Benchmark Radar Day 57: A Run That Refused to Publish"
date: 2026-09-21
permalink: /posts/2026/09/benchmark-radar-day57/
tags:
  - AI
  - Benchmarks
  - Data Quality
---

Day fifty-seven of Benchmark Radar. The daily run failed on purpose. A safety check found 16 records sharing one description and refused to publish them. Scoreboard: 238 stars, 41 forks.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar is live.** Track new AI benchmarks, datasets, and leaderboards every day: [open the dashboard](https://benchmark-radar.org/) or [star it on GitHub](https://github.com/ktwu01/benchmark-radar). Read the paper: [arXiv:2609.11115](https://arxiv.org/abs/2609.11115). Query the data: [Hugging Face dataset](https://huggingface.co/datasets/ktwu01/benchmark-radar).

The pipeline has a rule: if several records carry the exact same summary, that text is probably a template, so the run stops before publishing it.

Today's trigger came from Zenodo, a research archive that mints a separate record and DOI for every file an uploader deposits. One depositor was archiving a single dataset one file per record, all with the same description. The deduplication step keys on titles, DOIs, and URLs, which were all distinct, so the copies reached the publish stage, and the guard caught them.

No snapshot was recorded for the day. Contribution scores and the contributors image were refreshed.

Why this matters.

A missing day is visible and fixable. Sixteen near-identical findings published as sixteen discoveries would have been neither. The guard traded one day of output for the integrity of every day after it.

Issues addressed

- daily run: stopped by the repeated-description guard (fixed on Day 58 in #680)
- contribution scores and contributors image refreshed
- scoreboard: 238 of 1,000 stars, 41 forks

Day fifty-eight: the root causes get fixed, and the guard stays exactly as strict.

> Want to follow Benchmark Radar? [Star the repo on GitHub](https://github.com/ktwu01/benchmark-radar) for daily updates, or [open the live dashboard](https://benchmark-radar.org/) to explore the scans. Read the paper: [arXiv:2609.11115](https://arxiv.org/abs/2609.11115).
