---
title: "Benchmark Radar 第四十一天：先定数据契约，再谈排行榜"
date: 2026-09-05
permalink: /zh/posts/2026/09/benchmark-radar-day41/
tags:
  - AI
  - Benchmarks
  - Ranking
  - Data Quality
  - Audit
  - Plain English
---

Benchmark Radar 的第四十一天。新鲜发布的排行榜引擎第一阶段上线，先把数据契约写在前头；报告审计也把原始最高分和同一协议下测出的分数分开。记分牌：160 颗星，28 个 fork。

> 作者：[Koutian Wu](https://www.linkedin.com/in/ktwu01/)；[GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar 已上线。** 每天追踪新的 AI 基准测试、数据集与排行榜：[打开仪表盘](https://benchmark-radar.org/) 或 [在 GitHub 上 Star](https://github.com/ktwu01/benchmark-radar)。

数据契约是数据结构必须遵守的成文规则集。队列是按发布时间分组的发布集合。窗口是发布必须落在其中才算数的天数跨度。协议是分数测量时采用的确切规则集；饱和指的是一套基准的分数已经贴近天花板。

PR #531 交付了新鲜发布排行榜的第一阶段。一个新的校验块检查每份快照里的结构化注意力数据，排行榜引擎评估 7 天、30 天和 90 天窗口。只有经过验证的发布事件算数，例行更新不算；重复身份会合并，一个专门仓库检查阻止单体仓库继承父仓库的星数。分数做归一化，缺失值按「未知」处理而不是按零，没有足够持久信号的发布得到 `limited_signals` 标签而不是一个名次。

PR #514 审计了报告里关于接近天花板基准的说法。原始最高分和协议可比序列讲的是两个不同的故事，报告现在把它们分开，把支撑分数的 ID 记进一份入库的 JSON 审计，并用一张协议感知的表格重建下一稿。

PR #556 把 sunblaze-ucb 组织加进发现注册表，并把扫描上限从 360 提到 361，让这条新记录真的会被扫到。

为什么要在意

排行榜有多诚实，取决于它的规则。先把数据契约和测试写好，意味着数字由项目可以检验的规则决定，然后才是任何界面把它们展示给世界。

饱和度声明是评测报告最容易夸大的地方。把原始最高分和同一协议下测出的分数分开，是「一张图」和「一句声明」的区别。

解决的问题

- #530：新鲜发布的数据契约与排行榜引擎，第一阶段
- #457：饱和度审计把原始分数和协议可比分数分开
- #555：sunblaze-ucb 加入组织发现
- 记分牌：160 / 1000 星，28 个 fork

第四十二天：新鲜发布排行榜来到仪表盘。

> 想跟进 Benchmark Radar？[在 GitHub 上 Star 仓库](https://github.com/ktwu01/benchmark-radar) 获取每日更新，或 [打开实时仪表盘](https://benchmark-radar.org/) 浏览扫描结果。