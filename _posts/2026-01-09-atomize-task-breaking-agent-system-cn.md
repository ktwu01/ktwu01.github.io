---
title: "Atomize：受 Goblin Tools 启发的任务分解 Agent 系统"
date: 2026-01-09
permalink: /posts/2026/01/atomize-task-breaking-agent-system-cn/
tags:
  - AI Agent
  - LLM
  - Startup
  - Product
  - Productivity
  - Open Source
---

> TL;DR
>
> 我和 [Yuxuan](https://www.linkedin.com/in/yuxuan-cao-4b235110b/) 讨论 AI Agent 的想法已经有一段时间了。昨天，我们终于做出了决定：我们要做 **Atomize**，一个从 [Goblin Tools](https://goblin.tools/) 演化而来的任务分解 Agent 系统。

## 灵感来源：Goblin Tools

[Goblin Tools](https://goblin.tools/) 是一个非常棒的小型 AI 工具集合，专为那些觉得事情太大或太复杂的时候设计。它的 **Magic ToDo** 功能可以将任务分解成可管理的子任务——这正是有 ADHD 或执行功能障碍的人所需要的。

但我们看到了更大的机会。

## 为什么做 Atomize？

核心洞察很简单：**将复杂任务分解为原子级子任务是有效 AI Agent 的基础。**

Goblin Tools 为人类做这件事。我们想构建一个既能为 AI Agent 也能为人类服务的系统，底层有更复杂的架构。

## 架构设计（给创始人和开发者看的）

终端用户不需要知道这些，但作为创始人和开发者，我们需要理解底层系统：

![Meta Agent 架构](/images/atomize-meta-agent-architecture.png)
*来源：[arXiv 2407.15734](https://arxiv.org/abs/2407.15734)*

关键组件：

1. **Meta Agent** - 接收主任务并协调分解
2. **子任务分发** - 将子任务路由到适当的处理程序：
   - 简单操作直接调用 **Function Call**
   - 更复杂的子任务交给 **Inner Agent**
3. **共享内存** - 在 Agent 之间传递上下文和状态
4. **任务完成** - 结果聚合并存储

这种架构允许：
- 递归任务分解
- 跨子任务的上下文保持
- 尽可能并行执行
- 内存高效处理复杂工作流

## 我们在构建什么

**Atomize** 将结合 Goblin Tools 用户友好的简洁性，以及：

- 用于复杂任务处理的健壮 Meta Agent 架构
- API 优先的开发者设计
- 开源核心 + 高级功能
- 与现有生产力工具的集成

## 旅程开始

我们已经讨论这个想法很多次了，但一直在来回犹豫。昨天，我们终于下定决心。当我们意识到以下几点时，决定就明确了：

1. 问题是真实的（每个人都在与压倒性的任务作斗争）
2. 解决方案以碎片形式存在（Goblin Tools 证明了用户体验）
3. 技术已经成熟（LLM Agent 已经成熟）
4. 我们有互补的技能来构建这个

敬请关注我们的进展更新。

---

**联合创始人：** [Yuxuan Cao](https://www.linkedin.com/in/yuxuan-cao-4b235110b/)

**灵感来源：** [Goblin Tools](https://goblin.tools/)

