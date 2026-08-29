---
title: "Benchmark Radar Day 32: Errors That Never Shouted, Adoption Without Binaries, and a Briefing a Person Would Write"
date: 2026-08-27
permalink: /posts/2026/08/benchmark-radar-day32/
tags:
  - AI
  - Benchmarks
  - Data Quality
  - Ranking
  - Briefing
  - Plain English
---

Day thirty-two of Benchmark Radar. We fixed data errors that failed silently, taught the ranking to count adoption for releases that ship no binary files, and rewrote the daily briefing so it reads like a person wrote it. Scoreboard: 113 stars, 21 forks.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

A silent data error is one that corrupts results without failing loudly, so the pipeline reports success on data it mangled. Adoption means how widely something is used; for a release it used to mean only how many binary files were downloaded. A briefing is the short daily summary of what moved.

PR #403 hunts down silent errors across the whole pipeline. Creation and update timestamps for GitHub and Hugging Face records are now kept distinct, malformed and future timestamps are rejected instead of inventing freshness, and date-only values parse consistently as UTC. Individual first-party feeds and OpenReview venues are isolated, so one failing source no longer erases healthy results. Daily dedup and same-day snapshot identity are now genuinely transitive, newer same-day pass metadata survives a stale retry, and fixes land for arXiv PDF identity, Semantic Scholar boundary-day loss, and backfill cross-day mutation. Every one of these failed silently before.

PR #407 changes what adoption means in the ranking. GitHub Release records used to score adoption only from release-asset downloads, so a widely used repository with no binary assets looked like nobody used it. Now collected releases are enriched with repository stars and forks after pagination, under a separate request cap, and the release parser is bumped to `github-releases/3`. The ranking also stops giving routine updates the same recency credit as first announcements, and the rubric publishes v5 with the new field-based provenance checks.

PR #378 makes the daily briefing human-readable. The briefing is a short GPT-written summary of the day's evidence, and it read like AI slop: noun-stacked, listy, with no plain-language spine. A Writing style block was added to the briefing instructions, and the tests pin the rules so a future edit cannot silently drop them. The same day, the briefing was expanded from 3 to at most 10 insights, with the Chinese bullet ceiling aligned to the same cap.

Why this matters.

Silent errors are worse than loud ones because nobody fixes what nobody sees. A wrong timestamp quietly ages a fresh benchmark into irrelevance; a dedup that is not transitive quietly doubles a record. Fixing these makes the daily snapshot trustworthy, and the fix ships with regression coverage so the silence cannot come back.

Adoption without binaries matters because most AI benchmarks are code repositories, not products with downloads. A repo with 20,000 stars and no release assets was scored as zero adoption. Counting repository stars and forks alongside downloads is the difference between measuring the field and measuring only its installers.

A daily briefing nobody can stand to read is a daily briefing nobody reads. The writing-style fix changed the output without changing the evidence pipeline, and pinning the rules in tests means the next model update cannot quietly reintroduce the slop.

Issues addressed

- #371: ranking v5, adoption now includes repository stars and forks
- #377: daily briefing reads human, writing rules pinned by tests
- #378: briefing expanded from 3 to at most 10 insights
- #403: silent pipeline data errors fixed across timestamps, dedup, identity, and isolation
- scoreboard: 113 of 1,000 stars, 21 forks

Day thirty-three: a radar that finds benchmark releases no keyword search would ever catch.