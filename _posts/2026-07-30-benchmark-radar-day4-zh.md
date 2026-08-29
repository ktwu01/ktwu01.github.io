---
title: "Benchmark Radar 第四天：历史记忆与新鲜度检测"
date: 2026-07-30
permalink: /zh/posts/2026/07/benchmark-radar-day4/
tags:
  - AI
  - Benchmarks
  - History
  - Freshness
  - Agentic AI
---

雷达学会了记忆。第四天，我们加了历史数据回填、过期检测，还有 agentic 这个分类。

> 作者：[Koutian Wu](https://www.linkedin.com/in/ktwu01/)；[GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar 已上线。** 每天追踪新的 AI 基准测试、数据集与排行榜：[打开仪表盘](https://ktwu01.github.io/benchmark-radar/) 或 [在 GitHub 上 Star](https://github.com/ktwu01/benchmark-radar)。

今天做的事

我们加了一个命令行命令，叫 simulate-history。它会假装过去的每一天都跑过一次采集，用来补出历史快照。我们用它生成了四个历史快照，趋势图这下有了真东西可画。

我们在仪表板上加了过期提示横幅。仪表板就是一个网页，每天把采集到的信息摆出来给你看。如果某天采集失败或者停了，横幅会直接告诉你数据过期了，而不是让你继续相信一份旧数据。

今天视图（打开网站第一眼看到的当天汇总）现在会按分类显示去重后的总量。分类有四种：基准、数据集、排行榜、研究。这样你一眼就能看出整体规模有多大。

我们在分类体系里加了一个 agentic 类别。分类体系就是给每个基准贴标签的规则，比如它是基准还是数据集。以前 agent 类基准被笼统塞进通用类别，现在它们有了自己的家。agent 类基准，指的是专门测试 AI 能不能自己完成任务的基准，比如让 AI 写代码、上网、操作电脑。

我们修了趋势增量的 bug。重新发布的更新不再被算进趋势增量里。我们还加了一个只看正式发布的视图，并把 arXiv 的关键词过滤收紧，只盯基准和数据集的首次发布。arXiv 是研究者发论文预印本的地方。

展开一条记录时，仪表板现在会显示新内容，不再重复贴一遍预告文字。

我们把雷达设成每天跑两次。这样就算某次触发失败，当天还有机会再跑一次。

为什么这件事重要

没有历史的雷达只是一份日报。有历史的雷达才是一张地图。simulate-history 补出了过去几天的数据，趋势图终于有真实内容可展示了。

过期横幅这件事也值得单独说。如果数据其实是两天前的，仪表板就该明说。只有把新鲜度摊开讲清楚，你才会继续信任它。

加 agentic 分类是因为市场在变。像 SWE-bench、WebArena、OSWorld 这类 agent 基准增长很快，已经值得单独成类了。

解决的问题

- #35, #42, #45：过期提示横幅、语料库总量、历史回填
- #52：语料库总量可见性
- #53：新鲜度字段
- #55：趋势增量修复
- #58：agentic 分类

明天：趋势图悬浮卡片和基准全景分析报告。

> 想跟进 Benchmark Radar？[在 GitHub 上 Star 仓库](https://github.com/ktwu01/benchmark-radar) 获取每日更新，或 [打开实时仪表盘](https://ktwu01.github.io/benchmark-radar/) 浏览扫描结果。
