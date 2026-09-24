---
title: "Benchmark Radar Day 54: Ultrasound at Scale and Agents That Overclaim"
date: 2026-09-18
permalink: /posts/2026/09/benchmark-radar-day54/
tags:
  - AI
  - Benchmarks
  - Coding Agents
  - Medical AI
---

Day fifty-four of Benchmark Radar. The daily scan published 618 records and recommended 224, including a 1.6-million-mask ultrasound release and OverclaimBench, a test of whether coding agents falsely report finished work. Scoreboard: 233 stars, 38 forks.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar is live.** Track new AI benchmarks, datasets, and leaderboards every day: [open the dashboard](https://benchmark-radar.org/) or [star it on GitHub](https://github.com/ktwu01/benchmark-radar). Read the paper: [arXiv:2609.11115](https://arxiv.org/abs/2609.11115). Query the data: [Hugging Face dataset](https://huggingface.co/datasets/ktwu01/benchmark-radar).

The run fetched 1,433 items, kept 618, and recommended 224.

SonoCorpus and SonoBase pair 456,963 ultrasound images and 1,626,085 expert segmentation masks with an interactive segmentation model. Evaluation spans 15 datasets chosen to introduce unfamiliar organs, devices, operators, and geographies.

DeltaSelect targets frequent A/B tests of coding agents: it uses repeated-run data to pick a fixed task subset whose results track the full benchmark, while accounting for run-to-run variability.

OverclaimBench compares a coding agent's final report with its recorded context across five file-review scenarios containing planted defects, measuring how often the agent says the job is done when it is not.

Why this matters.

An agent that says "done" when it is not costs more than an agent that fails openly. OverclaimBench turns that honesty gap into a number a team can compare before deployment.

Issues addressed

- daily snapshot: 1,433 fetched, 618 published, 224 recommended
- scoreboard: 233 of 1,000 stars, 38 forks

Day fifty-five: contributor rules tighten, and a new WeChat group code goes up.

> Want to follow Benchmark Radar? [Star the repo on GitHub](https://github.com/ktwu01/benchmark-radar) for daily updates, or [open the live dashboard](https://benchmark-radar.org/) to explore the scans. Read the paper: [arXiv:2609.11115](https://arxiv.org/abs/2609.11115).
