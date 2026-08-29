---
title: "Benchmark Radar Day 14: Feed Coverage, Briefing Reliability, and Production Q&A"
date: 2026-08-09
permalink: /posts/2026/08/benchmark-radar-day14/
tags:
  - AI
  - Benchmarks
  - Feed Coverage
  - Briefing
  - Production
---

The daily pipeline went from fragile to reliable. Day fourteen added more feeds, hardened the briefing, and turned on Q&A in production.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar is live.** Track new AI benchmarks, datasets, and leaderboards every day: [open the dashboard](https://benchmark-radar.org/) or [star it on GitHub](https://github.com/ktwu01/benchmark-radar).

Hi, Koutian here. The radar collects from a bunch of sources every day. We widened that net and then made sure nothing falls through the cracks.

We added more first-party benchmark feeds, the ones the benchmark teams publish themselves, plus a few curated feeds for AI news. That means more benchmarks land in the daily scan without us hunting for them.

Some GitHub repos exist only to pile up links for search ranking. They inflate our counts without adding anything real. We now filter those out, so the numbers you see are honest.

The daily briefing uses OpenAI's API to write itself. That API limits how many words you can send per minute (we call that the TPM, or tokens per minute). Before, one rate-limit error could kill the whole briefing. Now it retries enough times to wait out the limit.

We also check whether the briefing got cut off mid-sentence. If it did, we throw it away and ask again instead of posting a broken summary.

We changed the schedule to one run a day at 9AM Singapore time. Running it several times a day made people wonder which run "counted." One fixed time is easy to audit.

The daily Q&A is now live in production, not just in testing. Every day the radar writes its own questions about the benchmark world and answers them from the data it collected.

We started labeling each source by how we actually collected it, instead of a generic "Radar ingest" tag. That way, when a row looks wrong, we can tell which part of the pipeline made it. Old snapshots got a backfill with the right label. And we told git to ignore the .worktrees/ folder, which holds separate working copies of the code.

Why this matters.

The single 9AM run was about sanity. Multiple runs left everyone guessing which one was the real daily record. Now there is one, and you can trust it.

Turning on Q&A in production was a step toward the radar watching on its own. It notices things and reports them, instead of waiting for a person to ask. That is the whole point of a radar.

Issues addressed

- #169: add more first-party benchmark feeds
- #170: filter out sponsor-bait spam repos
- #171: let the briefing retry past rate limits
- #172: stop posting a cut-off briefing
- #175: turn on daily Q&A in production
- #176: one run a day at 9AM Singapore time
- #177: label sources by how they were collected
- collection method backfill for old snapshots

Day fifteen: social media integration and daily post generation.

> Want to follow Benchmark Radar? [Star the repo on GitHub](https://github.com/ktwu01/benchmark-radar) for daily updates, or [open the live dashboard](https://benchmark-radar.org/) to explore the scans.
