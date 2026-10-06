---
title: "Benchmark Radar 第六十八天：不看视频也能答的视频测试"
date: 2026-10-02
permalink: /zh/posts/2026/10/benchmark-radar-day68/
tags:
  - AI
  - Benchmarks
---

Benchmark Radar 的第六十八天。每日扫描发布 668 条记录，推荐 244 条，领头的是 Video-Index：这个元基准审计视频测试是否真的需要理解视频。记分牌：272 颗星，45 个 fork。

> 作者：[Koutian Wu](https://www.linkedin.com/in/ktwu01/)；[GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar 已上线。** 每天追踪新的 AI 基准测试、数据集与排行榜：[打开仪表盘](https://benchmark-radar.org/) 或 [在 GitHub 上 Star](https://github.com/ktwu01/benchmark-radar)。阅读论文：[arXiv:2609.11115](https://arxiv.org/abs/2609.11115)。查询数据：[Hugging Face 数据集](https://huggingface.co/datasets/ktwu01/benchmark-radar)。

本轮抓取 1,424 条，保留 668 条，推荐 244 条。

Video-Index 审计视频测试是否真的需要理解视频。它的五层攻击金字塔逐级测试信息量越来越大的捷径。作者报告，在 35 个被审计的基准上，看不到帧内容的攻击者接近完整视频的准确率，打乱帧顺序后仍保留完整准确率的中位数 96%。

Finding the Right Fit 研究了 66 种智能体配置，把语言模型和它的执行框架（提供工具并管理动作的软件）当作一个整体来评估。它报告了模型排名在不同框架和任务之间发生反转。

Scores That Hold, Benchmarks That Leak 审计公开的脑肿瘤磁共振图像分类语料。它在三个层面检查测试的独立性（重复图像、重复患者、采集来源），并度量每一种泄漏对报告性能的影响。

为什么要在意

如果看不到帧内容的攻击者也能接近满分，这个分数描述的是捷径，和视频无关。一天之内有三项审计，对不同领域问了同一个问题。

解决的问题

- 每日快照：抓取 1,424，发布 668，推荐 244
- 记分牌：272 / 1000 星，45 个 fork

第六十九天：扫描继续，星数来到 272。

> 想跟进 Benchmark Radar？[在 GitHub 上 Star 仓库](https://github.com/ktwu01/benchmark-radar) 获取每日更新，或 [打开实时仪表盘](https://benchmark-radar.org/) 浏览扫描结果。阅读论文：[arXiv:2609.11115](https://arxiv.org/abs/2609.11115)。
