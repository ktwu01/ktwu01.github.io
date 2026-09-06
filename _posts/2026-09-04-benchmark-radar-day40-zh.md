---
title: "Benchmark Radar 第四十天：盯上论文的登记处，找回一个基准，发到更多地方"
date: 2026-09-04
permalink: /zh/posts/2026/09/benchmark-radar-day40/
tags:
  - AI
  - Benchmarks
  - Discovery
  - Social
  - Open Source
  - Plain English
---

Benchmark Radar 的第四十天。雷达开始盯着大多数新基准论文拿到 DOI 的那个网络，靠搜索一个基准的精确名字把它找了回来，并开始向以前没发过的地方发布。记分牌：147 颗星，27 个 fork。

> 作者：[Koutian Wu](https://www.linkedin.com/in/ktwu01/)；[GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar 已上线。** 每天追踪新的 AI 基准测试、数据集与排行榜：[打开仪表盘](https://benchmark-radar.org/) 或 [在 GitHub 上 Star](https://github.com/ktwu01/benchmark-radar)。

DOI 是出版社给论文分配的永久标识符，Crossref 是给大多数论文分配 DOI 的组织。递归自我改进指的是一个致力于提升自身改进能力的系统。清单是每日社媒例行要走的完整排序版目的地与动作列表。

PR #546 把 Crossref 加为可选的每日发现源。雷达现在会去查它最近带 DOI 的基准论文，保留 DOI 身份、作者、单位和引用数，并拒绝格式错误或未来日期的记录。Crossref 不需要 API 密钥，所以这个新源不引入任何机密。

PR #495 找回了 RSI-Exam。这套基准在 88 个任务、六个领域上测试可执行的递归自我改进，但 GitHub 连接器从未搜过它的精确名字，于是它既没被发现，就算直接抓取也不够格发布。一条精确名字查询加一条具名观察名单把它带回来，无关的交易和安全类仓库仍然进不来。

PR #538 和 PR #539 扩大了发布范围。每日社媒 issue 变成完整的排序版牵引清单，覆盖全部 94 个目的地与动作，配 11 个可复用帖子示例。Bilibili 进入每日发布块，WhatsApp Communities、Pinterest、Snapchat 和 Quora 加入面向美国用户的每周渠道。

PR #536 把共享框架精简到核心：RSS、语言、联系方式和星数。PR #537 把 Junjie Zhou 加为各引用表面的第二作者；PR #542 把 Jiayu Wang 已完成的一个真实用例连同六张截图加进报告草稿，并延长了署名栏。

为什么要在意

基准论文在留下大多数其他痕迹之前，就已经用 DOI 宣告了自己。盯住 Crossref 补上了大多数雷达留着的缺口，而且不需要任何凭证。

一个像 RSI-Exam 这样不寻常的基准竟然有发现盲区，这是关于精确名字的一课。仓库靠里面的词被找到，所以一个任何查询都没包含其名字的基准，直到那条查询被写下来之前都是不可见的。

分发也是开源项目工作的一部分。排序版清单让每日发布可以重复，新渠道则触达从不看 GitHub 的读者。

解决的问题

- #506：Crossref 加入为可选的每日发现源
- #408：靠精确名字发现 RSI-Exam
- #412：Bilibili 和面向美国用户的渠道加入清单
- #532：共享框架精简
- #492：报告草稿加入 Jiayu Wang 的真实用例和署名
- 记分牌：147 / 1000 星，27 个 fork

第四十一天：给新鲜发布的排行榜引擎，先定数据契约，再谈改界面。

> 想跟进 Benchmark Radar？[在 GitHub 上 Star 仓库](https://github.com/ktwu01/benchmark-radar) 获取每日更新，或 [打开实时仪表盘](https://benchmark-radar.org/) 浏览扫描结果。