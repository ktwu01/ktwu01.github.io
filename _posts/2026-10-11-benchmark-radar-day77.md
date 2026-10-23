---
title: "Benchmark Radar Day 77: Does Agent Memory Follow Revised Requirements?"
date: 2026-10-11
permalink: /posts/2026/10/benchmark-radar-day77/
tags:
  - AI
  - Benchmarks
---

Day 77 of Benchmark Radar. The scan fetched 1,263 items, published 477, and marked 164 as recommended.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar is live.** [Open the dashboard](https://benchmark-radar.org/), [star the repository](https://github.com/ktwu01/benchmark-radar), or read the [paper](https://arxiv.org/abs/2609.11115). The [Hugging Face dataset](https://huggingface.co/datasets/ktwu01/benchmark-radar) provides the data.

Two-Stage Measurement of Update Adherence tests whether a memory-enabled agent follows a revised requirement. It scores the context assembled by the memory system separately from the final answer, using deterministic rules. This makes it possible to distinguish failure to retrieve the update from failure to use an update already present. [Two-Stage Measurement of Update Adherence in Language Model Memory Agents: benchmark, event records, and scoring scripts](https://doi.org/10.5281/zenodo.23280324).

Tariff Cost Benchmark evaluates 228 binding customs rulings issued after the latest disclosed training cutoff among the compared models. It reports the larger 1,098-ruling set separately as an upper-bound analysis and weights errors by the customs duty at stake. This connects classification mistakes to their cost while making likely training exposure explicit. [Tariff Cost Benchmark: Duty-at-Stake and Direction Bias in LLM Customs Classification](https://doi.org/10.5281/zenodo.23289975).

## Why this matters

A useful diagnosis identifies where an error enters the workflow and what that error costs. Aggregate accuracy alone leaves both questions open.

## Scan coverage

This is a keyword-filtered discovery feed, not a representative survey of AI research. The archived briefing used 115 of 477 captured evidence records. These findings summarize its cited releases; discovery dates do not necessarily equal original publication dates.

Data and briefing: [2026-10-11 archived snapshot](https://github.com/ktwu01/benchmark-radar/blob/2f75b7a07c6f233bcbcb461631befc2b118be584/data/snapshots/2026-10-11.json).
