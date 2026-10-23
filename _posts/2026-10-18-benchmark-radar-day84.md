---
title: "Benchmark Radar Day 84: What Does Each Correct Answer Cost?"
date: 2026-10-18
permalink: /posts/2026/10/benchmark-radar-day84/
tags:
  - AI
  - Benchmarks
---

Day 84 of Benchmark Radar. The scan fetched 1,233 items, published 488, and marked 165 as recommended.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar is live.** [Open the dashboard](https://benchmark-radar.org/), [star the repository](https://github.com/ktwu01/benchmark-radar), or read the [paper](https://arxiv.org/abs/2609.11115). The [Hugging Face dataset](https://huggingface.co/datasets/ktwu01/benchmark-radar) provides the data.

Cost Per Correct ranks agents by dollars spent per correct answer. Its version 1.0 contains five easy tasks with deterministic regular-expression checks. The small task set supports a narrow cost comparison; it does not establish performance on complex agent work. [Cost Per Correct: benchmark tasks for cost-per-correct-answer evaluation of LLM agents](https://doi.org/10.5281/zenodo.23439614).

Accuracy-Matched Is Not Cost-Matched measures served GPU time per solved problem for a 4-bit quantized reasoning model. On the reported setup, longer outputs consumed 41–47% of per-token savings under memory-constrained load, compared with 6% at batch size one. Serving conditions change the cost calculation. [Accuracy-Matched Is Not Cost-Matched: Pricing INT4 Reasoning Deployments by Served GPU Time per Solved Problem](https://zenodo.org/records/23448613).

## Why this matters

Compare cost per completed task on the intended workload. Token prices, answer length, and concurrency all contribute to the bill.

## Scan coverage

This is a keyword-filtered discovery feed, not a representative survey of AI research. The archived briefing used 126 of 488 captured evidence records. These findings summarize its cited releases; discovery dates do not necessarily equal original publication dates.

Data and briefing: [2026-10-18 archived snapshot](https://github.com/ktwu01/benchmark-radar/blob/2f75b7a07c6f233bcbcb461631befc2b118be584/data/snapshots/2026-10-18.json).
