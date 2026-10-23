---
title: "Benchmark Radar 第 74 天：安全监控需要完整日志"
date: 2026-10-08
permalink: /zh/posts/2026/10/benchmark-radar-day74/
tags:
  - AI
  - Benchmarks
---

Benchmark Radar 第 74 天。安全监控需要完整日志。本轮抓取 1,326 条，发布 604 条，其中 274 条标为推荐。

> 作者：[Koutian Wu](https://www.linkedin.com/in/ktwu01/)；[GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar 已上线。** [打开仪表盘](https://benchmark-radar.org/)、[在 GitHub 上 Star](https://github.com/ktwu01/benchmark-radar)，或阅读[论文](https://arxiv.org/abs/2609.11115)。数据见 [Hugging Face 数据集](https://huggingface.co/datasets/ktwu01/benchmark-radar)。

一项运行时验证研究用形式化规则重放 AgentDojo 和 STAC 轨迹，识别了约 70% 的成功攻击，也把 29.3% 的良性运行标为异常。作者认为，轨迹很少记录审批信息，也从不记录时间戳，影响了判断的准确性。日志缺少这些字段，监控器就难以还原操作是否合规。 [Formal Runtime Verification for Tool-Using LLM Agents: An Offline Same-Benchmark Study on AgentDojo and STAC](https://doi.org/10.48550/arxiv.2610.09793)。

《Coding-Agent Benchmarks Should Match Their Users’ Task Flows》把软件问题任务与 4,782 个真实编程智能体会话作了比较。在至少有三条用户消息的会话中，用户会在提问、规划、审查、重构和执行之间切换。只测单个问题的解决情况，很难覆盖这些转换。 [Coding-Agent Benchmarks Should Match Their Users' Task Flows](https://arxiv.org/abs/2610.09633)。

## 为什么要在意

工作过程本身就是测试的一部分。安全审计需要审批和时间记录，交互式编程评估需要保留任务切换。

## 扫描范围

这是按关键词筛选的发现信息流，不能代表全部 AI 研究。归档简报使用了所收录 604 条证据中的 158 条。本文概述其中引用的发布成果；扫描发现日期不一定是成果的最初发布日期。

数据与简报：[2026-10-08 归档快照](https://github.com/ktwu01/benchmark-radar/blob/2f75b7a07c6f233bcbcb461631befc2b118be584/data/snapshots/2026-10-08.json)。
