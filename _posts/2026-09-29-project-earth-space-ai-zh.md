---
title: "Earth-Space-AI"
date: 2026-09-29
permalink: /zh/posts/2026/09/project-earth-space-ai/
tags:
  - media
  - project
---

[Earth-Space-AI](https://github.com/earth-space-ai) 是一个面向地球与空间科学的开源组织，收录 AI 工具、Skill 包和研究项目。

> 作者：[Koutian Wu](https://www.linkedin.com/in/ktwu01/)；[GitHub: ktwu01](https://github.com/ktwu01/)

地球系统模式是世界上规模最大的科学程序之一。WRF 做天气预报，CTSM 模拟陆地和植被，WACCM-X 从地面一直算到太空边缘。每个模式都积累了几十年关于怎么编译、怎么配置、怎么调试的经验，而这些经验大多散落在用户邮件列表、研讨会幻灯片和少数资深研究者的脑子里。

AI 编程智能体能读源代码，却读不到 2014 年那封邮件，那封邮件解释了为什么某个 namelist 参数千万不能按直觉设置。Earth-Space-AI 就是为了补上这个缺口。它的一句话介绍是：“面向地球、行星与空间科学的程序性知识 Skills。”

## 里面有什么

组织托管的是 Skill 包。每个包是一组结构化的 markdown 文件，智能体按需加载，研究者也可以当参考手册读。`SKILL.md` 负责把智能体引到正确的章节，更深的参考文档只在需要时加载，这样智能体不会把上下文窗口浪费在用不上的内容上。具体结构我在[之前的文章](/zh/posts/2026/05/earth-space-ai-org-skill-packages/)里写过。

目前已有的包包括：

- **WRF**，天气研究与预报模式
- **CTSM**，社区陆地系统模式
- **Noah-MP**，陆面模式，以及它的 HRLDAS 驱动
- **WACCM** 和 **WACCM-X**，CESM 中的全大气模式，后者延伸到电离层和热层
- **ROMS**，区域海洋模式
- **RegCM**，ICTP 的区域气候模式
- **OpenIFS**，ECMWF 面向科研和教学发布的预报模式版本
- **NorESM**，挪威地球系统模式

模式 Skills 之外，组织还运营两个社区工具。[Benchmark Radar](https://github.com/earth-space-ai/benchmark-radar) 每天追踪 AI 评测和数据集，由我发起，已被 fork 超过 50 次。[Scientific Resources](https://github.com/earth-space-ai/scientific-resources) 整理面向科研人员的算力、云服务与 API 额度，以及科研经费信息。

## 为什么先做 Skills

AI 进入地球科学，常见的说法是训练一个新的神经网络模型来取代物理模式。这些模型又快又惊艳，可它们依然需要物理模式提供训练数据，需要物理模式去算那些还没被学到的变量，也需要物理模式回答“为什么”。物理模式不会消失。

真正拖慢研究者的，是把这些模式正确地跑起来。一个研究生可能因为一个编译错误或一个配置错误的区域，耗掉整整一学期。如果智能体能带着这些配置经验，这一学期就能还给科学本身。Skill 包写起来便宜，检查起来容易，第一天就能用，所以我从这里开始。

## 还难在哪里

上游模式一更新，Skill 就会过时，所以每个包都要跟着它覆盖的模式一起维护。署名也很重要。这些模式属于庞大的社区，Skill 包应该把用户引回官方文档和许可证，和官方资料互补。

一个科学模式最有价值的部分，往往是那些从没写进手册的建议。

浏览 [GitHub 上的 Earth-Space-AI](https://github.com/earth-space-ai)。
