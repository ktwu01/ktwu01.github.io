---
title: "My PhD Advisor Built a Land Surface Model That Forecasted Hurricane Harvey"
date: 2026-05-09
permalink: /posts/2026/05/zong-liang-yang-noah-mp-advisor/
tags:
  - PhD
  - Noah-MP
  - climate
  - UT Austin
  - mentorship
  - earth system science
---

When you join a lab, you do not just get a research direction. You inherit a 30-year codebase that is currently running inside the U.S. National Water Model and was on the critical path forecasting Hurricane Harvey. That is what working with Zong-Liang Yang at the Jackson School of Geosciences actually looks like.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

> Zong-Liang's chronicle: [ktwugoat.github.io/zong-liang-yang-chronicle](https://ktwugoat.github.io/zong-liang-yang-chronicle/). It is one of a directory of chronicles forked from the [Sean Xiang chronicle template](https://github.com/ktwu01/sean-xiang-chronicle), all built by UT Austin colleagues and me. The full directory: [Ashley Matheny](https://ut01.github.io/ashley-matheny-chronicle/), [Chen Ning Yang](https://ut01.github.io/chen-ning-yang-chronicle/), [Daniella Rempe](https://ut01.github.io/daniella-rempe-chronicle/), [Eric C. Greene](https://yzliu03.github.io/Eric-Greene-chronicle/), [Geeta Persad](https://ut01.github.io/geeta-persad-chronicle/), [Gengchen Mai](https://ut01.github.io/gengchen-mai-chronicle/), [Juan Santiago](https://qijiang-yoyo.github.io/juan-santiago-chronicle/), [Kehan Dong](https://ut01.github.io/kehan-dong-chronicle/), [Marc Hesse](https://ut01.github.io/marc-hesse-chronicle/), [Sean Xiang](https://ktwu01.github.io/sean-xiang-chronicle/), [Zong-Liang Yang](https://ktwugoat.github.io/zong-liang-yang-chronicle/).

Zong-Liang did his PhD at Macquarie University in Sydney in 1992, after a Master's in Meteorology at the University of Melbourne. He spent his postdoc and early research-faculty years at the University of Arizona. He has been at UT Austin since 2001, and today he holds the John A. and Katherine G. Jackson Chair in Earth System Sciences plus the Dave P. Carlton Centennial Professorship, and he directs the Center for Integrated Earth System Science. In 2025 he was elected an AGU Fellow.

I am going to be honest, when you first see that CV you can feel a little intimidated. 230+ peer-reviewed articles, a Google Scholar h-index of 81, more than 8 million dollars in PI funding, and the land surface models he co-developed (CLM and Noah-MP) being used by every major U.S. modeling center plus the National Centers for Environmental Prediction, NSF NCAR, the National Water Center, NASA, NOAA. That is not a research group. That is essentially a small piece of national infrastructure.

But here is the part that actually matters when you are sitting across from him in his office on the fourth floor of the Jackson Geological Sciences Building. He treats Noah-MP like a living thing that you can still poke at, still question, still ask why this particular parameterization was chosen in 2010 and whether it should still be there in 2026. The model is not sacred. The science is.

I am working on integrating explainable AI into Noah-MP to better simulate plant-rock-water interactions. That phrase sounds like grant-application English, so let me unpack it. Noah-MP is a physics-based land surface model. It tries to simulate how rain hits the ground, how water moves through soil, how plants pull it up through their roots, how it gets transpired back into the atmosphere. Every one of those steps has a parameterization, a chunk of code that says "given these inputs, here is roughly what the physics does." Some of those parameterizations are excellent. Some are decades old and were never built to handle, say, the kind of plant hydraulic stress you see in a Texas drought, or the kind of bedrock-water storage that Daniella Rempe has been documenting in California.

The ML side is not "let us replace Noah-MP with a neural network." That misses the entire point. The leverage is in using ML to figure out which parameterizations are wrong, in what regimes, and then sending that information back into the model so the next version of Noah-MP gets the physics right. Then you keep all the things a physics-based model gives you, like extrapolation outside the training distribution, like physical interpretability, like the ability to forecast a hurricane that has not happened yet.

This is what I think people miss when they talk about "AI for science" as if it is a single thing. There is the version where you train a foundation model on weather data and it spits out forecasts. That is interesting. There is also the version where you use AI as a diagnostic tool to find the cracks in the physics, and then you patch the physics. The second version is harder to publish, harder to demo, harder to explain at a conference. It is also the one that has a chance of compounding for the next 30 years, the way Noah-MP itself has compounded.

Zong-Liang has lived through multiple climate research waves and his models have survived all of them. Watching him pick which problems to spend his time on is its own seminar. He will not chase a hot trend. He will spend three weeks on a soil moisture parameterization that, in his judgment, is going to matter for someone modeling a drought five years from now.

I am writing this around six months into my PhD. The work I am doing right now is running on the NSF NCAR Derecho-GPU supercomputer under allocation UTAA0012, which I administer. The first published output from that direction is at AMS 2026, joint with Lingcheng Li, Daniella Rempe, Ashley Matheny, Mehnaz Mbarak, and Zong-Liang. It is just the opening move. The interesting question is what the next 20 papers look like, and whether Noah-MP in 2040 looks meaningfully different because of work this group is doing now.

If you ask me what is the single most useful thing about doing a PhD with someone like Zong-Liang, it is not the chair, the funding, or the network. It is that the model literally runs in production at the National Water Center. The work is not academic in the dismissive sense. It is academic in the original sense, which is, it is going to outlive you.
