---
title: "ResearchClawBench"
date: 2026-09-29
permalink: /posts/2026/09/project-researchclawbench/
tags:
  - media
  - project
---

[ResearchClawBench](https://internscience.github.io/ResearchClawBench-Home/) evaluates whether AI agents can carry out end-to-end scientific research tasks.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

Most AI benchmarks for science test a slice of the job. Answer a hard physics question. Write the code for one analysis. Summarize a paper. Research is the whole loop: read the literature, look at the raw data, decide what experiment to run, run it, notice when the result is wrong, and write down a claim someone else can check. ResearchClawBench asks whether an agent can do that whole loop, start to finish, without a human steering it.

I am one of the 51 authors of the [paper](https://arxiv.org/abs/2606.07591), first submitted to arXiv on May 28, 2026, and submitted to AAAI 2027.

## How the benchmark works

There are 40 tasks across 10 scientific domains. Each task is built from a real published paper. The agent gets the related literature and the raw data the original authors worked from, but not the target paper itself. Its job is to get from the data to the findings on its own.

This setup is the core design choice. A real paper gives you ground truth that experts already accepted. Hiding it means the agent cannot copy the answer, and it has to re-discover it.

Scoring uses expert-curated multimodal rubrics. Each target scientific artifact, a figure, a number, a fitted curve, a conclusion, is broken into weighted criteria. A rubric can check whether the agent reproduced the key result, and it also leaves room to credit a result the original paper did not reach. The project site describes this as moving "from Re-Discovery to New-Discovery." On the site's frontier view, 50 means matching the original paper and 100 means going beyond it.

## What the results say

The paper evaluates seven autonomous research agents under one protocol, and seventeen native language models through a lightweight harness called ResearchHarness.

The numbers are low. The strongest agent, Claude Code, averages 21.5. The strongest model under ResearchHarness, Claude-Opus-4.7, averages 20.7. Even the frontier, the best result on each task across every system, averages only 26.5. Matching the original paper would be 50.

So the best combination of everything we tested gets about halfway to re-discovering work that human scientists already published.

## Why agents fail

The error analysis sorts failures into three groups.

1. **Experimental protocol mismatch.** The agent runs a different experiment from the one the question needs, then answers confidently about the wrong thing.
2. **Evidence mismatch.** The claim in the write-up does not follow from the numbers the agent actually produced.
3. **Missing scientific core.** The output looks like a paper, with figures, sections, and citations, but the central finding is absent.

The third one worries me most. A human reviewer skimming the output would see something that looks finished. That is the gap between producing research-shaped text and doing research.

## What I take from it

Two things.

First, "AI scientist" claims need a test where the answer is hidden and the data is raw. Benchmarks built from exam questions measure recall and reasoning on a clean problem. They do not measure whether a system can choose the right experiment when nobody tells it what the experiment is.

Second, the rubric matters more than the leaderboard. A single score hides whether an agent missed the method, the evidence, or the point. Weighted criteria per artifact tell you where the system broke, which is the information you need to improve it.

The code is on [GitHub](https://github.com/InternScience/ResearchClawBench), and the project site links the datasets on Hugging Face and ModelScope.

An agent that writes like a scientist is not yet an agent that discovers like one.

Explore [ResearchClawBench](https://internscience.github.io/ResearchClawBench-Home/).
