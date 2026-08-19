---
title: "Benchmark Radar Day 23: External Benchmark Catalog and Leaderboard Navigator"
date: 2026-08-18
permalink: /posts/2026/08/benchmark-radar-day23/
tags:
  - AI
  - Benchmarks
  - External Catalog
  - Leaderboard
  - Search
  - Normalization
---

The radar absorbed external catalogs. Day twenty-three built the external catalog system and added benchmark search to the leaderboard.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

## What shipped

**External benchmark catalog.** A new system normalizes external benchmark catalogs (llm-stats, OpenCompass) into the radar's internal format. Each source is crawled, normalized into per-benchmark shards, and validated against an identity layer.

**Identity layer.** A hand-checked seed of benchmark identities (`identity.yml`) anchors the normalization. Candidates are generated automatically, but the authoritative identities are human-verified. This prevents incorrect merges while allowing automated expansion.

**Per-benchmark shards.** The `normalize-external` command emits per-benchmark shard files. Each shard contains the benchmark's metadata, scores, and source references in a standardized format.

**Leaderboard benchmark search.** The leaderboard navigator now includes benchmark search (M1 starting point). Users can search for specific benchmarks by name, capability level, or vendor.

**Search index.** The search index is emitted into `site/data` for client-side search. This enables fast, offline-capable benchmark lookup.

**OpenCompass round 2 integration.** The OpenCompass round 2 catalog was merged into the external catalog with full identity resolution.

**Collapsed issue sections.** The issue #240 sections default to collapsed but visible, reducing visual clutter while keeping content accessible.

**Pages deploy for external catalog.** The external catalog is built and deployed as part of the GitHub Pages workflow.

**Invariant pinning.** Shard and identity invariants are pinned at 100%, ensuring the normalization pipeline maintains perfect consistency.

**Navigator audit correction.** The navigator claim was corrected and office hours findings were recorded.

**Ruff formatting applied.** All external catalog modules were formatted with ruff.

## Why it matters

The external catalog was the radar's biggest architectural expansion. Before this, the radar collected data from its own sources. After this, it can ingest and normalize data from external benchmark registries. This means the radar's coverage is no longer limited by what its own crawlers can reach; it can absorb the entire benchmark ecosystem by integrating existing catalogs.

The identity layer was the key technical decision. Automated normalization is powerful but dangerous: a wrong merge (two different benchmarks merged into one, or one benchmark split into two) corrupts the data permanently. The hand-checked seed ensures correctness at the foundation while the automated system handles scale.

The leaderboard search was the first step toward making the radar's data navigable at scale. With hundreds of benchmarks, scrolling is not enough. Search makes specific benchmarks findable in seconds.

## Issues addressed

- \#240: external catalog sections
- \#246: external catalog modules
- \#247: navigator audit correction
- External catalog system (llm-stats, OpenCompass)
- Identity layer with hand-checked seed
- Per-benchmark shard emission
- Leaderboard benchmark search
- Search index generation
- Invariant pinning at 100%

---

*This concludes the first 23 days of Benchmark Radar development. From a blank repository to a full-featured benchmark intelligence platform with Chinese i18n, AI-powered briefings, social media integration, and external catalog normalization, the project shipped something every day for three weeks straight.*
