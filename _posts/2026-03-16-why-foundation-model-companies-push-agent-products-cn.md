---
title: '为什么大模型厂商还在亏钱，却还要拼命推 Agent 产品'
date: 2026-03-16
permalink: /posts/2026/03/why-foundation-model-companies-push-agent-products-cn/
tags:
  - AI
  - LLM
  - Economics
  - Agent
  - Strategy
---
真正值得警惕的信号不是 AI 公司增长太慢，而是它们增长得很快，现金流压力却仍在放大。

> 作者：[Koutian Wu](https://www.linkedin.com/in/ktwu01/)；[GitHub: ktwu01](https://github.com/ktwu01/)

很多人问：为什么 OpenAI、Anthropic、xAI 还在重投入，甚至继续推更重的 Agent 产品？答案不是一句“它们贪心”，而是当前行业还处在“先抢结构位置，再谈利润兑现”的阶段。

## 先上数据：增长很快，但投入同样凶猛

先看已经有公开来源支撑的事实（截至 2026-03）：

OpenAI 侧，Reuters 报道其 CFO 披露 2025 年年化收入已超过 200 亿美元（2024 年为 60 亿美元），同时算力容量从 2024 年的 0.6GW 升至 2025 年的 1.9GW。这个数字组合的含义很直接：收入在涨，但对算力供给的依赖也在同步放大。

Anthropic 侧，其官方公告显示 2026-02 完成 300 亿美元 Series G，投后估值 3800 亿美元；同一公告还给出 run-rate revenue 已到 140 亿美元。它不是没增长，而是在高速增长下继续融资扩张基础设施和产品能力。

xAI 侧，公开报道显示其在 2026 年初完成 200 亿美元融资，并继续把资金压到数据中心和算力建设上。这说明它当前更像资本开支驱动的竞赛，而不是“利润收割期”的企业形态。

“14B 亏损”这类具体亏损数字，目前主要来自媒体对内部预测文件的报道（例如 The Information，被 Reuters 转述），应视为“有来源的估算”，不是公司审计口径财报。

## 为什么说“Google / Meta 能赚钱”不等于“大模型天然赚钱”

Google 和 Meta 的公开财报给了一个很清楚的对照组：

Alphabet 2025 年营收 4028 亿美元、营业利润 1290 亿美元、资本开支 914 亿美元；其中 Google Services 营业利润 1394 亿美元，Google Cloud 营业利润 139 亿美元。它们能扛高投入，是因为本体业务现金机器足够强。

Meta 2025 年营收 2009.66 亿美元、营业利润 832.76 亿美元、资本开支 722.2 亿美元；同年 Reality Labs 经营亏损 191.93 亿美元。也就是说，Meta 是用 FoA 的利润池在持续补贴高投入前沿方向。

所以“头部科技公司有利润”这件事，不能简单外推为“独立基础模型公司已经进入稳态盈利”。

## 为什么会推 Agent：这是商业结构动作，不是产品情怀

Agent 的关键价值不在于“更酷”，而在于把一次性消费变成持续消费。

一次问答通常是低频、短链路；而接入搜索、浏览器、工具调用、长流程自动化之后，模型被调用的频率、时长和上下文深度都会抬升。这会直接改变单位用户的 token 消耗和留存结构。

换句话说，Agent 更像“使用密度放大器”：它把模型从答题工具，推向 workflow 基础设施。对厂商来说，这才是决定未来定价权和续费质量的关键战场。

## 这条路也有边界：高投入不自动等于高利润

要把话说完整：推 Agent 不是利润灵药。它只是给了平台一个更可能跑通长期商业化的路径。

所以更准确的说法不是“因为亏钱，所以推 Agent”；而是“在高烧钱竞赛里，谁先拿下高频工作流入口，谁更有机会把今天的亏损换成未来的结构性收益”。

这也是 OpenClaw 这类产品容易爆火的底层原因之一：它把 AI 从“对话框”推进到了“可持续执行的操作层”。

如果你想看产品层面的完整分析，可以看我那篇主文：[`OpenClaw：把命令行世界接成你的第二大脑`](../openclaw-second-brain-for-ai-workers-cn/)。

## Sources

- Reuters（OpenAI 年化收入与算力容量披露）：[OpenAI CFO says annualized revenue crosses $20 billion in 2025](https://www.reuters.com/business/openai-cfo-says-annualized-revenue-crosses-20-billion-2025-2026-01-19/)
- Anthropic 官方公告（Series G、估值、run-rate）：[Anthropic raises $30 billion in Series G funding](https://www.anthropic.com/news/anthropic-raises-30-billion-series-g-funding-380-billion-post-money-valuation)
- Reuters（xAI 融资）：[Musk's xAI raises $20 billion in upsized Series E funding round](https://reut.rs/3Nb1TLy)
- Reuters 转述（OpenAI 2026 亏损预测来源）：[OpenAI tops $25 billion in annualized revenue, The Information reports](https://www.reuters.com/technology/openai-tops-25-billion-annualized-revenue-last-month-information-reports-2026-03-05)
- The Information（OpenAI 亏损预测原始媒体来源）：[OpenAI Projections Imply Losses Tripling to $14 Billion in 2026](https://www.theinformation.com/articles/openai-projections-imply-losses-tripling-to-14-billion-in-2026)
- Alphabet 2025 Form 10-K（营收、营业利润、分部利润、CapEx）：[SEC filing](https://www.sec.gov/Archives/edgar/data/1652044/000165204426000018/goog-20251231.htm)
- Meta Q4/FY2025 业绩（收入、营业利润、Reality Labs 亏损、CapEx 指引）：[SEC Exhibit 99.1](https://www.sec.gov/Archives/edgar/data/1326801/000162828026003832/meta-12312025xexhibit991.htm)
