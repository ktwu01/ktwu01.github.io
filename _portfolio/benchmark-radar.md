---
title: "Benchmark Radar: Daily Evidence-First Radar for AI Benchmarks"
excerpt: "Open-source daily radar and adoption leaderboard tracking which benchmarks frontier labs actually report, across 30+ curated documents from 10 organizations."
collection: portfolio
header:
  teaser: /images/portfolio/covers/benchmark-radar.svg
---

Benchmark Radar is a production-deployed, open-source dashboard that ranks which benchmarks appear in model cards, system cards, and technical reports from frontier labs, and runs a daily radar for new benchmark, evaluation, dataset, and data-quality work.

## Project Overview
The hand-curated Model Card Adoption Rank answers a narrow question: which AI benchmarks do frontier labs actually report when they release a model? Each document counts at most once per benchmark, with card count and organization count published separately. The automated daily radar collects new work from eight sources, deduplicates it, classifies it with a published taxonomy, and exposes the ranking components.

## What It Does
- 30+ curated model-release documents from 10 organizations, 79+ tracked benchmarks
- Leaderboard with card count, organization count, and scores-over-time charts
- Daily radar pipeline: arXiv, OpenReview, Hugging Face, GitHub, Semantic Scholar, OpenAlex, Brave Search, Hacker News
- Self-generated star-history chart published to its own branch, so every growth claim is checkable

## Status
Open source (MIT), v0.8.0, 117+ stars. Built as part of my AI Data Trial research internship at Tencent.

## Links
- **Live dashboard**: [https://koutian.is-a.dev/benchmark-radar/](https://koutian.is-a.dev/benchmark-radar/)
- **Code**: [https://github.com/ktwu01/benchmark-radar](https://github.com/ktwu01/benchmark-radar)
- **Daily log series**: [Benchmark Radar Day 30](/posts/2026/08/benchmark-radar-day30/)