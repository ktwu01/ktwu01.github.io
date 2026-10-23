---
title: "Benchmark Radar Day 81: Remove Patient Overlap, Not Just Duplicate Images"
date: 2026-10-15
permalink: /posts/2026/10/benchmark-radar-day81/
tags:
  - AI
  - Benchmarks
---

Day 81 of Benchmark Radar. The scan fetched 1,711 items, published 899, and marked 425 as recommended.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar is live.** [Open the dashboard](https://benchmark-radar.org/), [star the repository](https://github.com/ktwu01/benchmark-radar), or read the [paper](https://arxiv.org/abs/2609.11115). The [Hugging Face dataset](https://huggingface.co/datasets/ktwu01/benchmark-radar) provides the data.

An audit of a brain-tumor MRI benchmark reports that all 761 traceable tumor test images came from patients also represented in training. Patient-disjoint cross-validation reduced reported overall accuracy from roughly 99% to 95%. Removing pixel duplicates alone did not produce the same correction. [Complete Patient-Level Leakage Among Traceable Images in a Widely Used Brain Tumor MRI Benchmark](https://doi.org/10.21203/rs.3.rs-11078963/v1).

EvoProbe regenerates agent tasks using diagnostic feedback. It scores verifiable subtasks and examines complete action sequences to identify phase-level bottlenecks. This offers a way to inspect planning and execution separately when the final success rate changes little. [EvoProbe: Evaluation-Driven Benchmark Evolution for LLM Agents](https://doi.org/10.48550/arxiv.2610.19433).

## Why this matters

Test on the unit that must generalize. For repeated images of the same person, that unit is the patient; for agent workflows, retain evidence about the stages that failed.

## Scan coverage

This is a keyword-filtered discovery feed, not a representative survey of AI research. The archived briefing used 189 of 899 captured evidence records. These findings summarize its cited releases; discovery dates do not necessarily equal original publication dates.

Data and briefing: [2026-10-15 archived snapshot](https://github.com/ktwu01/benchmark-radar/blob/2f75b7a07c6f233bcbcb461631befc2b118be584/data/snapshots/2026-10-15.json).
