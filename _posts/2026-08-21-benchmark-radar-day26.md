---
title: "Benchmark Radar Day 26: The Ranking Leads, Back Finally Works, and a Frontier That Tells the Truth"
date: 2026-08-21
permalink: /posts/2026/08/benchmark-radar-day26/
tags:
  - AI
  - Benchmarks
  - Leaderboard
  - Navigation
  - Charts
  - Plain English
---

Day twenty-six of Benchmark Radar. We put the ranking where it belongs, made the Back button work, and replaced an invented chart with one we can draw.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

A ranking is an ordered list from most to least. The Back button is the browser arrow that returns you to the last page. A frontier line is a stepped line that connects the best score seen so far. A stale banner is the warning shown when the page is out of date.

PR #302 fixes four things on the same two pages, the leaderboard and the per-benchmark chart. First, the ranking now leads `?view=leaderboard`. It used to be the sixth block on the page, collapsed behind a method note, an evidence strip, a findings panel, a search box, and a 480px chart. Now you see a five-line summary first and the full 80-row table right under it. The table keeps its filter, its show-all toggle, and its collapsed default, so no link breaks. The ranking and the chart now agree by design: the chart opens on rank 1, which is GPQA Diamond, not on the newest instrument we happened to crawl.

PR #302 also fixes Back navigation. Every address change had used `replaceState`, which overwrites the current history entry instead of adding a new one. So searching, opening a benchmark, and pressing Back left the site. Now eight kinds of navigation push a new entry, like changing the view, picking a benchmark, or following a finding, while six kinds still replace, like typing in the filter box. A `popstate` listener re-renders the restored address, so Forward works too. Typing `mmlu` does not add a history entry on every keystroke, but picking a benchmark does.

PR #302 also changes the chart. The request was for a Pareto frontier like `harbor-index.org`, but Harbor plots cost against accuracy, and this collection has no cost for any score. Inventing that axis would be lying. Instead we draw a running best: a flat step, then a vertical jump when a later model beats the record, with no diagonal that suggests values between points. The idea is the same, but on axes we have. For crawled scores we do not draw the line at all, because those rows have no shared measure to compare. The title was also cut from four repeating labels to one title plus one short subline, axes gained middle ticks, and search rows were trimmed to name plus one count so three `not established` fields do not fill the screen.

Five follow-up commits in the same PR moved the figure above the fold. On a 1440 by 900 screen the chart started at 1356px, behind about 1180px of cards and tables that were summarizing the very thing they hid. It now starts at 567px, so about 57 percent is visible on load, without shrinking its 480px height. Three headings that said the same sentence in different words became one. The explainer text was rewritten so it does not need words like saturated or vendor attention, and it now ships with the data in `radar.json` instead of living only in the browser. The disclosure arrow grew from about 16px to a 48px hit area, the legend moved under the chart, and the search sidebar changed from the page background color to a real grey so it no longer looks like it is floating.

PR #306 pins the repair for a dead benchmark slug in `?lfrontier=`. Before, visiting a slug that does not exist left the bad slug in the address bar while the panel showed the default chart, GPQA Diamond. Now all four tested shapes, `does-not-exist`, `llm-stats-deleted-benchmark`, `opencompass-9999-gone`, and `not_a_canonical_id`, clear the bad slug and show GPQA Diamond. Pressing Back after visiting `llm-stats-aime-2025` and picking another benchmark returns to `llm-stats-aime-2025` with the heading still matching. The fix lives at the point where the requested entry is looked up and not found.

PR #308 rewrites the stale banner in plain language and adds two buttons, an explanation of what broke and a contact link. The banner used to sound like a system error. Now it tells you the data is old and gives you two things to do. On the server side the same PR surfaces the numbers behind an OpenAI rate limit, so an error about the daily briefing now includes the quota that ran out instead of just saying it failed.

Why this matters.

The ranking change is about honesty in layout. A page named after a ranking that you cannot see asks you to trust a chart before it has shown you the count behind it. Putting five lines and a table before a 480px figure lets you read the answer before the explanation, and opening on rank 1 means the first chart you see matches the top row above it.

The Back fix is about trust in navigation. If every click replaces the last address, the browser stops being a way back and becomes a trap. Making eight navigations push and six replace keeps the history true to what you did, so exploring and returning does not punish you.

The frontier choice is about not drawing what you do not have. A Pareto line needs two measures. Without cost, any diagonal would invent a trade-off the data never made. A stepped running best only says nothing had beaten this value yet, which is exactly what the dated scores support, and dropping it for crawled rows where even that claim fails keeps the line honest.

Issues addressed

- #256: ranking leads the leaderboard page
- #286: Back and Forward work across views
- #288: stepped running best instead of an invented axis
- #298: one title and readable axes
- #304: dead `lfrontier` slug clears the address bar
- figure now above the fold with honest copy shipped in `radar.json`
- stale banner rewritten with two actions
- OpenAI quota surfaced on rate-limit errors

Day twenty-seven: paging the Today list, halving a title, and naming 21 benchmarks correctly.
