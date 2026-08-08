---
title: "我的博士导师打造的陆面模型，曾用于预报飓风 Harvey"
date: 2026-05-09
permalink: /zh/posts/2026/05/zong-liang-yang-noah-mp-advisor/
tags:
  - PhD
  - Noah-MP
  - climate
  - UT Austin
  - mentorship
  - earth system science
---

加入实验室以后，你会接过一个研究方向，也会继承一套已有 30 年历史的代码库。它目前运行在美国国家水模型中，也曾处在飓风 Harvey 预报工作的关键路径上。这就是在 Jackson School of Geosciences 与 Zong-Liang Yang 一起工作的真实样子。

> 作者：[Koutian Wu](https://www.linkedin.com/in/ktwu01/)；[GitHub: ktwu01](https://github.com/ktwu01/)

> Zong-Liang 的人物纪事：[ktwugoat.github.io/zong-liang-yang-chronicle](https://ktwugoat.github.io/zong-liang-yang-chronicle/)。它属于一个人物纪事目录。这些网站都从 [Sean Xiang chronicle template](https://github.com/ktwu01/sean-xiang-chronicle) 派生，由我和 UT Austin 的同事共同构建。完整目录包括：[Ashley Matheny](https://ut01.github.io/ashley-matheny-chronicle/)、[Chen Ning Yang](https://ut01.github.io/chen-ning-yang-chronicle/)、[Daniella Rempe](https://ut01.github.io/daniella-rempe-chronicle/)、[Eric C. Greene](https://yzliu03.github.io/Eric-Greene-chronicle/)、[Geeta Persad](https://ut01.github.io/geeta-persad-chronicle/)、[Gengchen Mai](https://ut01.github.io/gengchen-mai-chronicle/)、[Juan Santiago](https://qijiang-yoyo.github.io/juan-santiago-chronicle/)、[Kehan Dong](https://ut01.github.io/kehan-dong-chronicle/)、[Marc Hesse](https://ut01.github.io/marc-hesse-chronicle/)、[Sean Xiang](https://ktwu01.github.io/sean-xiang-chronicle/) 和 [Zong-Liang Yang](https://ktwugoat.github.io/zong-liang-yang-chronicle/)。

Zong-Liang 在墨尔本大学取得气象学硕士学位后，于 1992 年在悉尼的麦考瑞大学获得博士学位。他在亚利桑那大学完成博士后研究，并在那里担任早期教研岗位。2001 年起，他一直任职于 UT Austin。如今，他担任 John A. and Katherine G. Jackson Chair in Earth System Sciences 和 Dave P. Carlton Centennial Professorship，并负责 Center for Integrated Earth System Science。2025 年，他当选 AGU Fellow。

Zong-Liang 已发表 230 多篇同行评审论文，Google Scholar h-index 为 81，作为 PI 获得超过 800 万美元资助。他参与开发的陆面模型 CLM 和 Noah-MP，被美国各大建模中心以及 National Centers for Environmental Prediction、NSF NCAR、National Water Center、NASA 和 NOAA 使用。

他仍把 Noah-MP 视为可修改、可质疑的模型。他会追问 2010 年为何选择某项参数化，以及它在 2026 年是否仍应保留。

Noah-MP 是一个基于物理的陆面模型。它试图模拟雨水如何落到地面，水如何穿过土壤，植物如何通过根系吸水，以及水如何经由蒸腾回到大气。我正在把可解释 AI 集成进 Noah-MP，以更好地模拟植物、岩石和水之间的相互作用。每一步都有一项参数化，也就是一段代码，用来表达“给定这些输入后，物理过程大致会怎样发展”。这些参数化来自不同年代，其中一些已有几十年历史，设计时并未覆盖得州干旱中的植物水力胁迫或 Daniella Rempe 在加州持续记录的基岩储水现象。

机器学习部分的目标不是用神经网络替换 Noah-MP，而是识别参数化在不同情景下的偏差，并把诊断结果送回模型开发。这样，后续版本可以修改相关物理过程的表示，同时保留显式的物理结构、物理可解释性，以及在训练分布之外使用模型的能力，包括对尚未发生的飓风进行预报。

“AI for science”包括不同路线。一种做法是在天气数据上训练 Foundation Model，让它直接生成预报结果。另一种做法是用 AI 诊断物理模型的偏差，再修正模型对相关过程的表示。第二种做法更难发表、演示和解释，但其改进可以在后续模型版本中累积。

Zong-Liang 经历过多轮气候研究浪潮，他参与开发的模型也持续使用至今。我观察到，他会把三个星期投入一项土壤湿度参数化，因为根据他的判断，这项工作会影响五年后某位研究者对干旱的模拟。

写下这篇文章时，我的博士生涯刚开始约六个月。我目前的工作运行在 NSF NCAR 的 Derecho-GPU 超级计算机上，使用由我管理的 UTAA0012 计算资源配额。这个方向首项公开发表的成果出现在 AMS 2026，由我与 Lingcheng Li、Daniella Rempe、Ashley Matheny、Mehnaz Mbarak 和 Zong-Liang 共同完成。后续研究将检验这些方法能否改变 Noah-MP 对植物、岩石和水相互作用的表示。

Noah-MP 目前运行在 National Water Center 的生产环境中，这使相关研究直接面向一套正在业务系统中使用的模型。
