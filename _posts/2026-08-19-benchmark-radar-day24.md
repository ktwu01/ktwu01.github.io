---
title: "Benchmark Radar Day 24: Results-First Today View and Honest Empty States"
date: 2026-08-19
permalink: /posts/2026/08/benchmark-radar-day24/
tags:
  - AI
  - Benchmarks
  - Today View
  - Empty States
  - Issue Forms
  - Brand Marks
---

The Today view leads with results, and the radar stopped blaming the reader for an empty page. Day twenty-four redesigned the homepage and made the crawl's data availability visible.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

## What shipped

**Results-first Today view.** PR #249 reorders the Today view: matching results lead, the daily briefing and Q&A move to the right sidebar, and the filter bar becomes one compact row with a Filters (N) trigger whose badge counts active secondary filters.

**Homepage review applied.** PR #252 applies the #248 review: title-led rows, integer priority scores on the 100-point scale, no uppercase pill chips. The RECOMMENDED badge is removed because it flagged most top rows and communicated nothing.

**Case-insensitive source filter.** PRs #255 and #270 make the source filter case-insensitive, so `/?source=GitHub+Release` and `/?source=First-party+feed` work regardless of casing or + encoding.

**Saturation panel trimmed.** PR #258 reduces the saturation panel to the score curve only: the adoption staircase, advance diamonds, card rug, release marker, reporting-stage badge, counts line and milestones column are all removed. No line joins two score points.

**Weekly jargon audit.** PR #271 adds `scripts/audit_jargon.py`, which scans user-facing strings for 15 project-only terms and runs every Monday at 02:00 UTC. The first run found 25 hits.

**Show the sources that found nothing.** PR #274 makes the Source mix column list sources that returned zero, so the reader can tell "looked and found nothing today" from "this source does not exist."

**One form to report anything.** PR #275 replaces the picker menu with a single issue form of three fields, superseding #272 and #273.

**Say why the list is empty.** PR #277 stops telling the reader to "clear one or more filters" when no evidence was ever collected, finishing the half that #274 left open.

**Navigator claim corrected.** PR #247 corrects the audit's claim: the real gap is 79 of roughly 1,066 crawled benchmarks selectable, not 13 of 79. The findings are recorded in `OFFICE-HOURS-DISPLAY.md`.

**Real brand marks.** Issues #266 and #267 source real logos for the 24 organizations drawing a generic spark and fix five wordmarks that go illegible at chart size, resolving #261.

**Model-family audit.** Issue #268 surfaces 75 crawled models across 23 organizations that have no model-family card on the audit page.

**Crawl identity scoped.** Issue #259's crawl job is narrowed to 76 dense llm-stats benchmarks, with the 6 wrong `source_benchmark_ids` fixed first in #263.

## Why it matters

The Today view redesign puts the answer before the explanation. The briefing and Q&A no longer compete with the data; results lead, and everything else hangs off a single compact row.

The empty-state work is a matter of honesty. The radar now distinguishes "no data collected" from "no data exists," and it never blames the reader's filters for a gap in the crawl. A source that quietly stays at zero is usually a broken source, and the page now says so.

The jargon audit is a standing quality bar, not a one-off cleanup. Running it every Monday keeps user-facing text from drifting back into project-only vocabulary.

## Issues addressed

- \#247: navigator claim correction
- \#248: homepage UI review
- \#249: results-first Today view
- \#252: homepage review applied
- \#254: first-party feed and GitHub Release at zero
- \#255, \#270: case-insensitive source filter
- \#257: visual issue template field
- \#258: saturation panel trimmed
- \#259: crawl identity scoped
- \#260: source mix gaps shown
- \#261, \#266, \#267: real brand marks
- \#263: wrong source_benchmark_ids fixed
- \#268: model-family audit
- \#271: weekly jargon audit
- \#274: sources that found nothing
- \#275: one form to report anything
- \#277: why the list is empty

Day twenty-five: scores on their dates, and a radar that does not rank itself.