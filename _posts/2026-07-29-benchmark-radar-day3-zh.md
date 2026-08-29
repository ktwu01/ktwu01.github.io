---
title: "Benchmark Radar 第三天：可链接的评分对话框与过滤器修复"
date: 2026-07-29
permalink: /zh/posts/2026/07/benchmark-radar-day3/
tags:
  - AI
  - Benchmarks
  - UX
  - URL Routing
---

内容不多，但两处精准的修复让雷达变得能分享了。

> 作者：[Koutian Wu](https://www.linkedin.com/in/ktwu01/)；[GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar 已上线。** 每天追踪新的 AI 基准测试、数据集与排行榜：[打开仪表盘](https://ktwu01.github.io/benchmark-radar/) 或 [在 GitHub 上 Star](https://github.com/ktwu01/benchmark-radar)。

今天做了什么

我们修了扫描日期过滤器。之前你选好日期，过滤器会自己跳回旧日期。现在修好之后，它会稳稳停在你新选的那天。

我们做了一个能链接的评分细则对话框。评分细则就是解释「这个分数怎么算出来」的那个弹窗。现在它可以靠 URL 里的一串哈希直接打开。你可以在消息或论文里直接发链接，指到某个具体的评分细则。

我们加了一个评分细则哈希测试。这个测试防止链接行为以后又退回原样。

我们修了记录展开显示的 bug。之前展开状态渲染得不对，现在好了。

我们修了趋势图全语料库的问题。趋势图现在展示完整语料库，而不只是其中一部分。

为什么要在意

可链接这件事听着不起眼，但它改变了一个工具的用法。当你能把一个 URL 发给别人，让对方直接落到某个具体基准的评分细则上，雷达就从「你偶尔去瞄一眼的网页」变成了「你写论文时引用、在聊天里分享」的东西。

扫描日期过滤器的修复是个信任问题。如果用户选了日期，过滤器却自己跳回去，他们就不再信这些控件了。小修小补会一点点攒成信任。

解决的问题

- #48：扫描日期过滤器和评分细则链接
- 评分细则对话框可通过 URL 哈希访问
- 记录展开状态渲染
- 趋势图全语料库展示

明天：历史数据回填、新鲜度提示横幅和 agentic 分类学。

> 想跟进 Benchmark Radar？[在 GitHub 上 Star 仓库](https://github.com/ktwu01/benchmark-radar) 获取每日更新，或 [打开实时仪表盘](https://ktwu01.github.io/benchmark-radar/) 浏览扫描结果。
