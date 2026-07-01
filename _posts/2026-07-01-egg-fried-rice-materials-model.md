---
title: 'A Materials-Science Model of Egg Fried Rice, Three Years Later'
date: 2026-07-01
permalink: /posts/2026/07/egg-fried-rice-materials-model/
tags:
  - physics
  - chatgpt
  - open-source
  - modeling
  - food
  - side-project
---

In October 2023 I asked ChatGPT an over-engineered question: how do you fry rice so that *every* grain of rice ends up bonded to egg, with no bare rice grains and no isolated clumps of egg sitting off on their own? I saved that conversation as an HTML file, dropped it in my Downloads folder, and did not look at it again for almost three years. Last week I finally turned it into an actual [open-source repo](https://github.com/ktwu01/egg-fried-rice-materials-model), and going back through the original conversation to build it was more interesting than I expected.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

**The question was silly on purpose, which is exactly why it turned into real modeling.**

"No bare rice, no isolated egg" is not how anyone actually judges fried rice, but stating it as a hard constraint is what forced the conversation past vague cooking advice ("use high heat," "stir constantly") into something with actual variables. Once you ask for full, uniform coverage as a literal condition, you need a notion of coverage, a way for it to change over time, and some description of what's fighting against it. That's a materials-science problem whether or not you intended to write one.

**ChatGPT briefly solved the wrong dish, and that mattered.**

Partway through, the conversation drifted into "egg-wrapped rice," which is a real but different dish where a solid egg sheet encases a block of rice, rather than egg fragmenting into a coating across many separate grains. It's an easy mix-up: both involve egg and rice achieving maximal mutual contact, but one is a continuous membrane problem and the other is a dispersed-coating problem. Sorting out which dish we were actually modeling mattered because the two need different physics. A membrane wrapping a block is a geometry problem. A coating spread thin across thousands of separate grains, each getting knocked into the egg and into each other by a spatula, is a stochastic kinetics problem. Getting pulled toward the wrong one and then explicitly correcting course is part of why the resulting first-pass model was usable at all.

**The 2023 model's core idea was right: treat coagulation as a phase transition, not a temperature switch.**

Egg white and yolk are not "raw" and then instantly "cooked" past some threshold temperature. Proteins denature and cross-link progressively, so the fraction of egg that has coagulated at time *t*, call it φ(t), is a continuous variable, not a step function. The original conversation modeled adhesion energy as proportional to that coagulated fraction, on the reasoning that raw egg doesn't stick to much of anything but fully coagulated egg forms a real bonded film, so partial coagulation should give partial stickiness. Then it multiplied that adhesion term by a "contact probability" that depended on stirring, on the idea that egg and rice have to physically collide before they can bond at all. Two effects, multiplied together into one binding probability. That's a reasonable skeleton, and it's also where all the real gaps were.

**The original coagulation kinetics were a guess, not a mechanism, so I replaced them with the same math used for crystallization.**

The 2023 model treated φ(t) as a bare first-order relaxation, coagulation approaching completion smoothly and exponentially from the moment heat is applied. That's not how protein coagulation actually works. Coagulation nucleates at scattered points and then grows outward from those nuclei, which is exactly the physical situation that Avrami kinetics was built to describe for crystallization: φ(t) = 1 − exp[−(k(T)t)ⁿ]. The exponent n controls whether growth looks closer to instantaneous nucleation everywhere at once or a slower nucleate-then-spread process, and k(T) carries the temperature dependence, so a hotter wok both starts coagulation sooner and drives it faster. Swapping in Avrami kinetics wasn't cosmetic; it changes the *shape* of how coverage builds over the cook, which changes everything downstream that depends on timing.

**The original stirring term had the sign backwards, and fixing it revealed a real optimum.**

This is the part of the 2023 conversation I'm least proud of and most glad I went back to. The original model used P = P₀e^(−I/I₀) for contact probability as a function of stirring intensity I, which means more stirring monotonically reduces egg-rice contact, with no stated mechanism for why. It also flatly contradicts kitchen experience: barely-stirred fried rice does not bond evenly, it scrambles into segregated patches. The rework instead models two competing effects that both plausibly scale with stirring intensity. Collision frequency between rice grains and egg fragments grows roughly linearly with I, more agitation means more chances to touch. But stirring is not purely constructive: it also physically tears already-bonded egg film back off the grains it's stuck to, and that shear-induced fragmentation grows roughly quadratically with I, since it depends on both how often grains collide and how hard. Linear gain, quadratic loss, means fragmentation eventually wins at high I. That produces a genuine non-monotonic optimum, a specific stirring intensity I* that maximizes final coverage for a given cook time, instead of a model where the answer to "how much should I stir" is just "as little as possible" or "as much as possible." Both under-stirring and over-stirring ruining a dish, for different physical reasons, is a very ordinary cooking experience. The original model couldn't produce that. The rework does.

**Even a perfect process can't beat not having enough egg.**

The original conversation didn't budget egg mass at all — implicitly, given enough time and stirring, coverage could approach 100% regardless of how little egg was in the pan. I added a stoichiometric ceiling, θ_max(r) = min(1, r/r_c), where r is the egg-to-rice mass ratio. Below some critical ratio r_c, there just isn't enough coagulated protein to physically coat every grain, no matter how well-timed or well-stirred the process is. This is the most obvious fix in hindsight and the one the original conversation most clearly missed, because it was reasoning purely in terms of rates and probabilities without ever checking the underlying mass balance.

**"Fully bonded" is a claim about variance, not just about the average.**

The original question was about *every* grain being bonded, and the original model only ever tracked mean coverage, ⟨θ⟩. But a population of rice grains can hit a high mean coverage while still failing the actual question: some grains completely bare, others buried in egg, averaging out to a respectable-looking number that describes no individual grain in the pan. The rework adds a real criterion for "no isolated rice grains, no isolated egg": you need both ⟨θ⟩ ≥ θc *and* low variance across grains. High mean with high variance is exactly the "bald patches next to egg clumps" failure mode anyone who's rushed a stir-fry has produced.

**The repo keeps the original mistake visible instead of quietly fixing it.**

[`original-2023/蛋炒饭的材料学模型.html`](https://github.com/ktwu01/egg-fried-rice-materials-model) is the literal, untouched browser-saved snapshot of the 2023 conversation, framework JS bundles and all, preserved byte-for-byte rather than cleaned up or re-exported. I could have just written up the improved model and left the original in a private folder. I didn't, because the gaps above are only interesting in contrast with what was actually said in 2023, and because a three-year-old ChatGPT conversation with a wrong stirring sign and no mass balance is a more honest artifact than a tidied-up summary of it would be.

**The interactive demo caught its own bug after I thought it was done.**

[`demo.html`](https://github.com/ktwu01/egg-fried-rice-materials-model) is a self-contained, no-build-step simulation of the reworked model: sliders for wok temperature, stirring intensity, egg-to-rice mass ratio, and cook time, an animated wok of rice grains that shift from white to golden as their simulated coverage builds, and a live numerical sweep that finds the optimal stirring intensity I* for whatever parameters are currently set. After I published it, I noticed the egg:rice ratio slider stopped doing anything visible once you moved it past roughly a third of its range. The cause was r_c, the critical ratio in the stoichiometric ceiling, being set too small, so the coverage cap saturated at 1.0 well before the slider reached its own maximum — the rest of the slider's range was silently doing nothing. The fix was widening r_c so the cap scales across the slider's full range instead of maxing out early. It's a small bug, but it's the kind that's easy to miss precisely because the demo still looks like it's working: nothing crashes, the animation still runs, it just quietly stops responding to one of your inputs.

None of this needed to be this rigorous. It's fried rice. But the reason I went back to a three-year-old browser snapshot and actually rebuilt the model instead of just writing a nostalgia post about it is that the original conversation had specific, identifiable gaps, a backwards stirring term, no mass balance, no variance criterion, and those gaps were fixable with standard tools from an adjacent field. That's a more satisfying use of an old ChatGPT transcript than I expected to get out of my Downloads folder.

Repo, if you want the code, the theory writeup, or the original transcript: [github.com/ktwu01/egg-fried-rice-materials-model](https://github.com/ktwu01/egg-fried-rice-materials-model)

**Related posts:**
- [中文版：蛋炒饭材料学模型，三年之后]({{ site.baseurl }}/zh/posts/2026/07/egg-fried-rice-materials-model/)
