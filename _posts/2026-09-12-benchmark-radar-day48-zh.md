---
title: "Benchmark Radar 第四十八天：读者优先的仪表盘——首页、基准页与直白分数"
date: 2026-09-12
permalink: /zh/posts/2026/09/benchmark-radar-day48/
tags:
  - AI
  - Benchmarks
  - UX
  - SEO
  - Documentation
  - Plain English
---

Benchmark Radar 的第四十八天。仪表盘迎来读者优先改造：首页横幅保留文字、去掉像素占用，基准页围绕读者真实搜索重写，About 页把项目故事讲在站内。记分牌：185 颗星，30 个 fork。

> 作者：[Koutian Wu](https://www.linkedin.com/in/ktwu01/)；[GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar 已上线。** 每天追踪新的 AI 基准测试、数据集与排行榜：[打开仪表盘](https://benchmark-radar.org/) 或 [在 GitHub 上 Star](https://github.com/ktwu01/benchmark-radar)。阅读论文：[arXiv:2609.11115](https://arxiv.org/abs/2609.11115)。

About 页上线，引用页改名 Publications——研究者熟悉的词。路径保持 `/cite/`，旧链接继续有效，菜单开始说读者的语言。

基准页告别 stub。每个页面点名该基准拥有的产物，按读者的原话组织章节：它是什么、产物链接、在册分数、引用它的来源、同能力姐妹基准。没有数据的章节直接省略，页面不再承诺目录中没有的产物。

首页横幅收成视觉隐藏标题：读屏器与爬虫照常拿到主题，读者提前一屏看到结果。菜单栏去掉圆圈 info 标记，Blog 与 About 移入页脚，工具行留给工具。优先级分数从五个信号减到三个：数字、条形、评分方法链接。

每日简报只说一次日期。hero 区不再重复眉题、日期行、固定标签与截断导语。博客卡片减成标题加当日发现，种类徽标与日期列随之取消。

PR #618 把论文引用塞进每个查询载荷（`data.citation` 含 APA、BibTeX 与引用 key），同步写入 `site/llms.txt`，测试把五处 BibTeX 表面钉在 `citation.py` 上。PR #619 新增模型卡 SOP（分数随卡走，agent 自报身份），AGENTS.md 拆成参考指南。PR #621 落定 Benchmark Radar™ 名称与贡献者版权行。

为什么要在意

搜索者输入基准名加 paper、dataset、code、leaderboard 或 results。按这些词建页，在查询起点接住读者。About 页让从搜索进来的读者有地方了解项目缘起，链回目录的设计让它有去有回。

解决的问题

- #606：第一方源相对链接按源地址解析
- #609：结构化数据警告修复，基准页逐页 dating
- #612：Publications 别名收敛到 /cite/，sitemap lastmod 补齐
- #618：查询载荷与 llms.txt 内嵌论文引用
- #619：模型卡 SOP，AGENTS.md 拆成参考指南
- #621：Benchmark Radar™ 名称与贡献者版权行
- 记分牌：185 / 1000 星，30 个 fork

第四十九天：README 写清谁在使用雷达——机构研究者横幅与新的微信群二维码。

> 想跟进 Benchmark Radar？[在 GitHub 上 Star 仓库](https://github.com/ktwu01/benchmark-radar) 获取每日更新，或 [打开实时仪表盘](https://benchmark-radar.org/) 浏览扫描结果。阅读论文：[arXiv:2609.11115](https://arxiv.org/abs/2609.11115)。
