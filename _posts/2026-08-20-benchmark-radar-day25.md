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

Day twenty-five of Benchmark Radar. We stopped the radar from ranking itself, put scores on the dates they belong to, and let a benchmark with no score still speak for itself.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

A "frontier chart" shows the best scores for a benchmark over time. An "adoption count" is how many groups have actually used a benchmark. A "worktree" is a separate copy of the code where you try changes.

PR #291 ships scoring version 4. The radar now excludes `ktwu01/benchmark-radar` from its own ranking. Its description is packed with benchmark words and it commits every day, so relevance and recency pushed it into the top 5 on 9 of the first 27 collected days. The exclusion matches the exact owner and name, never as a partial match, so a real record like `H20Zhang/Agent-Benchmark-Radar` stays put. The radar no longer stacks the deck in its own favor.

Scoring v4 also caps download counts. A dataset with 25,238 downloads and 1 like scored 88.0 and took the #2 spot from a repo with 3,265 stars. The cap stops raw download numbers from beating real signs of use. A popular download count can no longer drown out a repo people actually build on.

PR #290 fixes #279. All 5,544 crawled score rows now keep their `announcement_date`, which the normalizer used to throw away. The leaderboard frontier chart is now ordered by release date instead of by score. So `?view=leaderboard&lfrontier=llm-stats-aime-2025` no longer draws a ramp that only looks like progress. The chart now tells the truth about time.

PR #289 fixes #287. The URL `?view=leaderboard&lfrontier=rsi_bench` was drawing AutomationBench's chart under a link still reading rsi_bench. RSI-Bench has no adopters yet, so the adopter filter dropped it before the guard could catch it. The guard now runs before the filter. The chart you open is the benchmark you asked for.

PR #285 adds RSI-Bench to the registry with an adoption count of zero. That zero is a reading, not a gap in the crawl. A benchmark nobody has scored is exactly the one you cannot find any other way. The entry carries the name, aliases, publisher, release date, and an id for the first card that reports it. You can now find a benchmark before anyone has scored it.

PR #284 fixes the search half of #245. Before, the `?q=` box could only reach today's feed. Now it searches the whole registry, so `?q=researchclawbench` and `?q=terminal-bench` find the real records. Search now covers the full list, including older entries.

PR #294 fixes #292. The four benchmarks with `released: null` each turned out to have their own publication. ExploitBench (arXiv 2605.14153), BlueprintBench 2 (a launch post), BioMysteryBench (an Anthropic announcement), and VIBench (CAIS '26) now carry dates. All 80 registry benchmarks are now dated, and the era filter can ask for undated ones. Every benchmark now has a real release date.

PR #295 closes #265. The file `data/external/llm_stats_identity_overrides.yml` records the hand-checked identity for 19 of the 50 score-dense benchmarks that appear twice. They include SWE-bench Verified, Pro, and Multilingual, HLE, MMMU-Pro, and Terminal-Bench 1.0, 2.0, and 2.1. The other 31 stay blank until we find a second anchor, because a wrong publisher or license is worse than an honest blank. We corrected two wrong crawl values instead of carrying them. The data layer now prefers an honest blank over a confident error.

PR #296 closes #264. Nine RSS and Atom feeds are now listed in `config.yml` under `sources.first_party_feeds.feeds`. Each was re-checked to parse with at least one titled entry: Qwen, Ollama, Stability AI, Nomic AI, Replicate, NVIDIA Developer, IBM Research, Databricks, and LangChain. Qwen gets a search fallback because its feed's newest entry is from 2025-09-23. Nine official sources now feed the radar and each one was verified to work.

PRs #281 and #282 close #276. The seven terms that only make sense inside the project are now plain English. The last five findings on the Pareto readiness panel, on `site/logos.html`, and in the zh translations were rewritten. The audit that reported 25 hits now reports 0. The project words are gone from what you read.

PR #297 adds `pythonpath = ["src"]` to the pytest config. A test run inside a worktree now measures the branch you are on, not whatever copy was pip-installed. Tests now check the code you are actually changing.

Why this matters.

The self-ranking fix protects the ranking's credibility. A leaderboard that ranks itself near the top teaches you to distrust every number on the page. Excluding the radar from its own ranking is the price of the ranking meaning anything.

The date-axis fix changes what a chart claims. A score-sorted list drawn as a smooth ramp says "progress over time" when it is really just a sorted list. Putting the 5,544 scores on their release dates lets the data make its own claim.

The RSI-Bench fixes close the loop between the registry and the charts. Recording a benchmark before anyone scores it, and letting an unscored one answer for itself, means the permalink you open is the benchmark you get. The identity overrides do the same at the data layer: an honest blank beats a confident wrong value.

Issues addressed

- #244: RSI-Bench new benchmark
- #245: search finds the benchmark
- #264: first-party vendor feeds
- #265: llm-stats identity overrides
- #276: jargon audit to zero
- #278: self-recommendation and capped downloads
- #279: announcement_date on crawled scores
- #287: unscored benchmark draws its own chart
- #292: undated registry benchmarks
- scoring v4 with self-exclusion
- date-ordered frontier charts
- nine verified first-party feeds
- identity overrides for 19 benchmarks
- pytest worktree import fix

Day twenty-six: frontier curves and the return of the Back button.
