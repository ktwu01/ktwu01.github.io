---
title: "大规模协作科学的崛起 2026年人工智能与跨学科「巨型作者」项目深度调研报告"
date: 2026-02-04
permalink: /zh/posts/2026/02/massive-collaborative-science-mega-authors/
tags:
  - ai
  - research
  - collaboration
---

如果你最近经常逛 arxiv，你一定会被那些作者名单长到需要翻页的 AI 论文给震撼到。

> 作者：[Koutian Wu](https://www.linkedin.com/in/ktwu01/)；[GitHub: ktwu01](https://github.com/ktwu01/)

坦率的讲，过去我们总觉得科研是一个老教授带着几个博士生在实验室里苦熬的闭门造车。这两天我复盘了一下最近爆发的各种顶会论文，发现科研的玩法早就变天了。

其实吧，这种被称为「巨型作者」的项目，正在成为2026年跨学科研究的绝对主流。

事情是这样的。

以前咱们看高能物理的论文，比如 CERN 欧洲核子研究中心发一篇关于上帝粒子的文章，后面跟着几千个作者。大家都觉得那是大科学工程的特例。毕竟人家要建几十公里长的粒子加速器。

你想想看，现在的 AI 领域，正在完美复刻这种大科学的模式。

不管是 OpenAI 还是那些顶级的开源组织，他们手里握着算力，手里有 Transformer 架构。他们最缺的，是那些能难倒最强 AI 的硬核数据。

互联网上能爬到的公开文本早就被他们吃干抹净了。现在的瓶颈，卡在那些只有真正的领域专家才知道的缄默知识上。

为了拿到这些数据，AI 社区硬生生发明出了一种「大规模众包评测」的新范式。

# 大规模协作科学的崛起：2026年人工智能与跨学科“巨型作者”项目深度调研报告

## 1. 绪论：从“孤独天才”到“千人作者”的范式转移

在21世纪的科学史册中，2020年代中期将被记录为一个分水岭。科学发现的模式正经历着自“大科学”（Big Science）时代以来最深刻的结构性变革。过去，顶尖学术期刊如《自然》（Nature）或《科学》（Science）的版面长期被小型精英实验室所垄断，但在人工智能（AI）大模型爆发的催化下，一种全新的科研形态——**大规模协作科学（Massively Collaborative Science, MCS）**——正在重塑学术界的权力版图。

本报告旨在响应一个在技术社区日益流行的文化现象，即所谓的“我在Nature发了论文，但我只是做了一点微小的贡献”。这种现象并非偶然，而是AI评估危机下的必然产物。随着大型语言模型（LLM）的能力逐渐逼近甚至超越人类平均水平，传统的自动化测试基准（Benchmarks）已全面失效。为了评估比人类更“聪明”的机器，科学界不得不回归到人类智慧的本身——不仅是编程能力，更是深厚的领域知识（Domain Expertise）、语言多样性（Linguistic Diversity）和复杂的伦理推理能力。

截至2026年初，这一趋势已催生了数个具有里程碑意义的“巨型作者”（Hyper-authorship）项目。最典型的案例便是**Humanity's Last Exam (HLE)**，该项目通过集结全球数千名专家构建了一个机器难以攻克的“人类最后试卷”，并最终登上了顶级学术殿堂。对于非计算机专业背景的领域专家、语言学者、甚至拥有特殊知识储备的普通公众而言，这不仅是一个参与科学前沿的窗口，更是一条通往顶级学术发表的“低代码”甚至“无代码”捷径。

本报告将对2026年活跃的同类项目进行详尽的梳理与分析，涵盖AI基准测试、多语言NLP、AI安全红队测试（Red Teaming）、以及生物医学与天文学领域的公民科学项目。我们将深入剖析这些项目的运作机制、贡献门槛、以及如何通过“微小贡献”获得正式的学术署名权。

---

## 2. 评估的危机：为何AI需要人类的“微小贡献”

要理解为何顶尖AI实验室急需非技术人员的参与，首先必须理解当前AI领域面临的“评估崩溃”危机。

### 2.1 MMLU的饱和与“由于训练数据污染导致的虚假高分”

在2023年之前，MMLU（Massive Multitask Language Understanding）被视为衡量大模型智能水平的黄金标准。然而，到了2025年，随着GPT-5级别模型的问世，主流模型在MMLU上的得分普遍超过90%。这并不意味着模型真的达到了人类专家的全知全能，更多是因为模型在训练阶段“背诵”了互联网上的题库。这种现象被称为“数据污染”（Data Contamination）。

### 2.2 “谷歌防御”（Google-Proof）标准的诞生

为了打破这一僵局，以**Center for AI Safety (CAIS)** 和 **Scale AI** 为首的研究机构提出了新的标准：如果一个问题的答案可以通过简单的谷歌搜索（Information Retrieval）在前三条结果中找到，那么它就不是一个合格的测试题。

真正的智能测试必须是“谷歌防御”的。例如，与其问“拿破仑哪一年滑铁卢战败？”，不如问“考虑到1815年6月比利时的降雨量记录与当时法军炮兵移动速度的数学关系，泥泞的地面导致法军火炮部署延迟了多少小时，进而如何改变了内伊元帅的骑兵冲锋窗口？”

这类问题无法通过爬虫抓取现成答案，它需要历史学家的综合推理。**机器无法生成这类数据，因为机器正是被测试的对象。** 因此，唯一的数据来源便是人类——尤其是那些拥有非互联网公开知识（如绝版书籍、口述历史、临床经验、方言俚语）的人类。这便是“微小贡献”通往《Nature》的理论基础。

---

## 3. 核心案例：Humanity's Last Exam (HLE) 与 HLE-Rolling

作为用户查询的核心参照物，_Humanity's Last Exam_ (HLE) 代表了这一领域的最高标准。虽然其第一阶段已于2025年4月结束并发表了重磅论文，但该项目并未终结，而是演化为更具生命力的**HLE-Rolling**版本。

### 3.1 HLE的历史定位与方法论

HLE不仅仅是一套试卷，它是一场全球范围内的智力众包实验。其核心目标是构建一个封闭式的、多模态的、且极其困难的学术基准。

- **规模**：2,500道专家级问题。
    
- **贡献者**：来自全球500多所顶尖大学和研究机构的1,000多名教授与研究人员。
    
- **难度**：即使是拥有互联网访问权限的熟练人类，也需要相当长的时间才能解出，而不仅仅是搜索。
    
- **成果**：论文发表于《Nature》或同级别顶级刊物，所有贡献被采纳的问题设计者均列入作者名单。
    

### 3.2 2026年的新机遇：HLE-Rolling（滚动更新机制）

随着AI模型的快速迭代，静态的HLE数据集面临着被模型“过拟合”的风险。因此，组织方在2025年10月推出了**HLE-Rolling**机制，这是一个动态的、持续更新的分支版本。

#### 3.2.1 参与机制与门槛

- **非技术门槛**：参与者不需要懂编程，不需要会训练模型。你需要的是**领域知识**。如果你是古生物学博士生、资深税务律师、或者是研究苏美尔楔形文字的学者，你就是HLE最渴求的贡献者。
    
- **提交渠道**：
    
    - **电子邮件**：直接发送提案至 `agibenchmark@safe.ai`。
        
    - **官方仪表盘**：通过 `lastexam.ai` 或 `agi.safe.ai` 的Dashboard进行提交。
        
- **题目设计要求**：
    
    - **封闭性**：必须是多选题或短答题（便于自动化评分）。
        
    - **唯一性**：答案必须是客观且无争议的（Unambiguous）。
        
    - **隐蔽性**：答案不能直接存在于公开网页的文本中，必须经过推理得出。
        
    - **多模态**：鼓励包含图表、化学分子式、显微镜切片等图像信息。
        

#### 3.2.2 署名权与学术回报

根据HLE项目的既定惯例和HLE-Rolling的说明，组织方承诺“致力于为后续贡献者提供共同署名权（Co-authorship）”。这意味着，如果在滚动更新期间你的问题被采纳并进入了下一个版本的核心数据集，你极有可能出现在后续发表的System Report或期刊论文的作者列表中。对于学术圈外的人士，这是一份极具分量的背书；对于在读博士生，这可能意味着一篇顶级会议的共同作者身份。

|特征|HLE (第一版)|HLE-Rolling (当前)|
|---|---|---|
|**状态**|已完结 (2025.04)|**活跃中**|
|**主要目标**|建立基准|防止基准饱和/过拟合|
|**贡献方式**|集中征集|**持续征集 (邮件/Dashboard)**|
|**回报**|Nature/ArXiv 署名|**未来版本署名/致谢**|

---

## 4. 语言的守护者：多语言NLP与去殖民化科学

如果说HLE是智力的巅峰挑战，那么多语言NLP（Multilingual NLP）项目则是广度的最大化。这是目前对非技术背景（Non-STEM）贡献者最友好的领域。AI界正面临严重的“英语中心主义”问题，为了让模型在斯瓦希里语、盖丘亚语或粤语中也能表现出色，各大实验室急需母语者的帮助。

### 4.1 Masakhane：非洲NLP的草根奇迹

**Masakhane**（意为“我们一起建设”）是全球最成功的分布式AI研究组织之一。它打破了“西方实验室研究，非洲提供数据”的旧模式，建立了一种参与式研究的新范式。

- **项目性质**：去中心化的草根研究社区。
    
- **适合人群**：非洲语言母语者、语言学学生、翻译人员、社会活动家。
    
- **核心理念**：参与即贡献。在Masakhane，翻译数据、整理词汇表、甚至是在社区会议中提供文化背景解释，都被视为“智力贡献”。
    
- **署名文化**：Masakhane的论文（常发表于ACL, ICLR, EMNLP等顶会）以其超长的作者名单闻名。他们明确反对“直升机科研”（Helicopter Science），坚持让每一个数据贡献者都在论文上留名。
    
- **2026年活跃项目**：
    
    - **Decolonise Science**：将科学术语（如“量子”、“疫苗”）翻译成非洲本土语言。这需要深厚的语言功底，而非代码能力。
        
    - **MasakhaNER**：命名实体识别数据集构建。你需要做的只是阅读文本，标记出人名、地名、机构名。
        

### 4.2 AmericasNLP：美洲原住民语言的复兴

与Masakhane类似，**AmericasNLP**专注于美洲原住民语言（如Quechua, Guarani, Bribri, Nahuatl）。

- **Shared Tasks（共享任务）**：这是NLP领域的“奥林匹克”。每年AmericasNLP都会举办比赛。
    
- **2026年机会**：
    
    - **任务1（机器翻译）**：虽然构建模型需要技术，但构建评估集（Evaluation Set）需要母语者。你可以贡献一手翻译的文本，或者作为裁判（Human Judge）评估模型的输出质量。
        
    - **任务3（翻译度量标准）**：2026年新增的任务，重点在于开发适合原住民语言的评估标准。这需要对语言结构的深刻理解，而非单纯的算法知识。
        
- **回报**：参与者通常会被邀请撰写“System Description Paper”或作为“Findings Paper”的共同作者。
    

### 4.3 Mozilla Common Voice & TidyVoice 2026

Mozilla的Common Voice是全球最大的开源语音数据集。虽然普通贡献者（仅仅录音的人）通常只在致谢中提及，但**社区领袖**和**语言验证者**有机会进入核心圈层。

- **TidyVoice 2026 Challenge**：这是Interspeech 2026会议上的一个挑战赛，旨在解决跨语言说话人验证问题。
    
- **贡献点**：该挑战赛基于Common Voice数据，需要大量的跨语言元数据清理和验证。对于精通多种语言的用户，帮助整理和验证这些元数据是获得论文署名的潜在路径。
    

---

## 5. 安全红队与偏见赏金：在破坏中建设

如果你擅长“找茬”，或者对社会公平、伦理道德有敏锐的直觉，那么AI安全（AI Safety）领域是你的主场。这里不需要你构建模型，只需要你攻破模型。

### 5.1 Humane Intelligence与“偏见赏金”（Bias Bounties）

由Rumman Chowdhury博士创立的Humane Intelligence是非营利性AI评估机构的先驱。他们发明了“偏见赏金”这一概念——模仿黑客界的“Bug Bounty”，但针对的是算法偏见而非代码漏洞。

- **2026年大动作：Zindi试点**
    
    - Humane Intelligence将在2026年第三季度（Q3）将其平台迁移至**Zindi**（非洲最大的数据科学竞赛平台），开启大规模试点。
        
- **适合人群**：社会学学生、少数族裔权益倡导者、特定领域专家（如农业、医疗）。
    
- **具体任务**：
    
    - **气候适应与原住民知识**：测试AI给出的农业建议是否忽略了当地传统的生态知识？
        
    - **城乡地图精度**：测试AI在识别农村地区卫星图像时是否表现出系统性偏差？
        
- **无代码参与**：你不需要写脚本去攻击模型。通常平台会提供一个聊天界面或可视化工具，你只需要输入Prompt，记录AI的错误回答，并提交报告。
    
- **回报**：除了现金奖励（Bounty），获胜者和高价值报告的提交者通常会被邀请共同撰写“回顾报告”（Retrospective Paper），这些报告在AI伦理会议（如FAccT, AIES）上具有极高的引用率。
    

### 5.2 MLCommons: AI Risk & Reliability (AIRR)

MLCommons是AI界的“ISO标准组织”。其AIRR工作组致力于制定AI安全的行业标准。

- **SafeBench竞赛**：悬赏25万美元征集新的安全基准测试思路。
    
- **贡献机会**：他们需要的不仅仅是数据，而是**测试设计思路**。
    
    - _例子_：如果你是心理学家，你可以设计一套测试AI是否会通过“煤气灯效应”（Gaslighting）操纵用户的方案。
        
    - _例子_：如果你是法律专家，你可以设计一套测试AI是否会提供违反GDPR建议的方案。
        
- **署名权**：AIRR工作组发表的白皮书和基准测试论文（如AILuminate）通常包含所有活跃的工作组成员。加入工作组并定期参加会议、贡献观点，是在该领域确立专家地位的有效途径。
    

### 6. 跨界科学：从天文学到细胞生物学的“公民科学家”

虽然用户的查询主要关注AI，但提到“Nature论文”和“多人大项目”，不得不提公民科学（Citizen Science）的鼻祖们。这些领域在处理署名权问题上最为成熟，且与AI技术的结合日益紧密。

### 6.1 Zooniverse：众包科学的航母

Zooniverse是全球最大的公民科学平台。这里的项目通常涉及处理海量的图像或音频数据，这些数据量太大，科学家无法独自处理，而AI目前又不够精准。

- **2026年活跃项目**：
    
    - **Planetary Response Network (莫桑比克洪灾2026)**：在卫星地图上标记受灾建筑。这是典型的人道主义救援与AI训练数据的结合。
        
    - **Snapshot Wisconsin**：分类红外相机拍摄的野生动物。
        
- **如何获得署名？**
    
    - 仅仅做分类任务（点击图片）通常只能获得“集体致谢”。
        
    - **通往署名的秘诀**：活跃于"Talk"（讨论区）。科学发现往往源于异常值。如果你发现了一张奇怪的图片（比如著名的“Tabby's Star”或“Hanny's Voorwerp”），并在论坛中引发了科学家的注意，你很可能会作为发现者之一被列入论文作者名单。
        
    - **AI纠错**：许多新项目是“人机协作”模式。AI先做预处理，人类负责纠正AI的错误。这种“纠错数据”对于提升模型性能至关重要，深度参与者（Super-users）常被视为研究合作伙伴。
        

### 6.2 Human Cell Atlas (HCA)：人类细胞图谱

这是一个宏大的生物学工程，旨在绘制人体每一个细胞的图谱。

- **贡献方式**：HCA经常组织“注释马拉松”（Annotathons），邀请医学生、生物学家协助标注细胞类型。
    
- **回报**：HCA是一个联盟（Consortium）。核心贡献者会被吸纳进联盟，其发表在《Nature》、《Science》上的论文通常会列出庞大的“HCA Consortium”作者列表，其中包括了数据贡献者。
    

---

## 7. 深度解析：不同类型项目的“投入产出比”分析

为了帮助读者选择最适合自己的路径，我们对上述项目进行多维度的对比分析。

|项目名称|领域|核心需求 (你的贡献)|技术门槛|署名概率|顶级刊物潜力|适合人群|
|---|---|---|---|---|---|---|
|**HLE-Rolling**|AI基准|高难度、反直觉的专业问题|低 (需领域知识)|高 (积累制)|极高 (Nature级)|博士生、行业专家、历史/科学发烧友|
|**Masakhane**|NLP|非洲语言翻译、语料收集|低 (需语言能力)|极高 (社区文化)|高 (ACL/ICLR)|语言学者、多语种使用者|
|**SemEval 2026**|NLP评估|幽默感判断、文本相关性标注|低 (需阅读理解)|中 (Shared Task Paper)|中高 (ACL Workshop)|文科生、创意写作者|
|**Humane Intel.**|AI安全|找茬、发现偏见、攻击模型|低 (需批判思维)|中 (回顾报告)|中 (FAccT/AIES)|社会学背景、权益倡导者|
|**Zooniverse**|自然科学|找异常、纠正AI分类|极低 (需耐心)|低 (需成为Super-user)|高 (天文学/生物学顶刊)|爱好者、学生|
|**FrontierMath**|数学|提出未解/极难数学问题|极高 (需数学造诣)|高|极高 (数学/AI顶刊)|数学系研究生|

---

## 8. 实操指南：如何最大化你的贡献可见度

“做了微小贡献”并不自动等于“出现在作者列表”。在大型协作项目中，你需要策略性地管理你的参与。以下是基于2026年社区规范的生存指南：

### 8.1 寻找“元任务”（Meta-Tasks）

不要只做最基础的数据生产。大多数人只负责“答题”，如果你能负责“出题”或者“改卷”，你的地位会直线上升。

- **文档编写**：主动提出为数据集撰写**Data Sheet**或**Model Card**。这是AI伦理领域非常看重但工程师往往不愿做的繁琐工作。
    
- **质量控制**：在Masakhane或Common Voice中，主动担任“验证者”（Validator），审核其他人的提交。
    
- **社区协调**：帮助组织周会、整理会议纪要、管理Discord频道。这种“隐形劳动”在去中心化组织中极受尊重。
    

### 8.2 抓住“Opt-in”的关键时刻

大型项目（如BigScience）在论文发表前，通常会分发一份**Authorship Opt-in Form**（署名确认表）。

- **警惕**：这份表格通常只在Slack/Discord的核心频道发布，或者通过邮件列表发送。如果你只是默默提交数据而不看群消息，你不仅会错过署名，甚至可能连致谢都漏掉。
    
- **策略**：保持在官方沟通渠道的活跃度，确保组织者知道你的ID背后是一个真实的人。
    

### 8.3 瞄准“Shared Tasks”的论文机会

像AmericasNLP或SemEval这样的比赛，只要你提交了有效结果（哪怕是基线水平），通常都有资格提交一篇**System Description Paper**。这篇论文会收录在ACL等顶会的Workshop Proceedings中，是被Google Scholar索引的正式学术发表。这是最稳妥的“发Paper”路径。

### 8.4 利用“长尾知识”的优势

不要去卷“通用知识”。HLE不需要更多关于“光合作用”的问题，ChatGPT已经背得滚瓜烂熟了。

- **差异化竞争**：去贡献那些**书本上没有、互联网搜不到**的知识。
    
    - _例子_：你家乡的方言俚语中关于天气的特定表达。
        
    - _例子_：你所在工厂的特种设备维修手册中的故障排查流程。
        
    - _例子_：你收藏的民国时期报纸上的广告文案。
        
    - 这些“私有数据”或“隐性知识”是AI目前最匮乏的养料。
        

---

## 9. 结论：在这个时代，每个人都是AI的老师

用户的查询虽然带有戏谑成分，但它敏锐地捕捉到了科学范式的转变。AI正在经历一个从“数据挖掘”到“数据耕种”的过程。在这个过程中，机器需要的不再是更多的GPU，而是更高质量的**人类反馈（RLHF）**和**人类评估（Human Evaluation）**。

像Humanity's Last Exam (HLE)这样的项目，实际上是在为全人类的知识建立一座数字化的防波堤。它证明了人类智能的深度、复杂性和不可预测性仍然是机器难以企及的。通过参与这些项目，无论是提交一道精心设计的历史难题，还是录制一句濒危语言的问候，你不仅是在为一篇《Nature》论文做贡献，更是在为AI定义什么是“真实”，什么是“正确”，以及什么是“人类”。

在2026年，科学的大门前所未有地敞开。你不需要是博士，不需要是程序员，你只需要带着你的好奇心、你的专业知识、甚至你的偏见（作为测试样本），加入到Discord、Slack或Zooniverse中去。那篇未来的《Nature》论文作者列表中，也许真的会留下你的名字。

---

## 附录：核心资源导航

- **HLE-Rolling 提交入口**: `lastexam.ai` / 邮箱: `agibenchmark@safe.ai`
    
- **Masakhane 社区**: `masakhane.io` (强烈建议加入其Discord)
    
- **Zindi 竞赛平台**: `zindi.africa` (关注2026 Q3的Bias Bounty)
    
- **AmericasNLP**: `turing.iimas.unam.mx/americasnlp/`
    
- **SemEval 2026**: `semeval.github.io/SemEval2026/`
    
- **Zooniverse**: `zooniverse.org`
    
- **Scale AI Human Frontier Collective**: `scale.com/careers` (搜索 HFC Fellow)

顺着上面的再聊聊。这不仅是文科或者计算机学者的狂欢，对于搞气候和地球科学（Geoscience）的朋友来说，这绝对是一片蓝海。

我之前一直觉得，地球科学的时空尺度太大了。你要验证亚马逊雨林或者西伯利亚冻土的碳通量模型，必须依赖全世界各地的实地采样。但现在，这种物理分布的属性反而成了巨大的优势。

比如圈子里现在很火的 Project Polyclimate 项目。他们受数学界众包解题的启发，正在把气候科学直接 GitHub 化。你想知道全球剩余碳预算是多少？不用等政府的滞后报告。大家直接在 GitHub 上提交 Pull Request，修复数据源或者优化计算代码。只要你的代码被合并了，你就是项目白皮书的核心作者。

这种「代码即论文」的模式，简直太赤鸡了。

不仅如此，很多传统的数据收集项目也在觉醒。像全美跑相机陷阱的 Snapshot USA，或者搞水质采样的 EXCHANGE Consortium，以前你给他们提供数据，顶多在致谢里提你一句。现在不同了，只要你提供了高质量的独家数据，你就能作为 Consortium Authorship（联盟作者）堂堂正正地挂在 Ecology 这种顶刊上。

更不要说像 Climate Change AI（CCAI）这样的枢纽组织。他们不仅在 NeurIPS、ICLR 这种顶级会场办 workshop，还直接发几十万美元的种子基金。你在他们的 Discord 频道里逛一圈，到处都是“我有高分辨率卫星甲烷数据，急寻计算机视觉合作者”这种帖子。

连 KDD 这种数据挖掘的顶级顶会，在2026年都专门开辟了 AI for Sciences 赛道。这就差直接把“我们需要跨学科专家”写在脸上了。

不管你是搞气象模拟的，还是研究土壤循环的。只要你能拿着自己独家的数据和隐性知识，去给这些大模型喂招，人家绝对夹道欢迎。这是一种双赢。他们拿到了高质量的评测数据，你拿到了顶会论文的共一或者核心作者席位。

我一时间无语凝噎。科技的进步，总是以我们意想不到的方式把所有人卷入其中。

当我们都在焦虑自己会不会被 AI 取代的时候，AI 却在绝望地呼唤着人类最后的专家知识。机器可以一秒钟生成一万篇看似通顺的综述。但它造不出一道只有地质学家才知道哪里有坑的题目。

不管大模型怎么进化，科学研究的真相，依然是人类好奇心的大规模协作。

如果你也是一个在自己领域里死磕了好多年的地球科学研究者，今天不妨去那些 AI 社区里逛逛。把你脑子里的那些隐性知识拿出来，去给这个时代的 AI 巨兽喂招。磨平一些信息差，说不定你也能在那份长长的巨型作者名单里，留下自己的名字。


[

![](https://t2.gstatic.com/faviconV2?url=https://en.wikipedia.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://en.wikipedia.org/wiki/Humanity%27s_Last_Exam)[

![](https://t0.gstatic.com/faviconV2?url=https://artificialanalysis.ai/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://artificialanalysis.ai/evaluations/humanitys-last-exam)[

![](https://t1.gstatic.com/faviconV2?url=https://github.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://github.com/centerforaisafety/hle)[

![](https://t3.gstatic.com/faviconV2?url=https://scale.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://scale.com/research/humanitys-last-exam)[

![](https://t0.gstatic.com/faviconV2?url=https://e.vnexpress.net/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://e.vnexpress.net/news/news/education/vietnamese-engineer-co-leads-nature-paper-introducing-humanity-s-last-exam-for-ai-5013275.html)[

![](https://t0.gstatic.com/faviconV2?url=https://intuitionlabs.ai/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://intuitionlabs.ai/articles/humanitys-last-exam-ai-benchmark)[

![](https://t2.gstatic.com/faviconV2?url=https://blog.promptlayer.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://blog.promptlayer.com/humans-last-exam-llm-a-comprehensive-evaluation-2/)[

![](https://t0.gstatic.com/faviconV2?url=https://safe.ai/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://safe.ai/work/research)[

![](https://t1.gstatic.com/faviconV2?url=https://arxiv.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://arxiv.org/html/2601.23112v1)[

![](https://t0.gstatic.com/faviconV2?url=https://safe.ai/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://safe.ai/)[

![](https://t0.gstatic.com/faviconV2?url=https://www.cs.cmu.edu/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://www.cs.cmu.edu/~sgururaj/assets/pdf/sireesh_thesis_proposal.pdf)[

![](https://t1.gstatic.com/faviconV2?url=https://arxiv.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://arxiv.org/pdf/2601.10599)[

![](https://t1.gstatic.com/faviconV2?url=https://lists.seas.upenn.edu/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://lists.seas.upenn.edu/pipermail/types-announce/2025/012247.html)[

![](https://t0.gstatic.com/faviconV2?url=https://futurehealth.bmj.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://futurehealth.bmj.com/news)[

![](https://t2.gstatic.com/faviconV2?url=https://wildlabs.net/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://wildlabs.net/groups/ai-conservation)[

![](https://t0.gstatic.com/faviconV2?url=https://www.techuk.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://www.techuk.org/resource/nato-launches-new-commercial-space-platform-spacenet.html)[

![](https://t0.gstatic.com/faviconV2?url=https://www.eleuther.ai/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://www.eleuther.ai/community)[

![](https://t0.gstatic.com/faviconV2?url=https://www.eleuther.ai/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://www.eleuther.ai/)[

![](https://t1.gstatic.com/faviconV2?url=https://blog.mozilla.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://blog.mozilla.org/en/mozilla/dataset-convening/)[

![](https://t0.gstatic.com/faviconV2?url=https://www.eleuther.ai/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://www.eleuther.ai/papers-blog)[

![](https://t1.gstatic.com/faviconV2?url=https://bigscience.huggingface.co/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://bigscience.huggingface.co/)[

![](https://t0.gstatic.com/faviconV2?url=https://ml4physicalsciences.github.io/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://ml4physicalsciences.github.io/)[

![](https://t0.gstatic.com/faviconV2?url=https://bigscience.nl/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://bigscience.nl/events)[

![](https://t2.gstatic.com/faviconV2?url=https://huggingface.co/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://huggingface.co/bigscience)[

![](https://t1.gstatic.com/faviconV2?url=https://github.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://github.com/bigscience-workshop)[

![](https://t3.gstatic.com/faviconV2?url=https://mlcommons.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://mlcommons.org/benchmarks/)[

![](https://t3.gstatic.com/faviconV2?url=https://mlcommons.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://mlcommons.org/get-involved/)[

![](https://t3.gstatic.com/faviconV2?url=https://mlcommons.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://mlcommons.org/working-groups/benchmarks/inference/)[

![](https://t3.gstatic.com/faviconV2?url=https://mlcommons.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://mlcommons.org/working-groups/)[

![](https://t3.gstatic.com/faviconV2?url=https://mlcommons.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://mlcommons.org/working-groups/benchmarks/storage/)[

![](https://t2.gstatic.com/faviconV2?url=https://cs.nyu.edu/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://cs.nyu.edu/~davise/Benchmarks/BigBenchDiscussion.html)[

![](https://t2.gstatic.com/faviconV2?url=https://openreview.net/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://openreview.net/forum?id=YrycTjllL0)[

![](https://t1.gstatic.com/faviconV2?url=https://arxiv.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://arxiv.org/html/2502.19187v1)[

![](https://t1.gstatic.com/faviconV2?url=https://github.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://github.com/google/BIG-bench)[

![](https://t2.gstatic.com/faviconV2?url=https://huggingface.co/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://huggingface.co/datasets/google/bigbench)[

![](https://t1.gstatic.com/faviconV2?url=https://github.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://github.com/mlcommons/dynabench/blob/main/docs/owners.md)[

![](https://t2.gstatic.com/faviconV2?url=https://aclanthology.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://aclanthology.org/2021.naacl-main.324.pdf)[

![](https://t0.gstatic.com/faviconV2?url=https://dynabench.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://dynabench.org/about)[

![](https://t0.gstatic.com/faviconV2?url=https://dynabench.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://dynabench.org/)[

![](https://t1.gstatic.com/faviconV2?url=https://arxiv.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://arxiv.org/abs/2104.14337)[

![](https://t2.gstatic.com/faviconV2?url=https://www.microsoft.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://www.microsoft.com/en-us/msrc/bounty-ai)[

![](https://t3.gstatic.com/faviconV2?url=https://www.bugcrowd.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://www.bugcrowd.com/solutions/ai/)[

![](https://t2.gstatic.com/faviconV2?url=https://openai.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://openai.com/bio-bug-bounty/)[

![](https://t0.gstatic.com/faviconV2?url=https://www.offsec.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://www.offsec.com/blog/red-teaming-llm/)[

![](https://t2.gstatic.com/faviconV2?url=https://neurips.cc/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://neurips.cc/Conferences/2025/CallForDatasetsBenchmarks)[

![](https://t2.gstatic.com/faviconV2?url=https://neurips.cc/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://neurips.cc/virtual/2025/loc/san-diego/events/datasets-benchmarks-2025)[

![](https://t0.gstatic.com/faviconV2?url=https://blog.neurips.cc/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://blog.neurips.cc/2025/12/05/neurips-datasets-benchmarks-track-from-art-to-science-in-ai-evaluations/)[

![](https://t2.gstatic.com/faviconV2?url=https://neurips.cc/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://neurips.cc/)[

![](https://t2.gstatic.com/faviconV2?url=https://openreview.net/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://openreview.net/group?id=NeurIPS.cc/2025/Datasets_and_Benchmarks_Track)[

![](https://t0.gstatic.com/faviconV2?url=https://mmintelligence.github.io/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://mmintelligence.github.io/)[

![](https://t0.gstatic.com/faviconV2?url=https://iclr.cc/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://iclr.cc/Conferences/2026/CallForWorkshops)[

![](https://t3.gstatic.com/faviconV2?url=https://sites.google.com/view/iclr2026finai/home/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://sites.google.com/view/iclr2026finai/home)[

![](https://t0.gstatic.com/faviconV2?url=https://iclr.cc/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://iclr.cc/Conferences/2026/CallForPapers)[

![](https://t0.gstatic.com/faviconV2?url=https://iclr.cc/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://iclr.cc/)[

![](https://t1.gstatic.com/faviconV2?url=https://au.news.yahoo.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://au.news.yahoo.com/ai-failing-humanity-last-exam-235408129.html)[

![](https://t0.gstatic.com/faviconV2?url=https://singularityhub.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://singularityhub.com/2026/02/03/humanitys-last-exam-stumps-top-ai-models-and-thats-a-good-thing/)[

![](https://t2.gstatic.com/faviconV2?url=https://www.reddit.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://www.reddit.com/r/accelerate/comments/1igc3q2/within_a_month_%C2%BC_of_humanitys_last_exam_conquered/)[

![](https://t3.gstatic.com/faviconV2?url=https://scale.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://scale.com/dwarkesh)[

![](https://t3.gstatic.com/faviconV2?url=https://scale.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://scale.com/research)[

![](https://t3.gstatic.com/faviconV2?url=https://scale.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://scale.com/leaderboard/tool_use_chat)[

![](https://t0.gstatic.com/faviconV2?url=https://www.maginative.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://www.maginative.com/article/scale-launches-leaderboard-to-provide-better-evaluations-for-frontier-ai-models/)[

![](https://t0.gstatic.com/faviconV2?url=https://mashable.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://mashable.com/article/scale-ai-seal-showdown-benchmarking-leaderboard-lmarena)[

![](https://t1.gstatic.com/faviconV2?url=https://epoch.ai/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://epoch.ai/consultations)[

![](https://t1.gstatic.com/faviconV2?url=https://epoch.ai/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://epoch.ai/)[

![](https://t1.gstatic.com/faviconV2?url=https://epoch.ai/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://epoch.ai/our-funding)[

![](https://t2.gstatic.com/faviconV2?url=https://www.matsprogram.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://www.matsprogram.org/stream/epoch)[

![](https://t1.gstatic.com/faviconV2?url=https://epoch.ai/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://epoch.ai/blog/announcing-epoch)[

![](https://t2.gstatic.com/faviconV2?url=https://metr.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://metr.org/)[

![](https://t2.gstatic.com/faviconV2?url=https://metr.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/)[

![](https://t1.gstatic.com/faviconV2?url=https://github.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://github.com/METR/public-tasks)[

![](https://t2.gstatic.com/faviconV2?url=https://metr.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://metr.org/blog/2025-08-12-research-update-towards-reconciling-slowdown-with-time-horizons/)[

![](https://t2.gstatic.com/faviconV2?url=https://metr.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://metr.org/blog/2024-11-22-evaluating-r-d-capabilities-of-llms/)[

![](https://t3.gstatic.com/faviconV2?url=https://unesdoc.unesco.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://unesdoc.unesco.org/ark:/48223/pf0000245122)[

![](https://t0.gstatic.com/faviconV2?url=https://www.researchgate.net/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://www.researchgate.net/publication/305602116_A_Taxonomy_of_Massive_Open_Online_Courses)[

![](https://t3.gstatic.com/faviconV2?url=https://www.spie.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://www.spie.org/Publications/Proceedings/Volume/11006)[

![](https://t0.gstatic.com/faviconV2?url=https://www.cedtech.net/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://www.cedtech.net/article/a-taxonomy-of-massive-open-online-courses-6174)[

![](https://t1.gstatic.com/faviconV2?url=https://papers.iafor.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://papers.iafor.org/wp-content/uploads/papers/aceid2020/ACEID2020_55192.pdf)[

![](https://t1.gstatic.com/faviconV2?url=https://www.umu.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://www.umu.com/ask/q11122301573854279528)[

![](https://t2.gstatic.com/faviconV2?url=https://www.reddit.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://www.reddit.com/r/skibidiscience/comments/1jijsrc/humanai_synergy_in_polymathic_intelligence_a_new/)[

![](https://t1.gstatic.com/faviconV2?url=https://www.forasoft.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://www.forasoft.com/blog/article/polymath-ai-lesson-plan-generation)[

![](https://t1.gstatic.com/faviconV2?url=https://stevenmilanese.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://stevenmilanese.com/blog/the-modern-polymath-how-to-cultivate-a-multidisciplinary-mindset-in-the-digital-age)[

![](https://t1.gstatic.com/faviconV2?url=https://www.datapro.news/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://www.datapro.news/p/digital-polymaths-are-coming-to-augment-you)[

![](https://t0.gstatic.com/faviconV2?url=https://www.armyupress.army.mil/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://www.armyupress.army.mil/Journals/Military-Review/English-Edition-Archives/Professional-Military-Writing/Writing-Is-a-Team-Sport/)[

![](https://t3.gstatic.com/faviconV2?url=https://www.isca-archive.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://www.isca-archive.org/interspeech_2025/zhang25s_interspeech.pdf)[

![](https://t2.gstatic.com/faviconV2?url=https://aclanthology.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://aclanthology.org/2024.lrec-main.187/)[

![](https://t1.gstatic.com/faviconV2?url=https://arxiv.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://arxiv.org/html/2506.00733v1)[

![](https://t0.gstatic.com/faviconV2?url=https://discourse.mozilla.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://discourse.mozilla.org/t/licensing-and-contribution-to-common-voice/31746)[

![](https://t2.gstatic.com/faviconV2?url=https://humane-intelligence.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://humane-intelligence.org/insights/)[

![](https://t3.gstatic.com/faviconV2?url=https://researcher2.eleuther.ai/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://researcher2.eleuther.ai/get-involved/)[

![](https://t3.gstatic.com/faviconV2?url=https://www.minizinc.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://www.minizinc.org/challenge/)[

![](https://t2.gstatic.com/faviconV2?url=https://www.ssoar.info/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://www.ssoar.info/ssoar/bitstream/document/86729/1/86729_1.pdf)[

![](https://t0.gstatic.com/faviconV2?url=https://futurehealth.bmj.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://futurehealth.bmj.com/call-problems)[

![](https://t1.gstatic.com/faviconV2?url=https://arxiv.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://arxiv.org/html/2501.14249v8)[

![](https://t2.gstatic.com/faviconV2?url=https://humane-intelligence.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://humane-intelligence.org/programs-services/bias-bounty/challenge-set-1/)[

![](https://t2.gstatic.com/faviconV2?url=https://humane-intelligence.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://humane-intelligence.org/programs-services/)[

![](https://t3.gstatic.com/faviconV2?url=https://scale.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://scale.com/)[

![](https://t3.gstatic.com/faviconV2?url=https://fairnow.ai/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://fairnow.ai/)[

![](https://t3.gstatic.com/faviconV2?url=https://hfc.scale.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://hfc.scale.com/)[

![](https://t2.gstatic.com/faviconV2?url=https://dimesociety.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://dimesociety.org/ai-implementation-in-healthcare-playbook/ai-tool-selection-guide/ai-tool-evaluation-essentials/)[

![](https://t3.gstatic.com/faviconV2?url=https://siliconangle.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://siliconangle.com/2024/05/29/scale-ai-publishes-first-llm-leaderboards-ranking-performance-ai-models-specific-domains/)[

![](https://t2.gstatic.com/faviconV2?url=https://huggingface.co/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://huggingface.co/datasets/bigcode/the-stack)[

![](https://t3.gstatic.com/faviconV2?url=https://crfm.stanford.edu/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://crfm.stanford.edu/fmti/May-2024/company-reports/BigCode-HuggingFace-ServiceNow_StarCoder.html)[

![](https://t1.gstatic.com/faviconV2?url=https://r.jordan.im/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://r.jordan.im/download/language-models/kocetkov2022.pdf)[

![](https://t3.gstatic.com/faviconV2?url=https://www.opensourceforu.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://www.opensourceforu.com/2022/09/bigcode-project-an-ai-system-that-generates-open-source-code-is-available/)[

![](https://t1.gstatic.com/faviconV2?url=https://github.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://github.com/masakhane-io/masakhane-mt)[

![](https://t1.gstatic.com/faviconV2?url=https://www.masakhane.io/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://www.masakhane.io/ongoing-projects/masakhane-mt-decolonise-science)[

![](https://t1.gstatic.com/faviconV2?url=https://www.masakhane.io/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://www.masakhane.io/community)[

![](https://t1.gstatic.com/faviconV2?url=https://www.masakhane.io/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://www.masakhane.io/events/social-icml-2022)[

![](https://t2.gstatic.com/faviconV2?url=https://pmc.ncbi.nlm.nih.gov/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://pmc.ncbi.nlm.nih.gov/articles/PMC10436040/)[

![](https://t0.gstatic.com/faviconV2?url=https://www.silkroadnlp.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://www.silkroadnlp.org/about)[

![](https://t1.gstatic.com/faviconV2?url=https://turing.iimas.unam.mx/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://turing.iimas.unam.mx/americasnlp/2025_st_1.html)[

![](https://t3.gstatic.com/faviconV2?url=https://mlcommons.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://mlcommons.org/working-groups/ai-risk-reliability/ai-risk-reliability/)[

![](https://t3.gstatic.com/faviconV2?url=https://mlcommons.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://mlcommons.org/2025/10/ailuminate-jailbreak-v05/)[

![](https://t3.gstatic.com/faviconV2?url=https://mlcommons.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://mlcommons.org/ailuminate/safety/)[

![](https://t3.gstatic.com/faviconV2?url=https://mlcommons.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://mlcommons.org/benchmarks/ailuminate/)[

![](https://t3.gstatic.com/faviconV2?url=https://mlcommons.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://mlcommons.org/2025/11/iso-aus/)[

![](https://t2.gstatic.com/faviconV2?url=https://satml.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://satml.org/competitions/)[

![](https://t3.gstatic.com/faviconV2?url=https://www.gamesec-conf.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://www.gamesec-conf.org/)[

![](https://t2.gstatic.com/faviconV2?url=https://www.imda.gov.sg/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://www.imda.gov.sg/activities/activities-catalogue/singapore-ai-safety-red-teaming-challenge)[

![](https://t2.gstatic.com/faviconV2?url=https://humane-intelligence.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://humane-intelligence.org/get-involved/events/)[

![](https://t1.gstatic.com/faviconV2?url=https://www.zooniverse.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://www.zooniverse.org/projects)[

![](https://t1.gstatic.com/faviconV2?url=https://www.zooniverse.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://www.zooniverse.org/)[

![](https://t1.gstatic.com/faviconV2?url=https://www.nsta.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://www.nsta.org/connected-science-learning/connected-science-learning-april-june-2020/discover-wild-world-citizen)[

![](https://t1.gstatic.com/faviconV2?url=https://blog.zooniverse.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://blog.zooniverse.org/2025/04/)[

![](https://t0.gstatic.com/faviconV2?url=https://www.aclweb.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://www.aclweb.org/portal/content/call-participation-semeval-2026-task-8-mtrageval-evaluating-multi-turn-rag-conversations)[

![](https://t3.gstatic.com/faviconV2?url=https://www.codabench.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://www.codabench.org/competitions/10669/)[

![](https://t1.gstatic.com/faviconV2?url=https://semeval.github.io/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://semeval.github.io/)[

![](https://t1.gstatic.com/faviconV2?url=https://semeval.github.io/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://semeval.github.io/SemEval2026/cft.html)[

![](https://t2.gstatic.com/faviconV2?url=https://markets.financialcontent.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://markets.financialcontent.com/whittierdailynews/quote/news?CurrentPage=2&ChannelType=NEWS&Symbol=NQ%3AWMT)[

![](https://t1.gstatic.com/faviconV2?url=https://www.lesswrong.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://www.lesswrong.com/posts/iiHReWZKxqn9wo75R/the-evolution-of-agentic-ai-evaluation)[

![](https://t1.gstatic.com/faviconV2?url=https://labelbox.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://labelbox.com/guides/labelbox-leaderboards-redefining-ai-evaluation-with-human-assessments/)[

![](https://t1.gstatic.com/faviconV2?url=https://arxiv.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://arxiv.org/html/2412.04363v1)[

![](https://t0.gstatic.com/faviconV2?url=https://01.me/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://01.me/en/2024/04/chatbot-arena/)[

![](https://t1.gstatic.com/faviconV2?url=https://github.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://github.com/open-compass/opencompass)[

![](https://t0.gstatic.com/faviconV2?url=https://opencompass-test.readthedocs.io/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://opencompass-test.readthedocs.io/_/downloads/en/latest/epub/)[

![](https://t1.gstatic.com/faviconV2?url=https://pypi.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://pypi.org/project/opencompass/0.1.7/)[

![](https://t1.gstatic.com/faviconV2?url=https://www.unesco.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://www.unesco.org/en/articles/ai-and-education-collective-intelligence-futures-perspective)[

![](https://t1.gstatic.com/faviconV2?url=https://www.cmu.edu/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://www.cmu.edu/tepper/news/stories/2024/0920-collective-intelligence-and-llms)[

![](https://t3.gstatic.com/faviconV2?url=https://ci2024.weebly.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://ci2024.weebly.com/special-issue.html)[

![](https://t2.gstatic.com/faviconV2?url=https://pmc.ncbi.nlm.nih.gov/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://pmc.ncbi.nlm.nih.gov/articles/PMC12093911/)[

![](https://t2.gstatic.com/faviconV2?url=https://ci.acm.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://ci.acm.org/2023/submit.html)[

![](https://t0.gstatic.com/faviconV2?url=https://www.humancellatlas.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://www.humancellatlas.org/learn-more/frequently-asked-questions/)[

![](https://t2.gstatic.com/faviconV2?url=https://pmc.ncbi.nlm.nih.gov/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://pmc.ncbi.nlm.nih.gov/articles/PMC5762154/)[

![](https://t0.gstatic.com/faviconV2?url=https://www.humancellatlas.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://www.humancellatlas.org/publications/)[

![](https://t1.gstatic.com/faviconV2?url=https://elifesciences.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://elifesciences.org/articles/27041)[

![](https://t0.gstatic.com/faviconV2?url=https://www.humancellatlas.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://www.humancellatlas.org/news/multi-tissue-cell-atlases-lead-to-leap-of-understanding-of-immunity-and-disease/)[

![](https://t2.gstatic.com/faviconV2?url=https://www.springernature.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://www.springernature.com/gp/group/media/press-releases)[

![](https://t0.gstatic.com/faviconV2?url=https://curiosityneverkilledthewriter.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://curiosityneverkilledthewriter.com/58-calls-for-submissions-in-february-2026-paying-markets-95a307d5e8ca)[

![](https://t0.gstatic.com/faviconV2?url=https://mizna.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://mizna.org/mizna-online/30-new-swana-books-to-read-in-2026/)[

![](https://t1.gstatic.com/faviconV2?url=https://agi.safe.ai/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://agi.safe.ai/)[

![](https://t3.gstatic.com/faviconV2?url=https://www.codabench.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://www.codabench.org/competitions/9719/)[

![](https://t1.gstatic.com/faviconV2?url=https://github.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://github.com/pln-fing-udelar/semeval-2026-humor-gen)[

![](https://t0.gstatic.com/faviconV2?url=https://www.aclweb.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://www.aclweb.org/portal/content/semeval-2026-task-1-mwahaha-models-write-automatic-humor-and-humans-annotate)[

![](https://t0.gstatic.com/faviconV2?url=https://groups.google.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://groups.google.com/g/semeval-2026-task-1-humor-gen)[

![](https://t1.gstatic.com/faviconV2?url=https://sig-edu.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://sig-edu.org/sharedtasks)[

![](https://t0.gstatic.com/faviconV2?url=https://www.aclweb.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://www.aclweb.org/portal/events?order=field_event_date&sort=desc)[

![](https://t0.gstatic.com/faviconV2?url=https://www.aclweb.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://www.aclweb.org/portal/events?order=field_event_city&sort=asc)[

![](https://t2.gstatic.com/faviconV2?url=https://aclanthology.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://aclanthology.org/venues/ws/)[

![](https://t1.gstatic.com/faviconV2?url=https://cocoxu.github.io/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://cocoxu.github.io/)[

![](https://t2.gstatic.com/faviconV2?url=https://www.techpolicy.press/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://www.techpolicy.press/the-uns-global-dialogue-on-ai-must-give-citizens-a-real-seat-at-the-table/)[

![](https://t0.gstatic.com/faviconV2?url=https://medium.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://medium.com/patrick-j-mcgovern-foundation/divya-siddarth-is-shaping-ai-with-global-input-995313b5adf0)[

![](https://t1.gstatic.com/faviconV2?url=https://ash.harvard.edu/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://ash.harvard.edu/programs/allen-lab-technology/)[

![](https://t2.gstatic.com/faviconV2?url=https://www.mpib-berlin.mpg.de/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://www.mpib-berlin.mpg.de/press-releases/llms-and-collective-intelligence)[

![](https://t1.gstatic.com/faviconV2?url=https://arxiv.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://arxiv.org/html/2601.21960v1)[

![](https://t0.gstatic.com/faviconV2?url=https://www.researchgate.net/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://www.researchgate.net/publication/400236476_TidyVoice_2026_Challenge_Evaluation_Plan)[

![](https://t3.gstatic.com/faviconV2?url=https://datacollective.mozillafoundation.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://datacollective.mozillafoundation.org/datasets/cmihtsewu023so207xot1iqqw)[

![](https://t1.gstatic.com/faviconV2?url=https://blog.mozilla.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://blog.mozilla.org/l10n/2026/01/07/mozilla-localization-in-2025/)[

![](https://t0.gstatic.com/faviconV2?url=https://research.google/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://research.google/blog/introducing-cvss-a-massively-multilingual-speech-to-speech-translation-corpus/)[

![](https://t2.gstatic.com/faviconV2?url=https://aclanthology.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://aclanthology.org/2024.americasnlp-1.28/)[

![](https://t1.gstatic.com/faviconV2?url=https://www.mdpi.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://www.mdpi.com/2076-3417/14/15/6497)[

![](https://t2.gstatic.com/faviconV2?url=https://aclanthology.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://aclanthology.org/volumes/2024.americasnlp-1/)[

![](https://t0.gstatic.com/faviconV2?url=https://groups.google.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://groups.google.com/g/wmt-tasks)[

![](https://t0.gstatic.com/faviconV2?url=https://list.elra.info/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://list.elra.info/mailman3/hyperkitty/list/corpora@list.elra.info/latest?amp%3Bpage=268&page=115)[

![](https://t0.gstatic.com/faviconV2?url=https://www.aisafety.camp/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://www.aisafety.camp/)[

![](https://t1.gstatic.com/faviconV2?url=https://www.lesswrong.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://www.lesswrong.com/posts/3sjtEXzbwDpyALR4H/ai-safety-camp-10-outputs)[

![](https://t0.gstatic.com/faviconV2?url=https://manifund.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://manifund.org/projects/11th-edition-of-ai-safety-camp)[

![](https://t2.gstatic.com/faviconV2?url=https://www.matsprogram.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://www.matsprogram.org/team)[

![](https://t3.gstatic.com/faviconV2?url=https://forum.effectivealtruism.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://forum.effectivealtruism.org/posts/CuPnmeS4v5sFE6nQj/impact-assessment-of-ai-safety-camp-arb-research)[

![](https://t2.gstatic.com/faviconV2?url=https://www.matsprogram.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://www.matsprogram.org/program/summer-2026)[

![](https://t2.gstatic.com/faviconV2?url=https://www.matsprogram.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://www.matsprogram.org/)[

![](https://t2.gstatic.com/faviconV2?url=https://www.matsprogram.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://www.matsprogram.org/faq)[

![](https://t3.gstatic.com/faviconV2?url=https://www.cognitiverevolution.ai/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://www.cognitiverevolution.ai/building-scaling-the-ai-safety-research-community-with-ryan-kidd-of-mats/)[

![](https://t0.gstatic.com/faviconV2?url=https://sparai.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://sparai.org/)[

![](https://t3.gstatic.com/faviconV2?url=https://lastexam.ai/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://lastexam.ai/)[

![](https://t1.gstatic.com/faviconV2?url=https://semeval.github.io/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://semeval.github.io/SemEval2026/tasks.html)[

![](https://t1.gstatic.com/faviconV2?url=https://epoch.ai/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://epoch.ai/frontiermath/tiers-1-4/about)[

![](https://t1.gstatic.com/faviconV2?url=https://epoch.ai/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://epoch.ai/benchmarks/frontiermath)[

![](https://t1.gstatic.com/faviconV2?url=https://epoch.ai/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://epoch.ai/blog/openai-and-frontiermath)[

![](https://t1.gstatic.com/faviconV2?url=https://epoch.ai/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://epoch.ai/frontiermath)[

![](https://t1.gstatic.com/faviconV2?url=https://arxiv.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://arxiv.org/html/2411.04872v7)[

![](https://t1.gstatic.com/faviconV2?url=https://github.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://github.com/open-compass/VLMEvalKit)[

![](https://t1.gstatic.com/faviconV2?url=https://arxiv.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://arxiv.org/html/2601.09668v1)[

![](https://t1.gstatic.com/faviconV2?url=https://arxiv.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://arxiv.org/html/2601.11960v1)[

![](https://t1.gstatic.com/faviconV2?url=https://arxiv.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://arxiv.org/html/2602.00505v1)[

![](https://t1.gstatic.com/faviconV2?url=https://github.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://github.com/bigscience-workshop/bigscience)[

![](https://t0.gstatic.com/faviconV2?url=https://automatorslab.ai/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://automatorslab.ai/blog/guide/huggingface-statistics/)[

![](https://t2.gstatic.com/faviconV2?url=https://huggingface.co/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://huggingface.co/papers?q=standardized%20taxonomy)[

![](https://t2.gstatic.com/faviconV2?url=https://huggingface.co/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://huggingface.co/datasets/bigbio/chemprot)[

![](https://t2.gstatic.com/faviconV2?url=https://kairntech.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://kairntech.com/blog/articles/top-open-source-llm-models-in-2026/)[

![](https://t2.gstatic.com/faviconV2?url=https://hltcoe.jhu.edu/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://hltcoe.jhu.edu/research/scale/scale-2026/)[

![](https://t2.gstatic.com/faviconV2?url=https://openreview.net/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://openreview.net/pdf/0ab9d1236ec0d8a1c512c63ad3d09c2fd850c5c4.pdf)[

![](https://t2.gstatic.com/faviconV2?url=https://openlifescience-ai.github.io/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://openlifescience-ai.github.io/ai-deadlines/)[

![](https://t0.gstatic.com/faviconV2?url=https://journal.hep.com.cn/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://journal.hep.com.cn/fcs/EN/10.1007/s11704-023-2525-y)[

![](https://t0.gstatic.com/faviconV2?url=https://f1000research.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://f1000research.com/articles/7-803)[

![](https://t0.gstatic.com/faviconV2?url=https://www.researchgate.net/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://www.researchgate.net/publication/399901985_Recognition_in_numbers_can_authorship_norms_in_large_research_teams_help_reform_research_assessment_practices)[

![](https://t0.gstatic.com/faviconV2?url=https://www.researchgate.net/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://www.researchgate.net/publication/262276620_Massively_distributed_authorship_of_academic_papers)[

![](https://t2.gstatic.com/faviconV2?url=https://www.southampton.ac.uk/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://www.southampton.ac.uk/about/governance/regulations-policies/policies/authorship-contribution-publishing)[

![](https://t3.gstatic.com/faviconV2?url=https://www.govinfo.gov/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://www.govinfo.gov/content/pkg/GPO-TNW-26-1-2025/pdf/GPO-TNW-26-1-2025.pdf)[

![](https://t2.gstatic.com/faviconV2?url=https://www.fwf.ac.at/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://www.fwf.ac.at/en/news/detail/open-science-2025-new-top-citizen-science-projects-bring-society-and-research-together)[

![](https://t0.gstatic.com/faviconV2?url=https://www.societyforscience.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://www.societyforscience.org/research-at-home/citizen-science/)[

![](https://t2.gstatic.com/faviconV2?url=https://www.nasa.gov/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://www.nasa.gov/ames/space-biosciences/slstp-projects/)[

![](https://t3.gstatic.com/faviconV2?url=https://participatorysciences.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://participatorysciences.org/conferences/caps-2026/program/)[

![](https://t1.gstatic.com/faviconV2?url=https://science.nasa.gov/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://science.nasa.gov/citizen-science/)[

![](https://t0.gstatic.com/faviconV2?url=https://moda.gov.tw/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://moda.gov.tw/en/major-policies/alignment-assemblies/1453)[

![](https://t0.gstatic.com/faviconV2?url=https://openfuture.eu/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://openfuture.eu/our-work/ai-and-the-commons/)[

![](https://t1.gstatic.com/faviconV2?url=https://ash.harvard.edu/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://ash.harvard.edu/resources/cooperative-paradigms-for-artificial-intelligence/)[

![](https://t3.gstatic.com/faviconV2?url=https://democracy-technologies.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://democracy-technologies.org/participation/consensus-building-in-taiwan/)[

![](https://t2.gstatic.com/faviconV2?url=https://codalab.lisn.upsaclay.fr/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://codalab.lisn.upsaclay.fr/competitions/)[

![](https://t0.gstatic.com/faviconV2?url=https://raduionescu.herokuapp.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://raduionescu.herokuapp.com/)[

![](https://t1.gstatic.com/faviconV2?url=https://www.mlsafety.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://www.mlsafety.org/safebench/about)[

![](https://t0.gstatic.com/faviconV2?url=https://safe.ai/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://safe.ai/work/field-building)[

![](https://t1.gstatic.com/faviconV2?url=https://www.mlsafety.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://www.mlsafety.org/safebench/winners)[

![](https://t1.gstatic.com/faviconV2?url=https://newsletter.mlsafety.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://newsletter.mlsafety.org/)[

![](https://t0.gstatic.com/faviconV2?url=https://futurehealth.bmj.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://futurehealth.bmj.com/newsletters)[

![](https://t2.gstatic.com/faviconV2?url=https://jcom.sissa.it/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://jcom.sissa.it/articles/keyword/26/)[

![](https://t2.gstatic.com/faviconV2?url=https://iucn.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://iucn.org/resources)[

![](https://t1.gstatic.com/faviconV2?url=https://science.nasa.gov/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://science.nasa.gov/citizen-science/publications/)[

![](https://t1.gstatic.com/faviconV2?url=https://www.zooniverse.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://www.zooniverse.org/about/publications)[

![](https://t3.gstatic.com/faviconV2?url=https://academic.oup.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://academic.oup.com/bioscience/article/74/4/290/7647240)[

![](https://t1.gstatic.com/faviconV2?url=https://eosc.eu/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://eosc.eu/wp-content/uploads/2022/09/National-Guidelines-for-Open-Science_SE_2024.pdf)[

![](https://t3.gstatic.com/faviconV2?url=https://openscience.se/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://openscience.se/en/national-guidelines-for-open-science/areas-within-open-science)[

![](https://t3.gstatic.com/faviconV2?url=https://cscw.acm.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://cscw.acm.org/2026/rolling.html)[

![](https://t2.gstatic.com/faviconV2?url=https://www.imaging.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://www.imaging.org/IST/IST/Conferences/Archiving/Archiving2026/Archiving2026_Home.aspx?46c611a9cb64=7)[

![](https://t2.gstatic.com/faviconV2?url=https://www.maastrichtuniversity.nl/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://www.maastrichtuniversity.nl/file/um-open-science-policy-update-2022-v13pdf)[

![](https://t3.gstatic.com/faviconV2?url=https://scale.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://scale.com/careers/4574113005)[

![](https://t3.gstatic.com/faviconV2?url=https://careerservices.fas.harvard.edu/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://careerservices.fas.harvard.edu/jobs/scale-ai-human-frontier-collective-hfc-human-frontier-collective-medical-fellow/)[

![](https://t3.gstatic.com/faviconV2?url=https://scale.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://scale.com/careers/4591782005)[

![](https://t3.gstatic.com/faviconV2?url=https://scale.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://scale.com/careers/4613327005)[

![](https://t1.gstatic.com/faviconV2?url=https://github.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://github.com/InternLM/POLAR)[

![](https://t1.gstatic.com/faviconV2?url=https://github.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://github.com/InternLM/InternLM)[

![](https://t1.gstatic.com/faviconV2?url=https://lmdeploy.readthedocs.io/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://lmdeploy.readthedocs.io/_/downloads/en/latest/pdf/)[

![](https://t3.gstatic.com/faviconV2?url=https://icml.cc/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://icml.cc/virtual/2025/poster/43831)[

![](https://t0.gstatic.com/faviconV2?url=https://www.researchgate.net/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://www.researchgate.net/publication/394830650_Intern-S1_A_Scientific_Multimodal_Foundation_Model)[

![](https://t0.gstatic.com/faviconV2?url=https://www.researchgate.net/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://www.researchgate.net/publication/399809627_Institutional_AI_A_Governance_Framework_for_Distributional_AGI_Safety)[

![](https://t1.gstatic.com/faviconV2?url=https://arxiv.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://arxiv.org/html/2601.10599v1)[

![](https://t2.gstatic.com/faviconV2?url=https://www.sigarch.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://www.sigarch.org/call-contributions/)[

![](https://t1.gstatic.com/faviconV2?url=https://arxiv.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://arxiv.org/html/2602.00014v1)[

![](https://t2.gstatic.com/faviconV2?url=https://openreview.net/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://openreview.net/)[

![](https://t3.gstatic.com/faviconV2?url=https://2025.emnlp.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://2025.emnlp.org/calls/main_conference_papers/)[

![](https://t3.gstatic.com/faviconV2?url=https://fever.ai/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://fever.ai/workshop.html)[

![](https://t1.gstatic.com/faviconV2?url=https://arxiv.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://arxiv.org/html/2601.18724v1)[

![](https://t0.gstatic.com/faviconV2?url=https://lib.msu.edu/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://lib.msu.edu/collections/scholcomm/support)[

![](https://t1.gstatic.com/faviconV2?url=https://www.butlernature.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://www.butlernature.com/2026/01/29/when-tree-planting-helps-nature-and-when-it-doesnt/)[

![](https://t0.gstatic.com/faviconV2?url=https://scitechdaily.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://scitechdaily.com/massive-global-study-rewrites-the-biology-of-type-2-diabetes/)[

![](https://t1.gstatic.com/faviconV2?url=https://github.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://github.com/yuzhimanhua/Awesome-Scientific-Language-Models)[

![](https://t1.gstatic.com/faviconV2?url=https://backend.orbit.dtu.dk/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://backend.orbit.dtu.dk/ws/files/305410313/1_s2.0_S0166361522002330_main.pdf)[

![](https://t2.gstatic.com/faviconV2?url=https://archive.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://archive.org/stream/PC-Mag-1982-11/PC-Mag-1982-11_djvu.txt)[

![](https://t1.gstatic.com/faviconV2?url=http://isabelle.systems/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](http://isabelle.systems/zulip-archive/stream/247541-Mirror.3A-Isabelle-Users-Mailing-List/index.html)[

![](https://t1.gstatic.com/faviconV2?url=https://isabelle.systems/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://isabelle.systems/zulip-archive/stream/336180-Archive-Mirror.3A-Isabelle-Users-Mailing-List/index.html)[

![](https://t2.gstatic.com/faviconV2?url=https://humane-intelligence.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://humane-intelligence.org/programs-services/bias-bounty/challenge-set-3/)[

![](https://t2.gstatic.com/faviconV2?url=https://humane-intelligence.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://humane-intelligence.org/programs-services/bias-bounty/)[

![](https://t2.gstatic.com/faviconV2?url=https://www.cm.law/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://www.cm.law/cassat-builtin-algorithmic-bias-bounties/)[

![](https://t2.gstatic.com/faviconV2?url=https://pmc.ncbi.nlm.nih.gov/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://pmc.ncbi.nlm.nih.gov/articles/PMC12851929/)[

![](https://t0.gstatic.com/faviconV2?url=https://www.researchgate.net/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://www.researchgate.net/publication/400185039_A_benchmark_of_expert-level_academic_questions_to_assess_AI_capabilities)[

![](https://t1.gstatic.com/faviconV2?url=https://arxiv.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://arxiv.org/html/2501.14249v2)[

![](https://t1.gstatic.com/faviconV2?url=https://arxiv.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://arxiv.org/html/2501.14249v1)[

![](https://t3.gstatic.com/faviconV2?url=https://pure.manchester.ac.uk/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://pure.manchester.ac.uk/ws/portalfiles/portal/356660354/2501.14249v2.pdf)[

![](https://t0.gstatic.com/faviconV2?url=https://static.scale.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://static.scale.com/uploads/654197dc94d34f66c0f5184e/Publication%20Ready%20Humanity's%20Last%20Exam.pdf)[

![](https://t0.gstatic.com/faviconV2?url=https://www.researchgate.net/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://www.researchgate.net/publication/388400409_Humanity's_Last_Exam_Organizing_Team_Dataset_Contributors)[

![](https://t1.gstatic.com/faviconV2?url=https://arxiv.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://arxiv.org/html/2502.13320v2)[

![](https://t2.gstatic.com/faviconV2?url=https://pmc.ncbi.nlm.nih.gov/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://pmc.ncbi.nlm.nih.gov/articles/PMC3041584/)[

![](https://t2.gstatic.com/faviconV2?url=https://jcom.sissa.it/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://jcom.sissa.it/article/pubid/JCOM_2005_2021_A02/)[

![](https://t2.gstatic.com/faviconV2?url=https://ec.europa.eu/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://ec.europa.eu/research/participants/documents/downloadPublic?documentIds=080166e5beac2f88&appId=PPGMS)[

![](https://t1.gstatic.com/faviconV2?url=https://academiccommons.columbia.edu/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://academiccommons.columbia.edu/doi/10.7916/575j-ac46/download)[

![](https://t2.gstatic.com/faviconV2?url=https://openreview.net/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://openreview.net/pdf?id=MB_O268uCY)[

![](https://t3.gstatic.com/faviconV2?url=https://calmatters.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://calmatters.org/economy/technology/2024/07/ai-tests/)[

![](https://t3.gstatic.com/faviconV2?url=https://ieeexplore.ieee.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://ieeexplore.ieee.org/iel8/8566059/10680473/10664609.pdf)[

![](https://t2.gstatic.com/faviconV2?url=https://pmc.ncbi.nlm.nih.gov/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://pmc.ncbi.nlm.nih.gov/articles/PMC11573903/)[

![](https://t3.gstatic.com/faviconV2?url=https://www.tandfonline.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://www.tandfonline.com/doi/full/10.1080/14479338.2023.2215740)[

![](https://t0.gstatic.com/faviconV2?url=https://www.afdb.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://www.afdb.org/sites/default/files/documents/publications/africas_ai_productivity_gain_afdb_detailed_report_1.pdf)[

![](https://t1.gstatic.com/faviconV2?url=https://bsky.app/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://bsky.app/profile/humaneintelligence.bsky.social)[

![](https://t2.gstatic.com/faviconV2?url=https://malakumar.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://malakumar.com/tech-social-good-strategy-design/)[

![](https://t1.gstatic.com/faviconV2?url=https://www.mlsafety.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://www.mlsafety.org/events/neurips/2024)[

![](https://t1.gstatic.com/faviconV2?url=https://www.mlsafety.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://www.mlsafety.org/resources)[

![](https://t1.gstatic.com/faviconV2?url=https://aigs.ca/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://aigs.ca/resources/)[

![](https://t1.gstatic.com/faviconV2?url=https://www.mlsafety.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://www.mlsafety.org/safebench)[

![](https://t1.gstatic.com/faviconV2?url=https://www.lesswrong.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://www.lesswrong.com/posts/3onCb5ph3ywLQZMX2/alignment-newsletter-one-year-retrospective)[

![](https://t1.gstatic.com/faviconV2?url=https://agi.safe.ai/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://agi.safe.ai/dashboard)[

![](https://t2.gstatic.com/faviconV2?url=https://humane-intelligence.org/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

Opens in a new window](https://humane-intelligence.org/post/announcing-bias-bounties-at-scale/)
