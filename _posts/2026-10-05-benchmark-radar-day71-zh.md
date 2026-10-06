---
title: "Benchmark Radar 第七十一天：通过你训练时见过的测试"
date: 2026-10-05
permalink: /zh/posts/2026/10/benchmark-radar-day71/
tags:
  - AI
  - Benchmarks
---

Benchmark Radar 的第七十一天。每日扫描发布 560 条记录，推荐 273 条，领头的是 《Passing the Test You Trained On》：一项针对 15 个提示注入检测器的研究。记分牌：279 颗星，45 个 fork。

> 作者：[Koutian Wu](https://www.linkedin.com/in/ktwu01/)；[GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar 已上线。** 每天追踪新的 AI 基准测试、数据集与排行榜：[打开仪表盘](https://benchmark-radar.org/) 或 [在 GitHub 上 Star](https://github.com/ktwu01/benchmark-radar)。阅读论文：[arXiv:2609.11115](https://arxiv.org/abs/2609.11115)。查询数据：[Hugging Face 数据集](https://huggingface.co/datasets/ktwu01/benchmark-radar)。

本轮抓取 1,275 条，保留 560 条，推荐 273 条。

《Passing the Test You Trained On》在由真实智能体基准的工具调用重建出的良性与注入输出上，评估了 15 个提示注入检测器。检测器的排名在不同基准之间迁移得很差：在公开的 BIPIA 基准上表现最好的检测器，在该研究的设定下只拦住了 2% 的 AgentDojo 注入。

milipoint-runs 重建了一个雷达数据集的评估划分，原因是打乱且重叠的窗口让大多数测试样本与训练样本共享帧。改为留出完整的录制批次之后，报告的 PointMLP 识别准确率从约 94% 降到 37% 至 39%。

OpenGameEval 让编程智能体在可复现、有状态的 Roblox Studio 会话中运行。它对编辑后的场景和模拟游玩都做可执行检查，并把观察工具和编辑工具分开，使探索行为可以和最终任务完成分开度量。

为什么要在意

一个检测器在一个基准上排第一、在另一个基准上只拦住 2%，说明它学到的是那个基准。当天的第二项研究，94% 降到 37% 至 39%，指向同一个结论。

解决的问题

- 每日快照：抓取 1,275，发布 560，推荐 273
- 记分牌：279 / 1000 星，45 个 fork

第七十二天：扫描继续，星数 279，fork 45 个。

> 想跟进 Benchmark Radar？[在 GitHub 上 Star 仓库](https://github.com/ktwu01/benchmark-radar) 获取每日更新，或 [打开实时仪表盘](https://benchmark-radar.org/) 浏览扫描结果。阅读论文：[arXiv:2609.11115](https://arxiv.org/abs/2609.11115)。
