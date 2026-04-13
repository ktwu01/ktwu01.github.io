---
title: "熵悖论：为什么AI难以实现科学发现"
date: 2026-04-04
permalink: /posts/2026/04/ai-science-entropy-paradox-cn/
tags:
  - AI
  - Science
  - Philosophy
  - AI4S
  - scientific-discovery
  - information-theory
  - tacit-knowledge
---
AI 自动化科研的愿景令人陶醉：想象机器能在我们睡觉时生成假设、设计实验、发表论文。然而，尽管关于“AI 科学家”的新闻铺天盖地，我们正在撞上一堵根本性的墙。问题不在于算力或数据集规模，而是某种更深刻的东西，根植于科学发现的本质和信息论之中。

> 作者：[Koutian Wu](https://www.linkedin.com/in/ktwu01/)；[GitHub: ktwu01](https://github.com/ktwu01/)

## 优先权系统：科学是一场“第一发现”的竞赛

科学实行的是赢者通吃的优先权系统。第二个发现相对论的人拿不到半个诺贝尔奖。正如关于 AI 辅助发现的最新研究所示，价值不仅在于正确性，而在于**非共识的正确性**——在别人还没想到的事情上是对的。这正是当前大语言模型（LLM）根本性失败的地方：它们擅长产生“平庸的正确”，即统计上可能、格式良好但在科学界毫无趣味的答案。科学奖励的是边缘案例和反直觉的跳跃，而非平庸的共识。

## 信息熵瓶颈：插值 vs. 外推

从数学角度看，LLM 本质上是插值引擎，致力于拟合现有人类知识的概率分布。相比之下，科学发现需要外推，即冒险进入具有真正高信息熵的假设空间。当前针对人类日常偏好的优化范式（如 RLHF）使得这个问题更加严重，因为模型会为了迎合偏好而产生看似合理的幻觉，而非基于客观物理规律的真实发现。我们需要实现的是真正的分布外（OOD）泛化，而非简单的概率拟合。

## 隐性知识鸿沟：论文无法捕捉的东西

人类科学家不只是阅读论文，他们还通过与世界的物理交互积累隐性知识。正如哲学家迈克尔·波兰尼的名言：“我们知道的比我们能说的更多。”这包括从不发表的失败实验数据、实验室直觉，以及跨学科的偶然联系。在文本语料库上训练的 LLM 错过了这些关键的维度。它们没有经历过合成失败的挫折，也无法捕捉到专家眼中那些暗示“这个方向值得探索”的微妙线索。

## 为非平庸发现设计工具

未来的方向不在于构建生成平庸论文的端到端“AI 科学家”，而在于开发能在品味层面运作的工具。有效的设计应侧重于导航而非生成，帮助专家识别假设空间中的高潜力盲点。我们需要交互式品味放大器，让科学家能够注入独特的见解，并利用 AI 完成复杂的推理链验证。这种私有上下文的集成将帮助科学家在追求“第一发现”的竞赛中保持优势。

AI 在科学中的未来不是关于自动化，而是关于创造能够放大人类品味、直觉和勇敢探索精神的工具。

---

### 参考文献

内容综合自以下研究：
- [Information Efficiency of Scientific Automation](https://arxiv.org/html/2511.15671) (arXiv)
- [On the Tacit Aspects of Science Pedagogy](http://journal.frontiersin.org/article/10.3389/fpsyg.2017.00656/full) (Frontiers)
- [AI-Enabled Tacit Knowledge Co-Evolution](https://www.mdpi.com/2673-9585/6/1/1) (MDPI)
- [Out-of-Distribution Generalization Survey](https://arxiv.org/html/2403.01874) (arXiv)
- [AI, Scientific Discovery, and Product Innovation](https://www.researchgate.net/publication/387382231_Artificial_Intelligence_Scientific_Discovery_and_Product_Innovation) (ResearchGate)
