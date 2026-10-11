---
title: "58 PRs in 10 Days: Ask the Human Before the Agent Writes"
date: 2026-10-11
permalink: /posts/2026/10/agent-pr-gate/
tags:
  - open-source
  - AI-agents
  - maintenance
---

One account opened **58 pull requests in 10 days** on benchmark-radar. Five were merged. I put the contribution policy into [agent-pr-gate](https://github.com/ktwu01/agent-pr-gate) so other maintainers can copy it: before an AI agent starts PR work, it asks its human four questions and waits for the answers.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

The [maintainer's account](https://github.com/ktwu01/benchmark-radar/blob/main/CONTRIBUTING.md#a-real-example-of-a-flood) links the PRs and records the bursts, including eight PRs in 27 seconds. The five merged changes fixed silent data loss or a real report bug. The rest of the queue still took attention to sort through.

Generating a patch is cheap. Deciding whether it belongs in a project still takes a person who understands that project.

## Ask before generating the work

The policy asks:

1. What outcome do you really want?
2. What is the highest-leverage variable that determines it?
3. Will this work move that variable, or just keep you busy?
4. Who is the customer, and what do they really want?

The human answers. The agent cannot fill in plausible answers on their behalf, or count the task request as an answer. It asks only the unanswered questions and waits before starting PR work. Here, the customer might be a user or the maintainer who will review and maintain the change.

The point is to make the contributor decide who benefits before the maintainer receives another patch. A real bug with evidence remains a useful contribution. A hypothetical failure invented to justify a patch can wait.

## Copy the guide

[agent-pr-gate's CONTRIBUTING.md](https://github.com/ktwu01/agent-pr-gate/blob/main/CONTRIBUTING.md) contains the questions and the contribution rules. Copy and adapt it to your project, or give your agent this instruction:

```text
help me copy and paste https://github.com/ktwu01/agent-pr-gate/blob/main/CONTRIBUTING.md into our CONTRIBUTING.md
```

Read the copied rules before adopting them. They include more than the four questions, such as requiring evidence of an observed problem. The repository uses CC0 1.0, so you can adapt it without attribution. No bot or dependencies are required.

This depends on the agent reading and following repository instructions. It cannot block a contributor who ignores them. benchmark-radar also has a separate limit of ten open issues and PRs combined per author, with maintainers exempt. That limit is distinct from the question gate.

I have not measured whether the questions reduce PR volume or improve acceptance rates. For now, this is a contribution policy other maintainers can try, with a documented reason for trying it.

Inspired by [@ycaophysics](https://x.com/ycaophysics). If your review queue has the same problem, [copy the policy from agent-pr-gate](https://github.com/ktwu01/agent-pr-gate).
