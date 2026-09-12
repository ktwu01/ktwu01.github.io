---
title: "Benchmark Radar 第四十二天：新鲜发布排行榜来到仪表盘"
date: 2026-09-06
permalink: /zh/posts/2026/09/benchmark-radar-day42/
tags:
  - AI
  - Benchmarks
  - Ranking
  - Dashboard
  - UI
  - Plain English
---

Benchmark Radar 的第四十二天。新鲜发布的排行榜引擎从后端走到仪表盘，每日雷达快照记下第一个完整的排序周期。记分牌：165 颗星，29 个 fork。

> 作者：[Koutian Wu](https://www.linkedin.com/in/ktwu01/)；[GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar 已上线。** 每天追踪新的 AI 基准测试、数据集与排行榜：[打开仪表盘](https://benchmark-radar.org/) 或 [在 GitHub 上 Star](https://github.com/ktwu01/benchmark-radar)。

队列是按发布时间分组的发布集合。窗口是发布必须落在其中才算数的天数跨度。排行榜引擎在入库时完成数据契约验证，评估七天、三十天和九十天窗口。

PR #531 第二阶段把排行榜引擎接入仪表盘。Today 页现在展示按队列窗口分组的新鲜发布排序流，每条记录给出基准身份、归一化分数、测试协议与证据链接。没有足够持久信号的发布显示 `limited_signals` 标签而非名次。七天队列每天更新，三十天队列每周更新，九十天队列每月更新。

PR #562 在排序流里加入协议列，读者能直接看到每个分数是按哪套规则测出来的。PR #563 修复队列标签在服务端与客户端渲染不一致的水合错误。PR #556（第四十一天）已把 sunblaze-ucb 组织加入发现注册表，今天的扫描抓到了它的第一个基准。

为什么要在意

只存在于数据库里的排行榜是承诺。把它放到仪表盘上，规则才真正可见：读者能看到某个发布落在哪个队列、哪个协议测出的分数、它拿的是名次还是 `limited_signals` 标签。

队列结构把扁平列表变成时间轴。一个只出现在七天窗口、不在三十天窗口的基准，讲的故事与贯穿三个窗口的基准完全不同。

解决的问题

- #530：新鲜发布的数据契约与排行榜引擎，第二阶段（仪表盘接入）
- #562：排序流增加协议列
- #563：队列标签水合修复
- 记分牌：165 / 1000 星，29 个 fork

第四十三天：论文准备进入冲刺——源计数、图表数据、审计管道冻结，准备 arXiv 投稿。

> 想跟进 Benchmark Radar？[在 GitHub 上 Star 仓库](https://github.com/ktwu01/benchmark-radar) 获取每日更新，或 [打开实时仪表盘](https://benchmark-radar.org/) 浏览扫描结果。阅读论文：[arXiv:2609.11115](https://arxiv.org/abs/2609.11115)。