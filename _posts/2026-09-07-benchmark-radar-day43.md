---
title: "Benchmark Radar Day 43: Paper Cutoff Day — Source Counts and Figure Data Freeze"
date: 2026-09-07
permalink: /posts/2026/09/benchmark-radar-day43/
tags:
  - AI
  - Benchmarks
  - Paper
  - Data Freeze
  - Audit
  - Plain English
---

Day forty-three of Benchmark Radar. The discovery cutoff for the technical paper locks at 2026-09-07. Source counts, figure data, and the full-catalog audit pipeline freeze for the v0.11.0 release and arXiv submission. Scoreboard: 170 stars, 30 forks.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar is live.** Track new AI benchmarks, datasets, and leaderboards every day: [open the dashboard](https://benchmark-radar.org/) or [star it on GitHub](https://github.com/ktwu01/benchmark-radar).

A data cutoff is the date after which no new discovery snapshots, registry inputs, model reports, or scores enter the paper's evidence base. The v0.11.0 release pins software commit `8f46bbf` and a discovery cutoff of 2026-09-07. Registry snapshots retain their August collection dates.

PR #571 derives the discovery ingest source count for the report: 37 public sources (13 direct connectors, 24 first-party lab feeds) feed the daily discovery pipeline. The count is computed from the live registry and written into the paper's figure data.

PR #572 holds the README source count to the live registry so the badge and the paper agree. PR #573 runs the six-step CI sequence to export `figure-data.tex` through the paper submodule, recording input SHA-256 hashes in the header. PR #574 executes the full-catalog audit: `audit_catalog.py` verifies 1,283 source records (790 scored, 493 unscored) with 12,916 numeric observations, and `audit_findings.py` exports the complete findings tables.

PR #575 rebuilds the model registry with the leaderboard's model identities, and PR #576 re-freezes the logo audit IDs around the new leaderboard models.

Why this matters.

The cutoff is not a pause — it is a contract. Every number in the paper, every figure, every table trace back to inputs frozen on this day. The SHA-256 hashes in `figure-data.tex` and the release archive `benchmark-radar-paper-data-v0.11.0.zip` make the evidence tamper-evident.

Freezing the source count at 37 means the paper's "37 public sources" claim is verifiable against the registry that existed on 2026-09-07, not a number that drifts with later additions.

Issues addressed

- #570: derive discovery ingest source count for report (37 sources)
- #571: hold README source count to live registry
- #572: export figure-data.tex with input hashes
- #573: full-catalog audit — 1,283 source records, 12,916 observations
- #574: rebuild model registry with leaderboard identities
- #575: re-freeze logo audit IDs
- scoreboard: 170 of 1,000 stars, 30 forks

Day forty-four: the paper submodule advances through citation revision, source-count revision, and the rebuilt PDF — the arXiv submission package takes shape.

> Want to follow Benchmark Radar? [Star the repo on GitHub](https://github.com/ktwu01/benchmark-radar) for daily updates, or [open the live dashboard](https://benchmark-radar.org/) to explore the scans. Read the paper: [arXiv:2609.11115](https://arxiv.org/abs/2609.11115).