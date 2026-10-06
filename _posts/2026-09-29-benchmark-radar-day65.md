---
title: "Benchmark Radar Day 65: Benchmarks From Deployment Traces"
date: 2026-09-29
permalink: /posts/2026/09/benchmark-radar-day65/
tags:
  - AI
  - Benchmarks
---

Day sixty-five of Benchmark Radar. The daily scan published 758 records and recommended 381, led by TraceDance, which turns real agent deployment traces into benchmarks for undesirable behavior. Scoreboard: 266 stars, 43 forks.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar is live.** Track new AI benchmarks, datasets, and leaderboards every day: [open the dashboard](https://benchmark-radar.org/) or [star it on GitHub](https://github.com/ktwu01/benchmark-radar). Read the paper: [arXiv:2609.11115](https://arxiv.org/abs/2609.11115). Query the data: [Hugging Face dataset](https://huggingface.co/datasets/ktwu01/benchmark-radar).

The run fetched 1,423 items, kept 758, and recommended 381.

TraceDance turns real agent deployment traces into targeted benchmarks for user-specified undesirable behaviors. It evaluates the model's next action from a recorded decision point, so a completed task is not treated as enough evidence that the behavior was acceptable.

Certified Selective Automation of LLM Agent Evaluation determines what fraction of trajectory reviews an automatic judge can handle while keeping its error rate within a stated budget. It accounts for correlated results from several agents attempting the same tasks, where the usual independent-sample assumptions fail.

WebPageBench verifies web-agent task completion from typed interface event logs instead of model judges or page scraping. It can rerender the same task with one user-interface control changed while preserving the prompt and the success conditions.

Why this matters.

The scan published 758 records, the highest count in this run of days. Most of them need the same question asked: what does the score count as success?

Issues addressed

- daily snapshot: 1,423 fetched, 758 published, 381 recommended
- scoreboard: 266 of 1,000 stars, 43 forks

Day sixty-six: the scan continues, with the scoreboard at 266 stars and 43 forks.

> Want to follow Benchmark Radar? [Star the repo on GitHub](https://github.com/ktwu01/benchmark-radar) for daily updates, or [open the live dashboard](https://benchmark-radar.org/) to explore the scans. Read the paper: [arXiv:2609.11115](https://arxiv.org/abs/2609.11115).
