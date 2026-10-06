---
title: "Benchmark Radar 第六十二天：从真实仓库里长出来的基准"
date: 2026-09-26
permalink: /zh/posts/2026/09/benchmark-radar-day62/
tags:
  - AI
  - Benchmarks
---

Benchmark Radar 的第六十二天。每日扫描发布 540 条记录，推荐 171 条，领头的是 repo2bench：它把 Python 仓库转成编程智能体的任务。记分牌：255 颗星，41 个 fork。

> 作者：[Koutian Wu](https://www.linkedin.com/in/ktwu01/)；[GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar 已上线。** 每天追踪新的 AI 基准测试、数据集与排行榜：[打开仪表盘](https://benchmark-radar.org/) 或 [在 GitHub 上 Star](https://github.com/ktwu01/benchmark-radar)。阅读论文：[arXiv:2609.11115](https://arxiv.org/abs/2609.11115)。查询数据：[Hugging Face 数据集](https://huggingface.co/datasets/ktwu01/benchmark-radar)。

本轮抓取 1,256 条，保留 540 条，推荐 171 条。

repo2bench 把 Python 仓库转成编程智能体的任务，任务来自版本历史，或由删除函数生成。模型起草的任务必须先通过确定性检查才会被收录，检查包括抽象语法树变异测试：系统性地改动代码，验证测试能否发现错误。

Era by Eon 在四个领先模型拿到原始 27 道题中的 22 到 25 道之后，扩展了这个企业智能体测试。新增模板要求智能体从相互矛盾或间接的公司记录中推断隐藏事实。每家公司由代码生成，标准答案也由代码算出，不经过语言模型。

LongHorizon Orchestrator Benchmark 固定底层控制策略，只隔离机器人视觉语言调度器所做的决策。它分别考察指令分解、视觉完成检查，以及多物体操作中对已完成目标的记忆。

为什么要在意

标准答案由代码产生，不由另一个模型给出，任何人都可以重新核对分数。

解决的问题

- 每日快照：抓取 1,256，发布 540，推荐 171
- 记分牌：255 / 1000 星，41 个 fork

第六十三天：扫描继续，星数来到 255。

> 想跟进 Benchmark Radar？[在 GitHub 上 Star 仓库](https://github.com/ktwu01/benchmark-radar) 获取每日更新，或 [打开实时仪表盘](https://benchmark-radar.org/) 浏览扫描结果。阅读论文：[arXiv:2609.11115](https://arxiv.org/abs/2609.11115)。
