---
title: 'Earth System Model Skill Packages: Deep Knowledge Bundles for Noah-MP, CLM, CAM, MOM6, WRF, E3SM, and More'
date: 2026-05-07
permalink: /posts/2026/05/esm-skill-packages/
tags:
  - earth-system-models
  - climate-modeling
  - noah-mp
  - clm
  - cam
  - mom6
  - wrf
  - e3sm
  - jules
  - parflow
  - summa
  - vic
  - skill
  - llm
  - ai-agents
---
Earth system models are some of the most complex scientific software ever written, and they are also some of the worst-documented for newcomers. I have been building a series of "skill packages" — structured, progressive-disclosure knowledge bundles — for the major Earth system and land surface models, designed to be used by both new graduate students and AI coding agents.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

## What Is a Skill Package

Each repo in this series is built around a `SKILL.md` routing hub that points to a `reference/` directory of deep-dive documents. The structure is designed so that:

- A new graduate student can find the install path, the case workflow, and the debugging section without reading every paper in the bibliography.
- An AI coding agent can route to the right reference doc on demand instead of stuffing the entire model manual into context.
- Contributors know exactly where new content belongs.

The format borrows from progressive disclosure: high-signal index at the top, full depth one click down.

## The Skill Packages

| Model | Domain | Repo |
| --- | --- | --- |
| **Noah-MP** | Land surface (NCAR/noahmp + HRLDAS) | [noahmp-skill](https://github.com/ktwu01/noahmp-skill) |
| **CTSM / CLM** | Land surface (Community Terrestrial Systems Model) | [ctsm-skill](https://github.com/ktwu01/ctsm-skill) |
| **JULES** | Land surface (Joint UK Land Environment Simulator) | [jules-skill](https://github.com/ktwu01/jules-skill) |
| **SUMMA** | Land surface (Structure for Unifying Multiple Modeling Alternatives) | [summa-skill](https://github.com/ktwu01/summa-skill) |
| **ParFlow** | Watershed flow (parallel) | [parflow-skill](https://github.com/ktwu01/parflow-skill) |
| **VIC** | Macroscale hydrology (Variable Infiltration Capacity) | [vic-skill](https://github.com/ktwu01/vic-skill) |
| **CAM** | Atmosphere (Community Atmosphere Model) | [cam-skill](https://github.com/ktwu01/cam-skill) |
| **WRF** | Atmosphere (Weather Research and Forecasting) | [wrf-skill](https://github.com/ktwu01/wrf-skill) |
| **MOM6** | Ocean (Modular Ocean Model 6) | [mom6-skill](https://github.com/ktwu01/mom6-skill) |
| **E3SM** | Coupled (Energy Exascale Earth System Model) | [e3sm-skill](https://github.com/ktwu01/e3sm-skill) |

## What Each Skill Package Covers

The exact contents vary by model, but every package has the same shape:

- **Architecture** — the data flow and the major code units, in a few diagrams.
- **Physics options** — what knobs exist, what they actually do.
- **Case workflow** — how to set up, compile, and run a real case.
- **Output and diagnostics** — the formats and how to inspect them.
- **Coupling** — how the model talks to its neighbors (atmosphere, ocean, land).
- **Debugging** — the failure modes that bite every new user.
- **Contributing** — how to send a PR upstream.

## Why I Built These

Three reasons:

1. **Personal use.** I work on land surface models for a living. I needed the notes anyway.
2. **AI-agent compatibility.** When AI agents try to modify Earth system code, they fail in revealing ways. A well-structured skill package improves their hit rate dramatically. (Related: [ESM-bench](/posts/2026/04/esm-bench-ai-agents-earth-system-models/), my benchmark for measuring exactly this.)
3. **Onboarding.** Most of these models would benefit from one good "first 30 days" document. The skill packages are an attempt at that document.

## Who These Are For

- New graduate students starting on a specific model.
- AI coding agents working on Earth system code.
- Researchers cross-checking how a similar problem is handled in another model.
- Anyone writing tutorials or documentation for these communities.

## Contributing

Each repo is independent. If you spot something wrong in a specific skill package, open an issue or PR there. If you want to start a skill package for a model that isn't on this list, the noahmp-skill repo is the closest thing to a template.

---

Earth system models are one of the few software ecosystems where a strong index is more valuable than a clever feature. These skill packages are my attempt at that index.
