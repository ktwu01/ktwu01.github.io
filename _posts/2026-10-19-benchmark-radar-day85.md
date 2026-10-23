---
title: "Benchmark Radar Day 85: Track Evidence Changes at the Claim Level"
date: 2026-10-19
permalink: /posts/2026/10/benchmark-radar-day85/
tags:
  - AI
  - Benchmarks
---

Day 85 of Benchmark Radar. The scan fetched 1,355 items, published 602, and marked 281 as recommended.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar is live.** [Open the dashboard](https://benchmark-radar.org/), [star the repository](https://github.com/ktwu01/benchmark-radar), or read the [paper](https://arxiv.org/abs/2609.11115). The [Hugging Face dataset](https://huggingface.co/datasets/ktwu01/benchmark-radar) provides the data.

Evidence-State Drift records normalized claims, supporting passages, source identities, timestamps, and content fingerprints across repeated retrievals. Its replay benchmark covers 67 claims and 871 observations. It distinguishes a substantive evidence change from a page that changed only its formatting. [Evidence-State Drift: A Claim-Level Framework and Replay Benchmark for Web-Connected LLM Agents](https://doi.org/10.5281/zenodo.23452676).

The versioned Honest agent scores package recomputes 3,300 Terminal-Bench 4.0 runs. It reports that removing 30 flagged tasks or changing repeat aggregation did not materially alter rankings, while differences of roughly 9.5 points or less were ties with 66 tasks. The result is specific to that package and analysis. [Honest agent scores: do benchmark defects or repeats change which AI agent wins?](https://doi.org/10.6084/m9.figshare.34515048.v2)

## Why this matters

Before acting on a regression alert or a leaderboard gap, ask whether the underlying evidence changed and whether the measured difference resolves the uncertainty.

## Scan coverage

This is a keyword-filtered discovery feed, not a representative survey of AI research. The archived briefing used 172 of 602 captured evidence records. These findings summarize its cited releases; discovery dates do not necessarily equal original publication dates.

Data and briefing: [2026-10-19 archived snapshot](https://github.com/ktwu01/benchmark-radar/blob/2f75b7a07c6f233bcbcb461631befc2b118be584/data/snapshots/2026-10-19.json).
