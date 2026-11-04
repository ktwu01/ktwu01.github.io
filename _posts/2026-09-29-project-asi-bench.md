---
title: "ASI-Bench"
date: 2026-09-29
permalink: /posts/2026/09/project-asi-bench/
tags:
  - media
  - project
---

[ASI-Bench](https://asibench.apexin.ai/) evaluates AI agents on 60 research-grade tasks across 11 scientific domains.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

A common way to test an AI scientist is to hand it a well-posed problem and check the answer. ASI-Bench asks a harder question. What happens when you take the instructions away?

I am one of the 42 authors of the [paper](https://arxiv.org/abs/2608.17271), "ASI-Bench: At the Dawn of Artificial Superintelligence," posted to arXiv on August 18, 2026. The project comes from Apex Intelligence and is released under the MIT License.

## The tasks

There are 60 project-level research tasks in 11 domains: astronomy, biology, biostatistics, chemistry, computer science, earth science, electrical engineering, materials, math, physics, and robotics. Some examples from the site:

- Study the Kosterlitz-Thouless phase transition in the 2D XY model.
- Compute an electron-transfer rate with Marcus theory.
- Calibrate a LiDAR against an IMU.
- Optimize a solver for the Euclidean traveling salesman problem.

Each one is a full project. An agent has to understand the problem, pick a method, implement it, run experiments, diagnose failures, refine, and validate. Each task has a fixed objective, fixed data, and expected outputs, so a scorer can check the submitted artifacts against ground truth.

More than 40 experts built the tasks, with over 31,000 hours of human work. Every task went through expert review, AI-assisted auditing, sandbox execution, and scorer validation before it entered the set.

## Taking the guidance away

The key design is the four prompt levels, B1 to B4. The scientific goal stays the same at every level. What changes is how much method the prompt gives the agent. At the top level the agent gets the full recipe. At the bottom it gets the goal and has to work out the method itself. The levels also add distractors, to test whether the agent can ignore information that looks useful and is not.

This turns one benchmark into a measurement of dependence. You can see exactly how much of an agent's score came from the human who wrote the prompt.

## What the numbers show

Across 18 agent and model configurations, the average score falls as guidance is withdrawn:

| Guidance | Average score |
|---|---|
| Full methodological guidance | 50.91 |
| Method named only | 29.10 |
| Agent chooses the method | 26.62 |

The biggest drop happens at the first step. Once the prompt stops spelling out how to do the work, scores fall by about 40 percent. The paper's conclusion is direct: current systems still lean heavily on human guidance and are far from running project-level research on their own.

Submissions must produce reproducible artifacts that pass sandbox execution, and each one carries a provenance hash that the maintainers verify before it reaches the leaderboard. Anyone can run it with `pip install asibench`. As of November 3, 2026, the leaderboard lists 25 agent and model combinations, mostly Claude Code and Codex running a range of frontier models.

## Why this design matters

When people report that a model "did research," they rarely report how much of the method was in the prompt. That hidden variable can account for half the score. A benchmark that holds the goal fixed and varies the guidance makes the variable visible.

My skeptical read is that the B1 score is the one most papers quote, and the B4 score is the one that predicts whether a system can work in a lab where nobody knows the method yet. The gap between them is what to watch.

An agent's real ability starts where the instructions end.

Explore [ASI-Bench](https://asibench.apexin.ai/).
