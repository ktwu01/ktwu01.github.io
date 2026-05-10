---
title: "能源奇点与智能革命：可控核聚变全景深度研究报告——原理、商业化进程与Sam Altman的战略赌注"
date: 2026-01-05
permalink: /zh/posts/2026/01/nuclear-fusion-singularity/
tags:
  - energy
  - nuclear-fusion
  - ai
  - sam-altman
  - deep-dive
---

引言：AI 的算力尽头，是能源的终极解法。

> 作者：[Koutian Wu](https://www.linkedin.com/in/ktwu01/)；[GitHub: ktwu01](https://github.com/ktwu01/)

# 能源奇点与智能革命：可控核聚变全景深度研究报告——原理、商业化进程与Sam Altman的战略赌注

## 1. 执行摘要

2026年初，全球能源与科技产业正站在一个历史性的十字路口。可控核聚变（Controlled Nuclear Fusion），这一曾被视为“永远只有三十年之遥”的科学圣杯，正在经历从纯理论物理实验向硬科技工程落地的剧烈范式转移。本报告旨在对可控核聚变的物理原理、技术路径、工程瓶颈及商业化前景进行详尽的拆解与分析，并深入探讨OpenAI首席执行官Sam Altman为何将个人财富与声誉重注于这一领域，以及这种支持背后的深层逻辑。

当前，聚变能源的研发格局呈现出明显的二元分化：一方面是以ITER（国际热核聚变实验堆）和中国国家级项目（如CFETR）为代表的公共部门，它们致力于攻克氘氚（D-T）聚变的工程难题，追求大规模、稳态的基荷能源；另一方面是以Helion Energy、Commonwealth Fusion Systems (CFS) 为代表的私营企业，它们利用高温超导体、先进算法和新型约束构型，试图通过更紧凑、更快速的迭代实现商业突围。

本报告的核心发现指出，Sam Altman对核聚变——特别是对Helion Energy的投资，并非单纯的财务行为，而是其通用人工智能（AGI）大战略中不可或缺的一环。随着AI模型参数与算力需求的指数级增长，“智能的成本”将最终收敛于“能源的成本”。Altman对Helion的大力支持——体现在数亿美元的真金白银投入及微软购电协议的签署上——是真实且激进的。然而，这一赌注面临着巨大的物理与工程不确定性，特别是Helion所采用的磁惯性约束与氘-氦3燃料循环，虽然理论上拥有极高的经济性（直接电能捕获），但在2025-2026年间仍未完全兑现其“净发电”的公开承诺。

报告将分为七个主要章节，全面覆盖从原子核物理到底层供应链，从地缘政治竞争到硅谷资本逻辑的每一个维度。

---

## 2. 可控核聚变的物理学原理与核心挑战

核聚变是宇宙中能量产生的主导机制，为恒星提供动力。在地球上实现这一过程，需要克服极端的物理条件，将轻原子核结合成重原子核，并释放出巨大的结合能。

### 2.1 基本物理机制与库仑势垒

核聚变的本质是利用爱因斯坦质能方程 $$E=mc^2$$，通过质量亏损释放能量。最基础的反应涉及氢的同位素。然而，原子核带正电，彼此之间存在强大的静电排斥力（库仑力）。要发生聚变，原子核必须靠得足够近（费米尺度，$$10^{-15}$$米），以使短程的强核力克服长程的电磁排斥力。

这要求燃料处于等离子体状态（电子脱离原子核），并具备极高的动能。衡量聚变是否发生的标准被称为**劳森判据（Lawson Criterion）**，或者是“三重积”（Triple Product），即以下三个参数的乘积必须超过特定阈值：

1. **密度 ($$n$$)**：单位体积内的粒子数。
    
2. **温度 ($$T$$)**：通常以千电子伏特（keV）或亿摄氏度为单位。
    
3. **能量约束时间 ($$\tau_E$$)**：能量在等离子体中停留的时间。
    

目标是实现能量增益因子 $$Q > 1$$，即聚变产生的能量大于维持等离子体所需的输入能量。当 $$Q$$ 趋于无穷大时，聚变反应产生的阿尔法粒子足以维持等离子体温度，无需外部加热，这被称为**点火（Ignition）** 。

### 2.2 燃料循环：工程路径的分岔口

选择何种燃料组合，直接决定了反应堆的物理设计、工程难度及经济模型。这是理解Helion与主流托卡马克路线差异的关键。

**表 1：主要核聚变燃料循环的物理特性与工程影响对比**

|**燃料循环**|**反应式**|**点火温度要求**|**中子产额与能量**|**优点**|**缺点**|
|---|---|---|---|---|---|
|**氘-氚 (D-T)**|$$^2H + ^3H \rightarrow ^4He + n$$|~1.5亿 °C (15 keV)|**极高** (80%能量为14.1 MeV中子)|反应截面最大（最易发生）；能量输出高。|需要氚增殖（氚天然稀缺）；高能中子严重损伤材料；必须使用蒸汽轮机循环。|
|**氘-氘 (D-D)**|$$^2H + ^2H \rightarrow ^3He + n$$ 或 $$T + p$$|~5亿 °C|中等|燃料来源极丰富（海水）；无需初始氚。|反应截面低；仍产生显著中子辐射。|
|**氘-氦3 (D-He3)**|$$^2H + ^3He \rightarrow ^4He + p$$|~6-10亿 °C|**极低** (<5%能量为中子)|**无中子潜力**；产物主要为带电质子，可**直接发电**；辐射低。|氦-3在地球极度稀缺；点火温度极高，约束极难。|
|**质子-硼11 (p-B11)**|$$p + ^{11}B \rightarrow 3 ^4He$$|~10亿 °C|几乎为零|燃料丰富；完全无中子；产物清洁。|物理上极难实现；韧致辐射损失可能超过聚变产出。|

_分析：_ 目前，ITER、CFS（SPARC）及中国的大部分项目均采用 **D-T** 路线，因为其物理门槛最低。然而，D-T 反应释放的高能中子无法被磁场约束，会直接轰击反应堆内壁，这就需要笨重的“增殖包层”来吸收中子并将热能转化为蒸汽，再去推动汽轮机发电。这一过程工程极其复杂且效率受限于卡诺循环。相比之下，Helion选择 **D-He3** 路线，旨在利用带电产物进行磁感应直接发电，这在大规模商业化上具有巨大的系统简化优势，但物理难度呈指数级上升 。

### 2.3 约束方式的演进：从磁场到惯性

#### 2.3.1 磁约束核聚变 (MCF)

利用带电粒子在磁场中做螺旋运动的特性，将其约束在特定的几何形状中。

- **托卡马克 (Tokamak)**：外形如甜甜圈（环形）。利用外部环向磁场和等离子体内部电流产生的极向磁场，以此合成螺旋磁场来约束等离子体。
    
    - _现状_：技术最成熟，ITER及中国的EAST、HL-3均属此类。
        
    - _局限_：等离子体电流可能导致扭曲模不稳定性，引发“破裂”（Disruption），瞬间释放的能量可能损坏装置 。
        
- **仿星器 (Stellarator)**：完全依靠外部扭曲的线圈产生螺旋磁场，无需等离子体电流。
    
    - _现状_：以德国W7-X为代表。
        
    - _优势_：固有稳定性好，适合稳态运行。
        
    - _局限_：磁体设计与制造工艺极端复杂。
        

#### 2.3.2 惯性约束核聚变 (ICF)

利用高能驱动器（激光或离子束）轰击微小的燃料靶丸，使其外层瞬间烧蚀爆炸，产生反向冲击波将燃料向内压缩至极高密度。

- _现状_：美国国家点火装置（NIF）在2022年实现了科学增益（Q>1）。
    
- _局限_：脉冲频率极低（一天几次），激光效率低，难以转化为连续电能 。
    

#### 2.3.3 磁惯性约束 (MIF) —— 第三种路径

结合了MCF的磁场隔热与ICF的脉冲压缩。

- _原理_：首先生成一个磁化等离子体团（如场反向构型 FRC），然后利用磁场对其进行快速压缩。
    
- _代表_：**Helion Energy**。
    
- _优势_：可以达到比托卡马克更高的密度，同时比激光聚变具有更长的约束时间。最关键的是，脉冲式的压缩与膨胀过程天然适合直接电能回收 。
    

---

## 3. 全球发展格局与地缘技术竞争

到2026年，核聚变领域已不再是纯粹的科学合作，而是演变为国家战略竞争与私营资本博弈的复杂战场。

### 3.1 国家队：巨人的进击与迟缓

**ITER（国际热核聚变实验堆）**：

作为由欧盟、中国、美国、俄罗斯等七方参与的巨型项目，ITER旨在验证聚变堆的工程可行性。

- _2026年状态_：项目深受延期困扰。尽管大部分土建与核心部件安装已完成，但预计的氘-氚运行时间已推迟至2039年，D-D等离子体实验也推迟至2035年。ITER的庞大体量使其在灵活性上无法与私营公司相比，但其在材料辐照、氚增殖包层测试（TBM）方面的基础研究仍无可替代 。
    

**中国的战略加速**：

中国将核聚变视为能源安全的终极保障，并在国家层面制定了清晰的“三步走”战略（热堆-快堆-聚变堆）。

- **装置突破**：2025年，新一代人造太阳 **HL-3（环流三号）** 实现了100万安培电流运行，核心离子温度突破1亿度；**EAST（东方超环）** 在2025年1月创下了维持等离子体运行1066秒的世界纪录 。
    
- **体制创新**：2025年中期，中国正式成立了国家级平台 **中国聚变能源有限公司（China Fusion Energy Co Ltd）**，由中核集团牵头，整合了中国科学院、三峡集团等25家央企与科研机构的力量，旨在举国体制下加速 **CFETR（中国聚变工程实验堆）** 的建设 。CFETR的目标是在2030-2035年间建成，不仅要实现燃烧等离子体，还要解决氚自持这一关键工程难题 。
    
- **混合堆路径**：据报道，中国还在推进聚变-裂变混合堆项目（如江西的“星火”项目），利用聚变产生的中子驱动裂变材料，这被视为一条更早实现商业应用的折中路线 。
    

### 3.2 私营部门（Fusion 2.0）：资本驱动的敏捷开发

截至2025年，全球私营聚变公司融资总额已接近100亿美元 。这些公司采用“快速失败、快速迭代”的硅谷模式。

**表 2：全球主要私营聚变企业技术路线与2026年状态对比**

|**公司**|**总部**|**技术路线**|**关键差异点**|**2026年预期状态/里程碑**|**知名投资方**|
|---|---|---|---|---|---|
|**Helion Energy**|美国|脉冲磁惯性 (MIF) + FRC|氘-氦3燃料；**直接发电**；无蒸汽循环；工厂量产模式。|原计划2024净发电未达成；Polaris原型机正在调试运行；致力于2028年微软供电。|Sam Altman, Peter Thiel, Microsoft|
|**Commonwealth Fusion Systems (CFS)**|美国|紧凑型托卡马克 (SPARC)|高温超导磁体 (REBCO)；强磁场缩小体积；传统的D-T热循环。|SPARC装置组装中；预计2026/2027年实现首次等离子体及Q>1验证。|Bill Gates, Google, MIT|
|**Tokamak Energy**|英国|球形托卡马克|高温超导；球形构型提高贝塔值（效率）。|推进ST80-HTS原型机；磁体技术验证。|英国政府, 私募基金|
|**Zap Energy**|美国|Z-Pinch (Z箍缩)|无磁体线圈；利用剪切流稳定等离子体；结构极其简单。|验证“剪切流稳定”在更高电流下的有效性；无需昂贵磁体。|Chevron, Bill Gates|
|**General Fusion**|加拿大|磁化靶聚变 (MTF)|液态金属（铅锂）衬套；活塞压缩；液态壁保护。|在英国建设LM26示范装置；验证液态金属压缩效率。|Jeff Bezos|

---

## 4. 工程瓶颈：从物理可行性到商业可行性

即使物理上实现了 $$Q>1$$（如NIF所做的那样），商业化聚变电站仍面临三大“灰犀牛”级别的工程挑战。私营公司往往在宣传中淡化这些问题，但它们是决定成败的根本。

### 4.1 材料的“中子噩梦”

在D-T聚变中，80%的能量以14.1 MeV的高能中子形式释放。这种能量是裂变反应堆中子的10倍以上。

- **原子位移 (dpa)**：高能中子会撞击反应堆壁材料的晶格原子，使其移位。在其服役寿命内，每个原子可能被撞离原位上百次。这会导致材料脆化、肿胀和断裂。
    
- **活化**：中子轰击会使原本非放射性的结构材料（如钢）变成放射性废料。
    
- _现状_：目前尚无任何材料能在商业聚变堆所需的通量下长期生存。IFMIF（国际聚变材料辐照设施）等项目正在建设中，但材料科学的进展严重滞后于等离子体物理 。
    

### 4.2 氚增殖：关闭燃料循环

氚（Tritium）半衰期仅12.3年，地球上几乎没有天然氚。目前的氚主要来自重水堆（CANDU）的副产品，全球存量仅约25-30公斤，极其昂贵（约30,000美元/克）。

- **增殖包层**：商业D-T堆必须“自给自足”，即利用聚变产生的中子与锂反应生产氚（$$n + ^6Li \rightarrow T + ^4He$$）。
    
- **挑战**：氚增殖比（TBR）必须大于1。这意味着不仅要捕获每一个中子，还要弥补中子在结构材料中的损耗。目前该技术从未在全尺寸反应堆中验证过 。
    
- _注_：这也是Helion选择D-He3路线的核心原因——试图绕过氚增殖和中子损伤的难题，尽管它们面临着氦-3来源的新难题。
    

### 4.3 热提取与经济性

托卡马克利用偏滤器（Divertor）排出废热和氦灰。偏滤器靶板面临的热负荷可能超过 $$10-20 MW/m^2$$，相当于航天飞机重返大气层时热负荷的数倍，且需持续运行。 此外，要与太阳能+储能竞争，聚变电价需降至50美元/MWh以下。庞大的托卡马克+蒸汽轮机系统的资本支出（CAPEX）极高，这使得CFS等公司必须追求极致的紧凑化，而Helion则追求直接发电的系统简化 。

---

## 5. 深度剖析：Sam Altman、Helion Energy 与 AI 的战略绑定

Sam Altman不仅是Helion的投资者，更是其商业叙事的构建者。要理解这一支持，必须将其置于Altman对未来世界图景的构想中：一个算力与能源均为无限供给的时代。

### 5.1 Helion Energy 的技术特异性

Helion的技术路径（磁惯性约束+D-He3+直接发电）在聚变领域是绝对的异类。

1. **场反向构型 (FRC)**：Helion不使用托卡马克那种外部线圈强行约束，而是生成两个像烟圈一样的等离子体团（FRC），它们自身携带电流并产生磁场。
    
2. **脉冲对撞与压缩**：两个FRC以每小时100万英里的速度在燃烧室中心对撞合并，然后利用外部磁场在微秒级时间内将其压缩到极高密度和温度。
    
3. **直接能量捕获**：这是Helion的“杀手锏”。当聚变发生，带电产物（质子和阿尔法粒子）推动等离子体膨胀，反推磁场。根据法拉第电磁感应定律，磁通量的变化在外部线圈中感应出电流。
    
    - _意义_：这使得发电过程像再生制动（Regenerative Braking）一样高效，理论转换效率可达95%，且无需昂贵的蒸汽轮机和冷却塔 。
        
4. **氦-3 来源**：Helion计划通过 D-D 副反应自产氦-3（D+D反应有50%几率产生氦-3，50%几率产生氚，氚衰变后也是氦-3）。这闭环了燃料链，但也意味着在早期阶段它们仍需处理D-D反应产生的中子 。
    

### 5.2 Sam Altman 支持的深层逻辑：AI 的物理极限

为什么是核聚变？为什么是Helion？

用户提出的“为什么大力支持”可以归结为以下三点核心逻辑：

1. **算力-能源等价论**： Altman在参议院听证会及多次访谈中明确表示：“没有能源突破，就无法实现AGI（通用人工智能）。” 。
    
    - _数据支撑_：随着模型参数量和训练数据量的指数增长，以及推理阶段（Inference）的大规模应用，AI数据中心的能耗正在爆炸式增长。单个ChatGPT查询的能耗是传统Google搜索的10-100倍 。
        
    - _愿景_：Altman认为，未来的智能成本将由能源成本决定。如果能源不能像摩尔定律那样下降，AI的普及将受阻。
        
2. **制造而非建造 (Manufacturing vs Construction)**：
    
    Altman偏爱Helion的另一个原因是其工程哲学。
    
    - 托卡马克（如ITER或CFS）是类似于核电站的土木工程项目，建设周期长，监管复杂。
        
    - Helion的装置（Polaris）大小如集装箱，且由数千个标准化的电容器和磁体组成。这意味着它们可以在工厂里批量生产，然后运到数据中心旁安装。这符合硅谷“软件定义硬件”、“可扩展性优先”的投资逻辑 。
        
3. **时间窗口的匹配**： Renewables（风光）虽然便宜，但即便配合储能，也难以满足吉瓦级（GW）数据中心24/7的稳定性需求（"Five Nines"可靠性）。裂变核电虽稳，但审批和建设周期动辄10年。Helion承诺的2028年供电，虽然激进，但在时间线上是唯一能与OpenAI计算集群扩容计划相匹配的基荷电源方案 。
    

### 5.3 他真的“大力支持”了吗？—— 事实核查

**结论：是的，支持力度是空前的，且具有排他性战略意义。**

- **真金白银的投入**：
    
    - 2021年，Altman个人向Helion投资了 **3.75亿美元**（Series E）。这在当时是他个人最大的单笔投资，远超他在其他初创公司的投入 。
        
    - 2025年1月，Helion宣布了 **4.25亿美元** 的F轮融资，Altman再次跟投，并继续担任董事会主席 。
        
- **声誉押注与商业绑定**：
    
    - Altman促成了 **微软与Helion的购电协议 (PPA)**。协议规定Helion需从2028年起向微软提供50 MW电力。这不仅仅是一个意向书，而是包含违约金条款的正式商业合同。微软作为OpenAI的最大金主，这一合同实际上将OpenAI的算力命运与Helion的成败通过Altman绑定在了一起 。
        
    - 在2025年的参议院听证会上，Altman公开将Helion作为美国在AI时代保持竞争力的关键基础设施进行背书 。
        

### 5.4 现状核查：承诺与现实的落差 (2025-2026)

虽然支持是真实的，但技术进展是否如愿？

- **错过的里程碑**：Helion曾在2021年高调承诺，其第7代原型机 **Polaris** 将在2024年演示“净发电”（Net Electricity）。然而，截至2026年初，这一目标 **未能实现**。
    
- **当前状态**：Polaris已在2024年底建成，并在2025年中期开始运行，产生了大尺寸FRC等离子体，但尚未公开宣布实现净电输出 。
    
- **外界质疑**：物理学界对Helion的批评集中在其从未在同行评审期刊上发表足够的数据。D-He3所需的温度比D-T高得多（近10亿度），而FRC在如此极端条件下的稳定性在主流等离子体物理中被认为是极其困难的。有批评者指出，Helion的激进时间表带有典型的“硅谷式夸大”（如Theranos），利用风投圈对物理的无知进行融资 。
    
- **辩护**：Helion的支持者认为，他们选择不公开数据是为了保护知识产权（防止被竞争对手复制），且F轮融资的完成表明，尽管公开里程碑延期，但内部数据足以说服SoftBank和Altman继续注资 。
    

---

## 6. 应用与未来发展前景

如果（这是一个巨大的“如果”）核聚变，特别是Helion这类紧凑型方案能成功，其影响将超越电力行业。

### 6.1 深度脱碳与基荷电源

这是最直接的应用。聚变电站可以像燃煤电厂一样提供稳定的基荷电力，但零碳排放。对于拥有庞大重工业（钢铁、化工）和超大城市群的国家（如中国），聚变是替代化石能源的终极方案。

### 6.2 工业供热与制氢

高温超导托卡马克和Helion的废热（即使是直接发电，也会有热损耗）可以用于高温电解水制氢或直接驱动工业流程，进一步替代天然气。

### 6.3 空间推进 (Space Propulsion)

Helion的技术（磁脉冲喷射）本质上是一种等离子体引擎。如果稍加改造，它可以作为高比冲、大推力的航天推进器，将人类往返火星的时间从几个月缩短到几周。这也是Helion创始人David Kirtley经常提及的长期愿景 。

### 6.4 经济重构

廉价、无限的能源将使海水淡化、垂直农业、碳捕获（Direct Air Capture）等目前因能耗过高而无法大规模推广的技术变得经济可行。正如Altman所言，这将导致“物质的边际成本趋向于零”。

---

## 7. 结论

2026年的可控核聚变领域，正处于黎明前最混沌的时刻。

**技术层面**：物理原理已通过科学验证（NIF的点火、托卡马克的高约束模），但工程实现的鸿沟（材料、氚、热负荷）依然深不见底。中国通过举国体制稳步推进传统的托卡马克路线，提供了确定性最高的保底方案；而以Helion为首的美国私营公司则在进行一场高风险的赌博，试图通过物理机制的创新来规避工程难题。

**Altman的角色**：Sam Altman的大力支持是毋庸置疑的。他并非被动等待技术成熟，而是试图通过巨额资本和市场订单强行催熟一项技术。他的赌注建立在两个判断之上：一是AI对能源的渴求将很快耗尽现有电网的潜力；二是只有类似Helion这种可工厂化制造、直接发电的聚变方案，才能跟上AI指数级扩张的步伐。

**最终展望**：Helion错过了2024年的最后期限，这在硬科技创业中并不罕见，但也增加了风险。未来2-3年（2026-2028）将是决定性的。如果Polaris能实现净发电，或者CFS的SPARC能实现Q>1，聚变将瞬间成为全球最大的投资风口。反之，如果这些项目遭遇物理学的“硬墙”，行业将面临漫长的寒冬。但无论如何，人类在瓶中以此规模控制恒星之火的尝试，已进入了不可逆转的冲刺阶段。

---

### 表 3：Helion Energy 原型机迭代与状态

|**原型机代号**|**时期**|**目标/成就**|**状态**|
|---|---|---|---|
|**IPA / Venti**|2005-2012|验证FRC的形成与加速；验证D-D中子产生。|已退役|
|**Grande**|2013-2014|验证磁压缩效率；等离子体温度达到keV级别。|已退役|
|**Trenta**|2018-2023|实现了1亿度（9 keV）离子温度；运行超过1万次脉冲；验证了能量回收电路。|2023年退役，为Polaris让路|
|**Polaris**|2024-今|**目标：** 演示净电力输出（Net Electricity）。<br><br>  <br><br>**现状：** 2024年底建成，2025年运行中，尚未宣布达成净电目标。|**运行中** (关键验证期)|
|**Antares (计划)**|2028+|首个商业化电站；向微软交付50 MW电力。|规划中，依赖Polaris的成功|

_(注：本报告所有数据基于2026年1月前可获得的公开信息及行业分析整理。)_

  

[

![](https://t2.gstatic.com/faviconV2?url=https://www.reddit.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

reddit.com

Opens in a new window](https://www.reddit.com/r/askscience/comments/81aevl/what_is_the_difference_between_inertial/#:~:text=Inertial%20confinement%20focuses%20on%20compressing,creating%20a%20more%20sustained%20reaction.)[

![](https://t3.gstatic.com/faviconV2?url=https://www.nationalacademies.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

nationalacademies.org

Chapter: 2 Technical Background - National Academies of Sciences, Engineering, and Medicine

Opens in a new window](https://www.nationalacademies.org/read/18288/chapter/4)[

![](https://t2.gstatic.com/faviconV2?url=https://en.wikipedia.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

en.wikipedia.org

Helion Energy - Wikipedia

Opens in a new window](https://en.wikipedia.org/wiki/Helion_Energy)[

![](https://t2.gstatic.com/faviconV2?url=https://www.reddit.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

reddit.com

Helion's Unique Approach to Renewable Energy : r/fusion - Reddit

Opens in a new window](https://www.reddit.com/r/fusion/comments/1op2ppc/helions_unique_approach_to_renewable_energy/)[

![](https://t2.gstatic.com/faviconV2?url=https://www.goldsea.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

goldsea.com

Commercial Fusion Power Faces 3 More Epic Tech Hurdles | GOLDSEA

Opens in a new window](https://www.goldsea.com/article_details/commercial-fusion-power-faces-3-more-decades-of-hurdles)[

![](https://t3.gstatic.com/faviconV2?url=https://www.epj-conferences.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

epj-conferences.org

Inertial confinement fusion: Recent results and perspectives - EPJ Web of Conferences

Opens in a new window](https://www.epj-conferences.org/articles/epjconf/pdf/2024/20/epjconf_lnes2024_00013.pdf)[

![](https://t2.gstatic.com/faviconV2?url=https://en.wikipedia.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

en.wikipedia.org

Fusion power - Wikipedia

Opens in a new window](https://en.wikipedia.org/wiki/Fusion_power)[

![](https://t3.gstatic.com/faviconV2?url=https://www.helionenergy.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

helionenergy.com

More on Helion's pulsed approach to fusion | Helion

Opens in a new window](https://www.helionenergy.com/articles/more-on-helions-pulsed-approach-to-fusion/)[

![](https://t3.gstatic.com/faviconV2?url=https://www.helionenergy.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

helionenergy.com

Technology - Helion

Opens in a new window](https://www.helionenergy.com/technology/)[

![](https://t2.gstatic.com/faviconV2?url=https://en.wikipedia.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

en.wikipedia.org

ITER - Wikipedia

Opens in a new window](https://en.wikipedia.org/wiki/ITER)[

![](https://t0.gstatic.com/faviconV2?url=https://www.iter.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

iter.org

Tritium breeding - ITER

Opens in a new window](https://www.iter.org/machine/supporting-systems/tritium-breeding)[

![](https://t0.gstatic.com/faviconV2?url=https://en.cnnc.com.cn/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

en.cnnc.com.cn

China sets new records in the research of new-generation "artificial sun" HL-3

Opens in a new window](https://en.cnnc.com.cn/2025-03/31/c_1082798.htm)[

![](https://t2.gstatic.com/faviconV2?url=https://en.wikipedia.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

en.wikipedia.org

Experimental Advanced Superconducting Tokamak - Wikipedia

Opens in a new window](https://en.wikipedia.org/wiki/Experimental_Advanced_Superconducting_Tokamak)[

![](https://t1.gstatic.com/faviconV2?url=https://www.energy-reporters.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

energy-reporters.com

"Scientists Shiver in Awe" as New Fusion Breakthrough Ignites Energy Revolution That Could Change the World

Opens in a new window](https://www.energy-reporters.com/news/scientists-shiver-in-awe-as-new-fusion-breakthrough-ignites-energy-revolution-that-could-change-the-world/)[

![](https://t3.gstatic.com/faviconV2?url=https://policycn.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

policycn.com

fusion energy SOE launched in Shanghai - PRC commentary | China Policy

Opens in a new window](https://policycn.com/public/commentaries/fusion-energy-soe-launched-in-shanghai-50172)[

![](https://t2.gstatic.com/faviconV2?url=https://en.wikipedia.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

en.wikipedia.org

China Fusion Engineering Test Reactor - Wikipedia

Opens in a new window](https://en.wikipedia.org/wiki/China_Fusion_Engineering_Test_Reactor)[

![](https://t1.gstatic.com/faviconV2?url=https://www.nucnet.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

nucnet.org

China Aims To Operate World's First Hybrid Fusion-Fission Nuclear Plant By 2030 - NucNet

Opens in a new window](https://www.nucnet.org/news/china-aims-to-operate-world-s-first-hybrid-fusion-fission-nuclear-plant-by-2030-3-5-2025)[

![](https://t1.gstatic.com/faviconV2?url=https://www.peaknano.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

peaknano.com

The State of the Fusion Energy Industry in 2025: A Global Transformation in Progress

Opens in a new window](https://www.peaknano.com/blog/the-state-of-the-fusion-energy-industry-in-2025)[

![](https://t0.gstatic.com/faviconV2?url=https://www.nae.edu/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

nae.edu

Materials Challenges for Fusion Energy - National Academy of Engineering

Opens in a new window](https://www.nae.edu/7558/MaterialsChallengesforFusionEnergy)[

![](https://t0.gstatic.com/faviconV2?url=https://scientific-publications.ukaea.uk/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

scientific-publications.ukaea.uk

Materials Challenges for Successful Roll-out of Commercial Fusion Reactors - UKAEA Scientific Publications

Opens in a new window](https://scientific-publications.ukaea.uk/wp-content/uploads/UKAEA-CCFE-PR2152.PDF)[

![](https://t0.gstatic.com/faviconV2?url=https://energy.sustainability-directory.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

energy.sustainability-directory.com

Tritium Breeding Challenges → Term - Energy → Sustainability Directory

Opens in a new window](https://energy.sustainability-directory.com/term/tritium-breeding-challenges/)[

![](https://t2.gstatic.com/faviconV2?url=https://www.fundacionbankinter.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

fundacionbankinter.org

Fusion Energy: From Scientific Promise to Technological - Fundación Innovación Bankinter

Opens in a new window](https://www.fundacionbankinter.org/wp-content/uploads/2025/07/Future-Trends-Forum-Report-Preview-%E2%80%93-FusionForward-2025.pdf)[

![](https://t0.gstatic.com/faviconV2?url=https://www.energycouncil.com.au/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

energycouncil.com.au

Nuclear Fusion Deals – Based on reality or a dream? - Australian Energy Council

Opens in a new window](https://www.energycouncil.com.au/analysis/nuclear-fusion-deals-based-on-reality-or-a-dream/)[

![](https://t0.gstatic.com/faviconV2?url=https://www.youtube.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

youtube.com

Helion's approach to fusion: How it works - YouTube

Opens in a new window](https://www.youtube.com/watch?v=HlNfP3iywvI)[

![](https://t1.gstatic.com/faviconV2?url=https://www.nucnet.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

nucnet.org

Nuclear Fusion / OpenAI Boss Sam Altman 'Motivated To Invest More' - NucNet

Opens in a new window](https://www.nucnet.org/news/openai-boss-sam-altman-motivated-to-invest-more-1-4-2024)[

![](https://t2.gstatic.com/faviconV2?url=https://www.energycentral.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

energycentral.com

OpenAI CEO Altman Says Future of AI Depends on an Energy Breakthrough

Opens in a new window](https://www.energycentral.com/energy-biz/post/openai-ceo-altman-says-future-ai-depends-energy-breakthrough-PumCqEWpu8jh08z)[

![](https://t2.gstatic.com/faviconV2?url=https://futurism.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

futurism.com

Sam Altman Says AI Using Too Much Energy, Will Require Breakthrough Energy Source

Opens in a new window](https://futurism.com/sam-altman-energy-breakthrough)[

![](https://t2.gstatic.com/faviconV2?url=https://www.reddit.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

reddit.com

Can someone ELI5 Helion's controversy ? : r/fusion - Reddit

Opens in a new window](https://www.reddit.com/r/fusion/comments/1dlmfu2/can_someone_eli5_helions_controversy/)[

![](https://t0.gstatic.com/faviconV2?url=https://techfundingnews.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

techfundingnews.com

Sam Altman-backed Helion raises $425M: Can fusion energy finally deliver clean power for Microsoft? - Tech Funding News

Opens in a new window](https://techfundingnews.com/helion-secures-425m-to-advance-fusion-energy/)[

![](https://t0.gstatic.com/faviconV2?url=https://observer.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

observer.com

8 Startups Sam Altman Invested in Outside OpenAI in 2025 - Observer

Opens in a new window](https://observer.com/2025/12/sam-altman-startup-investments-2025/)[

![](https://t0.gstatic.com/faviconV2?url=https://www.cleantechalliance.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

cleantechalliance.org

Sam Altman, SoftBank invest in $425M round for Helion, a Seattle-area startup chasing fusion power - CleanTech Alliance

Opens in a new window](https://www.cleantechalliance.org/2025/01/29/sam-altman-softbank-invest-in-425m-round-for-helion-a-seattle-area-startup-chasing-fusion-power/)[

![](https://t3.gstatic.com/faviconV2?url=https://www.helionenergy.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

helionenergy.com

Helion Announces $425M Series F Investment to Scale Commercialized Fusion Power

Opens in a new window](https://www.helionenergy.com/articles/helion-announces-425m-series-f-investment-to-scale-commercialized-fusion-power/)[

![](https://t0.gstatic.com/faviconV2?url=https://www.heraldnet.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

heraldnet.com

Helion celebrates smoother path to fusion energy site approval | HeraldNet.com

Opens in a new window](https://www.heraldnet.com/news/helion-celebrates-smoother-path-to-fusion-energy-site-approval/)[

![](https://t2.gstatic.com/faviconV2?url=https://www.techpolicy.press/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

techpolicy.press

Transcript: Sam Altman Testifies At US Senate Hearing On AI Competitiveness

Opens in a new window](https://www.techpolicy.press/transcript-sam-altman-testifies-at-us-senate-hearing-on-ai-competitiveness/)[

![](https://t2.gstatic.com/faviconV2?url=https://www.reddit.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

reddit.com

Helion said that Polaris should demonstrate electricity this year. Now it is the end of the year. : r/fusion - Reddit

Opens in a new window](https://www.reddit.com/r/fusion/comments/1ptp513/helion_said_that_polaris_should_demonstrate/)[

![](https://t2.gstatic.com/faviconV2?url=https://www.reddit.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

reddit.com

Can we talk about Helion? : r/fusion - Reddit

Opens in a new window](https://www.reddit.com/r/fusion/comments/133ttne/can_we_talk_about_helion/)[

![](https://t1.gstatic.com/faviconV2?url=https://www.geekwire.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

geekwire.com

Helion gives behind-the-scenes tour of secretive 60-foot fusion prototype as it races to deployment - GeekWire

Opens in a new window](https://www.geekwire.com/2025/helion-gives-behind-the-scenes-tour-of-secretive-60-foot-fusion-prototype-as-it-races-to-deployment/)[

![](https://t3.gstatic.com/faviconV2?url=https://www.helionenergy.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

helionenergy.com

Trenta's final fusion test campaign - Helion

Opens in a new window](https://www.helionenergy.com/articles/ending-trenta-operations/)[

![](https://t2.gstatic.com/faviconV2?url=https://en.wikipedia.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

en.wikipedia.org

Opens in a new window](https://en.wikipedia.org/wiki/Helion_Energy#:~:text=As%20of%20mid%2D2025%2C%20Helion,the%20end%20of%20the%20year.)

[

![](https://t2.gstatic.com/faviconV2?url=https://www.reddit.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://www.reddit.com/r/askscience/comments/81aevl/what_is_the_difference_between_inertial/)[

![](https://t0.gstatic.com/faviconV2?url=https://www.iaea.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://www.iaea.org/newscenter/news/fusion-energy-in-2025-six-global-trends-to-watch)[

![](https://t2.gstatic.com/faviconV2?url=https://english.www.gov.cn/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://english.www.gov.cn/news/202510/20/content_WS68f63030c6d00ca5f9a06eff.html)[

![](https://t0.gstatic.com/faviconV2?url=https://www.iter.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://www.iter.org/node/20687/fusion-consensus-strengthening)[

![](https://t2.gstatic.com/faviconV2?url=https://en.wikipedia.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://en.wikipedia.org/wiki/Sam_Altman)[

![](https://t0.gstatic.com/faviconV2?url=https://observer.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://observer.com/2025/01/sam-altman-nuclear-fusion-startup-fundraising/)[

![](https://t1.gstatic.com/faviconV2?url=https://www.popsci.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://www.popsci.com/technology/sam-altman-age-of-ai-will-require-an-energy-breakthrough/)[

![](https://t3.gstatic.com/faviconV2?url=https://www.helionenergy.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://www.helionenergy.com/faq/)[

![](https://t2.gstatic.com/faviconV2?url=https://www.frontiersin.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://www.frontiersin.org/journals/energy-research/articles/10.3389/fenrg.2023.1157394/full)[

![](https://t0.gstatic.com/faviconV2?url=https://www.researchgate.net/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://www.researchgate.net/publication/397082192_Breakthrough_in_China's_Fusion_Energy_HL-3_Tokamak_Achieves_High_Ion_Temperature_and_Fusion_Triple_Product)[

![](https://t1.gstatic.com/faviconV2?url=https://www.the-innovation.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://www.the-innovation.org/article/id/691d6fe37a2be313aa3f23c2)[

![](https://t2.gstatic.com/faviconV2?url=https://www.reddit.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://www.reddit.com/r/fusion/comments/10g95m9/the_problems_with_helion_energy_a_response_to/)[

![](https://t3.gstatic.com/faviconV2?url=https://forum.kerbalspaceprogram.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://forum.kerbalspaceprogram.com/topic/216068-helion-energy/)[

![](https://t2.gstatic.com/faviconV2?url=https://businesscraft.se/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://businesscraft.se/business/helion-cfs-tokamak-energy-tae-how-fusion-technologies-are-diverging-by-2026/)[

![](https://t2.gstatic.com/faviconV2?url=https://www.reddit.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://www.reddit.com/r/fusion/comments/1iqxctv/whats_different_about_helion_energy_the_nuclear/)[

![](https://t2.gstatic.com/faviconV2?url=https://www.reddit.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://www.reddit.com/r/fusion/comments/1ppxqx4/commonwealth_fusion_system_helion_tae_inside_the/)[

![](https://t2.gstatic.com/faviconV2?url=https://www.reddit.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://www.reddit.com/r/fusion/comments/17nuol3/do_you_think_that_cfs_or_helion_will_achieve/)[

![](https://t0.gstatic.com/faviconV2?url=https://www.fusionindustryassociation.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://www.fusionindustryassociation.org/tag/supply-chain/)[

![](https://t0.gstatic.com/faviconV2?url=https://ukaea.maglr.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://ukaea.maglr.com/supply-chain-aug-2025/fia-supply-chain-report)[

![](https://t0.gstatic.com/faviconV2?url=https://www.fusionindustryassociation.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://www.fusionindustryassociation.org/wp-content/uploads/2025/06/FIA-Supply-Chain-2025-Report.pdf)[

![](https://t0.gstatic.com/faviconV2?url=https://www.fusionindustryassociation.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://www.fusionindustryassociation.org/wp-content/uploads/2025/12/FIA-2025-Year-in-Review.pdf?mc_cid=7dc68615f1&mc_eid=a9957f7166)[

![](https://t3.gstatic.com/faviconV2?url=https://www.scsp.ai/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://www.scsp.ai/wp-content/uploads/2025/10/Fusion-Commission-Fall-2025-Report-Draft.pdf)[

![](https://t1.gstatic.com/faviconV2?url=https://www-pub.iaea.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://www-pub.iaea.org/MTCD/publications/PDF/p15935-25-02871E_WFO25_web.pdf)[

![](https://t2.gstatic.com/faviconV2?url=https://www.reddit.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://www.reddit.com/r/fusion/comments/1hv3ugl/sam_altman_i_would_expect_helion_will_show_you/)[

![](https://t3.gstatic.com/faviconV2?url=https://www.talk-polywell.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://www.talk-polywell.org/bb/viewtopic.php?t=6499&start=855)[

![](https://t2.gstatic.com/faviconV2?url=https://www.techpolicy.press/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://www.techpolicy.press/ai-doesnt-need-more-energy-it-needs-less-concentration-of-power/)[

![](https://t3.gstatic.com/faviconV2?url=https://www.helionenergy.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://www.helionenergy.com/articles/announcing-500-million-fundraise/)[

![](https://t2.gstatic.com/faviconV2?url=https://www.reddit.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://www.reddit.com/r/fusion/comments/1ow2fte/helion_news_letter_progress_keeps_us_on_track_to/)[

![](https://t0.gstatic.com/faviconV2?url=https://english.cas.cn/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://english.cas.cn/newsroom/cas_media/202510/t20251015_1089475.shtml)[

![](https://t2.gstatic.com/faviconV2?url=https://www.reddit.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://www.reddit.com/r/nuclear/comments/1q2yaut/chinese_reactor_construction_charts_january_2026/)[

![](https://t3.gstatic.com/faviconV2?url=https://www.moomoo.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://www.moomoo.com/news/post/63408118/the-industry-s-inaugural-year-is-being-driven-by-the)[

![](https://t0.gstatic.com/faviconV2?url=https://www.iaea.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://www.iaea.org/about/organizational-structure/department-of-nuclear-energy/webinars/challenges-and-advances-of-technology-development-for-fusion-energy-webinar-series/global-approaches-to-tritium-breeding-for-fusion)[

![](https://t0.gstatic.com/faviconV2?url=https://conferences.iaea.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://conferences.iaea.org/event/406/contributions/)[

![](https://t2.gstatic.com/faviconV2?url=https://www.energy.gov/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://www.energy.gov/articles/epri-fusion-blankets-report-2024)[

![](https://t2.gstatic.com/faviconV2?url=https://research.contrary.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://research.contrary.com/company/helion)[

![](https://t2.gstatic.com/faviconV2?url=https://www.reddit.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://www.reddit.com/r/fusion/comments/1q0fcm7/2025_at_helion/)[

![](https://t3.gstatic.com/faviconV2?url=https://talk-polywell.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://talk-polywell.org/bb/viewtopic.php?t=6499&start=930)[

![](https://t2.gstatic.com/faviconV2?url=https://time.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://time.com/7328213/nuclear-fusion-energy-ai/)[

![](https://t2.gstatic.com/faviconV2?url=https://www.reddit.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://www.reddit.com/r/fusion/comments/1onhlkz/scam_altman_the_technological_landscape_shifts_in/)[

![](https://t0.gstatic.com/faviconV2?url=https://www.ted.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://www.ted.com/pages/sam-altman-on-the-future-of-ai-and-humanity-transcript)[

![](https://t3.gstatic.com/faviconV2?url=https://www.helionenergy.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://www.helionenergy.com/polaris/)[

![](https://t2.gstatic.com/faviconV2?url=https://www.reddit.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://www.reddit.com/r/fusion/comments/1pkue34/the_first_look_at_polaris_helions_latest_nuclear/)

![](https://www.gstatic.com/lamda/images/immersives/google_logo_icon_2380fba942c84387f09cf.svg)

[![](https://t2.gstatic.com/faviconV2?url=https://www.reddit.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

](https://www.reddit.com/r/askscience/comments/81aevl/what_is_the_difference_between_inertial/#:~:text=Inertial%20confinement%20focuses%20on%20compressing,creating%20a%20more%20sustained%20reaction.)[![](https://t3.gstatic.com/faviconV2?url=https://www.nationalacademies.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

](https://www.nationalacademies.org/read/18288/chapter/4)[![](https://t3.gstatic.com/faviconV2?url=https://www.epj-conferences.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

](https://www.epj-conferences.org/articles/epjconf/pdf/2024/20/epjconf_lnes2024_00013.pdf)[![](https://t2.gstatic.com/faviconV2?url=https://en.wikipedia.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

](https://en.wikipedia.org/wiki/Fusion_power)[![](https://t2.gstatic.com/faviconV2?url=https://www.reddit.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

](https://www.reddit.com/r/askscience/comments/81aevl/what_is_the_difference_between_inertial/)[![](https://t0.gstatic.com/faviconV2?url=https://www.iaea.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

](https://www.iaea.org/newscenter/news/fusion-energy-in-2025-six-global-trends-to-watch)[![](https://t2.gstatic.com/faviconV2?url=https://english.www.gov.cn/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

](https://english.www.gov.cn/news/202510/20/content_WS68f63030c6d00ca5f9a06eff.html)[![](https://t1.gstatic.com/faviconV2?url=https://www-pub.iaea.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

](https://www-pub.iaea.org/MTCD/publications/PDF/p15935-25-02871E_WFO25_web.pdf)[![](https://t0.gstatic.com/faviconV2?url=https://www.iter.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

](https://www.iter.org/node/20687/fusion-consensus-strengthening)[![](https://t2.gstatic.com/faviconV2?url=https://en.wikipedia.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

](https://en.wikipedia.org/wiki/ITER)[![](https://t0.gstatic.com/faviconV2?url=https://www.cleantechalliance.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

](https://www.cleantechalliance.org/2025/01/29/sam-altman-softbank-invest-in-425m-round-for-helion-a-seattle-area-startup-chasing-fusion-power/)[![](https://t2.gstatic.com/faviconV2?url=https://en.wikipedia.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

](https://en.wikipedia.org/wiki/Sam_Altman)[![](https://t0.gstatic.com/faviconV2?url=https://observer.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

](https://observer.com/2025/12/sam-altman-startup-investments-2025/)[![](https://t0.gstatic.com/faviconV2?url=https://techfundingnews.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

](https://techfundingnews.com/helion-secures-425m-to-advance-fusion-energy/)[![](https://t0.gstatic.com/faviconV2?url=https://observer.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

](https://observer.com/2025/01/sam-altman-nuclear-fusion-startup-fundraising/)[![](https://t1.gstatic.com/faviconV2?url=https://www.nucnet.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

](https://www.nucnet.org/news/openai-boss-sam-altman-motivated-to-invest-more-1-4-2024)[![](https://t2.gstatic.com/faviconV2?url=https://www.techpolicy.press/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

](https://www.techpolicy.press/ai-doesnt-need-more-energy-it-needs-less-concentration-of-power/)[![](https://t1.gstatic.com/faviconV2?url=https://www.popsci.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

](https://www.popsci.com/technology/sam-altman-age-of-ai-will-require-an-energy-breakthrough/)[![](https://t2.gstatic.com/faviconV2?url=https://futurism.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

](https://futurism.com/sam-altman-energy-breakthrough)[![](https://t2.gstatic.com/faviconV2?url=https://www.energycentral.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

](https://www.energycentral.com/energy-biz/post/openai-ceo-altman-says-future-ai-depends-energy-breakthrough-PumCqEWpu8jh08z)

![](https://www.gstatic.com/lamda/images/immersives/google_logo_icon_2380fba942c84387f09cf.svg)

[![](https://t2.gstatic.com/faviconV2?url=https://en.wikipedia.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

](https://en.wikipedia.org/wiki/Helion_Energy)[![](https://t3.gstatic.com/faviconV2?url=https://www.helionenergy.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

](https://www.helionenergy.com/articles/more-on-helions-pulsed-approach-to-fusion/)[![](https://t3.gstatic.com/faviconV2?url=https://www.helionenergy.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

](https://www.helionenergy.com/technology/)[![](https://t3.gstatic.com/faviconV2?url=https://www.helionenergy.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

](https://www.helionenergy.com/faq/)[![](https://t0.gstatic.com/faviconV2?url=https://www.youtube.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

](https://www.youtube.com/watch?v=HlNfP3iywvI)[![](https://t0.gstatic.com/faviconV2?url=https://www.nae.edu/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

](https://www.nae.edu/7558/MaterialsChallengesforFusionEnergy)[![](https://t0.gstatic.com/faviconV2?url=https://scientific-publications.ukaea.uk/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

](https://scientific-publications.ukaea.uk/wp-content/uploads/UKAEA-CCFE-PR2152.PDF)[![](https://t2.gstatic.com/faviconV2?url=https://www.frontiersin.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

](https://www.frontiersin.org/journals/energy-research/articles/10.3389/fenrg.2023.1157394/full)[![](https://t0.gstatic.com/faviconV2?url=https://energy.sustainability-directory.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

](https://energy.sustainability-directory.com/term/tritium-breeding-challenges/)[![](https://t2.gstatic.com/faviconV2?url=https://www.goldsea.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

](https://www.goldsea.com/article_details/commercial-fusion-power-faces-3-more-decades-of-hurdles)[![](https://t0.gstatic.com/faviconV2?url=https://en.cnnc.com.cn/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

](https://en.cnnc.com.cn/2025-03/31/c_1082798.htm)[![](https://t0.gstatic.com/faviconV2?url=https://www.researchgate.net/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

](https://www.researchgate.net/publication/397082192_Breakthrough_in_China's_Fusion_Energy_HL-3_Tokamak_Achieves_High_Ion_Temperature_and_Fusion_Triple_Product)[![](https://t2.gstatic.com/faviconV2?url=https://en.wikipedia.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

](https://en.wikipedia.org/wiki/Experimental_Advanced_Superconducting_Tokamak)[![](https://t1.gstatic.com/faviconV2?url=https://www.the-innovation.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

](https://www.the-innovation.org/article/id/691d6fe37a2be313aa3f23c2)[![](https://t1.gstatic.com/faviconV2?url=https://www.energy-reporters.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

](https://www.energy-reporters.com/news/scientists-shiver-in-awe-as-new-fusion-breakthrough-ignites-energy-revolution-that-could-change-the-world/)[![](https://t2.gstatic.com/faviconV2?url=https://www.reddit.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

](https://www.reddit.com/r/fusion/comments/1op2ppc/helions_unique_approach_to_renewable_energy/)[![](https://t2.gstatic.com/faviconV2?url=https://www.reddit.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

](https://www.reddit.com/r/fusion/comments/10g95m9/the_problems_with_helion_energy_a_response_to/)[![](https://t2.gstatic.com/faviconV2?url=https://www.reddit.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

](https://www.reddit.com/r/fusion/comments/1dlmfu2/can_someone_eli5_helions_controversy/)[![](https://t3.gstatic.com/faviconV2?url=https://forum.kerbalspaceprogram.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

](https://forum.kerbalspaceprogram.com/topic/216068-helion-energy/)[![](https://t2.gstatic.com/faviconV2?url=https://www.reddit.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

](https://www.reddit.com/r/fusion/comments/133ttne/can_we_talk_about_helion/)

![](https://www.gstatic.com/lamda/images/immersives/google_logo_icon_2380fba942c84387f09cf.svg)

[![](https://t0.gstatic.com/faviconV2?url=https://www.energycouncil.com.au/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

](https://www.energycouncil.com.au/analysis/nuclear-fusion-deals-based-on-reality-or-a-dream/)[![](https://t2.gstatic.com/faviconV2?url=https://businesscraft.se/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

](https://businesscraft.se/business/helion-cfs-tokamak-energy-tae-how-fusion-technologies-are-diverging-by-2026/)[![](https://t2.gstatic.com/faviconV2?url=https://www.reddit.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

](https://www.reddit.com/r/fusion/comments/1iqxctv/whats_different_about_helion_energy_the_nuclear/)[![](https://t2.gstatic.com/faviconV2?url=https://www.reddit.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

](https://www.reddit.com/r/fusion/comments/1ppxqx4/commonwealth_fusion_system_helion_tae_inside_the/)[![](https://t2.gstatic.com/faviconV2?url=https://www.reddit.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

](https://www.reddit.com/r/fusion/comments/17nuol3/do_you_think_that_cfs_or_helion_will_achieve/)[![](https://t0.gstatic.com/faviconV2?url=https://www.fusionindustryassociation.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

](https://www.fusionindustryassociation.org/tag/supply-chain/)[![](https://t1.gstatic.com/faviconV2?url=https://www.peaknano.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

](https://www.peaknano.com/blog/the-state-of-the-fusion-energy-industry-in-2025)[![](https://t0.gstatic.com/faviconV2?url=https://ukaea.maglr.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

](https://ukaea.maglr.com/supply-chain-aug-2025/fia-supply-chain-report)[![](https://t0.gstatic.com/faviconV2?url=https://www.fusionindustryassociation.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

](https://www.fusionindustryassociation.org/wp-content/uploads/2025/06/FIA-Supply-Chain-2025-Report.pdf)[![](https://t0.gstatic.com/faviconV2?url=https://www.fusionindustryassociation.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

](https://www.fusionindustryassociation.org/wp-content/uploads/2025/12/FIA-2025-Year-in-Review.pdf?mc_cid=7dc68615f1&mc_eid=a9957f7166)[![](https://t3.gstatic.com/faviconV2?url=https://www.scsp.ai/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

](https://www.scsp.ai/wp-content/uploads/2025/10/Fusion-Commission-Fall-2025-Report-Draft.pdf)[![](https://t1.gstatic.com/faviconV2?url=https://www-pub.iaea.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

](https://www-pub.iaea.org/MTCD/publications/PDF/p15935-25-02871E_WFO25_web.pdf)[![](https://t2.gstatic.com/faviconV2?url=https://www.reddit.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

](https://www.reddit.com/r/nuclear/comments/1q2yaut/chinese_reactor_construction_charts_january_2026/)[![](https://t2.gstatic.com/faviconV2?url=https://en.wikipedia.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

](https://en.wikipedia.org/wiki/China_Fusion_Engineering_Test_Reactor)[![](https://t3.gstatic.com/faviconV2?url=https://policycn.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

](https://policycn.com/public/commentaries/fusion-energy-soe-launched-in-shanghai-50172)[![](https://t2.gstatic.com/faviconV2?url=https://www.reddit.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

](https://www.reddit.com/r/fusion/comments/1hv3ugl/sam_altman_i_would_expect_helion_will_show_you/)[![](https://t3.gstatic.com/faviconV2?url=https://www.talk-polywell.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

](https://www.talk-polywell.org/bb/viewtopic.php?t=6499&start=855)[![](https://t2.gstatic.com/faviconV2?url=https://www.reddit.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

](https://www.reddit.com/r/fusion/comments/1onhlkz/scam_altman_the_technological_landscape_shifts_in/)[![](https://t3.gstatic.com/faviconV2?url=https://www.helionenergy.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

](https://www.helionenergy.com/articles/more-on-helions-pulsed-approach-to-fusion/)[![](https://t2.gstatic.com/faviconV2?url=https://www.techpolicy.press/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

](https://www.techpolicy.press/ai-doesnt-need-more-energy-it-needs-less-concentration-of-power/)

![](https://www.gstatic.com/lamda/images/immersives/google_logo_icon_2380fba942c84387f09cf.svg)

[![](https://t3.gstatic.com/faviconV2?url=https://www.helionenergy.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

](https://www.helionenergy.com/articles/announcing-500-million-fundraise/)[![](https://t3.gstatic.com/faviconV2?url=https://www.helionenergy.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

](https://www.helionenergy.com/articles/ending-trenta-operations/)[![](https://t2.gstatic.com/faviconV2?url=https://en.wikipedia.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

](https://en.wikipedia.org/wiki/Helion_Energy)[![](https://t0.gstatic.com/faviconV2?url=https://www.heraldnet.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

](https://www.heraldnet.com/news/helion-celebrates-smoother-path-to-fusion-energy-site-approval/)[![](https://t2.gstatic.com/faviconV2?url=https://www.reddit.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

](https://www.reddit.com/r/fusion/comments/1ptp513/helion_said_that_polaris_should_demonstrate/)[![](https://t2.gstatic.com/faviconV2?url=https://en.wikipedia.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

](https://en.wikipedia.org/wiki/Helion_Energy#:~:text=As%20of%20mid%2D2025%2C%20Helion,the%20end%20of%20the%20year.)[![](https://t3.gstatic.com/faviconV2?url=https://www.helionenergy.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

](https://www.helionenergy.com/polaris/)[![](https://t2.gstatic.com/faviconV2?url=https://www.reddit.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

](https://www.reddit.com/r/fusion/comments/1ow2fte/helion_news_letter_progress_keeps_us_on_track_to/)[![](https://t1.gstatic.com/faviconV2?url=https://www.geekwire.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

](https://www.geekwire.com/2025/helion-gives-behind-the-scenes-tour-of-secretive-60-foot-fusion-prototype-as-it-races-to-deployment/)[![](https://t1.gstatic.com/faviconV2?url=https://www.nucnet.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

](https://www.nucnet.org/news/china-aims-to-operate-world-s-first-hybrid-fusion-fission-nuclear-plant-by-2030-3-5-2025)[![](https://t0.gstatic.com/faviconV2?url=https://english.cas.cn/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

](https://english.cas.cn/newsroom/cas_media/202510/t20251015_1089475.shtml)[![](https://t3.gstatic.com/faviconV2?url=https://policycn.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

](https://policycn.com/public/commentaries/fusion-energy-soe-launched-in-shanghai-50172)[![](https://t2.gstatic.com/faviconV2?url=https://www.reddit.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

](https://www.reddit.com/r/nuclear/comments/1q2yaut/chinese_reactor_construction_charts_january_2026/)[![](https://t3.gstatic.com/faviconV2?url=https://www.moomoo.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

](https://www.moomoo.com/news/post/63408118/the-industry-s-inaugural-year-is-being-driven-by-the)[![](https://t0.gstatic.com/faviconV2?url=https://www.iaea.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

](https://www.iaea.org/about/organizational-structure/department-of-nuclear-energy/webinars/challenges-and-advances-of-technology-development-for-fusion-energy-webinar-series/global-approaches-to-tritium-breeding-for-fusion)[![](https://t0.gstatic.com/faviconV2?url=https://www.iter.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

](https://www.iter.org/machine/supporting-systems/tritium-breeding)[![](https://t0.gstatic.com/faviconV2?url=https://conferences.iaea.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

](https://conferences.iaea.org/event/406/contributions/)[![](https://t2.gstatic.com/faviconV2?url=https://www.fundacionbankinter.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

](https://www.fundacionbankinter.org/wp-content/uploads/2025/07/Future-Trends-Forum-Report-Preview-%E2%80%93-FusionForward-2025.pdf)[![](https://t2.gstatic.com/faviconV2?url=https://www.energy.gov/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

](https://www.energy.gov/articles/epri-fusion-blankets-report-2024)

![](https://www.gstatic.com/lamda/images/immersives/google_logo_icon_2380fba942c84387f09cf.svg)

[![](https://t3.gstatic.com/faviconV2?url=https://www.helionenergy.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

](https://www.helionenergy.com/articles/helion-announces-425m-series-f-investment-to-scale-commercialized-fusion-power/)[![](https://t2.gstatic.com/faviconV2?url=https://en.wikipedia.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

](https://en.wikipedia.org/wiki/Helion_Energy)[![](https://t2.gstatic.com/faviconV2?url=https://research.contrary.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

](https://research.contrary.com/company/helion)[![](https://t2.gstatic.com/faviconV2?url=https://www.reddit.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

](https://www.reddit.com/r/fusion/comments/1q0fcm7/2025_at_helion/)[![](https://t3.gstatic.com/faviconV2?url=https://talk-polywell.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

](https://talk-polywell.org/bb/viewtopic.php?t=6499&start=930)[![](https://t2.gstatic.com/faviconV2?url=https://time.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

](https://time.com/7328213/nuclear-fusion-energy-ai/)[![](https://t2.gstatic.com/faviconV2?url=https://www.reddit.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

](https://www.reddit.com/r/fusion/comments/1onhlkz/scam_altman_the_technological_landscape_shifts_in/)[![](https://t0.gstatic.com/faviconV2?url=https://www.ted.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

](https://www.ted.com/pages/sam-altman-on-the-future-of-ai-and-humanity-transcript)[![](https://t2.gstatic.com/faviconV2?url=https://www.techpolicy.press/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

](https://www.techpolicy.press/transcript-sam-altman-testifies-at-us-senate-hearing-on-ai-competitiveness/)[![](https://t1.gstatic.com/faviconV2?url=https://www.peaknano.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

](https://www.peaknano.com/blog/the-state-of-the-fusion-energy-industry-in-2025)[![](https://t3.gstatic.com/faviconV2?url=https://www.helionenergy.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

](https://www.helionenergy.com/polaris/)[![](https://t2.gstatic.com/faviconV2?url=https://www.reddit.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

](https://www.reddit.com/r/fusion/comments/1pkue34/the_first_look_at_polaris_helions_latest_nuclear/)