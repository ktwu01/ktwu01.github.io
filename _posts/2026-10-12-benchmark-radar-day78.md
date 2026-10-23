---
title: "Benchmark Radar Day 78: Separate Injection Reach from Compliance"
date: 2026-10-12
permalink: /posts/2026/10/benchmark-radar-day78/
tags:
  - AI
  - Benchmarks
---

Day 78 of Benchmark Radar. The scan fetched 997 items, published 449, and marked 223 as recommended.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar is live.** [Open the dashboard](https://benchmark-radar.org/), [star the repository](https://github.com/ktwu01/benchmark-radar), or read the [paper](https://arxiv.org/abs/2609.11115). The [Hugging Face dataset](https://huggingface.co/datasets/ktwu01/benchmark-radar) provides the data.

MultiAgentInject contains 4,050 trials that vary task, agent-network topology, attack class, stealth, and propagation depth. It records whether an injected instruction reaches another agent separately from whether that agent complies. Those events point to different defenses: communication boundaries and behavior after exposure. [MultiAgentInject dataset, injection templates, and analysis scripts](https://doi.org/10.5281/zenodo.23297959).

SimGlot supplies eight integrity checks and 21 injected fault variants across seven defect classes for an agent benchmark’s task generator and reward function. Its records bind results to frozen software revisions. The scoring machinery becomes something that can be tested against known faults. [SimGlot: Oracle-Integrity Auditing and Configuration-Dependent Measurement in an LLM Agent Benchmark](https://doi.org/10.5281/zenodo.23290600).

## Why this matters

Keep intermediate events visible. A single success flag cannot locate either an attack-defense failure or a defect in the benchmark itself.

## Scan coverage

This is a keyword-filtered discovery feed, not a representative survey of AI research. The archived briefing used 124 of 449 captured evidence records. These findings summarize its cited releases; discovery dates do not necessarily equal original publication dates.

Data and briefing: [2026-10-12 archived snapshot](https://github.com/ktwu01/benchmark-radar/blob/2f75b7a07c6f233bcbcb461631befc2b118be584/data/snapshots/2026-10-12.json).
