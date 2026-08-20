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

Some benchmarks were counted wrong, and the dashboards were overwhelming. Day sixteen fixed both.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

Hi, Koutian here. A leaderboard is just a public ranking of who scored best. Ours had a quiet bug, and the pages were too busy. We cleaned both up.

Benchmarks adopted by only one model card were being under-counted. A model card is a short public sheet where a lab describes one of its AI models. The fix now counts them correctly, even when just one lab picked them up.

Drill-down sections are now collapsed by default on the leaderboard, the Q&A, and the homepage. You click to open what you want instead of facing everything at once. This is called progressive disclosure: show the summary, hide the detail until asked.

We brought back the daily social-checklist issue after retiring it by mistake. Its date now comes from the report, not the computer's clock, so it no longer lands on the wrong day across time zones.

Manual pipeline runs now publish by default (issue #88). Before, you had to tick a box every time you ran it by hand. A workflow_dispatch is just a manual button to start the build, and now it does the expected thing.

The frontier circles on the chart now show real brand icons: OpenAI, Google, Anthropic, and others, instead of plain dots. The frontier is the edge of which models adopt which benchmarks, and the icons make it scannable at a glance.

Why this matters.

The count fix was about trust. If a one-adopter benchmark shows as zero, the adoption map looks less diverse than reality. For a tool that tracks adoption, a wrong count is a broken promise.

Progressive disclosure is about not drowning people. The radar grabs a lot of data. Collapsing it lets a quick visitor read the summary and a researcher expand what they need.

The brand icons save you a legend. See the OpenAI mark next to a point and you know who adopted it without hunting.

Issues addressed

- #88: default manual runs to publish, bring back the daily social issue, date it from the report
- #99: fix under-counted single-adopter benchmarks
- #183: restore progressive disclosure
- #184: bring back the daily social issue
- #185: default the manual publish flag
- #187: audit single-adopter counts
- #188: restore progressive disclosure
- #178: brand icons in frontier circles

Day seventeen: audit hardening, masthead actions, and production polish.
