---
title: "Benchmark Radar Day 41: A Ranking Decided by Contract First"
date: 2026-09-05
permalink: /posts/2026/09/benchmark-radar-day41/
tags:
  - AI
  - Benchmarks
  - Ranking
  - Data Quality
  - Audit
  - Plain English
---

Day forty-one of Benchmark Radar. The ranking engine for recent releases shipped its first phase with the data contract written first, and the report audit separated raw best scores from scores measured under the same protocol. Scoreboard: 160 stars, 28 forks.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar is live.** Track new AI benchmarks, datasets, and leaderboards every day: [open the dashboard](https://benchmark-radar.org/) or [star it on GitHub](https://github.com/ktwu01/benchmark-radar).

A data contract is the written rule set a data structure must obey. A cohort is a set of releases grouped by when they were published. A window is the span of days a release must land in to count. A protocol is the exact rule set a score was measured under, and saturation means a benchmark whose scores sit close to its ceiling.

PR #531 delivers phase one of the recent-releases ranking. A new validation block checks the structured attention data in every snapshot, and the ranking engine evaluates seven-, thirty-, and ninety-day windows. Only verified release events count, routine updates do not, duplicate identities collapse, and a dedicated-repository check stops a monorepo from inheriting its parent's stars. Scores are normalized, missing values are treated as unknown rather than zero, and releases without enough durable signal get a `limited_signals` label instead of a rank.

PR #514 audits the report's claim about near-ceiling benchmarks. Raw best scores and protocol-comparable series tell different stories, so the report now separates them, records the supporting score IDs in a checked-in JSON audit, and rebuilds the next draft with a protocol-aware table.

PR #556 adds the sunblaze-ucb organization to the discovery registry and raises the scan limit from 360 to 361 so the new entry is actually scanned.

Why this matters.

A ranking is only as honest as its rules. Writing the data contract and the tests first means the numbers are decided by rules the project can check, before any UI makes them visible to the world.

Saturation claims are where evaluation reports most easily overstate. Separating raw best scores from scores measured under the same protocol is the difference between a chart and a claim.

Issues addressed

- #530: data contract and ranking engine for recent releases, phase one
- #457: saturation audit separates raw and protocol-comparable scores
- #555: sunblaze-ucb added to organization discovery
- scoreboard: 160 of 1,000 stars, 28 forks

Day forty-two: the recent-releases ranking reaches the dashboard.

> Want to follow Benchmark Radar? [Star the repo on GitHub](https://github.com/ktwu01/benchmark-radar) for daily updates, or [open the live dashboard](https://benchmark-radar.org/) to explore the scans. Read the paper: [arXiv:2609.11115](https://arxiv.org/abs/2609.11115).