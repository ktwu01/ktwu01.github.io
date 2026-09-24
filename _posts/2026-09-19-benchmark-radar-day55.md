---
title: "Benchmark Radar Day 55: Start From the Latest Main"
date: 2026-09-19
permalink: /posts/2026/09/benchmark-radar-day55/
tags:
  - AI
  - Benchmarks
  - Open Source
  - Contributors
---

Day fifty-five of Benchmark Radar. The contributor guide gains one rule: start every branch from an up-to-date main. The WeChat group QR code is refreshed, and the daily scan ran on schedule. Scoreboard: 234 stars, 40 forks.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar is live.** Track new AI benchmarks, datasets, and leaderboards every day: [open the dashboard](https://benchmark-radar.org/) or [star it on GitHub](https://github.com/ktwu01/benchmark-radar). Read the paper: [arXiv:2609.11115](https://arxiv.org/abs/2609.11115). Query the data: [Hugging Face dataset](https://huggingface.co/datasets/ktwu01/benchmark-radar).

The AGENTS.md rules for branches and pull requests (merged the next day as PR #672) now require starting from an up-to-date main and rebasing a branch that has fallen behind before opening its PR. Follow-up edits say how: reach the latest main with a fetch rather than by pulling local main, create the branch without tracking, and set its upstream on the first push.

The rule names two quiet failures a stale base causes. The branch carries old copies of files that changed on main since, so a one-line edit can revert someone else's work. And the technical-report submodule pointer can move backward, pinning the paper to an earlier commit.

Issue #668 replaced the WeChat group QR code in the repository assets.

Why this matters.

Neither failure shows up in a small diff, which is why reviewers miss them. Writing the rule down moves the check from the reviewer's memory to the contributor's first command.

Issues addressed

- #672: start branches from an up-to-date main
- #668: WeChat group QR code update
- scoreboard: 234 of 1,000 stars, 40 forks

Day fifty-six: two fixes from an outside contributor land, and the paper's source catches up with main.

> Want to follow Benchmark Radar? [Star the repo on GitHub](https://github.com/ktwu01/benchmark-radar) for daily updates, or [open the live dashboard](https://benchmark-radar.org/) to explore the scans. Read the paper: [arXiv:2609.11115](https://arxiv.org/abs/2609.11115).
