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

Day twenty-three of Benchmark Radar. We started pulling in other people's benchmark lists, and we made the leaderboard searchable.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar is live.** Track new AI benchmarks, datasets, and leaderboards every day: [open the dashboard](https://benchmark-radar.org/) or [star it on GitHub](https://github.com/ktwu01/benchmark-radar).

A leaderboard is a public ranking of who scored best. A "shard" is just a small data file. "Normalizing" means converting data into one common shape. Today the radar learned to read catalogs built by other projects and turn them into its own format.

We built an external benchmark catalog. It reads catalogs from llm-stats and OpenCompass and converts them into the radar's internal format. Each source is crawled, split into per-benchmark files, and checked against an identity layer. You now get benchmarks we did not have to crawl ourselves.

The identity layer is a hand-checked list that says which names mean the same benchmark. We seed it by hand and let the system suggest the rest. The authoritative names are verified by a human. This stops the system from wrongly merging two different benchmarks, or splitting one in two. Two different benchmarks will not get fused by mistake.

The `normalize-external` command now writes one file per benchmark. Each file holds that benchmark's metadata, scores, and source links in one standard shape. Each benchmark's data lives in one predictable place.

The leaderboard navigator now has benchmark search. You can look up a benchmark by name, capability level, or vendor. This is the first step (we call it M1) toward browsing at scale. You can find a benchmark in seconds instead of scrolling forever.

The search index is written into `site/data` so the browser can search without a server. That makes lookups fast and they work offline. Lookup works even with no internet.

We merged the OpenCompass round 2 catalog into the external catalog with full identity resolution. More benchmarks, fully identified.

The sections in issue #240 now start collapsed but still visible. That cuts clutter while keeping the content one click away. You see less noise, same info.

The external catalog is now built and deployed as part of the GitHub Pages workflow. The catalog now shows up on the live site.

We pinned the shard and identity rules at 100% consistency. The pipeline must stay perfectly consistent or the data is meaningless. Attention to this is why the numbers hold up.

We corrected the navigator's earlier claim and recorded what we learned in office hours. We fixed a wrong claim we had made before.

All external catalog modules were formatted with ruff. Cleaner code, fewer style fights.

Why this matters.

The external catalog is the biggest change to the radar's structure so far. Before, the radar only read its own sources. Now it can swallow whole catalogs built by others. So its coverage is no longer capped by what our own crawler can reach.

The identity layer was the key call. Automatic conversion is powerful but risky: one wrong merge corrupts the data for good. The hand-checked seed keeps the base correct while the machine handles the volume.

The leaderboard search is the first step to making hundreds of benchmarks browsable. Scrolling does not scale. Search finds a specific benchmark in seconds.

Issues addressed

- #240: external catalog sections
- #246: external catalog modules
- #247: navigator audit correction
- external catalog system (llm-stats, OpenCompass)
- identity layer with hand-checked seed
- per-benchmark file output
- leaderboard benchmark search
- search index generation
- invariant pinning at 100%

---

That closes out the first 23 days of Benchmark Radar. We started from an empty repo and, every day for three weeks, shipped something: Chinese language support, AI-written briefings, social posts, and now external catalog normalization.

> Want to follow Benchmark Radar? [Star the repo on GitHub](https://github.com/ktwu01/benchmark-radar) for daily updates, or [open the live dashboard](https://benchmark-radar.org/) to explore the scans.
