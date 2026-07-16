---
title: 'Is Contributing on GitHub Like Donating Sperm?'
date: 2026-07-16
permalink: /posts/2026/07/is-contributing-on-github-like-donating-sperm/
tags:
  - open-source
  - GitHub
  - collaboration
  - ideas
  - reflection
---

Here is an inappropriate analogy that nevertheless captures something real about open-source work:

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

> Going around GitHub opening issues and pull requests is surprisingly like donating sperm—and not much like donating eggs.

The analogy is deliberately provocative. It is not a claim about gender or the value of either form of donation. It describes an asymmetry in **replication cost, contribution volume, and selection**.

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

A useful issue demonstrates that the problem exists, defines its scope, and distinguishes it from known cases. A useful pull request fits the architecture, passes tests, explains its tradeoffs, and reduces rather than exports maintenance burden.

High volume produces exposure. It does not by itself produce impact.

## From spreading genes to raising offspring

The analogy is funniest—and most accurate—at the lowest-commitment edge of open source: opening many issues, proposing many ideas, and sending small patches into unfamiliar projects.

It becomes less accurate as responsibility increases.

Submitting a thought is propagation. Getting it reviewed is selection. Getting it merged is inheritance. Maintaining it through future releases is something else: parenting.

That is the dividing line between merely leaving traces across GitHub and building something with other people. The strongest open-source contributors do not only distribute their ideas widely. They stay long enough to help those ideas survive contact with reality.

**Related post:**
- [中文版：在 GitHub 到处提 Issue 和 PR，为什么像“捐精”而不像“捐卵”]({{ site.baseurl }}/zh/posts/2026/07/github-contributions-sperm-vs-egg-donation/)
