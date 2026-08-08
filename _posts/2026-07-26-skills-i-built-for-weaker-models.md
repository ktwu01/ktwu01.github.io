---
title: 'The Skills I Built for Weaker Models, and Why I Deleted Most of Them'
date: 2026-07-26
permalink: /posts/2026/07/skills-i-built-for-weaker-models/
tags:
  - Claude Code
  - AI Agents
  - Tooling
  - Context Engineering
  - Developer Experience
---

I ran a health check on my Claude Code setup this week and found 174 custom skills, 124 of which I had never invoked once. They were not failures. Most of them were scaffolding I built for a model that needed it, and then kept long after the model stopped needing it.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

A skill, in Claude Code, is a folder with a markdown file that tells the agent how to do a specific task. The name and description of every installed skill sit in the model's context at the start of every session, so the agent knows what it can reach for. The body loads only when the skill is invoked. That design is good: it means a hundred skills cost you a hundred descriptions, not a hundred procedures.

The catch is that descriptions are not free. Mine had grown to roughly 13,800 tokens of listing before I touched anything. Claude Code budgets the skill listing at about one percent of the context window, and past that it truncates and routing degrades. I had gone seven times over. The skills I actually used were getting harder for the agent to find because of the ones I did not.

## What the skills were compensating for

Reading back through the ones I never called, a pattern shows up. They fall into a few groups, and almost every group is a workaround for a specific weakness.

The largest group is procedural decomposition. Skills like `paper-plan`, `research-pipeline`, `experiment-plan`, and `dse-loop` exist to hold a multi-step process in place. Write the outline, then the methods, then the results, then check the figures against the claims. I wrote them because earlier models would start strong and lose the thread by step four. The skill was an external memory for a process the model could not hold on its own.

The second group is output-shape enforcement. `formal-docs-affirmative-prose`, `sci-writing-prose-rules`, `figure-never-annotation-caption`. These encode rules I was tired of restating. Do not hedge. Do not put the caption inside the figure. Do not use marketing language in a methods section. Each one existed because the model would drift back to a generic register unless something held it.

The third group is verification scaffolding: `result-to-claim`, `sci-validation-checklist`, `sci-geoscience-metric-claims`. These force the agent to trace a number in a paper back to the code that computed it. I built them after being burned by plausible-sounding figures whose numbers did not survive checking.

The fourth group is not about capability at all. `dbs-*`, `nature-*`, `ios-*` came in as external skill packs. I installed them, tried one or two, and left the rest. They were never compensating for anything. They were just clutter, and they are the easiest to justify removing.

## The ones that stopped earning their place

Groups one and two are where the interesting change is. Current models plan multi-step work without a checklist telling them the steps, and they hold a register once you tell them the register. When I invoke `paper-plan` today, I am mostly telling the model to do what it was already going to do, in an order I picked eighteen months ago.

That is the cost people miss. A stale skill is not neutral. It is a fixed instruction competing with the model's own judgment, and it wins, because I wrote it as an instruction. If the procedure encoded in the skill is worse than what the model would do unprompted, the skill actively makes the output worse while appearing to add rigor.

Group three did not stop earning its place, and I want to be precise about why. `result-to-claim` is not compensating for weak reasoning. It is compensating for the fact that an agent has no independent access to whether a number is true. It has to go read the code. That is a structural gap, not a capability gap, and no amount of model improvement closes it, because the model cannot verify a claim about my data by thinking harder about it. Those skills stay.

The same logic keeps a few others. `gemini-review` routes an artifact to a different model for critique, which is valuable precisely because it is not the same model grading itself. `wkt` creates a git worktree before implementation work, which is a policy choice about my repo, not a reasoning aid. `atomic-commit` encodes how I want history to look. None of these are scaffolding. They are preferences and structural facts, and a better model does not make them obsolete.

## The test I ended up with

The distinction I landed on is whether a skill compensates for something the model cannot do, or for something it merely could not do yet.

Skills that encode access to the world stay. Reading a file, calling another model, checking a number against its source, following a convention specific to my repository. The model cannot derive any of these by being smarter.

Skills that encode a procedure the model could now infer should go, and the honest way to test that is to delete the skill and do the task without it. If the output is the same, the skill was ceremony. If it degrades, the skill was carrying something real and belongs back.

Two things make this easier than it sounds. Disabling is reversible, so a wrong call costs one settings edit. And usage counters make the first pass mechanical: a skill with zero invocations across more than a thousand sessions is not a judgment call.

## What actually changed

I disabled the 124 unused skills. The listing dropped from roughly 13,800 tokens to about 5,700, and most of what remains is built-in skills and one plugin I had left enabled in a repository where it does not apply.

I also moved a long block of project-specific review criteria out of an always-loaded instructions file and into a skill that loads only when invoked. That is the same principle from the other direction: the content was worth keeping and did not need to be resident in every session.

The part worth generalizing is not the token count. It is that I had accumulated a year of workarounds and never revisited whether the thing being worked around was still there. Tooling built against a model's limitations should be re-examined when the limitations move, and the counters that tell you which tools you actually reach for are sitting in a config file the whole time.
