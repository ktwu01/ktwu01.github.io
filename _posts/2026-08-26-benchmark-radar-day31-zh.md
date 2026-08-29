---
title: "Benchmark Radar 第三十一天：一行摘要的发布卡片、两项必填的 Issue 表单、读得下去的 README"
date: 2026-08-26
permalink: /zh/posts/2026/08/benchmark-radar-day31/
tags:
  - AI
  - Benchmarks
  - Open Source
  - Data Plumbing
  - i18n
  - Plain English
---

Benchmark Radar 的第三十一天。每张发布卡片现在都带一行摘要，而不是一个光秃秃的版本号；提交 issue 最多填两个必填项；两份 README 也精简到读得下去。记分牌：107 颗星，20 个 fork。

> 作者：[Koutian Wu](https://www.linkedin.com/in/ktwu01/)；[GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar 已上线。** 每天追踪新的 AI 基准测试、数据集与排行榜：[打开仪表盘](https://benchmark-radar.org/) 或 [在 GitHub 上 Star](https://github.com/ktwu01/benchmark-radar)。

发布卡片是某个基准新版本的条目。裸标签就是版本号本身，比如 `v1.11.0`，读者看不出这次改了什么。必填项是提交表单前必须填写的输入框。sighting 是雷达某次扫描中看到一条记录。

PR #383 修复了把发布标题解析成裸标签的 bug。`modelscope/evalscope@v1.11.0` 之前被命名为 `v1.11.0`，卡片读起来像版本号而不是发布。PR #385 随后回填了剩余的 10 个裸标签标题，覆盖八个每日快照中的六个 EvalScope 和 MTEB 发布，并把所有修正和未来的记录打上 `github-releases/2` 标记，同时保留原始载荷哈希。现在每张发布卡片都有一行可扫读的摘要。

PR #387 修复了 All dates 视图。它过去会把同一条记录在每次重叠扫描里重复展示，所以 `modelscope/evalscope@v1.11.0` 因为两天的 sighting 出现了两次。现在每个源记录只显示最新一次匹配的 sighting。单个日期视图、每日快照和趋势计算保留完整历史。

PR #389 和 PR #394 简化了 issue 模板。报 bug 现在只需一个必填项（发生了什么），提新功能两个（加什么、为什么），使用案例两个，模型卡片两个。真正的拦路虎是框外的说明文字，所以每个标签和描述都改成一行，报 bug 文案从 516 字压到 240 字，新功能从 619 压到 324。PR #394 还加了空状态恢复清单，页面没有匹配记录时告诉读者下一步做什么。

PR #390 把站点和 README 测试夹具里的 61 处中文词「基准」替换成 benchmark，因为注册表和分类法用的是英文术语。现在有一条回归测试，出现「基准」就失败。

PR #393、#395、#397、#398 让 README 值得打开。主 README 精简了，徽章标签变短，展示图换成 SWE-bench Verified 动图，新增的 See the dashboard 区块用中英文各一行说明展示 Today 和 Leaderboard 页面。

PR #399 修复漏掉的 arXiv 基准并公开卡片元数据。SWE Refactor Bench（`arXiv:2608.23564`）之前完全缺失，因为摘要里基准名写作 `Bench:`，而且没有采集 `cs.SE` 这个源。雷达现在能抓带 `Bench:` 的发布，纳入 `cs.SE`，并改在 UTC 凌晨 4 点 arXiv 公报之后运行，当天的投稿不会再晚一个扫描周期。卡片现在显示源提供的作者、机构、发布日期和活跃计数，真实零值和缺失计数区分开。

PR #400 是三个小的一致性修复：`.env.example` 补上每日工作流已经在用的 OpenReview 凭据说明，OpenReview 工作流文件补上结尾换行，包版本统一对齐到 0.8.0。

为什么要在意

标题只有裸标签的发布，看起来和普通版本升级没区别。一行摘要让卡片可扫读，回填旧条目让档案保持诚实，而不是只修未来。

填两项的表单才会有人填，像文书的表单不会。砍的是文案而不是输入框，模板才既能保持完整又能变快。

静默的数据错误才是最贵的。一条记录重复展示两次，或一个发布完全漏掉，读者看不出异样。这一批每个修复都带回归测试，下次改动没法悄悄带回同样的错误。

解决的问题

- #362：发布标题被解析成裸版本号，已修复并回填
- #357：两份 README 展示 Today 和 Leaderboard 页面
- #374：中文翻译里的「基准」全部换成 benchmark，带回归测试
- #386：空状态页面加上恢复清单
- #388：issue 模板最多两个必填项
- #361：基准卡片公开元数据（作者、机构、日期、活跃计数）
- #389：加入带 `Bench:` 的处理和 `cs.SE` 源后找到 SWE Refactor Bench
- 记分牌：107 / 1000 星，20 个 fork

第三十二天：一个发布没有任何二进制文件也能算采纳的排名。

> 想跟进 Benchmark Radar？[在 GitHub 上 Star 仓库](https://github.com/ktwu01/benchmark-radar) 获取每日更新，或 [打开实时仪表盘](https://benchmark-radar.org/) 浏览扫描结果。
