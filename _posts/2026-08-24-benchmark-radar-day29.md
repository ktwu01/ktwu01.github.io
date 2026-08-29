---
title: "Benchmark Radar Day 29: Releases Before Updates, Scores on 0 to 100, and a Nav That Looks Active"
date: 2026-08-24
permalink: /posts/2026/08/benchmark-radar-day29/
tags:
  - AI
  - Benchmarks
  - Ranking
  - Scaling
  - Briefing
  - Navigation
---

Day twenty-nine of Benchmark Radar. We ranked new releases before routine updates, put a 0 to 1 score on a 0 to 100 scale without changing its value, and made the active tab stay active.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar is live.** Track new AI benchmarks, datasets, and leaderboards every day: [open the dashboard](https://ktwu01.github.io/benchmark-radar/) or [star it on GitHub](https://github.com/ktwu01/benchmark-radar).

A release is a brand-new benchmark that did not exist before. An update is a change to something we already listed, like a version bump or a new score. A 0 to 1 score and a 0 to 100 score can show the same value with a different ruler.

PR #349 covers three linked fixes that shipped together as one release. The first is display scaling for the leaderboard. Crawled `llm-stats` scores are stored as 0 to 1, like 0.72, but the rest of the site speaks in 0 to 100. The chart geometry was already right, only the labels and the tooltip read off by a factor of 100. Now the display multiplies by 100, so 0.72 reads as 72, without changing the stored value or moving any point. A point at 72 on a 0 to 100 axis is still the same dot it was.

The second is ranking order. The radar used to intermix fresh releases and routine updates by the same age rank. Now releases rank ahead of updates, and within releases the freshest tier reaches page one first. That is done by grading the day's releases by age, so a benchmark published today outranks one from two weeks ago even if their relevance scores are close. Before, a new release could sit on page three behind a run of updates to older benchmarks. Now the first page shows what is new before what just changed.

The third is briefing selection. The daily briefing is a short GPT-written summary of what moved today. It used to read the unranked evidence and could be vetoed by a negative category-composition check, so a day dominated by one kind of benchmark could suppress the very releases the ranking now surfaces. Now it reads the release-first ranked evidence, and that composition check no longer vetoes release-level insights. The headline and the ranking therefore read from the same ordered list.

The same PR also quiets the site. Horizontal overflow was removed so the page no longer scrolls sideways on narrow screens. Visual rules were softened, all-caps labels were dropped, and a decorative face was removed. On the chart, record-setting points are drawn 1.5 times larger and points off the running-best line no longer dissolve until you hover; they stay readable at rest.

PR #350 fixes the navigation active state. Before, only some tabs looked active because Today, Leaderboard, Trends, Explore, and the Rubric dialog each used a slightly different class or relied on a different attribute. Now one shared active class drives all five, with correct ARIA semantics for routed views and for the Rubric dialog. Closing the Rubric restores the underlying view state that was underneath it, so the highlighted tab after the dialog closes is the view you actually returned to. Regression coverage was added for anchors, buttons, and dialog state.

Why this matters.

Releases before updates changes what page one means. Page one should answer what is new today, not what got a small edit today. Tiering releases by age makes freshness a ranking input rather than a filter you have to remember to set.

Scaling 0 to 1 onto 0 to 100 without moving the dots keeps the store and the picture consistent. The value was already right; only its label was wrong by two decimal places. Fixing the label instead of the geometry avoids a silent rewrite of history.

A nav that does not look active is not active for the reader. If the highlighted tab drifts from the view on screen, or forgets where you were before a dialog, you stop trusting the chrome. One shared class plus restored dialog state makes the highlight match the view at every step, including after you close something.

Issues addressed

- #341: crawled 0 to 1 scores displayed on a 0 to 100 scale
- #333: releases ranked ahead of updates, freshest tier reaches page one
- #332: horizontal overflow removed, visual treatment quieted, record points at 1.5x
- briefing now reads release-first ranked evidence with no veto from category composition
- #350: one shared active class for all nav items with ARIA and Rubric restore

Day thirty: one-line release summaries for every card you scan.

> Want to follow Benchmark Radar? [Star the repo on GitHub](https://github.com/ktwu01/benchmark-radar) for daily updates, or [open the live dashboard](https://ktwu01.github.io/benchmark-radar/) to explore the scans.
