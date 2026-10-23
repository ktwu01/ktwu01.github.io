---
title: "Benchmark Radar 第 79 天：标准答案能否从输入推出"
date: 2026-10-13
permalink: /zh/posts/2026/10/benchmark-radar-day79/
tags:
  - AI
  - Benchmarks
---

Benchmark Radar 第 79 天。标准答案能否从输入推出。本轮抓取 1,476 条，发布 624 条，其中 323 条标为推荐。

> 作者：[Koutian Wu](https://www.linkedin.com/in/ktwu01/)；[GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar 已上线。** [打开仪表盘](https://benchmark-radar.org/)、[在 GitHub 上 Star](https://github.com/ktwu01/benchmark-radar)，或阅读[论文](https://arxiv.org/abs/2609.11115)。数据见 [Hugging Face 数据集](https://huggingface.co/datasets/ktwu01/benchmark-radar)。

Unreachable Oracles 审计基准答案能否从智能体收到的信息中推导出来。它在明确声明的有限许可推导集合中，追踪目标值和构造步骤。比较模型准确率之前，需要先确认任务在自身规则下确实可解。 [Unreachable Oracles: Auditing Ground-Truth Derivability in a Synthetic Tool-Drift Benchmark for LLM Agents](https://doi.org/10.5281/zenodo.23334714)。

GraphInstruct 1.1 提供 900 条图生成指令，分为六个约束等级，并有 1,782 个算法合成的参考解。它公开五个确定性评分维度、模型原始回答和逐例得分，方便检查总通过率掩盖的失败。 [GraphInstruct: A Progressive Benchmark for Diagnosing Capability Gaps in LLM Graph Generation](https://doi.org/10.5281/zenodo.23330977)。

## 为什么要在意

先验证标准答案，再比较解题系统。评分还应保留足够细节，说明系统漏掉了哪些约束。

## 扫描范围

这是按关键词筛选的发现信息流，不能代表全部 AI 研究。归档简报使用了所收录 624 条证据中的 143 条。本文概述其中引用的发布成果；扫描发现日期不一定是成果的最初发布日期。

数据与简报：[2026-10-13 归档快照](https://github.com/ktwu01/benchmark-radar/blob/2f75b7a07c6f233bcbcb461631befc2b118be584/data/snapshots/2026-10-13.json)。
