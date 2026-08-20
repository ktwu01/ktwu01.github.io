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

Day twenty-two of Benchmark Radar. We locked down data integrity and opened up the community.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

A "PR" is a proposed change to the code. An "issue" is a tracked to-do or bug. A "README" is the main info page for a project. We used all three a lot today.

We protected the daily snapshots from stale runs. A stale run is old data from a delayed trigger. Before today, that old data could overwrite a newer snapshot. PR #235 fixes this, and we marked it P1, which means high priority for data integrity. This means the dashboard will not quietly replace good data with old data.

The GitHub Pages build now also runs when we change packages, not only when we change source code. That keeps the live site in step with its dependencies. You will not see a site that lags behind its own code.

We added QR codes for the WeChat group to both the English and Chinese READMEs. WeChat is a Chinese messaging app, and it is where most Chinese AI builders talk. You can join the group with one scan.

We documented how often we post to social channels and updated the channel list. You now know when to expect a post.

We fixed benchmark URLs and dates across the registry. That was issue #98. The links and dates now actually match reality.

We added RSS feeds for the major LLM providers. An RSS feed is a simple list of new posts. We also added scorecard pairs that link a model release to its benchmark results. This means you see how the models actually scored on those benchmarks.

We hardened the Chinese translation checks against review findings, and ran our formatter (ruff) on those files. The Chinese text stays correct.

We rewrote the Chinese README for clarity and added the current project status. Chinese readers get accurate, up to date info.

The daily GPT-written summary now shows in Chinese when the site is in Chinese mode. That was issue #231. Chinese readers get the summary in their own language.

We simplified the Explore view (#242) so it has less clutter. The page is easier to scan.

Why this matters.

The stale-run fix was the most important one today. If the radar overwrites fresh data with old data, you stop trusting it. A radar you cannot trust is worse than no radar at all.

The WeChat QR codes lower the bar to join the community. More eyes on the project means more people can report bad data.

The LLM RSS feeds changed what the radar covers. Before, it tracked which benchmarks exist. Now it also tracks how models score on those benchmarks. That is a bigger net.

Issues addressed

- #230: dashboard UX revisit
- #231: GPT prose in Chinese
- #232: benchmark URLs and dates fix plus RSS feeds
- #235: P1 data integrity, stale run protection
- WeChat group QR codes
- social channel posting schedule
- Chinese translation checks hardened
- Explore view simplified

Day twenty-three: external catalog and leaderboard navigator.
