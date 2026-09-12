---
title: "Benchmark Radar 第三十七天：引用、设置、全库搜索，一步到位"
date: 2026-09-01
permalink: /zh/posts/2026/09/benchmark-radar-day37/
tags:
  - AI
  - Benchmarks
  - Citations
  - CLI
  - Search
  - Plain English
---

Benchmark Radar 的第三十七天。写论文的人现在不用离开仪表盘就能复制引用，离线安装搬到了网站上，搜索默认会翻遍每一个采集过的日子。记分牌：130 颗星，25 个 fork。

> 作者：[Koutian Wu](https://www.linkedin.com/in/ktwu01/)；[GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar 已上线。** 每天追踪新的 AI 基准测试、数据集与排行榜：[打开仪表盘](https://benchmark-radar.org/) 或 [在 GitHub 上 Star](https://github.com/ktwu01/benchmark-radar)。

引用是对一篇作品的正式著录，格式如 APA 或 BibTeX。弹层是覆盖在页面上的小卡片。署名栏是文档上的作者名单。依赖是构建所依赖的外部组件。

PR #480 在 `/#cite` 加了一张引用卡片。三种格式一键可取：APA、BibTeX 和引用文件。卡片装的是固定文字，所以数据还没加载就能打开；浏览器拒绝剪贴板权限时，会改为选中引文并提示用户。

PR #482 在 `/#cli` 加了 CLI 设置弹层。仪表盘上的读者可以直接打开弹层，复制那一段交给编码智能体的提示词，不用离开网站去 README 里找。两张弹层共用一套复制控件和一个剪贴板处理器。

PR #484 让搜索默认翻遍所有日期。新查询不再继承最新一次扫描的结果；第一行结果会说明搜的是整个档案，给出回到今天的直达链接，超过十条的结果集则指向 CLI 设置做完整导出。

PR #489 把 Junjie Zhou 加进技术报告草稿的署名栏，保留 Koutian Wu 为通讯作者，并加了一个「下一稿」构建开关，拒绝覆盖已发布的 PDF。PR #485 和 PR #486 升级了 CI 里用的 checkout 与 setup-python 两个 action。

为什么要在意

没法被引用的项目，就是没法被感谢的项目。把引用放在页面上、放在数据旁边，就堵住了参考文献里把这份工作漏掉的所有借口。

离线路径一直有文档，但找不到入口。仪表盘里的一张设置卡补上了这个缺口；覆盖整个档案的搜索能回答任何一天的问题，而不是只回答最近一天。

解决的问题

- `/#cite` 引用卡片：APA、BibTeX 和引用文件三种格式
- #481：搜索默认覆盖全部日期
- `/#cli` CLI 设置弹层
- #489：技术报告草稿署名栏加入 Junjie Zhou
- #485 与 #486：升级 GitHub Actions 依赖
- 记分牌：130 / 1000 星，25 个 fork

第三十八天：仪表盘保持原样，而每个基准和每日简报都有了搜索引擎能读的页面。

> 想跟进 Benchmark Radar？[在 GitHub 上 Star 仓库](https://github.com/ktwu01/benchmark-radar) 获取每日更新，或 [打开实时仪表盘](https://benchmark-radar.org/) 浏览扫描结果。阅读论文：[arXiv:2609.11115](https://arxiv.org/abs/2609.11115)。