---
title: '弄了一份全屏幻灯，专门讲 Claude Code 和几个真干活场景'
date: 2026-05-10
permalink: /posts/2026/05/claude-code-demo-deck/
tags:
  - Claude Code
  - Claude
  - demo
  - vibe-coding
  - skills
  - agent
---
打开浏览器全屏，左右键翻页，不用 Keynote 也能把 Claude Code 从终端一路演示到浏览器 Computer Use。

> 作者：[Koutian Wu](https://www.linkedin.com/in/ktwu01/)；[GitHub: ktwu01](https://github.com/ktwu01/)

仓库根目录下的 `2026-05-09-claude-code-demo.html` 是自包含全屏幻灯，点屏幕左三分之一或右三分之一也能翻页，不挂 Jekyll，拖进浏览器就能讲。

我把上一版文件名里含糊的 tacit 去掉了，页面标题也改成「Claude Code Demo」，跟这场演示的主角对齐。

第一张片子直接承认一件事，我还在同时叠好几套 vibe coding 栈，Cursor 学生额度加 Gemini CLI 之类凑在一起也常常不够烧。这块我当时写过一篇更细的 IDE 对比，Cursor、Kiro、Antigravity 各有什么性格，你可以在 [这篇 vibe coding IDE 简报](https://ktwu01.github.io/posts/2025/12/vibe-coding-ides-brief-comparison/)里慢慢翻。

幻灯正文从第二场开始往后排了五个我平时真在用的场景。第一场是 Claude Code 在终端里从读仓库到跑测试、`git commit`、再用 `gh pr create` 把 PR 甩出来。第二场是把重复流程收成 Claude Code Skills，像 `buffett-check`、`hedge-review`、`redteam` 这种标签能一键拉起来，团队对齐口径会轻松很多。

后面几场顺着往业务侧摊开，公司内部知识检索、浏览器扩展 Computer Use（例如 LinkedIn 上那点重复点击的活），再到本仓库里 YAML 持仓加 skill 出 HTML dashboard 的那条路。每一页只讲一个场景，现场要展开哪一页就停在哪一页。

坦率的讲，这份东西不是教程，也不是什么完整产品路演，就是一页一页把「我平时到底怎么用 Claude 把活儿干完」摊在桌面上。你如果也在多 IDE、多 CLI 之间切来切去找额度，先看看上面那篇 IDE 对比，再打开这份 HTML，说不定能省掉几次「我跟别人解释我在干什么」的口水。

在线直接打开可以这样拼 URL，把域名换成你自己的 GitHub Pages 域名即可，`https://ktwu01.github.io/2026-05-09-claude-code-demo.html`。
