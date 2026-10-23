---
title: "Benchmark Radar Day 80: Scientific Agents on an Experimental Budget"
date: 2026-10-14
permalink: /posts/2026/10/benchmark-radar-day80/
tags:
  - AI
  - Benchmarks
---

Day 80 of Benchmark Radar. The scan fetched 1,506 items, published 773, and marked 410 as recommended.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar is live.** [Open the dashboard](https://benchmark-radar.org/), [star the repository](https://github.com/ktwu01/benchmark-radar), or read the [paper](https://arxiv.org/abs/2609.11115). The [Hugging Face dataset](https://huggingface.co/datasets/ktwu01/benchmark-radar) provides the data.

Autonomous Science Bench asks agents to select batches of experiments under a fixed budget, receive measurements from a laboratory service, and revise later experiments. Its first six campaigns use published biology, chemistry, and materials-science experiments. Evaluation follows sequential experimental choices rather than answers about a fixed dataset. [Autonomous Science Bench: Evaluating AI Agents for Autonomous Scientific Discovery](https://arxiv.org/abs/2610.18449).

Following the SimGlot archive in [Day 78](/posts/2026/10/benchmark-radar-day78/), today’s feed captures the related audit study. It reports detecting all seven injected defect classes with oracle-integrity checks. It also found a reward-function defect that changed environment state before scoring. A benchmark’s success check needs validation just as the agent’s experimental choices do. [When Agent Evaluation Becomes Unreliable: An Empirical Study of Oracle Failures and Configuration-Dependent Measurement in an LLM Agent Benchmark](https://doi.org/10.48550/arxiv.2610.16067).

## Why this matters

Budgeted scientific discovery needs both credible feedback and a checked success criterion. Otherwise, the agent can optimize a faulty measurement.

## Scan coverage

This is a keyword-filtered discovery feed, not a representative survey of AI research. The archived briefing used 162 of 773 captured evidence records. These findings summarize its cited releases; discovery dates do not necessarily equal original publication dates.

Data and briefing: [2026-10-14 archived snapshot](https://github.com/ktwu01/benchmark-radar/blob/2f75b7a07c6f233bcbcb461631befc2b118be584/data/snapshots/2026-10-14.json).
