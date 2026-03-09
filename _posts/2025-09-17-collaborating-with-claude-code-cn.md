---
title: '和 Claude Code 一起更新我的学术网站'
date: 2025-09-17
permalink: /posts/2025/09/claude-code-collaboration-cn/
tags:
  - web development
  - AI tools
  - academic website
  - automation
---

今天我经历了一次挺有意思的合作：和 Claude Code 一起，把我的个人学术网站彻底重做了一遍。作为 UT Austin Geological and Earth Sciences 的博士生，我需要把 GitHub Pages 站点从一堆占位符内容，更新成真正能代表我专业背景的信息。

## 挑战是什么

我的网站（ktwu01.github.io）是基于 Academic Pages 模板搭建的，但里面一直塞满了样例数据——虚构的论文、占位的报告，以及模拟出来的教学经历。我的真实信息其实都整理在云端的 LaTeX 文件里，但要手动把这些内容转成 Jekyll markdown 格式，不仅耗时，而且很容易出错。

## 合作过程

最让我印象深刻的是 Claude Code 的系统化工作方式：

1. **Analysis Phase**：Claude Code 先检查了现有网站结构和我的源文件，弄清楚数据格式以及需要做哪些转换。

2. **Content Verification**：它会仔细把 LaTeX CV 各部分和我提供的信息逐项交叉核对，确保准确无误，包括作者标注（比如通讯作者的星号）和 citation 格式。

3. **Systematic Updates**：AI 非常有条理地更新了各个板块：
   - Publications：补充了我的 JGR: Space Physics 论文和教育研究成果
   - Conference talks and presentations：加入了 AGU、NASA workshops 和 JSG symposium 的报告信息
   - Teaching experience：详细记录了我在 Earth in 2100 课程中的助教经历（520+ 名学生）
   - Portfolio projects：展示了我的 AI/ML 与地球科学相关项目，包括获得 NCAR 资助的 Noah-MP 研究

## 技术细节

这次协作涉及更新多个 Jekyll collections：
- `_publications/` - 添加了我的 JGR: Space Physics 论文和教育研究内容
- `_talks/` - 纳入了来自 AGU、NASA workshops 和 JSG symposium 的报告
- `_teaching/` - 记录了我在 Earth in 2100（520+ 学生）中的 TA 经验
- `_portfolio/` - 展示了我的 AI 项目，包括 NCAR 资助的 Noah-MP 研究

## 质量保证

Claude Code 最出色的一点，是它对细节的重视。当我让它“再全部检查一遍”时，它确实发现并修正了几个准确性问题：
- citation 里遗漏的通讯作者星号
- 一个本该被加入却漏掉的 AGU 报告
- venue 名称格式的统一与修正

## 学到的东西

这次经历让我更清楚地感受到，AI 工具在以下方面真的很有价值：
- **Data Transformation**：在不同格式之间转换内容（LaTeX → Markdown）
- **Accuracy Verification**：交叉核对多个数据源
- **Best Practice Compliance**：确保符合 Jekyll 格式与学术规范
- **Systematic Organization**：管理跨多个文件的复杂更新

关键在于：你要给 Claude Code 提供完整的源材料，并且明确强调准确性要求。“把所有内容再 double-check 一遍” 这种做法，确实能抓住那些本来很容易漏掉的细节。

## 展望

作为一个工作在 AI 与地球科学交叉领域的人，这次合作也是一次很实际的展示：AI 工具如何真正增强学术工作流。现在的网站更准确地体现了我的研究方向——包括 Noah-MP 陆面模型中的可解释 AI、我在实习期间做的 AI evaluation systems，以及我在 space physics 和 Earth system science 方面更广泛的工作。

更新后的网站，既是一个更专业的个人作品集，也可以被看作一次高质量 human-AI collaboration 的实际案例。

---

*这篇文章写于 2025 年 9 月 17 日，也就是我刚刚与 Claude Code 一起完成网站更新之后。*