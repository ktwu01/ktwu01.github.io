---
title: "Benchmark Radar 第二十五天：分数落在它们所属的日期上，一个不再推荐自己的雷达"
date: 2026-08-20
permalink: /zh/posts/2026/08/benchmark-radar-day25/
tags:
  - AI
  - Benchmarks
  - Scoring
  - Date Axis
  - Identity
  - Feeds
  - Plain English
---

一个推荐自己的雷达不是雷达。第二十五天让排名不再自我博弈，让爬取分数落在它们所属的日期上，并让一个无人评分的基准为自己作答。

> 作者：[Koutian Wu](https://www.linkedin.com/in/ktwu01/)；[GitHub: ktwu01](https://github.com/ktwu01/)

## 今日交付

**雷达不再推荐自己。** PR #291 交付评分 v4：`ktwu01/benchmark-radar` 从自己的排名中排除。它的描述通篇是基准词汇且每日提交，因此相关性与新颖性把它在首 27 个采集日中的 9 天推入前五。排除以精确的 owner/name 对匹配，绝不用子串，所以 `H20Zhang/Agent-Benchmark-Radar` 这样的真实记录保持原位。

**下载量封顶。** 评分 v4 同时封顶下载量：一个有 25,238 次下载和 1 个赞的数据集得了 88.0 分，从 3,265 星的仓库手里抢走了第二名。封顶阻止原始下载量压过真实的采纳信号。

**爬取分数落在它们的日期上。** PR #290 修复 #279：全部 5,544 行爬取分数都带 `announcement_date`，而规范化器一直把它丢弃。排行榜前沿图现在按发布日期而非分数排序，`?view=leaderboard&lfrontier=llm-stats-aime-2025` 不再画出看起来像进展、其实只是排序列表的光滑斜坡。

**无人评分的基准为自己作答。** PR #289 修复 #287：`?view=leaderboard&lfrontier=rsi_bench` 在 URL 仍写着 `rsi_bench` 的情况下画出了 AutomationBench 的图。RSI-Bench 尚无采纳者，所以采纳者筛选先于守卫把它过滤掉了。守卫现在先于筛选运行。

**RSI-Bench 在无人评分前入册。** PR #285 以采纳数零把 RSI-Bench 加入注册表。这个零是一种读数，而非爬取的缺口：没人评分的基准恰恰是读者无法通过任何其他途径找到的那个。条目携带名称、流通别名、发布方、发布日期，以及供第一张报告它的卡片解析的 id。

**搜索找到基准。** PR #284 修复 #245 的搜索半部：`?q=` 现在也查询注册表，而不仅仅是每日源。`?q=researchclawbench` 与 `?q=terminal-bench` 现在能找到真实记录，而此前搜索框根本无法触达注册表。

**四个无日期基准补上日期。** PR #294 修复 #292：四个 `released: null` 的基准其实都有自己的论文。ExploitBench（arXiv 2605.14153）、BlueprintBench 2（发布博客）、BioMysteryBench（Anthropic 公告）与 VIBench（CAIS '26）现在都有了日期，全部 80 个注册表基准均已注明日期，年代筛选也可以专门询问无日期条目。

**19 个 llm-stats 基准的复核身份。** PR #295 关闭 #265：`data/external/llm_stats_identity_overrides.yml` 记录了 50 个分数密集基准中锚定两次的 19 个的手工复核身份，包括 SWE-bench Verified/Pro/Multilingual、HLE、MMMU-Pro 与 Terminal-Bench 1.0/2.0/2.1。其余 31 个在找到第二个锚点前保持空白，因为错误的发布方或许可证比诚实的空白更糟。两个错误的爬取值被修正而非照搬。

**经核验的第一方订阅源。** PR #296 关闭 #264：九个 RSS/Atom 订阅源被收入 `config.yml` 的 `sources.first_party_feeds.feeds`，每个都重新核验可解析且至少带一条有标题的条目：Qwen、Ollama、Stability AI、Nomic AI、Replicate、NVIDIA Developer、IBM Research、Databricks、LangChain。由于 Qwen 订阅源最新一条是 2025-09-23，它为 Qwen 增加了搜索兜底。

**术语归零。** PR #281 与 #282 关闭 #276：七个只在项目内成立的术语换成平实英文，Pareto 就绪面板、`site/logos.html` 与中文译文的最后五处命中全部重写。原本报告 25 处命中的审计现在为 0。

**测试导入所在检出目录的源码。** PR #297 在 pytest 配置中加入 `pythonpath = ["src"]`，使工作树中的测试运行测量的是所在分支，而非已 pip 安装的检出目录。

## 为什么重要

自我推荐的修复保护排名的可信度。一个在读者眼皮底下把自己排到第 2 的排行榜，会教会读者怀疑页面上每一个数字。把雷达从自己的排名中排除不是自贬，而是排名有意义的前提。

日期轴修复改变了一张图的断言。把按分数排序的列表画成平滑斜坡，等于宣称「随时间进展」，而它其实只是一张排序表。让 5,544 行爬取分数落在它们的发布日期上，是让数据自己说话，而非替它编造说法。

RSI-Bench 的一系列修复让注册表与图表之间的回路闭合。在无人评分前记录一个基准，并让无人评分的基准为自己作答，意味着你读到的永久链接就是你得到的基准。身份覆写在数据层做同样的事：诚实的空白胜过自信的错误值。

## 解决的问题

- \#244：RSI-Bench 新基准
- \#245：搜索找到基准
- \#264：第一方厂商订阅源
- \#265：llm-stats 身份覆写
- \#276：术语审计归零
- \#278：自我推荐与下载量封顶
- \#279：爬取分数的 announcement_date
- \#287：无人评分的基准画出自己的图
- \#292：无日期注册表基准
- 含自我排除的评分 v4
- 日期排序的前沿图
- 九个经核验的第一方订阅源
- 19 个基准的身份覆写
- Pytest 工作树导入修复

第二十六天：前沿曲线与返回按钮的回归。