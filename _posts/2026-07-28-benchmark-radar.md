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

AI benchmarks are now appearing faster than any researcher can evaluate them, so I built a radar that makes discovery daily, transparent, and auditable.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

[Benchmark Radar](https://github.com/ktwu01/benchmark-radar) is an open-source system that looks for newly released AI benchmarks, evaluation methods, datasets, leaderboards, and data-quality research every day. It gathers records from primary and structured sources, removes duplicates, classifies them with a visible taxonomy, ranks them with explainable signals, and publishes both a daily GitHub Issue and a [cumulative dashboard](https://ktwu01.github.io/benchmark-radar/).

I am about to begin a new adventure, and an important part of my job will be searching for exactly this kind of information. I need to know which benchmarks, evaluation methods, datasets, and data-quality ideas are emerging—and I need a reliable way to keep up with them. That is why I needed Benchmark Radar, and why I built it.

The project addresses a simple problem: following AI evaluation work has become a research task of its own.

A new benchmark may first appear as an arXiv paper, an OpenReview submission, a GitHub repository, or a Hugging Face dataset. Its leaderboard may arrive later. The same artifact may then be discussed by several secondary sources, each with a slightly different title and description. A normal feed gives all of these records equal visual weight and leaves the reader to reconstruct what is new, what is duplicated, and what has real evidence behind it.

Benchmark Radar is my attempt to make that process more systematic.

## What the radar watches

The default taxonomy covers four connected areas:

- new AI and LLM benchmarks, challenge sets, and evaluation suites;
- evaluation frameworks, judge models, safety and capability evaluations, and leaderboards;
- public datasets, preference data, synthetic data, and other data releases;
- work on contamination, leakage, provenance, deduplication, annotation quality, and related data-quality problems.

The collector queries arXiv, OpenReview, Hugging Face, GitHub, GitHub Releases, Semantic Scholar, OpenAlex, and Brave Search. Optional sources can fail or be unavailable without stopping the daily report. When that happens, the source-health table shows the missing coverage instead of quietly pretending that the run was complete.

That detail matters. A trend line built from changing source coverage can look like momentum even when it is only a collection artifact.

## Evidence before novelty

The central design choice is that every ranked item carries four visible component scores:

- **Relevance** measures how closely the record matches the benchmark, evaluation, dataset, and data-quality taxonomy.
- **Evidence** rewards primary or structured sources, authorship signals, and corroborating artifacts.
- **Recency** captures how recently the work was published or materially updated.
- **Adoption** uses signals such as stars, downloads, likes, or citations on a logarithmic scale.

The default priority score is:

```text
0.35 relevance + 0.20 evidence + 0.20 recency + 0.25 adoption
```

The result is reported on a 0–100 scale. The weights and component bands live in the same code that scores the records, and that rubric is also exported to the dashboard. Clicking a priority score shows the record's component values and the weighted calculation behind its rank.

This does not make the ranking objectively correct. It makes it inspectable.

Benchmark Radar is a triage system, not a scientific quality judge. It cannot tell whether a benchmark measures the capability its authors claim, whether its test set is contaminated, or whether a leaderboard result will reproduce. What it can do is show why an artifact reached the daily list and give the reader a cleaner evidence trail for deciding what deserves a closer look.

## Counting artifacts instead of mentions

Deduplication is one of the less visible but more important parts of the system.

The cumulative corpus resolves entities from exact identifiers such as DOI, arXiv, OpenReview, GitHub, and Hugging Face IDs. It does not silently merge two similarly titled projects with fuzzy matching. Observations remain connected to their discovered artifacts, and the dashboard can expand multiple records without turning every mention into a new benchmark.

The same caution applies to historical comparisons. Trend calculations only compare snapshots collected with the same report limit and the same connector-coverage signature. Incomplete days remain visible and are labeled rather than being smoothed away.

That sounds conservative because it is. A radar is useful only if an increase in the chart means more than “the crawler behaved differently today.”

## A daily research artifact

The entire workflow runs in GitHub Actions at 12:15 UTC and can also be triggered manually. A run collects and scores records, validates a versioned daily snapshot, updates the date-filtered GitHub Issue, and rebuilds the cumulative dashboard.

Each snapshot records the selection funnel from fetched records to deduplicated, qualified, and published items. It also preserves retrieval time, parser version, and a fingerprint of the upstream payload without publishing credentials or raw API responses.

The repository therefore contains more than a generated webpage. It contains the code, configuration, schemas, and versioned observations needed to inspect how the feed was produced.

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

Ranking systems easily hide editorial decisions inside a score. Data pipelines easily hide missing sources behind a clean interface. Cumulative dashboards easily count attention as evidence and repeated mentions as new activity. Benchmark Radar does not eliminate those risks, but it tries to expose them in the product itself: visible components, source-health warnings, versioned schemas, explicit limits, deterministic rebuilds, and links back to the discovered records.

The project is inspired by [agents-radar](https://github.com/duanyytop/agents-radar), with its sources and scoring redesigned for benchmark and AI-data research. It is released under the MIT License, and both the [source code](https://github.com/ktwu01/benchmark-radar) and [live dashboard](https://ktwu01.github.io/benchmark-radar/) are public.

The goal is not to produce one more leaderboard. It is to make the fast-moving landscape around benchmarks a little easier to inspect—and a little harder to misread.
