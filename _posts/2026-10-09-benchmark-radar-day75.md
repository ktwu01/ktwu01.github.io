---
title: "Benchmark Radar Day 75: Did the Agent Change, or Did the Scorer?"
date: 2026-10-09
permalink: /posts/2026/10/benchmark-radar-day75/
tags:
  - AI
  - Benchmarks
---

Day 75 of Benchmark Radar. The scan fetched 1,338 items, published 616, and marked 281 as recommended.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar is live.** [Open the dashboard](https://benchmark-radar.org/), [star the repository](https://github.com/ktwu01/benchmark-radar), or read the [paper](https://arxiv.org/abs/2609.11115). The [Hugging Face dataset](https://huggingface.co/datasets/ktwu01/benchmark-radar) provides the data.

TRACE uses paired runs and rescoring of unchanged trajectories to diagnose brittle evaluators. In its controlled suite, renaming tools reduced a scripted agent’s score even though its operations stayed identical. The result shows why a score regression needs an evaluator check before it is attributed to the agent. [TRACE: Diagnosing Verifier Brittleness in Agentic Evaluation](https://arxiv.org/abs/2610.11678).

A tabular-data clarification benchmark separates the policy for asking questions from the eventual solution. It also tracks oracle leakage: a simulated user supplying information that a real user would not provide. Success with an overly helpful simulator can overstate an assistant’s ability to resolve ambiguity. [Conversational Task Disambiguation over Tabular Data: Leakage-Aware Formulation, Benchmark Suite, and Training](https://arxiv.org/abs/2610.10740).

## Why this matters

Check the scorer and simulated user before treating a better score as better behavior. Both can change the measurement while the agent stays the same.

## Scan coverage

This is a keyword-filtered discovery feed, not a representative survey of AI research. The archived briefing used 163 of 616 captured evidence records. These findings summarize its cited releases; discovery dates do not necessarily equal original publication dates.

Data and briefing: [2026-10-09 archived snapshot](https://github.com/ktwu01/benchmark-radar/blob/2f75b7a07c6f233bcbcb461631befc2b118be584/data/snapshots/2026-10-09.json).
