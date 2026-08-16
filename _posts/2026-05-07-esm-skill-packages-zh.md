---
title: '地球系统模型技能包：为 Noah-MP、CLM、CAM、MOM6、WRF、E3SM 等量身打造的深层知识包'
date: 2026-05-07
permalink: /zh/posts/2026/05/esm-skill-packages/
tags:
  - earth-system-models
  - climate-modeling
  - noah-mp
  - clm
  - cam
  - mom6
  - wrf
  - e3sm
  - jules
  - parflow
  - summa
  - vic
  - skill
  - llm
  - ai-agents
---
地球系统模型是人类写过的、有史以来最复杂的一批科学软件，可它们对新手来说偏偏又是文档最糟糕的一批。我一直在为主要的几大地球系统和陆地表面模型构建一系列"技能包"——结构化的、渐进式披露的知识包——设计给刚入门的研究生和 AI 编码代理两类使用者使用。

> 作者：[Koutian Wu](https://www.linkedin.com/in/ktwu01/)；[GitHub: ktwu01](https://github.com/ktwu01/)

## 什么是技能包

本系列里的每个仓库都围绕一个指向 `reference/` 目录的 `SKILL.md` 路由枢纽构建，里面是各个深度文档。这种结构的设计目的是：

- 新研究生不用读完参考文献里的每一篇论文，就能找到安装路径、案例流程和调试章节。
- AI 编码代理能按需路由到正确的参考文档，而不是把整本模型手册硬塞进上下文。
- 贡献者清楚新内容该放在哪里。

这种格式借鉴了渐进式披露：高层有高信号索引，往下点一层就是完整深度。

## 这些技能包

| 模型 | 领域 | 仓库 |
| --- | --- | --- |
| **Noah-MP** | 陆地表面（NCAR/noahmp + HRLDAS） | [noahmp-skill](https://github.com/ktwu01/noahmp-skill) |
| **CTSM / CLM** | 陆地表面（社区陆面系统模型） | [ctsm-skill](https://github.com/ktwu01/ctsm-skill) |
| **JULES** | 陆地表面（英国联合陆地环境模拟器） | [jules-skill](https://github.com/ktwu01/jules-skill) |
| **SUMMA** | 陆地表面（统一多建模选项结构） | [summa-skill](https://github.com/ktwu01/summa-skill) |
| **ParFlow** | 流域水流（并行） | [parflow-skill](https://github.com/ktwu01/parflow-skill) |
| **VIC** | 大尺度水文（可变下渗能力） | [vic-skill](https://github.com/ktwu01/vic-skill) |
| **CAM** | 大气（社区大气模型） | [cam-skill](https://github.com/ktwu01/cam-skill) |
| **WRF** | 大气（天气研究与预报） | [wrf-skill](https://github.com/ktwu01/wrf-skill) |
| **MOM6** | 海洋（模块化海洋模型 6） | [mom6-skill](https://github.com/ktwu01/mom6-skill) |
| **E3SM** | 耦合（Energy Exascale Earth System Model） | [e3sm-skill](https://github.com/ktwu01/e3sm-skill) |

## 每个技能包覆盖什么

具体内容因模型而异，但每个包的形状都一样：

- **架构** —— 用几张图说明数据流和主要代码单元。
- **物理选项** —— 有哪些旋钮、它们实际做什么。
- **案例流程** —— 怎么搭建、编译、运行一个真实案例。
- **输出与诊断** —— 格式是什么、怎么检查它们。
- **耦合** —— 模型如何与其邻居（大气、海洋、陆地）对话。
- **调试** —— 每个新手都会踩的那些失效模式。
- **贡献** —— 怎么向上游发一个 PR。

## 我为什么建这些

三个原因：

1. **自用。** 我以研究陆地表面模型为业。这些笔记我反正需要。
2. **AI 代理兼容性。** AI 代理尝试修改地球系统代码时，会用非常暴露问题的方式失败。一个结构良好的技能包能大幅提升它们的命中率。（相关：[ESM-bench](/posts/2026/04/esm-bench-ai-agents-earth-system-models/)，这是我专门用来测量这件事的基准。）
3. **上手。** 这些模型大多会受益于一份好的"前 30 天"文档。技能包就是对这份文档的一次尝试。

## 这些给谁

- 刚开始使用特定模型的新研究生。
- 处理地球系统代码的 AI 编码代理。
- 交叉核对另一个模型里类似问题如何被处理的研究者。
- 任何为这些社群写教程或文档的人。

## 贡献

每个仓库都是独立的。如果你在某个特定技能包里发现错误，就到那个仓库开 issue 或 PR。如果你想为一个不在此列表里的模型开一个技能包，noahmp-skill 仓库最接近可用的模板。

---

地球系统模型是为数不多"一份好的索引比一个机灵的 feature 更有价值"的软件生态。这些技能包就是我对那份索引的尝试。