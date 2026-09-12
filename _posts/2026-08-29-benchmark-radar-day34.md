---
title: "Benchmark Radar Day 34: A Radar You Can Run From a Command Line"
date: 2026-08-29
permalink: /posts/2026/08/benchmark-radar-day34/
tags:
  - AI
  - Benchmarks
  - Open Source
  - CLI
  - Offline
  - Plain English
---

Day thirty-four of Benchmark Radar. The radar now runs from a command line on your own computer, offline, no dashboard in between, and a coding agent can answer benchmark questions straight from the data. Scoreboard: 121 stars, 23 forks.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar is live.** Track new AI benchmarks, datasets, and leaderboards every day: [open the dashboard](https://benchmark-radar.org/) or [star it on GitHub](https://github.com/ktwu01/benchmark-radar).

A command line is a text window where you type instructions to a computer, and a CLI is a program you run there. Sync means bringing your local copy of the data up to date with the master copy. A checksum is a short fingerprint of a file that changes whenever the file changes. A social image is the picture shown when a link is shared.

PR #426, the twelve-point centerpiece, adds a local-first query CLI with `search`, `show`, `recent`, `status`, `init`, and `sync`. Search stays offline and reproducible; sync checks the small manifest first, supports ETag caching, and validates size, SHA-256, ZIP safety, catalog integrity, and shard completeness before switching to the new version. A failed activation keeps the previous verified copy, and the downloader rejects insecure downgrades. The same PR ships the benchmark-radar Agent Skill, which routes questions through the CLI instead of guessing, and documents the setup in English and Chinese. The public one-command install stayed blocked until the HTTPS routing was corrected.

PR #418 closes the budget gaps the expanded briefing limits exposed, so no evidence gets silently dropped. PR #427 fixes Pages publishing by removing a stray root CNAME and retries an unsafe Chinese translation while keeping strict quantity checks. PR #428 makes the social image show the saturation chart instead of the leaderboard card.

PR #429 and PR #431 repair the contributor image pipeline. Contributor avatars in the README had rendered as six broken icons because an SVG loaded as an image cannot fetch external resources, so the new generator inlines every avatar directly. The workflow that updates the image now opens pull requests instead of pushing to protected main, the missing Actions permission is enabled, and one external action is replaced by the CLI already installed on the runner.

PR #435 makes the README easier to scan: the intro now names a single number, 37 public sources, and the internal-only docs move behind a foldable block.

Why this matters.

A radar you can run offline is a radar that works anywhere, in a notebook, a laptop, or an agent, with the same reproducible answers every time. The dashboard remains the front door; the CLI makes the data portable.

The invisible fixes matter as much as the visible feature. A broken social image or a failing contributor workflow looks small until it stops the project from being shared or from crediting the people who helped. Pages publishing, translation retries, and contributor images are the rails everything else runs on.

Issues addressed

- #426: local-first CLI, managed data sync, and the benchmark-radar Agent Skill
- #404: social image now shows the saturation chart
- #396: contributor-image updates open pull requests instead of direct pushes
- #430: README intro simplified to 37 public sources
- #378: briefing budget gaps closed, including Chinese rendering
- scoreboard: 121 of 1,000 stars, 23 forks

Day thirty-five: one page for every benchmark, built for search engines instead of screens.

> Want to follow Benchmark Radar? [Star the repo on GitHub](https://github.com/ktwu01/benchmark-radar) for daily updates, or [open the live dashboard](https://benchmark-radar.org/) to explore the scans. Read the paper: [arXiv:2609.11115](https://arxiv.org/abs/2609.11115).