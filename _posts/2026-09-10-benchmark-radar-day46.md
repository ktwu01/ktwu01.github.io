---
title: "Benchmark Radar Day 46: arXiv Release — arXiv:2609.11115 Published and v0.11.0 Released"
date: 2026-09-10
permalink: /posts/2026/09/benchmark-radar-day46/
tags:
  - AI
  - Benchmarks
  - Paper
  - arXiv
  - Release
  - Plain English
---

Day forty-six of Benchmark Radar. The technical paper is now on arXiv as `arXiv:2609.11115`, the v0.11.0 release is published with frozen data and verified hashes, and citation surfaces across the project update to the live arXiv entry. Scoreboard: 185 stars, 30 forks.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar is live.** Track new AI benchmarks, datasets, and leaderboards every day: [open the dashboard](https://benchmark-radar.org/) or [star it on GitHub](https://github.com/ktwu01/benchmark-radar).

The paper: **Benchmark Radar: A Living Database and Search Engine for AI Benchmarks and Evaluation** (Koutian Wu, Junjie Zhou, Ergan Shang, Jiayu Wang, Pengqian Han, Junkai Wang, Wanghan Xu). arXiv:2609.11115 [cs.AI]. [PDF](https://arxiv.org/pdf/2609.11115) · [Abs](https://arxiv.org/abs/2609.11115)

The v0.11.0 release on GitHub pins the complete evidence package:
- Software commit: `8f46bbfa91f5d9900c8b08a5d552c3df5c9597b0`
- Discovery cutoff: 2026-09-07
- Data archive: `benchmark-radar-paper-data-v0.11.0.zip` with SHA-256 sums
- Census: 1,283 source records (790 scored, 493 unscored), 12,916 numeric observations
- 37 public sources (13 direct connectors, 24 first-party lab feeds)

PR #591 advances the paper submodule to the citation revision and verifies the arXiv submission tarball. PR #592 advances to the source-count revision with the finalized 37-source breakdown. PR #593 advances to the rebuilt PDF — the exact `main.pdf` submitted to arXiv, now checked in.

PR #594 adds the Abstract section to both READMEs, describing the living database, daily discovery across 37 sources, the benchmark catalog with score histories, the leaderboard with saturation and trend views, and the CLI for offline queries.

PR #595 documents the score sources accurately in both READMEs: lab model reports and system cards for SWE-bench Verified; Artificial Analysis and LLM Stats for nearly all other model scores; OpenCompass Hub for the wider benchmark catalog. Every score keeps its source citation.

PR #596 credits the score sources on the citation page, and PR #597 updates the contribution scores. PR #598 checks the frozen paper data in CI, confirming hash matches and census consistency.

Why this matters.

The arXiv publication makes the Benchmark Radar methodology citable, permanent, and discoverable. The v0.11.0 release makes the evidence reproducible: the frozen commit, the fixed cutoff, the hashed data archive, and the CI-verified hashes mean anyone can verify the paper's numbers against the same inputs.

The citation updates across the project — README badges, the Cite page, the dashboard footer, the CLI help — now point to a real arXiv identifier instead of a preprint placeholder. The paper enters the scholarly record.

Issues addressed

- #590: paper submodule — citation revision
- #591: paper submodule — source-count revision
- #592: paper submodule — rebuilt PDF (submitted main.pdf)
- #593: Abstract section in both READMEs
- #594: accurate score source documentation in READMEs
- #595: score sources credited on citation page
- #596: CI checks on frozen paper data
- #597: contribution scores updated
- scoreboard: 185 of 1,000 stars, 30 forks

Day forty-seven: citation surfaces become reader-first, the Cite card collapses APA/BibTeX by default, and a Cite link joins the top navigation.

> Want to follow Benchmark Radar? [Star the repo on GitHub](https://github.com/ktwu01/benchmark-radar) for daily updates, or [open the live dashboard](https://benchmark-radar.org/) to explore the scans. Read the paper: [arXiv:2609.11115](https://arxiv.org/abs/2609.11115).