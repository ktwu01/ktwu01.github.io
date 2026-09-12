---
title: "Benchmark Radar 第三十九天：每日简报有了自己的家"
date: 2026-09-03
permalink: /zh/posts/2026/09/benchmark-radar-day39/
tags:
  - AI
  - Benchmarks
  - Blog
  - Open Source
  - Data
  - Plain English
---

Benchmark Radar 的第三十九天。每日简报现在有了自己的落地页、完整存档和订阅源，仪表盘导航也短到一眼能扫完。记分牌：144 颗星，27 个 fork。

> 作者：[Koutian Wu](https://www.linkedin.com/in/ktwu01/)；[GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar 已上线。** 每天追踪新的 AI 基准测试、数据集与排行榜：[打开仪表盘](https://benchmark-radar.org/) 或 [在 GitHub 上 Star](https://github.com/ktwu01/benchmark-radar)。

落地页是一个版块的第一页。存档是过去全部页面的完整集合。订阅源是读者订阅的机器可读清单。页面框架是每个页面周围都会出现的共享页眉、导航和页脚。

PR #521 把博客发布在 `/blog/`。每个采集日一个页面，最新三十天出现在落地页，存档列出每一天，另有一个独立订阅源服务订阅者。三种日子各有标签：存了简报的叫每日简报；变化不够大的叫无实质变化；在简报机制出现之前的老快照叫证据摘要。这里没有任何地方调用模型或网络，所以重新构建的结果逐字节一致。

PR #525 精简了仪表盘框架。菜单现在依次是 Today、CLI、Leaderboard、Trends；Explore 和 Rubric 从菜单栏隐藏，但仍在各自网址正常发布；页眉保留星数气泡，去掉 fork 和 issue 气泡。

PR #519 把 CLI 安装缩成一条命令：`npx skills add ktwu01/benchmark-radar`。读者以前要复制再转述的第二步没有了，技能现在从头到尾接管安装，自己检查 CLI、必要时自己修复，并报告它跑了什么。

PR #526 从和仪表盘同一个源提取博客框架，博客页面于是带有相同的导航、语言切换和徽章；框架切到中文时，未翻译的英文正文依然可见。

为什么要在意

这个项目产出里最好读的东西，现在也是最容易够到的东西。带落地页、存档和订阅源的每日记录，是搜索引擎能爬、读者能订阅的记录，而且构建时不调用模型。

更安静的仪表盘意味着更快的决定。菜单更少、徽章数字更少，眼睛就落在数据上；隐藏的路径对已经认识它们的人照常可用。

解决的问题

- `/blog/` 每日简报博客，含存档和 RSS 订阅源
- #512：仪表盘导航和徽章精简
- #519：CLI 安装缩成一条命令
- #526：博客页面与仪表盘框架一致
- 记分牌：144 / 1000 星，27 个 fork

第四十天：一个大多数雷达都不看的发布网络，以及一个靠精确名字找回来的基准。

> 想跟进 Benchmark Radar？[在 GitHub 上 Star 仓库](https://github.com/ktwu01/benchmark-radar) 获取每日更新，或 [打开实时仪表盘](https://benchmark-radar.org/) 浏览扫描结果。阅读论文：[arXiv:2609.11115](https://arxiv.org/abs/2609.11115)。