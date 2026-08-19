---
title: "Benchmark Radar Day 2: Cumulative Trends and Artifact Deduplication"
date: 2026-07-28
permalink: /posts/2026/07/benchmark-radar-day2/
tags:
  - AI
  - Benchmarks
  - Data Quality
  - Deduplication
---

The radar gained memory. Day two built cumulative trend maps and solved the artifact alias problem.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

## What shipped

**Cumulative trend map.** The radar now shows how benchmark counts change over time, not just today's snapshot. Each category (benchmarks, datasets, leaderboards, research) gets its own trend line.

**Artifact alias resolution.** The same benchmark can appear under different names across sources. The system now resolves aliases across snapshots so one artifact counts once in cumulative trends, regardless of how many titles it has been listed under.

**Explorer merged into main radar.** The separate Explorer view was folded into the primary radar interface. Two views were competing for attention; one unified view won.

**Priority scoring recalibrated.** The scoring system was adjusted to better distinguish genuinely new benchmarks from re-announced updates.

**Evidence source coverage expanded.** More sources were added to the evidence collection pipeline.

**UI chrome cleanup.** Redundant UI elements were removed from the masthead, Trends section, and Sources panel. The Sources panel was unpinned. Repo badges were changed from rosters to actionable links.

## Why it matters

Artifact deduplication is the core technical challenge of any benchmark radar. Without it, the same benchmark appears ten times under ten slightly different names, and every count is inflated. The alias resolver uses exact identifiers, not fuzzy title matching, which keeps precision high.

The cumulative trend map was the first sign that this project was not just a daily scanner. It was becoming a longitudinal instrument, tracking the AI benchmark ecosystem across time.

## Issues addressed

- \#29: radar UX and coverage fixes
- \#33: resolve radar issues
- \#46: resolve artifact aliases across snapshots
- Duplicate detection via exact identifiers
- Priority scoring recalibration

Day three: scan date filter fixes and linkable rubric dialogs.
