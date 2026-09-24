---
title: "Benchmark Radar 第五十八天：修源头，留守门"
date: 2026-09-22
permalink: /zh/posts/2026/09/benchmark-radar-day58/
tags:
  - AI
  - Benchmarks
  - Data Quality
  - Hugging Face
---

Benchmark Radar 的第五十八天。两个修复解除了昨天的停机，却没有放松触发停机的检查：Zenodo 的分文件批量存档合并为一条发现，Hugging Face 模板的复制文本不再冒充描述。记分牌：246 颗星，41 个 fork。

> 作者：[Koutian Wu](https://www.linkedin.com/in/ktwu01/)；[GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar 已上线。** 每天追踪新的 AI 基准测试、数据集与排行榜：[打开仪表盘](https://benchmark-radar.org/) 或 [在 GitHub 上 Star](https://github.com/ktwu01/benchmark-radar)。阅读论文：[arXiv:2609.11115](https://arxiv.org/abs/2609.11115)。查询数据：[Hugging Face 数据集](https://huggingface.co/datasets/ktwu01/benchmark-radar)。

PR #680 合并批量存档。当多条 Zenodo 记录重复同一组作者和同一段描述时，雷达只保留最早的一条，并注明它代表多少个文件。两个条件缺一不可：只看描述相同，可能把恰好措辞一样的两个团队合并；只看作者相同，可能把同一实验室真正独立的存档合并。

PR #679 处理 Hugging Face 上的另一种复制问题。排行榜模板自带一句写好的简介，复制模板时这句话原样带走，于是三个排行榜差点把 “Duplicate this leaderboard to initialize your own!” 当作自己的描述发布。修复先剔除已知的模板句子；更持久的一层是：如果一句单行简介早已由另一位作者先发布过，就清除这份复制品。以后出现新模板，也无需手动加入名单。

手动重跑和定时运行都成功了。快照发布 410 条记录、推荐 163 条，包括面向数据筛选智能体的 Curation-Bench、检验智能体能否质疑用户所提方案的 XYEval，以及覆盖 111 个编程目标的记忆基准 VibeMemBench。

为什么要在意

省事的做法是放松守门检查。持久的做法是教会数据源阶段识别复制品。流水线中的守门检查一行未改，依然会硬性失败，所以下一种未知的复制模式仍会先让运行停下，到不了读者面前。

解决的问题

- #680：Zenodo 批量存档合并为一条发现
- #679：不再把 Hugging Face 模板简介当作仓库自己的描述
- 每日快照：抓取 1,140，发布 410，推荐 163
- 记分牌：246 / 1000 星，41 个 fork

第五十九天：每日雷达继续扫描，两种复制模式都已在源头处理。

> 想跟进 Benchmark Radar？[在 GitHub 上 Star 仓库](https://github.com/ktwu01/benchmark-radar) 获取每日更新，或 [打开实时仪表盘](https://benchmark-radar.org/) 浏览扫描结果。阅读论文：[arXiv:2609.11115](https://arxiv.org/abs/2609.11115)。
