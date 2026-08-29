---
title: "Benchmark Radar 第二十八天：数据只剩一个真相来源，页面只剩一个 h1，引用一键可复制"
date: 2026-08-23
permalink: /zh/posts/2026/08/benchmark-radar-day28/
tags:
  - AI
  - Benchmarks
  - Data Plumbing
  - i18n
  - SEO
  - Citation
---

别给同一份真相留两个副本，否则它们迟早对不上。第二十八天我们做了三件事：把可生成的数据移出版本库，让页面只对爬虫说一个标题，给作品一个可引用的名字。先说几个词：真相来源是唯一可信的那份源文件，其余都由它生成；`h1` 是页面的主标题，爬虫期望整页只有一个；`i18n` 是国际化，让界面按语言显示；引用是你写论文时粘贴的那条参考文献。

> 作者：[Koutian Wu](https://www.linkedin.com/in/ktwu01/)；[GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar 已上线。** 每天追踪新的 AI 基准测试、数据集与排行榜：[打开仪表盘](https://benchmark-radar.org/) 或 [在 GitHub 上 Star](https://github.com/ktwu01/benchmark-radar)。

PR #337 移除可生成的分片。`site/data/benchmark-index.json` 与 `site/data/benchmarks/` 里的 1,148 个文件，本就是 `benchmark-radar normalize-external` 从已入库的抓取 CSV、`data/leaderboard_snapshots.yml` 与 `data/external/identity.yml` 生成的。它们又被提交了一次，仓库里就有两份同一目录。直接在 `main` 上重跑，会改写 50 个已漂移的分片。现在它们被 gitignore，改为在 CI 里生成。全新检出会先生成再让下游读取，模型注册表在分片缺失时直接拒绝写入。不再用提交去复制真相。

PR #329 润色文档。两份 README 都把语言切换挪到标题右上角，改成直白标签 `[中文](README.zh-CN.md)` 与 `[English](README.md)`，不再是文件名样式。两份都新增 Acknowledgements 致谢，说明前沿分数的数据源是 `llm-stats`，AIME 2025 图表即基于 `llm-stats.com`。两份都在末尾加上 BibTeX，`Wu 2026`，指向 `CITATION.cff` 的机器可读元数据。首页支援卡也改成提醒可引用，头部新增 Cite 按钮，一键可得引用。

PR #331 补齐 26 条缺失的 `zh` 并修 SEO。所有 `t()` 调用点对 `zh` 词典做审计，剩余缺口归零，覆盖 `not scored`、`not recorded`、相关记录标签、基准详情的加载与错误文案、饱和度边界文案、采纳排名说明、徽标提示、分页、star、fork、issue 徽标。SEO 上，页面现在只有一个 `h1`，Today's radar，排行榜、地图、趋势与错误态标题改成 `h2`，视觉不变。以前爬虫会在隐藏视图里看到四个并列 `h1`。`og:title` 现与文档标题一致，站内链接也一并修复，分析仪分数升至 85。

PR #335 把引用元数据升至 `v0.8.0`。`CITATION.cff` 从 `v0.3.0` 升到 `v0.8.0` 并记下发布日期。

PR #331 与 PR #337 也调整了 CI 的工序顺序。`benchmark-radar classify` 与分片生成提前跑，可生成产物不再读陈旧输入。这和读者的使用顺序一致：先小首包，再按需取全量。

为什么要在意

同一目录两份副本，按构造就会漂移，刚才就漂了 50 个。解法不是更仔细地提交，而是只提交来源，即抓取 CSV 与身份文件，其余每次检出与每次 CI 都重新生成。一个真相来源意味着从 `main` 重建的结果，和上次发布说的是同一件事。

一个 `h1` 与一致的 `og:title`，让爬虫听到同一个标题。一次只展示一个视图的页面，也该一次只声明一个主标题。翻译同理：中文下仍剩 26 句英文，意味着语言切换假装切了却留下一半没切。补齐它们，切换才真在切换。

可引用的参考文献，让使用变成署名。对 `llm-stats` 的致谢把分数的出处说清楚，`CITATION.cff` 加 BibTeX 加头部 Cite 按钮，让复用雷达的人有处可引。

解决的问题

- #329：README 语言切换置顶右侧、`llm-stats` 致谢、BibTeX 与首页 Cite 按钮
- #331：26 条缺失 `zh`、单一 `h1`、`og:title` 对齐、站内链接、分析仪 85 分
- `v0.8.0` 引用元数据写入 `CITATION.cff`
- 可生成 `site/data/benchmarks/` 分片移出版本库、在 CI 生成、先于消费步骤构建
- CI 中分片与分类提前于读取步骤执行

第二十九天：发布先于更新、分数落在 0 到 100、导航高亮看得见。

> 想跟进 Benchmark Radar？[在 GitHub 上 Star 仓库](https://github.com/ktwu01/benchmark-radar) 获取每日更新，或 [打开实时仪表盘](https://benchmark-radar.org/) 浏览扫描结果。
