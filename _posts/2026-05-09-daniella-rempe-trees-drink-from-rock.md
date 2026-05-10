---
title: "Trees Drink From Rock, and Daniella Rempe Proved It"
date: 2026-05-09
permalink: /posts/2026/05/daniella-rempe-trees-drink-from-rock/
tags:
  - critical zone
  - hydrogeology
  - PhD
  - UT Austin
  - plant water
  - bedrock
---

If you ask most people where trees in California get their water in a drought, they will say "the soil." It turns out a huge fraction of it comes from cracks in the bedrock underneath the soil, and Daniella Rempe is the person who put numbers on it.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

Daniella did her undergraduate degree at UT Austin in Geosystems Engineering and Hydrogeology, that joint program between the Cockrell School of Engineering and the Jackson School of Geosciences. She then did her Master's and PhD at UC Berkeley in Earth and Planetary Science, working primarily at the Eel River Critical Zone Observatory in Northern California. Her dissertation was on water storage and transport in fractured weathered bedrock. She came back to UT Austin in 2016 as Assistant Professor, was promoted to tenured Associate Professor in 2023, and the same year she received the AGU Hydrologic Sciences Early Career Award. She now runs the Rempe Research Group, serves as Department Associate Chair, and directs the Water, Climate and Environment program.

That is the resume version. The reason her work matters to my PhD is that you cannot honestly model land surface processes in places like the western United States without dealing with what she discovered.

The standard land surface model picture is "soil column on top, atmosphere on top of that, plants in between, water moves up and down through this stack." The bedrock layer at the bottom is treated like a wall. Water hits it, stops. Daniella's work showed this is not how nature works. In a lot of mountainous regions, trees have figured out how to extend their root systems down into fractured weathered bedrock and pull moisture from those rock fractures during drought. The volume of water stored in that zone, what people now call the rock moisture reservoir, is large enough that ignoring it gives you the wrong answer about how forests respond to dry years.

The follow-up work was even weirder. She and her group took some of the first carbon dioxide measurements from inside forest bedrock and found that nearly a third of CO2 released by forests is coming from microbes living in rock fractures. Not from the soil. From the rock. The implication is that the carbon cycle picture in those ecosystems is also incomplete if you treat bedrock as inert.

I am co-authoring a paper with her at AMS 2026 on integrating plant hydraulics into Noah-MP. From a modeling standpoint, the question is, how do you take what Daniella has documented in the field and put it inside a model that runs at scale, on a supercomputer, for the entire continental US. There is a very long road between "we measured rock moisture at one watershed in Northern California" and "every grid cell in your global land surface model now correctly accounts for bedrock-water storage." The interesting research is in that road.

Daniella's other contribution that is harder to put on a CV is what she has done for the hydrologic sciences degree programs at UT Austin. She redesigned the hydrology field camp to integrate computational tools, and she said the line that I now repeat to anyone asking me about the field. "Solving big problems with big data is becoming a standard skillset." That sounds obvious until you sit through a hydrology curriculum that still teaches you Darcy's law for two semesters before letting you near Python. She is one of the people pushing the field to update.

What I keep noticing in her work is the discipline. She does not announce a flashy headline result and move on. She measures, she instruments a site, she keeps the instruments running for years, and only then does she write the paper. There is a deep tradition in critical zone science of going to one watershed and understanding it really, really well, then generalizing carefully. Daniella is in that tradition.

For me, working with her means the modeling I do has to pass her field-experimentalist sniff test. If a Noah-MP simulation predicts something about plant water uptake during drought, and that something does not match what she has actually measured at her sites, the simulation is wrong. The model has to defer to the measurements, not the other way around. That sounds obvious, but a lot of modeling careers have been built on simulations that nobody bothered to check against careful field data.

The thing I want to take from her, as a PhD student who is going to spend a lot of years writing code, is the patience. The bedrock-moisture story took years of fieldwork before anyone could write a clean version of it. The good results in this field do not come from the next clever architecture. They come from someone who decided to stay at one watershed long enough to actually understand what the trees were doing.
