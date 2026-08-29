---
title: "Benchmark Radar Day 20: Full Chinese Language Support and Insight Blocks"
date: 2026-08-15
permalink: /posts/2026/08/benchmark-radar-day20/
tags:
  - AI
  - Benchmarks
  - i18n
  - Chinese
  - UX
  - Social Media
---

Hi, Koutian here. Day twenty taught the radar to speak Chinese and to summarize itself.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar is live.** Track new AI benchmarks, datasets, and leaderboards every day: [open the dashboard](https://benchmark-radar.org/) or [star it on GitHub](https://github.com/ktwu01/benchmark-radar).

i18n means internationalization, which is just the setup that lets a site show more than one language. We added a full Chinese dictionary with the static HTML wiring, so every label and description on the site now has a Chinese version. In Chinese mode the site title reads "Benchmark 雷达日报", which means Benchmark Radar Daily.

The Today page now compiles the day's scan into short insight blocks. Instead of a wall of raw findings, you see small summaries sorted by how important they are. You can grasp the day in thirty seconds instead of studying it for thirty minutes.

We overhauled the daily social checklist. We dropped the personal and direct channels that were just noise. We added Reddit subreddit links and the Hacker News submit URL, which is where the real signal lives. Weekly channels are now split from daily ones. Every daily checklist now leads with a badge showing the record count. Non-daily channels still show every day but sit in their own group.

We added model cards to the adoption registry for DeepSeek-V4-Pro-0813, GLM-5.1, GLM-5.2, Qwen3.8-27B, and AI2 OLMo 3. A model card is a short profile that records a model's key facts. We simplified the README around the core use cases and published the record-count badge. We also added a Chinese README with the WeChat group QR code.

We tightened the Q&A caveat rule. It no longer applies to shares that are not in a category. An uncited score of 100 now gets rejected by validation, so a fake-looking number cannot slip through.

We marked the social test channels as daily so timezone differences stop causing test failures.

Why this matters to you.

The Chinese support is a reach decision. China's AI labs, DeepSeek, Qwen, GLM, and others, post benchmarks often. A Chinese UI opens the radar to a much larger audience. The insight blocks save you time: the dashboard now does the first pass of reading for you. The social change means we post where people actually look, not everywhere at once.

Issues addressed:

- #197: records badge and zh-CN README
- #201: simplify README
- #203: Today page insight blocks
- #206: social checklist overhaul
- #207: Q&A uncited score rejection
- #210: records badge daily
- #211: insight blocks
- #213: icon fixes
- #216: zh i18n dictionary
- #217: social test timezone fix
- Model card additions (DeepSeek, GLM, Qwen, OLMo)

Day twenty-one: OpenReview auth, wide-screen layout, and mobile fixes.

> Want to follow Benchmark Radar? [Star the repo on GitHub](https://github.com/ktwu01/benchmark-radar) for daily updates, or [open the live dashboard](https://benchmark-radar.org/) to explore the scans.
