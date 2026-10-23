---
title: "Benchmark Radar 第 73 天：不读消息，怎样审计智能体"
date: 2026-10-07
permalink: /zh/posts/2026/10/benchmark-radar-day73/
tags:
  - AI
  - Benchmarks
---

Benchmark Radar 第 73 天。不读消息，怎样审计智能体。本轮抓取 1,657 条，发布 833 条，其中 376 条标为推荐。

> 作者：[Koutian Wu](https://www.linkedin.com/in/ktwu01/)；[GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar 已上线。** [打开仪表盘](https://benchmark-radar.org/)、[在 GitHub 上 Star](https://github.com/ktwu01/benchmark-radar)，或阅读[论文](https://arxiv.org/abs/2609.11115)。数据见 [Hugging Face 数据集](https://huggingface.co/datasets/ktwu01/benchmark-radar)。

ANT 测试能否只看网络流量，就判断语言模型智能体在做什么，而不查看用户的私密消息。它收录了 3,114 个执行回合，覆盖 20 项任务，并标注整体风险、场景和基本动作。安全团队可以据此测试流量监控能识别哪些行为。 [ANT: A Multi-Granularity Network Traffic Dataset and Benchmark for Agents Behavior Auditing](https://arxiv.org/abs/2610.06514)。

FREA 用 751 个专家标注的化学反应评估反应可行性验证器，候选反应来自多种来源。报告的评估中，没有一个验证器在所有来源上都领先。筛选器在某类候选反应上表现好，换一批生成方式后，仍需重新验证。 [FREA: A Multi-Source Expert Benchmark for Reaction Feasibility Verification](https://arxiv.org/abs/2610.06614)。

## 为什么要在意

评估应保留实际工作中的信息边界和输入来源。能看到什么、输入从哪里来，都会影响分数的含义。

## 扫描范围

这是按关键词筛选的发现信息流，不能代表全部 AI 研究。归档简报使用了所收录 1,107 条证据中的 190 条。本文概述其中引用的发布成果；扫描发现日期不一定是成果的最初发布日期。

数据与简报：[2026-10-07 归档快照](https://github.com/ktwu01/benchmark-radar/blob/2f75b7a07c6f233bcbcb461631befc2b118be584/data/snapshots/2026-10-07.json)。
