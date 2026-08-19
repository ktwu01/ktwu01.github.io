---
title: "Benchmark Radar Day 17: Audit Hardening and Presentation-Ready Polish"
date: 2026-08-12
permalink: /posts/2026/08/benchmark-radar-day17/
tags:
  - AI
  - Benchmarks
  - Audit
  - UX
  - Export
  - Contacts
---

The audit findings were addressed. Masthead got contact info and data export. Day seventeen was a hardening and polish day.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

## What shipped

**WeChat/Discord contact sheet in masthead.** The masthead now shows contact information for WeChat and Discord, making it easy for users to join the community.

**One-click data export dialog.** A new dialog in the masthead lets users export the radar's data in one click. This makes the radar's data portable and reusable.

**Real brand icons in frontier circles.** The adoption frontier circles now show actual vendor logos at score saturation points. This was the visual completion of the brand icon work from the previous day.

**Dashboard audit fixes.** Several dashboard behaviors flagged by an internal audit were hardened, including edge cases in rendering and data display.

**HTTP retry exhaustion fix.** When HTTP requests exhaust their retry budget, the system now raises a `RequestError` instead of asserting. This prevents crashes and provides better error messages.

**Hacker News sort fix.** Numeric cluster keys from Hacker News were being sorted lexicographically instead of numerically. The fix ensures proper numeric ordering.

**Snapshot rescore.** Snapshots were rescored with the pipeline's word-start matcher to correct scoring inconsistencies.

**Stats alignment fix.** Composition-shift detail keys were aligned with the returned fields, fixing a data display issue.

**CI rebuild on score/config changes.** The Pages workflow now rebuilds when scores or config files change, not just when source code changes.

**OpenAI briefing documentation.** The OpenAI briefing flags and local PAT setup were documented.

**Graphify-out and .claude gitignored.** Development artifacts were added to `.gitignore`.

## Why it matters

The data export dialog was a commitment to data portability. A radar that only shows data on its own dashboard is a walled garden. A radar that lets you export everything is a tool others can build on.

The HTTP retry exhaustion fix was a production reliability improvement. An assertion failure crashes the process; a `RequestError` can be caught, logged, and retried. This is the difference between "the daily run failed silently" and "the daily run reported what went wrong."

## Issues addressed

- \#178: real brand icons in frontier circles
- \#190: frontier marker assertions
- \#191: WeChat/Discord contact sheet
- \#193: one-click data export dialog
- \#194: masthead actions
- \#196: audit hardening round
- HTTP retry exhaustion fix
- Hacker News sort fix
- Snapshot rescore
- Stats alignment fix
- CI rebuild triggers

Day eighteen: stable operation.
