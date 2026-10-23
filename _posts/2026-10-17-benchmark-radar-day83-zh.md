---
title: "Benchmark Radar 第 83 天：安全分数也取决于检测器版本"
date: 2026-10-17
permalink: /zh/posts/2026/10/benchmark-radar-day83/
tags:
  - AI
  - Benchmarks
---

Benchmark Radar 第 83 天。安全分数也取决于检测器版本。本轮抓取 1,562 条，发布 749 条，其中 246 条标为推荐。

> 作者：[Koutian Wu](https://www.linkedin.com/in/ktwu01/)；[GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar 已上线。** [打开仪表盘](https://benchmark-radar.org/)、[在 GitHub 上 Star](https://github.com/ktwu01/benchmark-radar)，或阅读[论文](https://arxiv.org/abs/2609.11115)。数据见 [Hugging Face 数据集](https://huggingface.co/datasets/ktwu01/benchmark-radar)。

NVIDIA garak v0.17.1 为每个探针与检测器组合增加 hit@k，衡量攻击是否在前 k 次尝试内成功。它还修复了未检查文件可能算作通过，以及拒答检测计数偏高的问题。模型不变，这些修复也可能让安全分数改变。 [NVIDIA/garak v0.17.1](https://github.com/NVIDIA/garak/releases/tag/v0.17.1)。

一个 FormAI-v2 复现包提供修正后的漏洞标签、固定的训练与留出划分、反事实测试，以及多个验证器版本的输出。研究者可以据此检查漏洞检测器学到的是预期区别，还是标签引入的捷径。 [Replication package for "Version-Dependent Verifier Labels Teach Vulnerability Detectors a scanf Shortcut in FormAI-v2, a Benchmark of LLM-Generated C Code"](https://doi.org/10.5281/zenodo.23421590)。

## 为什么要在意

除了模型版本，也要固定检测器和验证器版本。保留机器可读结果，才能区分评分修正与能力变化。

## 扫描范围

这是按关键词筛选的发现信息流，不能代表全部 AI 研究。归档简报使用了所收录 749 条证据中的 121 条。本文概述其中引用的发布成果；扫描发现日期不一定是成果的最初发布日期。

数据与简报：[2026-10-17 归档快照](https://github.com/ktwu01/benchmark-radar/blob/2f75b7a07c6f233bcbcb461631befc2b118be584/data/snapshots/2026-10-17.json)。
