---
title: "Benchmark Radar Day 47: Citation Surfaces Turn Reader-First — Cite Card, CITATION.md, and Top-Nav Link"
date: 2026-09-11
permalink: /posts/2026/09/benchmark-radar-day47/
tags:
  - AI
  - Benchmarks
  - Citation
  - UX
  - Documentation
  - Plain English
---

Day forty-seven of Benchmark Radar. With the arXiv paper live, the citation surfaces get a reader-first refresh: the Cite card collapses APA and BibTeX blocks by default, `CITATION.md` lands in the repo root, and a Cite link joins the top navigation bar. Scoreboard: 185 stars, 30 forks.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar is live.** Track new AI benchmarks, datasets, and leaderboards every day: [open the dashboard](https://benchmark-radar.org/) or [star it on GitHub](https://github.com/ktwu01/benchmark-radar). Read the paper: [arXiv:2609.11115](https://arxiv.org/abs/2609.11115).

PR #601 cites the arXiv paper across all citation surfaces: the dashboard footer, the CLI `--cite` output, the README badges, and the Cite page now all reference `arXiv:2609.11115` with the full author list and year.

PR #602 adds a Cite entry to the top navigation bar. Readers can jump to the citation page from anywhere on the dashboard without hunting through the footer.

PR #603 collapses the APA and BibTeX blocks on the Cite dialog by default. The card now shows the recommended citation sentence first, with "Show APA" and "Show BibTeX" toggles. This puts the human-readable format front and center — the format most readers actually copy — while keeping the machine-readable formats one click away.

PR #604 makes the Cite card reader-first: the recommended sentence uses natural language ("Benchmark Radar: A Living Database and Search Engine for AI Benchmarks and Evaluation, arXiv:2609.11115, 2026"), the copy button copies plain text, and the arXiv link opens the abstract page. The APA and BibTeX expanders preserve exact formatting for reference managers.

Why this matters.

A citation is not a trophy — it is a tool. Readers who want to cite the work need the right string in two seconds. Hiding the raw APA/BibTeX behind toggles reduces visual noise for the 90% who just need the sentence; the 10% who need the structured format get it with one click.

`CITATION.md` in the repo root makes the citation discoverable for tools (GitHub's "Cite this repository" button, reference managers, automated workflows) without requiring a dashboard visit.

The top-nav Cite link completes the loop: dashboard → paper → cite → dashboard. A reader who finds a benchmark on the leaderboard can cite the project in three clicks.

Issues addressed

- #600: cite arXiv paper across all citation surfaces
- #601: add Cite link to top navigation
- #602: collapse APA/BibTeX blocks by default on Cite dialog
- #603: make Cite card reader-first (recommended sentence, copy button, arXiv link)
- scoreboard: 185 of 1,000 stars, 30 forks

Day forty-eight: the daily radar keeps scanning — new benchmarks, fresh scores, and the living database grows.

> Want to follow Benchmark Radar? [Star the repo on GitHub](https://github.com/ktwu01/benchmark-radar) for daily updates, or [open the live dashboard](https://benchmark-radar.org/) to explore the scans. Read the paper: [arXiv:2609.11115](https://arxiv.org/abs/2609.11115).