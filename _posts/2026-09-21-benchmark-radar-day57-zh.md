---
title: "Benchmark Radar 第五十七天：一次拒绝发布的运行"
date: 2026-09-21
permalink: /zh/posts/2026/09/benchmark-radar-day57/
tags:
  - AI
  - Benchmarks
  - Data Quality
---

Benchmark Radar 的第五十七天。每日运行按设计失败了。一项安全检查发现 16 条记录共用同一段描述，拒绝发布。记分牌：238 颗星，41 个 fork。

> 作者：[Koutian Wu](https://www.linkedin.com/in/ktwu01/)；[GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar 已上线。** 每天追踪新的 AI 基准测试、数据集与排行榜：[打开仪表盘](https://benchmark-radar.org/) 或 [在 GitHub 上 Star](https://github.com/ktwu01/benchmark-radar)。阅读论文：[arXiv:2609.11115](https://arxiv.org/abs/2609.11115)。查询数据：[Hugging Face 数据集](https://huggingface.co/datasets/ktwu01/benchmark-radar)。

流水线有一条规则：如果多条记录的摘要一字不差，这段文字多半是模板，运行就停下，不予发布。

今天触发它的是 Zenodo。这个科研存档平台会为上传者存入的每个文件单独生成记录和 DOI。有一位上传者把同一个数据集拆成一个文件一条记录来存档，所有记录共用同一段描述。去重步骤依据标题、DOI 和网址判断，而这些都各不相同，于是这批副本一路走到发布阶段，被守门检查拦下。

当天没有记录快照。贡献分数和贡献者头像墙已刷新。

为什么要在意

缺一天是看得见、修得好的。把十六条几乎相同的记录当成十六项发现发布出去，则既看不见，也难修复。守门检查用一天的产出，换来此后每一天的可信度。

解决的问题

- 每日运行：被重复描述守门检查拦下（第五十八天由 #680 修复）
- 贡献分数与贡献者头像墙刷新
- 记分牌：238 / 1000 星，41 个 fork

第五十八天：修复根因，守门检查保持同样严格。

> 想跟进 Benchmark Radar？[在 GitHub 上 Star 仓库](https://github.com/ktwu01/benchmark-radar) 获取每日更新，或 [打开实时仪表盘](https://benchmark-radar.org/) 浏览扫描结果。阅读论文：[arXiv:2609.11115](https://arxiv.org/abs/2609.11115)。
