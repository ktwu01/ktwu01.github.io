---
title: "Benchmark Radar Day 56: Two Community Fixes Make Records Order-Independent"
date: 2026-09-20
permalink: /posts/2026/09/benchmark-radar-day56/
tags:
  - AI
  - Benchmarks
  - Open Source
  - Contributors
---

Day fifty-six of Benchmark Radar. Contributor winklemad lands two fixes: one makes record-holder credit agree with the record chart, the other keeps every benchmark's page address unique. Scoreboard: 236 stars, 41 forks.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar is live.** Track new AI benchmarks, datasets, and leaderboards every day: [open the dashboard](https://benchmark-radar.org/) or [star it on GitHub](https://github.com/ktwu01/benchmark-radar). Read the paper: [arXiv:2609.11115](https://arxiv.org/abs/2609.11115). Query the data: [Hugging Face dataset](https://huggingface.co/datasets/ktwu01/benchmark-radar).

PR #662 fixes how a tied best score picks its record holder. The old code let the order of rows in the source file decide, so on the frontier_challenge benchmark the summary credited GPT-5.6 Sol while the record chart credited Grok 4.6 for the same 20.6 score on the same date. Ties now break the way the chart does: best value, then earliest date, then a stable ID. After the change, no shipped benchmark disagrees with itself.

PR #664 fixes the function that assigns each benchmark its short name, which is also its file name and its page address. Under rare inputs it could hand two benchmarks the same name, silently overwriting one record and taking the query tools down. The current data never triggered it; the fix closes the gap before the growing catalog does.

The technical report submodule moved to the latest paper source, contribution scores were refreshed, and the daily snapshot recorded 411 published records, 125 recommended, including a slang-aware Traditional Chinese prompt-injection benchmark and a semantic-cache test built from 131 near-duplicate question pairs.

Why this matters.

A database that credits two different models for one record loses trust on the first click. Both fixes remove a dependence on accidental ordering, so the same data always tells the same story. Both came from outside the core team.

Issues addressed

- #662: saturation record holder matches the record chart on ties
- #664: unique benchmark short names
- #672: contributor branch rule merged
- daily snapshot: 1,128 fetched, 411 published, 125 recommended
- scoreboard: 236 of 1,000 stars, 41 forks

Day fifty-seven: the daily run stops itself before publishing copied text.

> Want to follow Benchmark Radar? [Star the repo on GitHub](https://github.com/ktwu01/benchmark-radar) for daily updates, or [open the live dashboard](https://benchmark-radar.org/) to explore the scans. Read the paper: [arXiv:2609.11115](https://arxiv.org/abs/2609.11115).
