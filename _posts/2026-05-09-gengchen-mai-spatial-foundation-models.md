---
title: "Gengchen Mai Is Building Spatial Foundation Models, and Geographers Should Pay Attention"
date: 2026-05-09
permalink: /posts/2026/05/gengchen-mai-spatial-foundation-models/
tags:
  - GeoAI
  - foundation models
  - geography
  - UT Austin
  - spatial reasoning
  - knowledge graphs
---

The same way text foundation models ate NLP and image models ate computer vision, someone is going to build the foundation model that eats spatial reasoning. Gengchen Mai is one of the people taking that bet seriously, and his SEAI Lab at UT Austin is one of the places it is being built.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

> Gengchen's chronicle: [ut01.github.io/gengchen-mai-chronicle](https://ut01.github.io/gengchen-mai-chronicle/). It is one of a directory of chronicles forked from the [Sean Xiang chronicle template](https://github.com/ktwu01/sean-xiang-chronicle), all built by UT Austin colleagues and me. The full directory: [Ashley Matheny](https://ut01.github.io/ashley-matheny-chronicle/), [Chen Ning Yang](https://ut01.github.io/chen-ning-yang-chronicle/), [Daniella Rempe](https://ut01.github.io/daniella-rempe-chronicle/), [Eric C. Greene](https://yzliu03.github.io/Eric-Greene-chronicle/), [Geeta Persad](https://ut01.github.io/geeta-persad-chronicle/), [Gengchen Mai](https://ut01.github.io/gengchen-mai-chronicle/), [Juan Santiago](https://qijiang-yoyo.github.io/juan-santiago-chronicle/), [Kehan Dong](https://ut01.github.io/kehan-dong-chronicle/), [Marc Hesse](https://ut01.github.io/marc-hesse-chronicle/), [Sean Xiang](https://ktwu01.github.io/sean-xiang-chronicle/), [Zong-Liang Yang](https://ktwugoat.github.io/zong-liang-yang-chronicle/).

Gengchen's lab pages and personal website lay out the trajectory. He spent his PhD years at UC Santa Barbara in the geography department, which historically has been one of the strongest places in the US for the formal study of GIScience. He then moved to the University of Georgia for a faculty appointment in the AI institute, before coming to UT Austin in the geography department. His SEAI Lab, the Spatial Explorer of AI Lab, sits inside the College of Liberal Arts geography program at UT Austin and his group page documents the broader research network.

The reason this matters to anyone doing Earth system science is the underlying conviction that spatial data, geographic data, and Earth observation data are not just inputs to be fed into a generic neural network. They have structure, topology, and scale that a generic model architecture is going to miss. Tobler's first law of geography, that nearby things are more related than distant things, is not a statement most language models internalize.

The work coming out of the GeoAI community, of which Gengchen is one of the more visible voices, has been pushing on a few specific problems. The first is location encoding. How do you turn a latitude and longitude into a vector that a neural network can use, in a way that respects the spherical geometry of the Earth and the multi-scale nature of geographic phenomena. The second is integrating knowledge graphs of geographic entities with the kind of statistical learning that foundation models do well. The third is building genuinely multimodal models that can reason across satellite imagery, ground photos, text descriptions, and structured spatial data simultaneously.

If you sit in the Jackson School and look at this from a land surface modeling angle, the immediate question is whether spatial foundation models can help with the parameterization problem. Noah-MP, like every land surface model, has parameters that should vary spatially in physically meaningful ways. Soil hydraulic properties, vegetation water-use strategies, root distributions, all of these have spatial structure. The classical approach is to look up a value in a soil database or a vegetation map. A spatial foundation model that has internalized cross-modal information about a place could in principle do better.

I am going to be honest, the GeoAI literature can read a little disconnected from operational Earth system modeling sometimes. There are papers about spatial transformers that are mathematically elegant but never run on a real climate dataset, and there are papers about climate models that use deep learning in ways that any GeoAI person would call naive. The interesting research lives in the intersection, and I think that intersection is going to grow significantly in the next five years. Gengchen is one of the people who can actually talk across that boundary because he has been on the GIScience side long enough to understand what good spatial reasoning looks like.

What I particularly respect about his approach is the willingness to take geography seriously as a discipline with its own theoretical commitments. A lot of the AI-for-X papers treat the underlying domain as a target dataset and nothing more. The geography is just a benchmark. The SEAI Lab work is the opposite. It starts from real questions in spatial cognition and geographic information science, and asks how modern ML changes what is possible to answer.

There is a practical UT Austin angle. The SEAI Lab is building infrastructure that the broader campus can use, including for projects like mine. If I want to integrate a spatial foundation model into the Noah-MP improvement pipeline, the path of least resistance is to walk across campus rather than reinvent the wheel. That kind of cross-departmental availability is one of the underrated benefits of being at a research university with several strong AI groups in different schools.

The career-shape lesson here is similar to the one I take from a lot of the UT Austin researchers I am writing about. Pick a discipline that is undergoing a real methodological shift, position yourself at the intersection of the old expertise and the new tools, and build the lab that did not exist before you got there. SEAI is exactly that kind of lab.

For me as a PhD student starting now, the question is not whether to use spatial foundation models. The question is whether I can collaborate with people who actually know how to build them, instead of bolting a generic transformer onto a problem and pretending it is novel. The honest answer is, the people who know how to build them are right here, and I should walk over more often.
