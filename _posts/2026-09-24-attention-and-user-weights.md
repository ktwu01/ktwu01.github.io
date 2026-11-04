---
title: "Why Does AI Forget Your Other Requests When You Just Say \"Make It Look Nicer\"?"
date: 2026-09-24
permalink: /posts/2026/09/attention-and-user-weights/
tags:
  - AI
  - LLM
  - attention
  - instruction-following
---

Have you ever run into this while using AI?

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

You give it several requirements: a polite tone, accurate content, a nice layout, a bit more spacing. It hands over a first draft. You think it's nearly there and only want to adjust the look, so you add one line:

"Can you make it look a bit nicer?"

The next draft changes visibly: a bolder title, more white space, less text. But look closely and, to make the page cleaner, a paragraph of explanation is gone, and a qualification that needed to stay has been squeezed into a slogan.

You quickly say, "Keep the accuracy, though."

It revises again. This time the explanation is back, and the page is crammed with text again.

You start correcting back and forth between two directions. You think you are fine-tuning, yet the AI seems to reinterpret the whole task every time.

**You said "turn this one up a little," and the result looks like "now only this one matters."**

That is the question here: when a task contains A, B, and C at once, why does stressing B make A and C fall apart?

A natural idea is to hand the AI a set of weights directly.

Politeness 20%, accuracy 30%, looks 40%, spacing 10%. All requirements stay; only their priorities change. Like faders on a mixing desk: raising the vocals should not mute the drums and guitar along the way.

Besides, large language models already contain a mechanism called attention. It already allocates weights. So why not give these faders to the user?

To answer that, we first need to be clear about what attention actually assigns weight to.

When we read a passage, we keep linking earlier and later information. Seeing "please change the title of the second draft," we need to find the second draft, identify the title, and then understand how to change it.

A language model also needs to link pieces of text. Attention is one mechanism it uses for this computation: when processing the current position, it reads information from different earlier positions according to learned matching patterns, then combines that information. [1]

You can think of it as "writing while flipping through reference material": at different points you consult different material to different degrees. But this is only an analogy. There is no person inside the model turning pages.

Written as math, the process splits into two steps. Step one computes how much to consult each position:

$$
a_{ij}=
\frac{\exp\!\left(q_i^\top k_j/\sqrt{d_k}\right)}
{\sum_{m\in S_i}\exp\!\left(q_i^\top k_m/\sqrt{d_k}\right)}
$$

Don't let the symbols scare you. $$i$$ is the position being processed, and $$j$$ is a position it can consult. $$q_i$$ is called the Query and $$k_j$$ the Key. Both are lists of numbers, and the dot product $$q_i^\top k_j$$ gives a match score. Roughly, read it as "how well the information needed right now matches the clue this position offers," though the matching itself is learned in training.

$$d_k$$ is the dimension of these vectors, and dividing by its square root rescales the scores. $$S_i$$ is the set of positions that may be read. In standard causal attention, text that hasn't appeared yet cannot be read. Finally, $$\exp$$ is the exponential: it turns each position's score into a positive number, and dividing by the sum of those numbers gives proportions. This whole conversion is called **softmax**.

So $$a_{ij}$$ reads as: "while processing position $$i$$, the share of reading given to position $$j$$."

Step two combines information by those proportions:

$$
z_i=\sum_{j\in S_i}a_{ij}v_j
$$

$$v_j$$ is called the Value, the information vector carried by position $$j$$, and $$\sum$$ means adding the terms up. If three positions get 20%, 30%, and 50%, this step is "the first piece times 0.2, plus the second times 0.3, plus the third times 0.5." The resulting $$z_i$$ goes on to later computation.

**At this point, the formula has selected and combined information. It has not yet computed whether the answer is accurate or polite.**

The problem sits exactly between "how much to consult" and "what to prioritize."

**Consulting a sentence more does not automatically mean carrying it out better.**

Suppose you have someone reread "please stay accurate" over and over. They really do spend a lot of time on that sentence, but if they don't check the numbers, understand the qualifications, and review what was cut, they may still get it wrong.

Models are the same. Giving the word "accurate" more attention does not conjure up the ability to check facts, nor does it automatically set up a check for "does deleting this sentence change the meaning?"

Also, a model has no single "master attention switch" that splits 100% among politeness, accuracy, looks, and spacing. It reads information again and again, across many layers and many positions. These internal weights describe relations between text representations. The user's weights describe how the result should trade things off.

Training can link the two, but they cannot simply be equated.

Softmax also reveals a kind of competition worth noting. Suppose an attention head at some position consults only three places, and their match scores are all 0, so each gets about a third. If only the second score rises from 0 to 3, the shares become:

| Match scores | Share of place 1 | Share of place 2 | Share of place 3 |
| --- | ---: | ---: | ---: |
| $$(0,0,0)$$ | 33.3% | 33.3% | 33.3% |
| $$(0,3,0)$$ | 4.5% | 90.9% | 4.5% |

This example plugs straight into the formula. The second place's exponential goes from 1 to about 20.1, so it takes nine-tenths of a total of about 22.1. The other positions are not deleted, but their relative shares drop sharply.

In shape, this looks a lot like "stress one item and the others fade." But the three places in the table are token positions, not the goals of politeness, accuracy, and looks, and this local computation does not stand for the whole model.

This also means "it ignored my other requests, so attention must have been stolen" is still only a guess. From the final answer alone, we cannot see which step failed.

So why can't AI remember the requirements we already agreed on, the way a collaborator would?

To understand this, picture two ways of making a revision.

In one, after hearing "make it nicer," you directly hand over a version that looks nicer.

In the other, you first determine which requirements still apply, then change the look, and finally check that the numbers, meaning, tone, and spacing still meet the requirements.

As users we naturally expect the second process. But a model that can produce a revision does not automatically come with that whole checking procedure.

Large language models usually generate text one small piece at a time. They can plan, reason, and check along the way, but those behaviors have to be trained in or arranged by a surrounding system. Producing an answer that looks like it meets the latest request does not guarantee that every earlier requirement was checked off.

The generation process can be written as:

$$
p_\theta(y\mid x)
=\prod_{t=1}^{T}p_\theta(y_t\mid x,y_{<t})
$$

$$x$$ is the context the model actually receives, $$y$$ is the full answer, and $$\theta$$ are the trained model parameters. $$y_t$$ is the $$t$$-th token, a unit of text that is not necessarily exactly one character or one word, and $$y_{<t}$$ is the part generated so far.

The bar $$\mid$$ means "given these conditions," and $$\prod$$ means multiply together. The whole line says: the probability of an answer is the product of the probabilities of generating each token, given the context at that step.

The formula explains why what has already been written shapes what comes next. It does not prove that models cannot plan, and it carries no guarantee that "all requirements are met." For instance, nothing in the formula is a built-in check that confirms the opening qualification is still there at the end.

Post-training matters here. Think of it as further training a model that has already learned the patterns of language, through demonstrations, feedback, and rewards, so that it gets better at following instructions. Work such as InstructGPT showed how this training improves instruction following. [2]

But what training rewards shapes what the model learns.

Imagine this: a user says "make it nicer," the model cuts a lot of text, and the rater finds the page cleaner and gives a high score. If the rating never checked whether the deleted content affected accuracy, the model might learn a problematic editing habit: make the change obvious at a glance, without equally learning to protect earlier requirements.

This explanation needs experiments to test it, and it does not let us assert that any particular model was trained this way. It suggests that training should check what improved and also what got worse.

So when a user has been clear and the AI still doesn't comply, the system should of course improve. But before fixing, find out: did it fail to use that requirement, or did it understand and fail to deliver? Did the model break it, or did the application never pass the earlier requirement along?

Calling all of these "didn't listen" describes the experience well enough, but does not locate the cause.

Back to the four faders.

What if we write "politeness 20%, accuracy 30%, looks 40%, spacing 10%" directly? Would that help? Maybe. The model can infer relative priorities from the numbers.

But **between writing down a ratio and getting results that reliably follow it, there is a stretch of engineering.**

To make those four percentages a clear comparison rule, we can write:

$$
U_w(y)=
0.2r_{\text{polite}}(y)
+0.3r_{\text{accurate}}(y)
+0.4r_{\text{looks}}(y)
+0.1r_{\text{spacing}}(y)
$$

Here $$y$$ is a candidate piece of work, $$r$$ is the score on one aspect, and $$U_w$$ is the total computed with weights $$w$$. Treat it as a scoring sheet: multiply each score by its weight and add them up.

Note that the 0.4 here multiplies "the whole work's looks score." The proportions in attention earlier multiplied "the information vector at a position." **Both formulas weight things, but they weight different objects and do different jobs.**

If the system first generates a set of candidates $$\mathcal{Y}$$ and then runs

$$
y^*=\arg\max_{y\in\mathcal{Y}}U_w(y),
$$

that means "among these candidates, pick the one with the highest total." This turns weighting into an operation. But it can only pick from existing candidates, and it depends on the scores being reliable. Writing the same formula into a prompt does not guarantee an ordinary model has actually carried out the whole procedure.

Take "more spacing." If the task is web layout, we can check the specific style values. "Look a bit nicer" is not so direct: cutting text, changing colors, unifying fonts can all improve the look, and can all bring changes the user didn't want.

A trustworthy fader needs to know what it controls, and how the result actually changed once it was pushed up. Otherwise the 40% on the interface is just a number that looks precise.

The scale of the scores must be handled too. If looks are scored 0–100 and accuracy 0–1, then looks can contribute up to 40 points and accuracy only 0.3. That is clearly not the tradeoff a user expects from "40% versus 30%." Only after putting the scores on one scale, and calibrating what each score means with examples, do the percentages mean anything.

One more easily missed point: even when the weighting is done right, it does not guarantee that no item gets worse.

Say one of two page versions explains more fully and the other better matches the preferred look. Raise the weight on looks, and the system may switch from the first to the second. The other requirements were not deleted. They were sacrificed in the total-score comparison.

An example with only accuracy and looks shows how to compute this switch. The scores below are made up for illustration, all between 0 and 1:

| Page | Accuracy score | Looks score |
| --- | ---: | ---: |
| A | 0.95 | 0.55 |
| B | 0.75 | 0.85 |

Let the looks weight be $$b$$ and the accuracy weight $$1-b$$. The totals are:

$$
U(A)=0.95(1-b)+0.55b=0.95-0.40b
$$

$$
U(B)=0.75(1-b)+0.85b=0.75+0.10b
$$

Setting the two totals equal gives $$b=0.4$$. Below that value A scores higher; above it B scores higher.

So moving the looks weight from 39% to 41% can make the system switch answers, with accuracy dropping from 0.95 to 0.75. Even though no other weight went to zero, the result can change abruptly. **A small change in weights does not guarantee only a small change in output.**

So the "don't forget my other requests" we started with actually holds two expectations. Sometimes we allow tradeoffs and only want them to follow our preferences. Other times we only want to change the look and never authorized cutting content.

**"Care more about looks" and "you may drop information for the sake of looks" must not be treated by default as the same thing.**

A system that can collaborate with users has to judge the scope of each edit from context. If the user explicitly says "only change the spacing," the text should stay. Only when the user says "content can be trimmed, visuals come first" is there room for a different kind of edit.

This distinction can be written into the math as well. For example, if the user requires the accuracy score to reach at least some level $$\tau$$, the system can add a constraint when choosing among candidates:

$$
\max_{y\in\mathcal{Y}}U_w(y)
\quad\text{subject to}\quad
r_{\text{accurate}}(y)\ge\tau
$$

$$\tau$$ is the floor that must not be broken. Set it to 0.9, and B above cannot be chosen, however nice it looks. If no candidate meets the requirement, the system has to keep searching or explain the conflict. This guarantee still depends on the scorer scoring correctly.

For "only change the spacing," we can also directly check whether the old and new text are identical, without turning it into a subjective score. Weights govern the allowed tradeoffs; constraints set the bounds of what is allowed.

This does not require the user to rewrite a contract every round. Requirements already stated, and still valid, should simply carry forward.

Can such a control mechanism be built? Existing research is trying.

One path intervenes directly in attention. PASTA studied how to make a model weigh user-specified text more heavily at inference time. Another path trains models specifically to adjust outputs according to multiple preferences. Rewards-in-Context belongs to this direction. [3][4]

This research shows that "the user marks what matters, and the model changes its behavior accordingly" can be done. But strengthening the effect of a passage is still some distance from making four goals change as predictably as faders on a mixing desk.

The scenario at the start can also be solved through system design: have the AI keep a running list of current requirements, update only the relevant part when an edit comes in, and afterward check that the other requirements are still met.

If the user says "make it nicer," the system should treat it as an update to the current task. Accuracy, politeness, and spacing still stand, unless the user withdraws them or the new request truly conflicts with them.

The checks must also land on the result: were words or numbers changed, did a qualification disappear, did the spacing change. For looks and tone, use predefined criteria or user feedback. The model saying "I have balanced all requirements" does not count as acceptance.

To learn which approach works, run a very direct experiment: give the same task several requirements, let the AI complete it, then adjust only one of them. Record whether that item improved, and also whether the others regressed without permission. Then compare plain conversation, extra checking, and targeted training.

That takes us from "is its attention not enough?" to an observable question: what exactly did it improve, and what did it break?

Back to the beginning. When a user says "can you make it look a bit nicer," the "a bit" usually already carries an expectation of collaboration: we are still revising the same piece of work, and what we agreed on before still counts.

That continuity is exactly what AI needs to learn.

**When you push one fader up, it should know the other faders are still where you left them.**

Further reading:

1. [Attention Is All You Need](https://arxiv.org/abs/1706.03762): the computation behind the Transformer and attention.
2. [Training language models to follow instructions with human feedback](https://arxiv.org/abs/2203.02155): how demonstrations and human feedback improve instruction following.
3. [Tell Your Model Where to Attend: Post-hoc Attention Steering for LLMs](https://arxiv.org/abs/2311.02262): strengthening the effect of specified text through attention intervention.
4. [Rewards-in-Context: Multi-objective Alignment of Foundation Models with Dynamic Preference Adjustment](https://arxiv.org/abs/2402.10207): training that supports adjusting multi-objective preferences.
