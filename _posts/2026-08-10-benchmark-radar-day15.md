---
title: "Benchmark Radar Day 15: Social Media Pipeline and WeChat Integration"
date: 2026-08-10
permalink: /posts/2026/08/benchmark-radar-day15/
tags:
  - AI
  - Benchmarks
  - Social Media
  - WeChat
  - CI/CD
---

The radar started posting to social media. Day fifteen built that pipeline and retired the daily GitHub Issue.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

Hi, Koutian here. A GitHub Issue is just a tracked to-do or note on the project page. We used to open one every day. Now the radar writes social posts instead.

We built a generator that turns each day's findings into posts ready to share. It formats them per platform, so the same news fits WeChat (a Chinese messaging app), Reddit, and Hacker News without you rewriting it.

We added a WeChat checklist with copy in Chinese that you can post as-is. That lowers the bar for sharing the project with Chinese readers.

The daily GitHub Issue is gone. The build pipeline used to open one every morning. Now it writes the social material to a CI artifact, which is a file the pipeline keeps for you. Less clutter in the issue tracker, same content.

When we merge several days of data, that evidence now flows into items.json so the social pipeline sees it. We also fixed the daily channel flag, so pre-set social config actually fires and the tracking ticks survive the merge.

Each Q&A answer now carries a small ID that points back to the exact data it came from. If you doubt an answer, you can trace it.

We cleaned the README and code comments to drop the retired daily Issue.

Why this matters.

This was the radar's first outbound channel. Before, it collected data and showed a dashboard. Now it hands you posts you can drop onto WeChat, Reddit, or Hacker News. The radar stopped being a quiet log and started being a service.

Killing the daily Issue cut noise. It helped early on, but it turned into clutter. Moving the material to artifacts keeps it available without flooding the tracker.

Issues addressed

- #180: generate daily social posts
- #181: remove the retired daily Issue from the README
- #182: add traceable IDs to Q&A answers
- social post section generator
- WeChat channel checklist
- merged-day evidence routing

Day sixteen: single-adopter audit, progressive disclosure, and daily social issue restoration.
