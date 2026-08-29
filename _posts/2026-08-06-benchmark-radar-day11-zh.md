---
title: "Benchmark Radar 第十一天：KW-Bench 能力层与社区发布"
date: 2026-08-06
permalink: /zh/posts/2026/08/benchmark-radar-day11/
tags: [benchmark-radar, kw-bench, capability-rubric, shadow-mode, community]
---

第十一天，KW-Bench 的能力分级上线了，社区发布也开始了。

> 作者：[Koutian Wu](https://www.linkedin.com/in/ktwu01/)；[GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar 已上线。** 每天追踪新的 AI 基准测试、数据集与排行榜：[打开仪表盘](https://ktwu01.github.io/benchmark-radar/) 或 [在 GitHub 上 Star](https://github.com/ktwu01/benchmark-radar)。

大家好，我是 Koutian。先说几个词。KW-Bench 是我们自己做的一套基准测试。内容哈希（content hash）是一段数据的指纹，同样的内容永远得到同样的指纹，所以能用来做确定性判定。影子模式（shadow mode）是新功能先在背后运行、不影响真实输出的做法，验证没问题了再正式启用。

第十一天做了这些。

KW-Bench 的 L0 到 L5 能力分级标准正式上线了。它用的是确定性、基于内容哈希的判定，不靠人拍脑袋评级。同样的内容每次判定结果都一样，可以复现，也可以审计。

影子模式发布功能跑起来了。新的验证逻辑可以先在后台测，正式生效前完成验证，这样发布风险小了很多。

影子存储恢复也准备好了，保证状态一致。

基准测试的主轨道整理规范了。

内容哈希缓存上线了，重复查询更快。

维恩图（一种展示集合重叠的图）的重叠显示问题修好了。

社区发布的帖文写好了。

雷达数据源的描述也更正了。

为什么重要。

能力分级回答了一个问题：哪些基准测试真的难？这不是主观评级，而是基于内容哈希的判定，结果可复现、可审计。影子模式让新的验证逻辑能先悄悄测一遍，不对外生效，降低了发布风险。

解决掉的 issue：

- Issue #144
- Issue #148
- Issue #151
- Issue #154

> 想跟进 Benchmark Radar？[在 GitHub 上 Star 仓库](https://github.com/ktwu01/benchmark-radar) 获取每日更新，或 [打开实时仪表盘](https://ktwu01.github.io/benchmark-radar/) 浏览扫描结果。
