---
title: "Benchmark Radar 第五十六天：两个社区修复，让记录与顺序无关"
date: 2026-09-20
permalink: /zh/posts/2026/09/benchmark-radar-day56/
tags:
  - AI
  - Benchmarks
  - Open Source
  - Contributors
---

Benchmark Radar 的第五十六天。贡献者 winklemad 合并两个修复：一个让纪录保持者的归属与纪录图一致，另一个保证每个基准的页面地址唯一。记分牌：236 颗星，41 个 fork。

> 作者：[Koutian Wu](https://www.linkedin.com/in/ktwu01/)；[GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar 已上线。** 每天追踪新的 AI 基准测试、数据集与排行榜：[打开仪表盘](https://benchmark-radar.org/) 或 [在 GitHub 上 Star](https://github.com/ktwu01/benchmark-radar)。阅读论文：[arXiv:2609.11115](https://arxiv.org/abs/2609.11115)。查询数据：[Hugging Face 数据集](https://huggingface.co/datasets/ktwu01/benchmark-radar)。

PR #662 修正并列最高分时如何认定纪录保持者。旧代码让源文件中的行序决定结果，于是在 frontier_challenge 基准上，同一天、同一个 20.6 分，摘要记在 GPT-5.6 Sol 名下，纪录图却记在 Grok 4.6 名下。现在并列时按纪录图的规则判定：先比分数，再比最早达成日期，最后比稳定编号。修复后，已发布数据中没有任何基准再自相矛盾。

PR #664 修正为每个基准分配短名的函数。短名同时是文件名和页面地址。在少见的输入组合下，它可能给两个基准分配同一个名字，悄悄覆盖其中一条记录，并让查询工具整体报错。现有数据从未触发这个问题；修复赶在目录继续扩大之前堵上了漏洞。

技术报告子模块同步到最新论文源码，贡献分数刷新。每日快照发布 411 条记录、推荐 125 条，其中包括一个按俚语年份检验繁体中文提示注入防御的基准，以及一个用 131 对高度相似问题构造的语义缓存测试。

为什么要在意

同一条纪录记在两个模型名下，读者点开第一下就不再信任。两个修复都去掉了对偶然顺序的依赖，让同一份数据始终讲同一个故事。两个修复都来自核心团队之外。

解决的问题

- #662：并列时纪录保持者与纪录图一致
- #664：基准短名保证唯一
- #672：贡献者分支规则合并
- 每日快照：抓取 1,128，发布 411，推荐 125
- 记分牌：236 / 1000 星，41 个 fork

第五十七天：每日运行在发布重复文本之前主动停下。

> 想跟进 Benchmark Radar？[在 GitHub 上 Star 仓库](https://github.com/ktwu01/benchmark-radar) 获取每日更新，或 [打开实时仪表盘](https://benchmark-radar.org/) 浏览扫描结果。阅读论文：[arXiv:2609.11115](https://arxiv.org/abs/2609.11115)。
