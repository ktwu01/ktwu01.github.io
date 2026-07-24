---
title: 'Prompt Caching Is Not Technical Debt'
date: 2026-05-10
permalink: /posts/2026/05/prompt-caching-is-not-technical-debt/
tags:
  - LLM
  - prompt-caching
  - engineering
  - AI
---

Prompt Caching Is Not Technical Debt. It's what the math demands.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

---

There's a recurring complaint in AI developer circles: prompt caching feels like a hack. A band-aid over expensive token pricing. A temporary workaround that will eventually be "fixed" when models get cheaper to run.

This view is wrong. Not directionally wrong — completely wrong. Prompt caching isn't an engineering compromise. It's what the transformer architecture mathematically requires.

---

## What Actually Happens During Inference

When a transformer processes a sequence of tokens, the attention mechanism computes three matrices for each token at each layer: **Query (Q)**, **Key (K)**, and **Value (V)**. The attention output for position $$i$$ is:

$$\text{Attention}(Q_i, K, V) = \text{softmax}\left(\frac{Q_i K^T}{\sqrt{d_k}}\right) V$$

The critical observation: **K and V depend only on the input tokens, not on the query position being computed**. For a prompt of length $$N$$, generating $$M$$ new tokens requires computing the full KV matrices for all $$N$$ prompt tokens — once — and then reusing them for each of the $$M$$ decoding steps.

This is KV cache. Not a product decision. Not a cost optimization hack. The **mathematically correct way to implement autoregressive decoding**.

If you're not caching KV, you're recomputing the same matrix products on every forward pass. That's not "cleaner" — that's waste.

---

## Why "Technical Debt" Is the Wrong Frame

Technical debt means: *we made a short-term tradeoff that reduces future flexibility*. The classic form is cutting corners in architecture to ship faster, accumulating maintenance cost that compounds over time.

KV cache doesn't fit this definition on any axis:

**It doesn't reduce flexibility.** The cache is invalidated the moment the prefix changes. It doesn't constrain what prompts you can send, what models you can swap, or what system you can build on top.

**It doesn't accumulate.** There's no hidden complexity that grows with usage. A session with 1,000 cached tokens is architecturally identical to one with 100.

**It's not a workaround.** KV cache is implemented at the mathematical layer of attention — it emerges from how the operation is defined, not from engineering choices layered on top.

Saying prompt caching is technical debt is like saying that memoization in dynamic programming is technical debt. It's the algorithm. The insight *is* the algorithm.

---

## The Claim Implies a False Counterfactual

The implicit alternative being proposed is: *in a better world, tokens would be cheap enough that caching wouldn't matter*.

But even if inference cost dropped 100x, KV cache would still be the correct implementation. You'd use it because recomputing K and V matrices you already have is mathematically redundant — not because it's expensive. Cost is downstream of correctness.

If anything, the argument runs the other direction: as models get larger and context windows get longer (128K → 1M tokens), the value of caching grows. Recomputing KV across a million-token context window without caching isn't a future we're building toward — it's a computation that doesn't make sense.

---

## What Claude Code Is Actually Doing

Claude Code caches system prompts, tool definitions, and repository context across turns in a session. Each of these is a fixed prefix that doesn't change between user messages. Caching them is not a product optimization — it's applying the fundamental property that the K and V matrices for a fixed prefix are reusable.

The pricing reflects this (cache hits cost ~10% of fresh tokens on Claude's API). But the pricing is a consequence of the engineering reality, not the reason for the design.

---

## If You Want to Call Something Technical Debt

There are real technical debts in current LLM infrastructure:

- **Quadratic attention complexity** in standard transformers — this actually *is* being worked around with sparse attention, linear attention variants, and state space models.
- **Lack of persistent memory** across sessions — prompting-based memory systems are a genuine workaround for a missing architectural primitive.
- **Context window limits as a hard boundary** — prefill-and-extend strategies are genuinely temporary.

These are cases where the current implementation diverges from the ideal due to practical constraints. KV cache is not in this category. It's what you get when you implement the math correctly.

---

## Conclusion

The transformer architecture, as currently defined, makes KV cache the optimal computation strategy for autoregressive decoding. Prompt caching in products like Claude Code is a direct expression of this — not a workaround layered on top.

You could argue that transformers themselves are a temporary architecture. That's a legitimate claim. Attention is $$O(n^2)$$ in sequence length; something will eventually replace it for long-context tasks.

But that argument proves too much. If transformers are technical debt, then yes, everything built correctly on top of transformers inherits that framing. That's not a useful lens for evaluating engineering decisions *within* a transformer-based system.

For now: transformers are the substrate. KV cache is what the math demands. Prompt caching is the product-level expression of that fact.

Call it something else. Just not technical debt.

---

*Written in response to Lingtai WeChat group debate about Claude Code's caching behavior.*
