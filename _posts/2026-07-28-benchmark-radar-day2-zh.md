---
title: "Benchmark Radar 第二天：累积趋势与工件去重"
date: 2026-07-28
permalink: /zh/posts/2026/07/benchmark-radar-day2/
tags:
  - AI
  - Benchmarks
  - Data Quality
  - Deduplication
---

雷达开始有记忆了。第二天我们建起了累积趋势图，还顺手解决了工件别名的问题。先说一个词：工件（artifact）就是被追踪的每一个具体东西，比如某个基准或数据集。

> 作者：[Koutian Wu](https://www.linkedin.com/in/ktwu01/)；[GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar 已上线。** 每天追踪新的 AI 基准测试、数据集与排行榜：[打开仪表盘](https://ktwu01.github.io/benchmark-radar/) 或 [在 GitHub 上 Star](https://github.com/ktwu01/benchmark-radar)。

今天做了什么

我们建起了累积趋势图。雷达现在能画出各基准数量随时间的变化，而不只是当天的快照。每个分类（基准、数据集、排行榜、研究）都有自己那条趋势线。

我们做了工件别名解析。同一个基准在不同来源下可能叫不同的名字。系统现在能跨多次快照认出它们是同一个，保证在累积趋势里一个工件只被数一次，管它顶着多少个名字。

我们把 Explorer 视图并进了主雷达。原本独立的 Explorer 被整合进主界面。两个视图在抢注意力，最后统一的那个赢了。

我们重新校准了优先级评分。调整了评分系统，更好地区分「真的新基准」和「重新发布的旧更新」。

我们给证据采集流水线加了更多来源。

我们清理了一批 UI 元素。去掉了顶部导航栏、趋势板块和来源面板里多余的东西。来源面板不再固定。仓库徽章从纯名单变成了可点的链接。

为什么要在意

工件去重是这类雷达的核心难题。不去重的话，同一个基准会以十个略有不同的名字出现十次，所有计数都膨胀。别名解析用的是精确标识符，不是模糊的标题匹配，所以精度高。

累积趋势图是第一个明确信号：这个项目不只是一个每日扫描器，它正在变成一个纵向观测工具，追着 AI 基准生态的演变轨迹看。

解决的问题

- #29：雷达 UX 和覆盖范围修复
- #33：解决雷达问题
- #46：跨快照解析工件别名
- 基于精确标识符的重复检测
- 优先级评分重新校准

明天：扫描日期过滤器修复和可链接的评分细则对话框。

> 想跟进 Benchmark Radar？[在 GitHub 上 Star 仓库](https://github.com/ktwu01/benchmark-radar) 获取每日更新，或 [打开实时仪表盘](https://ktwu01.github.io/benchmark-radar/) 浏览扫描结果。
