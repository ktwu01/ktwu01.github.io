---
title: "Benchmark Radar Day 6: Hacker News Integration and Scheduled Reliability"
date: 2026-08-01
permalink: /posts/2026/08/benchmark-radar-day6/
tags:
  - AI
  - Benchmarks
  - Hacker News
  - Reliability
  - RSS
---

The radar now watches Hacker News. Day six added community attention signals and hardened the daily schedule.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

## What shipped

**Hacker News attention collection.** The radar now pulls benchmark-related discussions from Hacker News. This adds a community signal: when a benchmark gets discussed on HN, it means practitioners are paying attention, not just researchers.

**Hacker News observations kept stable and bounded.** The HN collector produces a bounded set of observations per run. This prevents a single viral thread from overwhelming the daily snapshot.

**arXiv RSS document filtering.** Incompatible arXiv RSS documents are now rejected instead of crashing the pipeline. Some arXiv RSS entries have malformed metadata; the system skips them gracefully.

**Empty arXiv day handling.** When arXiv returns no results for a day (which happens on weekends and holidays), the radar completes successfully instead of failing.

**Scheduled radar reliability.** PR #75 addressed reliability issues in the scheduled workflow, including fallback handling and error recovery.

**Landscape report figures.** Generated figures from the landscape report were added to the documentation.

**GitHub App token bump.** The `actions/create-github-app-token` was updated from 2.2.2 to 3.2.0.

## Why it matters

Hacker News is where AI practitioners discuss what they actually use, not what they publish. Adding HN signals meant the radar could detect when a benchmark was gaining practical traction, not just academic citations. This was the first community-sourced signal in the system.

The arXiv hardening was equally important. A daily run that fails on a quiet Sunday is a run you stop trusting. Making the system survive empty days and malformed RSS entries meant the schedule could run unattended.

## Issues addressed

- \#70: GitHub App token bump
- \#71: landscape report figures
- \#73: hide duplicate report tables
- \#75: scheduled radar reliability
- \#76: Hacker News collector integration
- arXiv RSS document filtering
- Empty arXiv day handling

Day seven: model card adoption leaderboard and registry expansion.
