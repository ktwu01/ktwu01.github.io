---
title: "Benchmark Radar 第十三天：仪表板美化与证据溯源"
date: 2026-08-08
permalink: /zh/posts/2026/08/benchmark-radar-day13/
tags: [benchmark-radar, dashboard, evidence-grounding, qa, openalex]
---

第十三天的重点是让仪表盘更好看，并且把每条结论都说得有凭有据。

> 作者：[Koutian Wu](https://www.linkedin.com/in/ktwu01/)；[GitHub: ktwu01](https://github.com/ktwu01/)

大家好，我是 Koutian。先说两个词。favicon 是浏览器标签页上那个小图标。OpenAlex 是一个收录论文和作者的数据库。证据溯源（evidence grounding）指的是每条结论都能追回到原始数据，你自己能去核对。

第十三天做了这些。

我们给仪表板加了 favicon。

URL 参数的作用域修好了。

仪表板现在有「每日问答」功能了。你能直接问它问题，它会回答。

简报的证据溯源做完了。以前大约 80% 的证据都被丢掉，现在找回来了。每条简报的结论都能链回具体证据。

KW-Bench 的评分标准现在放进仓库里管理了。

我们启动了一项「基准测试构建者」调研。

轨迹上的数据点现在可以单独检查了。

联系人清单整理完了。

OpenAlex 里空标题的问题修好了。

为什么重要。

证据溯源是这次最要紧的改动。如果一个雷达系统说「基准测试 X 正在升温」，却拿不出数据来源，那它说的其实只是自己的看法。现在每条简报的结论都能追到一条证据链，你可以自己验证。每日问答让仪表板能主动解释。它把数据摆出来，同时回答你可能想问的常见问题。

解决掉的 issue：

- Issue #160
- Issue #161
- Issue #162
- Issue #159
- Issue #163
- Issue #164
- Issue #166
- Issue #167
- Issue #168
