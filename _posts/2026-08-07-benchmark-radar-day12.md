---
title: "Benchmark Radar Day 12: Daily RSS Feed from Snapshot History"
date: 2026-08-07
permalink: /posts/2026/08/benchmark-radar-day12/
tags:
  - AI
  - Benchmarks
  - RSS
  - Syndication
  - Automation
---

The radar now has an RSS feed. Day twelve was a small day, one feature, but it changes how you follow the project.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

Hi, Koutian here. RSS is a simple way to subscribe to updates, like a bookmark that fills itself in. You paste the feed link into any RSS reader and new items show up without visiting the site. No email signup, no API key, no setup.

We added a step to the automatic build pipeline (a PR is a proposed change to the code, and CI is the pipeline that runs our build). It scans the saved daily snapshots and turns them into one RSS entry per day. Each entry links straight to the evidence behind the finding. The feed is hosted on GitHub Pages, the free web host GitHub gives each project.

Why this matters.

Benchmarks do not arrive on a timetable. Some weeks are quiet, then five drop at once. RSS fits that mess: you see what happened and when, and the radar never has to decide how to "notify" you.

The feed also makes our output readable by other programs. Another tool can watch the feed and run its own work the moment a new benchmark appears. That is how the radar starts talking to the rest of the ecosystem.

Day thirteen: favicon, URL fixes, and daily Q&A on the dashboard.
