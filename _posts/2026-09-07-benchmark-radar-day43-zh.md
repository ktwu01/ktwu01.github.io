---
title: "Benchmark Radar 第四十三天：论文截数日——源计数与图表数据冻结"
date: 2026-09-07
permalink: /zh/posts/2026/09/benchmark-radar-day43/
tags:
  - AI
  - Benchmarks
  - Paper
  - Data Freeze
  - Audit
  - Plain English
---

Benchmark Radar 的第四十三天。技术论文的发现截数锁定在 2026-09-07。源计数、图表数据、全目录审计管道全部冻结，服务 v0.11.0 发布与 arXiv 投稿。记分牌：170 颗星，30 个 fork。

> 作者：[Koutian Wu](https://www.linkedin.com/in/ktwu01/)；[GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar 已上线。** 每天追踪新的 AI 基准测试、数据集与排行榜：[打开仪表盘](https://benchmark-radar.org/) 或 [在 GitHub 上 Star](https://github.com/ktwu01/benchmark-radar)。

截数日期是在此之后不再有新的发现快照、注册表输入、模型报告或分数进入论文证据库的日期。v0.11.0 发布锁定软件提交 `8f46bbf` 与 2026-09-07 发现截数。注册表快照保留其八月采集日期。

PR #571 推导报告用的发现入库源计数：37 个公开源（13 个直连连接器，24 个第一方实验室源）驱动每日发现管道。计数从实时注册表计算并写入论文图表数据。

PR #572 把 README 的源计数锁定到实时注册表，徽章与论文保持一致。PR #573 跑完六步 CI 序列，通过论文子模块导出 `figure-data.tex`，头部记录输入 SHA-256 哈希。PR #574 执行全目录审计：`audit_catalog.py` 核验 1,283 条源记录（790 条有分、493 条无分）与 12,916 个数值观测，`audit_findings.py` 导出完整发现表。

PR #575 用排行榜的模型身份重建模型注册表，PR #576 在新排行榜模型周围重冻结 Logo 审计 ID。

为什么要在意

截数不是暂停——它是契约。论文里的每个数字、每张图、每张表，都追溯到这一天冻结的输入。`figure-data.tex` 与发布包 `benchmark-radar-paper-data-v0.11.0.zip` 里的 SHA-256 哈希让证据可验证、防篡改。

把源计数冻结在 37，意味着论文里的「37 个公开源」声明可对 2026-09-07 当时的注册表核验，而非随后续新增漂移的数字。

解决的问题

- #570：推导报告用发现入库源计数（37 源）
- #571：README 源计数锁定实时注册表
- #572：导出带输入哈希的 figure-data.tex
- #573：全目录审计——1,283 源记录，12,916 观测值
- #574：用排行榜身份重建模型注册表
- #575：重冻结 Logo 审计 ID
- 记分牌：170 / 1000 星，30 个 fork

第四十四天：论文子模块经引用修订、源计数修订、重建 PDF 推进——arXiv 投稿包成型。

> 想跟进 Benchmark Radar？[在 GitHub 上 Star 仓库](https://github.com/ktwu01/benchmark-radar) 获取每日更新，或 [打开实时仪表盘](https://benchmark-radar.org/) 浏览扫描结果。