---
title: 'The Value of Benchmarks, Market Mispricing, and the Ability to Frame Questions: A Raw Conversation with My Good Bro from Northeast China at CMU'
date: 2026-07-11
permalink: /posts/2026/07/benchmark-value-market-and-scientific-question-setting/
tags:
  - AI
  - Benchmark
  - Research
  - Career
  - Science
  - Reflection
---

Does building a benchmark count as research, or is it “crowdfunding a paper”? Does it create public value or consume public resources? Can it build lasting capabilities, or is it useful only for a startup team trying to show investors its potential?

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

A few days ago, I discussed this question with a good friend from Northeast China who trains large models at CMU. I have preserved part of our original conversation below, followed by my interpretation.

The conversation partner remains anonymous and appears below as “my good bro from Northeast China (CMU).” His remarks reflect an informal private exchange and carry no institutional attribution.

## The original conversation

**Me:**

> It still makes a contribution.

**My good bro from Northeast China (CMU):**

> Benchmarks don't contribute that much 🤣

**Me:**

> Look at all these models from different companies. When they launch, don't they all need benchmarks to test how good they are?
>
> Designing the right questions to stump these models still takes skill.
>
> Research will eventually become, at its core, a matter of framing questions.
>
> Building a benchmark means bringing together a group of people who frame questions. The bar for those people will keep rising until they become some of the smartest people in the world.
>
> If you work with the smartest people in the world, things probably won't turn out too badly.

**My good bro from Northeast China (CMU):**

> Let me ask it another way. If I had to choose between training models and benchmarking them, I'd choose training. The main reason is that no company wants me 🤣

**Me:**

> The contribution and value of a piece of work, the barrier to doing it, and how outsiders evaluate it do not necessarily match.
>
> Some markets don't have narrow spreads. In other words, they aren't liquid enough.

**My good bro from Northeast China (CMU):**

> Even students on campus can benchmark models 🤣
>
> I was chatting recently with a USTC alumna at Amazon. She described this kind of work as consuming public resources.

**Me:**

> Classic Jiahao behavior, haha.

**My good bro from Northeast China (CMU):**

> I think the mainstream view in industry now is that benchmarking isn't serious work.
>
> People said PhD graduates working on LLM security couldn't find jobs. I think it's the same thing.
>
> The mainstream pipeline is still pre-training and post-training. Benchmarks? I'm not sure.
>
> Industry also generally thinks pre-training is more impressive than post-training. It's a hierarchy of contempt.
>
> The evaluation is something like this: a group writes a review paper and gets a pile of citations. The review is actually useless, just academic attention seeking.
>
> Applied to our side, some groups want to start companies and need to show investors their potential. So many people crowdsource a paper, combine their contributions with a novel angle, and submit it to Nature so investors think the team has potential. But after a few years, the benchmark may no longer mean anything.
>
> I still think that the techniques and firsthand experience from pre-training will survive much longer, no matter what happens.

**Me:**

> Congratulations, you have discovered the essence of how some people start companies 🤣🤣🤣
>
> Fair point.
>
> Are you working on pre-training or post-training now?

## My interpretation: our argument was about how value is recognized, not about benchmarks

On the surface, the conversation compared three kinds of work:

1. pre-training;
2. post-training;
3. benchmarks and evaluation.

The deeper question was this: **how much value a piece of work creates, how difficult it is, and how much the market will reward it do not automatically align.**

People often treat "what companies want to hire for now" as identical to "what has value." That reasoning may work in a liquid market with clear job definitions and frequent transactions. The research market is not fully efficient.

Research value often appears before evaluation systems catch up. Evaluation systems can also become inflated and then manufacture the appearance of value.

We therefore cannot ask only:

> Do companies want benchmark researchers now?

We must also ask:

> Does this benchmark define a problem that the future will have to solve?
> Does it establish a measurement standard that others must use?
> Does it turn a vague argument into reproducible results?
> Does it create data, tasks, evaluation infrastructure, and a research network?

If the answer is no, then my good bro from Northeast China at CMU is right. The work may amount to a group of people assembling questions, accumulating authors and citations, and then showing academia or investors that they have occupied a field.

When the answer is yes, the benchmark defines how the field judges progress.

## The low-barrier parts of benchmark production can be copied at scale

When my good bro from Northeast China at CMU said, "Even students on campus can benchmark models," he had a point.

Many benchmarks today follow this production process:

- collect tasks from existing question banks;
- convert their formats;
- call several models;
- produce a leaderboard;
- describe the failure cases;
- package the result under a new name.

This work can produce a paper without producing knowledge.

It measures a capability that someone else has already defined, or moves an old problem behind a new data interface. The leaderboard may become obsolete when the model version changes. Rankings may shift when the prompting strategy changes. The conclusion may collapse when training-data contamination comes to light.

This kind of benchmark may indeed have a short half-life.

The claim that "building benchmarks has value" therefore cannot stand without conditions.

A more accurate claim is:

> A benchmark constitutes a research contribution only when it defines a real, stable capability that is difficult to fake and produces interpretable signals when systems fail.

## The core of a high-value benchmark is deciding what deserves measurement, not writing questions

Writing a difficult question is not necessarily hard. Hiding the answer, adding context, or using obscure knowledge can all make a model fail.

The difficult part is answering these questions:

- Does this capability correspond to a bottleneck in the real world?
- When the model fails, can we determine why?
- When the model passes, has it acquired the capability, or has it exploited a shortcut?
- Can an expert following a reasonable process pass consistently?
- Does the evaluation distinguish missing knowledge, failed reasoning, failed tool use, coding failures, and data problems?
- Will the results change training, products, or scientific workflows?

This is more than gathering a group to write questions. The designer must understand the task domain, model behavior, measurement error, data contamination, validation mechanisms, and research incentives.

From this perspective, benchmark design resembles measurement theory in science.

Science advances through explanations, but it also advances through new ways of measuring. Telescopes, microscopes, weather observation networks, standardized trials, shared datasets, and reproducible protocols all change which questions can be studied.

AI benchmarks can play a similar role, but only if they measure real objects instead of creating a leaderboard game.

## "People who frame questions will become more important," but the idea should not be romanticized

In the original conversation, I said that research would increasingly center on framing questions and that benchmark projects would gather people who could frame them.

I still agree with that direction, subject to important conditions.

Framing a question does not create value by itself. Someone can keep asking grand, vague, unfalsifiable questions without bearing the cost of solving them.

A high-value question must meet at least three conditions:

1. **It points to a real constraint.** Its purpose is not to embarrass a model, but to reveal a bottleneck in science, engineering, or decision-making.
2. **It can be operationalized.** It can be converted into tasks, data, validation methods, and error analysis.
3. **It can change resource allocation.** The results affect model training, system design, research directions, or product decisions.

The scarce skill will be defining a problem precisely enough to drive action. Asking questions alone will not be enough.

Defining a problem at that level requires decisions about:

- where the boundaries lie;
- which variables need to be controlled;
- what evidence could overturn the conclusion;
- how to avoid rewarding cheating;
- how to make different systems accept the same comparison;
- which results deserve another round of resources.

## Why pre-training experience looks more substantial

The strongest part of my good bro's argument is that firsthand pre-training experience is usually tied to compute, systems, data, and training stability.

This experience is difficult to copy in full from papers. Much of the knowledge lives in logs, failed runs, infrastructure, the order of tuning steps, and team collaboration. Companies can also map these capabilities to jobs more directly:

- training throughput;
- distributed systems;
- data quality;
- loss stability;
- scaling;
- model architecture;
- cost and performance.

By comparison, benchmark work is easy to misread as "writing questions, calling APIs, and making tables."

From the perspective of the job market, pre-training experience therefore has a more direct pricing channel.

That does not mean benchmarks lack value. It means benchmark researchers must turn their capabilities into verifiable assets instead of relying only on paper titles.

For example:

- build evaluation infrastructure that multiple teams continue to use;
- discover and demonstrate systematic failure modes in mainstream models;
- design diagnostic sets that guide training data or post-training;
- establish comparison systems between human experts and models;
- convert evaluation results into product decisions or research directions;
- develop data and communities that can be maintained over time.

Once a benchmark enters the training loop, it participates in improving the model as well as evaluating it.

## Benchmarks, startups, and signal production

My good bro from Northeast China at CMU argued that some teams collaboratively build a benchmark, publish a high-impact paper, and then use it to demonstrate the team's potential to investors.

An early-stage startup has no revenue, customers, or long-term product data, so the team has to produce signals. Papers, leaderboards, open-source projects, benchmarks, communities, and collaboration networks can all serve as signals.

Its value depends on whether the signal corresponds to a real capability.

A benchmark can have three properties at once:

- a research tool;
- marketing material;
- a tool for organizing a team.

A benchmark with a promotional function creates lasting value only when it leaves an asset that continues to accumulate afterward.

If the project ends with only a paper and a list of authors, then my good bro's description, "crowdfunding a paper," may be correct.

If the project leaves a continuously updated task system, real users, an expert network, training feedback, and datasets that improve through continued use, then the benchmark may become an entry point to a company's infrastructure.

I now judge such projects with a more direct question:

> After interest in the paper fades, who will still need to use it?

If there is no clear answer, the project's value may come mainly from its short-term signal.

## My conclusion

I would not place benchmarks and pre-training in a simple hierarchy of contempt.

They address problems at different levels:

- pre-training determines how a model acquires capabilities;
- post-training determines how a model behaves, aligns, and completes tasks;
- benchmarks determine whether we know which capabilities the model acquired and where failures occur.

All three can become infrastructure, and all three can become superficial engineering.

Low-quality pre-training can amount to burning compute. Low-quality post-training can amount to chasing a reward model. A low-quality benchmark can amount to manufacturing a ranking.

The questions that matter are:

1. Does it address a real bottleneck?
2. Does it produce knowledge or assets that others cannot easily replace?
3. Does it enter a later loop of decisions and improvements?
4. Does anyone still use it after attention fades?
5. Do the participants acquire transferable firsthand capabilities?

I still believe that defining problems and measurement standards will become increasingly important.

But that path does not acquire value automatically through the phrase "framing questions." Benchmark researchers have to prove that they are not manufacturing more questions. They are allowing a field to see itself clearly for the first time.
