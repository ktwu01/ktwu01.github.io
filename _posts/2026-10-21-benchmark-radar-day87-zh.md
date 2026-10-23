---
title: "Benchmark Radar 第 87 天：任务成功仍需检查授权"
date: 2026-10-21
permalink: /zh/posts/2026/10/benchmark-radar-day87/
tags:
  - AI
  - Benchmarks
---

Benchmark Radar 第 87 天。任务成功仍需检查授权。本轮抓取 1,692 条，发布 884 条，其中 391 条标为推荐。

> 作者：[Koutian Wu](https://www.linkedin.com/in/ktwu01/)；[GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar 已上线。** [打开仪表盘](https://benchmark-radar.org/)、[在 GitHub 上 Star](https://github.com/ktwu01/benchmark-radar)，或阅读[论文](https://arxiv.org/abs/2609.11115)。数据见 [Hugging Face 数据集](https://huggingface.co/datasets/ktwu01/benchmark-radar)。

AuthorizationBench 把智能体是否遵守用户授权，与任务完成和常规伤害评估分开。它有 286 个可执行任务，覆盖十个应用领域，并改变情境触发条件和直接后果。智能体完成任务，仍可能超出用户授权。 [Act on Your Behalf, Beyond Your Authorization: Benchmarking LLM Agent Authorization Alignment](https://arxiv.org/abs/2610.27548)。

一项受控扰动研究在两组各 4,320 个回合的匹配实验中，按不同严重程度加入工具拒绝访问、目标变化和约束收紧。它把执行中的调整过程保留下来，便于检查智能体怎样应对变化。 [Benchmarking the responsiveness of LLM-based agentic systems under controlled mid-task perturbations](https://doi.org/10.1038/s41598-026-72720-7)。

## 为什么要在意

评估既要检查智能体获准做什么，也要检查条件变化后如何调整。完成率只能回答其中一部分。

## 扫描范围

这是按关键词筛选的发现信息流，不能代表全部 AI 研究。归档简报使用了所收录 884 条证据中的 183 条。本文概述其中引用的发布成果；扫描发现日期不一定是成果的最初发布日期。

数据与简报：[2026-10-21 归档快照](https://github.com/ktwu01/benchmark-radar/blob/2f75b7a07c6f233bcbcb461631befc2b118be584/data/snapshots/2026-10-21.json)。
