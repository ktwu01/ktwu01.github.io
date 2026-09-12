---
title: "Benchmark Radar Day 36: 37 Scores on One Model Card"
date: 2026-08-31
permalink: /posts/2026/08/benchmark-radar-day36/
tags:
  - AI
  - Benchmarks
  - Model Cards
  - Search
  - Data Quality
  - Plain English
---

Day thirty-six of Benchmark Radar. The biggest model card yet landed with 37 scores across 34 benchmarks, and search stopped guessing which result answered the question. Scoreboard: 128 stars, 24 forks.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar is live.** Track new AI benchmarks, datasets, and leaderboards every day: [open the dashboard](https://benchmark-radar.org/) or [star it on GitHub](https://github.com/ktwu01/benchmark-radar).

A model card is the document a lab publishes with a model. A protocol is the exact rule set a score was measured under, such as with tools or without them. Lexical search matches words and phrases directly, the way a dictionary index does, instead of understanding meaning. Identity is the rule that decides two records describe the same repository.

PR #472 adds the Tencent Hy4 preview model card with 37 scores across 34 benchmark IDs. Protocols stay distinct: SWE Atlas splits into three, and HLE is recorded with tools and without. Nine benchmarks the report labels Internal do not enter the public tracking layer, and a duplicate instrument ID for GDPval-AA V2 is unified.

PR #459 makes lexical search show its work. The search returns retrieval evidence instead of a single confidence guess: a retrieval score, coverage across terms, and which tokens matched and which were missing. The agent that answers the question makes the final call between a verified match, a possible candidate, and no confident match. The judgment set now covers 23 wrapper-phrase cases like find GPQA Diamond and SWE bench verified please.

PR #466 wires the reviewed identity overrides into the catalog outputs, so 46 resolved repositories appear with the correct owner and path, and 11 unresolved rows stay visible without inventing links. PR #463 folds the long privacy notice behind a one-click disclosure.

Why this matters.

A model card without protocol detail is a number without a ruler. Recording with-tools and without-tools scores separately, and keeping internal-only results out of the public layer, is what makes 37 numbers usable.

A search that exposes its evidence is a search you can audit. When the tool shows which terms matched and which did not, a wrong answer becomes explainable instead of mysterious.

Issues addressed

- #416: Tencent Hy4 preview model card with 37 scores
- #432: lexical search exposes retrieval evidence instead of guessing
- llm-stats identity: 27 resolved, 9 not found, 2 needing review
- #446: privacy notice folded behind a disclosure
- scoreboard: 128 of 1,000 stars, 24 forks

Day thirty-seven: a citation card, a one-click CLI setup, and a search that covers the whole archive.

> Want to follow Benchmark Radar? [Star the repo on GitHub](https://github.com/ktwu01/benchmark-radar) for daily updates, or [open the live dashboard](https://benchmark-radar.org/) to explore the scans. Read the paper: [arXiv:2609.11115](https://arxiv.org/abs/2609.11115).