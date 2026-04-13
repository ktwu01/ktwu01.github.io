---
title: 'Neural Galaxy - 属于你的 AI 对话可视化宇宙'
date: 2025-11-26
permalink: /posts/2025/11/neural-galaxy-cn/
tags:
  - visualization
  - ai
  - react
  - threejs
---
一个支持手势控制的 3D 可视化项目，把你的 AI 对话历史变成可以飞行探索的星系。你可以在 ChatGPT 对话之间穿梭，也可以把抽象的人工智能概念变成一个能亲手操作的可视化空间。[Try Live Demo](https://ktwu01.github.io/neural-galaxy/)

> 作者：[Koutian Wu](https://www.linkedin.com/in/ktwu01/)；[GitHub: ktwu01](https://github.com/ktwu01/)

[![GitHub stars](https://img.shields.io/github/stars/ktwu01/neural-galaxy?style=social)](https://github.com/ktwu01/neural-galaxy/stargazers) [![GitHub forks](https://img.shields.io/github/forks/ktwu01/neural-galaxy?style=social)](https://github.com/ktwu01/neural-galaxy/fork) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://github.com/ktwu01/neural-galaxy/issues) ![License](https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-informational.svg)

> 一个支持手势控制的 3D 可视化系统，用来展示你的 **AI 对话语料宇宙**。在 **ChatGPT** 对话之间飞行穿梭，并以沉浸式方式探索 **artificial intelligence** 相关概念。

## 项目亮点

- **Instant Spacewalk** —— **零部署即可体验。** 只需要在浏览器中打开 [web app](https://ktwu01.github.io/neural-galaxy/)，就能立刻探索内置示例对话，并体验带有强 bloom 效果的 cyberpunk 风格 UI。
- **Setup Guide Wizard** —— 一个简单的引导流程（快捷键：按 `I`）帮助你在几秒内导入自己的 **ChatGPT** 历史记录。**你的数据 100% 保留在本地**——处理完全发生在浏览器中，保证隐私。
- **Gesture + Keyboard Modes** —— 可以在 MediaPipe 手势追踪与经典 Orbit controls 之间一键切换，HUD 还会展示系统当前看到的动作信息。
- **Floating Utilities** —— 一键按钮可查看键盘帮助、生成全界面截图（`S` 快捷键，带倒计时），并直接进入 onboarding wizard。
- **Python Data Builder** —— `/scripts` 中的脚本可提取并预处理你的聊天数据，让你在离线状态下重新生成 `galaxy_data.json`，同时保持一致的颜色与空间布局。

## 1 分钟上手

直接打开浏览器，访问 [https://ktwu01.github.io/neural-galaxy/](https://ktwu01.github.io/neural-galaxy/)，即可开始体验。

## 导入你自己的对话历史

1. 导出你的聊天记录（支持 ChatGPT JSON、Claude、Gemini 等）。
2. 在运行中的应用里，点击 **Import (I)** 按钮，或直接按 `I`。
3. 跟随 Setup Guide 向导：
   - 学习如何从不同平台导出聊天记录
   - 在 File Import（Upload）步骤拖入你的 JSON 文件
   - 点击 `Import`，就完成了
4. 当成功页面出现后，回到星系视图——你的数据已经可见、持久保存并可随时探索。按下 `S` 还能生成一个方便分享的截图覆盖层（包含 3 秒倒计时）。

## 控制方式与快捷键

| Action | Keyboard / Mouse | Gesture Mode |
| --- | --- | --- |
| Toggle gesture mode | `M` or panel switch | 正常抬手/放手切换 |
| Focus particle HUD | `K` | 指向并 pinch |
| Keyboard help | `H` | — |
| Setup/import wizard | `I` | — |
| Screenshot whole UI | `S`（或 Screenshot 按钮） | — |
| Close overlays | `ESC` | 手掌回到 neutral |

额外的 UI 辅助：
- 浮动的 import/help/screenshot 按钮位于右下角
- minimap 在左下角，gesture info 在右下角，focus HUD 在顶部中间
- 版权信息与社交链接会持续显示，便于分享

## 自己生成 Galaxy 数据（可选）

如果你更希望在浏览器外预处理数据：

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install numpy sentence-transformers umap-learn hdbscan  # tweak as needed

# 1. Drop your raw export at data/conversations.json
python3 scripts/extract_messages.py  # -> data/extracted_messages.json

# 2. Adjust scripts/config.py (neighbors, distances, palette, etc.)
python3 scripts/build_galaxy.py      # -> frontend/src/assets/galaxy_data.json
```

刷新浏览器即可看到重新生成后的数据集。你也可以在 `docs/CONFIGURATION.md` 中进一步调整聚类方式、空间分布或粒子尺寸。

## 技术栈

- **Frontend:** React + Vite + @react-three/fiber + Drei + MediaPipe Hands
- **Visualization:** Instanced particles、circular minimap、draggable gesture HUD、floating panels
- **Tooling:** ESLint、modern CSS、基于 html2canvas 的截图功能
- **Backend Scripts:** Python + NumPy，用于位置生成和消息提取辅助

## 参与贡献与支持

欢迎想法、issues 和 PR——这是一个不断演化的个人数据可视化实验场。如果你遇到问题，可以前往 [GitHub issue](https://github.com/ktwu01/neural-galaxy/issues) 提交；也欢迎 fork 仓库，做出你自己的 Neural Galaxy。🚀

## 致谢

- 灵感来自 [@Suryansh777777](https://x.com/Suryansh777777) 的 [Jarvis-CV](https://github.com/Suryansh777777/Jarvis-CV)、[@SarthakHuh](https://x.com/SarthakHuh) 的 Neural Visualizer，以及 [@jinaycodes](https://x.com/jinaycodes) 的 [soarxiv.org](https://soarxiv.org/)。欢迎交流反馈！
