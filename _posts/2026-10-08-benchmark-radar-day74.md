---
title: "Benchmark Radar Day 74: Safety Monitors Need Better Event Logs"
date: 2026-10-08
permalink: /posts/2026/10/benchmark-radar-day74/
tags:
  - AI
  - Benchmarks
---

Day 74 of Benchmark Radar. The scan fetched 1,326 items, published 604, and marked 274 as recommended.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar is live.** [Open the dashboard](https://benchmark-radar.org/), [star the repository](https://github.com/ktwu01/benchmark-radar), or read the [paper](https://arxiv.org/abs/2609.11115). The [Hugging Face dataset](https://huggingface.co/datasets/ktwu01/benchmark-radar) provides the data.

A runtime-verification study replayed AgentDojo and STAC trajectories through formal rules. It detected about 70% of successful attacks, but also flagged 29.3% of benign runs. The authors link this imprecision to traces that rarely record approvals and never record timestamps. Those missing fields limit what a monitor can infer. [Formal Runtime Verification for Tool-Using LLM Agents: An Offline Same-Benchmark Study on AgentDojo and STAC](https://doi.org/10.48550/arxiv.2610.09793).

Coding-Agent Benchmarks Should Match Their Users’ Task Flows compares issue-derived tasks with 4,782 real coding-agent sessions. Sessions with at least three user messages include changes between asking questions, planning, review, refactoring, and execution. Isolated issue resolution leaves these transitions largely untested. [Coding-Agent Benchmarks Should Match Their Users' Task Flows](https://arxiv.org/abs/2610.09633).

## Why this matters

The recorded workflow is part of the test. Preserve approvals and timing for safety audits, and task transitions for interactive coding evaluations.

## Scan coverage

This is a keyword-filtered discovery feed, not a representative survey of AI research. The archived briefing used 158 of 604 captured evidence records. These findings summarize its cited releases; discovery dates do not necessarily equal original publication dates.

Data and briefing: [2026-10-08 archived snapshot](https://github.com/ktwu01/benchmark-radar/blob/2f75b7a07c6f233bcbcb461631befc2b118be584/data/snapshots/2026-10-08.json).
