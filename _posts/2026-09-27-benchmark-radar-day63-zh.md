---
title: "Benchmark Radar 第六十三天：安静的周日，和一次评分器修复"
date: 2026-09-27
permalink: /zh/posts/2026/09/benchmark-radar-day63/
tags:
  - AI
  - Benchmarks
---

Benchmark Radar 的第六十三天。每日扫描发布 314 条记录，推荐 106 条，领头的是 Kalyvox Voice Benchmark 2026：它用 240 通受控通话给一个语音智能体打分。记分牌：257 颗星，41 个 fork。

> 作者：[Koutian Wu](https://www.linkedin.com/in/ktwu01/)；[GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar 已上线。** 每天追踪新的 AI 基准测试、数据集与排行榜：[打开仪表盘](https://benchmark-radar.org/) 或 [在 GitHub 上 Star](https://github.com/ktwu01/benchmark-radar)。阅读论文：[arXiv:2609.11115](https://arxiv.org/abs/2609.11115)。查询数据：[Hugging Face 数据集](https://huggingface.co/datasets/ktwu01/benchmark-radar)。

本轮抓取 1,006 条，保留 314 条，推荐 106 条。

Kalyvox Voice Benchmark 2026 用 240 通法语和英语的受控通话评估一个语音智能体，覆盖 12 个场景族。它报告交互层面的指标：响应延迟、意图准确率、任务完成、转接、预约和兜底处理，而不依赖转写质量。

更新后的全文提取流水线保留了原来冻结的评分器，另加一个对齐评分器，修正三处已确认的缺陷，其中包括比较以开尔文记录的温度时没有做换算。归档还保留了溯源片段，把每个提取出的数值连回原文。

agent-eval-platform 把每次客服智能体试验放进独立的 Kubernetes 任务，度量 pass^k 可靠性（重复尝试是否都能成功），并在 tau-bench 银行任务上注入故障来测试恢复能力。

为什么要在意

评分器修复说明了冻结指标的代价：三处缺陷一直留在数字里，直到旁边加了第二个评分器。

解决的问题

- 每日快照：抓取 1,006，发布 314，推荐 106
- 记分牌：257 / 1000 星，41 个 fork

第六十四天：工作日的扫描恢复。

> 想跟进 Benchmark Radar？[在 GitHub 上 Star 仓库](https://github.com/ktwu01/benchmark-radar) 获取每日更新，或 [打开实时仪表盘](https://benchmark-radar.org/) 浏览扫描结果。阅读论文：[arXiv:2609.11115](https://arxiv.org/abs/2609.11115)。
