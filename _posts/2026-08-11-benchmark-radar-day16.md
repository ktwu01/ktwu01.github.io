---
title: "Benchmark Radar Day 16: Counting Accuracy and Progressive Disclosure"
date: 2026-08-11
permalink: /posts/2026/08/benchmark-radar-day16/
tags:
  - AI
  - Benchmarks
  - Counting
  - UI
  - Progressive Disclosure
---

Single-adopter benchmarks were under-counted. Drill-downs were overwhelming. Day sixteen fixed both.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

## What shipped

**Single-adopter benchmark count fix.** Benchmarks adopted by only one model card were being under-counted. The fix ensures these benchmarks are counted accurately, even when their adoption is narrow.

**Progressive disclosure restored.** Drill-down sections in the leaderboard, Q&A, and homepage are now collapsed by default. Users expand what they want to read instead of being confronted with everything at once.

**Daily social-checklist issue restored.** The daily social-checklist issue was restored after being accidentally retired. The issue date is now derived from the report date, not the wall clock, preventing timezone-related misalignment.

**workflow_dispatch publish default.** The `workflow_dispatch` publish input now defaults to `true` (issue #88). Previously, manual workflow runs required explicitly setting the publish flag.

**Brand icons in frontier circles.** The adoption frontier circles now show real brand icons (OpenAI, Google, Anthropic, etc.) instead of generic markers. This makes the frontier chart immediately scannable.

## Why it matters

The single-adopter count fix addressed a data accuracy issue. When a benchmark has exactly one adopter, under-counting it makes the adoption landscape look less diverse than it is. For a tool that claims to track benchmark adoption, this kind of error undermines trust.

Progressive disclosure was a UX principle applied to information density. The radar collects a lot of data; showing all of it at once overwhelms new users. Collapsing drill-downs lets the dashboard serve both casual browsers (who see summaries) and deep researchers (who expand what they need).

The brand icons in frontier circles were a visual identity improvement. When you see the OpenAI logo next to a benchmark adoption point, you immediately know who adopted it, without reading a legend.

## Issues addressed

- \#88: default workflow_dispatch publish to true, restore daily social issue, date from report
- \#99: correct under-counted single-adopter benchmarks
- \#183: restore progressive disclosure
- \#184: restore daily social issue
- \#185: workflow_dispatch default
- \#187: single-adopter audit
- \#188: progressive disclosure restore
- \#178: brand icons in frontier circles

Day seventeen: audit hardening, masthead actions, and production polish.
