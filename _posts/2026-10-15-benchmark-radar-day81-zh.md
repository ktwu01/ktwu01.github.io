---
title: "Benchmark Radar 第 81 天：去重后仍要按患者划分"
date: 2026-10-15
permalink: /zh/posts/2026/10/benchmark-radar-day81/
tags:
  - AI
  - Benchmarks
---

Benchmark Radar 第 81 天。去重后仍要按患者划分。本轮抓取 1,711 条，发布 899 条，其中 425 条标为推荐。

> 作者：[Koutian Wu](https://www.linkedin.com/in/ktwu01/)；[GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar 已上线。** [打开仪表盘](https://benchmark-radar.org/)、[在 GitHub 上 Star](https://github.com/ktwu01/benchmark-radar)，或阅读[论文](https://arxiv.org/abs/2609.11115)。数据见 [Hugging Face 数据集](https://huggingface.co/datasets/ktwu01/benchmark-radar)。

一项脑肿瘤 MRI 基准审计报告称，所有可追溯的 761 张肿瘤测试图像，都来自训练集中也出现过的患者。按患者隔离的交叉验证使报告的总体准确率从约 99% 降到 95%。只移除像素级重复图像，没有带来同样的修正。 [Complete Patient-Level Leakage Among Traceable Images in a Widely Used Brain Tumor MRI Benchmark](https://doi.org/10.21203/rs.3.rs-11078963/v1)。

EvoProbe 根据诊断反馈重新生成智能体任务。它给可验证的子任务评分，并检查完整动作序列，定位各阶段的瓶颈。即使最终成功率变化很小，也能分别检查规划和执行是否改善。 [EvoProbe: Evaluation-Driven Benchmark Evolution for LLM Agents](https://doi.org/10.48550/arxiv.2610.19433)。

## 为什么要在意

测试应围绕需要泛化的对象来划分。同一个人有多张图像时，隔离单位应是患者；智能体工作流则应保留失败阶段的证据。

## 扫描范围

这是按关键词筛选的发现信息流，不能代表全部 AI 研究。归档简报使用了所收录 899 条证据中的 189 条。本文概述其中引用的发布成果；扫描发现日期不一定是成果的最初发布日期。

数据与简报：[2026-10-15 归档快照](https://github.com/ktwu01/benchmark-radar/blob/2f75b7a07c6f233bcbcb461631befc2b118be584/data/snapshots/2026-10-15.json)。
