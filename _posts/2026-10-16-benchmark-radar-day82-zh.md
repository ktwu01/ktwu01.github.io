---
title: "Benchmark Radar 第 82 天：输出得分无法证明运行时完整"
date: 2026-10-16
permalink: /zh/posts/2026/10/benchmark-radar-day82/
tags:
  - AI
  - Benchmarks
---

Benchmark Radar 第 82 天。输出得分无法证明运行时完整。本轮抓取 1,672 条，发布 846 条，其中 346 条标为推荐。

> 作者：[Koutian Wu](https://www.linkedin.com/in/ktwu01/)；[GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar 已上线。** [打开仪表盘](https://benchmark-radar.org/)、[在 GitHub 上 Star](https://github.com/ktwu01/benchmark-radar)，或阅读[论文](https://arxiv.org/abs/2609.11115)。数据见 [Hugging Face 数据集](https://huggingface.co/datasets/ktwu01/benchmark-radar)。

DIB-Bench 测试评判器能否发现遭到篡改、却仍能生成预期输出的部署运行时。来源报告称，在 7,560 个样例和六类篡改中，规则评判器和模型评判器接受了 88.6% 至 94.1% 的篡改输出。这是特定实验设置下的报告结果，不能直接推广到所有部署。 [Stronger Judges Do Not See More: Deployment-Integrity Blindness in LLM Evaluation](https://arxiv.org/abs/2610.21135)。

VELD-QA 把长篇视觉文档中的证据查找与证据理解分开评估。它包含 15,000 个人工编写的问答对，覆盖 5,859 份 PDF，并标注支持页面和视觉元素。答错时，可以进一步检查是找错页面，还是误读了找到的证据。 [VELD-QA: A Large-Scale Dataset for Visual Evidence Grounding and Question Answering in Long Documents](https://arxiv.org/abs/2610.20964)。

## 为什么要在意

评估要测到决策关心的环节。输出正确不足以确认实际运行的技术栈，文档问答准确率也无法定位每次检索失败。

## 扫描范围

这是按关键词筛选的发现信息流，不能代表全部 AI 研究。归档简报使用了所收录 846 条证据中的 185 条。本文概述其中引用的发布成果；扫描发现日期不一定是成果的最初发布日期。

数据与简报：[2026-10-16 归档快照](https://github.com/ktwu01/benchmark-radar/blob/2f75b7a07c6f233bcbcb461631befc2b118be584/data/snapshots/2026-10-16.json)。
