---
title: "Atomize: Building a Task-Breaking Agent System Inspired by Goblin Tools"
date: 2026-01-09
permalink: /posts/2026/01/atomize-task-breaking-agent-system/
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
> [Yuxuan](https://www.linkedin.com/in/yuxuan-cao-4b235110b/) and I have been discussing AI agent ideas for a while. Yesterday, we finally decided: we're building **Atomize**, a task-breaking agent system evolved from [Goblin Tools](https://goblin.tools/).

## The Spark: Goblin Tools

[Goblin Tools](https://goblin.tools/) is a fantastic collection of small, simple AI tools designed for when things feel too big or complicated. Their **Magic ToDo** feature breaks down tasks into manageable subtasks—exactly what people with ADHD or executive dysfunction need.

But we see a bigger opportunity here.

## Why Atomize?

The core insight is simple: **breaking down complex tasks into atomic subtasks is the foundation of effective AI agents.**

Goblin Tools does this for humans. We want to build a system that does this for AI agents AND humans, with a more sophisticated architecture under the hood.

## The Architecture (For Founders & Developers)

End users don't need to know this, but as founders and developers, we need to understand the underlying system:

![Meta Agent Architecture](/images/atomize-meta-agent-architecture.png)
*Source: [arXiv 2407.15734](https://arxiv.org/abs/2407.15734)*

The key components:

1. **Meta Agent** - Receives the main task and orchestrates the breakdown
2. **Subtask Distribution** - Routes subtasks to appropriate handlers:
   - Direct **Function Calls** for simple operations
   - **Inner Agents** for more complex subtasks
3. **Shared Memory** - Context and state passed between agents
4. **Task Completion** - Results aggregated and stored

This architecture allows for:
- Recursive task decomposition
- Context preservation across subtasks
- Parallel execution where possible
- Memory-efficient handling of complex workflows

## What We're Building

**Atomize** will take the user-friendly simplicity of Goblin Tools and combine it with:

- A robust meta-agent architecture for complex task handling
- API-first design for developers
- Open-source core with premium features
- Integration with existing productivity tools

## The Journey Begins

We've talked about this idea multiple times but kept going back and forth. Yesterday, we finally committed. The decision crystallized when we realized:

1. The problem is real (everyone struggles with overwhelming tasks)
2. The solution exists in fragments (Goblin Tools proves the UX)
3. The technology is ready (LLM agents have matured)
4. We have complementary skills to build this

Stay tuned for updates on our progress.

---

**Co-founder:** [Yuxuan Cao](https://www.linkedin.com/in/yuxuan-cao-4b235110b/)

**Inspiration:** [Goblin Tools](https://goblin.tools/)

