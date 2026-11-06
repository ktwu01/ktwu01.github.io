---
title: 'Reasoning with Limited Knowledge: A Reading List'
date: 2026-11-06
permalink: /posts/2026/11/reasoning-with-limited-knowledge/
tags:
  - AI
  - Reasoning
  - Research
---

I want to understand how to build a model that can reason with limited prior knowledge. These projects explore abstraction, learning from feedback, and solving unfamiliar problems.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

- **François Chollet and ARC Prize.** Chollet's [On the Measure of Intelligence](https://arxiv.org/abs/1911.01547) frames intelligence around the efficiency of acquiring new skills, accounting for prior knowledge and experience. ARC tests generalization from a few examples. The [ARC Prize 2025 technical report](https://arxiv.org/abs/2601.10904) discusses iterative refinement, program synthesis, and small networks trained without broad pretraining. ARC performance measures a particular set of capabilities; broader intelligence needs further evidence.

- **Alexia Jolicoeur-Martineau: Tiny Recursive Model (TRM).** [Less is More: Recursive Reasoning with Tiny Networks](https://arxiv.org/abs/2510.04871) studies a small network that repeatedly updates an internal state and a proposed answer. The paper reports puzzle-solving results with 7 million parameters. TRM is a specialized reasoning model. Its results leave open how well the approach transfers to general language tasks.

- **DeepSeek-AI: R1-Zero.** [DeepSeek-R1](https://arxiv.org/abs/2501.12948) explores reinforcement learning for reasoning. R1-Zero skips a preliminary supervised fine-tuning stage and learns from rewards on tasks with checkable answers. It starts from a pretrained base model, so its results depend on substantial prior training.

- **Google DeepMind: AlphaGeometry.** [AlphaGeometry](https://deepmind.google/blog/alphageometry-an-olympiad-level-ai-system-for-geometry/) combines a learned proposal system with symbolic deduction and uses synthetic geometry data for training. It demonstrates advanced reasoning within a structured mathematical domain. Transfer to other domains remains a separate research question.

The question I want to keep asking: how much can a model infer on an unfamiliar task, with how little prior knowledge and computation?
