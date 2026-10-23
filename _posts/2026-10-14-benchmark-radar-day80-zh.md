---
title: "Benchmark Radar 第 80 天：用实验预算评估科研智能体"
date: 2026-10-14
permalink: /zh/posts/2026/10/benchmark-radar-day80/
tags:
  - AI
  - Benchmarks
---

Benchmark Radar 第 80 天。用实验预算评估科研智能体。本轮抓取 1,506 条，发布 773 条，其中 410 条标为推荐。

> 作者：[Koutian Wu](https://www.linkedin.com/in/ktwu01/)；[GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar 已上线。** [打开仪表盘](https://benchmark-radar.org/)、[在 GitHub 上 Star](https://github.com/ktwu01/benchmark-radar)，或阅读[论文](https://arxiv.org/abs/2609.11115)。数据见 [Hugging Face 数据集](https://huggingface.co/datasets/ktwu01/benchmark-radar)。

Autonomous Science Bench 要求智能体在固定预算下分批选择实验，接收实验室服务的测量结果，再调整后续实验。首批六项实验活动采用已发表的生物学、化学和材料科学实验。评估由此跟踪连续的实验选择，超出了对固定数据集作答的范围。 [Autonomous Science Bench: Evaluating AI Agents for Autonomous Scientific Discovery](https://arxiv.org/abs/2610.18449)。

[第 78 天](/zh/posts/2026/10/benchmark-radar-day78/)介绍过 SimGlot 数据包。今天收录的相关审计研究，用标准答案判定机制的完整性检查，检测到了全部七类注入缺陷，还发现奖励函数在评分前改变环境状态的问题。智能体的实验选择需要验证，基准的成功判定也需要验证。 [When Agent Evaluation Becomes Unreliable: An Empirical Study of Oracle Failures and Configuration-Dependent Measurement in an LLM Agent Benchmark](https://doi.org/10.48550/arxiv.2610.16067)。

## 为什么要在意

用预算评估科学发现能力，需要可信的反馈，也需要经过检查的成功标准。否则，智能体可能只是在优化错误的测量结果。

## 扫描范围

这是按关键词筛选的发现信息流，不能代表全部 AI 研究。归档简报使用了所收录 773 条证据中的 162 条。本文概述其中引用的发布成果；扫描发现日期不一定是成果的最初发布日期。

数据与简报：[2026-10-14 归档快照](https://github.com/ktwu01/benchmark-radar/blob/2f75b7a07c6f233bcbcb461631befc2b118be584/data/snapshots/2026-10-14.json)。
