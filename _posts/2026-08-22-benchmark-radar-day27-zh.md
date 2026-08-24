---
title: "Benchmark Radar 第二十七天：今日列表分页、标题减半、21 个基准正名"
date: 2026-08-22
permalink: /zh/posts/2026/08/benchmark-radar-day27/
tags:
  - AI
  - Benchmarks
  - Today View
  - Pagination
  - i18n
  - SEO
---

一天 136 条还要一次全画出来，只会让首屏变慢。第二十七天我们做了三件事：让今日列表一页页加载，把标题砍半，让 21 个基准显示真名。先说几个词：分页是一长串内容分多页看完；首包是页面为了快而先加载的小数据包；SEO 是让搜索引擎看懂并收录网站的做法。

> 作者：[Koutian Wu](https://www.linkedin.com/in/ktwu01/)；[GitHub: ktwu01](https://github.com/ktwu01/)

PR #315 给今日列表加分页。以前首屏要把当天全部观察全画出来，浏览器既要取完整数据又要一次性渲染。现在首屏只画 20 张卡片，列表底下放一个岗哨。滚到底附近就地追加下 20 张，已展开的卡不收起，排名跨页连续。底部状态行写已加载多少、共多少，例如 20 of 136，scroll for more。图例精简到 136 normal、9 attention 加一句排序说明，重复的原始总数删掉。导出徽标、弹窗和前端 CSV 拼装也删掉，需要全量数据的去联系页索取。

PR #317 给饱和度视图加了自左向右的入场。最好成绩线自左向右展开，每个点在动画扫过其日期时淡入。截至该日期仍保持最好值的点保持强调，其余点退到线后，悬停或聚焦时再显现。成员来自同一份按日期的最佳值归并，限于该线所属的可比分组，且只在线实际要画时才生效。入场是表现层，而强调规则是数据驱动的。

PR #319 把排行榜标题砍半。原来 48px，把排名和图往下推。现在是 `clamp(1.25rem, 2vw, 1.5rem)`，大约一半，首屏回到排名。蓝色 (i) 信息开关不再飘在几百像素外；标题和开关同一行 flex 排布，窄屏自动换行。

PR #320 给排名加表头和横条。以前五行没有标签，左边是名次还是数量得靠猜。现在表头写 Rank、Benchmark、Model cards。每行还画一条以屏内最大值为基准的横条，GPQA Diamond 26 对 AIME 17 的差距一眼可见。笨重的全大写带框 SHOW ALL 换成更轻的展开收起，在前 5 与全部 79 之间切换。

PR #321 翻译基准详情面板。Identity、Publisher、Modality、Openness、Size、Code/Data licence 这些节标题，以及所有 not established 占位，都走 `t()` 并补齐 `zh` 条目。以前只有 Released 有中文，其余回落到英文，面板中英混排。切到中文后现在整块都是中文。

PR #323 关掉 #262。76 个分数密集的 `llm-stats` 基准里 21 个显示 publisher not established，只因 `llm-stats` API 本来就不带出处，而同一轮抓取里 OpenCompass 已有同名记录，且带有论文、仓库、数据集、发布方和发布日期。这 21 个现以 equivalent 组写入 `data/external/identity.yml`，加载时让 `llm-stats` 记录显示其已审核同伴的身份。其余记录在拿到第二个锚点前仍不硬连。

PR #328 修了首包。PR #327 为让首屏变快，把首包换成精简的 bootstrap，并把完整的 34MB 数据懒加载给趋势和全量日期视图。但 `dashboard_bootstrap()` 把 `benchmark_score_progression` 也从首包里清掉，理由是历史只和全量一起用，不是。排行榜的 Scores over time 面板正好读这块，于是每访必显 No benchmark in this registry has a score read from a document yet。现在首包重新带上这段进展，`stateNeedsFullData()` 仍只在趋势、地图和历史今日视图时才升级到 `radar.json`，排行榜不再需要。

PR #327 还落地了首屏和传播改动：带岗哨的分页、稳定的联系与评分细则链接、合理的 star 与分享提示、引用元数据，以及文档里的公开下游用例模板。

PR #325 补上 #236 的机械 SEO。生成式 `sitemap.xml` 覆盖所有可索引视图，加上 `robots.txt`、每页互不相同的标题与描述、Open Graph 与 `twitter:image`、规范链接，以及 `Dataset` 与带 `SearchAction` 的 `WebSite` 的 JSON-LD。未新增内容或关键词 targeting，只是让爬虫读到已有的东西。

为什么要在意

分页让稠密日子仍可用。136 张一起画不会更清晰，只会让可用时间更晚。一次 20 张、岗哨续载，既保住滚动位置也保住已打开的卡。

给 21 个基准正名，是在身份层补上本就有的联系。一个 publisher not established 若只是因为某个 API 本来不带出处，就不该当缺口展示，而是把同名、已有论文与仓库的另一来源连过去，让记录用对的出处说话。

标题、横条与翻译，是让阅读无需猜。标题减半把首屏还给数据；横条让 26 对 17 的差距不用在脑内比数；详情面板全量翻译，让语言切换真的切换整页。

解决的问题

- #311：今日列表每次 20 条、就地续载
- #312：饱和度线自左向右展开、按数据强调
- #313：排行榜标题减半、信息开关锚定
- #314：排名加表头、横条、轻量展开
- #316：基准详情面板完整中文化
- #262：21 个 `llm-stats` 身份经 OpenCompass 同名对齐
- #236：生成式 sitemap、`robots.txt`、规范链接与结构化数据
- #322：首包首屏加懒加载全量、分页与引用元数据
- #328：排行榜 Scores over time 在首包中恢复

第二十八天：数据只剩一个真相来源，页面只剩一个 `h1`。
