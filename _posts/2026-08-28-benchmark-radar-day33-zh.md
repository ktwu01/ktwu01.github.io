---
title: "Benchmark Radar 第三十三天：关键词搜索永远抓不到的发布，雷达能抓到了"
date: 2026-08-28
permalink: /zh/posts/2026/08/benchmark-radar-day33/
tags:
  - AI
  - Benchmarks
  - Discovery
  - Model Cards
  - Open Source
  - Plain English
---

Benchmark Radar 的第三十三天。雷达学会了找到关键词搜索永远抓不到的基准发布，注册表里也进了一张带 14 个基准的新前沿模型卡片。记分牌：115 颗星，21 个 fork。

> 作者：[Koutian Wu](https://www.linkedin.com/in/ktwu01/)；[GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar 已上线。** 每天追踪新的 AI 基准测试、数据集与排行榜：[打开仪表盘](https://benchmark-radar.org/) 或 [在 GitHub 上 Star](https://github.com/ktwu01/benchmark-radar)。

关键词搜索只能找到包含你搜索词的页面。一个知名 AI 机构里刚建好的全新仓库可能完全漏掉，因为仓库里还没有可搜索的文字。发现源是雷达盯着看新工作的地方。模型卡片是实验室随模型一起发布的文档。

PR #415 把发现能力扩展到关键词搜索之外。雷达现在扫描 360 个重点 GitHub 机构的新建公开仓库，在知名实验室里上线的基准靠「谁建的」被找到，而不是靠碰巧包含什么词。Hugging Face Daily Papers、Kaggle 数据集和 Zenodo 记录加入发现源，Hugging Face Spaces 也纳入视野，公开排行榜和基准浏览器都可见。每个候选仍要过现有的分类法、低价值抑制、打分、未来日期检查和精确 URL 去重，视野变宽不等于过滤变松。

PR #413 加入 GLM-5.3-Flash 模型卡片，带 14 个基准，数据来自 z.ai 官方技术博客，同一次合并里与注册表的大小写和身份规则对齐。卡片带证据链接，14 个条目可以对着源核对，而不是凭记忆抄。

为什么要在意

关键词发现有个盲区，而盲区恰好是最重要新工作的所在地：实验室建了仓库，头几天甚至几周页面上没有多少文字可匹配。盯着机构本身补上了这个缺口，所有候选仍然过现有过滤，网撒大了但不进噪声。

每日雷达的好坏，取决于它漏掉的最后一个发布。8 月 28 日的快照记下 115 颗星和 21 个 fork，产出它的发现管道现在盯的是机构，不只是文字。

解决的问题

- #409：抓到关键词搜索之外的基准发布，包括知名 AI 与评测机构的新仓库
- #401：GLM-5.3-Flash 模型卡片加入，14 个基准来自 z.ai 官方博客
- 记分牌：115 / 1000 星，21 个 fork

第三十四天：仓库自己重画的星标历史图，一条线一条线。

> 想跟进 Benchmark Radar？[在 GitHub 上 Star 仓库](https://github.com/ktwu01/benchmark-radar) 获取每日更新，或 [打开实时仪表盘](https://benchmark-radar.org/) 浏览扫描结果。
