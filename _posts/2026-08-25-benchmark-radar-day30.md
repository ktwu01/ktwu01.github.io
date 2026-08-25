---
title: "Benchmark Radar Day 30: A Live Log on the Road to 1,000 Stars"
date: 2026-08-25
permalink: /posts/2026/08/benchmark-radar-day30/
tags:
  - AI
  - Benchmarks
  - Open Source
  - Growth
  - Distribution
  - Plain English
---

Day thirty of Benchmark Radar. Thirty posts in, this log has become a live broadcast of one open-source project trying to reach 1,000 stars, and today the scoreboard reads 86.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

A star is a bookmark a GitHub user leaves on a repository, and the star count is the crudest measure of attention a project gets. A fork is a copy of the repository someone else owns. A badge is one of the small labeled images at the top of a README. A registry is the radar's master list of benchmarks.

The scoreboard first. The repository went public on July 27. For its first four weeks it collected 33 stars, about one a day, while shipping something every single day. Then came 27 stars on August 24 and 26 more today, 53 in two days, for 86 total plus 17 forks. The goal this series now tracks in the open is 1,000. Nine hundred fourteen to go.

Nothing big launched on August 24 itself. What shipped in the three days before it was plumbing: version 0.8.0 with citation metadata, a BibTeX block and a Cite button, a generated sitemap and canonical URLs so search engines can read every view, a compact first-paint payload that cut load time, README language links moved to the top-right, and a plain-language pass across the interface. I cannot prove which of those moved the number. What I can say is that the jump arrived right after the project became easy to cite, easy to find, and fast to open, and after four weeks of being none of those things.

PR #352 turned the scoreboard into part of the repository. A script inside the repo pulls the star history from GitHub's GraphQL API and renders light-mode and dark-mode SVG charts into both READMEs. It regenerates on every merge and on every new star, with a daily fallback run, and publishes to a `star-history` branch so the README preview never waits for a schedule. The first chart was drawn at 57 stars. From here on, every day recorded in this log has a line on a chart anyone can check.

PR #358 brought the first registry entries from a contributor outside the project. junjiezhou1122 answered issue #347 with four benchmarks: JointAVBench (multimodal, released December 14, 2025, ICLR 2026), OmniVideoBench (multimodal, October 12, 2025, NJU-LINK), ASI-Bench (agent, August 18, 2026), and SWE-bench Science (coding agent, August 20, 2026, OpenMOSS/Fudan). Every field came from the arXiv abstract page or the official repository rather than memory, and each entry carries the caveat that CONTRIBUTING.md requires. The review pass corrected the venue, source URL, domain, and disclosure before merge.

PR #364 closed #324, the last large data source on the wishlist. The Artificial Analysis snapshot had arrived as a zip archive, so this PR unpacked it into the tree and reshaped it into the registry's CSV format. Instead of copying the normalizer once per source, the shared helpers went public and one normalizer now serves every external source, parameterized by source. Scores file under the record's own source, so the new feed cannot rename models or mix metric scales. On the site, the metric picker is gone and score points no longer draw a dashed ring around third-party citations; the citation is named in the point's label and its pinned card.

PR #370 removed the word donor from the dashboard copy. The note explaining inherited identities now says the information comes from the matched source card, in English and Chinese at once, because donor was project shorthand a reader had no way to know. PR #368 made the issue templates bilingual, asking every reporter for the same four things in either language: what happened, where, expected behavior, and why it matters, plus guidance on which use cases are worth showing off.

PR #366 wrote the showcase rules down where the agents that work on the repo will read them, in AGENTS.md and CLAUDE.md, and synced the documented CI sequence with the five steps CI actually runs. PR #367 trimmed the five-badge header so the X, LinkedIn, and Google Scholar badges carry their icon and purpose instead of the owner's handle, with the same change mirrored in the Chinese README.

Why this matters.

Four weeks of daily shipping bought one star a day. Two days of citability, findability, and speed coincided with 53. From here to 1,000, this log will keep testing that observation. Nobody cites a project they cannot find, and nobody stars one that takes ten seconds to show a number.

The contribution rails mattered before the first contributor showed up. Verified-field rules and required caveats meant the first outside pull request took one review pass instead of a rewrite, and bilingual templates mean the next one can be filed in Chinese or English.

Measurement keeps the broadcast honest. The repository draws its own star curve with its own script, so every growth claim this series makes can be checked against a chart everyone can see.

Issues addressed

- #324: Artificial Analysis snapshot normalized into the catalog
- #347: JointAVBench, OmniVideoBench, ASI-Bench, SWE-bench Science from the first outside contributor
- #351: star history chart generated and published by the repository itself
- #353: badge labels simplified in both READMEs
- #356: bilingual issue templates
- #340: donor jargon removed from dashboard copy
- scoreboard: 86 of 1,000 stars, 53 of them in the last two days

Day thirty-one: a one-line summary on every release card.
