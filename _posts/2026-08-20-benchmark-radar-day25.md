---
title: "Benchmark Radar Day 25: Scores on Their Dates, and a Radar That Does Not Rank Itself"
date: 2026-08-20
permalink: /posts/2026/08/benchmark-radar-day25/
tags:
  - AI
  - Benchmarks
  - Scoring
  - Date Axis
  - Identity
  - Feeds
  - Plain English
---

A radar that recommends itself is not a radar. Day twenty-five stopped the ranking from gaming itself, put crawled scores on the dates they belong to, and let an unscored benchmark answer for itself.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

## What shipped

**The radar stops recommending itself.** PR #291 ships scoring v4: `ktwu01/benchmark-radar` is excluded from its own ranking. Its description is wall-to-wall benchmark vocabulary and it commits daily, so relevance and recency carried it into the top 5 on 9 of the first 27 collected days. The exclusion matches the exact owner/name pair, never as a substring, so a real record like `H20Zhang/Agent-Benchmark-Radar` keeps its place.

**Download counts capped.** Scoring v4 also caps downloads: a dataset with 25,238 downloads and 1 like scored 88.0 and took #2 from a 3,265-star repo. The cap stops raw download counts from outranking real adoption signals.

**Crawled scores on their dates.** PR #290 fixes #279: `announcement_date` is present on all 5,544 crawled score rows and the normalizer was discarding it. The leaderboard frontier chart is now ordered by the release date instead of by score, so `?view=leaderboard&lfrontier=llm-stats-aime-2025` no longer draws a score-sorted ramp that only looks like progression.

**An unscored benchmark answers for itself.** PR #289 fixes #287: `?view=leaderboard&lfrontier=rsi_bench` was drawing AutomationBench's chart under a URL still reading `rsi_bench`. RSI-Bench has no adopters yet, so the adopter filter removed it before the guard could see it. The guard now runs before the filter.

**RSI-Bench recorded before any score.** PR #285 adds RSI-Bench to the registry with an adoption count of zero. That zero is a reading, not a hole in the crawl: a benchmark nobody has scored is the one a reader cannot find by any other route. The entry carries the name, aliases, publisher, release date, and an id for the first card that reports it.

**Search finds the benchmark.** PR #284 fixes the search half of #245: `?q=` now queries the registry too, not just the daily feed. `?q=researchclawbench` and `?q=terminal-bench` now find the real records, where before the box could not reach the registry at all.

**Four undated benchmarks dated.** PR #294 fixes #292: all four benchmarks with `released: null` turn out to have their own publications. ExploitBench (arXiv 2605.14153), BlueprintBench 2 (launch post), BioMysteryBench (Anthropic announcement), and VIBench (CAIS '26) now carry dates, so all 80 registry benchmarks are dated and the era filter can ask for undated ones.

**Reviewed identity for the 19 llm-stats benchmarks.** PR #295 closes #265: `data/external/llm_stats_identity_overrides.yml` records the hand-reviewed identity for 19 of the 50 score-dense benchmarks that anchor twice, including SWE-bench Verified/Pro/Multilingual, HLE, MMMU-Pro, and Terminal-Bench 1.0/2.0/2.1. The other 31 stay unrecorded until a second anchor is found, because a wrong publisher or license is worse than an honest blank. Two wrong crawl values are corrected, not carried.

**Verified first-party feeds.** PR #296 closes #264: nine RSS/Atom feeds are admitted to `config.yml` under `sources.first_party_feeds.feeds`, each re-verified to parse with at least one titled entry: Qwen, Ollama, Stability AI, Nomic AI, Replicate, NVIDIA Developer, IBM Research, Databricks, LangChain. Qwen gets a search fallback since its feed's newest entry is 2025-09-23.

**Jargon to zero.** PRs #281 and #282 close #276: the seven terms that only make sense inside the project are replaced with plain English, and the last five findings on the Pareto readiness panel, `site/logos.html`, and the zh translations are rewritten. The audit that reported 25 hits now reports 0.

**Tests import the checkout's own source.** PR #297 adds `pythonpath = ["src"]` to the pytest config, so a test run in a worktree measures the branch it is on rather than whatever checkout was pip-installed.

## Why it matters

The self-recommendation fix protects the ranking's credibility. A leaderboard that ranks itself #2 under the reader's own eyes teaches the reader to distrust every number on the page. Excluding the radar from its own ranking is not self-deprecation; it is the condition for the ranking to mean anything.

The date-axis fix changes what a chart claims. A score-sorted list drawn as a smooth ramp says "progress over time" when it is really just a sorted list. Putting the 5,544 crawled scores on their release dates lets the data make its own claim instead of an invented one.

The RSI-Bench fixes close the loop between the registry and the charts. Recording a benchmark before anyone scores it, and letting an unscored benchmark answer for itself, mean the permalink you read is the benchmark you get. The identity overrides do the same at the data layer: an honest blank outranks a confidently wrong value.

## Issues addressed

- \#244: RSI-Bench new benchmark
- \#245: search finds the benchmark
- \#264: first-party vendor feeds
- \#265: llm-stats identity overrides
- \#276: jargon audit to zero
- \#278: self-recommendation and capped downloads
- \#279: announcement_date on crawled scores
- \#287: unscored benchmark draws its own chart
- \#292: undated registry benchmarks
- Scoring v4 with self-exclusion
- Date-ordered frontier charts
- Nine verified first-party feeds
- Identity overrides for 19 benchmarks
- Pytest worktree import fix

Day twenty-six: frontier curves and the return of the Back button.