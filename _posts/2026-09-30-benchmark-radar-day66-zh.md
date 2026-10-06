---
title: "Benchmark Radar 第六十六天：谁来扮演用户？"
date: 2026-09-30
permalink: /zh/posts/2026/09/benchmark-radar-day66/
tags:
  - AI
  - Benchmarks
---

Benchmark Radar 的第六十六天。每日扫描发布 656 条记录，推荐 186 条，领头的是 UserProxyBench：它检验扮演用户的语言模型是否遵守它的私有指令。记分牌：268 颗星，43 个 fork。

> 作者：[Koutian Wu](https://www.linkedin.com/in/ktwu01/)；[GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar 已上线。** 每天追踪新的 AI 基准测试、数据集与排行榜：[打开仪表盘](https://benchmark-radar.org/) 或 [在 GitHub 上 Star](https://github.com/ktwu01/benchmark-radar)。阅读论文：[arXiv:2609.11115](https://arxiv.org/abs/2609.11115)。查询数据：[Hugging Face 数据集](https://huggingface.co/datasets/ktwu01/benchmark-radar)。

本轮抓取 1,661 条，保留 656 条，推荐 186 条。

UserProxyBench 检验交互式智能体基准里一个隐藏的依赖：扮演用户的语言模型是否遵守自己的私有指令。它加入了用户保真度得分，固定被评估的智能体，只在 375 个企业任务上改变模拟用户。

EnterpriseBench 把企业评估从静态问答推进到交互式决策，涉及信息缺失、不确定性、反馈和长期取舍。它还把已有的企业和金融问答数据集重组成一个统一的基础套件。

CTE-Bench 评估编程模型能否预测：改动代码或存储状态之后，一个运行中的服务在几次调用之后会怎样变化。它不要求模型动手修改，而是询问干预之后的未来行为，从而把状态追踪能力和动作选择分开。

为什么要在意

当由一个模型来扮演用户时，模拟用户的好坏会拉低或抬高被测智能体的分数。UserProxyBench 直接度量这种影响。

解决的问题

- 每日快照：抓取 1,661，发布 656，推荐 186
- 记分牌：268 / 1000 星，43 个 fork

第六十七天：扫描继续，星数来到 268。

> 想跟进 Benchmark Radar？[在 GitHub 上 Star 仓库](https://github.com/ktwu01/benchmark-radar) 获取每日更新，或 [打开实时仪表盘](https://benchmark-radar.org/) 浏览扫描结果。阅读论文：[arXiv:2609.11115](https://arxiv.org/abs/2609.11115)。
