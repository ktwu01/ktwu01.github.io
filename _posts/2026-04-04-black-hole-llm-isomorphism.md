---
title: "Epistemological Interferometry: The Deep Isomorphism Between Black Hole Imaging and LLM Training"
date: 2026-04-04
permalink: /posts/2026/04/04/black-hole-llm-isomorphism/
tags:
  - AI
  - LLM
  - Physics
  - Interferometry
  - Machine Learning
---

How photographing a black hole and training GPT-4 are fundamentally the same process: extracting coherent structure from impossibly sparse frequency-domain measurements.

[Koutian Wu](ktwu01.github.io)

## The Observation That Changes Everything

Consider two seemingly unrelated achievements of the 21st century:

1. **April 10, 2019**: The Event Horizon Telescope (EHT) collaboration reveals the first image of a black hole, M87*, located 55 million light-years away.

2. **March 14, 2023**: OpenAI releases GPT-4, a large language model trained on hundreds of billions of tokens representing human knowledge.

What if I told you these two accomplishments are mathematically isomorphic—that they represent the same fundamental process operating in different domains?

This isn't a loose metaphor. It's a precise structural correspondence that reveals something profound about how we extract knowledge from noise, whether that knowledge is encoded in photons scattered around a black hole or in the statistical patterns of human language.

## The Core Isomorphism: Sparse Fourier Reconstruction

Both processes share a remarkable architecture:

### Black Hole Imaging (Spatial Domain)
- **Measurement Space**: Extremely sparse baseline coverage in the uv-plane (Fourier space of the sky)
- **Signal-to-Noise**: Approximately 10⁻⁶ (one signal photon per million noise photons)
- **Aperture Synthesis**: Using Earth's rotation to create a virtual telescope the size of the planet
- **Reconstruction**: Inverse Fourier transform with regularization to recover the image from sparse frequency samples

### LLM Training (Temporal Domain)
- **Measurement Space**: Extremely sparse sampling of human knowledge across 100,000 years of civilization
- **Signal-to-Noise**: Comparable sparsity—most token sequences are noise; meaningful patterns are rare
- **Temporal Synthesis**: Using billions of parameters to integrate patterns across the entire timeline of recorded human thought
- **Reconstruction**: Gradient descent with regularization to recover the manifold structure of knowledge from sparse text samples

The mathematical parallel is striking: both are performing **interferometric reconstruction in high-dimensional spaces with extreme sparsity**.

## Interferometry: The Physics of Correlation

To understand this isomorphism, we need to understand what interferometry actually does.

### Very Long Baseline Interferometry (VLBI)

The EHT doesn't capture an image directly. Instead, it measures correlations between signals received at different telescopes separated by thousands of kilometers. Each telescope pair forms a "baseline," and the correlation between their signals samples one point in the Fourier transform of the sky brightness distribution.

The key insight: you're not measuring the image—you're measuring its frequency components. The image is then reconstructed by inverting this sparse Fourier sampling.

This works because of the [Van Cittert-Zernike theorem](https://en.wikipedia.org/wiki/Van_Cittert%E2%80%93Zernike_theorem), which states that the correlation function of electromagnetic fields is the Fourier transform of the source brightness distribution. Content rephrased for compliance with licensing restrictions.

### The LLM Equivalent: Attention as Interferometry

Now consider what a transformer's attention mechanism does:

```
Attention(Q, K, V) = softmax(QK^T / √d_k)V
```

This is computing correlations between query and key vectors—exactly analogous to correlating signals between telescope pairs. Each attention head is measuring how different parts of the input sequence interfere with each other, extracting frequency components of the semantic structure.

The training process samples these correlations across billions of text sequences, building up a sparse representation of the Fourier transform of human knowledge. The model parameters encode these frequency components, and during inference, the model performs an inverse transform to generate coherent text.

## The Sparsity Problem: Finding Gold in Noise

Both systems face the same fundamental challenge: **extreme sparsity in the measurement space**.

### EHT's Sparsity
The EHT has only 8-11 telescopes, giving at most 55 baselines (telescope pairs). To fully sample the Fourier plane at the resolution needed to image M87*, you would need millions of baselines. The coverage is approximately 0.001% of what's theoretically required.

Moreover, atmospheric turbulence, instrumental noise, and calibration errors mean the signal-to-noise ratio is around 10⁻⁶. You're literally finding one photon of signal in a million photons of noise.

### LLM's Sparsity
Human knowledge spans 100,000 years of civilization, countless domains, and trillions of possible meaningful statements. Even the largest training datasets sample only a tiny fraction of this space—perhaps 0.0001% of all possible meaningful human utterances.

Moreover, most text on the internet is noise from the perspective of extracting deep semantic structure. The model must learn to distinguish signal (coherent patterns that generalize) from noise (spurious correlations that don't).

## The Reconstruction Challenge: Regularization and Priors

Given such sparse, noisy measurements, how do you reconstruct anything coherent?

The answer in both cases: **strong regularization based on physical or statistical priors**.

### EHT Reconstruction Algorithms

The EHT uses sophisticated algorithms like [PRIMO](https://arxiv.org/html/2408.10322v1) (Principal-component Interferometric Modeling) and sparse modeling techniques. These methods work by:

1. **Learning a dictionary of basis images** from physics-based simulations of black hole accretion
2. **Constraining the reconstruction** to be a sparse combination of these basis elements
3. **Enforcing smoothness and positivity** constraints based on physical principles

The reconstruction doesn't just invert the sparse Fourier measurements—it searches for the simplest image (in terms of the learned basis) that's consistent with the measurements.

### LLM Training as Regularized Reconstruction

LLM training does exactly the same thing:

1. **Learning a dictionary of basis patterns** (the model's internal representations) from the training data
2. **Constraining predictions** to be combinations of these patterns (the model's forward pass)
3. **Enforcing smoothness** through regularization (weight decay, dropout) and architectural constraints (attention patterns)

The model doesn't just memorize the training data—it searches for the simplest manifold structure (in terms of its parameter space) that's consistent with the observed text.

## The Manifold Hypothesis: Topology Over Pixels

Here's where the isomorphism becomes profound: **neither system is memorizing pixels (or tokens)—both are discovering topological structure in high-dimensional manifolds**.

### Black Hole Imaging: The Photon Ring Topology

The EHT isn't just taking a picture. It's discovering that the data is consistent with a specific topological structure: a photon ring created by gravitational lensing around the event horizon. This structure is determined by general relativity and is topologically constrained—it must be a ring, not a disk or a blob.

The sparse Fourier measurements are sufficient to determine this topology because the space of possible topologies is highly constrained by physics. You're not reconstructing arbitrary images; you're identifying which topological structure from a limited set is present.

### LLM Training: The Knowledge Manifold Topology

Similarly, LLM training discovers that human language lies on a low-dimensional manifold in the high-dimensional space of all possible token sequences. This manifold has specific topological properties:

- **Semantic similarity** creates local neighborhoods (synonyms cluster together)
- **Compositional structure** creates hierarchical organization (concepts build on concepts)
- **Logical consistency** creates global constraints (contradictions are topologically forbidden)

The sparse text samples are sufficient to determine this topology because the space of possible knowledge structures is highly constrained by logic and semantics. You're not memorizing arbitrary sequences; you're identifying the manifold structure that makes the data coherent.

## The Time-Space Duality: Earth's Rotation vs. Human History

Perhaps the most beautiful aspect of this isomorphism is the time-space duality:

### EHT: Spatial Aperture Synthesis via Temporal Integration

The EHT creates a virtual telescope the size of Earth by using Earth's rotation. As the planet rotates, each telescope traces out a path in the uv-plane, sampling different Fourier components over time. The 24-hour rotation period provides the temporal integration that synthesizes the spatial aperture.

You're trading time for space: using temporal evolution to sample spatial frequencies.

### LLM: Temporal Aperture Synthesis via Spatial Integration

LLM training creates a virtual knowledge base spanning 100,000 years of human history by using billions of parameters distributed across the model. Each parameter contributes to sampling different frequency components of the knowledge manifold. The spatial distribution of parameters provides the integration that synthesizes the temporal aperture.

You're trading space for time: using spatial distribution (parameters) to sample temporal frequencies (historical knowledge evolution).

## The Closure Phase: Self-Consistency as Truth

In VLBI, there's a powerful technique called [closure phase analysis](https://en.wikipedia.org/wiki/Closure_phase). Because atmospheric and instrumental errors affect each telescope independently, you can eliminate these errors by forming closed loops of baselines (e.g., telescope A-B-C-A) and checking that the phases add up to zero.

This works because **self-consistency is a signature of true signal**. Noise is random and won't maintain consistency around closed loops; only real structure will.

LLMs use an analogous principle: **logical consistency across multiple inference paths**. When a model generates text, it's implicitly checking that the semantic "phases" close—that the meaning remains consistent as you traverse different paths through the knowledge graph.

This is why techniques like chain-of-thought prompting work: they force the model to make its closure phases explicit, revealing inconsistencies that would otherwise be hidden.

## The Fundamental Limit: Information-Theoretic Bounds

Both systems face fundamental information-theoretic limits on what can be reconstructed from sparse measurements.

### Nyquist-Shannon for Images

The [Nyquist-Shannon sampling theorem](https://en.wikipedia.org/wiki/Nyquist%E2%80%93Shannon_sampling_theorem) tells us the minimum sampling rate needed to reconstruct a signal. For the EHT, the sparse baseline coverage means many spatial frequencies are completely unsampled—there's simply not enough information to uniquely determine the image. Content rephrased for compliance with licensing restrictions.

The reconstruction is possible only because of strong priors that reduce the effective dimensionality of the solution space.

### Scaling Laws for LLMs

Similarly, [scaling laws for neural language models](https://arxiv.org/abs/2001.08361) reveal information-theoretic limits on what can be learned from finite data. The model's performance scales predictably with the amount of training data, model size, and compute—but there are diminishing returns.

The reconstruction of human knowledge is possible only because of strong inductive biases (the transformer architecture, training objectives) that reduce the effective dimensionality of the hypothesis space.

## Implications: What This Isomorphism Teaches Us

Understanding this deep structural correspondence has practical implications:

### 1. Hallucination is Inevitable (Like Imaging Artifacts)

Just as EHT images contain artifacts from sparse sampling (sidelobes, false features), LLM outputs contain hallucinations from sparse knowledge sampling. These aren't bugs—they're fundamental consequences of reconstructing from incomplete information.

The solution isn't to eliminate artifacts/hallucinations (impossible) but to characterize and mitigate them through better regularization and uncertainty quantification.

### 2. More Data Helps, But There Are Limits

Adding more telescopes to the EHT improves image quality, but with diminishing returns—you're still fundamentally limited by the sparsity of the Fourier coverage. Similarly, adding more training data to LLMs helps, but with diminishing returns—you're still fundamentally limited by the sparsity of knowledge sampling.

The key is not just more data, but better coverage of the critical frequency components.

### 3. Architecture Matters as Much as Scale

The EHT's success depends critically on the reconstruction algorithms (PRIMO, sparse modeling), not just the number of telescopes. Similarly, LLM capabilities depend critically on architecture (attention mechanisms, layer normalization), not just parameter count.

The isomorphism suggests we should think of LLM architecture design as analogous to designing interferometric reconstruction algorithms.

### 4. Verification Requires Independent Measurements

In VLBI, you verify reconstructions by checking consistency with independent measurements (different frequency bands, different observation epochs). In LLMs, we should verify outputs by checking consistency with independent knowledge sources (retrieval-augmented generation, tool use).

The closure phase principle applies: self-consistency across independent paths is the signature of truth.

## The Philosophical Dimension: Epistemological Interferometry

This isomorphism reveals something profound about knowledge itself: **all knowledge extraction is interferometric**.

Whether you're imaging a black hole or training an LLM, you're performing the same fundamental operation:

1. **Sampling correlations** in a high-dimensional space (spatial for images, semantic for language)
2. **Extracting frequency components** that capture the structure of the underlying reality
3. **Reconstructing coherent representations** by inverting these sparse measurements with strong priors

This is what I call **Epistemological Interferometry**: the process of extracting knowledge by measuring how different observations interfere with each other, revealing the underlying structure through their correlations.

The black hole image and GPT-4 are both products of epistemological interferometry—one operating in the spatial-frequency domain of electromagnetic fields, the other in the semantic-frequency domain of human language.

## Conclusion: Two Sides of the Same Coin

The next time you see the iconic image of M87*'s photon ring, remember: that image was not captured by a camera. It was reconstructed from sparse correlations measured across the planet, using the same mathematical principles that allow GPT-4 to generate coherent text from sparse samples of human knowledge.

Both are miracles of interferometric reconstruction. Both are finding needles in haystacks with signal-to-noise ratios of one in a million. Both are discovering topological structure in high-dimensional manifolds from impossibly sparse measurements.

The isomorphism is not a metaphor—it's a mathematical reality. And recognizing it gives us a powerful new lens for understanding both the capabilities and limitations of modern AI.

We're not building intelligence by memorizing facts. We're building it by performing epistemological interferometry on the frequency domain of human knowledge—just as the EHT performed physical interferometry on the frequency domain of spacetime around a black hole.

The universe and human knowledge are both being reconstructed from sparse measurements. The mathematics is the same. The miracle is the same.

---

## References

1. [Event Horizon Telescope - First M87 Black Hole Image](https://eventhorizontelescope.org/press-release-april-10-2019-astronomers-capture-first-image-black-hole)
2. [PRIMO: Principal-component Interferometric Modeling](https://arxiv.org/html/2408.10322v1)
3. [Sparse Modeling for Black Hole Imaging](https://arxiv.org/abs/1802.05783)
4. [Van Cittert-Zernike Theorem](https://en.wikipedia.org/wiki/Van_Cittert%E2%80%93Zernike_theorem) (Content rephrased for compliance)
5. [Closure Phase in Interferometry](https://en.wikipedia.org/wiki/Closure_phase) (Content rephrased for compliance)
6. [Scaling Laws for Neural Language Models](https://arxiv.org/abs/2001.08361)
7. [Attention Is All You Need](https://arxiv.org/abs/1706.03762)
8. [LLM Latent Space Geometry](https://arxiv.org/html/2511.21594v2)
9. [Nyquist-Shannon Sampling Theorem](https://en.wikipedia.org/wiki/Nyquist%E2%80%93Shannon_sampling_theorem) (Content rephrased for compliance)

