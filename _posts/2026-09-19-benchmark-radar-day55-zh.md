---
title: "Benchmark Radar 第五十五天：从最新的 main 开始"
date: 2026-09-19
permalink: /zh/posts/2026/09/benchmark-radar-day55/
tags:
  - AI
  - Benchmarks
  - Open Source
  - Contributors
---

Benchmark Radar 的第五十五天。贡献者指南新增一条规则：每个分支都从最新的 main 开始。微信群二维码更新，每日扫描按时运行。记分牌：234 颗星，40 个 fork。

> 作者：[Koutian Wu](https://www.linkedin.com/in/ktwu01/)；[GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar 已上线。** 每天追踪新的 AI 基准测试、数据集与排行榜：[打开仪表盘](https://benchmark-radar.org/) 或 [在 GitHub 上 Star](https://github.com/ktwu01/benchmark-radar)。阅读论文：[arXiv:2609.11115](https://arxiv.org/abs/2609.11115)。查询数据：[Hugging Face 数据集](https://huggingface.co/datasets/ktwu01/benchmark-radar)。

AGENTS.md 中关于分支和 PR 的规则（次日作为 PR #672 合并）现在要求：分支必须从最新的 main 开始，落后的分支在开 PR 前先 rebase。后续补充写明了做法：用 fetch 拿到最新 main，不去 pull 本地 main；建分支时不设跟踪；首次 push 时再设置上游。

规则点名了过时基线造成的两种隐蔽问题。第一，分支带着 main 上已经改过的旧文件，一行改动就可能顺手撤掉别人的工作。第二，技术报告子模块的指针可能倒退，把论文钉回更早的版本。

Issue #668 更新了仓库里的微信群二维码。

为什么要在意

这两种问题在小 diff 里都看不出来，所以审查者容易漏掉。把规则写下来，就把检查从审查者的记忆挪到了贡献者的第一条命令。

解决的问题

- #672：分支从最新的 main 开始
- #668：微信群二维码更新
- 记分牌：234 / 1000 星，40 个 fork

第五十六天：外部贡献者的两个修复合并，论文源码同步到最新。

> 想跟进 Benchmark Radar？[在 GitHub 上 Star 仓库](https://github.com/ktwu01/benchmark-radar) 获取每日更新，或 [打开实时仪表盘](https://benchmark-radar.org/) 浏览扫描结果。阅读论文：[arXiv:2609.11115](https://arxiv.org/abs/2609.11115)。
