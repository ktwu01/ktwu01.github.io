---
title: 'Why Filing Issues and PRs All Over GitHub Is Like "Donating Sperm" and Not Like "Donating Eggs"'
date: 2026-07-16
permalink: /posts/2026/07/github-contributions-sperm-vs-egg-donation/
tags:
  - open-source
  - GitHub
  - collaboration
  - ideas
  - reflection
---

Let me offer a comparison that's a bit inappropriate but does capture a real structure of open-source collaboration:

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

> Filing issues and PRs all over GitHub is a lot like "donating sperm," and not much like "donating eggs."

This metaphor is deliberately provocative. It isn't about gender, and it doesn't judge the value of the two kinds of donation. It describes an asymmetry in **cost of replication, volume of contribution, and the power to filter**.

## Why the metaphor holds

An issue or PR carries a small slice of its author's information: a problem definition, design preferences, a code pattern, and a judgment about how a system should run. That slice of information enters someone else's project and comes into contact with other people's thoughts.

The two therefore show some similar structures:

- **Contributors can contribute in large volume.** One person can file issues or patches to many repositories.
- **The marginal cost of replication is low.** Once an idea takes shape, it can be modified, copied, and aimed at other contexts.
- **The process is open.** Contributors usually don't need an employment contract, an institutional affiliation, or a pre-existing relationship with the maintainer.
- **The receiving side holds the power to filter.** The maintainer decides whether to reject, modify, merge, or simply not respond.
- **Most contributions don't spread.** Many issues get no follow-up, and many PRs are never merged; only a few enter a project's history and influence future versions.
- **Contributors enter a larger "gene pool."** Review recombines individual judgment with the repository's architecture, conventions, and accumulated knowledge.
- **Attribution is kept, but control diminishes.** Git records the author, but the maintainer can modify, refactor, revert, or even eventually replace the contribution.

This process also brings a direct kind of pleasure: you spot a problem, shape an intervention, send it out into the world, and wait to see whether it connects with some project. If the connection succeeds, your thought becomes part of a larger system.

## Why it's more like "donating sperm" than "donating eggs"

The relevant distinction here comes from cost structure, not moral judgment.

Egg donation faces limited supply, medical intervention, recovery time, strict screening, and physical cost. Sperm, meanwhile, can be produced and donated in greater quantities and at much lower marginal cost.

Most GitHub contributions follow the latter cost structure. Ideas and text can be copied, issues can be filed quickly, and a single patch can sometimes migrate to multiple repositories. The platform lets contributors spread at scale with little formal restriction.

This doesn't mean contributions are free of cost. Understanding a codebase, reproducing a bug, designing a compatible solution, writing tests, and responding to review can consume days or even months. So this metaphor fits casually filed issues better than deep engineering contributions.

## Issues and PRs aren't the same kind of contribution

If we stop lumping all GitHub activity together, the metaphor gains explanatory power.

| GitHub behavior | What is actually contributed |
|---|---|
| Filing an issue | A problem, observation, or need |
| Writing a proposal | A problem model and possible routes |
| Submitting a PR | An implementation requesting entry into the codebase |
| Code review | Filtering, correction, and recombination |
| Merge | Entering a project's lineage |
| Sustained maintenance | Taking responsibility for whether a contribution survives |
| Fork | Forming a new lineage under different selection pressures |
| Revert | Removing a trait that failed to fit the environment |

An issue is closer to releasing an idea into a group. A PR carries more: it wraps the idea in an implementation that must interact with an existing system.

But even a serious PR can't be described purely as "donating." When an author understands the repository, negotiates the design, revises the patch, adds tests, and keeps maintaining after the merge, the two sides have entered a co-development relationship.

## Where the metaphor breaks down

Software isn't biology.

First, code allows exact replication. Biological inheritance can't let a single donor send the same complete contribution to thousands of environments at nearly zero cost.

Second, GitHub contributions can be continuously edited. An author can revise a patch in response to review, split it into smaller changes, withdraw it, or return months later with a new plan.

Third, projects can reverse merges. A merge can be reverted, a repository can be forked, an implementation can be replaced, while the original commit stays in history.

Fourth, maintainers don't only filter. They also explain local constraints, adjust the direction of work, fill in missing information, and sometimes co-build the final solution with the contributor. Receiving a project changes the contribution first, and only then does the contribution change the project.

Finally, a merge isn't success. A PR that nobody uses, creates maintenance cost, or gets deleted in the next version hasn't accomplished much. The stricter test is whether the contribution kept solving a problem over time.

## An uncomfortable conclusion: the more abundant contributions are, the more filtering matters

When contributions become cheap, attention becomes the scarce resource.

Open-source platforms let ideas spread at scale. The same mechanism also manufactures vague feature requests, duplicate issues, one-off patches, AI-generated PRs in bulk, and "contributions" that shift the cost of verification onto maintainers.

So the core question can no longer be:

> How many repositories have I contributed to?

It should be:

> How much uncertainty did my contributions remove for the project's leader?

A useful issue needs to demonstrate the problem exists, define its scope, and distinguish it from what's already known. A useful PR needs to fit the architecture, pass the tests, explain its trade-offs, and reduce maintenance burden rather than hand it to someone else.

Mass propagation can raise visibility, but it doesn't automatically create impact.

## From spreading genes to co-parenting

This metaphor is most accurate, and funniest, at the lowest-commitment end of open-source collaboration: filing issues everywhere, expressing ideas everywhere, and sending small patches to unfamiliar projects.

As responsibility increases, it becomes steadily less accurate.

Sending an idea is propagation, accepting review is filtering, getting merged is inheritance, and maintaining across multiple versions is something else entirely: co-parenting.

This line separates two behaviors: leaving traces all over GitHub, and genuinely building systems together with other people. The strongest open-source contributors don't just spread ideas widely. They also stay, and help those ideas face the test of reality.