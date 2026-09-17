---
title: "Benchmark Radar 第五十二天：数据发布与直白语言——Hugging Face 数据集上线，黑话退场"
date: 2026-09-16
permalink: /zh/posts/2026/09/benchmark-radar-day52/
tags:
  - AI
  - Benchmarks
  - Dataset
  - Hugging Face
  - Plain English
---

Benchmark Radar 的第五十二天。数据集随自动同步上线 Hugging Face，十七处项目黑话退出界面，换成直白语言。记分牌：226 颗星，35 个 fork。

> 作者：[Koutian Wu](https://www.linkedin.com/in/ktwu01/)；[GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar 已上线。** 每天追踪新的 AI 基准测试、数据集与排行榜：[打开仪表盘](https://benchmark-radar.org/) 或 [在 GitHub 上 Star](https://github.com/ktwu01/benchmark-radar)。阅读论文：[arXiv:2609.11115](https://arxiv.org/abs/2609.11115)。查询数据：[Hugging Face 数据集](https://huggingface.co/datasets/ktwu01/benchmark-radar)。

PR #657 合并 Hugging Face 数据集导出（关闭 #644）：基准目录、详情记录、每日发现快照作为版本化数据集发布，附自动同步工作流。后续修复保留无模型 ID 的分数行，对齐导出分数行，严格验证目录分片，雷达语料绑定到解析后的索引父级。

PR #640 把十七处面向用户的项目词汇换成直白语言：corpus 换成采集内容的直接描述，frontier 章节换成 Most tested hard benchmarks，Pareto frontier 换成 Best trade-off，protocol 换成 run conditions。三个无调用点的僵尸翻译条目一并清理。

每日快照照常入库。活体数据库住进两个地方：读者浏览的仪表盘，机器查询的数据集。

为什么要在意

可下载的数据集把读者变成建设者：任何人都能对论文审计过的同一语料跑离线查询。直白语言把访客变成读者：每个删掉的内部词都少一个跳出的理由。先发布数据，再说人话。

解决的问题

- #644：Hugging Face 数据集导出与自动同步
- #657：数据集发布合并
- #640：十七处面向用户文案的直白语言改造
- 记分牌：226 / 1000 星，35 个 fork

第五十三天：每日雷达持续扫描——新基准、新分数，活体数据库持续生长。

> 想跟进 Benchmark Radar？[在 GitHub 上 Star 仓库](https://github.com/ktwu01/benchmark-radar) 获取每日更新，或 [打开实时仪表盘](https://benchmark-radar.org/) 浏览扫描结果。阅读论文：[arXiv:2609.11115](https://arxiv.org/abs/2609.11115)。
