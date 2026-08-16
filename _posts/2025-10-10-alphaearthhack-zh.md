---
title: 'AlphaEarthHack：德州大学奥斯汀分校地球系统 AI 黑客松项目'
date: 2025-10-10
permalink: /zh/posts/2025/10/alphaearthhack/
tags:
  - hackathon
  - geoscience
  - earth-system
  - ai
  - machine-learning
  - jupyter
  - ut-austin
  - climate
---
AlphaEarthHack 是我们团队为德州大学奥斯汀分校地球科学黑客松打造的项目。目标只有一个：看看在一个周末内，我们能在地球系统数据上把 AI 推到多远。[试试在线演示](https://ktwu01.github.io/AlphaEarthHack/)

> 作者：[Koutian Wu](https://www.linkedin.com/in/ktwu01/)；[GitHub: ktwu01](https://github.com/ktwu01/)

[![GitHub stars](https://img.shields.io/github/stars/ktwu01/AlphaEarthHack?style=social)](https://github.com/ktwu01/AlphaEarthHack/stargazers) [![GitHub forks](https://img.shields.io/github/forks/ktwu01/AlphaEarthHack?style=social)](https://github.com/ktwu01/AlphaEarthHack/fork)

## 关于黑客松

德州大学奥斯汀分校的地球科学黑客松，把杰克逊学院及整个大学范围内的学生和研究人员聚在一起，用周末的时间，在真实的地球科学问题上动手做出具体的东西。我们团队挑了一个我们觉得小到能在期限内交付、又大到值得去做的问题。

## 我们构建了什么

一条处理管道：接收地球观测数据，应用一种学到的表示，然后在原始信号里很难看出来的地方浮现出模式。仓库是一个 Jupyter Notebook 的逐步讲解，你可以从端到端重新运行。

工作内容涵盖：
- 从公共地球科学数据集中进行数据摄入。
- 为地理空间数据那些乱七八糟的现实做预处理。
- 一个能产生有用嵌入或预测的模型层。
- 能把结果呈现给领域科学家、使其一目了然的可视化。

## 一分钟试用

打开 [https://ktwu01.github.io/AlphaEarthHack/](https://ktwu01.github.io/AlphaEarthHack/) 查看项目页面，或克隆仓库并在本地运行 notebook：

```bash
git clone https://github.com/ktwu01/AlphaEarthHack.git
cd AlphaEarthHack
jupyter notebook
```

## 技术栈

- **Python** + **Jupyter Notebook** 用于分析管道。
- 用于地球科学数据的地理空间库（rasterio、xarray 等）。
- 用于模型层的机器学习库。
- 用于项目落地页的 HTML。

## 为什么这值得读

黑客松的代码通常在演示日之后就被扔掉了。我们试图让 AlphaEarthHack 保持一个状态：让某个人——包括未来的我们自己——能接手、理解其中的取舍并加以扩展。Notebook 的结构和 README，正是为这样的读者而写的。

## 致谢

感谢德州大学奥斯汀分校地球科学黑客松的组织者和我们的队友。黑客松的胜负，取决于你坐在一起的那些人。

## 参与贡献

如果你是想扩展这条管道的地球科学或机器学习从业者，欢迎在 [github.com/ktwu01/AlphaEarthHack](https://github.com/ktwu01/AlphaEarthHack) 提交 issue 或 PR。

---

一个周末不足以解决地球系统科学。但足以提出一个好问题。