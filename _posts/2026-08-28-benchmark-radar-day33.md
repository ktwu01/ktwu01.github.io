---
title: "Benchmark Radar Day 33: A Radar That Finds Releases No Keyword Search Can Catch"
date: 2026-08-28
permalink: /posts/2026/08/benchmark-radar-day33/
tags:
  - AI
  - Benchmarks
  - Discovery
  - Model Cards
  - Open Source
  - Plain English
---

Day thirty-three of Benchmark Radar. The radar learned to find benchmark releases that keyword search would never catch, and a new frontier model card with 14 benchmarks joined the registry. Scoreboard: 115 stars, 21 forks.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar is live.** Track new AI benchmarks, datasets, and leaderboards every day: [open the dashboard](https://ktwu01.github.io/benchmark-radar/) or [star it on GitHub](https://github.com/ktwu01/benchmark-radar).

Keyword search only finds pages that contain the words you searched for. A brand-new repository inside a known AI lab can slip past it because the repo has no searchable text yet. A discovery source is a place the radar watches for new work. A model card is the document a lab publishes with a model.

PR #415 expands discovery beyond keyword search. The radar now scans 360 priority GitHub organizations for newly created public repositories, so a benchmark that launches inside a known lab is found by who made it, not by what words it happens to contain. Hugging Face Daily Papers, Kaggle datasets, and Zenodo records were added as discovery sources, and Hugging Face Spaces are included so public leaderboards and benchmark explorers are visible. Every candidate still passes through the existing taxonomy, low-value suppression, scoring, future-date checks, and exact URL deduplication, so broader eyes do not mean a looser filter.

PR #413 adds the GLM-5.3-Flash model card with 14 benchmarks, sourced from z.ai's official technical blog and aligned with the registry's casing and identity rules in the same pass. The card carries the evidence link, so the 14 entries are checkable against the source rather than copied from memory.

Why this matters.

Discovery by keywords has a blind spot exactly where the most important new work lives: a lab creates a repository, and for the first days or weeks there is little text on the page to match. Watching the organizations themselves closes that gap, and keeping every candidate behind the existing filters means the wider net does not admit noise.

A daily radar is only as good as the last release it missed. The August 28 snapshot recorded 115 stars and 21 forks, and the discovery pipeline that produced it now watches organizations, not just words.

Issues addressed

- #409: catch benchmark releases beyond keyword search, including new repos in known AI and evaluation organizations
- #401: GLM-5.3-Flash model card added with 14 benchmarks from the official z.ai blog
- scoreboard: 115 of 1,000 stars, 21 forks

Day thirty-four: the star history chart redrawn by the repository itself, line by line.

> Want to follow Benchmark Radar? [Star the repo on GitHub](https://github.com/ktwu01/benchmark-radar) for daily updates, or [open the live dashboard](https://ktwu01.github.io/benchmark-radar/) to explore the scans.
