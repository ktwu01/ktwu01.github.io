---
title: "Benchmark Radar Day 82: Output Scores Cannot Prove Runtime Integrity"
date: 2026-10-16
permalink: /posts/2026/10/benchmark-radar-day82/
tags:
  - AI
  - Benchmarks
---

Day 82 of Benchmark Radar. The scan fetched 1,672 items, published 846, and marked 346 as recommended.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar is live.** [Open the dashboard](https://benchmark-radar.org/), [star the repository](https://github.com/ktwu01/benchmark-radar), or read the [paper](https://arxiv.org/abs/2609.11115). The [Hugging Face dataset](https://huggingface.co/datasets/ktwu01/benchmark-radar) provides the data.

DIB-Bench tests whether judges can detect a tampered deployment runtime that still produces expected evaluation outputs. Across 7,560 examples and six tamper types, the source reports that rule-based and model-based judges accepted 88.6% to 94.1% of tampered outputs. This is a reported result on that setup, rather than proof about every deployment. [Stronger Judges Do Not See More: Deployment-Integrity Blindness in LLM Evaluation](https://arxiv.org/abs/2610.21135).

VELD-QA separates finding supporting evidence from interpreting it in long visual documents. Its 15,000 human-authored question-answer pairs span 5,859 PDFs, with annotations for supporting pages and visual elements. A wrong answer can therefore be traced to page retrieval or interpretation of the retrieved evidence. [VELD-QA: A Large-Scale Dataset for Visual Evidence Grounding and Question Answering in Long Documents](https://arxiv.org/abs/2610.20964).

## Why this matters

Measure the component that matters to the decision. Correct outputs cannot by themselves identify the running stack, and document-answer accuracy cannot locate every retrieval failure.

## Scan coverage

This is a keyword-filtered discovery feed, not a representative survey of AI research. The archived briefing used 185 of 846 captured evidence records. These findings summarize its cited releases; discovery dates do not necessarily equal original publication dates.

Data and briefing: [2026-10-16 archived snapshot](https://github.com/ktwu01/benchmark-radar/blob/2f75b7a07c6f233bcbcb461631befc2b118be584/data/snapshots/2026-10-16.json).
