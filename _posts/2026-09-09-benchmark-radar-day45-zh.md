---
title: "Benchmark Radar 第四十五天：论文最后准备——重新授权、CI 核验与报告测试对齐"
date: 2026-09-09
permalink: /zh/posts/2026/09/benchmark-radar-day45/
tags:
  - AI
  - Benchmarks
  - Paper
  - License
  - CI
  - Plain English
---

Benchmark Radar 的第四十五天。论文进入最后准备阶段：编辑内容改授 CC BY-NC-SA 4.0，CI 核验冻结论文数据，报告测试与手稿对齐。记分牌：180 颗星，32 个 fork。

> 作者：[Koutian Wu](https://www.linkedin.com/in/ktwu01/)；[GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar 已上线。** 每天追踪新的 AI 基准测试、数据集与排行榜：[打开仪表盘](https://benchmark-radar.org/) 或 [在 GitHub 上 Star](https://github.com/ktwu01/benchmark-radar)。

PR #585 把编辑内容（技术报告、README 正文、文档）改授 CC BY-NC-SA 4.0。软件保持 MIT。新增 `LICENSE-CONTENT.md` 与更新后的 `README.md`/`README.zh-CN.md` 明确分离：代码任意用途免费；论文的散文、图表、原创编辑内容需署名、非商业、相同方式共享。

PR #586 为冻结论文数据加 CI 核验。工作流验证提交的 `figure-data.tex` 哈希与 v0.11.0 发布包一致、`catalog-data.tex` 与 `findings-data.tex` 符合冻结普查、重建 PDF 通过小数值扫描。确保论文的量化声明在数据截止后不再漂移。

PR #587 让报告测试与手稿、入库导出对齐。测试套件现在核验论文的普查数字（1,283 条来源记录、790 条有评分、493 条无评分、12,916 个观测值）与导出的图表数据一致，审计 JSON 证据文件（`evidence/catalog-audit.json`、`evidence/catalog-findings.json`）结构完好。

PR #588 合并 agents 分支策略：动 `main` 或论文子模块指针需显式请求。PR #589 把基准官方排行榜并入报告目录，PR #590 用基准来源的注册名称做分数标题。

为什么要在意

授权分离是有意为之。MIT 代码让任何人都能在雷达引擎上构建。CC BY-NC-SA 4.0 保护论文的编辑成果——散文、图表、分析——不被未经许可商业打包，同时保持对研究与教育开放。

冻结数据的 CI 核验是论文的免疫系统。它们在哈希不匹配、普查漂移、异常渲染数值到达 arXiv 前拦截。测试对齐意味着报告的数字不只是声称——它们持续经受同一冻结输入的验证。

解决的问题

- #585：编辑内容改授 CC BY-NC-SA 4.0
- #586：冻结论文数据 CI 核验（哈希、普查、小数值扫描）
- #587：报告测试与手稿、入库导出对齐
- #588：agents 分支策略（保护 main 与论文指针）
- #589：基准官方排行榜并入报告目录
- #590：注册名称做分数标题
- 记分牌：180 / 1000 星，32 个 fork

第四十六天：arXiv 论文上线——`arXiv:2609.11115` 发布，v0.11.0 发布，全项目引用位置更新。

> 想跟进 Benchmark Radar？[在 GitHub 上 Star 仓库](https://github.com/ktwu01/benchmark-radar) 获取每日更新，或 [打开实时仪表盘](https://benchmark-radar.org/) 浏览扫描结果。阅读论文：[arXiv:2609.11115](https://arxiv.org/abs/2609.11115)。