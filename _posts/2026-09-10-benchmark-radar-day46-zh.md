---
title: "Benchmark Radar 第四十六天：arXiv 发布——arXiv:2609.11115 上线与 v0.11.0 发布"
date: 2026-09-10
permalink: /zh/posts/2026/09/benchmark-radar-day46/
tags:
  - AI
  - Benchmarks
  - Paper
  - arXiv
  - Release
  - Plain English
---

Benchmark Radar 的第四十六天。技术论文正式登上 arXiv，编号 `arXiv:2609.11115`；v0.11.0 发布携带冻结数据与经验证哈希；全项目引用位置更新指向在线 arXiv 条目。记分牌：185 颗星，30 个 fork。

> 作者：[Koutian Wu](https://www.linkedin.com/in/ktwu01/)；[GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar 已上线。** 每天追踪新的 AI 基准测试、数据集与排行榜：[打开仪表盘](https://benchmark-radar.org/) 或 [在 GitHub 上 Star](https://github.com/ktwu01/benchmark-radar)。

论文：**Benchmark Radar: A Living Database and Search Engine for AI Benchmarks and Evaluation**（Koutian Wu, Junjie Zhou, Ergan Shang, Jiayu Wang, Pengqian Han, Junkai Wang, Wanghan Xu）。arXiv:2609.11115 [cs.AI]。[PDF](https://arxiv.org/pdf/2609.11115) · [摘要](https://arxiv.org/abs/2609.11115)

GitHub v0.11.0 发布锁定完整证据包：
- 软件提交：`8f46bbfa91f5d9900c8b08a5d552c3df5c9597b0`
- 发现截止：2026-09-07
- 数据包：`benchmark-radar-paper-data-v0.11.0.zip` 含 SHA-256 校验和
- 普查：1,283 条来源记录（790 条有评分、493 条无评分），12,916 个数值观测
- 37 个公开来源（13 个直连连接器，24 个第一方实验室来源）

PR #591 推进论文子模块至引文修订并验证 arXiv 投稿包。PR #592 推进至来源计数修订，落实 37 个来源的拆解。PR #593 推进至重建 PDF——即提交 arXiv 的 `main.pdf`，现已入库。

PR #594 在两个 README 增加 Abstract 段，描述活体数据库、37 个来源的每日发现、带分数历史的基准目录、含饱和度与趋势视图的排行榜、离线查询 CLI。

PR #595 在两个 README 准确记录分数来源：实验室模型报告与系统卡提供 SWE-bench Verified；Artificial Analysis 与 LLM Stats 提供绝大多数其他模型分数；OpenCompass Hub 覆盖更宽的基准目录。每个分数保留来源引用。

PR #596 在引用页标注分数来源，PR #597 更新贡献评分。PR #598 CI 核验冻结论文数据，确认哈希匹配与普查一致。

为什么要在意

arXiv 发布让 Benchmark Radar 方法论可引用、永久可得、可被检索。v0.11.0 让证据可复现：冻结提交、固定的截止点、哈希数据包、CI 验证的哈希，意味着任何人都能对着同一组输入核验论文里的每个数字。

全项目引用位置——README 徽章、引用页、仪表盘页脚、CLI 帮助——现在指向真实的 arXiv 编号，而非预印本占位符。论文进入学术记录。

解决的问题

- #590：论文子模块——引文修订
- #591：论文子模块——来源计数修订
- #592：论文子模块——重建 PDF（提交版 main.pdf）
- #593：两个 README 增加 Abstract
- #594：README 准确记录分数来源
- #595：引用页标注分数来源
- #596：冻结论文数据 CI 核验
- #597：贡献评分更新
- 记分牌：185 / 1000 星，30 个 fork

第四十七天：引用位置转为读者优先，Cite 卡片默认折叠 APA/BibTeX，顶部导航新增 Cite 入口。

> 想跟进 Benchmark Radar？[在 GitHub 上 Star 仓库](https://github.com/ktwu01/benchmark-radar) 获取每日更新，或 [打开实时仪表盘](https://benchmark-radar.org/) 浏览扫描结果。阅读论文：[arXiv:2609.11115](https://arxiv.org/abs/2609.11115)。