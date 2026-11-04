---
title: "Earth-Space-AI"
date: 2026-09-29
permalink: /posts/2026/09/project-earth-space-ai/
tags:
  - media
  - project
---

[Earth-Space-AI](https://github.com/earth-space-ai) is an open-source organization for AI tools, skill packages, and research projects in earth and space science.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

Earth-system models are some of the largest scientific codes in the world. WRF forecasts the weather. CTSM simulates land and vegetation. WACCM-X reaches from the ground to the edge of space. Each one carries decades of judgment about how to build it, configure it, and debug it, and most of that judgment lives in user-group mailing lists, workshop slides, and the heads of a few senior researchers.

An AI coding agent can read the source tree. It cannot read the mailing list from 2014 that explains why a namelist option should never be set the obvious way. Earth-Space-AI exists to close that gap. Its one-line description: "Procedural-knowledge skills for Earth, planetary, and space sciences."

## What is in it

The organization hosts skill packages, each a structured set of markdown files that an agent loads on demand and a researcher can read as a reference. A `SKILL.md` file routes the agent to the right section, and deeper reference documents load only when needed, so the agent does not burn its context window on material it does not need. I described the layout in detail in an [earlier post](/posts/2026/05/earth-space-ai-org-skill-packages/).

Packages so far cover, among others:

- **WRF**, the Weather Research and Forecasting model
- **CTSM**, the Community Terrestrial Systems Model
- **Noah-MP**, a land surface model, with its HRLDAS driver
- **WACCM** and **WACCM-X**, the whole-atmosphere models in CESM, the second extended to the ionosphere and thermosphere
- **ROMS**, a regional ocean model
- **RegCM**, a regional climate model from ICTP
- **OpenIFS**, ECMWF's research and education release of its forecast model
- **NorESM**, the Norwegian Earth System Model

Beyond model skills, the organization runs two community tools. [Benchmark Radar](https://github.com/earth-space-ai/benchmark-radar) is a daily radar of AI benchmarks and datasets, which I started and which has been forked more than 50 times. [Scientific Resources](https://github.com/earth-space-ai/scientific-resources) tracks compute, cloud and API credits, and research funding open to scientists.

## Why skills and not a new model

The usual pitch for AI in earth science is a new neural model that replaces the physics. Those models are fast and impressive, and they still need the physics-based models for training data, for the variables nobody has learned yet, and for the cases where you need to know why. The physics-based models are not going away.

What slows researchers down is getting those models to run correctly. A graduate student can lose a semester to a build error or a misconfigured domain. If an agent can carry the setup knowledge, that semester goes back to science. A skill package is cheap to write, easy to check, and useful on day one, which is why I started there.

## What is still hard

Skills go stale when the upstream model changes, so each package has to be maintained alongside the model it covers. Credit matters too. These models belong to large communities, and a skill package should point users back to official documentation and licenses rather than compete with them.

The most valuable part of a scientific model is often the advice that never made it into the manual.

Browse [Earth-Space-AI on GitHub](https://github.com/earth-space-ai).
