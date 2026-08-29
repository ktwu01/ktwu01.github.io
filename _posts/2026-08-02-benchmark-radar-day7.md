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

Day seven was the biggest single day. Hi, Koutian here. We launched a new leaderboard, grew the registry to the 2026 frontier, and bumped the version to 0.3.0.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar is live.** Track new AI benchmarks, datasets, and leaderboards every day: [open the dashboard](https://ktwu01.github.io/benchmark-radar/) or [star it on GitHub](https://github.com/ktwu01/benchmark-radar).

A leaderboard is just a public ranking of who scored best. Our new Model Card Adoption Rank ranks benchmarks by how many model cards point at them. A model card is a short spec sheet that says what an AI model was tested on. If GPT-4, Claude, and Gemini all cite a benchmark in their cards, that benchmark ranks higher than one cited by a single paper. We compute the rank from a registry, which is a catalog of model card to benchmark links that we curate by hand.

The registry also grew up. It used to hold only summary counts. Now it holds full records, stretched out to the 2026 frontier, the newest crop of models. Each model card now expands to the exact benchmarks it reports, and those benchmarks link back to the cards that cited them.

We merged the Frontier-Bench series into Terminal-Bench in #96. The count stayed at 13 because this was a cleanup of overlapping benchmarks, not a new addition.

The registry is now a two-way graph. Model cards point to the benchmarks they cite, and benchmarks point back to every card that cited them. You can walk either direction.

We started trusting academic sources more than random web scrapes. A paper from a real venue counts for more than a blog post.

Three validation gaps closed. We now reject repeated documents, scalar aliases, and impossible mentions. Date checking got stricter too.

We bumped the version to 0.3.0 to signal how much the registry grew.

Two benchmark families, Fable 5 and Mythos 5, came out of a comparison table and joined the registry.

We stamped the existing corpus with its taxonomy, which is the tagging scheme used to sort the benchmarks. Category counts now bind to the taxonomy that produced them. If we reclassify later, that becomes a visible event you can see.

The adoption rank is now citable, and we added an on-ramp so new contributors can join in.

Why this matters.

The Model Card Adoption Rank was our first move past just listing benchmarks. It answers a sharper question: which benchmarks do the top labs actually use when they ship models? That tells you where to spend your own testing time, far better than a bare list of what exists.

Going from summary counts to full records was a data quality promise. Partial data gives you partial answers. Full records let anyone check our work.

The taxonomy stamp fixes a quiet trap. If you reclassify your corpus, you must record which taxonomy version sorted each record. Without that, comparing this month to last month means nothing.

Issues addressed:

- #85: model card adoption leaderboard
- #87: trust academic sources more than web scrapes
- #89: grow the model card registry
- #92: add Fable and Mythos benchmarks to the leaderboard
- #93: bump version to 0.3.0
- #96: merge Frontier-Bench into Terminal-Bench
- #100: merge frontier bench citations
- #101: make the adoption rank citable
- #102: bind category counts to the taxonomy
- #103: stamp the existing corpus with the taxonomy

Day eight: stabilization and radar minimum fixes.

> Want to follow Benchmark Radar? [Star the repo on GitHub](https://github.com/ktwu01/benchmark-radar) for daily updates, or [open the live dashboard](https://ktwu01.github.io/benchmark-radar/) to explore the scans.
