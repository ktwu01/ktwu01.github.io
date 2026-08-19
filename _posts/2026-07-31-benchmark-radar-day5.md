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

## What shipped

**Accessible hover card for trend chart.** The native browser tooltips on the trend chart were replaced with a custom hover card. It survives mixed input (mouse and trackpad), stays clear of tall bars, is exposed to screen readers, follows the column when the chart scrolls, and can be dismissed with Escape.

**Benchmark landscape report.** Issue #52 was rewritten as a full benchmark landscape report. The agentic benchmark count was corrected from 3 to 78, reflecting the actual scale of agent evaluation work in the ecosystem.

**Landscape TLDR.** A concise summary was added to make the landscape report scannable.

**Generated landscape figures.** Report figures were generated from the data and added to the documentation.

**Corpus totals panel defaulted open.** The panel was previously collapsed by default; now it opens automatically so users see the scale immediately.

## Why it matters

The hover card fix was an accessibility issue. Screen reader users could not interact with the trend chart. The new hover card is keyboard-accessible, follows focus, and announces itself to assistive technology.

The landscape report correction (3 to 78 agentic benchmarks) was a credibility moment. The radar had severely undercounted agent benchmarks because the taxonomy did not yet have an "agentic" category (added the previous day). Once the category existed, the actual count was startling. This is why taxonomy accuracy matters: wrong categories produce wrong counts, which produce wrong conclusions.

## Issues addressed

- \#52: corpus totals and agentic benchmark count correction
- \#59: corpus totals visibility
- \#60: trend hover card accessibility
- \#67: agentic benchmark count (3 to 78)
- \#68: benchmark landscape report
- \#69: trend hover card fixes
- \#71: landscape report figures
- \#73: hide duplicate report tables

Day six: Hacker News integration and scheduled radar reliability.
