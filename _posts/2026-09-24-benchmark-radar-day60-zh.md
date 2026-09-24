---
title: "Benchmark Radar 第六十天：250 颗星，以及一个背不下来的基准"
date: 2026-09-24
permalink: /zh/posts/2026/09/benchmark-radar-day60/
tags:
  - AI
  - Benchmarks
  - Milestone
---

Benchmark Radar 的第六十天。第六十天，Benchmark Radar 达到 250 颗星。每日扫描发布 471 条记录，推荐 199 条，领头的是 Uncheatable Eval：它用模型训练之后才发表的文本来打分。记分牌：250 颗星，41 个 fork。

> 作者：[Koutian Wu](https://www.linkedin.com/in/ktwu01/)；[GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar 已上线。** 每天追踪新的 AI 基准测试、数据集与排行榜：[打开仪表盘](https://benchmark-radar.org/) 或 [在 GitHub 上 Star](https://github.com/ktwu01/benchmark-radar)。阅读论文：[arXiv:2609.11115](https://arxiv.org/abs/2609.11115)。查询数据：[Hugging Face 数据集](https://huggingface.co/datasets/ktwu01/benchmark-radar)。

本轮抓取 1,055 条，保留 471 条，推荐 199 条。

Uncheatable Eval 衡量基础语言模型压缩新采集文本的效率。测试材料按计划持续更新，降低了模型在训练中见过答案的可能。

ElecVQA-Bench 在比较视觉语言模型与纯视觉模型的输电线路缺陷检测能力时，控制了六项评估设置。统一输入分辨率后，原本视觉语言模型领先 20.53 分，变成纯视觉模型领先 0.57 分。

SWE-Flux 检验编程模型能否预测真实代码在运行时的行为，覆盖 12 个 Python 仓库的 480 个案例，标准答案来自插桩后的测试运行，不依赖另一个模型的判断。

为什么要在意

统一输入后，20 分的差距缩到不足 1 分。这正是雷达读方法、不读标题的原因。第六十天，250 人为这样一个专门捕捉此类问题的工具点了星。

解决的问题

- 每日快照：抓取 1,055，发布 471，推荐 199
- 记分牌：250 / 1000 星，41 个 fork

第六十一天：每日雷达继续扫描：新基准、新分数，数据库持续生长。

> 想跟进 Benchmark Radar？[在 GitHub 上 Star 仓库](https://github.com/ktwu01/benchmark-radar) 获取每日更新，或 [打开实时仪表盘](https://benchmark-radar.org/) 浏览扫描结果。阅读论文：[arXiv:2609.11115](https://arxiv.org/abs/2609.11115)。
