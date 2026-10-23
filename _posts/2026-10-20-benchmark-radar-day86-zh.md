---
title: "Benchmark Radar 第 86 天：客服智能体还要检查操作过程"
date: 2026-10-20
permalink: /zh/posts/2026/10/benchmark-radar-day86/
tags:
  - AI
  - Benchmarks
---

Benchmark Radar 第 86 天。客服智能体还要检查操作过程。本轮抓取 1,430 条，发布 755 条，其中 389 条标为推荐。

> 作者：[Koutian Wu](https://www.linkedin.com/in/ktwu01/)；[GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar 已上线。** [打开仪表盘](https://benchmark-radar.org/)、[在 GitHub 上 Star](https://github.com/ktwu01/benchmark-radar)，或阅读[论文](https://arxiv.org/abs/2609.11115)。数据见 [Hugging Face 数据集](https://huggingface.co/datasets/ktwu01/benchmark-radar)。

CXBench 在六个受监管领域，同时评估使用工具的客服智能体的结果和操作过程。规则卡把义务与可观察的轨迹证据对应起来，涵盖告知、同意和必要步骤。只达到预期业务状态，无法拿到满分。 [CXBench: A Benchmark for Process-Compliant LLM Agents in Regulated Customer-Experience Workflows](https://doi.org/10.48550/arxiv.2610.25954)。

VibeTraining-Bench 评估科研智能体能否在固定资源预算下改进完整智能体系统。智能体根据验证反馈，修改训练数据、训练器和推理框架，再选择最终系统。怎样在相互影响的组件之间分配资源，也成为测试的一部分。 [VibeTraining-Bench: Data-Trainer-Harness Co-Design for Iterative System Improvement](https://arxiv.org/abs/2610.26342)。

## 为什么要在意

实际工作受哪些约束，评估就应保留哪些约束。最终结果可能掩盖被跳过的义务，也可能掩盖资源消耗过大的改进。

## 扫描范围

这是按关键词筛选的发现信息流，不能代表全部 AI 研究。归档简报使用了所收录 755 条证据中的 177 条。本文概述其中引用的发布成果；扫描发现日期不一定是成果的最初发布日期。

数据与简报：[2026-10-20 归档快照](https://github.com/ktwu01/benchmark-radar/blob/2f75b7a07c6f233bcbcb461631befc2b118be584/data/snapshots/2026-10-20.json)。
