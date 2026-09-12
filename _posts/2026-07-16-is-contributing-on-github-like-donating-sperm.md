---
title: 'Contributing on GitHub Is Sperm Donation'
date: 2026-07-16
permalink: /posts/2026/07/is-contributing-on-github-like-donating-sperm/
tags:
  - open-source
  - GitHub
  - collaboration
  - ideas
  - reflection
---

Going around GitHub opening issues and pull requests is sperm donation. The same mechanism, running as-is.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

The asymmetry sits in three places: **replication cost, contribution volume, and who does the selecting.** Nothing here is about gender, or about which form of donation is more admirable. Open source has spent twenty years covering that asymmetry with words like collaboration, community, and building together. The words do not cover it.

## Why the analogy works

An issue or pull request carries a small piece of its author's information: a problem definition, a design preference, a coding pattern, a theory about how a system should work. That information enters someone else's project and encounters other people's ideas.

Several structural similarities follow.

- **The contributor can contribute at scale.** One person can open issues or submit patches to many repositories.
- **The marginal cost of replication is low.** Once an idea has been articulated, it can be adapted and proposed elsewhere.
- **The process is open.** A contributor often needs no employment contract, institutional affiliation, or prior relationship with the maintainers.
- **The recipient selects.** Maintainers decide whether to reject, revise, merge, or ignore the contribution.
- **Most contributions do not propagate.** Many issues receive no action. Many pull requests never merge. A smaller number enter the project's history and affect later versions.
- **The contributor exchanges information with a larger gene pool.** Review combines the contributor's assumptions with the repository's architecture, standards, and accumulated knowledge.
- **Attribution survives while control weakens.** Git records authorship, but maintainers may modify, refactor, revert, or eventually replace the contribution.

There is also pleasure in the process. You notice a problem, formulate an intervention, send it into the world, and wait to see whether it connects. When it does, your thought becomes part of a system larger than yourself.

## Why it resembles sperm donation more than egg donation

The relevant distinction is economic and biological, not moral.

Egg donation involves a limited supply, medical intervention, recovery time, screening, and substantial physical cost. Sperm can be produced and donated in much greater volume at much lower marginal cost.

Most GitHub contributions have the second cost structure. Ideas and text can be copied. Issues can be filed quickly. A patch can sometimes be adapted across repositories. The platform permits high-volume contribution with few formal barriers.

That does not mean the contribution has no cost. Understanding a codebase, reproducing a bug, designing a compatible fix, writing tests, and responding to review can consume days or months. The analogy fits casual issue creation much better than deep engineering work.

## An issue and a pull request are not the same contribution

The metaphor becomes more useful when we stop grouping all GitHub activity together.

| GitHub action | What is actually contributed |
|---|---|
| Opening an issue | A problem, observation, or request |
| Writing a proposal | A model of the problem and a possible direction |
| Submitting a pull request | An implementation that asks to enter the codebase |
| Reviewing code | Selection, correction, and recombination |
| Merging | Admission into the project's lineage |
| Maintaining | Responsibility for whether the contribution survives |
| Forking | A new lineage with different selection pressures |
| Reverting | Removal of a trait that failed in its environment |

An issue is close to releasing an idea into a population. A pull request carries more: it packages the idea as an artifact that must interact with an existing organism.

But a serious pull request is still not well described as donation alone. Once the author studies the repository, negotiates design choices, revises the patch, adds tests, and remains available after merge, the relationship becomes cooperative development.

## Where the analogy breaks

Software is not biology.

First, code permits exact copying. Biological inheritance does not allow one donor to send the same complete contribution into thousands of environments at effectively zero cost.

Second, GitHub contributions remain editable. Authors can revise a patch after review, split it into smaller changes, withdraw it, or return months later with a better design.

Third, projects can reverse incorporation. A merge can be reverted. A repository can be forked. An implementation can be replaced while its commit remains in history.

Fourth, maintainers do more than select. They explain local constraints, redirect the work, supply missing context, and sometimes co-author the final solution. The receiving project changes the contribution before the contribution changes the project.

Finally, success is not reproduction. A merged pull request that nobody uses, that creates maintenance cost, or that is removed in the next release has achieved little. The stronger test is whether the contribution continues to solve a problem.

## The uncomfortable lesson: abundance increases the importance of selection

When contribution becomes cheap, attention becomes scarce.

Open-source platforms make it possible to distribute ideas at scale. The same mechanism also produces vague feature requests, duplicate issues, drive-by patches, AI-generated pull requests, and work that transfers verification costs to maintainers.

This changes the central question. It is no longer:

> How many repositories did I contribute to?

It becomes:

> How much uncertainty did my contribution remove for the people responsible for the project?

A useful issue demonstrates that the problem exists, defines its scope, and distinguishes it from known cases.

High volume produces exposure. It does not by itself produce impact.

That much I believed when I wrote this post. Then I started maintaining projects myself, and found out what the sentence actually costs.

## A note added later: when I became the egg

When I wrote this post, I was standing on the contributor's side. What I thought about was how to send my own ideas out, into as many projects as possible.

Then I started maintaining a few open-source projects of my own, and the view flipped. Now I am the one receiving the pull requests.

It is a strange experience. I used to think about how to get other people to accept my work. Now I think about what is worth letting in.

If opening pull requests all over GitHub is cyber sperm donation, then the maintainer is the egg. More precisely, the maintainer is the zona pellucida, the layer around it. Its job is not to wait for whoever turns up. Its job is to keep almost everyone out.

The process is not gentle. A single ejaculate is on the order of hundreds of millions of sperm; the number that reach the egg is on the order of hundreds; the number that completes fertilization is normally one. And the egg is not passive about it. The moment a sperm fuses with the egg membrane, a calcium wave inside the egg triggers the cortical granules to dump their contents. That shuts the door in two stages: the membrane stops accepting further fusion within minutes, and enzymes released into the surrounding space chemically modify the zona over the following half hour to few hours, until it can no longer be bound or penetrated at all. None of this machinery exists to let more sperm in. It exists to guarantee that **only one** does, because two ruins the embryo.

That is the maintainer's job, described honestly. Open source does not like describing it that way, because it does not sound welcoming to newcomers.

## Most pull requests should be rejected, and that is not unkind

The last couple of years brought a new category of arrival: the AI-generated pull request.

Someone points a model at a repository, asks it to find a few "improvements," and lets it submit. The title is well formed. The description is complete. The diff even looks clean. But open it up and you usually find: a function nobody calls, renamed; a block of already clear code, buried in comments; the README's English rewritten into different English that is equally correct and no better; or a fix for a bug that does not exist.

My prior is explicit: **assume this class of pull request is bad until it proves otherwise.**

Someone will call that prejudice against AI-assisted contributors. It is not. The prior is not on "you used AI." It is on "you did not verify." Someone who writes code with a model, runs the tests, can explain why the change is shaped that way, and will come back when it breaks: that pull request gets merged, and it is often better than the handwritten alternative. AI genuinely lowers the cost of good contributions too. What I am blocking is not the model. It is the move where generation cost goes to zero and verification cost gets handed entirely to me.

That move got very cheap very recently. When the cost of submitting a pull request falls to nearly zero, submission volume rises toward infinity, and the cost of review does not fall at all. A maintainer's attention is the one thing in this system that never got cheaper. It is a scarce resource and it has to be spent like one.

So the default stance is: **the burden of proof is yours, not mine.**

To get in, a pull request has to convince me of three things:

- **The problem is real.** Reproduction steps, or an issue, or an explanation of who actually hits this. "I think this is nicer" does not qualify.
- **The solution belongs to this project.** No parallel structure, no new dependency to save three lines, no rewriting my architecture into the one you are used to.
- **It does not hand me its maintenance cost.** Tests, documentation, edge cases considered. When it breaks later, I should not have to read it from scratch to find out what it was for.

Missing one, I ask for it. Missing all three, I close it, and I do not feel bad.

## A joke: I have been on both sides

I have a patch in `git/git`. That Git. The one everybody uses, the one Linus wrote. Junio C Hamano merged it, my name is on the commit as author, and [every `git clone` in the world now carries it](https://github.com/git/git/commit/0bf506efd40251ebdc9ed829d8bb90d879d2c7aa). It was a one-line fix: the `*.pl` line in `.gitattributes` said `eof=lf` where it should have said `eol=lf`.

The same person then opened several pull requests in a row against kimi-cli and had them rejected by the maintainer, one after another.

The difference between those two outcomes is exactly what this post is about.

The patch that landed in Git did not come from browsing the source looking for something to fix. It came from hitting a real CRLF/LF problem in my own blog repository, writing a `.gitattributes` by hand to solve it, and learning the difference between `eol` and `eof` in the process. A day later I recognized the same typo sitting in Git's own file. The problem was real, because I had been the one bitten by it. The fix was one line and touched no architecture. The maintenance cost was zero. All three conditions, met. And before submitting I went and learned that Git does not take GitHub pull requests at all: it runs on a mailing list, you go through GitGitGadget, you sign off your commits.

The rejected ones? I can see now what they were. Cheap to produce, clean on the surface, and built on somebody else's hole. I was doing exactly one thing: distributing.

So that maintainer was right. He was doing his job. He was being the zona pellucida.

And now I sit on the other side making the same call about other people's work. The useful part of that is it becomes very hard to resent being rejected. You know exactly what the person on the other side is doing, because you have done it.

## Saying no is a skill you have to learn

I used to be bad at saying no.

A pull request would come in, and even when it was weak, my first thought was: this person spent time on it, am I being too harsh? Maybe merge it now and clean it up later?

That instinct is wrong, and wrong in a specific way. Once code is merged, its maintenance cost is mine, not the contributor's. The contributor submits and leaves. I keep the thing alive for ten years. A "merge now, fix later" decision trades a one-time rejection cost for a permanent maintenance cost.

The asymmetry is this. Rejecting a pull request costs one uncomfortable conversation, once. Merging a bad one costs permanent technical debt, plus a precedent for everyone after: if that got in, so can this. You pay the first cost once. You pay the second forever.

And "I don't want to hurt them" is a false reason anyway. What hurts people is not rejection. It is being ignored. "We are not going in this direction, and here is why" is far more respectful than silence for three months. Rejecting someone is what you do when you take them seriously: I read your work, I judged it properly, I am telling you the result. Leaving it to rot is what not caring looks like.

So I reject fast now, and I say why.

Going from "how do I get my work out there" to "what is worth letting in" is not just a change of role. It is a change of skill. Distribution runs on volume and nerve. Selection runs on judgment and the ability to say no. The first can be powered by enthusiasm. The second can only be powered by standards. Enthusiasm runs out. Standards do not.

## From spreading genes to raising offspring

The analogy holds best at the lowest-commitment edge of open source: opening many issues, proposing many ideas, and sending small patches into unfamiliar projects.

It starts to break down the moment responsibility enters.

Submitting a thought is propagation. Getting it reviewed is selection. Getting it merged is inheritance. Maintaining it through future releases is something else: parenting.

That is the dividing line between merely leaving traces across GitHub and building something with other people. The strongest open-source contributors do not only distribute their ideas widely. They stay long enough to help those ideas survive contact with reality.

**Related posts:**
- [中文版：在 GitHub 上做贡献，就是赛博捐精]({{ site.baseurl }}/zh/posts/2026/07/is-contributing-on-github-like-donating-sperm/)
- [在 GitHub 到处提 Issue 和 PR，为什么像“捐精”而不像“捐卵”]({{ site.baseurl }}/zh/posts/2026/07/github-contributions-sperm-vs-egg-donation/)
- [I Am Now an Official Git Contributor]({{ site.baseurl }}/posts/2026/06/official-git-contributor/), the full story of that one-line patch.
- [I Sent My First Git Patch to GitGitGadget's Doorstep]({{ site.baseurl }}/posts/2026/06/gitgitgadget-first-pr/), and why Git does not take GitHub pull requests.
