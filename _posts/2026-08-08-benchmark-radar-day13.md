---
title: "Benchmark Radar Day 13: Dashboard Polish and Evidence Grounding"
date: 2026-08-08
permalink: /posts/2026/08/benchmark-radar-day13/
tags:
  - AI
  - Benchmarks
  - Evidence
  - Q&A
  - Favicon
---

Every claim now links to its source. Day thirteen added evidence grounding, daily Q&A, and several UX fixes.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

## What shipped

**Favicon.** The site finally got an icon. Small detail, big identity signal.

**URL parameter scoping.** Filters are now written only for the active view into the URL. Previously, all views' filters leaked into the URL, creating confusion when switching between views.

**Daily Q&A on dashboard.** The daily Q&A section is now rendered on the dashboard, making the radar's self-questions and answers visible to users.

**Briefing evidence grounding.** The daily briefing now answers questions instead of only listing findings. Each answer is grounded in specific evidence sources. 80% of previously discarded briefing evidence was recovered.

**KW-Bench rubric owned.** The KW-Bench rubric is now maintained within this repository instead of being an external dependency.

**Benchmark builder survey.** A survey of who builds the popular benchmarks was added (#164).

**Trajectory points inspectable.** Points on the trajectory chart can now be clicked or focused to reveal details.

**Complete contact inventory.** The benchmark contact CSV export now includes the complete inventory.

**OpenAlex null title fix.** Untitled OpenAlex works no longer crash the daily run. They are skipped with a warning.

## Why it matters

Evidence grounding was the most important change of the day. A radar that says "benchmark X is trending" without citing where that claim comes from is just opinion. A radar that says "benchmark X appeared in 3 model cards this week (GPT-4 card line 42, Claude card line 18, Gemini card line 31)" is evidence.

The URL parameter scoping fix addressed a real user confusion: when you shared a URL, it carried filters from views the recipient was not looking at. Scoping filters to the active view made URLs actually represent what they showed.

## Issues addressed

- \#160: URL parameter view scoping and favicon
- \#161: OpenAlex null title fix
- \#162: briefing evidence starvation
- \#159: render daily Q&A
- \#163: trajectory interactions
- \#164: benchmark builder survey
- \#166: render daily questions on dashboard
- \#167: complete contact CSV
- \#168: trajectory point inspection

Day fourteen: feed coverage, briefing reliability, and production Q&A.
