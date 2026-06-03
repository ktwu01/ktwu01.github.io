---
title: 'New Preprint: Noah-Agent, a Multi-Expert AI Agent Framework for Fortran Climate Models'
date: 2025-12-15
permalink: /posts/2025/12/noah-agent-preprint/
tags:
  - ai
  - agents
  - climate-models
  - preprint
---

Parameterizing a large Fortran climate model by hand is slow, error-prone, and hard to validate. Noah-Agent asks whether a team of specialized AI agents can do it instead.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

I have released **Noah-Agent (v0.1)** as a preprint on Zenodo. It is in preparation, so this is an early version rather than a final paper.

## The Problem
Large-scale Fortran climate models are powerful but hard to work with. Parameterizing them and validating their behavior usually takes careful manual effort across a large, old codebase. That work is slow and easy to get wrong.

## The Approach
Noah-Agent is a multi-expert AI agent framework for automated parameterization and validation of large-scale Fortran climate models. Instead of one model doing everything, several specialized agents coordinate:

- Some agents focus on selecting and adjusting parameters.
- Others focus on validating model behavior against reference outputs.

The goal is to automate steps that are otherwise done by hand, while keeping a human in the loop for judgment.

## How It Connects to My Other Work
Noah-Agent sits alongside two related efforts:

- **Noah-MP land surface modeling**, my main PhD research direction on physics-based land surface models.
- **[ESM-bench](/posts/2026/04/esm-bench-ai-agents-earth-system-models/)**, a benchmark for whether AI agents actually understand Earth System Model physics and code. Noah-Agent is a system that such a benchmark is meant to test.

## Status and Links
This is a preprint, version 0.1, in preparation. There are no claimed results or acceptances yet.

- **Preprint (Zenodo)**: [https://zenodo.org/records/17862049](https://zenodo.org/records/17862049)
- **Author**: Wu, K. (2025)
