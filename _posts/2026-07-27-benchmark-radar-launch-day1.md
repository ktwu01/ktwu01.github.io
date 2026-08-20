---
title: "Benchmark Radar Day 1: Building the Cumulative Dashboard MVP"
date: 2026-07-27
permalink: /posts/2026/07/benchmark-radar-launch-day1/
tags:
  - AI
  - Benchmarks
  - Open Source
  - Launch
---

Day one of Benchmark Radar. We went from nothing to a working daily dashboard in a single day.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

Hi, Koutian here. On day one, Benchmark Radar went from a blank page to a dashboard that quietly collects data every day. In one go, twenty chunks of work (we call each one a "commit") landed. They touched everything: the automatic build pipeline, how we store data, the daily view, and a backup plan for when the main source fails.

Here is what we built.

We set up the automatic pipeline. It now uses the latest versions of its tools, so it stays in step with the rest of the ecosystem.

The dashboard now saves each day's full set of data instead of throwing it away at the end of the day. That is the heart of the project: a growing record you can look back on.

We fixed some bugs where the dashboard showed the wrong numbers. Now what you see matches what the pipeline actually collected.

When the main arXiv search is down, the system now falls back to the RSS feed. arXiv search gets rate-limited, so this backup keeps the daily run alive instead of failing.

The main page is now short enough to read in thirty seconds.

Why this matters.

The hard part of a radar is not collecting data. It is making yesterday's data still useful tomorrow. So our first promise was to save every daily scan. Without that, the radar would forget everything overnight, and the whole idea falls apart.

The backup feed was also an important early choice. The main source fails sometimes. RSS is lower quality but tougher. Having both from day one means the daily run does not break when arXiv blocks the crawler.

Next up: trend maps over time, cleanup, and more sources.
