---
title: "Benchmark Radar Day 35: One URL for Every Benchmark"
date: 2026-08-30
permalink: /posts/2026/08/benchmark-radar-day35/
tags:
  - AI
  - Benchmarks
  - SEO
  - Open Source
  - Contributor
  - Plain English
---

Day thirty-five of Benchmark Radar. A week-old copycat outranked the real project for its own name because search engines could see only four pages here. Today every one of the 1,173 benchmarks the radar tracks has a page of its own. Scoreboard: 123 stars, 23 forks.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar is live.** Track new AI benchmarks, datasets, and leaderboards every day: [open the dashboard](https://benchmark-radar.org/) or [star it on GitHub](https://github.com/ktwu01/benchmark-radar).

SEO means making a website easy for search engines to find and rank. Indexable means a page a search engine can read and list. Structured data is machine-readable description embedded in a page, and a sitemap is the list of URLs a site wants search engines to know about. A ledger is a public list that records who earned what, and a byline is the list of authors on a document.

PR #442 is the big one. Each benchmark now gets a static page with a unique title, description, canonical URL, structured data, and per-source score tables, plus a directory page. The sitemap grows from 4 to 1,177 URLs. Internal links become absolute so analyzers can find them, the homepage gains Organization and enriched WebSite and Dataset schema, `llms.txt` is published, and the published CSS is minified. The rendered dashboard does not change.

PR #443 fixes the one thing that broke: the interactive view link on those pages now points at the leaderboard, where a frontier-model slug can actually render.

PR #449 publishes the contributor score ledger. Contributors can claim an issue, a claim expires after seven days, one person holds an issue at a time, and a daily job keeps the ledger current. PR #450 makes sure only work a contributor can actually complete is scored, and PR #451 raises the collaborator threshold from 6 to 12 points, with every accepted real use case worth 6. PR #458 links six scored paper research issues, each worth 6 to 12 points.

PR #441 adds a citation for the technical report and simplifies the local setup instructions, and PR #444 thanks Xiaopai Liu for the shout-out, moves the acknowledgements to the end, and flags the CLI version.

Why this matters.

The data advantage was real but invisible. A project holding 1,173 evidence-linked benchmarks was exposing four indexable URLs, so a copycat with none of the data could rank higher for the brand name. One page per benchmark turns the dataset itself into the search surface, which is exactly the surface a copycat cannot copy.

Outside contributors need rules they can trust. A public ledger, a claim mechanism, and scores tied to work that is actually completable turn contribution from a favor into a job with a fair price.

Issues addressed

- SEO: one static page per benchmark, absolute links, and structured data
- #440: README acknowledges Xiaopai Liu and moves acknowledgements last
- #449: contributor score ledger with claiming and seven-day expiry
- #450: only contributor-completable work is scored
- #451: collaborator threshold raised to 12 points
- #458: six scored paper research issues linked
- scoreboard: 123 of 1,000 stars, 23 forks

Day thirty-six: a frontier model card with 37 scores, and a search that shows its work.

> Want to follow Benchmark Radar? [Star the repo on GitHub](https://github.com/ktwu01/benchmark-radar) for daily updates, or [open the live dashboard](https://benchmark-radar.org/) to explore the scans.