---
name: hv-analysis-writer
description: |
  将 HV-analysis 中的研究报告整理成博客候选稿。适用于创建简短博客引言、复制 HTML 研究附件、并在博客中链接到可访问的 HTML 报告。
---

# HV-analysis 博客发布

当用户要求把 `/Users/kw35262/Documents/dev/HV-analysis` 的研究做成博客时：

1. 先确认报告主题、研究日期，并排除用户不想发布的政治、个人/特定人物或重复报告。
2. 将选定的 `.html` 复制到博客仓库的 `research/hv-analysis/`。
3. 为每份报告创建一篇简短的 `_drafts/YYYY-MM-DD-<slug>-cn.md` 引言，不把完整研究正文复制进博客文章。
4. 引言必须包含 Jekyll front matter、作者署名、一个清楚的钩子、简短背景、读者能获得什么，以及指向 `/research/hv-analysis/<filename>.html` 的完整报告链接。
5. 用户说“候选”或要求审核时，只使用 `_drafts/`，不要放入 `_posts/`，不要提交或推送。
6. 完成后列出候选文件、HTML 文件和来源研究日期，等待用户审核。

博客文章应把 HTML 报告作为主要研究材料，避免把报告未经编辑地当作正文发布。链接必须指向博客仓库中实际存在的 HTML 文件。
