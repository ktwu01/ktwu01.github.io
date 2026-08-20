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

雷达开始听 Hacker News 的动静了。第六天，我们加了社区注意力信号，还加固了每天定时运行的可靠性。

> 作者：[Koutian Wu](https://www.linkedin.com/in/ktwu01/)；[GitHub: ktwu01](https://github.com/ktwu01/)

今天做的事

我们让雷达从 Hacker News 拉取和基准有关的讨论。这多了一条社区信号：一个基准在 HN 上被聊，说明真有实践者在用，而不只是学术圈在发论文。Hacker News 是一个技术爱好者扎堆的新闻社区。

HN 采集器每次只产出一组固定数量的观察记录。这样万一有个爆款帖子，也不会把整天的快照淹没。

不兼容的 arXiv RSS 文档现在会被跳过，而不是让流水线崩溃。有些 arXiv RSS 条目的元数据格式是错的，系统会优雅地跳过它们。RSS 是一种订阅源格式，很多网站用它来广播新内容。

当 arXiv 某天没返回结果（周末和节假日常这样），雷达会正常跑完，而不是直接失败。

PR #75 修了定时工作流的可靠性问题，包括降级处理和出错后的恢复。

我们把全景报告里生成的图表加进了文档。

GitHub App 令牌从 2.2.2 升级到了 3.2.0（actions/create-github-app-token）。

为什么这件事重要

Hacker News 是 AI 实践者聊自己到底在用啥的地方，不是聊又发了啥论文的地方。加上 HN 信号，雷达就能检测一个基准是不是真的开始被用了，而不只是被引用。这是系统里第一条来自社区的信号。

arXiv 的加固同样重要。要是在某个安静的周日跑挂了一次，大家会慢慢不再信这个系统。让它能扛住空日和格式乱掉的 RSS，定时任务就能无人看管地一直跑。

解决的问题

- #70：GitHub App 令牌升级
- #71：全景报告图表
- #73：隐藏重复的报告表格
- #75：定时雷达可靠性
- #76：Hacker News 采集器集成
- arXiv RSS 文档过滤
- arXiv 空日处理

第七天：模型卡采纳排行榜与注册表扩展。
