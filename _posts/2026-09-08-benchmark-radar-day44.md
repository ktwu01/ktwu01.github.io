---
title: "Benchmark Radar Day 44: Paper Submodule Advances — Citation Revision and Rebuilt PDF"
date: 2026-09-08
permalink: /posts/2026/09/benchmark-radar-day44/
tags:
  - AI
  - Benchmarks
  - Paper
  - Citation
  - PDF
  - Plain English
---

Day forty-four of Benchmark Radar. The paper submodule advances through the citation revision and the source-count revision to the rebuilt PDF. The arXiv submission package assembles. Scoreboard: 175 stars, 31 forks.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar is live.** Track new AI benchmarks, datasets, and leaderboards every day: [open the dashboard](https://benchmark-radar.org/) or [star it on GitHub](https://github.com/ktwu01/benchmark-radar).

PR #580 merges the professional UI polish: the dashboard gets refined spacing, consistent typography, and smoother interactions across the Today page, Leaderboard, and Frontier views.

PR #581 advances the paper submodule to the citation revision: the manuscript updates its citation style, author list, and affiliation formatting to match arXiv requirements. PR #582 advances to the source-count revision: the "37 sources" claim and its breakdown (13 connectors, 24 lab feeds) are verified against the frozen registry and written into the manuscript.

PR #583 rebuilds the PDF from the revised LaTeX. The new `main.pdf` passes the small-number scan (no rendered values below 100 flagged as abnormal) and the figure hash check against the committed `figure-data.tex`. The arXiv submission tarball `arxiv.tar.gz` is produced with `main.bbl` and all figure inputs included.

PR #584 updates the WeChat group QR code in the README and dashboard footer.

Why this matters.

Each submodule advance is a verified step: the citation revision ensures the bibliography renders correctly on arXiv; the source-count revision locks the "37 sources" claim to the frozen registry; the rebuilt PDF is the exact artifact that will be submitted. The tarball `arxiv.tar.gz` is a self-contained submission package — unpack it, compile it, and you get the same PDF.

The UI polish is not cosmetic. Consistent spacing and typography reduce cognitive load when readers scan ranked feeds, compare protocols, or trace evidence links. A cleaner interface makes the data contract visible.

Issues addressed

- #580: professional UI polish (spacing, typography, interactions)
- #581: paper submodule — citation revision
- #582: paper submodule — source-count revision
- #583: paper submodule — rebuilt PDF and arxiv.tar.gz
- #584: WeChat group QR code update
- scoreboard: 175 of 1,000 stars, 31 forks

Day forty-five: final paper preparations — content relicensing, CI checks on frozen data, and the report tests match the manuscript.

> Want to follow Benchmark Radar? [Star the repo on GitHub](https://github.com/ktwu01/benchmark-radar) for daily updates, or [open the live dashboard](https://benchmark-radar.org/) to explore the scans. Read the paper: [arXiv:2609.11115](https://arxiv.org/abs/2609.11115).