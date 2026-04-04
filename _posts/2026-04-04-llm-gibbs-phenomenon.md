---
title: "The Gibbs Phenomenon in LLMs: Why Hallucination is Mathematical Destiny"
date: 2026-04-04
permalink: /posts/2026/04/04/llm-gibbs-phenomenon/
tags:
  - AI
  - LLM
  - Mathematics
  - Machine Learning
---

When continuous functions meet discontinuous truth: Understanding LLM hallucinations through the lens of Fourier analysis.

[Koutian Wu](ktwu01.github.io)

## The 8.9% Overshoot That Explains Everything

In 1899, physicist [Josiah Willard Gibbs](https://en.wikipedia.org/wiki/Josiah_Willard_Gibbs) discovered something peculiar: when you try to approximate a discontinuous function (like a square wave) using continuous functions (sine and cosine waves in a Fourier series), you inevitably get an overshoot of approximately 9% at the discontinuity point. No matter how many terms you add to your series, this overshoot never disappears—it just gets narrower and taller, converging to exactly 8.9% of the jump height.

This isn't a bug. It's not a numerical error. It's a fundamental mathematical property of continuous approximation.

And it might be the most underappreciated insight into why large language models hallucinate.

## The Parallel: Neural Networks as Continuous Function Approximators

Neural networks, at their core, are sophisticated continuous function approximators. The [Universal Approximation Theorem](https://en.wikipedia.org/wiki/Universal_approximation_theorem) tells us that a neural network with sufficient capacity can approximate any continuous function to arbitrary precision. This is powerful—but notice the constraint: *continuous* functions.

The world, however, is not entirely continuous. Human logic, objective truth, and factual knowledge often contain sharp discontinuities:

- A statement is either true or false (not 0.51 true)
- A historical event either happened or didn't happen
- A mathematical proof is either valid or invalid
- A URL either exists or doesn't exist

These are step functions—abrupt transitions from 0 to 1, from false to true, from nonexistent to existent. They represent the discrete, quantum nature of reality that resists smooth interpolation.

## The Gibbs Phenomenon in LLM Space

When we train an LLM, we're essentially asking a continuous probability distribution (the model's output space) to fit discrete, absolute truths. The model learns to assign probabilities to tokens, creating smooth gradients across its vast parameter space. But when it encounters a sharp logical boundary—a fact that is definitively true or false—it faces the same challenge that Fourier series face with square waves.

The result? That 8.9% overshoot manifests as **hallucination**.

Consider these examples:

1. **URL Hallucinations**: An LLM might generate `https://example.com/page1` when the actual URL is `https://example.com/page2`. The model has learned the smooth pattern of URL structures but overshoots when trying to approximate the discrete truth of which specific page exists.

2. **Date Confabulation**: Asked about when an event occurred, the model might confidently state "March 15, 2023" when it actually happened on "March 20, 2023". The continuous probability space around temporal information creates oscillations near the true discontinuous fact.

3. **Logical Reasoning Errors**: In multi-step reasoning, each logical step is a discrete transition (valid → valid or valid → invalid). The continuous approximation introduces small errors that compound, leading to confident but incorrect conclusions.

## Why This Matters: Hallucination as Mathematical Destiny

This perspective reframes hallucination from an engineering problem to a fundamental mathematical constraint. As long as we use continuous parameter spaces (neural networks) to approximate a world containing discrete truths, some level of hallucination is mathematically inevitable.

The Gibbs phenomenon teaches us several lessons:

### 1. You Can't Eliminate It, Only Relocate It

Just as adding more Fourier terms makes the overshoot narrower but not smaller, scaling up LLMs (more parameters, more data) can make hallucinations less frequent but not eliminate them. The 8.9% is baked into the mathematics.

### 2. The Overshoot Appears at Boundaries

Gibbs overshoot occurs at discontinuities. Similarly, LLM hallucinations are most pronounced at the boundaries of the model's knowledge—edge cases, rare facts, or novel combinations of concepts. The model is smoothest in well-trodden territory and most oscillatory at the frontiers.

### 3. Continuous Approximation Has Inherent Bias

The Fourier series doesn't just overshoot—it also exhibits ringing (oscillations) near the discontinuity. In LLMs, this manifests as the model's tendency to generate plausible-sounding but incorrect variations around true facts. The language is smooth, but the underlying structure is non-smooth, creating systematic bias.

## Implications for AI Safety and Alignment

If hallucination is a mathematical inevitability rather than merely an engineering challenge, our approach to AI safety must adapt:

- **Verification Over Generation**: We should focus on building robust verification systems rather than expecting perfect generation. Think of it as accepting the Gibbs overshoot but adding error-correcting mechanisms.

- **Hybrid Architectures**: Combining continuous neural networks with discrete symbolic reasoning systems might help. Use neural networks for pattern recognition and language generation, but defer to symbolic systems for logical inference and fact verification.

- **Uncertainty Quantification**: Since we can't eliminate hallucination, we must get better at detecting when the model is in a "high overshoot" region—near knowledge boundaries where hallucination is more likely.

- **Acceptance of Limitations**: Just as signal processing engineers accept and work around the Gibbs phenomenon, AI practitioners should acknowledge that some level of hallucination is inherent to the current paradigm.

## The Deeper Insight: Language is Smooth, Reality is Not

Perhaps the most profound insight from this analogy is the mismatch between the medium and the message. Language itself is inherently smooth—words flow into each other, meanings shade gradually, and context blends seamlessly. But the reality language describes often contains sharp edges: binary truths, discrete events, and logical absolutes.

LLMs are trained on language, which is smooth. They learn to generate smooth continuations. But when we ask them to represent non-smooth reality, we're asking continuous functions to approximate discontinuous ones. The Gibbs phenomenon is the mathematical price we pay for this mismatch.

## Conclusion: Living with the 8.9%

The Gibbs phenomenon has been known for over a century. Engineers in signal processing don't try to eliminate it—they understand it, work around it, and design systems that account for it. Perhaps it's time for the AI community to adopt a similar mindset regarding LLM hallucinations.

Hallucination isn't just a bug to be fixed with better training data or more parameters. It's a fundamental consequence of using continuous approximation methods to represent a world that contains discontinuities. That 8.9% overshoot—the mathematical ghost in the machine—will haunt us as long as we rely on neural networks as our primary tool for artificial intelligence.

The question isn't whether we can eliminate hallucination. The question is: how do we build systems that are robust despite its mathematical inevitability?

---

## References

1. [Gibbs Phenomenon - Wikipedia](https://en.wikipedia.org/wiki/Gibbs_phenomenon) (Content rephrased for compliance with licensing restrictions)
2. [Universal Approximation Theorem](https://en.wikipedia.org/wiki/Universal_approximation_theorem) (Content rephrased for compliance with licensing restrictions)
3. [Understanding Hallucinations in LLMs - ArXiv](https://arxiv.org/html/2502.08663v1)
4. [On the Fundamental Impossibility of Hallucination Control - ArXiv](https://arxiv.org/html/2506.06382)
5. [Fourier Series & Gibbs Phenomenon](https://iris.joshua-becker.com/lab/fourier-series-gibbs-phenomenon/)
