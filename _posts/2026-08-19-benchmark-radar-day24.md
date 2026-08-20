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

Day twenty-four of Benchmark Radar. We put the results first on the homepage, and we stopped blaming you when a page came up empty.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

A "filter" is a control that narrows what you see. A "sidebar" is a narrow column beside the main content. A "wordmark" is the text version of a logo.

PR #249 reorders the Today view. The matching results now lead. The daily briefing and the Q&A move to the right sidebar. The filter bar becomes one compact row with a "Filters (N)" button whose badge counts the active extra filters. You see the answer before the explanation.

PR #252 applies the earlier review from #248. Rows now lead with the title. Priority scores show as whole numbers on the 0-100 scale. We dropped the uppercase pill chips. The RECOMMENDED badge is gone too, because it flagged almost every top row and told you nothing. The page is honest about what is actually on top.

PRs #255 and #270 make the source filter ignore letter case. So `/?source=GitHub+Release` and `/?source=First-party+feed` both work, no matter the casing or the plus sign. Links from other sites will not break on you.

PR #258 trims the saturation panel down to just the score curve. We removed the adoption staircase, the advance diamonds, the card rug, the release marker, the reporting-stage badge, the counts line, and the milestones column. No line now joins two score points. The chart is easier to read at a glance.

PR #271 adds `scripts/audit_jargon.py`. It scans the user-facing text for 15 project-only terms and runs every Monday at 02:00 UTC. The first run found 25 hits. We now catch our own confusing words on a schedule.

PR #274 makes the Source mix column also list sources that returned zero. That way you can tell "we looked and found nothing today" from "this source does not exist." You can spot a broken source instead of guessing.

PR #275 replaces the picker menu with a single issue form of three fields. It replaces #272 and #273. Reporting a problem is now one form, not a menu maze.

PR #277 stops telling you to "clear one or more filters" when we never collected any evidence at all. It finishes the half that #274 left open. The page no longer blames your settings for a hole in our crawl.

PR #247 corrects an earlier audit claim. The real gap is 79 of about 1,066 crawled benchmarks being selectable, not 13 of 79. We wrote the findings in `OFFICE-HOURS-DISPLAY.md`. We fixed a number we had wrong before.

Issues #266 and #267 swap in real logos for 24 organizations that were showing a generic spark. We also fixed five wordmarks that went unreadable at chart size, which closes #261. The charts now show real brand marks, not a placeholder.

Issue #268 surfaced 75 crawled models across 23 organizations that have no model-family card on the audit page. We now know which models are missing a profile.

Issue #259's crawl job is now narrowed to 76 dense llm-stats benchmarks. We fixed the 6 wrong `source_benchmark_ids` first in #263. The crawl targets the right benchmarks and the bad ids are corrected.

Why this matters.

The Today view puts the answer before the explanation. The briefing and Q&A no longer fight the data for space. Results lead, and everything else hangs off one compact row.

The empty-state work is about honesty. The radar now tells "no data collected" apart from "no data exists," and it never blames your filters for a gap in the crawl. A source stuck at zero is usually a broken source, and the page now says so.

The jargon audit is a standing quality bar, not a one-time cleanup. Running it every Monday keeps the user-facing text from sliding back into project-only words.

Issues addressed

- #247: navigator claim correction
- #248: homepage UI review
- #249: results-first Today view
- #252: homepage review applied
- #254: first-party feed and GitHub Release at zero
- #255, #270: case-insensitive source filter
- #257: visual issue template field
- #258: saturation panel trimmed
- #259: crawl identity scoped
- #260: source mix gaps shown
- #261, #266, #267: real brand marks
- #263: wrong source_benchmark_ids fixed
- #268: model-family audit
- #271: weekly jargon audit
- #274: sources that found nothing
- #275: one form to report anything
- #277: why the list is empty

Day twenty-five: scores on their dates, and a radar that does not rank itself.
