---
title: 'Crypto Dashboard：AI 驱动的实时加密货币分析工具'
date: 2025-10-17
permalink: /zh/posts/2025/10/crypto-dashboard/
tags:
  - crypto
  - dashboard
  - ai
  - typescript
  - react
  - bitcoin
  - ethereum
  - market-analysis
---
大多数加密货币仪表盘要么把你淹没在数字里，要么把信号藏在付费墙后面。Crypto Dashboard 是我对一种简洁、由 AI 增强的市场视图的尝试，而且它完全运行在你的浏览器里。[试试在线演示](https://ktwu01.github.io/crypto-dashboard/)

> 作者：[Koutian Wu](https://www.linkedin.com/in/ktwu01/)；[GitHub: ktwu01](https://github.com/ktwu01/)

[![GitHub stars](https://img.shields.io/github/stars/ktwu01/crypto-dashboard?style=social)](https://github.com/ktwu01/crypto-dashboard/stargazers) [![GitHub forks](https://img.shields.io/github/forks/ktwu01/crypto-dashboard?style=social)](https://github.com/ktwu01/crypto-dashboard/fork) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://github.com/ktwu01/crypto-dashboard/issues)

## 我为什么做它

我想要一个单一的地方，让我不用同时切换五个标签页，就能扫一眼价格动向、成交量和市场情绪。我还希望这个仪表盘能*自己解释自己*，所以我加了一层 AI，用通俗的语言概括图表正在展示的内容。

核心理念：一个仪表盘应当回答"现在正在发生什么、我该不该在意？"，而不是仅仅画出蜡烛图。

## 亮点

- **比特币、以太坊和主要山寨币的实时市场数据**，实时刷新。
- **AI 生成的评论**，把原始价格走势转写成一段话解读。
- **简洁的 TypeScript + React 技术栈**，演示无需后端。
- **以 MIT 许可开源**，你可以 fork 并接入自己的模型或数据源。

## 一分钟试用

打开在线演示：[https://ktwu01.github.io/crypto-dashboard/](https://ktwu01.github.io/crypto-dashboard/)。无需注册、无需连接钱包、无追踪。

## 技术栈

- **前端：** React、TypeScript、Vite
- **图表：** 为加密货币蜡烛图调优的轻量级图表库
- **数据：** 公共加密货币价格 API
- **部署：** GitHub Pages

## 使用场景

- 交易日开始时快速扫一眼加密货币市场。
- 为任何想构建自己加密货币交易面板的人提供一个参考前端。
- 作为 AI 增强型数据仪表盘的教程示例。

## 参与贡献

如果你有心中想做的功能（更多币种、不同的时间区间叠加、情绪评分），欢迎在[仓库](https://github.com/ktwu01/crypto-dashboard)提交 issue 或 PR。这个项目够小，一个聚焦的 PR 能很快落地。

---

这个仪表盘是我自己想要的那种工具。如果你觉得它有用，给仓库点一个 star，能帮助更多人找到它。