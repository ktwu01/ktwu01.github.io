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

The leaderboard became a research workbench. Day nine added the adoption frontier, score progression, and saturation visualization.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

## What shipped

**Benchmark adoption frontier.** A new visualization showing which benchmarks are being adopted fastest across model card releases. The frontier chart plots adoption velocity against benchmark maturity.

**Score progression layer.** A new data layer with 70 source-verified benchmark score observations. Each observation links to the specific model card or paper that reported the score, with file and line evidence.

**Saturation and adoption on one time axis.** The dashboard now draws both score saturation and adoption on a shared time axis, making it possible to see when a benchmark's scores plateaued relative to when labs stopped adopting it.

**Research workbench redesign.** The leaderboard was redesigned (FINDING-001) to function as a research workbench rather than a simple ranked list. Each benchmark entry now shows score history, adoption trajectory, and source evidence.

**Score verification.** Each cited score card is verified against the actual benchmark it claims to report. This catches mismatches where a score is attributed to the wrong benchmark.

**Reading gap fixes.** The reading gap (the time between a benchmark's latest mention and the current date) is now measured against each benchmark's own latest mention, not a global clock.

**Pipeline fixes.** Custom registry pairing with default scores was fixed. The default registry is now recognized through an equivalent path. Non-finite score values are rejected.

**Aug 2 snapshot backfill.** The August 2 snapshot was backfilled after a collection gap.

**Discovery window documentation.** The second discovery window in the CI workflow was documented.

## Why it matters

This was the day the radar crossed from "collection tool" to "analysis instrument." The score progression layer made it possible to ask: "How have GPT-4's MMLU scores changed across releases?" The adoption frontier made it possible to ask: "Which benchmarks are labs converging on?" These are questions that matter for anyone deciding which benchmarks to run on their own models.

The research workbench redesign reflected a shift in who the tool was for. A ranked list serves a casual reader. A workbench serves a researcher who needs to trace claims back to sources.

## Issues addressed

- \#106: document discovery slot
- \#108: backfill Aug 2 snapshot
- \#113: document discovery window
- \#114: saturation visualization
- \#115: Aug 2 snapshot backfill
- Score progression with 70 source-verified observations
- Benchmark adoption frontier
- Research workbench redesign

Day ten: daily briefing, GPT radar insight, and launch preparation.
