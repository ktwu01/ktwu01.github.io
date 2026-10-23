---
title: "Benchmark Radar 第 89 天：工具说真话，也可能漏掉关键证据"
date: 2026-10-23
permalink: /zh/posts/2026/10/benchmark-radar-day89/
tags:
  - AI
  - Benchmarks
---

Benchmark Radar 第 89 天。工具说真话，也可能漏掉关键证据。本轮抓取 1,332 条，发布 630 条，其中 289 条标为推荐。

> 作者：[Koutian Wu](https://www.linkedin.com/in/ktwu01/)；[GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar 已上线。** [打开仪表盘](https://benchmark-radar.org/)、[在 GitHub 上 Star](https://github.com/ktwu01/benchmark-radar)，或阅读[论文](https://arxiv.org/abs/2609.11115)。数据见 [Hugging Face 数据集](https://huggingface.co/datasets/ktwu01/benchmark-radar)。

EpiSEM-Bench 测试工具返回的信息属实，却遗漏安全相关事实时，智能体会怎样行动。它在六个领域设置 300 组匹配的安全与不安全任务对，改变缺失证据，保持用户请求本身无害。这样可以把补全证据与常规拒答行为分开评估。 [EpiSEM-Bench: Evaluating Safety and Evidence Recovery in LLM Agents under Missing Evidence](https://arxiv.org/abs/2610.31650)。

AgentPhishing 测试自适应、带有说服性的钓鱼邮件，能否使邮件智能体漏检攻击并执行恶意请求。它既测检测，也测实际响应。识别可疑邮件与抵制其中的指令，是两种需要分别记录的结果。 [AgentPhishing: A Benchmark of LLM Email Agents Under Adaptive Attack](https://arxiv.org/abs/2610.31404)。

## 为什么要在意

安全评估应检查智能体能否发现证据缺失，以及漏检后会采取什么行动。作出操作时掌握了哪些信息，会影响安全结果。

## 扫描范围

这是按关键词筛选的发现信息流，不能代表全部 AI 研究。归档简报使用了所收录 630 条证据中的 161 条。本文概述其中引用的发布成果；扫描发现日期不一定是成果的最初发布日期。

数据与简报：[2026-10-23 归档快照](https://github.com/ktwu01/benchmark-radar/blob/2f75b7a07c6f233bcbcb461631befc2b118be584/data/snapshots/2026-10-23.json)。
