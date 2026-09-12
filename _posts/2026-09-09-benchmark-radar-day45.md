---
title: "Benchmark Radar Day 45: Final Paper Preparations — Relicensing, CI Checks, and Report Tests"
date: 2026-09-09
permalink: /posts/2026/09/benchmark-radar-day45/
tags:
  - AI
  - Benchmarks
  - Paper
  - License
  - CI
  - Plain English
---

Day forty-five of Benchmark Radar. The paper enters its final preparation phase: content relicensed to CC BY-NC-SA 4.0, CI checks validate frozen paper data, and report tests align with the manuscript. Scoreboard: 180 stars, 32 forks.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar is live.** Track new AI benchmarks, datasets, and leaderboards every day: [open the dashboard](https://benchmark-radar.org/) or [star it on GitHub](https://github.com/ktwu01/benchmark-radar).

PR #585 relicenses the editorial content (technical report, README prose, documentation) as CC BY-NC-SA 4.0. The software remains MIT. The new `LICENSE-CONTENT.md` and updated `README.md`/`README.zh-CN.md` make the split explicit: code is free for any use; the paper's prose, figures, and original editorial content require attribution, non-commercial use, and share-alike.

PR #586 adds CI checks for the frozen paper data. The workflow verifies that the committed `figure-data.tex` hashes match the v0.11.0 release archive, that `catalog-data.tex` and `findings-data.tex` are consistent with the frozen census, and that the small-number scan passes on the rebuilt PDF. This ensures the paper's quantitative claims cannot drift after the cutoff.

PR #587 matches the report tests to the manuscript and the ingest export. The test suite now validates that the paper's census numbers (1,283 source records, 790 scored, 493 unscored, 12,916 observations) match the exported figure data, and that the audit JSON evidence files (`evidence/catalog-audit.json`, `evidence/catalog-findings.json`) are structurally sound.

PR #588 merges the agents branch policy: explicit request required before touching `main` or the paper submodule pointer. PR #589 joins benchmark-owned leaderboards to the report catalog, and PR #590 reads a benchmark source's registered name as its score title.

Why this matters.

The license split is deliberate. The MIT code lets anyone build on the radar engine. The CC BY-NC-SA 4.0 content protects the paper's editorial work — its prose, figures, and analysis — from commercial repackaging without permission, while keeping it open for research and education.

The CI checks on frozen data are the paper's immune system. They catch hash mismatches, census drift, and abnormal rendered numbers before they reach arXiv. The test alignment means the report's numbers are not just claimed — they are continuously verified against the same frozen inputs.

Issues addressed

- #585: relicense editorial content as CC BY-NC-SA 4.0
- #586: CI checks on frozen paper data (hashes, census, small-number scan)
- #587: report tests match manuscript and ingest export
- #588: agents branch policy (protect main and paper pointer)
- #589: benchmark-owned leaderboards join report catalog
- #590: registered name as score title
- scoreboard: 180 of 1,000 stars, 32 forks

Day forty-six: the arXiv paper goes live — `arXiv:2609.11115` published, v0.11.0 released, and the citation surfaces updated across the project.

> Want to follow Benchmark Radar? [Star the repo on GitHub](https://github.com/ktwu01/benchmark-radar) for daily updates, or [open the live dashboard](https://benchmark-radar.org/) to explore the scans. Read the paper: [arXiv:2609.11115](https://arxiv.org/abs/2609.11115).