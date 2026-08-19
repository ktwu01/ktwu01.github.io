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

OpenReview got authenticated. Wide screens got wider. Phones stopped breaking. Day twenty-one was a cross-cutting fix day.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

## What shipped

**OpenReview API v2 authentication.** The radar can now authenticate with OpenReview's API v2 using the `openreview-py` client. This opens access to peer review data from NeurIPS, ICML, ICLR, and other venues.

**OpenReview auth test workflow.** A CI workflow tests the OpenReview authentication to catch credential issues early.

**Language toggle button wired.** The Chinese/English language toggle button was wired so it actually responds to clicks. Previously the button existed but did nothing.

**Language glyph display.** The toggle button now shows the target script as a 中/EN glyph instead of a generic label.

**Mobile utility grid fixes.** Three fixes addressed phone layout issues:
- Icons corrected to render properly on small screens
- Masthead wrapped on narrow phones so the utility grid does not overflow
- Mobile squares shrunk to 2.1rem to fit a 320px phone

**Wide-screen layout.** The radar now uses more horizontal space on wide screens (issue #223). Header nav icons were enlarged and right-side whitespace was reduced.

**Dashboard performance.** `radar.json` is now cached and filter re-renders are debounced (issue #222). This prevents the dashboard from re-rendering on every keystroke.

**Saturation score identification.** Saturation scores are now identified with model logos, making the chart self-documenting.

**Daily questions section widened.** The daily questions section was given more width for readability.

**Utility icon feedback.** Utility icon interactions now provide immediate visual feedback.

**Formatter baseline restored.** Code formatting was restored to a clean baseline after the i18n changes.

## Why it matters

The OpenReview authentication was the most strategically important change. OpenReview hosts peer reviews for the top AI conferences. Accessing this data means the radar can track not just which benchmarks are released, but how they are received by the peer review community. A benchmark that gets strong reviews at NeurIPS is more likely to be adopted than one that gets rejected.

The mobile fixes were a usability commitment. If the dashboard breaks on a 320px phone, it is unusable for anyone checking the radar on their commute. The wide-screen fix was the opposite end: on a 4K monitor, the radar should use the available space, not center itself in a narrow column.

## Issues addressed

- \#220: mobile utility grid overflow
- \#221: language toggle wiring
- \#222: cache radar.json and debounce filters
- \#223: wide-screen horizontal space
- OpenReview API v2 authentication
- Language glyph display
- Dashboard performance improvements
- Daily questions section width

Day twenty-two: data integrity, social cadence, and RSS feeds.
