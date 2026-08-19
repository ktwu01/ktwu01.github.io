---
title: "Benchmark Radar 第六天：Hacker News 集成与定时可靠性"
date: 2026-08-01
permalink: /zh/posts/2026/08/benchmark-radar-day6/
tags:
  - AI
  - Benchmarks
  - Hacker News
  - Reliability
  - RSS
---

雷达开始监听 Hacker News。第六天加入了社区注意力信号，并加固了每日定时运行的可靠性。

> 作者：[Koutian Wu](https://www.linkedin.com/in/ktwu01/)；[GitHub: ktwu01](https://github.com/ktwu01/)

## 今日交付

**Hacker News 注意力采集。** 雷达现在从 Hacker News 拉取与基准相关的讨论。这增加了一条社区信号：当一个基准在 HN 上被讨论，说明实践者在关注，而不只是学术圈在讨论。

**Hacker News 观察记录保持稳定且有界。** HN 采集器每次运行产生一组有界的观察记录。这防止了一个爆款帖子淹没整个每日快照。

**arXiv RSS 文档过滤。** 不兼容的 arXiv RSS 文档现在会被跳过而不是导致流水线崩溃。部分 arXiv RSS 条目的元数据格式有误，系统会优雅地跳过它们。

**arXiv 空日处理。** 当 arXiv 在某天没有返回结果（周末和节假日经常如此），雷达能成功完成运行而不是直接失败。

**定时雷达可靠性。** PR #75 解决了定时工作流中的可靠性问题，包括降级处理和错误恢复。

**全景报告图表。** 将全景报告中生成的图表添加到了文档中。

**GitHub App 令牌升级。** `actions/create-github-app-token` 从 2.2.2 升级到了 3.2.0。

## 为什么重要

Hacker News 是 AI 实践者讨论他们真正在用什么的地方，而不是在讨论他们发表了什么。加入 HN 信号意味着雷达能够检测一个基准何时获得了实际使用中的牵引力，而不仅仅是学术引用。这是系统中第一个来自社区的信号。

arXiv 的加固同样重要。一次在安静的周日失败的每日运行，会让人逐渐不再信任这个系统。让系统能够经受住空日和格式错误的 RSS 条目，意味着定时任务可以无人值守地运行。

## 解决的问题

- \#70：GitHub App 令牌升级
- \#71：全景报告图表
- \#73：隐藏重复的报告表格
- \#75：定时雷达可靠性
- \#76：Hacker News 采集器集成
- arXiv RSS 文档过滤
- arXiv 空日处理

第七天：模型卡采纳排行榜与注册表扩展。
