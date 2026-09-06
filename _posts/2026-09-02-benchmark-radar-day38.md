---
title: "Benchmark Radar Day 38: A Blog Built From Evidence"
date: 2026-09-02
permalink: /posts/2026/09/benchmark-radar-day38/
tags:
  - AI
  - Benchmarks
  - Blog
  - SEO
  - CLI
  - Plain English
---

Day thirty-eight of Benchmark Radar. The daily brief, the thing the project already wrote every day and never gave a page, now has a blog and a feed. Scoreboard: 137 stars, 26 forks.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar is live.** Track new AI benchmarks, datasets, and leaderboards every day: [open the dashboard](https://benchmark-radar.org/) or [star it on GitHub](https://github.com/ktwu01/benchmark-radar).

A blog is a set of dated pages, one per day. An RSS feed is a machine-readable list that readers and apps subscribe to. A snapshot is the stored record of one day's collection. A briefing is the short daily summary of what moved.

PR #476 gives the daily brief a home. The briefings, questions, caveats, and coverage numbers that were written into every snapshot and never displayed now publish at `/blog/`, with a landing page, a full archive, and an RSS feed. The leaderboard, trends, and explore views return real HTML in the same visual language, and translated posts use one canonical URL with a same-page toggle.

PR #494 makes a briefing source directly clickable. When the day's evidence resolves to exactly one validated citation, the single source chip becomes a link to it; multi-source chips stay as counts rather than ambiguous links.

PR #507 ends every query CLI round with a citation reminder. A single source file mirrors the citation file and the version number, so a release bumps the citation without a second edit, and in machine mode the reminder rides on the error stream so the data stays clean.

PR #505 fixes Today rendering empty after a sheet is closed or Back is pressed, and PR #509 pushes the contributors image straight to main using an app token and a path allowlist instead of an unreviewed write. PR #517 reduces the Agent Skill setup to one command and lets the agent detect and repair a broken CLI itself.

Why this matters.

Evidence that is written but never published might as well not exist. A blog gives the daily record a URL, a feed gives it subscribers, and both are built from the snapshot alone, with no model call at build time.

A citable CLI is part of the scientific loop. Ending every query round with a citation ask is a small nudge that compounds every time someone uses the tool.

Issues addressed

- #448: evidence blog and static pages while preserving the dashboard UI
- #467: singular briefing sources directly clickable
- #483: every CLI round ends with a citation reminder
- #503: Today renders empty after closing a sheet or pressing Back, fixed
- #516: Agent Skill setup reduced to one command
- scoreboard: 137 of 1,000 stars, 26 forks

Day thirty-nine: the daily brief gets a landing page, an archive, and a feed of its own.

> Want to follow Benchmark Radar? [Star the repo on GitHub](https://github.com/ktwu01/benchmark-radar) for daily updates, or [open the live dashboard](https://benchmark-radar.org/) to explore the scans.