---
title: "Benchmark Radar 第 75 天：分数变了，先查评分器"
date: 2026-10-09
permalink: /zh/posts/2026/10/benchmark-radar-day75/
tags:
  - AI
  - Benchmarks
---

Benchmark Radar 第 75 天。分数变了，先查评分器。本轮抓取 1,338 条，发布 616 条，其中 281 条标为推荐。

> 作者：[Koutian Wu](https://www.linkedin.com/in/ktwu01/)；[GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar 已上线。** [打开仪表盘](https://benchmark-radar.org/)、[在 GitHub 上 Star](https://github.com/ktwu01/benchmark-radar)，或阅读[论文](https://arxiv.org/abs/2609.11115)。数据见 [Hugging Face 数据集](https://huggingface.co/datasets/ktwu01/benchmark-radar)。

TRACE 通过配对运行和重新评分相同轨迹，检查评估器是否稳定。在它的受控测试中，仅重命名工具就使脚本智能体得分下降，实际操作却完全相同。因此，分数下降时，应先检查评估器，再判断智能体能力是否退步。 [TRACE: Diagnosing Verifier Brittleness in Agentic Evaluation](https://arxiv.org/abs/2610.11678)。

一项表格数据澄清基准把提问策略与最终解答分开评估，也追踪模拟用户泄漏信息的问题：模拟用户可能提供真实用户不会给出的信息。模拟器过于配合，会让助手消除歧义的能力显得过强。 [Conversational Task Disambiguation over Tabular Data: Leakage-Aware Formulation, Benchmark Suite, and Training](https://arxiv.org/abs/2610.10740)。

## 为什么要在意

把高分解释为行为改善之前，先检查评分器和模拟用户。智能体没变，测量过程也可能让分数改变。

## 扫描范围

这是按关键词筛选的发现信息流，不能代表全部 AI 研究。归档简报使用了所收录 616 条证据中的 163 条。本文概述其中引用的发布成果；扫描发现日期不一定是成果的最初发布日期。

数据与简报：[2026-10-09 归档快照](https://github.com/ktwu01/benchmark-radar/blob/2f75b7a07c6f233bcbcb461631befc2b118be584/data/snapshots/2026-10-09.json)。
