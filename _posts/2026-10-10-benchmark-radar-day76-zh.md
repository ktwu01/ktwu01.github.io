---
title: "Benchmark Radar 第 76 天：测试集要留出完整录制"
date: 2026-10-10
permalink: /zh/posts/2026/10/benchmark-radar-day76/
tags:
  - AI
  - Benchmarks
---

Benchmark Radar 第 76 天。测试集要留出完整录制。本轮抓取 1,316 条，发布 547 条，其中 234 条标为推荐。

> 作者：[Koutian Wu](https://www.linkedin.com/in/ktwu01/)；[GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar 已上线。** [打开仪表盘](https://benchmark-radar.org/)、[在 GitHub 上 Star](https://github.com/ktwu01/benchmark-radar)，或阅读[论文](https://arxiv.org/abs/2609.11115)。数据见 [Hugging Face 数据集](https://huggingface.co/datasets/ktwu01/benchmark-radar)。

milipoint-runs 重新检查了 MiliPoint 雷达数据中的重叠窗口。留出完整的一次录制后，报告的识别准确率从约 94% 降到 37% 至 39%。训练窗口和测试窗口共享帧时，随机划分可能测到对录制内容的识别，难以据此判断对新录制的泛化。 [milipoint-runs: run-disjoint evaluation of the MiliPoint millimeter-wave radar dataset](https://doi.org/10.5281/zenodo.23271684)。

Inspect AI 0.3.278 为日志和数据表增加任务及样本描述，把工具审查扩展到交接调用，并修复上下文压缩、token 计数和重试问题。评估框架升级后，审计记录和资源计量都可能变化。 [UKGovernmentBEIS/inspect_ai 0.3.278](https://github.com/UKGovernmentBEIS/inspect_ai/releases/tag/0.3.278)。

## 为什么要在意

比较结果时，应同时记录数据划分和评估框架版本。数据集名称相同，不足以保证两次测量可比。

## 扫描范围

这是按关键词筛选的发现信息流，不能代表全部 AI 研究。归档简报使用了所收录 547 条证据中的 142 条。本文概述其中引用的发布成果；扫描发现日期不一定是成果的最初发布日期。

数据与简报：[2026-10-10 归档快照](https://github.com/ktwu01/benchmark-radar/blob/2f75b7a07c6f233bcbcb461631befc2b118be584/data/snapshots/2026-10-10.json)。
