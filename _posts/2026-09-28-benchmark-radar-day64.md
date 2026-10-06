---
title: "Benchmark Radar Day 64: Finance Agents and Leaked Group Labels"
date: 2026-09-28
permalink: /posts/2026/09/benchmark-radar-day64/
tags:
  - AI
  - Benchmarks
---

Day sixty-four of Benchmark Radar. The daily scan published 505 records and recommended 233, led by the Finance Agents Benchmark, which packages financial due diligence as an end-to-end agent test. Scoreboard: 264 stars, 42 forks.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar is live.** Track new AI benchmarks, datasets, and leaderboards every day: [open the dashboard](https://benchmark-radar.org/) or [star it on GitHub](https://github.com/ktwu01/benchmark-radar). Read the paper: [arXiv:2609.11115](https://arxiv.org/abs/2609.11115). Query the data: [Hugging Face dataset](https://huggingface.co/datasets/ktwu01/benchmark-radar).

The run fetched 1,266 items, kept 505, and recommended 233.

The Finance Agents Benchmark packages financial due diligence as 50 tasks, 160 documents, 231 grading criteria, an execution harness, and a shared synthetic company data room. A companion release provides 600 complete runs with traces, answers, criterion-level verdicts, and judge explanations.

A study of two-stage recommenders finds that fixed-candidate evaluation, which gives every ranking model the same retrieved items, selected a different top pipeline from end-to-end evaluation in eight of ten benchmark instances. End-to-end evaluation tests each ranker on the candidates produced by its own retrieval stage.

A new audit reports cross-interaction leakage in three ephemeral group-recommendation benchmarks. Held-out group-item labels were already present in every corresponding member's individual interaction history, and they made up as much as 23.4% of individual interactions.

Why this matters.

If the evaluation hands every model the same candidates, it may crown a different winner than the system people actually deploy.

Issues addressed

- daily snapshot: 1,266 fetched, 505 published, 233 recommended
- scoreboard: 264 of 1,000 stars, 42 forks

Day sixty-five: the scan continues, with the scoreboard at 264 stars and 42 forks.

> Want to follow Benchmark Radar? [Star the repo on GitHub](https://github.com/ktwu01/benchmark-radar) for daily updates, or [open the live dashboard](https://benchmark-radar.org/) to explore the scans. Read the paper: [arXiv:2609.11115](https://arxiv.org/abs/2609.11115).
