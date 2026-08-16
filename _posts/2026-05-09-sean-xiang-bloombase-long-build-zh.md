---
title: "Sean Xiang 已经打造 Bloombase 14 年，AI 时代终于追上了它"
date: 2026-05-09
permalink: /zh/posts/2026/05/sean-xiang-bloombase-long-build/
tags:
  - founder
  - enterprise security
  - long term
  - infrastructure
  - X-Institute
  - cryptography
---
大多数企业安全公司冒个泡、赶一波趋势，然后在下一个基础设施周期里消失。Sean Xiang 从 2012 年 1 月起就在打造 Bloombase，这家公司却阴差阳错站到了此后每一波重大基础设施转变的正确一边，包括当下的 AI 加速器时代。那不是运气，那是一套论点。

> 作者：[Koutian Wu](https://www.linkedin.com/in/ktwu01/)；[GitHub: ktwu01](https://github.com/ktwu01/)

> 我建了最初的 [Sean Xiang 年鉴](https://ktwu01.github.io/sean-xiang-chronicle/) 和它的 [模板仓库](https://github.com/ktwu01/sean-xiang-chronicle)，也就是整个这批年鉴被分叉出来所依据的那个模板，在我把它改造成自己页面之前是这样。完整目录：[Ashley Matheny](https://ut01.github.io/ashley-matheny-chronicle/)、[Chen Ning Yang](https://ut01.github.io/chen-ning-yang-chronicle/)、[Daniella Rempe](https://ut01.github.io/daniella-rempe-chronicle/)、[Eric C. Greene](https://yzliu03.github.io/Eric-Greene-chronicle/)、[Geeta Persad](https://ut01.github.io/geeta-persad-chronicle/)、[Gengchen Mai](https://ut01.github.io/gengchen-mai-chronicle/)、[Juan Santiago](https://qijiang-yoyo.github.io/juan-santiago-chronicle/)、[Kehan Dong](https://ut01.github.io/kehan-dong-chronicle/)、[Marc Hesse](https://ut01.github.io/marc-hesse-chronicle/)、[Sean Xiang](https://ktwu01.github.io/sean-xiang-chronicle/)、[Zong-Liang Yang](https://ktwugoat.github.io/zong-liang-yang-chronicle/)。所以我和他的时间线相处的时间比几乎任何人都久。他的轨迹是这样的。他在山西长大，1980 年起在中国科学技术大学读物理本科，在香港中文大学读电子与电气工程博士，1996-1997 年在香港科技大学做研究助理，然后 1997 到 1999 年在加州大学尔湾分校的 Beckman 激光研究所做科学家。2012 年 1 月，他在硅谷红木城联合创办了 Bloombase。

公司做的是一种他们称为"智能存储防火墙"的东西。Bloombase StoreSafe 是针对静态数据的应用透明加密，覆盖 SAN、NAS、云存储和终端系统。底层是一个 NIST FIPS 140-2 认证的密码模块，支持 AES、RSA、ECDSA 和抗量子算法，符合 IEEE 1619，采用 OASIS KMIP 密钥管理。他们还推出 Bloombase KeyCastle 做企业密钥生命周期管理。客户足迹遍布虚拟机管理程序（VMware ESXi、Citrix Xen、Microsoft Hyper-V、IBM PowerVM、Red Hat KVM）和云（AWS、Azure、GCP、Rackspace、IBM SoftLayer/Bluemix、VMware vCloud Air）。

如果你只看这些，它听起来像是一家称职的中间件公司。我之所以觉得它比这更有意思，是因为那条结盟的轨迹。从 2013 年起，是一长串密集的合作。2013 年 2 月 OpenStack 社区。2013 年 5 月 EMC 技术合作伙伴计划。2013 年 8 月 VMware 技术联盟伙伴。2014 年 1 月 Dell 认证。2014 年 11 月 Hitachi Data Systems 联盟。2015 年 HP Enterprise Secure Key Manager 互操作。2015 年 Thales ASAP 联盟。2015 年 HPE Helion Ready 和 ArcSight。2016 年 Ultra Electronics AEP Keyper HSM。2017 年 IBM Ready for Security Intelligence。2017 年 ATTO 和华为。2018 年 VMware Cloud on AWS。2019 年 Microsoft Azure Marketplace。2019-2020 年 Marvell LiquidSecurity、nCipher、Futurex。2023 年 NVIDIA DPU/GPU 重新定位。2024 年 11 月 PKI Consortium 会员。2024 年 Entrust nShield Connect。2025 年 4 月 Utimaco 联盟。

那是跨多个平台体制、累积起来的十二年信任层基础设施工作，主线始终如一：静态数据必须加密、密钥必须放在某个安全的地方、密钥管理必须符合标准、架构必须随底层算力的演进而演进。

大多数公司熬不过那么多基础设施转型。熬过来的公司往往共享一个结构性特征。它们下注在一个不会过时的原语上（这里指的是密码学数据保护），而且愿意在别人之前去做与接下来十个企业平台集成的、并不光鲜的工作。Bloombase 2013 年做了 OpenStack，2018-2019 年做了云市场，2023 年做了 NVIDIA DPU/GPU。每一次都恰好是那个特定时刻的正确选择。

2023 年的 NVIDIA 转向是我觉得最令人清晰的一点。论点是：静态数据安全必须原生跑在加速器上，否则它就会变成 AI 数据管道的瓶颈。这句话现在听起来理所当然。在 2023 年它对大多数安全公司并不明显，它们仍把 GPU 当作"ML 团队用的东西"，而不是"安全栈必须栖身的东西"。到 2024 年，同一家公司就在 GTC 上演示了在 NVIDIA GPU、DPU 和 Morpheus AI 上运行的抗量子密码学。2025 年的 Utimaco 联盟，通过为 AI 时代的负载做的 FIPS 140-2 Level 3 HSM 集成，闭环了这一环。

与此同时，Sean 还开了一段学术篇章。2018 年 1 月到 2021 年 6 月，他是深圳技术大学人工智能学院的特聘教授和创始院长，同时仍领导 Bloombase。2021 年 6 月到 2023 年 12 月，他是深圳 X-Institute 的讲席教授、联合创始人和执行总裁——正是我作为学生研究员待过两年半的那个 X-Institute。所以在我知道 Bloombase 是什么之前很久，他就已经是我间接遇见其工作的人之一。

他轨迹的职业形状教训很有意思，也有点让人不舒服。流行的叙事说，要造出持久之物你必须专注一件事。他在 Bloombase 专注于企业数据安全，但他也创办了一所深圳的 AI 学院、联合创办了一个研究机构、还持续发表。真正的专注是那句底层的技术论点（密码学、基础设施信任、平台层安全）。那句论点栖身的机构形态则多变。硅谷的公司、深圳的学院、同一座城市的研究机构，彼此互相强化。

Bloombase 的模式也反推了风投规模的叙事线。十二年过去，多个办公室（红木城、温哥华、法兰克福、香港）、一条长长的结盟轨迹、真实的营收、真实的客户，而公司并不是那个没有人会去发推文的独角兽。它是那种会安静地出现在你听过名字的组织的安全架构里的公司，而运营它的人做了一个刻意的选择：为这个而优化，而不是为光鲜的融资而优化。

对我这个研究者来说，元教训是时间跨度。在一个技术领域复利十二年，会产出一个没人能在两年周期里与之竞争的位置。眼前这个博士比那短，但它应该用同一种货币来衡量。无论我在 Noah-MP 里造的是什么，问题都是：它在 2040 年还会不会以某种形式运行。如果是，就值得做。如果不是，那可能根本不该开始。