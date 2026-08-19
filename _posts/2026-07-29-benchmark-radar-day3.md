---
title: "Benchmark Radar Day 3: Linkable Rubric Dialogs and Filter Fixes"
date: 2026-07-29
permalink: /posts/2026/07/benchmark-radar-day3/
tags:
  - AI
  - Benchmarks
  - UX
  - URL Routing
---

A small day with two precise fixes that made the radar shareable.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

## What shipped

**Scan date filter fix.** The scan date filter was reverting to the old date on selection. The fix ensures the filter stays on the newly selected date.

**Linkable rubric dialog.** The rubric dialog (which explains the scoring criteria) is now accessible via a URL hashtag. You can link directly to a specific rubric in a message or paper.

**Rubric hash test.** A new test guards against regression in the rubric linking behavior.

**Record expansion display fix.** The record expansion state was not rendering correctly; now it does.

**Trend map corpus fix.** The trend map now represents the full corpus, not just a subset.

## Why it matters

Linkability sounds trivial, but it changes how a tool gets used. When you can send someone a URL that lands on a specific benchmark's rubric, the radar becomes something you cite in a paper or share in a Slack channel, not just something you visit once.

The scan date filter fix was a UX reliability issue: if a user selects a date and the filter reverts, they learn not to trust the controls. Small fixes compound into trust.

## Issues addressed

- \#48: scan date filter and rubric link
- Rubric dialog linkable via URL hashtag
- Record expansion state rendering
- Trend map full corpus representation

Day four: history backfill, freshness banners, and the agentic taxonomy.
