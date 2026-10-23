---
title: "Benchmark Radar 第 85 天：逐条判断证据是否改变"
date: 2026-10-19
permalink: /zh/posts/2026/10/benchmark-radar-day85/
tags:
  - AI
  - Benchmarks
---

Benchmark Radar 第 85 天。逐条判断证据是否改变。本轮抓取 1,355 条，发布 602 条，其中 281 条标为推荐。

> 作者：[Koutian Wu](https://www.linkedin.com/in/ktwu01/)；[GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar 已上线。** [打开仪表盘](https://benchmark-radar.org/)、[在 GitHub 上 Star](https://github.com/ktwu01/benchmark-radar)，或阅读[论文](https://arxiv.org/abs/2609.11115)。数据见 [Hugging Face 数据集](https://huggingface.co/datasets/ktwu01/benchmark-radar)。

Evidence-State Drift 在重复检索中记录规范化后的论断、支持段落、来源身份、时间戳和内容指纹。回放基准覆盖 67 条论断和 871 次观测，用来区分实质性证据变化与单纯的页面格式变化。 [Evidence-State Drift: A Claim-Level Framework and Replay Benchmark for Web-Connected LLM Agents](https://doi.org/10.5281/zenodo.23452676)。

版本化的 Honest agent scores 数据包重新计算了 3,300 次 Terminal-Bench 4.0 运行。它报告称，移除 30 个被标记任务，或改变重复运行的聚合方式，都未实质改变排名；在 66 个任务下，约 9.5 分以内的差距被判为并列。该结论限于这份数据包和分析。 [Honest agent scores: do benchmark defects or repeats change which AI agent wins?](https://doi.org/10.6084/m9.figshare.34515048.v2)

## 为什么要在意

看到回归警报或排行榜分差时，先检查底层证据是否变化，以及测得的差距能否排除不确定性。

## 扫描范围

这是按关键词筛选的发现信息流，不能代表全部 AI 研究。归档简报使用了所收录 602 条证据中的 172 条。本文概述其中引用的发布成果；扫描发现日期不一定是成果的最初发布日期。

数据与简报：[2026-10-19 归档快照](https://github.com/ktwu01/benchmark-radar/blob/2f75b7a07c6f233bcbcb461631befc2b118be584/data/snapshots/2026-10-19.json)。
