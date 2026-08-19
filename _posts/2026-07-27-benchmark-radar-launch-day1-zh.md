---
title: "Benchmark Radar 第一天：构建累积仪表板 MVP"
date: 2026-07-27
permalink: /posts/2026/07/benchmark-radar-launch-day1/
tags:
  - AI
  - Benchmarks
  - Open Source
  - Launch
---

Benchmark Radar 项目的第一天。从零开始，一天之内搭建出了可运行的累积仪表板。

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

第一天覆盖了系统的每一层：CI/CD 流水线、数据持久化、Today 仪表板 MVP、注意力信号处理，以及 arXiv RSS 降级方案。一次性推送了 20 个 commit。

## 今日交付

**基础设施。** 建立了 GitHub Actions 工作流，将 actions/checkout、upload/download-artifact 和 setup-python 升级到最新大版本。pytest 的版本上限从 `<9` 放宽到 `<10`，与上游保持同步。

**累积仪表板 MVP。** 核心思路是：把每日快照持久化到受保护的 `main` 分支之外，让它们随时间累积。每个快照捕获的是完整打分语料库，而不只是摘要。

**注意力信号修复。** 移除了重复信号，修正了详情渲染，让仪表板真正反映出流水线采集到的内容。

**arXiv RSS 降级。** 当 arXiv 主搜索端点失败时，系统会回退到 RSS feed。这很关键，因为 arXiv 的搜索接口有速率限制，在大规模运行时不太可靠。

**Today 仪表板。** 对概览页面做了精简、清理和简化，目标是三十秒内就能扫完。

## 为什么重要

搭建雷达最难的部分不是收集数据，而是让昨天的数据到明天依然有意义。持久化是我们做出的第一个承诺：每次日常扫描都会产生一条记录，供后续运行进行比对。没有这个，雷达隔夜就会失忆。

arXiv 降级同样是奠基性的决策。主端点会挂，RSS feed 精度低但更健壮。从第一天起就两者兼备，确保了每日运行不会因为 arXiv 限流而中断。

## 解决的问题

- \#4, \#5, \#1, \#2, \#3：依赖版本升级
- \#10：累积雷达仪表板 MVP
- \#11：将快照持久化到受保护的 main 分支之外
- \#13：注意力信号的详情与去重
- \#14：精简 Today 概览
- \#16：清理 Today 仪表板 UI
- \#17：忽略本地开发产物
- \#18：简化 Today 仪表板
- \#21：主快照作为唯一真实来源
- \#22：降级到 arXiv RSS

明天：累积趋势图、UI 清理、证据来源扩展。
