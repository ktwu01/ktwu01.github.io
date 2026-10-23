---
title: "Benchmark Radar 第 84 天：每个正确答案花多少钱"
date: 2026-10-18
permalink: /zh/posts/2026/10/benchmark-radar-day84/
tags:
  - AI
  - Benchmarks
---

Benchmark Radar 第 84 天。每个正确答案花多少钱。本轮抓取 1,233 条，发布 488 条，其中 165 条标为推荐。

> 作者：[Koutian Wu](https://www.linkedin.com/in/ktwu01/)；[GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar 已上线。** [打开仪表盘](https://benchmark-radar.org/)、[在 GitHub 上 Star](https://github.com/ktwu01/benchmark-radar)，或阅读[论文](https://arxiv.org/abs/2609.11115)。数据见 [Hugging Face 数据集](https://huggingface.co/datasets/ktwu01/benchmark-radar)。

Cost Per Correct 按每个正确答案的美元成本给智能体排名。1.0 版只有五项简单任务，用确定性的正则表达式检查评分。这个小规模任务集可用于有限的成本比较，无法说明复杂智能体工作的表现。 [Cost Per Correct: benchmark tasks for cost-per-correct-answer evaluation of LLM agents](https://doi.org/10.5281/zenodo.23439614)。

《Accuracy-Matched Is Not Cost-Matched》用每解出一题所需的 GPU 服务时间，衡量一个 4 位量化推理模型。在报告的设置中，受内存约束的负载下，较长输出抵消了 41% 至 47% 的单 token 节省；批量大小为一时，这一比例为 6%。服务条件会改变成本核算。 [Accuracy-Matched Is Not Cost-Matched: Pricing INT4 Reasoning Deployments by Served GPU Time per Solved Problem](https://zenodo.org/records/23448613)。

## 为什么要在意

在目标工作负载上比较每完成一项任务的成本。token 价格、答案长度和并发量都会影响账单。

## 扫描范围

这是按关键词筛选的发现信息流，不能代表全部 AI 研究。归档简报使用了所收录 488 条证据中的 126 条。本文概述其中引用的发布成果；扫描发现日期不一定是成果的最初发布日期。

数据与简报：[2026-10-18 归档快照](https://github.com/ktwu01/benchmark-radar/blob/2f75b7a07c6f233bcbcb461631befc2b118be584/data/snapshots/2026-10-18.json)。
