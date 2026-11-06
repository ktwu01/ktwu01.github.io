---
title: '怎么样让 LLM 变得更杰出？'
date: 2026-11-06
permalink: /zh/posts/2026/11/reasoning-with-limited-knowledge/
tags:
  - AI
  - Reasoning
  - Research
---

什么样的人是杰出的？我们怎么样才能造出杰出的东西？杰出的东西和平庸的东西有什么区别？

> 作者：[Koutian Wu](https://www.linkedin.com/in/ktwu01/)；[GitHub: ktwu01](https://github.com/ktwu01/)

从一开始，我一直在寻找卓越。我关心 taste，也就是分辨杰出与平庸的能力。这种判断力，在研究和其他领域里都重要。

这个问题放到 AI 上，就是：怎么样让 LLM 变得更杰出？我希望它能凭借有限的已有知识，推理出没有被直接教过的东西。面对陌生问题，它能形成判断、检验答案，并发现自己的错误。

我知道这很难，所以想看看已经有谁在做。这几个项目各自研究了其中一部分。

- **François Chollet 和 ARC Prize。** Chollet 在 [On the Measure of Intelligence](https://arxiv.org/abs/1911.01547) 中，主张衡量智能时要看获取新技能的效率，并考虑已有知识和经验的影响。ARC 测试模型能否从少量示例中学会解决新问题。[ARC Prize 2025 技术报告](https://arxiv.org/abs/2601.10904) 讨论了迭代改进、程序合成，以及没有经过大规模通用预训练的小网络。ARC 成绩反映特定的一组能力，更广泛的智能还需要其他证据。

- **Alexia Jolicoeur-Martineau：Tiny Recursive Model（TRM）。** [Less is More: Recursive Reasoning with Tiny Networks](https://arxiv.org/abs/2510.04871) 研究一个反复更新内部状态和候选答案的小网络。论文报告了一个 700 万参数模型在谜题任务上的表现。TRM 是专门用于推理任务的模型，这种方法能在多大程度上迁移到通用语言任务，仍有待研究。

- **DeepSeek-AI：R1-Zero。** [DeepSeek-R1](https://arxiv.org/abs/2501.12948) 探索用强化学习训练推理能力。R1-Zero 跳过了前置的监督微调阶段，在答案可检验的任务上通过奖励学习。它从一个已经预训练的基础模型开始，因此这些结果依赖已有的大量训练。

- **Google DeepMind：AlphaGeometry。** [AlphaGeometry](https://deepmind.google/blog/alphageometry-an-olympiad-level-ai-system-for-geometry/) 将学会提出候选方案的模型与符号演绎系统结合，并用合成几何数据训练。它在规则明确的数学领域展示了复杂推理能力，向其他领域迁移的能力还需要单独研究。

我想继续追问：面对陌生任务，一个模型能用多少的已有知识和计算，推导出多少东西？
