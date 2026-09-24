---
title: "Benchmark Radar Day 60: 250 Stars, and a Benchmark You Cannot Memorize"
date: 2026-09-24
permalink: /posts/2026/09/benchmark-radar-day60/
tags:
  - AI
  - Benchmarks
  - Milestone
---

Day sixty of Benchmark Radar. Benchmark Radar reaches 250 stars on day sixty. The daily scan published 471 records and recommended 199, led by Uncheatable Eval, which scores models on text published after they were trained. Scoreboard: 250 stars, 41 forks.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar is live.** Track new AI benchmarks, datasets, and leaderboards every day: [open the dashboard](https://benchmark-radar.org/) or [star it on GitHub](https://github.com/ktwu01/benchmark-radar). Read the paper: [arXiv:2609.11115](https://arxiv.org/abs/2609.11115). Query the data: [Hugging Face dataset](https://huggingface.co/datasets/ktwu01/benchmark-radar).

The run fetched 1,055 items, kept 471, and recommended 199.

Uncheatable Eval measures how well base language models compress freshly collected text. Because the test material is refreshed on a schedule, it limits the chance that a model saw the answers during training.

ElecVQA-Bench controls six evaluation choices when comparing vision-language models with vision-only models on power-line defect inspection. Once input resolution is matched, a reported 20.53-point lead for the vision-language model becomes a 0.57-point lead for the vision-only model.

SWE-Flux tests whether coding models can predict what real code does at runtime, across 480 cases from 12 Python repositories, with answers taken from instrumented test runs rather than from another model's judgment.

Why this matters.

A 20-point gap that shrinks to half a point once the inputs match is the reason this radar reads the methods section. Sixty days in, 250 people have starred a tool built to catch exactly that.

Issues addressed

- daily snapshot: 1,055 fetched, 471 published, 199 recommended
- scoreboard: 250 of 1,000 stars, 41 forks

Day sixty-one: the daily radar keeps scanning: new benchmarks, fresh scores, and a growing database.

> Want to follow Benchmark Radar? [Star the repo on GitHub](https://github.com/ktwu01/benchmark-radar) for daily updates, or [open the live dashboard](https://benchmark-radar.org/) to explore the scans. Read the paper: [arXiv:2609.11115](https://arxiv.org/abs/2609.11115).
