---
title: 'Five Orders of Magnitude on Purpose, Why Text AI and Embodied AI Are Not Playing the Same Data Game'
date: 2026-05-08
permalink: /posts/2026/05/text-vs-embodied-ai-data-first-principles/
tags:
  - ai
  - llm
  - robotics
  - embodied-ai
  - information-theory
  - first-principles
  - earth-system-model
  - ai4science
---

Call it a \(10^5\) gap if you like, once you put semantic entropy and effective training samples on the board, the difference between internet-scale text and embodied robotics data stops sounding like rhetorical inflation and starts sounding almost conservative. You just have to separate raw physics bits from semantics a learner can actually use.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

I argued this back and forth with friends who train manipulation policies and world models until we tired ourselves out. The strange part is we agreed more at the end than at the start. The fight was never really about who had more bytes. It was about how much abstraction humans already folded into the signal before it reached the model.

## Compression and symbolic abstraction

Text is physics after a brutal compression pass into symbols. One token (often quoted as ~0.75 of an English word) can smuggle an entire causal stack under a casual sentence. When you read that a cup fell and shattered, you are not getting six atomic events. Gravity, rigid contact, brittle fracture mechanics, all of that got collapsed into everyday language because human brains already bridged the gap from continuous flow to discrete wording.

Embodied stacks live on the other side of that bridge. Video frames, tactile pressure traces, joint angles, these are high-rate sensor streams. Ten seconds of grasping at 30Hz is on the order of three hundred high-dimensional images before you even talk about depth, force, or proprioception. Plenty of raw measurement, still thin on reusable semantics.

So from the angle of effective world description, the tens of trillions of tokens sitting on the open web are not just big numbers. They are a map laid down by millennia of checked logic. Cross-embodiment collections like Open X-Embodiment are still closer to teaching a toddler to walk than to encoding full civilization-scale know-how. A five- or six-order-of-magnitude gap in coverage, at the semantics layer, does not shock me.

## Sampling cost and economics

First principles push you toward cost per sample next.

Language-model data mostly comes from accumulated internet text, books, code, pages. Collection is mostly passive. Marginal cost trends toward zero. Scale rides bandwidth and storage curves. Embodied data comes from real contact or sim rollouts. Collection is active interaction. Wear, power, human supervision push unit cost up. You cannot duplicate wall-clock time the way you duplicate bits.

Sanity-check the magnitudes. Frontier LLM training conversations often land near tens of trillions of tokens, call it \(1.5 \times 10^{13}\) as an order-of-magnitude anchor. Even pooling across institutions, action-labeled trajectories that plug cleanly into imitation or reinforcement pipelines often sit closer to the \(10^6\) million-trajectory ballpark.

$$
\frac{10^{13}}{10^6} = 10^7
$$

That is already a ten-millionfold ratio before you argue about how many token-scale semantics hide inside a single rollout. Shave that down with generous counting of semantic units per trajectory and landing near a hundred thousand X (\(10^5\)) still feels like a deliberately gentle estimate. That is how I square it with intuition without hand-waving.

## Dimensionality and state space

There is a sharp mathematical sting here too. Text models mostly negotiate discrete sequences over a finite vocabulary laid out in one dimension. Embodied agents wander continuous spaces. A six-DoF arm plus vision plus touch feeds a state you can treat as effectively infinite-dimensional.

Here is the paradox people love to quote. Raw video volume at YouTube scale, measured in exabytes, dwarfs text by raw bits. The scarcity is not pixels. The scarcity is actions, intent, reusable supervision. What you can feed into policy learning or dynamics learning without pretending remains tiny compared to passive footage.

So the field leans on LLMs or VLMs as a brain and fine-tunes a smaller cerebellum on modest trajectory sets. That split is not lack of ambition. It tracks the supply curve of validated embodied samples.

## Paradigm shift and the Earth-systems thread

Put the three panels together and I buy your audit. Semantic-layer text data can easily sit five or more orders of magnitude above effective embodied supervision, and the sentence survives scrutiny.

Reserve the twist. If world models learn stable physics from massive unlabeled video so that representation no longer screams for human action labels, embodied stacks could swing the comparison. The physical world is not short on information in principle. The variable that moves is whether you can distill causal structure out of unlabeled streams at scale.

I keep flashing to what I am building around Earth Systems Model Bench. Weather, hydrology, land models, it is the same class of headache. These fields are sensor streams off a planet-sized body, high-dimensional and continuous. Turning them into semantic tokens that models can act on, and benchmarks that track decisions not only curves, is part of the work that closes those order-of-magnitude gaps from the geoscience side.

If you want to keep pushing on how foundation models squeeze entropy out of physics, we can take the information-theory thread another lap.
