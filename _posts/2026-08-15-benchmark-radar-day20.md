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

The radar spoke Chinese. Day twenty delivered full zh i18n, insight blocks, and a complete social checklist.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

## What shipped

**Full zh i18n dictionary.** A complete Chinese translation dictionary was added with static HTML wiring. Every UI string, label, and description has a Chinese equivalent.

**Chinese title.** The site title translates to "Benchmark 雷达日报" (Benchmark Radar Daily) in Chinese mode.

**Today page insight blocks.** The day scan now compiles into scannable insight blocks. Instead of reading through raw findings, users see structured summaries organized by significance.

**Social checklist overhaul.** The daily social checklist was overhauled:
- Personal and direct channels were dropped from the daily rotation
- Reddit subreddit links and Hacker News submit URL were added
- Weekly cadence channels were separated from daily channels
- Every daily checklist now leads with the records-count badge
- Non-daily channels render every day but are grouped separately

**Model cards added.** DeepSeek-V4-Pro-0813, GLM-5.1, GLM-5.2, Qwen3.8-27B, and AI2 OLMo 3 were added to the adoption registry.

**README simplified.** The README was simplified around core use cases. A data-driven record-count badge was published.

**Zh-CN README.** A Chinese README was added with the WeChat group QR code.

**Caveat exemption tightened.** The Q&A caveat-exemption was restricted: it no longer applies to non-category shares. An uncited score of 100 is now rejected by validation.

**Social test timezone fix.** Social test channels were marked as daily to avoid timezone-dependent test failures.

## Why it matters

The Chinese i18n was a market decision. The AI benchmark ecosystem has significant activity in China: DeepSeek, Qwen, GLM, and other Chinese model labs publish benchmarks frequently. Making the radar accessible in Chinese expanded its potential audience significantly.

The insight blocks were a UX improvement for information density. Raw findings require interpretation; insight blocks deliver pre-interpreted summaries. This matters for users who scan the dashboard in thirty seconds rather than studying it for thirty minutes.

The social checklist overhaul reflected a shift from "post everywhere" to "post where it matters." Personal channels were noise; Reddit and Hacker News were signal.

## Issues addressed

- \#197: records badge and zh-CN README
- \#201: simplify README
- \#203: Today page insight blocks
- \#206: social checklist overhaul
- \#207: Q&A uncited score rejection
- \#210: records badge daily
- \#211: insight blocks
- \#213: icon fixes
- \#216: zh i18n dictionary
- \#217: social test timezone fix
- Model card additions (DeepSeek, GLM, Qwen, OLMo)

Day twenty-one: OpenReview auth, wide-screen layout, and mobile fixes.
