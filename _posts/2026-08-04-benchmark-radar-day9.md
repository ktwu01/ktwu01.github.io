---
title: "Benchmark Radar Day 9: Adoption Frontier and Score Progression Layer"
date: 2026-08-04
permalink: /posts/2026/08/benchmark-radar-day9/
tags:
  - AI
  - Benchmarks
  - Visualization
  - Scores
  - Research Workbench
---

The leaderboard became a research workbench. Hi, Koutian here. Day nine added the adoption frontier, score progression, and saturation charts.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

We added a benchmark adoption frontier. It is a chart that shows which benchmarks labs are picking up fastest across model card releases. It plots adoption speed against how mature each benchmark is.

We built a score progression layer with 70 source-verified score observations. Each observation links to the exact model card or paper that reported it, down to the file and line. MMLU is one standard test of broad knowledge, and now you can watch GPT-4's MMLU score move across releases.

The dashboard now draws score saturation and adoption on one shared time axis. You can see when a benchmark's scores stopped improving next to when labs stopped using it.

We redesigned the leaderboard, tracked as FINDING-001, into a research workbench instead of a plain ranked list. Each benchmark entry now shows score history, adoption path, and the source behind every claim. A ranked list serves a casual reader. A workbench serves a researcher who needs to trace a claim back to its source.

We now verify each cited score against the benchmark it claims to report. That catches cases where a score got pinned to the wrong benchmark.

The reading gap is the time between a benchmark's last mention and today. We now measure it against each benchmark's own last mention, not one global clock.

Pipeline fixes landed too. Custom registry pairing with default scores works now. The default registry is found through an equivalent path. Non-finite score values get rejected.

We backfilled the August 2 snapshot after a collection gap. We also documented the second discovery window in the CI workflow.

Why this matters.

This was the day the radar moved from a collection tool to an analysis tool. The score layer lets you ask how GPT-4's MMLU scores changed over time. The frontier lets you ask which benchmarks labs are converging on. Both questions help you pick which benchmarks to run on your own models.

The workbench redesign reflects who the tool is for now. A researcher needs to follow a claim back to the paper, not just see a number.

Issues addressed:

- #106: document discovery slot
- #108: backfill the August 2 snapshot
- #113: document the second discovery window
- #114: saturation visualization
- #115: backfill August 2 snapshot
- score progression with 70 source-verified observations
- benchmark adoption frontier
- research workbench redesign

Day ten: daily briefing, GPT radar insight, and launch preparation.
