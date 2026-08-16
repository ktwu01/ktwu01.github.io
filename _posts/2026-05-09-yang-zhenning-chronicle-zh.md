---
title: "我用一周为杨振宁建了一座年鉴，家谱才是真正的故事"
date: 2026-05-09
permalink: /zh/posts/2026/05/yang-zhenning-chronicle/
tags:
  - Yang Zhenning
  - chronicle
  - science of science
  - academic genealogy
  - Tsinghua
  - Nobel
  - USTC
---
大多数物理本科生知道杨振宁是诺贝尔奖得主，知道他是 Yang-Mills 里的那个 Yang。而为他建一座年鉴，让我看到了教科书略过的东西：他一生中最有分量的一个事实是谁是他的父亲，以及那个父亲在他出生之前，为他铺好了什么。

> 作者：[Koutian Wu](https://www.linkedin.com/in/ktwu01/)；[GitHub: ktwu01](https://github.com/ktwu01/)

> 年鉴网站：[ut01.github.io/chen-ning-yang-chronicle](https://ut01.github.io/chen-ning-yang-chronicle/)。配套文章：[杨振宁到底多有钱？](/posts/2026/05/yang-zhenning-wealth-questions/)。可复现图表：[github.com/ktwu01/yang-zhenning-wealth-figures](https://github.com/ktwu01/yang-zhenning-wealth-figures)。这三者设计成一起阅读。

> 这座年鉴是从 [Sean Xiang 年鉴模板](https://github.com/ktwu01/sean-xiang-chronicle) 分叉出来的一批之一，全部由我和 UT Austin 的同事构建。完整目录：[Ashley Matheny](https://ut01.github.io/ashley-matheny-chronicle/)、[Chen Ning Yang](https://ut01.github.io/chen-ning-yang-chronicle/)、[Daniella Rempe](https://ut01.github.io/daniella-rempe-chronicle/)、[Eric C. Greene](https://yzliu03.github.io/Eric-Greene-chronicle/)、[Geeta Persad](https://ut01.github.io/geeta-persad-chronicle/)、[Gengchen Mai](https://ut01.github.io/gengchen-mai-chronicle/)、[Juan Santiago](https://qijiang-yoyo.github.io/juan-santiago-chronicle/)、[Kehan Dong](https://ut01.github.io/kehan-dong-chronicle/)、[Marc Hesse](https://ut01.github.io/marc-hesse-chronicle/)、[Sean Xiang](https://ktwu01.github.io/sean-xiang-chronicle/)、[Zong-Liang Yang](https://ktwugoat.github.io/zong-liang-yang-chronicle/)。

2025 年 10 月 18 日杨教授去世时，中国的互联网立刻做了它每次面对一位著名老人去世都会做的事：开始争论钱。是 18 亿人民币吗？第二任妻子要继承吗？第一段婚姻的孩子们怎么办？我围观了这件事几周，注意到两件事。第一，几乎没有人引用真实数字，只有谣言。第二，问题本身是错的。杨一生有意思的部分，不是末尾的美元数字，而是开头的结构性设置。

于是我一口气建了三个东西。一篇长文，摆出问题并给出一个谨慎的估计（$10-50M，不是 $250M）。一个图表仓库，含 6 张可复现的 matplotlib 图，任何人都能重跑这个分析。以及一座年鉴，也就是我今天想重点写的，因为建造它的过程改变了我对项目其余部分的思考。

盖这些年鉴我已经做了一段时间了。最初的模板是我为 Sean Xiang 做的，那位我另写过文章的 X-Institute 联合创始人。从那时起，一小群 UT-Austin 同事和我把它分叉成一个年鉴目录，记录塑造了我们博士生涯的导师、前辈和人物：Daniella Rempe、Ashley Matheny、Zong-Liang Yang、Marc Hesse、Geeta Persad、Gengchen Mai、Eric Greene、Juan Santiago、Kehan Dong。每座年鉴都是一个由 JSON 驱动的页面，带时间线、故事地图和研究档案。约束条件是：一切都要有来源。你可以写任何你想写的叙事，但它必须落在一份真实的文件上。

杨振宁是我为素未谋面的人建的第一座年鉴。"一切都要有来源"这个约束在他的案例里出奇地高产，因为文献轨迹始于 1928 年——他父亲走进芝加哥大学，在 L. E. Dickson 指导下答辩一篇关于 Waring 问题的论文——而结束于 97 年后的清华教工住宅区。中间几乎每一件事都有地方记录在案。

填写时间线 JSON 时最击中我的，是他父亲周围那个紧密的簇。杨武之是中国第一位数论博士。他回到清华教书。杨家住在清华西院，那一片教工住宅里还住着陈寅恪、朱自清、闻一多、冯友兰和叶企孙。当全家随清华南迁避难时，振宁 15 岁，在西南联合大学的 2 万名考生里排名第 2。他在西南联大的本科导师是吴大猷。硕士导师是王竹溪。数学导师是陈省身，而陈省身上世纪 20 年代曾在清华做过杨武之的学生。他早年职业生涯里最要紧的三段学术关系，全是父亲同一系里的亲密同事。

你不可能在把这件事写进年鉴 JSON 的时候不注意到那个模式。1943 年的庚子赔款奖学金是一项全国竞争性奖学金。全国只有 6 个物理名额。杨赢下了一个。在 Edward Teller 指导下的芝加哥博士，比同辈学生快了四到五年，因为杨从中学起就在父亲的书架上预习 Dickson 的群论书。Wigner 休假那件事总是被框成一个幸运的巧合，它确实是,但更贴切的框架是：幸运巧合只会落在那些已经被带到门口的学生身上，才有产出。

这就是最近 Science of Science 文献已经放上数字的那类结构性模式。Novosad、Asher、Farquharson 和 Iljazi 2024 年发表了一篇工作论文，研究物理学、化学、医学和经济学领域的 739 位诺贝尔奖得主。得奖者父母的平均收入处于第 87 个百分位。平均父母教育处于第 90 个百分位。50% 到 60% 的得奖者来自前 5% 的家庭。Boulder 的 Morgan、Clauset 和同事 2022 年显示，美国终身教职的大学教授拥有博士学历父母的可能性是一般人口的 25 倍，而这个倍数在顶级大学几乎翻倍。Chetty 2019 年的《Lost Einsteins》论文显示，来自前 1% 家庭的孩子成为发明家的比例，是低于中位数家庭的孩子的 10 倍，即便控制三年级数学考试成绩后也是如此。Richard Tol 2024 年的 Scientometrics 论文把 727 位诺贝尔奖得主中的 696 位放到了同一棵学术家谱上，其中 668 位能追溯到 17 世纪巴塞尔的医学教授 Emmanuel Stupanus。

杨落在这每个分布的最右上端。他的家庭处于 1922 年中国社会的顶部 0.1%。他的父亲既有一流博士、又是一流大学教授。他坐在全球学术家谱的一个交汇节点上：Dickson → 杨武之这条数学线，与 Sommerfeld → Fermi/Teller 这条物理线在此相遇。年鉴让这一点可见，因为它逼你把日期和名字并排写下来。你没法告诉自己那个舒适的"他只是个恰好成功的聪明个体"的故事。结构性条件就出现在时间线上，不管你愿不愿意看。

更难写、我在年鉴最后一章尝试写了的部分，是怎么处理这些信息。承认杨的事业是由一堆结构性优势促成，并不会贬低他所做的。Yang-Mills 规范理论是 20 世纪物理学最重要的成果之一。与李政道那篇宇称不守恒论文是正确的物理。他挣得了自己的位置。但"他挣得了自己的位置"和"他的位置在他出生前就被铺好了"并不矛盾。两者同时为真，任何对自己诚实的传记阅读都必须同时握住它们。

年鉴结构逼迫我面对的，是这是常态、而非例外。如果我给居里夫人建一座年鉴，时间线会从一个波兰物理教授父亲开始。如果我给尼尔斯·玻尔建一座，会从他父母在哥本哈根办的哲学沙龙开始。如果我给 J.J. 汤姆孙建一座，会从曼彻斯特那个把他推向工程、然后偶然推进剑桥的书店家庭开始。这些都不是异常。它们是正典科学家传记的标准形状。诺贝尔委员会以一种特定方式书写它们，淡化了结构性那部分，但那部分只要你看就一直在。

年鉴还让另一个东西可见：所有这些声望都转化不了的财富差距。1957 年杨拿到的诺贝尔份额是 1957 年币值的 $20,177。如果他只是把它放进标普 500 拿住，到 2025 年会涨到大约 $13-18 million。在石溪做了 33 年爱因斯坦教授，他的工资大概还能攒出另外 $3-6 million。再加上 Bower 奖（1994 年 $250,000）、费萨尔国王奖（2001 年 $200,000），还有一长串更小的荣誉。扣除他捐给清华的约 $4 million，以及他拒绝领取 28 年的那笔捐赠年薪，他的身家很可能在 $10-50 million 区间。那是一大笔钱。但也比中国小报一直声称的那个 $250 million 少了 25 倍以上。而且比前沿实验室一位资深 AI 研究科学家 20 年职业生涯能攒下的钱，少了 200 倍以上。做 20 世纪理论物理学的经济账，不是做 21 世纪 AI 研究者的经济账。

我建这座年鉴的一部分原因，是为了让项目的其余部分变得可读。文章就科学特权提出论证，最终落到一个财富估计。图表仓库给你 matplotlib 代码。年鉴是那块连接组织，让读者能在杨的传记、science-of-science 文献和财富计算之间来回移动而不丢掉线索。

更大的原因，是我博士刚读了六个月，正在试图搞清楚自己正走在什么样的轨迹上。杨生命里的那个模式是真实的模式，我想正面去看它，而不是把目光移开。我自己的路不是杨的路。我是那个没有学术家庭资本就走进了深圳 X-Institute fellowship、如今在 Jackson 学院读博士的孩子。像杨那样的轨迹中有多大比例能从我这样的起点够到，正是 Chetty《Lost Einsteins》论文在大规模人口尺度上提出的问题。建这座年鉴，就是用传记分辨率，为一个具体的人、慢慢地问这个问题的方式之一。

如果你想看年鉴，它在 [ut01.github.io/chen-ning-yang-chronicle](https://ut01.github.io/chen-ning-yang-chronicle/)。配套长文在 [yang-zhenning-wealth-questions](/posts/2026/05/yang-zhenning-wealth-questions/)。可复现图表在 [github.com/ktwu01/yang-zhenning-wealth-figures](https://github.com/ktwu01/yang-zhenning-wealth-figures)。这个站点上所有年鉴分叉所凭据的那个模板，在 [github.com/ktwu01/sean-xiang-chronicle](https://github.com/ktwu01/sean-xiang-chronicle)。

留给这座年鉴的一句话，来自杨 1957 年诺贝尔晚宴的演讲，也是我在中科大二教楼他塑像前，在比我愿意承认的更多次期中考试前，一定会去向他求的那句："我对自己的中国血统和背景感到骄傲，正如我对现代科学——西方文明的组成部分之一——忠心耿耿一样。它是我为之付出了心血、并将继续付出心血的事业。"无论那个财富数字最终如何，这句话是他说身后留下的最重的东西。