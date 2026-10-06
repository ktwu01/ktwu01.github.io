---
title: "Benchmark Radar 第六十一天：会奖励假进展的部分得分"
date: 2026-09-25
permalink: /zh/posts/2026/09/benchmark-radar-day61/
tags:
  - AI
  - Benchmarks
---

Benchmark Radar 的第六十一天。每日扫描发布 450 条记录，推荐 198 条，领头的是 PartHackBench：它检验部分得分机制是否会奖励长时间运行的工具智能体的误导性进展。记分牌：252 颗星，41 个 fork。

> 作者：[Koutian Wu](https://www.linkedin.com/in/ktwu01/)；[GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar 已上线。** 每天追踪新的 AI 基准测试、数据集与排行榜：[打开仪表盘](https://benchmark-radar.org/) 或 [在 GitHub 上 Star](https://github.com/ktwu01/benchmark-radar)。阅读论文：[arXiv:2609.11115](https://arxiv.org/abs/2609.11115)。查询数据：[Hugging Face 数据集](https://huggingface.co/datasets/ktwu01/benchmark-radar)。

本轮抓取 1,128 条，保留 450 条，推荐 198 条。

PartHackBench 先由一个私有的认证器确认诚实轨迹与对抗轨迹的当前进度相同、智能体归属也相同，再对两者做比较。这样可以把得分虚高与真实的任务推进分开。

DynBench 会随底层知识的变化自动生成新的知识图谱问答数据集，针对静态测试过时和可能被背下来的问题。BRIE 对临床记录做了同样的事，可刷新的评估一天之内出现了两次。

SWE-Prometheus 把编程智能体的评估从修复给定问题推进了一步。智能体拿到一份仓库快照和一个开放式的治理目标，需要识别风险、排定干预的优先级，并验证自己的改动。

为什么要在意

部分得分只有在工作真的推进时才该上涨。PartHackBench 测的是它会不会因为错误的原因上涨。

解决的问题

- 每日快照：抓取 1,128，发布 450，推荐 198
- 记分牌：252 / 1000 星，41 个 fork

第六十二天：扫描继续，星数来到 252。

> 想跟进 Benchmark Radar？[在 GitHub 上 Star 仓库](https://github.com/ktwu01/benchmark-radar) 获取每日更新，或 [打开实时仪表盘](https://benchmark-radar.org/) 浏览扫描结果。阅读论文：[arXiv:2609.11115](https://arxiv.org/abs/2609.11115)。
