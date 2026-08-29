---
title: "Benchmark Radar Day 21: OpenReview Authentication and Responsive Layout"
date: 2026-08-16
permalink: /posts/2026/08/benchmark-radar-day21/
tags:
  - AI
  - Benchmarks
  - OpenReview
  - Responsive Design
  - Performance
  - i18n
---

Hi, Koutian here. Day twenty-one was a fix day that touched many parts at once.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar is live.** Track new AI benchmarks, datasets, and leaderboards every day: [open the dashboard](https://benchmark-radar.org/) or [star it on GitHub](https://github.com/ktwu01/benchmark-radar).

OpenReview is the site that hosts peer reviews for the top AI conferences. Peer review is the process where other researchers grade a paper before it is accepted. We can now log into OpenReview's API v2 using the `openreview-py` client. That opens up review data from NeurIPS, ICML, ICLR, and other venues. A CI workflow, the automated test that runs on every change, now checks that login works so we catch broken credentials early.

The Chinese and English toggle button now responds to clicks. Before, the button was there but did nothing. It also shows the target script as a 中 / EN glyph instead of a plain label.

We fixed three phone layout problems. Icons now render correctly on small screens. The masthead wraps on narrow phones so the utility row does not spill over the edge. The mobile squares shrank to 2.1rem so they fit a 320px phone.

On wide screens the radar now uses more horizontal space (issue #223). We enlarged the header nav icons and cut the empty space on the right.

The dashboard is faster now. `radar.json`, the data file behind the page, is cached, and filter updates wait for you to pause typing before re-rendering (issue #222). The page no longer redraws on every keystroke.

Saturation scores, the points where benchmark scores flatten out, are now tagged with model logos. The chart explains itself. We widened the daily questions section for easier reading, and utility icons now give instant visual feedback when you tap them. We also restored the code formatter to a clean baseline after the language changes.

Why this matters to you.

OpenReview is the most useful change here. The radar can now track not just which benchmarks get released, but how the research community receives them. A benchmark that gets strong reviews at NeurIPS is more likely to be used than one that gets rejected. The phone and wide-screen fixes mean the site works whether you check it on a bus or on a big monitor. The speed fix means the filters feel instant instead of laggy.

Issues addressed:

- #220: mobile utility grid overflow
- #221: language toggle wiring
- #222: cache radar.json and debounce filters
- #223: wide-screen horizontal space
- OpenReview API v2 authentication
- Language glyph display
- Dashboard performance improvements
- Daily questions section width

Day twenty-two: data integrity, social cadence, and RSS feeds.

> Want to follow Benchmark Radar? [Star the repo on GitHub](https://github.com/ktwu01/benchmark-radar) for daily updates, or [open the live dashboard](https://benchmark-radar.org/) to explore the scans.
