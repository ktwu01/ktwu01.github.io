---
title: "Benchmark Radar 第四十七天：引用位置转为读者优先——Cite 卡片、CITATION.md 与顶部导航入口"
date: 2026-09-11
permalink: /zh/posts/2026/09/benchmark-radar-day47/
tags:
  - AI
  - Benchmarks
  - Citation
  - UX
  - Documentation
  - Plain English
---

Benchmark Radar 的第四十七天。arXiv 论文上线后，引用位置全面转为读者优先：Cite 卡片默认折叠 APA 与 BibTeX，仓库根目录落地 `CITATION.md`，顶部导航新增 Cite 入口。记分牌：185 颗星，30 个 fork。

> 作者：[Koutian Wu](https://www.linkedin.com/in/ktwu01/)；[GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar 已上线。** 每天追踪新的 AI 基准测试、数据集与排行榜：[打开仪表盘](https://benchmark-radar.org/) 或 [在 GitHub 上 Star](https://github.com/ktwu01/benchmark-radar)。阅读论文：[arXiv:2609.11115](https://arxiv.org/abs/2609.11115)。

PR #601 在所有引用位置标注 arXiv 论文：仪表盘页脚、CLI `--cite` 输出、README 徽章、引用页现统一指向 `arXiv:2609.11115`，含完整作者列表与年份。

PR #602 在顶部导航栏加入 Cite 入口。读者在仪表盘任何页面都能一键跳转引用页，无需翻找页脚。

PR #603 让 Cite 对话框默认折叠 APA 与 BibTeX 块。卡片首推荐人类可读的引用句（"Benchmark Radar: A Living Database and Search Engine for AI Benchmarks and Evaluation, arXiv:2609.11115, 2026"），提供「显示 APA」「显示 BibTeX」开关。这把 90% 读者最常复制的格式放在最前，把结构化格式留给 10% 需要它的人——只需一键。

PR #604 让 Cite 卡片以读者为本：推荐句用自然语言，复制按钮复制纯文本，arXiv 链接直达摘要页。APA 与 BibTeX 展开区保留给参考文献管理器的精确格式。

为什么要在意

引用不是奖杯——是工具。想引用本项目的读者需要两秒拿到正确字符串。把原始 APA/BibTeX 隐在开关后，减少了大多数人的视觉噪音；需要结构化格式的人一键可得。

仓库根目录的 `CITATION.md` 让引用对工具可发现（GitHub「Cite this repository」按钮、参考文献管理器、自动化工作流），无需访问仪表盘。

顶部导航的 Cite 入口闭环：仪表盘 → 论文 → 引用 → 仪表盘。在排行榜发现基准的读者，三键完成引用。

解决的问题

- #600：所有引用位置标注 arXiv 论文
- #601：顶部导航新增 Cite 入口
- #602：Cite 对话框默认折叠 APA/BibTeX
- #603：Cite 卡片读者优先（推荐句、复制按钮、arXiv 链接）
- 记分牌：185 / 1000 星，30 个 fork

第四十八天：每日雷达持续扫描——新基准、新分数，活体数据库持续生长。

> 想跟进 Benchmark Radar？[在 GitHub 上 Star 仓库](https://github.com/ktwu01/benchmark-radar) 获取每日更新，或 [打开实时仪表盘](https://benchmark-radar.org/) 浏览扫描结果。阅读论文：[arXiv:2609.11115](https://arxiv.org/abs/2609.11115)。