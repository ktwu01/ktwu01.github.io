---
title: "Benchmark Radar 第六十四天：金融智能体，以及泄漏的群组标签"
date: 2026-09-28
permalink: /zh/posts/2026/09/benchmark-radar-day64/
tags:
  - AI
  - Benchmarks
---

Benchmark Radar 的第六十四天。每日扫描发布 505 条记录，推荐 233 条，领头的是 Finance Agents Benchmark：它把金融尽职调查做成端到端的智能体测试。记分牌：264 颗星，42 个 fork。

> 作者：[Koutian Wu](https://www.linkedin.com/in/ktwu01/)；[GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar 已上线。** 每天追踪新的 AI 基准测试、数据集与排行榜：[打开仪表盘](https://benchmark-radar.org/) 或 [在 GitHub 上 Star](https://github.com/ktwu01/benchmark-radar)。阅读论文：[arXiv:2609.11115](https://arxiv.org/abs/2609.11115)。查询数据：[Hugging Face 数据集](https://huggingface.co/datasets/ktwu01/benchmark-radar)。

本轮抓取 1,266 条，保留 505 条，推荐 233 条。

Finance Agents Benchmark 把金融尽职调查做成 50 个任务、160 份文档、231 条评分标准、一套执行框架，以及一个共享的合成公司数据室。配套发布的 600 次完整运行带有轨迹、答案、逐条标准的判定和裁判解释。

一项针对两阶段推荐系统的研究发现，固定候选集评估（让每个排序模型拿到相同的召回结果）在十个基准实例中有八个选出了与端到端评估不同的最优流水线。端到端评估让每个排序器处理自己召回阶段产出的候选。

一项新的审计报告了三个临时群组推荐基准中的跨交互泄漏。被留出的群组与物品标签，早已出现在每个对应成员的个人交互历史里，最多占个人交互的 23.4%。

为什么要在意

如果评估给每个模型相同的候选，选出的赢家可能和实际上线的系统不是同一个。

解决的问题

- 每日快照：抓取 1,266，发布 505，推荐 233
- 记分牌：264 / 1000 星，42 个 fork

第六十五天：扫描继续，星数 264，fork 42 个。

> 想跟进 Benchmark Radar？[在 GitHub 上 Star 仓库](https://github.com/ktwu01/benchmark-radar) 获取每日更新，或 [打开实时仪表盘](https://benchmark-radar.org/) 浏览扫描结果。阅读论文：[arXiv:2609.11115](https://arxiv.org/abs/2609.11115)。
