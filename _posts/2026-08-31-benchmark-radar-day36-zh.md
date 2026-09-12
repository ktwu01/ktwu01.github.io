---
title: "Benchmark Radar 第三十六天：一张模型卡，37 个分数"
date: 2026-08-31
permalink: /zh/posts/2026/08/benchmark-radar-day36/
tags:
  - AI
  - Benchmarks
  - Model Cards
  - Search
  - Data Quality
  - Plain English
---

Benchmark Radar 的第三十六天。迄今最大的一张模型卡落地了，34 个基准上排了 37 个分数；搜索也不再靠猜来回答哪个结果是对的。记分牌：128 颗星，24 个 fork。

> 作者：[Koutian Wu](https://www.linkedin.com/in/ktwu01/)；[GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar 已上线。** 每天追踪新的 AI 基准测试、数据集与排行榜：[打开仪表盘](https://benchmark-radar.org/) 或 [在 GitHub 上 Star](https://github.com/ktwu01/benchmark-radar)。

模型卡是实验室随模型一起发布的文档。协议是分数测量时采用的确切规则集，比如带工具还是不带工具。词法搜索是直接匹配单词和短语，像字典索引那样，而不是理解含义。身份是判定两条记录描述的是不是同一个仓库的规则。

PR #472 加入腾讯 Hy4 preview 模型卡，34 个基准 ID 上共 37 个分数。协议保持区分：SWE Atlas 拆成三个，HLE 分带工具和不带工具记录。报告里标为 Internal 的九个基准不进入公开跟踪层，GDPval-AA V2 重复的工具 ID 也统一了。

PR #459 让词法搜索把过程摊开。搜索返回的是检索证据而不是一个笼统的置信度猜测：一个检索分、跨词覆盖率，以及哪些词匹配上了、哪些缺失。回答问题的智能体做最终判断：确证匹配、疑似候选，还是没有可信匹配。判断集现在覆盖 23 个口语化包装句式，比如「找 GPQA Diamond」和「SWE bench verified please」。

PR #466 把审核过的身份覆盖规则接进目录输出，46 个解析成功的仓库以正确的所有者与路径出现，11 个解析不了的记录保持可见但不编造链接。PR #463 把冗长的隐私声明折叠到一次点击之后。

为什么要在意

没有协议细节的模型卡，就像没有刻度的尺。带工具和不带工具的分数分开记，内部结果不进公开层，这正是 37 个数字能用起来的原因。

把证据摊开的搜索才是可以审计的搜索。当工具告诉你哪些词匹配、哪些没匹配，一个错误答案就变得可以解释，而不是神秘。

解决的问题

- #416：腾讯 Hy4 preview 模型卡，37 个分数
- #432：词法搜索摊开检索证据，而不是靠猜
- llm-stats 身份：27 个解析成功，9 个未找到，2 个待审核
- #446：隐私声明折叠到披露按钮之后
- 记分牌：128 / 1000 星，24 个 fork

第三十七天：一张引用卡片、一次点击的 CLI 设置，以及覆盖整个档案的搜索。

> 想跟进 Benchmark Radar？[在 GitHub 上 Star 仓库](https://github.com/ktwu01/benchmark-radar) 获取每日更新，或 [打开实时仪表盘](https://benchmark-radar.org/) 浏览扫描结果。阅读论文：[arXiv:2609.11115](https://arxiv.org/abs/2609.11115)。