---
title: "Benchmark Radar Day 11: KW-Bench Capability Layer and Community Launch"
date: 2026-08-06
permalink: /posts/2026/08/benchmark-radar-day11/
tags:
  - AI
  - Benchmarks
  - KW-Bench
  - Capability Rubric
  - Community
---

KW-Bench got a capability rubric. The community got launch posts. Day eleven was a dual-track day.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

## What shipped

**KW-Bench L0-L5 capability rubric.** A deterministic rubric that assigns capability levels (L0 through L5) to benchmarks based on what they measure. The assignment is content-hash deterministic: the same input always produces the same level.

**KW-Bench shadow mode.** The capability layer was published in shadow mode, meaning it runs alongside the existing classification but does not yet override it. This lets the team validate the rubric against real data before making it authoritative.

**Shadow store recovery.** The shadow store (which tracks KW-Bench state across runs) was hardened against corruption and stale state. Seven regressions from the previous round of pattern fixes were corrected.

**Canonical benchmark tracks.** Benchmark tracks were derived and normalized, with deduplication applied to normalized track names.

**Content hash caching.** Classifications are cached by content hash, so re-running the rubric on unchanged data does not reprocess everything.

**Venn diagram overlap fix.** Overlapping trend categories now render independently instead of collapsing into each other.

**Community launch posts.** Copy-ready posts were prepared for community launch channels. The Chinese launch channels were documented.

**Radar source description corrected.** The README's description of what the radar watches was corrected for accuracy.

## Why it matters

The KW-Bench capability rubric was an attempt to answer a question the community kept asking: "Which benchmarks are actually hard?" L0 benchmarks are trivially solvable; L5 benchmarks represent genuine open problems. The deterministic assignment means the rubric is reproducible: anyone can verify the classification.

Shadow mode was a deliberate choice. Publishing a new classification system without validation is reckless. Shadow mode lets the team compare the rubric's output against known-good classifications before making it the default.

The community launch posts were the first external-facing communication. The radar had been building in private; this was the moment it went public.

## Issues addressed

- \#144: Chinese launch channels
- \#148: community launch copy
- \#151: Venn relation fix
- \#154: KW-Bench MVP merge
- KW-Bench L0-L5 capability rubric
- Shadow store recovery and hardening
- Canonical benchmark track derivation
- Content hash caching

Day twelve: daily RSS feed.
