---
title: "Benchmark Radar Day 22: Data Integrity and Community Channels"
date: 2026-08-17
permalink: /posts/2026/08/benchmark-radar-day22/
tags:
  - AI
  - Benchmarks
  - Data Integrity
  - WeChat
  - RSS
  - Social Media
---

Stale runs can no longer corrupt snapshots. The WeChat group went public. Day twenty-two hardened data integrity and expanded community channels.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

## What shipped

**Stale run protection.** Daily snapshot persistence is now protected from stale runs. If a run produces outdated data (e.g., from a delayed trigger), it does not overwrite a more recent snapshot. This was PR #235, flagged as P1 data integrity.

**Pages trigger for package changes.** The GitHub Pages workflow now triggers on package changes, not just source code changes. This ensures deployment stays in sync with dependency updates.

**WeChat group QR codes.** QR codes for the WeChat group were added to both English and Chinese READMEs.

**Social channel cadence updated.** The monthly social channel cadence was documented and the channel list updated.

**Benchmark URLs and dates fixed.** Issue #98 was resolved: benchmark URLs and dates were corrected across the registry.

**Major-LLM RSS feeds.** RSS feeds for major LLM providers were added, along with scorecard pairs that link model releases to their benchmark results.

**Zh validation hardened.** Chinese translation validation was hardened against review findings. Ruff formatting was applied to zh translation files.

**Chinese README revised.** The Chinese README was revised for clarity and updated with current project status.

**GPT prose in Chinese.** The daily GPT-generated prose now renders in Chinese when the site is in Chinese mode (issue #231).

**Explore view simplified.** The Explore view was simplified (#242) to reduce visual clutter.

## Why it matters

The stale run protection was the most critical fix of the day. A radar that overwrites fresh data with stale data is worse than no radar at all, because it erodes trust. The P1 designation reflected the severity: data integrity failures are existential for a data product.

The WeChat group QR codes were a community-building move. WeChat is the primary communication channel for Chinese AI practitioners. Making the group easily joinable lowered the barrier to community participation.

The RSS feeds for major LLM providers expanded the radar's coverage from "benchmarks that exist" to "how models perform on those benchmarks." This is a qualitative expansion: the radar now tracks both the evaluation instruments and the evaluation results.

## Issues addressed

- \#230: dashboard UX revisit
- \#231: GPT prose in Chinese
- \#232: benchmark URLs/dates fix and RSS feeds
- \#235: P1 data integrity (stale run protection)
- WeChat group QR codes
- Social channel cadence
- Zh validation hardening
- Explore view simplification

Day twenty-three: external catalog and leaderboard navigator.
