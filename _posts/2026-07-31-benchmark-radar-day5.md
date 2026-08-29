---
title: "Benchmark Radar Day 5: Accessible Trend Charts and Landscape Analysis"
date: 2026-07-31
permalink: /posts/2026/07/benchmark-radar-day5/
tags:
  - AI
  - Benchmarks
  - Accessibility
  - Trend Analysis
  - Landscape Report
---

The trend chart got a real hover card. The landscape report got published. And the agentic benchmark count jumped from 3 to 78.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar is live.** Track new AI benchmarks, datasets, and leaderboards every day: [open the dashboard](https://benchmark-radar.org/) or [star it on GitHub](https://github.com/ktwu01/benchmark-radar).

Hi, Koutian here. Today the chart became usable for everyone, and we found out we had badly undercounted agent benchmarks.

The trend chart used to rely on the browser's built-in tooltips. We replaced them with a custom hover card. It works with a mouse or trackpad, stays clear of tall bars, reads itself out to screen readers, follows the column as you scroll, and closes with the Escape key. Screen reader users can finally interact with the chart.

Issue #52 became a full benchmark landscape report. The agentic benchmark count was corrected from 3 to 78 once the new category existed. That number reflects how much agent evaluation work is actually out there. We added a short summary so the report is scannable, generated its figures from the data, and put them in the docs. The corpus totals panel now opens by default, so you see the scale right away.

Why this matters.

The hover card was an accessibility fix. Before, someone using a screen reader could not read the trend chart at all. Now the card follows focus and announces itself, so the chart is open to more people.

The 3 to 78 correction was a credibility moment. We had undercounted agent benchmarks only because the category did not exist yet. It shows why taxonomy accuracy matters: wrong categories give wrong counts, and wrong counts lead to wrong conclusions.

Issues addressed:
- #52: corpus totals and agentic benchmark count correction
- #59: corpus totals visibility
- #60: trend hover card accessibility
- #67: agentic benchmark count (3 to 78)
- #68: benchmark landscape report
- #69: trend hover card fixes
- #71: landscape report figures
- #73: hide duplicate report tables

Day six: Hacker News integration and scheduled radar reliability.

> Want to follow Benchmark Radar? [Star the repo on GitHub](https://github.com/ktwu01/benchmark-radar) for daily updates, or [open the live dashboard](https://benchmark-radar.org/) to explore the scans.
