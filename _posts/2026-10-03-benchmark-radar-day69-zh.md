---
title: "Benchmark Radar 第六十九天：公开逐条预测，而不只是分数"
date: 2026-10-03
permalink: /zh/posts/2026/10/benchmark-radar-day69/
tags:
  - AI
  - Benchmarks
---

Benchmark Radar 的第六十九天。每日扫描发布 577 条记录，推荐 174 条，领头的是 一项更新后的视网膜基准审计：它公开逐图像的清单和逐图像的预测。记分牌：275 颗星，45 个 fork。

> 作者：[Koutian Wu](https://www.linkedin.com/in/ktwu01/)；[GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar 已上线。** 每天追踪新的 AI 基准测试、数据集与排行榜：[打开仪表盘](https://benchmark-radar.org/) 或 [在 GitHub 上 Star](https://github.com/ktwu01/benchmark-radar)。阅读论文：[arXiv:2609.11115](https://arxiv.org/abs/2609.11115)。查询数据：[Hugging Face 数据集](https://huggingface.co/datasets/ktwu01/benchmark-radar)。

本轮抓取 1,318 条，保留 577 条，推荐 174 条。

更新后的视网膜基准审计提供按患者分组、按来源匹配、以及留出一个来源的三种评估的逐图像清单，另有逐图像的预测，并对 335 个可能的跨标签重复做了裁定。

Jeff/Gemma4 多模态包在冻结的设计下评估六个完整检查点。它公开逐条样本的预测、置信度与校准度量、GPU 延迟与显存，以及量化降低数值精度之后的配对漂移。

基于变换的对象约束语言基准，通过确定性且保持语义的操作改变模型表示，例如标识符重命名和关联具体化。它检验的是：所求约束的含义不变时，表现能否经得起表示方式的改变。

为什么要在意

每个样本都有公开的预测，读者就能自己重算那个标题数字，并查看它背后的具体案例。

解决的问题

- 每日快照：抓取 1,318，发布 577，推荐 174
- 记分牌：275 / 1000 星，45 个 fork

第七十天：扫描继续，星数来到 275。

> 想跟进 Benchmark Radar？[在 GitHub 上 Star 仓库](https://github.com/ktwu01/benchmark-radar) 获取每日更新，或 [打开实时仪表盘](https://benchmark-radar.org/) 浏览扫描结果。阅读论文：[arXiv:2609.11115](https://arxiv.org/abs/2609.11115)。
