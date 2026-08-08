---
title: "Gengchen Mai 正在构建空间基础模型，地理学者值得关注"
date: 2026-05-09
permalink: /zh/posts/2026/05/gengchen-mai-spatial-foundation-models/
tags:
  - GeoAI
  - foundation models
  - geography
  - UT Austin
  - spatial reasoning
  - knowledge graphs
---

文本基础模型已经改变了 NLP，图像模型也改变了计算机视觉。空间推理领域同样会出现自己的基础模型。Gengchen Mai 正在研究这一方向，他在 UT Austin 的 SEAI Lab 也开展相关工作。

> 作者：[Koutian Wu](https://www.linkedin.com/in/ktwu01/)；[GitHub: ktwu01](https://github.com/ktwu01/)

> Gengchen 的人物志：[ut01.github.io/gengchen-mai-chronicle](https://ut01.github.io/gengchen-mai-chronicle/)。它属于一组由 [Sean Xiang 人物志模板](https://github.com/ktwu01/sean-xiang-chronicle)派生的记录网站，全部由我和 UT Austin 的同事共同建立。完整目录包括：[Ashley Matheny](https://ut01.github.io/ashley-matheny-chronicle/)、[Chen Ning Yang](https://ut01.github.io/chen-ning-yang-chronicle/)、[Daniella Rempe](https://ut01.github.io/daniella-rempe-chronicle/)、[Eric C. Greene](https://yzliu03.github.io/Eric-Greene-chronicle/)、[Geeta Persad](https://ut01.github.io/geeta-persad-chronicle/)、[Gengchen Mai](https://ut01.github.io/gengchen-mai-chronicle/)、[Juan Santiago](https://qijiang-yoyo.github.io/juan-santiago-chronicle/)、[Kehan Dong](https://ut01.github.io/kehan-dong-chronicle/)、[Marc Hesse](https://ut01.github.io/marc-hesse-chronicle/)、[Sean Xiang](https://ktwu01.github.io/sean-xiang-chronicle/)、[Zong-Liang Yang](https://ktwugoat.github.io/zong-liang-yang-chronicle/)。

Gengchen 的实验室页面和个人网站记录了他的学术轨迹。他在 UC Santa Barbara 地理系攻读博士，该系长期以 GIScience 的形式化研究著称。随后，他进入 University of Georgia 的 AI institute 任教，之后来到 UT Austin 地理系。他的 SEAI Lab 全称为 Spatial Explorer of AI Lab，位于 UT Austin College of Liberal Arts 的地理项目内。研究组页面也记录了更广泛的合作网络。

这项工作与地球系统科学有关，因为空间数据、地理数据和地球观测数据本身包含结构、拓扑与尺度信息。通用神经网络若把它们当作普通输入，就可能遗漏这些属性。

GeoAI 社区正在处理几个具体问题，Gengchen 也是其中经常发声的研究者之一。第一个问题是位置编码：如何把经纬度转化为神经网络可用的向量，同时尊重地球的球面几何，以及地理现象的多尺度性质。第二个问题是把地理实体知识图谱与基础模型擅长的统计学习结合起来。第三个问题是构建能够在卫星影像、地面照片、文字描述和结构化空间数据之间进行推理的多模态模型。

如果从 Jackson School 的陆面建模视角看，最直接的问题是空间基础模型能否帮助解决参数化。Noah-MP 与其他陆面模型一样，包含一些应当按照物理意义随空间变化的参数。土壤水力性质、植被用水策略和根系分布都具有空间结构。传统方法会从土壤数据库或植被地图中查找数值。一个已经学习某地跨模态信息的空间基础模型，原则上可能做得更好。

在我的阅读中，GeoAI 文献有时与实际运行的地球系统建模脱节：有些空间 Transformer 论文侧重数学方法，没有在真实气候数据集上运行；有些气候模型论文采用的深度学习方法与 GeoAI 的研究范式不同。两类工作的交叉处仍有研究空间，我预计这个领域会在未来五年继续扩大。Gengchen 长期从事 GIScience 研究，这一经历为相关跨领域讨论提供了地理学背景。

SEAI Lab 的工作从空间认知和 GIScience 的问题出发，再考察现代 ML 让哪些原本难以回答的问题变得可解。

SEAI Lab 正在建设可供全校使用的基础设施，这类基础设施也可供我这样的项目使用。如果要把空间基础模型接入 Noah-MP 改进流程，最省力的路径是走到校园另一边合作，而不是从头重复建设。研究型大学在不同学院拥有多个 AI 团队，跨系合作因此变得可行，这项好处常常被低估。

这条职业路径给我的启发，与许多 UT Austin 研究者的经历相似：研究方法发生变化时，既有专业知识与新工具的交叉处会出现建立新实验室的机会。SEAI Lab 是一个例子。

对现在开始读博的我而言，空间基础模型会进入我的研究。接下来要解决的是，如何与有这类模型构建经验的人合作，并避免直接套用通用 Transformer。相关研究者就在校园里，我应该更常去交流。
