---
title: "AI 写 PR 前，先让人回答"
date: 2026-10-11
permalink: /zh/posts/2026/10/agent-pr-gate/
tags:
  - open-source
  - AI-agents
  - maintenance
---

一个账号，10 天给 benchmark-radar 提了 **58 个 PR**，最后合并了 5 个。我把贡献规则整理成了 [agent-pr-gate](https://github.com/ktwu01/agent-pr-gate)，方便其他维护者复制：AI agent 开始写 PR 前，先问使用它的人四个问题，等人回答后再动手。

> 作者：[Koutian Wu](https://www.linkedin.com/in/ktwu01/)；[GitHub: ktwu01](https://github.com/ktwu01/)

[维护记录](https://github.com/ktwu01/benchmark-radar/blob/main/CONTRIBUTING.md#a-real-example-of-a-flood)附了 PR 链接，也记下了提交最密集的时候：27 秒里来了 8 个 PR。合并的 5 个修复了数据被悄悄丢掉的问题，或报告里确实出现过的错误。剩下的 PR 也得有人花时间判断。

生成一份补丁很便宜。判断这份补丁值不值得收，仍然需要一个了解项目的人。

## 先问清楚谁需要这个改动

规则要求贡献者回答：

1. 我真正想要什么结果？
2. 决定这个结果的最关键变量是什么？
3. 今天这件事能改变那个变量，还是只让我觉得自己很忙？
4. 客户是谁，他们真正想要什么？

人必须亲自回答。Agent 不能代写一套看起来合理的答案，也不能把任务要求当成答案。它只追问还没回答的问题，等人答完再开始写 PR。这里的客户可以是用户，也可以是负责审查和长期维护改动的人。

我想让贡献者在提交补丁前，先想清楚谁会受益。有证据的真实 bug，修了当然有用。为了写补丁而设想出来的问题，可以先放一放。

## 把规则复制到自己的项目

[agent-pr-gate 的 CONTRIBUTING.md](https://github.com/ktwu01/agent-pr-gate/blob/main/CONTRIBUTING.md)包含这些问题和贡献规则。可以直接复制，再按自己的项目调整，也可以把这句话交给 agent：

```text
help me copy and paste https://github.com/ktwu01/agent-pr-gate/blob/main/CONTRIBUTING.md into our CONTRIBUTING.md
```

采用前先读一遍。里面除了四个问题，还要求修改规则时提供实际问题的证据。仓库用 CC0 1.0，允许自由修改，不要求署名，也不用装 bot 或依赖。

它能起作用的前提，是 agent 会读并遵守仓库里的指令。忽略指令的人仍然可以提交 PR。benchmark-radar 另有一条限制：每个作者同时打开的 issue 和 PR 合计最多 10 个，维护者除外。这条数量限制和提问规则是两回事。

我还没有测量这些问题能否减少 PR 数量，或提高合并率。目前它是一份有具体来由、其他维护者也能试用的贡献规则。

这个想法受 [@ycaophysics](https://x.com/ycaophysics) 启发。如果你的审查队列也遇到了同样的问题，可以[去 agent-pr-gate 复制这份规则](https://github.com/ktwu01/agent-pr-gate)。
