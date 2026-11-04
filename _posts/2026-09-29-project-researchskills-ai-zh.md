---
title: "ResearchSkills.ai"
date: 2026-09-29
permalink: /zh/posts/2026/09/project-researchskills-ai/
tags:
  - media
  - project
---

[ResearchSkills.ai](https://researchskills.ai/) 收录可以复用的科研 AI Skills，方便研究者查找和分享用于文献、分析、写作等研究环节的工具。

> 作者：[Koutian Wu](https://www.linkedin.com/in/ktwu01/)；[GitHub: ktwu01](https://github.com/ktwu01/)

资深研究者最有用的经验，很少写进论文。哪台仪器午饭后会漂移；哪个求解器参数看似无害，却会悄悄毁掉一次计算；哪篇名作里的结果，至今没人复现出来。用已发表文本训练的大模型从没见过这些，因为它们从没被发表过。

ResearchSkills 想把这类经验写下来，变成 AI 智能体可以加载的形式。代码和合集都在 [ResearchSkills 仓库](https://github.com/ktwu01/ResearchSkills)，隶属 ScienceIntelligence 组织。

## 什么是 Skill

一个 Skill 就是一个普通的 markdown 文件，Claude Code、Codex 这类工具在需要时读取它。每个 Skill 记录一条专家经验，并写明适用场景。

合集借用认知科学的分类，按记忆类型整理 Skills：

- **程序性。** 帮助走出僵局的“如果……就……”规则。细分类型包括选项打平、操作没有效果、约束失败和操作报错。
- **语义性。** 大模型缺失的事实。细分类型包括太新、还没进入训练数据的前沿结果，非公开知识，以及对模型常见错误的纠正。
- **情景性。** 真实科研中的具体经历：一次失败、一次调整、一次被注意到的异常。

这样分很有必要，因为每一类出错的方式不同。程序性 Skill 出错，是规则在错误的情境下被触发；语义性 Skill 会过时；情景性 Skill 只有在智能体意识到自己的处境和那段经历相似时才有用。

## 覆盖范围

Skills 按 arXiv 分类体系分为 8 个领域、155 个子类。物理的子类最多，有 51 个；其次是计算机 40 个、数学 32 个；再往后是定量生物、定量金融、统计、电子工程和经济。每个领域都在招募专家审稿人，审稿人可以把 Skill 从草稿提升为已审核状态。

## 怎么贡献

有三种方式：

1. **自动提取。** 安装 `@scienceintelligence/researchskills-extract`，在 Claude Code 或 Codex 里运行它的斜杠命令。它会读取一段科研对话，提出候选 Skills，并在任何内容离开你的电脑前征求同意。你可以在浏览器页面里逐条审阅。
2. **网页提示词。** 把一键提示词粘贴到 ChatGPT、Claude 或 Gemini，然后提交结果。
3. **手动编写。** 按照提交指南自己写一个 Skill。

所有内容采用 CC BY 4.0 许可，贡献者获得署名，任何人都可以复用。

## 我担心的地方

仓库 README 里有一条警告，我很认同：应用一个 Skill 可能触发大范围修改和大量 token 消耗。Skill 是写给智能体的指令，为一个实验室的环境写的指令，放到另一个环境里可能造成破坏。所以“已审核”的状态比总数量更重要。一千条未经审核的 Skills，就是一千种把智能体自信地推向错误方向的方式。

第二个担心是激励。研究者愿意分享隐性知识的前提，是成本低、能拿到署名。自动提取降低了成本，署名问题却还没解决，因为目前还没有哪个招聘委员会会把 Skill 贡献算进成果。

从没写进论文的经验，恰恰是智能体最需要的经验。

访问 [ResearchSkills.ai](https://researchskills.ai/)。
