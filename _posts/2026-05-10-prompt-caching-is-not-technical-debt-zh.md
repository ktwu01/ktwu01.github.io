---
title: 'Prompt Caching 不是技术债'
date: 2026-05-10
permalink: /zh/posts/2026/05/prompt-caching-is-not-technical-debt/
tags:
  - LLM
  - prompt-caching
  - engineering
  - AI
---

很多人把 prompt caching 看成一个省钱 hack，但我觉得这个判断刚好反了。

> 作者：[Koutian Wu](https://www.linkedin.com/in/ktwu01/)；[GitHub: ktwu01](https://github.com/ktwu01/)

最近在一些 AI 开发者讨论里，经常会看到一个说法，prompt caching 听起来像是一个临时补丁。像是在 token 价格太贵的时候，产品和工程团队搞出来的一个 band-aid。等模型推理成本降下来，这玩意自然就不重要了。

我觉得这个看法不对。

不是方向上有点偏，而是整个 framing 就错了。Prompt caching 不是工程上的妥协，它更接近 transformer 架构在数学上要求你这么做。

先回到推理过程本身。

Transformer 在处理一串 token 的时候，attention 机制会在每一层为每个 token 计算三组东西，Query，也就是 Q，Key，也就是 K，Value，也就是 V。对位置 $$i$$ 来说，attention 输出大概长这样。

$$\text{Attention}(Q_i, K, V) = \text{softmax}\left(\frac{Q_i K^T}{\sqrt{d_k}}\right) V$$

这里最关键的一点是，K 和 V 只依赖输入 token 本身，不依赖当前正在计算哪个 query 位置。

所以，如果一个 prompt 长度是 $$N$$，你要继续生成 $$M$$ 个新 token，那么那段 prompt 对应的 KV 矩阵只需要算一次。后面每一步 decode，都可以复用这批 K 和 V。

这就是 KV cache。

它不是一个产品决策，不是一个成本优化小技巧，也不是一个为了便宜才加上的缓存层。它是 autoregressive decoding 里数学上正确的实现方式。

你如果不缓存 KV，就等于每次 forward pass 都重新算一遍已经算过的矩阵乘法。

这不叫干净。

这叫浪费。

回到技术债这个词。

技术债通常指的是，我们为了短期交付，做了一个会损害长期灵活性的 tradeoff。比如架构先凑合，接口先糊上，测试先欠着，之后维护成本会慢慢复利。

KV cache 不符合这个定义。

它不会降低系统灵活性。prefix 一变，cache 就失效。它不会限制你发什么 prompt，不会限制你换什么模型，也不会限制你在上面搭什么产品。

它也不会随着使用慢慢累积成一个怪物。一个有 1,000 个 cached tokens 的 session，和一个有 100 个 cached tokens 的 session，在架构上没有本质差别。

更重要的是，它不是 workaround。KV cache 是从 attention 的定义里长出来的，不是工程师在数学之外又硬套了一层东西。

说 prompt caching 是技术债，有点像说动态规划里的 memoization 是技术债。

不是。

那就是算法本身。

很多时候，大家隐含的想象是，未来 token 足够便宜了，caching 就不重要了。

但就算推理成本下降 100 倍，KV cache 仍然是正确做法。你会用它，不是因为贵，而是因为重新计算已经拿到的 K 和 V 在数学上就是冗余。成本只是这个冗余的外在表现，不是问题的根。

甚至可以反过来讲，模型越大，context window 越长，caching 的价值越高。

当上下文从 128K 走到 1M tokens，你还想着每一轮都把完整 KV 重新算一遍，那不是一个更理想的未来。

那是一个不太讲道理的计算。

Claude Code 这块其实也一样。

Claude Code 会在一个 session 里缓存 system prompt、tool definitions、repo context。这些东西在多轮对话里通常就是固定 prefix。固定 prefix 的 K 和 V 可以复用，所以就应该复用。

Claude API 的价格也反映了这点，cache hit 大概是 fresh tokens 的 10% 左右。但这个价格不是设计的原因，而是工程现实的结果。

如果真要找技术债，LLM 基础设施里当然有一堆。

标准 transformer 的 quadratic attention complexity 是一个真实问题，所以大家才会研究 sparse attention、linear attention、state space models。

跨 session 的 persistent memory 还很不成熟，所以现在很多 prompting-based memory system 确实有 workaround 的味道。

Context window 仍然是硬边界，所以 prefill-and-extend 这类策略也可能只是阶段性办法。

这些问题的共同点是，当前实现和理想形态之间确实有 gap，大家在用工程办法绕过去。

但 KV cache 不属于这一类。

它不是绕过数学。

它是把数学实现对了。

当然，你可以说 transformer 本身只是一个阶段性架构。这个观点是成立的。Attention 对 sequence length 是 $$O(n^2)$$，长上下文任务迟早会逼出新的架构。

但这个论证一下子说太大了。

如果 transformer 本身都是技术债，那所有正确构建在 transformer 之上的东西，都可以被你一并叫做技术债。这个说法不是完全没道理，但它对判断具体工程决策没什么帮助。

至少在今天，transformer 还是我们正在使用的 substrate。

KV cache 是这个 substrate 里数学要求你做的事。

Prompt caching 是这个事实在产品层面的表达。

你可以叫它优化，可以叫它正确实现，可以叫它 inference economics。

但别叫它技术债。

---

*写于 Lingtai 微信群关于 Claude Code caching 行为的一次讨论之后。*
