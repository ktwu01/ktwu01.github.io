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

Hi, Koutian here. Day seventeen was a cleanup day. We fixed what an internal audit found and made the site look finished.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar is live.** Track new AI benchmarks, datasets, and leaderboards every day: [open the dashboard](https://benchmark-radar.org/) or [star it on GitHub](https://github.com/ktwu01/benchmark-radar).

The masthead is the bar at the top of the site. It now shows how to reach us on WeChat and Discord. WeChat and Discord are two chat apps. This makes it easy for you to join the community and ask questions.

The masthead also has a one-click export button now. You can download all the radar's data in one click. A radar that only shows data on its own page keeps that data locked up. One that lets you export everything becomes a tool you can build on.

The frontier circles now show the real logos of each vendor at the points where scores stop climbing. That finishes the brand-icon work from the day before.

We hardened several dashboard behaviors that the audit flagged. That covers edge cases in rendering and in how data is shown.

When an HTTP request runs out of retries, the system now reports a `RequestError` instead of crashing with an assertion. An assertion failure kills the whole process. A `RequestError` can be caught, logged, and retried. This means a failed daily run now tells you what went wrong instead of dying silently.

Hacker News sends us numbers as cluster keys. We were sorting them as text, so 10 landed before 2. The fix sorts them as real numbers. The order is now correct.

We rescored the saved snapshots with the pipeline's word-start matcher. This corrected some scoring mistakes. We also aligned the composition-shift detail keys with the fields the code actually returns, which fixed a display bug.

The Pages workflow is the job that publishes the site. It now rebuilds when scores or config files change, not only when the code changes. You see updates even when the change was just a number.

We documented the OpenAI briefing flags and how to set up a local token. We also added `graphify-out` and `.claude` to `.gitignore` so those dev folders stay out of the repo.

Why this matters to you.

The export button is the big one. If you can pull the data out, you can check our work or reuse it in your own project. The retry fix keeps the daily run alive, so the dashboard does not go blank after a small network hiccup.

Issues addressed:

- #178: real brand icons in the frontier circles
- #190: frontier marker assertions
- #191: WeChat and Discord contact info
- #193: one-click data export dialog
- #194: masthead actions
- #196: audit hardening round
- HTTP retry exhaustion fix
- Hacker News sort fix
- Snapshot rescore
- Stats alignment fix
- CI rebuild triggers

Day eighteen: stable operation.

> Want to follow Benchmark Radar? [Star the repo on GitHub](https://github.com/ktwu01/benchmark-radar) for daily updates, or [open the live dashboard](https://benchmark-radar.org/) to explore the scans.
