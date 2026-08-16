---
title: "For Dating and Resource-Sharing Markets, Should You Use Traditional Search/Ads/Rec or AI Recommendation Algorithms?"
date: 2026-03-20
permalink: /posts/2026/03/search-ads-rec-vs-ai-matching/
tags:
  - 推荐系统
  - ai
  - 产品
  - 创业
---
I've been discussing this question with a friend lately. He wants to use AI for matching in the dating market; I think with a small sample size this is perfectly feasible, you don't even need to build any search/ads/rec system at all. Just ask the large language model directly, toss in a few users' profiles, and have it rank them; the whole process is very simple.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

But once the sample size grows, say to dozens or hundreds of users, direct ranking by a large language model starts to struggle, and only then do you genuinely need a small search/rec system to label and filter. So the question becomes: when should you use traditional search/ads/rec, and when should you bring in AI recommendation algorithms? Where is the boundary between the two? And if you are building for the dating market, or a founder-investor resource-sharing platform, how does the choice differ? I went and looked up some hands-on experience from the industry and organized my thinking here.

## What Traditional Search/Ads/Rec Is

"Search/ads/rec" is the collective name for search, advertising, and recommendation, the most mature traffic-distribution system in internet products. The core of the traditional approach is **tagging + rules + collaborative filtering**.

More concretely, the flow goes roughly like this: first tag users and content (age, region, interest, behavior), then get candidate sets through multi-channel recall (content-based recall, collaborative filtering recall, popular recall, and so on), then pass through coarse ranking, fine ranking, and re-ranking, and finally present the results to the user.

This system has run for over a decade on Taobao, Douyin, and Weibo, and it is very mature engineering-wise. Its strengths are that it's interpretable, tunable, and has relatively low data requirements. Its weaknesses are equally clear: cold start is hard, it's difficult to recommend accurately to new users with no behavior data; the tagging system needs manual maintenance and goes stale easily; and fundamentally it optimizes explicit feedback like "click-through rate," which doesn't necessarily capture what users really want.

## What AI Recommendation Algorithms Do

"AI recommendation" here mainly refers to two types: end-to-end deep learning models (like two-tower models and Transformer sequence models), and the large language model (LLM)-assisted recommendation that has risen in the past two years.

The core advance of deep learning recommender systems is: instead of relying on manual tagging, let the model learn representations (embeddings) of user preference from the behavior sequence on its own. YouTube, Netflix, and Spotify all use this approach. Its advantage is that it captures finer-grained preferences, generalizes better, and, given enough data, outperforms traditional methods by a wide margin.

LLM-assisted recommendation is the newer direction. Industry practice falls roughly into three uses: first, using LLM for feature engineering to generate richer semantic descriptions for items; second, using LLM for cold start, understanding preferences through conversation with new users; third, using LLM directly for recommendation decisions, having the model output recommendations straight from the user's natural language description. The third is not yet mainstream in industry, because it's high-latency and expensive, but people are already testing it in small-scale, high-value scenarios.

## The Distinctive Nature of the Dating Market

A dating platform is a very special scenario that differs fundamentally from e-commerce and short-video recommendation: **it is two-sided matching, and the outcome is mutually exclusive.** The person you recommend to A, if A likes them, the other person may not like A back. This isn't the one-way "does the user like this content" problem; it's a pairing problem that requires mutual willingness.

Hinge currently uses a recommendation system improved on the basis of the Gale-Shapley stable matching algorithm, combined with machine learning models to predict two-way interaction probability. In its early days OkCupid relied on heavy questionnaires for tagging and weighted similarity for matching, a classic traditional search/ads/rec approach. But OkCupid itself admits that questionnaire data is getting harder to collect, and users' willingness to fill it out is declining.

In the dating scenario, the problem with traditional tagging is that people often describe their own preferences inaccurately. Users say they're looking for someone "mature and steady," but actual behavior data shows they interact more with people who are "humorous and outgoing." Tags capture users' self-perception, not their real preferences. AI models learning from behavior sequences get closer to the truth.

But dating scenarios usually don't have large data volumes, especially in vertical niches (like highly educated or specific-occupation groups). With sparse data, the advantage of deep learning models shrinks dramatically, and the traditional rule-plus-tagging approach becomes more stable instead.

## The Founder-Investor Resource-Sharing Market

This scenario is more complex than dating, because there are more matching dimensions: industry track, investment stage, geography, investor portfolio preferences, founder funding needs... and this market's user base is usually tiny, nowhere near enough data to support a deep learning recommender system.

Current industry practice, on platforms like Metal, Seedblink, and EasyVC, is basically a hybrid strategy: use structured data (investment history, industry tags, stage preferences) for basic filtering, then use an LLM for semantic understanding of unstructured information (investors' public articles, founders' pitch decks), and finally generate matching recommendations. In essence this is a combination of "traditional rule filtering + LLM semantic enhancement," not pure AI recommendation.

This approach is correct. In scenarios with sparse data, tiny user scale, and extremely high value per match, the LLM's semantic understanding is the real incremental value: it can read a natural-language description like "we focus on pre-A rounds in climate tech," whereas a traditional tagging system has to decompose that sentence into a dozen fields before it can process it.

## My Judgment

Dating and founder-venture resource sharing both look like "two-sided matching," but they are fundamentally two different scenarios, and you can't use the same logic to design the product.

Dating is low-frequency. A person in a lifetime seriously dates a few times and marries once; behavior data is extremely sparse. More importantly, the final judgment in dating cannot be outsourced to an algorithm: you have to go see, go feel, go try yourself. All an algorithm can do is narrow the candidate set and put "possibly compatible" people in front of you; it cannot replace your judgment and shouldn't try to. In this scenario, over-relying on AI recommendation is itself a misjudgment of product direction.

Founder-investor resource sharing is completely different. Founders come into contact with dozens to hundreds of investors during fundraising, and investors read dozens of BPs every week; both sides are engaged in high-frequency, repetitive screening and judgment. This is a classic repeated-game scenario: every interaction produces data, and every rejection or advancement is a signal. In this scenario, the AI recommendation algorithm isn't "replacing" human judgment; it's acting as a judgment accelerator: it filters out mismatches and prioritizes what's worth your time. As data accumulates and the model gets more accurate, that flywheel is real.

But both scenarios share one thing: no matter what technology you use, the founder has to build the product themselves. It's not about finding a technical person, closing their eyes, and letting the algorithm run. A dating product needs the founder to genuinely understand what users are looking for, afraid of, and at which step they give up; an investment platform needs the founder to have fought through this circle themselves and know investors' real decision logic. The algorithm is a tool; product sense is the prerequisite. Without the latter, no matter how ingenious the former is built, it's empty.

## A Rebuttal Worth Taking Seriously

My friend is more optimistic: he believes AI can dramatically improve dating-match accuracy, that traditional tagging matching might only reach about 2% success, and that AI doing personality-level pairing could push that number to 35%.

I don't fully agree, but I don't want to dismiss it lightly either.

Taleb has a view: if something has existed for a long time, it may well continue to exist for longer. Dating intermediaries and matchmakers have been a human activity for thousands of years. How long has AI existed? From this angle, overemphasizing AI's role is dangerous.

But from another angle, AI's semantic understanding happens to resemble what a traditional matchmaker does. What does a matchmaker do? Listens to you talk, understands what you truly want, then matches in their head. That isn't tagging; it's semantic understanding. In this sense, using an LLM for dating matching is closer to how humans have handled this for millennia than collaborative filtering or tagging systems: it's more human, not more mechanical.

So I'm not pessimistic about AI's prospects in the dating scenario; I'm just cautious about the timeline. The realistic constraint is compute cost, and LLM-based large-scale ranking is still too expensive. The more important constraint is data and experience: it has to be done by someone who genuinely understands the industry, who first accumulates enough data, first thinks through the product logic, and only then designs the algorithm. The order cannot be reversed.