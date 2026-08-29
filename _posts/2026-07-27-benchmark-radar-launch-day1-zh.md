---
title: "Benchmark Radar 第一天：构建累积仪表板 MVP"
date: 2026-07-27
permalink: /zh/posts/2026/07/benchmark-radar-launch-day1/
tags:
  - AI
  - Benchmarks
  - Open Source
  - Launch
---

Benchmark Radar 第一天。我们从零开始，一天之内搭出了一个能跑的累积仪表板。

> 作者：[Koutian Wu](https://www.linkedin.com/in/ktwu01/)；[GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar 已上线。** 每天追踪新的 AI 基准测试、数据集与排行榜：[打开仪表盘](https://benchmark-radar.org/) 或 [在 GitHub 上 Star](https://github.com/ktwu01/benchmark-radar)。

你好，我是 Koutian。第一天，Benchmark Radar 从一张白纸变成了一个每天默默收数据的仪表板。我们一次性落了 20 段代码改动（每段叫一个 commit，就是保存好的一段代码修改）。它们碰到了每一层：自动构建流水线、怎么存数据、每天视图，还有一个主源挂掉时的备用方案。

下面是搭起来的东西。

我们建好了自动流水线。它现在用最新版本的工具，所以能跟整个生态保持同步。

仪表板现在把每天一整份数据存下来，而不是当天结束就丢掉。这是项目的核心：一份会越长越厚的记录，你可以回头翻。

我们修了一些 bug，之前仪表板显示的数字是错的。现在你看到的，跟流水线实际抓到的对得上。

主源 arXiv 搜索挂掉时，系统会退回到 RSS 订阅。先说一句，arXiv 是研究者发论文预印本的地方。arXiv 搜索有频率限制，所以这个备用方案让每天的跑批活下来，而不是直接失败。

首页现在短到三十秒能扫完。

为什么要在意

搭雷达最难的部分不是收数据，而是让昨天的数据到明天还有用。所以我们第一个承诺就是存下每一次每日扫描。没有它，雷达睡一觉就把什么都忘了，整个想法就垮了。

备用源也是个重要的早期决定。主源偶尔会挂。RSS 质量低点但更扛造。从第一天起就两个都备着，每天跑批就不会因为 arXiv 限流而断掉。

解决的问题

- #4、#5、#1、#2、#3：依赖版本升级
- #10：累积雷达仪表板 MVP
- #11：把快照存到受保护的 main 分支之外
- #13：注意力信号的详情与去重
- #14：精简 Today 概览
- #16：清理 Today 仪表板 UI
- #17：忽略本地开发产物
- #18：简化 Today 仪表板
- #21：主快照作为唯一真实来源
- #22：降级到 arXiv RSS

明天：累积趋势图、UI 清理、证据来源扩展。

> 想跟进 Benchmark Radar？[在 GitHub 上 Star 仓库](https://github.com/ktwu01/benchmark-radar) 获取每日更新，或 [打开实时仪表盘](https://benchmark-radar.org/) 浏览扫描结果。
