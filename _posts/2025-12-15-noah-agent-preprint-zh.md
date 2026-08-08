---
title: '新预印本：Noah-Agent，面向 Fortran 气候模型的多专家 AI 智能体框架'
date: 2025-12-15
permalink: /zh/posts/2025/12/noah-agent-preprint/
tags:
  - ai
  - agents
  - climate-models
  - preprint
---

手动为大型 Fortran 气候模型配置参数，速度慢、容易出错，也难以验证。Noah-Agent 要检验的是，一组各有所长的 AI 智能体能否协作完成这项工作。

> 作者：[Koutian Wu](https://www.linkedin.com/in/ktwu01/)；[GitHub: ktwu01](https://github.com/ktwu01/)

我已将 **Noah-Agent (v0.1)** 作为预印本发布到 Zenodo。这篇论文仍在准备中，目前发布的是早期版本。

## Fortran 气候模型的参数化难题

大型 Fortran 气候模型功能强大，但使用门槛高。为模型配置参数并验证其行为，通常需要研究者在庞大且历史悠久的代码库中仔细操作。这项工作耗时，也容易出错。

## 多专家智能体协作

Noah-Agent 是一个多专家 AI 智能体框架，用于自动完成大型 Fortran 气候模型的参数化与验证。它让多个专业智能体分工协作，而不是由一个模型包办所有工作：

- 一部分智能体负责选择和调整参数。
- 另一部分智能体负责对照参考输出，验证模型行为。

目标是在保留人工判断环节的同时，将原本依靠手工完成的步骤自动化。

## 与其他工作的联系

Noah-Agent 与另外两项相关工作并行推进：

- **Noah-MP 陆面建模**，这是我博士研究的主要方向，重点是基于物理过程的陆面模型。
- **[ESM-bench](/posts/2026/04/esm-bench-ai-agents-earth-system-models/)**，用于评估 AI 智能体是否真正理解地球系统模型的物理过程与代码。Noah-Agent 正是这类 benchmark 要测试的系统。

## 当前状态与链接

这篇预印本的版本号为 0.1，目前仍在准备中。现阶段尚未宣称任何研究结果，论文也尚未获接收。

- **预印本（Zenodo）**：[https://zenodo.org/records/17862049](https://zenodo.org/records/17862049)
- **作者**：Wu, K. (2025)
