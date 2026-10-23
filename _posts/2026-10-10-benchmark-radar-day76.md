---
title: "Benchmark Radar Day 76: Hold Out Whole Recordings"
date: 2026-10-10
permalink: /posts/2026/10/benchmark-radar-day76/
tags:
  - AI
  - Benchmarks
---

Day 76 of Benchmark Radar. The scan fetched 1,316 items, published 547, and marked 234 as recommended.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar is live.** [Open the dashboard](https://benchmark-radar.org/), [star the repository](https://github.com/ktwu01/benchmark-radar), or read the [paper](https://arxiv.org/abs/2609.11115). The [Hugging Face dataset](https://huggingface.co/datasets/ktwu01/benchmark-radar) provides the data.

The milipoint-runs artifact revisits MiliPoint’s overlapping radar windows. Holding out complete recording runs reduced reported identification accuracy from about 94% to 37–39%. When training and test windows share frames, a random split can reward recognition of the recording rather than transfer to a new run. [milipoint-runs: run-disjoint evaluation of the MiliPoint millimeter-wave radar dataset](https://doi.org/10.5281/zenodo.23271684).

Inspect AI 0.3.278 adds task and sample descriptions to logs and data frames, extends tool review to handoff calls, and fixes context-compaction, token-counting, and retry issues. A harness update can therefore affect both the audit trail and the accounting of an evaluation. [UKGovernmentBEIS/inspect_ai 0.3.278](https://github.com/UKGovernmentBEIS/inspect_ai/releases/tag/0.3.278).

## Why this matters

Record both the split definition and the harness version. A familiar dataset name does not guarantee a comparable measurement.

## Scan coverage

This is a keyword-filtered discovery feed, not a representative survey of AI research. The archived briefing used 142 of 547 captured evidence records. These findings summarize its cited releases; discovery dates do not necessarily equal original publication dates.

Data and briefing: [2026-10-10 archived snapshot](https://github.com/ktwu01/benchmark-radar/blob/2f75b7a07c6f233bcbcb461631befc2b118be584/data/snapshots/2026-10-10.json).
