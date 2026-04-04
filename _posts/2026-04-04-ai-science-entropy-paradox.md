---
title: "The Entropy Paradox: Why AI Struggles with Scientific Discovery"
date: 2026-04-04
permalink: /posts/2026/04/ai-science-entropy-paradox/
tags:
  - AI
  - Science
  - Philosophy
  - AI4S
  - scientific-discovery
  - information-theory
  - tacit-knowledge
---

# The Entropy Paradox: Why AI Struggles with Scientific Discovery

## 熵悖论：为什么AI难以实现科学发现

---

### English Version

The promise of AI-automated science is intoxicating: imagine machines that can generate hypotheses, design experiments, and publish papers while we sleep. Yet despite the breathless headlines about "AI Scientists," we're hitting a fundamental wall. The problem isn't computational power or dataset size—it's something far more profound, rooted in the very nature of scientific discovery and information theory.

#### 1. The Priority System: Science as a Race for "First Discovery"

Science operates on a winner-takes-all priority system. The second person to discover relativity gets zero Nobel Prizes. This isn't arbitrary—it reflects the core economic and social structure of scientific progress. As [recent research on AI-assisted discovery](https://www.researchgate.net/publication/387382231_Artificial_Intelligence_Scientific_Discovery_and_Product_Innovation) shows, the value lies not in correctness alone, but in **non-consensus correctness**—being right about something nobody else has figured out yet.

This is where current large language models (LLMs) fundamentally fail. They excel at producing "mediocre correctness"—answers that are statistically likely, well-formed, and utterly uninteresting to the scientific community. If an AI can only output ideas that everyone could think of, it cannot help scientists "race for first." Science doesn't reward consensus; it rewards the edge cases, the counterintuitive leaps, the discoveries that lie just beyond the frontier of collective knowledge.

#### 2. The Information Entropy Bottleneck: Interpolation vs. Extrapolation

Here's the mathematical heart of the problem: LLMs are fundamentally **interpolation engines**. They fit probability distributions over existing human knowledge. Scientific discovery, by contrast, requires **extrapolation**—venturing into regions of hypothesis space with genuinely high information entropy (真正的新知识).

As [research on information efficiency in scientific automation](https://arxiv.org/html/2511.15671) demonstrates, scientific discovery can be framed as a thermodynamic process where agents invest work to acquire information under finite budgets. The challenge is that LLMs trained on past data distributions struggle with out-of-distribution (OOD) generalization—precisely what frontier science demands.

The current alignment paradigm makes this worse. Post-training techniques like RLHF align models to "human everyday preferences," not to "objective physical laws" or "scientific truth." Without grounding in real physical feedback loops, models hallucinate plausibly rather than discover genuinely.

**Key terminology clarification:**
- Not just "generalization" → **Out-of-Distribution (OOD) Generalization**
- Not just "training phases" → **Alignment to physical reality vs. human preference**
- Not just "missing context" → **Tacit knowledge** that never makes it into papers

#### 3. The Tacit Knowledge Gap: What Papers Don't Capture

Human scientists don't just read papers—they accumulate [tacit knowledge](http://journal.frontiersin.org/article/10.3389/fpsyg.2017.00656/full) through physical interaction with the world. As philosopher Michael Polanyi famously stated: "We can know more than we can tell."

This includes:
- Failed experiments that never get published (negative data)
- Laboratory intuitions and "feel" for when something is working
- Cross-disciplinary serendipity and unexpected connections
- Scientific "taste"—the ability to prune vast hypothesis spaces and jump directly to promising regions

LLMs trained on static text corpora miss all of this. They don't experience the frustration of a failed synthesis, the surprise of an unexpected result, or the subtle cues that tell an expert "this direction is worth exploring."

[Recent work on AI-enabled tacit knowledge co-evolution](https://www.mdpi.com/2673-9585/6/1/1) suggests positioning AI as an "epistemic partner" rather than a replacement—augmenting human interpretive processes rather than codifying experience.

#### 4. Designing Skills for Non-Mediocre Discovery

So what should we build? Not end-to-end "AI scientists" that generate mediocre papers. Instead, we need tools that operate at the **taste level**—augmenting rather than replacing human expertise.

**Practical design principles:**

1. **Navigation, not generation**: Build tools that help experts explore hypothesis spaces, identifying "high-potential, low-attention" blind spots rather than generating complete solutions.

2. **Interactive taste amplifiers**: Let experts input their unique insights or constraints, then have AI complete complex reasoning chains, cross-validate, or find analogous structures across disciplines.

3. **Private context integration**: Enable scientists to safely inject unpublished experimental data and intuitions that serve only their discovery process—helping them win the race for "first."

4. **Divergence vs. convergence**: Should AI primarily act as a **diverger** (providing cross-domain inspiration) or a **converger** (ruthlessly critiquing wild ideas with logic)? The answer: both, but at different stages of the discovery process.

The future of AI in science isn't about automation—it's about creating tools that amplify the irreplaceable human capacity for taste, intuition, and the courage to explore the non-obvious.

---

### 中文版本

AI自动化科研的愿景令人陶醉：想象机器能在我们睡觉时生成假设、设计实验、发表论文。然而，尽管关于"AI科学家"的新闻铺天盖地，我们正在撞上一堵根本性的墙。问题不在于算力或数据集规模——而是某种更深刻的东西，根植于科学发现的本质和信息论之中。

#### 1. 优先权系统：科学是一场"第一发现"的竞赛

科学实行的是赢者通吃的优先权系统。第二个发现相对论的人拿不到半个诺贝尔奖。这不是任意的——它反映了科学进步的核心经济和社会结构。正如[关于AI辅助发现的最新研究](https://www.researchgate.net/publication/387382231_Artificial_Intelligence_Scientific_Discovery_and_Product_Innovation)所示，价值不仅在于正确性，而在于**非共识的正确性**——在别人还没想到的事情上是对的。

这正是当前大语言模型（LLM）根本性失败的地方。它们擅长产生"平庸的正确"——统计上可能、格式良好、但对科学界毫无趣味的答案。如果AI只能输出每个人都能想到的想法，它就无法帮助科学家"抢占第一"。科学不奖励共识；它奖励边缘案例、反直觉的跳跃、那些恰好位于集体知识前沿之外的发现。

#### 2. 信息熵瓶颈：插值 vs. 外推

这是问题的数学核心：LLM本质上是**插值引擎**。它们拟合现有人类知识的概率分布。相比之下，科学发现需要**外推**——冒险进入具有真正高信息熵的假设空间区域。

正如[关于科学自动化信息效率的研究](https://arxiv.org/html/2511.15671)所示，科学发现可以被框定为一个热力学过程，其中智能体在有限预算下投入工作以获取信息。挑战在于，在过去数据分布上训练的LLM在分布外（OOD）泛化方面表现不佳——而这正是前沿科学所需要的。

当前的对齐范式使这个问题更加严重。像RLHF这样的后训练技术将模型对齐到"人类日常偏好"，而不是"客观物理规律"或"科学真理"。没有真实物理反馈循环的基础，模型会产生看似合理的幻觉，而不是真正的发现。

**关键术语澄清：**
- 不只是"泛化" → **分布外（OOD）泛化**
- 不只是"训练阶段" → **对齐到物理现实 vs. 人类偏好**
- 不只是"缺少上下文" → **隐性知识**，那些从未出现在论文中的知识

#### 3. 隐性知识鸿沟：论文无法捕捉的东西

人类科学家不只是阅读论文——他们通过与世界的物理交互积累[隐性知识](http://journal.frontiersin.org/article/10.3389/fpsyg.2017.00656/full)。正如哲学家迈克尔·波兰尼的名言："我们知道的比我们能说的更多。"

这包括：
- 从未发表的失败实验（负面数据）
- 实验室直觉和对"某事正在起作用"的"感觉"
- 跨学科的偶然性和意外联系
- 科学"品味"——修剪庞大假设空间并直接跳到有希望区域的能力

在静态文本语料库上训练的LLM错过了所有这些。它们没有经历过合成失败的挫折、意外结果的惊喜，或告诉专家"这个方向值得探索"的微妙线索。

[关于AI赋能的隐性知识共同进化的最新工作](https://www.mdpi.com/2673-9585/6/1/1)建议将AI定位为"认识论伙伴"而非替代品——增强人类的解释过程，而不是编码经验。

#### 4. 为非平庸发现设计技能

那么我们应该构建什么？不是生成平庸论文的端到端"AI科学家"。相反，我们需要在**品味层面**运作的工具——增强而非替代人类专业知识。

**实用设计原则：**

1. **导航，而非生成**：构建帮助专家探索假设空间的工具，识别"高潜力、低关注"的盲点，而不是生成完整的解决方案。

2. **交互式品味放大器**：让专家输入他们独特的洞察或约束，然后让AI完成复杂的推理链、交叉验证或跨学科寻找类似结构。

3. **私有上下文集成**：使科学家能够安全地注入未发表的实验数据和直觉，这些数据仅服务于他们的发现过程——帮助他们赢得"第一"的竞赛。

4. **发散 vs. 收敛**：AI应该主要充当**发散者**（提供跨领域灵感）还是**收敛者**（用逻辑无情地批评狂野想法）？答案是：两者都要，但在发现过程的不同阶段。

AI在科学中的未来不是关于自动化——而是关于创造工具，放大人类在品味、直觉和探索非显而易见事物的勇气方面不可替代的能力。

---

### References / 参考文献

Content synthesized and rephrased from:
- [Information Efficiency of Scientific Automation](https://arxiv.org/html/2511.15671) (arXiv)
- [On the Tacit Aspects of Science Pedagogy](http://journal.frontiersin.org/article/10.3389/fpsyg.2017.00656/full) (Frontiers)
- [AI-Enabled Tacit Knowledge Co-Evolution](https://www.mdpi.com/2673-9585/6/1/1) (MDPI)
- [Out-of-Distribution Generalization Survey](https://arxiv.org/html/2403.01874) (arXiv)
- [AI, Scientific Discovery, and Product Innovation](https://www.researchgate.net/publication/387382231_Artificial_Intelligence_Scientific_Discovery_and_Product_Innovation) (ResearchGate)

*Content was rephrased for compliance with licensing restrictions.*
