---
title: "Benchmark Radar Day 40: A Source for Papers, a Benchmark Restored, a Wider Broadcast"
date: 2026-09-04
permalink: /posts/2026/09/benchmark-radar-day40/
tags:
  - AI
  - Benchmarks
  - Discovery
  - Social
  - Open Source
  - Plain English
---

Day forty of Benchmark Radar. The radar started watching the network where most new benchmark papers get their DOI, brought a benchmark back by searching its exact name, and started posting where it was not posting before. Scoreboard: 147 stars, 27 forks.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar is live.** Track new AI benchmarks, datasets, and leaderboards every day: [open the dashboard](https://benchmark-radar.org/) or [star it on GitHub](https://github.com/ktwu01/benchmark-radar).

A DOI is the permanent identifier a publisher assigns to a paper, and Crossref is the organization that assigns most of them. Recursive self-improvement means a system that works on improving its own capability to improve. A checklist is the complete ranked list of destinations and actions the daily social routine follows.

PR #546 adds Crossref as an optional daily discovery source. The radar now queries it for recent DOI-bearing benchmark papers, keeps the DOI identity, authors, affiliations, and citation counts, and rejects malformed or future-dated records. Crossref needs no API key, so the new source adds no secret.

PR #495 restores RSI-Exam. The suite tests executable recursive self-improvement across 88 tasks and six domains, but the GitHub connector never searched its exact name, so it failed discovery and would not have been eligible if fetched. An exact-name query and a named watchlist bring it back, while unrelated trading and safety repositories stay out.

PR #538 and PR #539 widen the broadcast. The daily social issues become complete ranked traction checklists covering all 94 destinations and actions, with 11 reusable post examples. Bilibili moves into the daily distribution block, and WhatsApp Communities, Pinterest, Snapchat, and Quora join as US-facing weekly channels.

PR #536 simplifies the shared chrome to the essentials: RSS, language, contact, and stars. PR #537 adds Junjie Zhou as the second author across citation surfaces, and PR #542 adds Jiayu Wang's completed real use case to the report draft with six screenshots and extends the byline.

Why this matters.

Benchmark papers announce themselves with a DOI before most other traces exist. Watching Crossref closes a gap most radars leave open, and it does so without a single credential.

A discovery blind spot for a suite as unusual as RSI-Exam is a lesson in exact names. Repositories are found by the words in them, so a benchmark whose name no query contained was invisible until the query was written down.

Distribution is part of an open-source project's job. A ranked checklist makes the daily broadcast repeatable, and new channels reach readers who never check GitHub.

Issues addressed

- #506: Crossref added as an optional daily discovery source
- #408: RSI-Exam discovered by its exact name
- #412: Bilibili and US-facing channels added to the checklist
- #532: shared chrome simplified
- #492: Jiayu Wang real use case and byline added to the report draft
- scoreboard: 147 of 1,000 stars, 27 forks

Day forty-one: a ranking engine for fresh releases, locked down by a data contract before the UI changes.

> Want to follow Benchmark Radar? [Star the repo on GitHub](https://github.com/ktwu01/benchmark-radar) for daily updates, or [open the live dashboard](https://benchmark-radar.org/) to explore the scans. Read the paper: [arXiv:2609.11115](https://arxiv.org/abs/2609.11115).