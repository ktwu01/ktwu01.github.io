---
title: 'When Climate Data Comes Alive: A Day at TACC'
date: 2025-04-10
permalink: /posts/2025/04/tacc-field-trip/
tags:
  - field-trip
  - TACC
  - climate-science
  - visualization
  - earth-system-models
---

<!-- https://gemini.google.com/app/44385fe12abbae34 -->

On April 10, 2026, our GEO 371/391T Climate Data class ventured to the Texas Advanced Computing Center (TACC)—one of the largest university supercomputing facilities in the United States. What started as a routine field trip became something Professor Geeta Persad later described as "one of the best in recent years," noting she saw "lights in students' eyes" for the first time in a while. This wasn't just about seeing big computers. It was about wrestling with real climate science challenges and experiencing the moment when abstract data transforms into tangible understanding.

## The Challenge: Making Sense of Dimensional Chaos

Climate data isn't just big—it's bewilderingly multi-dimensional. Our task for the day was to explore extreme precipitation patterns using datasets that spanned:

- **2-D space** (latitude and longitude across the globe)
- **1-D time** (historical records through future projections)
- **4 observational datasets** and **10 different climate models**
- **~30 realizations** of natural variability (because Earth's climate is inherently chaotic)
- **3 future emission scenarios** (optimistic, middle-of-the-road, and business-as-usual)

We focused specifically on rolling time series of 1-day, 3-day, and 5-day cumulative rainfall at the 95th percentile—essentially tracking extreme precipitation events. The sheer dimensionality was overwhelming at first.

## The First Struggle: Parallel Coordinates and Information Overload

Our first tool was **PyCinema**, which uses parallel coordinate plots to help navigate multi-dimensional data. The initial reaction from most students? Confusion. 

One group spent nearly 45 minutes just trying to understand what each axis represented. "Wait, so this line represents one model's prediction for one location under one scenario?" asked a student, tracing a path through the tangled web of lines on screen. The answer was yes—and there were hundreds of such lines.

The breakthrough came when students realized they could interactively filter the data. By selecting specific ranges on different axes, they could isolate patterns. One team investigating Southeast Asian monsoons discovered that when they filtered for high 5-day cumulative rainfall, only certain models showed agreement with observational data. "It's like the models are arguing with each other," one student remarked. That's exactly what model uncertainty looks like.

## The "Aha" Moment: From Spaghetti Plots to Scientific Questions

The real learning happened when groups started formulating their own research questions:

**Group example** asked: "Which climate models best match historical observations for extreme rainfall in the Amazon basin?" They discovered that the GFDL model showed strong agreement for 3-day events but diverged significantly for 1-day extremes. This led to a discussion about model resolution and convective parameterization—concepts that suddenly mattered because they explained what students were seeing.

**Group 1** tackled xxx.

**Group 2** explored xxx.

## The Technical Hurdle: Paraview and 3D Visualization

After isolating interesting data subsets in PyCinema, students moved to **Paraview** for high-fidelity 3D visualization. This transition proved challenging.

"I can't figure out how to make the mesh of the continent explicitly visible," one student admitted, staring at a globe rendered in rainbow colors. Francesca from the TACC team walked them through ???.


"I can't figure out how to make the mesh of the continent explicitly visible," and one student from group 2 came to ask group1. and soon solved.


## The HPC Tour

Walking through TACC's machine room provided crucial context. Standing in front of rows of blinking servers, students learned that a single high-resolution climate model run for 100 simulated years can take weeks of real time on these machines and consume enough electricity to power a small town.

and like plane engine 轰鸣。。

[figures]

"Wait, so when we're running our Jupyter notebooks on TACC, we're using these?" a student asked, gesturing at the supercomputers. Yes—though their classroom exercises used a tiny fraction of the capacity. The scale suddenly made sense: you need this much computing power because you're solving fluid dynamics equations for millions of atmospheric grid cells, thousands of times per simulated day, for decades or centuries of simulation.

<!-- One student who'd been skeptical about climate models earlier in the semester had a visible shift in perspective. "I thought they were just, like, statistical fits or something. But you're actually solving physics equations for every point on Earth?" The computational intensity made the models' limitations—and their achievements—more tangible. -->

One student tried make maps herself and really said maps are difficult. and more respect for those scientists. with fuding winter these years, she still be hopeful to do phd in US with enthusiasm in sci.


## The Lightning Talks: Science Communication Under Pressure

The day concluded with 5-minute "lightning talks" where each group presented their question, workflow, visualization, and conclusions. This was harder than expected.

Groups that had spent hours exploring data struggled to distill their findings. "We found that... well, it's complicated," began one presentation.  Professor Persad gently pushed back: "What's the one thing someone should remember from your work?" This forced students to identify their core finding: "Model xxx."

Another group created a stunning Paraview visualization but couldn't explain what it showed scientifically. "It looks cool, but what am I learning?" Greg asked. The students regrouped and added annotations, highlighting specific regions where their chosen model diverged from observations. The revised version told a clear story.

The best presentation came from a group (Titus Li) that kept it simple: one clear question, well-filtered PyCinema plots showing their selection process, one Paraview visualization with a focused color scale, and three bullet points of conclusions. "Natural variability dominates near-term Texas precipitation uncertainty" was their headline finding, backed by visual evidence.

## What Students Actually Learned

Beyond the technical skills with PyCinema and Paraview, students gained several deeper insights:

1. **Models are tools, not truth**: Different models make different assumptions. Understanding where they agree and disagree is itself scientific knowledge.

2. **Visualization is analysis**: The process of creating a meaningful visualization forces you to understand your data. Pretty pictures without scientific insight are just decoration.

3. **Communication is hard**: Understanding something yourself and explaining it clearly to others are different skills, both essential for science.

## The Lights in Their Eyes

Professor Persad's observation about seeing "lights in students' eyes" captured something important. This wasn't about passive learning or memorizing facts. Students were actively struggling with real scientific challenges—the kind researchers face daily. The frustration when PyCinema plots made no sense, the excitement when patterns emerged, the satisfaction of creating a visualization that actually communicated something meaningful—these are the experiences that transform students from consumers of science to practitioners of it.

One student summed it up during the bus ride back: "I finally get why climate scientists are always talking about uncertainty. It's not that they don't know anything—it's that they know exactly how much they don't know."

That's the light Professor Persad saw: the moment when climate data stopped being abstract numbers and became a window into understanding our planet's future.

---

*Special thanks to Greg and Francesca from TACC's visualization team for their patient guidance, and to Professor Geeta Persad for designing a field trip that challenged us to think like climate scientists.*
