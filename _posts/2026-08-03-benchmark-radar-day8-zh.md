---
title: "Benchmark Radar 第八天：稳定化与最小修复"
date: 2026-08-03
permalink: /zh/posts/2026/08/benchmark-radar-day8/
tags:
  - AI
  - Benchmarks
  - Stabilization
  - Pipeline
---

注册表大爆炸之后，安静的一天。第八天，我们用两次精准修复稳住了流水线。

> 作者：[Koutian Wu](https://www.linkedin.com/in/ktwu01/)；[GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar 已上线。** 每天追踪新的 AI 基准测试、数据集与排行榜：[打开仪表盘](https://benchmark-radar.org/) 或 [在 GitHub 上 Star](https://github.com/ktwu01/benchmark-radar)。

今天做的事

当雷达同一天跑两次时，第二次现在会接在已有记录后面追加，而不是覆盖掉它。这样一整天的采集数据都留着，不会丢掉早上的那次。

定时延迟的告警范围收窄了。只有队列真的出现异常时才报警，而不是每次轻微延迟都响。CI 日志里的噪音因此少了。CI 是每次提交代码后自动跑测试的系统。

为什么这件事重要

第七天大改之后（注册表扩展、分类法盖章、版本升级），流水线得证明自己还能干净地跑。这两个修复针对的故障，只有当天真跑多次时才会出现。

追加而非替换对数据完整性尤其要紧。要是早上跑了 150 条、晚上 120 条，覆盖会丢掉 30 条，追加则全留着。

解决的问题

- #109：雷达最小修复
- 第二次运行的追加行为
- 定时延迟告警范围收窄

第九天：基准采纳前沿与分数可视化。

> 想跟进 Benchmark Radar？[在 GitHub 上 Star 仓库](https://github.com/ktwu01/benchmark-radar) 获取每日更新，或 [打开实时仪表盘](https://benchmark-radar.org/) 浏览扫描结果。
