---
title: "把树当成水泵：Ashley Matheny 改变了整个陆地模型"
date: 2026-05-09
permalink: /zh/posts/2026/05/ashley-matheny-trees-as-pumps/
tags:
  - ecohydrology
  - plant hydraulics
  - PhD
  - UT Austin
  - Noah-MP
  - vegetation
---
大多数陆地表面模型都把一棵树当成一根被动的吸管。水从根进来，水从叶出去，故事就这么简单。Ashley Matheny 的研究基本上在说：不对，树是一个带有储水、电容和策略的活跃水力系统，如果你不这样建模，你在干旱问题上就会犯错误。

> 作者：[Koutian Wu](https://www.linkedin.com/in/ktwu01/)；[GitHub: ktwu01](https://github.com/ktwu01/)

> Ashley 的年鉴：[ut01.github.io/ashley-matheny-chronicle](https://ut01.github.io/ashley-matheny-chronicle/)。属于从 [Sean Xiang 年鉴模板](https://github.com/ktwu01/sean-xiang-chronicle) 分叉出来的一批年鉴之一，全部由我和 UT Austin 的同事构建。完整目录：[Ashley Matheny](https://ut01.github.io/ashley-matheny-chronicle/)、[Chen Ning Yang](https://ut01.github.io/chen-ning-yang-chronicle/)、[Daniella Rempe](https://ut01.github.io/daniella-rempe-chronicle/)、[Eric C. Greene](https://yzliu03.github.io/Eric-Greene-chronicle/)、[Geeta Persad](https://ut01.github.io/geeta-persad-chronicle/)、[Gengchen Mai](https://ut01.github.io/gengchen-mai-chronicle/)、[Juan Santiago](https://qijiang-yoyo.github.io/juan-santiago-chronicle/)、[Kehan Dong](https://ut01.github.io/kehan-dong-chronicle/)、[Marc Hesse](https://ut01.github.io/marc-hesse-chronicle/)、[Sean Xiang](https://ktwu01.github.io/sean-xiang-chronicle/)、[Zong-Liang Yang](https://ktwugoat.github.io/zong-liang-yang-chronicle/)。

Ashley 在西弗吉尼亚州俄亥俄河畔的一个小镇长大，喜欢滑水、划独木舟和露营。她在俄亥俄州立大学完成了土木工程本科，随后在那里读了土木、环境与测绘工程方向的博士，导师是 Gil Bohrer，2016 年毕业。论文标题本身就能说明一切：《Development of a Novel Plant-Hydrodynamic Approach for Modeling of Forest Transpiration During Drought and Disturbance》。2017 年她来到 UT Austin 任助理教授。到 2021 年她拿下了 NSF CAREER 奖，2022 年获得 AMS 农业与森林气象杰出青年学者奖，期间还获得了 Jackson 学院的 Knebel 杰出教学奖。

她讲起自己为何进入这个领域的故事是：2010 年她为美国陆军工程兵团工作，研究水与大坝的相互作用，在俄亥俄河上看到了一道水跃（hydraulic jump）。正是这一次单一的观察，把她的职业轨迹转向了水文。我常想起这件事。在一条特定的河面前、一个特定的瞬间，整个研究项目随之而来。

她真正做的是测量树木内部的水。这是真实的测量，不是模拟。她和 Conservify 的 Pete Marchetto 开发了新型电容传感器，能随时间追踪树木含水量。她的野外站点遍布各地：密歇根大学生物站、德州丘陵地区（Ashe juniper 和活橡树）、新墨西哥的 Valles Caldera，以及德州墨西哥湾沿岸和远及澳大利亚、巴拿马、阿布扎比、牙买加的红树林生态系统。不同的生态系统、不同的水分策略，同一个根本问题：这个物种在胁迫下如何管理水分。

这里是与我的博士课题接轨的部分。Li, Yang, Matheny 等人 2021 年发表在 JAMES 上关于《Development of plant hydraulics in the Noah-MP Land Surface Model》的论文，本质上就是她野外测量与我现在所属的建模社群之间的桥梁。观点是：如果你把真实的植物水力机制放进一个陆地表面模型里，对干旱响应和蒸散发（transpiration）的预测就会定性变好。不同物种有不同的水力策略。有些是等水型（isohydric），为了保护水柱会激进地关闭气孔；有些是非等水型（anisohydric），继续蒸腾并冒水力失效的风险。一个不知道这二者区别的模型，在干旱年就会预测出错误的结果。

我承认，直到我自己亲手跑那些模拟之后，我才真正理解这一点。你可以读植物水力的论文并跟着点头。但真正亲手带着和带着水力模块去配置 Noah-MP，看着土壤湿度和 ET 时间序列分道扬镳，那种感受完全不同。模型里的树开始有树的行为了，不再是吸管。

Ashley 实验室另一块是国际红树林工作。红树林是盐生植物（halophyte），能耐受盐碱，而标准的植物水力模型从来不是为了处理高盐度下水分吸收的渗透这一面设计的。她一直在扩展模型做这件事。听起来像是一个细分领域的扩展，但如果想到红树林是地球上碳密度最高的生态系统之一，而且它们就处在气候脆弱的沿海地带，你就明白把它们的水碳平衡算对不是可选项。

在 AMS 2026 论文上与她的合作中，我注意到的是她对模型究竟能说什么、不能说什么的那份较真。建模的人（包括我自己）很容易被模拟产出的东西冲昏头脑。她会盯着一个输出问：好，但 UMBS 的液流传感器（sap flux sensor）实际会显示什么？如果你的模拟说出了传感器不会显示的东西，那你的模拟就是错的，再花哨的后处理也救不了。

她的成长轨迹里有一个我正在慢慢消化的更深层教训。新型电容传感器、长期液流记录、多物种比较、国际红树林站点。这些没有一个是快速取胜。你造一个传感器，把它放进一棵树里，等三年，然后你才有数据。那种在 AI 推特上按周发布成果的节奏与她的工作方式根本不相容。好消息是，她产出的数据会比同期每一篇速成的 AI 论文活得更久，因为背后的生物学不会消失。

对我而言，实际的教训是：当我声称 Noah-MP 加上 ML 能更好地模拟植物-岩石-水相互作用时，证据必须活在 Ashley 的数据里，而不是我的训练损失曲线里。否则我只是在用自己的假设去凑一条曲线。