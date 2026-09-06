---
title: "Benchmark Radar Day 37: Cite It, Set It Up, Search Everything"
date: 2026-09-01
permalink: /posts/2026/09/benchmark-radar-day37/
tags:
  - AI
  - Benchmarks
  - Citations
  - CLI
  - Search
  - Plain English
---

Day thirty-seven of Benchmark Radar. Anyone writing a paper can now copy a citation without leaving the dashboard, the offline setup moved onto the site, and search looks through every collected day by default. Scoreboard: 130 stars, 25 forks.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar is live.** Track new AI benchmarks, datasets, and leaderboards every day: [open the dashboard](https://benchmark-radar.org/) or [star it on GitHub](https://github.com/ktwu01/benchmark-radar).

A citation is the formal reference to a work, in a format such as APA or BibTeX. A pop-out is a small card that opens over the page. A byline is the list of authors on a document. A dependency is an external component a build relies on.

PR #480 adds a citation card at `/#cite`. Three formats are one click away: APA, BibTeX, and the citation file. The card carries fixed text, so it opens before the data loads, and where the browser blocks clipboard access, the citation is selected instead and the page says so.

PR #482 adds the CLI setup sheet at `/#cli`. A reader on the dashboard can now open the sheet and copy the one prompt to hand a coding agent, instead of leaving the site to find it in the README. Both sheets share one copy control and one clipboard handler.

PR #484 makes search look through all dates by default. A new query no longer inherits the newest scan; the first result row says the archive was searched, offers a direct link back to today, and points result sets over ten entries at the CLI setup for full export.

PR #489 adds Junjie Zhou to the technical report draft byline, keeps Koutian Wu as corresponding author, and adds a next-draft build flag that refuses to overwrite the published PDF. PR #485 and PR #486 bump the checkout and setup-python actions used in CI.

Why this matters.

A project people cannot cite is a project people cannot thank. Putting the citation on the page, next to the data, removes the last excuse for a reference list that leaves the work out.

The offline route was documented but not discoverable. A setup card inside the dashboard closes that gap, and search that covers the archive answers questions about any day, not just the latest one.

Issues addressed

- citation card at `/#cite` with APA, BibTeX, and citation-file formats
- #481: search all dates by default
- CLI setup sheet at `/#cli`
- #489: Junjie Zhou added to the technical report draft byline
- #485 and #486: GitHub Actions dependencies bumped
- scoreboard: 130 of 1,000 stars, 25 forks

Day thirty-eight: the dashboard keeps its face while every benchmark and the daily brief get pages search engines can read.

> Want to follow Benchmark Radar? [Star the repo on GitHub](https://github.com/ktwu01/benchmark-radar) for daily updates, or [open the live dashboard](https://benchmark-radar.org/) to explore the scans.