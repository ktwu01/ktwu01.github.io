---
title: "Benchmark Radar 第七十天：随机划分会高估表现"
date: 2026-10-04
permalink: /zh/posts/2026/10/benchmark-radar-day70/
tags:
  - AI
  - Benchmarks
---

Benchmark Radar 的第七十天。每日扫描发布 484 条记录，推荐 127 条，领头的是 2026 Cryo-EM Benchmark Dataset：12 个蛋白结构，沉积时间晚于 MICA 披露的所有测试集。记分牌：278 颗星，45 个 fork。

> 作者：[Koutian Wu](https://www.linkedin.com/in/ktwu01/)；[GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar 已上线。** 每天追踪新的 AI 基准测试、数据集与排行榜：[打开仪表盘](https://benchmark-radar.org/) 或 [在 GitHub 上 Star](https://github.com/ktwu01/benchmark-radar)。阅读论文：[arXiv:2609.11115](https://arxiv.org/abs/2609.11115)。查询数据：[Hugging Face 数据集](https://huggingface.co/datasets/ktwu01/benchmark-radar)。

本轮抓取 1,213 条，保留 484 条，推荐 127 条。

2026 Cryo-EM Benchmark Dataset 提供 12 个蛋白结构，沉积时间晚于 MICA 披露的所有测试集。MICA 是一个根据冷冻电镜密度图构建原子模型的人工智能系统。作者还以 25% 序列一致性阈值，对这些结构与 MICA 披露的训练集做了筛查。

有两项发布展示了：当相关的观测在训练和测试之间交叉时，按记录随机划分会高估表现。最清楚的一例是，一个含 1,030 条记录的混凝土强度基准只有 427 种不同配比，其中 76.1% 的记录与另一条记录的成分相同。

Presentation-Invariant Supplier Selection Benchmark 只改变供应商行的顺序，决策相关的信息保持不变。它组合了六个场景、四档目标冲突程度、三种均衡排序和三个开放权重语言模型，共 216 次调用。

为什么要在意

一个有 1,030 条记录、427 种不同配比的基准，独立的测试用例比它的规模所暗示的要少。随机划分会让同一种配比同时出现在两边。

解决的问题

- 每日快照：抓取 1,213，发布 484，推荐 127
- 记分牌：278 / 1000 星，45 个 fork

第七十一天：扫描继续，星数来到 278。

> 想跟进 Benchmark Radar？[在 GitHub 上 Star 仓库](https://github.com/ktwu01/benchmark-radar) 获取每日更新，或 [打开实时仪表盘](https://benchmark-radar.org/) 浏览扫描结果。阅读论文：[arXiv:2609.11115](https://arxiv.org/abs/2609.11115)。
