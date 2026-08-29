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

The radar now backs up every claim with a link. Day thirteen added evidence grounding, a daily Q&A on the dashboard, and a stack of small fixes.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar is live.** Track new AI benchmarks, datasets, and leaderboards every day: [open the dashboard](https://ktwu01.github.io/benchmark-radar/) or [star it on GitHub](https://github.com/ktwu01/benchmark-radar).

Hi, Koutian here. A leaderboard is just a public ranking of who scored best, and we have one. We spent the day making that ranking honest and easy to read.

We gave the site an icon, finally. It is the small picture in your browser tab, and it makes the project feel real instead of a blank page.

Filters now stay where you expect them. Before, the web address (the URL) carried filters from every view at once. Switch views and you got settings for a page you were not even looking at. Now the URL only records the view you are on, so a link you share shows exactly what you saw.

The daily Q&A now shows up on the dashboard. Each day the radar asks itself questions about the benchmark world and answers them. Now you can read those questions instead of them living in a hidden file.

The daily briefing changed shape. It used to just list findings. Now it answers questions, and every answer points at the source it came from. We recovered about 80% of the evidence we used to throw away, so the briefing got much fuller.

A model card is a short public sheet where a lab describes one of its AI models. We also pulled the KW-Bench rubric, our grading checklist for benchmarks, into this repository. It used to live outside as a dependency, so now it cannot break underneath us.

We added a survey of who builds the popular benchmarks (issue #164). You can now click points on the trajectory chart to see what they mean. The contact CSV export now lists the full set of benchmark contacts. And until now, a research paper with no title in OpenAlex (a free catalog of papers and authors) could crash the daily run. We skip those now with a warning.

Why this matters.

The evidence grounding was the big one. A radar that says "benchmark X is trending" with no source is just an opinion. A radar that says "benchmark X showed up in three model cards this week, here are the line numbers" is proof you can check yourself.

The URL fix solved a real annoyance. You share a link, and the person who opens it sees the filters you meant, not leftover settings from a different page.

Issues addressed

- #160: scope URL filters to the active view and add the site icon
- #161: stop OpenAlex papers with no title from crashing the run
- #162: fix the briefing running out of evidence
- #159: show the daily Q&A
- #163: let users click trajectory points
- #164: survey of who builds popular benchmarks
- #166: render daily questions on the dashboard
- #167: full contact list in the CSV
- #168: click trajectory points for details

Day fourteen: feed coverage, briefing reliability, and production Q&A.

> Want to follow Benchmark Radar? [Star the repo on GitHub](https://github.com/ktwu01/benchmark-radar) for daily updates, or [open the live dashboard](https://ktwu01.github.io/benchmark-radar/) to explore the scans.
