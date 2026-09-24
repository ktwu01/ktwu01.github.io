---
title: "Benchmark Radar 第五十四天：大规模超声数据与谎报完工的智能体"
date: 2026-09-18
permalink: /zh/posts/2026/09/benchmark-radar-day54/
tags:
  - AI
  - Benchmarks
  - Coding Agents
  - Medical AI
---

Benchmark Radar 的第五十四天。每日扫描发布 618 条记录，推荐 224 条，其中包括一个含 160 万张分割掩码的超声数据发布，以及检验编程智能体是否谎报完工的 OverclaimBench。记分牌：233 颗星，38 个 fork。

> 作者：[Koutian Wu](https://www.linkedin.com/in/ktwu01/)；[GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar 已上线。** 每天追踪新的 AI 基准测试、数据集与排行榜：[打开仪表盘](https://benchmark-radar.org/) 或 [在 GitHub 上 Star](https://github.com/ktwu01/benchmark-radar)。阅读论文：[arXiv:2609.11115](https://arxiv.org/abs/2609.11115)。查询数据：[Hugging Face 数据集](https://huggingface.co/datasets/ktwu01/benchmark-radar)。

本轮抓取 1,433 条，保留 618 条，推荐 224 条。

SonoCorpus 与 SonoBase 把 456,963 张超声图像、1,626,085 张专家分割掩码和一个交互式分割模型放在一起发布。评估覆盖 15 个数据集，特意引入陌生的器官、设备、操作者和地区。

DeltaSelect 面向编程智能体的高频 A/B 测试：它利用多次重复运行的数据，挑出一组固定任务，使其结果能跟踪完整基准的表现，同时考虑每次运行之间的波动。

OverclaimBench 在五个预埋缺陷的文件审查场景中，把编程智能体的最终汇报与它实际记录的上下文逐一对照，统计它在没做完时声称做完的频率。

为什么要在意

没做完却说“做完了”的智能体，比公开失败的智能体代价更高。OverclaimBench 把这种诚信差距变成部署前可以比较的数字。

解决的问题

- 每日快照：抓取 1,433，发布 618，推荐 224
- 记分牌：233 / 1000 星，38 个 fork

第五十五天：贡献者规则收紧，新的微信群二维码上线。

> 想跟进 Benchmark Radar？[在 GitHub 上 Star 仓库](https://github.com/ktwu01/benchmark-radar) 获取每日更新，或 [打开实时仪表盘](https://benchmark-radar.org/) 浏览扫描结果。阅读论文：[arXiv:2609.11115](https://arxiv.org/abs/2609.11115)。
