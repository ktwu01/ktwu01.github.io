---
title: 'AlphaEarthHack: A UT Austin Geoscience Hackathon Project on Earth System AI'
date: 2025-10-10
permalink: /posts/2025/10/alphaearthhack/
tags:
  - hackathon
  - geoscience
  - earth-system
  - ai
  - machine-learning
  - jupyter
  - ut-austin
  - climate
---
AlphaEarthHack is the project our team built for the UT Austin Geoscience Hackathon. The goal: see how far we could push AI on Earth system data inside a single weekend. [Try Live Demo](https://ktwu01.github.io/AlphaEarthHack/)

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

[![GitHub stars](https://img.shields.io/github/stars/ktwu01/AlphaEarthHack?style=social)](https://github.com/ktwu01/AlphaEarthHack/stargazers) [![GitHub forks](https://img.shields.io/github/forks/ktwu01/AlphaEarthHack?style=social)](https://github.com/ktwu01/AlphaEarthHack/fork)

## The Hackathon

The UT Austin Geoscience Hackathon brings together students and researchers across the Jackson School and the broader university to build something concrete on real Earth science problems in a weekend. Our team picked a question we thought was small enough to ship and big enough to matter.

## What We Built

A pipeline that takes Earth observation data, applies a learned representation, and surfaces patterns that would be hard to see in the raw signal. The repo is a Jupyter Notebook walkthrough you can re-run end to end.

The work covers:
- Data ingestion from public Earth science datasets.
- Preprocessing for the messy realities of geospatial data.
- A model layer that produces useful embeddings or predictions.
- Visualizations that make the result legible to a domain scientist.

## Try It in 1 Minute

Open [https://ktwu01.github.io/AlphaEarthHack/](https://ktwu01.github.io/AlphaEarthHack/) for the project page, or clone the repo and run the notebooks locally:

```bash
git clone https://github.com/ktwu01/AlphaEarthHack.git
cd AlphaEarthHack
jupyter notebook
```

## Tech Stack

- **Python** + **Jupyter Notebook** for the analysis pipeline.
- Geospatial libraries (rasterio, xarray, etc.) for Earth science data.
- ML libraries for the model layer.
- HTML for the project landing page.

## Why This Is Worth Reading

Hackathon code is usually thrown away after demo day. We tried to leave AlphaEarthHack in a state where someone — including future us — could pick it up, understand the choices, and extend it. The notebook structure and the README are written for that reader.

## Acknowledgments

Thanks to the UT Austin Geoscience Hackathon organizers and our teammates. Hackathons are won and lost on the people you sit next to.

## Contributing

If you're a geoscience or ML person who wants to extend the pipeline, open an issue or PR at [github.com/ktwu01/AlphaEarthHack](https://github.com/ktwu01/AlphaEarthHack).

---

A weekend isn't enough to solve Earth system science. It is enough to ask a question well.
