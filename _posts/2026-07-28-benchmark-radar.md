---
title: "Benchmark Radar: An Evidence-First Daily Radar for AI Benchmarks"
date: 2026-07-28
permalink: /posts/2026/07/benchmark-radar/
tags:
  - AI
  - Benchmarks
  - Evaluation
  - Datasets
  - Open Source
---

AI benchmarks now show up faster than any one researcher can keep up with. So I built a radar that checks for them every day, and shows its work.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar is live.** Track new AI benchmarks, datasets, and leaderboards every day: [open the dashboard](https://benchmark-radar.org/) or [star it on GitHub](https://github.com/ktwu01/benchmark-radar).

[Benchmark Radar](https://github.com/ktwu01/benchmark-radar) is an open-source tool that looks for new AI benchmarks, evaluation methods, datasets, leaderboards, and data-quality research every day. A benchmark is a test that measures how well an AI model does at something. It pulls records from primary and structured sources, removes duplicates, sorts them with a visible tagging system, ranks them with explainable signals, and publishes both a daily GitHub Issue and a [cumulative dashboard](https://benchmark-radar.org/).

I am about to start a new adventure, and part of that job is exactly this kind of searching. I need to know which benchmarks, evaluation methods, datasets, and data-quality ideas are showing up, and I need a reliable way to keep up. That is why I needed Benchmark Radar, and why I built it.

The project tackles a simple problem. Keeping up with AI evaluation work has become a research job on its own.

A new benchmark might first show up as an arXiv paper. arXiv is a site where researchers post papers before peer review. It might be an OpenReview submission, a GitHub repo, or a Hugging Face dataset. Hugging Face is a site where people share machine-learning models and data. Its leaderboard may arrive later. The same artifact may then be written up by several secondary sources, each with a slightly different title and description. A normal feed gives all these records equal space and leaves you to figure out what is new, what is a duplicate, and what has real evidence behind it.

Benchmark Radar is my attempt to make that process more systematic.

## What the radar watches

The default tagging system covers four connected areas. A taxonomy is just a way of grouping things.

It watches new AI and LLM benchmarks, challenge sets, and evaluation suites.

It watches evaluation frameworks, judge models, safety and capability tests, and leaderboards.

It watches public datasets, preference data, synthetic data, and other data releases.

It watches work on contamination, leakage, provenance, deduplication, annotation quality, and related data-quality problems.

The collector queries several sources: arXiv, OpenReview, Hugging Face, GitHub, GitHub Releases, Semantic Scholar, OpenAlex, and Brave Search. Semantic Scholar and OpenAlex are databases of academic papers. Brave Search is a search engine. Optional sources can fail without stopping the daily report. When that happens, the source-health table shows the missing coverage instead of pretending the run was complete.

That detail matters. A trend line built from changing source coverage can look like real momentum even when it is only an artifact of how the collection ran.

## Evidence before novelty

The central design choice is that every ranked item carries four visible component scores.

Relevance measures how closely the record matches the benchmark, evaluation, dataset, and data-quality grouping.

Evidence rewards primary or structured sources, authorship signals, and supporting artifacts.

Recency captures how recently the work was published or meaningfully updated.

Adoption uses signals such as stars, downloads, likes, or citations, on a logarithmic scale.

The default priority score is:

```text
0.35 relevance + 0.20 evidence + 0.20 recency + 0.25 adoption
```

The result is reported on a 0-100 scale. The weights and the bands live in the same code that scores the records, and that rubric is also exported to the dashboard. Clicking a priority score shows the record's component values and the weighted math behind its rank.

This does not make the ranking objectively correct. It makes it inspectable.

Benchmark Radar is a triage system, not a scientific quality judge. It cannot tell whether a benchmark measures the capability its authors claim, whether its test set is contaminated, or whether a leaderboard result will reproduce. What it can do is show why an artifact reached the daily list and give you a cleaner evidence trail for deciding what deserves a closer look.

## Counting artifacts instead of mentions

Deduplication is one of the less visible but more important parts of the system.

The cumulative corpus resolves entities from exact identifiers such as DOI, arXiv, OpenReview, GitHub, and Hugging Face IDs. A DOI is a permanent identifier for a paper or dataset. It does not silently merge two similarly titled projects with fuzzy matching. Observations stay connected to the artifacts that produced them, and the dashboard can expand several records without turning every mention into a new benchmark.

The same caution applies to historical comparisons. Trend calculations only compare snapshots collected with the same report limit and the same connector-coverage signature. Incomplete days stay visible and are labeled rather than smoothed away.

That sounds conservative because it is. A radar is only useful if a rise in the chart means more than "the crawler behaved differently today."

## A daily research artifact

The whole workflow runs in GitHub Actions at 12:15 UTC and can also be triggered by hand. A run collects and scores records, validates a versioned daily snapshot, updates the date-filtered GitHub Issue, and rebuilds the cumulative dashboard.

Each snapshot records the selection funnel from fetched records to deduplicated, qualified, and published items. It also preserves retrieval time, parser version, and a fingerprint of the upstream payload, without publishing credentials or raw API responses.

The repository therefore holds more than a generated webpage. It holds the code, configuration, schemas, and versioned observations you need to inspect how the feed was produced.

You can run it locally with Python 3.11 or later:

```bash
git clone https://github.com/ktwu01/benchmark-radar.git
cd benchmark-radar
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e '.[dev]'
benchmark-radar
```

The main outputs are a Markdown report, a machine-readable evidence snapshot, a dated corpus snapshot, and the browser-ready data used by the dashboard.

## Why I built it in public

AI evaluation needs better discovery infrastructure, but it also needs skepticism toward the infrastructure doing the discovery.

Ranking systems easily hide editorial decisions inside a score. Data pipelines easily hide missing sources behind a clean interface. Cumulative dashboards easily count attention as evidence and repeated mentions as new activity. Benchmark Radar does not remove those risks, but it tries to expose them in the product itself: visible components, source-health warnings, versioned schemas, explicit limits, deterministic rebuilds, and links back to the discovered records.

The project is inspired by [agents-radar](https://github.com/duanyytop/agents-radar), with its sources and scoring redesigned for benchmark and AI-data research. It is released under the MIT License, and both the [source code](https://github.com/ktwu01/benchmark-radar) and the [live dashboard](https://benchmark-radar.org/) are public.

The goal is not to produce one more leaderboard. It is to make the fast-moving landscape around benchmarks a little easier to inspect, and a little harder to misread.

Update, August 25, 2026. This log is now also a live record of the road to 1,000 stars. Thirty daily posts in, the repository holds 86 stars and 17 forks, including 53 stars in the two days after the v0.8.0 release and the search and citation work described along the way. The newest entry is Benchmark Radar Day 30, and the repository now charts its own star history in the README.

> Want to follow Benchmark Radar? [Star the repo on GitHub](https://github.com/ktwu01/benchmark-radar) for daily updates, or [open the live dashboard](https://benchmark-radar.org/) to explore the scans.
