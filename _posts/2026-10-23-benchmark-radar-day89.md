---
title: "Benchmark Radar Day 89: True Tool Outputs Can Still Omit Critical Evidence"
date: 2026-10-23
permalink: /posts/2026/10/benchmark-radar-day89/
tags:
  - AI
  - Benchmarks
---

Day 89 of Benchmark Radar. The scan fetched 1,332 items, published 630, and marked 289 as recommended.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar is live.** [Open the dashboard](https://benchmark-radar.org/), [star the repository](https://github.com/ktwu01/benchmark-radar), or read the [paper](https://arxiv.org/abs/2609.11115). The [Hugging Face dataset](https://huggingface.co/datasets/ktwu01/benchmark-radar) provides the data.

EpiSEM-Bench tests agents facing tool outputs that are true but omit a safety-relevant fact. Its 300 matched safe and unsafe task pairs across six domains vary the missing evidence while keeping the user request benign. The design separates evidence recovery from ordinary refusal behavior. [EpiSEM-Bench: Evaluating Safety and Evidence Recovery in LLM Agents under Missing Evidence](https://arxiv.org/abs/2610.31650).

AgentPhishing evaluates whether adaptive, persuasive phishing messages make email agents miss an attack and comply with its malicious request. It measures the agent’s response as well as detection. Recognizing a suspicious message and resisting its instructions are separate outcomes. [AgentPhishing: A Benchmark of LLM Email Agents Under Adaptive Attack](https://arxiv.org/abs/2610.31404).

## Why this matters

A safety suite should check whether the agent notices missing evidence and what it does after detection fails. The information available at action time matters.

## Scan coverage

This is a keyword-filtered discovery feed, not a representative survey of AI research. The archived briefing used 161 of 630 captured evidence records. These findings summarize its cited releases; discovery dates do not necessarily equal original publication dates.

Data and briefing: [2026-10-23 archived snapshot](https://github.com/ktwu01/benchmark-radar/blob/2f75b7a07c6f233bcbcb461631befc2b118be584/data/snapshots/2026-10-23.json).
