---
title: "Benchmark Radar 第六十七天：系统提示词里的日期会改变分数"
date: 2026-10-01
permalink: /zh/posts/2026/10/benchmark-radar-day67/
tags:
  - AI
  - Benchmarks
---

Benchmark Radar 的第六十七天。每日扫描发布 688 条记录，推荐 289 条，领头的是 《Dating the Model》：这项研究表明，一行隐藏的当前日期会改变测得的表现。记分牌：268 颗星，45 个 fork。

> 作者：[Koutian Wu](https://www.linkedin.com/in/ktwu01/)；[GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar 已上线。** 每天追踪新的 AI 基准测试、数据集与排行榜：[打开仪表盘](https://benchmark-radar.org/) 或 [在 GitHub 上 Star](https://github.com/ktwu01/benchmark-radar)。阅读论文：[arXiv:2609.11115](https://arxiv.org/abs/2609.11115)。查询数据：[Hugging Face 数据集](https://huggingface.co/datasets/ktwu01/benchmark-radar)。

本轮抓取 1,490 条，保留 688 条，推荐 289 条。

《Dating the Model》报告称，注入系统提示词的隐藏当前日期文本，使九个大语言模型在六个数据集上的测得表现发生变化，数学任务上的变化最高达 14%。模型排名也跟着变了，而用户提示词其余部分完全没动。

EngramBench 围绕“能力重叠、解法不重叠”设计：学习任务和测试任务需要相关的技能，但避免高度相似的解法。它包含 30 个学习任务和 13 个未见任务，用来区分可复用的技能积累与照抄先前的代码。

Argus 为计算机操作智能体的置信度估计建立基准，这类智能体把视觉语言模型的预测转成图形界面点击。它比较了四个开放权重智能体、四个数据集上的 27 种方法，以及三家闭源厂商上的 8 种方法。

为什么要在意

在不同日期、不同隐藏提示词下比较的两个模型，可能根本算不上被比较过。

解决的问题

- 每日快照：抓取 1,490，发布 688，推荐 289
- 记分牌：268 / 1000 星，45 个 fork

第六十八天：扫描继续，星数 268，fork 45 个。

> 想跟进 Benchmark Radar？[在 GitHub 上 Star 仓库](https://github.com/ktwu01/benchmark-radar) 获取每日更新，或 [打开实时仪表盘](https://benchmark-radar.org/) 浏览扫描结果。阅读论文：[arXiv:2609.11115](https://arxiv.org/abs/2609.11115)。
