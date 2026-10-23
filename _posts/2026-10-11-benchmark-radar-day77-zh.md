---
title: "Benchmark Radar 第 77 天：记忆能否跟上新要求"
date: 2026-10-11
permalink: /zh/posts/2026/10/benchmark-radar-day77/
tags:
  - AI
  - Benchmarks
---

Benchmark Radar 第 77 天。记忆能否跟上新要求。本轮抓取 1,263 条，发布 477 条，其中 164 条标为推荐。

> 作者：[Koutian Wu](https://www.linkedin.com/in/ktwu01/)；[GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar 已上线。** [打开仪表盘](https://benchmark-radar.org/)、[在 GitHub 上 Star](https://github.com/ktwu01/benchmark-radar)，或阅读[论文](https://arxiv.org/abs/2609.11115)。数据见 [Hugging Face 数据集](https://huggingface.co/datasets/ktwu01/benchmark-radar)。

Two-Stage Measurement of Update Adherence 测试带记忆的智能体能否遵循修订后的要求。它用确定性规则，分别给记忆系统组装的上下文和最终答案评分。这样可以区分两种失败：没找回新要求，或已经找回却没有采用。 [Two-Stage Measurement of Update Adherence in Language Model Memory Agents: benchmark, event records, and scoring scripts](https://doi.org/10.5281/zenodo.23280324)。

Tariff Cost Benchmark 评估了 228 份海关约束性裁定，其发布时间晚于参评模型已披露的训练截止时间中的最晚日期。更大的 1,098 份裁定集被单独作为上界分析，并按涉及的关税衡量错误。这让分类错误的代价和训练数据接触风险都能被看见。 [Tariff Cost Benchmark: Duty-at-Stake and Direction Bias in LLM Customs Classification](https://doi.org/10.5281/zenodo.23289975)。

## 为什么要在意

有用的诊断应说明错误发生在哪个环节，以及错误会造成什么代价。单一准确率回答不了这两个问题。

## 扫描范围

这是按关键词筛选的发现信息流，不能代表全部 AI 研究。归档简报使用了所收录 477 条证据中的 115 条。本文概述其中引用的发布成果；扫描发现日期不一定是成果的最初发布日期。

数据与简报：[2026-10-11 归档快照](https://github.com/ktwu01/benchmark-radar/blob/2f75b7a07c6f233bcbcb461631befc2b118be584/data/snapshots/2026-10-11.json)。
