---
title: "Benchmark Radar 第五十九天：隐藏的重复与互相冲突的智能体"
date: 2026-09-23
permalink: /zh/posts/2026/09/benchmark-radar-day59/
tags:
  - AI
  - Benchmarks
  - Coding Agents
  - Chemistry
---

Benchmark Radar 的第五十九天。每日扫描发布 510 条记录，推荐 211 条。领头的是一项发现训练集与测试集之间隐藏重复的分子数据审计，以及一个检验编程智能体补丁合并后是否冲突的基准。记分牌：249 颗星，41 个 fork。

> 作者：[Koutian Wu](https://www.linkedin.com/in/ktwu01/)；[GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar 已上线。** 每天追踪新的 AI 基准测试、数据集与排行榜：[打开仪表盘](https://benchmark-radar.org/) 或 [在 GitHub 上 Star](https://github.com/ktwu01/benchmark-radar)。阅读论文：[arXiv:2609.11115](https://arxiv.org/abs/2609.11115)。查询数据：[Hugging Face 数据集](https://huggingface.co/datasets/ktwu01/benchmark-radar)。

本轮抓取 1,177 条，保留 510 条，推荐 211 条。

针对血脑屏障数据集 B3DB 的一项新审计指出：常用的二维分子格式会把不同的三维构型（立体异构体）映射成同一个输入。在划分时看似分开的分子，实际上可能是重复样本，从而抬高测试分数。审计在 7,807 条记录上比较了常规去重与考虑表示方式的整理方法。

《Trains but Doesn't Learn》提出一个十阶段基准，检验智能体在预算、人工审批和可复现要求下微调并交付模型的能力，专门针对训练损失下降、模型却没有变好的情况。

stale 基准先分别测试两个编程智能体的补丁，再测试合并后的结果，只统计由组合引起的失败。

为什么要在意

三者揭示的都是看起来没问题、实际有问题的分数：暗中与训练数据重叠的测试集，掩盖模型毫无进步的损失下降，各自通过却合在一起失败的两个补丁。发现这种差距，正是基准存在的意义。

解决的问题

- 每日快照：抓取 1,177，发布 510，推荐 211
- 采集状况：OpenReview、Semantic Scholar 与 Brave 报错，其余来源支撑了本轮运行
- 记分牌：249 / 1000 星，41 个 fork

第六十天：记分牌突破 250 颗星。

> 想跟进 Benchmark Radar？[在 GitHub 上 Star 仓库](https://github.com/ktwu01/benchmark-radar) 获取每日更新，或 [打开实时仪表盘](https://benchmark-radar.org/) 浏览扫描结果。阅读论文：[arXiv:2609.11115](https://arxiv.org/abs/2609.11115)。
