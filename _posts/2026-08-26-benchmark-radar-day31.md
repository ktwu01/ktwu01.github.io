---
title: "Benchmark Radar Day 31: One-Line Release Cards, Two-Field Forms, and a README You Can Read"
date: 2026-08-26
permalink: /posts/2026/08/benchmark-radar-day31/
tags:
  - AI
  - Benchmarks
  - Open Source
  - Data Plumbing
  - i18n
  - Plain English
---

Day thirty-one of Benchmark Radar. Every release card now carries a one-line summary instead of a bare version tag, filing an issue takes at most two required fields, and both READMEs got short enough to read. Scoreboard: 107 stars, 20 forks.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

A release card is the entry for a new version of a benchmark. A bare tag is just the version string, like `v1.11.0`, which tells a reader nothing about what changed. A required field is a box a reporter must fill before the form submits. A sighting is one scan in which the radar saw a record.

PR #383 fixes the parsing bug that made a release title a bare tag. `modelscope/evalscope@v1.11.0` had been named `v1.11.0`, so the card read like a version number instead of a release. PR #385 then backfilled the 10 persisted bare-tag titles that remained, covering six EvalScope and MTEB releases across eight daily snapshots, and stamped every corrected and future record with `github-releases/2` while keeping the original raw-payload hashes. Every release card now has a one-line summary a reader can scan.

PR #387 fixes the All dates view. It used to replay the same record from every overlapping daily scan, so `modelscope/evalscope@v1.11.0` appeared twice for two days of sightings. Now each source record shows its one latest matching sighting. Individual date views, daily snapshots, and trend calculations keep the complete history.

PR #389 and PR #394 simplify the issue templates. Filing a report now takes one required field (what happened), a feature request two (what to add and why), a use case two, and a model card two. The prose around the boxes was the real problem, so every label and description is now one line, cutting report copy from 516 to 240 characters and feature requests from 619 to 324. PR #394 also adds an empty-state recovery checklist so a page with no matching records tells you what to do next.

PR #390 replaces 61 occurrences of the Chinese word 基准 with benchmark across the site and README fixtures, because the English term is what the registry and the taxonomy use. A regression test now fails if 基准 reappears.

PR #393, #395, #397, and #398 make the READMEs worth opening. The main README is condensed, the badge labels are shorter, the showcase image becomes the SWE-bench Verified GIF, and a See the dashboard section shows the Today and Leaderboard pages with one-line captions in both English and Chinese.

PR #399 fixes missed arXiv benchmarks and exposes card metadata. SWE Refactor Bench (`arXiv:2608.23564`) was missing entirely because its abstract names the benchmark as `Bench:` and the `cs.SE` feed was not collected. The radar now catches named `Bench:` releases, includes `cs.SE`, and runs after the 04:00 UTC arXiv bulletin so daily submissions are not a scan late. Cards now show source-provided authors, organizations, publication dates, and activity counters, with a real zero kept distinct from a missing counter.

PR #400 is three small consistency fixes: `.env.example` documents the OpenReview credentials the daily workflow already supplies, the OpenReview workflow file ends with a newline, and the package version is aligned at 0.8.0 everywhere after the earlier mismatch.

Why this matters.

A release titled with its bare tag is a release nobody can tell apart from a version bump. One-line titles make the card scannable, and backfilling the old ones keeps the archive honest rather than fixing only the future.

Forms that take two fields get filed; forms that read like paperwork do not. Cutting the copy, not the boxes, is what let the templates stay complete while becoming fast.

Silent data errors are the expensive kind. A record replayed twice or a release missed entirely looks fine to a reader who does not know it should be there. Every fix in this batch came with a regression test, so the next change cannot quietly reintroduce the same shape of mistake.

Issues addressed

- #362: release titles parsed as bare version tags, fixed and backfilled
- #357: Today and Leaderboard pages shown in both READMEs
- #374: 基准 replaced with benchmark in all zh translations, with a regression test
- #386: empty-state pages now carry a recovery checklist
- #388: issue templates reduced to at most two required fields
- #361: card metadata (authors, organizations, dates, activity counters) exposed on benchmark cards
- #389: SWE Refactor Bench found after adding named `Bench:` handling and the `cs.SE` feed
- scoreboard: 107 of 1,000 stars, 20 forks

Day thirty-two: a ranking that counts adoption even when a release ships no binary files.