---
title: "Benchmark Radar Day 19: Geospatial Signals and Vendor Logo Saturation"
date: 2026-08-14
permalink: /posts/2026/08/benchmark-radar-day19/
tags:
  - AI
  - Benchmarks
  - Geospatial
  - Satellite
  - Visualization
---

Hi, Koutian here. Day nineteen pushed the radar into maps and satellites.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

We expanded the `DATA_SIGNALS` config to watch for geospatial and satellite AI vendors. Geospatial AI is software that reads the Earth from space: land use, crop health, disaster damage, that kind of thing. The radar now tracks benchmarks and models from companies working on Earth observation, remote sensing, and geospatial intelligence.

The frontier chart shows where benchmark scores stop improving, a plateau we call saturation. Those saturation points now display the vendor logos that produced them. When a score curve flattens out, you can see which companies drove it there.

Why this matters to you.

Geospatial and satellite AI is a fast-growing corner of the field. Models like Prithvi (from NASA and IBM), SatMAE, and Clay get tested on tasks like land use classification, change detection, and atmospheric modeling. Adding these signals means the radar is no longer stuck on language and general AI. It now covers a wider slice of AI evaluation.

The vendor logos make the chart tell its own story. Before, you had to cross-check a legend to learn who pushed a benchmark forward. Now the logos say it on the chart itself.

Issues addressed:

- #156: geospatial and satellite vendor signals in DATA_SIGNALS
- Vendor logos on score saturation points

Day twenty: Chinese i18n, insight blocks, and social checklist.
