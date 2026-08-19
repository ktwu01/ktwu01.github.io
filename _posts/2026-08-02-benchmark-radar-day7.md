---
title: "Benchmark Radar Day 7: Model Card Adoption Leaderboard and Registry v0.3.0"
date: 2026-08-02
permalink: /posts/2026/08/benchmark-radar-day7/
tags:
  - AI
  - Benchmarks
  - Model Cards
  - Leaderboard
  - Version Release
---

The biggest single day. The Model Card Adoption Rank leaderboard launched, the registry expanded to the 2026 frontier, and the version bumped to 0.3.0.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

## What shipped

**Model Card Adoption Rank leaderboard.** A new leaderboard view that ranks benchmarks by how many model cards reference them. A benchmark cited by GPT-4, Claude, and Gemini model cards scores higher than one cited by a single paper. The rank is computed from a curated registry of model card to benchmark mappings.

**Registry expansion.** The registry was expanded from summary counts to full records, then to the 2026 frontier. Each model card is now expanded to the specific benchmarks it reports, with reverse links from benchmarks back to citing cards.

**Frontier-Bench merged into Terminal-Bench.** The Frontier-Bench series was merged into the Terminal-Bench series (#96). The count stayed at 13 because the merge was a consolidation of overlapping benchmarks, not an addition.

**Bidirectional registry links.** The registry is now a bidirectional graph: model cards link to the benchmarks they cite, and benchmarks link back to every card that cites them.

**Scholarly source reliability hardening.** Sources from academic venues are now treated with higher reliability than random web scrapes.

**Validation hardening.** Three remaining registry validation gaps were closed. Rejected: repeated documents, scalar aliases, impossible mentions. Date validation was hardened.

**Version bump to 0.3.0.** The version was bumped to reflect the scope of the registry expansion.

**Fable 5 / Mythos 5 benchmarks.** These benchmarks were extracted from a comparison table and added to the registry.

**Taxonomy stamp.** The existing corpus was stamped with the taxonomy that classified it, and category counts were bound to their producing taxonomy. Reclassification became a visible event.

**Adoption rank citable.** The adoption rank was made citable, and a contributor on-ramp was added.

## Why it matters

The Model Card Adoption Rank was the project's first competitive intelligence feature. Instead of just listing benchmarks, the radar now answered: which benchmarks do the top labs actually use when they release models? This is a fundamentally different question from "which benchmarks exist," and the answer is far more useful for anyone deciding where to invest evaluation effort.

The registry expansion from summary counts to full records was a data quality commitment. Partial data produces partial conclusions; full records produce auditable ones.

The taxonomy stamp addressed a subtle but critical issue: if you reclassify your corpus, you need to record which taxonomy version classified each record. Otherwise, historical comparisons are meaningless.

## Issues addressed

- \#85: model card adoption leaderboard
- \#87: scholarly source reliability
- \#89: expand model card registry
- \#92: leaderboard Fable/Mythos benchmarks
- \#93: version bump to 0.3.0
- \#96: merge Frontier-Bench into Terminal-Bench
- \#100: frontier bench citation merge
- \#101: citable adoption rank
- \#102: bind category counts to taxonomy
- \#103: stamp existing corpus with taxonomy

Day eight: stabilization and radar minimum fixes.
