---
title: "Benchmark Radar Day 87: Task Success Does Not Establish Authorization"
date: 2026-10-21
permalink: /posts/2026/10/benchmark-radar-day87/
tags:
  - AI
  - Benchmarks
---

Day 87 of Benchmark Radar. The scan fetched 1,692 items, published 884, and marked 391 as recommended.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar is live.** [Open the dashboard](https://benchmark-radar.org/), [star the repository](https://github.com/ktwu01/benchmark-radar), or read the [paper](https://arxiv.org/abs/2609.11115). The [Hugging Face dataset](https://huggingface.co/datasets/ktwu01/benchmark-radar) provides the data.

AuthorizationBench evaluates whether an agent stays within the authority its user delegated, separately from task completion or conventional harm. Its 286 executable tasks vary situational triggers and direct consequences across ten application domains. An agent can finish a task and still act beyond its user’s authorization. [Act on Your Behalf, Beyond Your Authorization: Benchmarking LLM Agent Authorization Alignment](https://arxiv.org/abs/2610.27548).

A controlled perturbation study injects tool denial, goal changes, and tighter constraints at graded severity in two matched grids of 4,320 episodes each. Its design makes adaptation during execution observable, instead of reducing every disrupted run to one final outcome. [Benchmarking the responsiveness of LLM-based agentic systems under controlled mid-task perturbations](https://doi.org/10.1038/s41598-026-72720-7).

## Why this matters

Test what the agent may do and how it responds when conditions change. Completion rates leave both questions partly unanswered.

## Scan coverage

This is a keyword-filtered discovery feed, not a representative survey of AI research. The archived briefing used 183 of 884 captured evidence records. These findings summarize its cited releases; discovery dates do not necessarily equal original publication dates.

Data and briefing: [2026-10-21 archived snapshot](https://github.com/ktwu01/benchmark-radar/blob/2f75b7a07c6f233bcbcb461631befc2b118be584/data/snapshots/2026-10-21.json).
