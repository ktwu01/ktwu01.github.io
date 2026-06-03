---
title: "ESM-bench: Benchmarking AI Agents on Earth System Model Physics and Code"
excerpt: "A 243-task benchmark evaluating whether AI agents understand Earth System Model physics and code, with multi-model evaluation and leakage detection<br/><img src='/images/500x300.png'>"
collection: portfolio
---

ESM-bench is a benchmark that tests whether AI agents understand the physics and code of Earth System Models, rather than producing plausible output without grounding.

## Project Overview
AI agents can generate fluent code and explanations about Earth System Models without reasoning about the underlying physics or the structure of the codebase. ESM-bench measures that gap with a structured, reproducible task set.

## Status
Preprint, released on Zenodo, in preparation for NeurIPS Datasets and Benchmarks. Lead developer.

## What It Measures
- A 243-task benchmark drawn from Earth System Model physics and codebases
- A classification rubric scored with precision, recall, and F1
- Multi-model evaluation across several agents and models
- Leakage detection to guard against memorized answers

## Links
- **Preprint (Zenodo)**: [https://zenodo.org/records/19802836](https://zenodo.org/records/19802836)
- **Publication entry**: [ESM-bench](/publication/2026-esm-bench)
- **Blog post**: [ESM-bench: testing whether AI agents understand Earth System Model physics](/posts/2026/04/esm-bench-ai-agents-earth-system-models/)
