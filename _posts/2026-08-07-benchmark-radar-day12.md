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

The radar now publishes an RSS feed. Day twelve was a single-feature day with an outsized impact.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

## What shipped

**Daily RSS feed.** A new CI step generates an RSS feed from the snapshot history. Each day's findings appear as an RSS entry with links to the cited evidence. The feed is published as a GitHub Pages artifact.

## Why it matters

RSS is the lowest-friction way to subscribe to a data stream. No email setup, no webhook configuration, no API key. You point your RSS reader at the feed URL and you get daily updates.

For a benchmark radar, RSS is particularly natural. Benchmarks are updated on irregular schedules. Some weeks are quiet; others have five new releases. RSS handles this gracefully: you see what happened, when it happened, without the radar needing to decide how to "notify" you.

The feed also made the radar's output machine-readable. Other tools can subscribe to the feed and trigger their own workflows when new benchmarks appear.

## Issues addressed

- \#157: publish daily RSS feed from snapshot history

Day thirteen: favicon, URL fixes, and daily Q&A on the dashboard.
