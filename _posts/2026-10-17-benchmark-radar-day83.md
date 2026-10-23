---
title: "Benchmark Radar Day 83: Security Scores Depend on Detector Versions"
date: 2026-10-17
permalink: /posts/2026/10/benchmark-radar-day83/
tags:
  - AI
  - Benchmarks
---

Day 83 of Benchmark Radar. The scan fetched 1,562 items, published 749, and marked 246 as recommended.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar is live.** [Open the dashboard](https://benchmark-radar.org/), [star the repository](https://github.com/ktwu01/benchmark-radar), or read the [paper](https://arxiv.org/abs/2609.11115). The [Hugging Face dataset](https://huggingface.co/datasets/ktwu01/benchmark-radar) provides the data.

NVIDIA garak v0.17.1 adds hit@k for each probe-and-detector pair, measuring whether an attack succeeds within the top k attempts. It also fixes cases where an unexamined file could count as a pass and refusal detection over-counted results. Scores can change after these fixes without a change to the evaluated model. [NVIDIA/garak v0.17.1](https://github.com/NVIDIA/garak/releases/tag/v0.17.1).

A FormAI-v2 replication package supplies corrected vulnerability labels, a fixed training and holdout split, counterfactual tests, and outputs from several verifier versions. It supports checking whether a vulnerability detector learned the intended distinction or a shortcut introduced by its labels. [Replication package for "Version-Dependent Verifier Labels Teach Vulnerability Detectors a scanf Shortcut in FormAI-v2, a Benchmark of LLM-Generated C Code"](https://doi.org/10.5281/zenodo.23421590).

## Why this matters

Pin the detector and verifier versions alongside the model. Keep machine-readable results so a scoring correction can be separated from a capability change.

## Scan coverage

This is a keyword-filtered discovery feed, not a representative survey of AI research. The archived briefing used 121 of 749 captured evidence records. These findings summarize its cited releases; discovery dates do not necessarily equal original publication dates.

Data and briefing: [2026-10-17 archived snapshot](https://github.com/ktwu01/benchmark-radar/blob/2f75b7a07c6f233bcbcb461631befc2b118be584/data/snapshots/2026-10-17.json).
