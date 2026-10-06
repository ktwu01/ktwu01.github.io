---
title: "Benchmark Radar 第六十五天：来自部署轨迹的基准"
date: 2026-09-29
permalink: /zh/posts/2026/09/benchmark-radar-day65/
tags:
  - AI
  - Benchmarks
---

Benchmark Radar 的第六十五天。每日扫描发布 758 条记录，推荐 381 条，领头的是 TraceDance：它把真实的智能体部署轨迹变成针对不良行为的基准。记分牌：266 颗星，43 个 fork。

> 作者：[Koutian Wu](https://www.linkedin.com/in/ktwu01/)；[GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar 已上线。** 每天追踪新的 AI 基准测试、数据集与排行榜：[打开仪表盘](https://benchmark-radar.org/) 或 [在 GitHub 上 Star](https://github.com/ktwu01/benchmark-radar)。阅读论文：[arXiv:2609.11115](https://arxiv.org/abs/2609.11115)。查询数据：[Hugging Face 数据集](https://huggingface.co/datasets/ktwu01/benchmark-radar)。

本轮抓取 1,423 条，保留 758 条，推荐 381 条。

TraceDance 把真实的智能体部署轨迹变成针对用户指定的不良行为的基准。它从一个记录下来的决策点出发，评估模型的下一步动作，所以任务完成并不被当作行为可接受的充分证据。

Certified Selective Automation of LLM Agent Evaluation 这个方法回答的问题是：在错误率不超出给定预算的前提下，自动裁判能处理多大比例的轨迹复核。它考虑了多个智能体做同一批任务时结果相关的情况，此时通常的独立样本假设不成立。

WebPageBench 根据带类型的界面事件日志来验证网页智能体的任务完成，不用模型裁判，也不抓取页面。它可以只改动一个界面控件而重新渲染同一个任务，提示词和成功条件保持不变。

为什么要在意

本轮扫描发布了 758 条记录，是这一段日子里最多的一天。对每一条都值得问同一个问题：这个分数把什么算作成功？

解决的问题

- 每日快照：抓取 1,423，发布 758，推荐 381
- 记分牌：266 / 1000 星，43 个 fork

第六十六天：扫描继续，星数 266，fork 43 个。

> 想跟进 Benchmark Radar？[在 GitHub 上 Star 仓库](https://github.com/ktwu01/benchmark-radar) 获取每日更新，或 [打开实时仪表盘](https://benchmark-radar.org/) 浏览扫描结果。阅读论文：[arXiv:2609.11115](https://arxiv.org/abs/2609.11115)。
