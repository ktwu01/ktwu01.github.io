---
title: "Benchmark Radar 第五十三天：词义、稳定币与网约车智能体"
date: 2026-09-17
permalink: /zh/posts/2026/09/benchmark-radar-day53/
tags:
  - AI
  - Benchmarks
  - Daily Snapshot
---

Benchmark Radar 的第五十三天。每日扫描发布 666 条记录，推荐其中 261 条。领头的是一个修正过的词义基准、一个稳定币压力测试场，以及一个网约车智能体测试。记分牌：229 颗星，36 个 fork。

> 作者：[Koutian Wu](https://www.linkedin.com/in/ktwu01/)；[GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar 已上线。** 每天追踪新的 AI 基准测试、数据集与排行榜：[打开仪表盘](https://benchmark-radar.org/) 或 [在 GitHub 上 Star](https://github.com/ktwu01/benchmark-radar)。阅读论文：[arXiv:2609.11115](https://arxiv.org/abs/2609.11115)。查询数据：[Hugging Face 数据集](https://huggingface.co/datasets/ktwu01/benchmark-radar)。

本轮从各来源抓取 1,467 条，去重和评分后保留 666 条，其中 261 条标为推荐。

lexEN 用人工裁定的修正层替换有争议的词义标签：改动 211 个，删除 56 个。配套的 SenseBench 工具公开 57 个模型、192 次运行的逐题结果。

StableEval Arena 让智能体诊断稳定币压力，并预测未来七天内价格偏离一美元的情况。它用历史回放构造测试，避免未来信息泄漏进题目。

RideWay 只在网约车智能体完成任务后才计算效率，多余的工具调用和多余的对话轮次都会扣分。

为什么要在意

修正自身标签的基准、阻断未来信息泄漏的测试、为多余步骤扣分的评分：三者都把测试自身的漏洞挡在分数之外。雷达要找的正是这类发布。

解决的问题

- 每日快照：抓取 1,467，发布 666，推荐 261
- 记分牌：229 / 1000 星，36 个 fork

第五十四天：更多新基准，其中一个专门抓编程智能体谎报完工。

> 想跟进 Benchmark Radar？[在 GitHub 上 Star 仓库](https://github.com/ktwu01/benchmark-radar) 获取每日更新，或 [打开实时仪表盘](https://benchmark-radar.org/) 浏览扫描结果。阅读论文：[arXiv:2609.11115](https://arxiv.org/abs/2609.11115)。
