---
title: "Benchmark Radar Day 11: KW-Bench Capability Layer and Community Launch"
date: 2026-08-06
permalink: /posts/2026/08/benchmark-radar-day11/
tags:
  - AI
  - Benchmarks
  - KW-Bench
  - Capability Rubric
  - Community
---

KW-Bench got a capability rubric. The community got launch posts. Hi, Koutian here. Day eleven ran on two tracks at once.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar is live.** Track new AI benchmarks, datasets, and leaderboards every day: [open the dashboard](https://benchmark-radar.org/) or [star it on GitHub](https://github.com/ktwu01/benchmark-radar).

We built a KW-Bench capability rubric. KW-Bench is our own set of benchmarks. The rubric assigns a level, L0 through L5, to each benchmark based on what it measures. The assignment is content-hash deterministic, meaning the same input always yields the same level, so anyone can check it.

We published the capability layer in shadow mode. It runs next to the old classification but does not override it yet. That lets us test the rubric on real data before we trust it as the default.

The shadow store tracks KW-Bench state across runs. We hardened it against corruption and stale state, and fixed seven regressions left over from the last round of pattern fixes.

We derived and normalized benchmark tracks, then deduplicated the normalized names so the same track is not listed twice.

Classifications are now cached by content hash. Re-running the rubric on unchanged data skips the reprocessing.

Overlapping trend categories used to collapse into each other in the Venn diagram, which shows how groups overlap. Now they render independently.

We prepared copy-ready posts for the community launch channels and documented the Chinese launch channels.

We corrected the README's description of what the radar watches, so it matches what the tool actually does.

Why this matters.

The capability rubric answers a question the community kept asking: which benchmarks are actually hard? L0 benchmarks are trivially solvable. L5 benchmarks are genuine open problems. Because the assignment is deterministic, you can reproduce it yourself and confirm the labels.

Shadow mode was a deliberate choice. Shipping a new classification without testing it would be reckless. Shadow mode lets us compare the rubric's output against known-good labels before it becomes the default.

The launch posts were our first message to the outside world. The radar had been building in private. This was the day it went public.

Issues addressed:

- #144: Chinese launch channels
- #148: community launch copy
- #151: fix the Venn overlap rendering
- #154: merge the KW-Bench MVP
- KW-Bench L0-L5 capability rubric
- shadow store recovery and hardening
- canonical benchmark track derivation
- content hash caching

Day twelve: daily RSS feed.

> Want to follow Benchmark Radar? [Star the repo on GitHub](https://github.com/ktwu01/benchmark-radar) for daily updates, or [open the live dashboard](https://benchmark-radar.org/) to explore the scans.
