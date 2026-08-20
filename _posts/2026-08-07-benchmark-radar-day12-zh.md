---
title: "Benchmark Radar 第十二天：每日 RSS 订阅源"
date: 2026-08-07
permalink: /zh/posts/2026/08/benchmark-radar-day12/
tags: [benchmark-radar, rss, github-pages, subscriptions]
---

雷达现在能订阅了。第十二天，我们加了一个每天更新的 RSS 订阅源。

> 作者：[Koutian Wu](https://www.linkedin.com/in/ktwu01/)；[GitHub: ktwu01](https://github.com/ktwu01/)

大家好，我是 Koutian。先说两个词。RSS 是一种订阅方式，你把它加到自己的阅读器里，有更新就会自动收到。GitHub Pages 是 GitHub 提供的免费网页托管，网站就挂在上面。

第十二天做了这些。

我们做了一个每日 RSS 订阅源，内容根据每天的快照历史生成，已经作为 GitHub Pages 的产物发布了。它输出的是机器可读的格式。

为什么重要。

RSS 是摩擦最小的订阅方式。它不用配邮件服务器，不用搭 webhook，也不依赖任何第三方推送服务。基准测试的更新时间本来就不规律，RSS 刚好合适：你在自己的阅读器里刷新一下，就能拿到最新内容。订阅源输出成机器可读格式，也给以后接自动化打下了基础。

解决掉的 issue：

- Issue #157
