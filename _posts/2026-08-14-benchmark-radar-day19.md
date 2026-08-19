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

The radar expanded into geospatial and satellite AI. Day nineteen added domain-specific signals and vendor logos to the saturation chart.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

## What shipped

**Geospatial/satellite vendor signals.** The DATA_SIGNALS configuration was expanded to include geospatial and satellite AI vendors. This means the radar now watches for benchmarks and models from companies working on Earth observation, remote sensing, and geospatial intelligence.

**Vendor logos on saturation points.** The score saturation points in the frontier chart now display vendor logos. When a benchmark's scores reach a saturation plateau, the chart shows which vendors contributed those scores.

## Why it matters

Geospatial and satellite AI represent a growing segment of the benchmark landscape. Models like Prithvi (NASA/IBM), SatMAE, and Clay are being evaluated on tasks like land use classification, change detection, and atmospheric modeling. Adding these signals meant the radar was no longer limited to NLP and general AI benchmarks; it was covering the full breadth of AI evaluation work.

The vendor logos on saturation points made the frontier chart self-documenting. Previously, you needed to cross-reference a legend to understand who was driving a benchmark's score progression. Now the logos tell the story directly.

## Issues addressed

- \#156: geospatial/satellite vendor signals in DATA_SIGNALS
- Vendor logos on score saturation points

Day twenty: Chinese i18n, insight blocks, and social checklist.
