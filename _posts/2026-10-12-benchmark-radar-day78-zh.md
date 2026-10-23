---
title: "Benchmark Radar 第 78 天：注入传到了，不等于执行了"
date: 2026-10-12
permalink: /zh/posts/2026/10/benchmark-radar-day78/
tags:
  - AI
  - Benchmarks
---

Benchmark Radar 第 78 天。注入传到了，不等于执行了。本轮抓取 997 条，发布 449 条，其中 223 条标为推荐。

> 作者：[Koutian Wu](https://www.linkedin.com/in/ktwu01/)；[GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar 已上线。** [打开仪表盘](https://benchmark-radar.org/)、[在 GitHub 上 Star](https://github.com/ktwu01/benchmark-radar)，或阅读[论文](https://arxiv.org/abs/2609.11115)。数据见 [Hugging Face 数据集](https://huggingface.co/datasets/ktwu01/benchmark-radar)。

MultiAgentInject 包含 4,050 次试验，分别改变任务、智能体网络拓扑、攻击类别、隐蔽性和传播深度。它把注入指令是否到达其他智能体，与对方是否照做分开记录。这两种结果对应不同的防护问题：通信边界是否挡住传播，以及接触攻击后是否遵从。 [MultiAgentInject dataset, injection templates, and analysis scripts](https://doi.org/10.5281/zenodo.23297959)。

SimGlot 针对智能体基准的任务生成器和奖励函数，提供八项完整性检查，以及覆盖七类缺陷的 21 个注入故障变体。记录把结果与固定的软件修订版绑定，便于用已知故障检查评分机制。 [SimGlot: Oracle-Integrity Auditing and Configuration-Dependent Measurement in an LLM Agent Benchmark](https://doi.org/10.5281/zenodo.23290600)。

## 为什么要在意

保留中间事件，才能定位问题。单一的成功标记，很难说明防御在哪一步失效，或基准自身出了什么错。

## 扫描范围

这是按关键词筛选的发现信息流，不能代表全部 AI 研究。归档简报使用了所收录 449 条证据中的 124 条。本文概述其中引用的发布成果；扫描发现日期不一定是成果的最初发布日期。

数据与简报：[2026-10-12 归档快照](https://github.com/ktwu01/benchmark-radar/blob/2f75b7a07c6f233bcbcb461631befc2b118be584/data/snapshots/2026-10-12.json)。
