---
title: "ResearchSkills.ai"
date: 2026-09-29
permalink: /posts/2026/09/project-researchskills-ai/
tags:
  - media
  - project
---

[ResearchSkills.ai](https://researchskills.ai/) is a directory for reusable AI skills built for research workflows. It helps researchers find and share tools for literature work, analysis, writing, and other parts of the research process.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

The most useful things a senior researcher knows rarely make it into a paper. Which instrument drifts after lunch. Which solver setting looks harmless and quietly ruins the run. Which result in a famous paper nobody has managed to reproduce. A language model trained on published text has never seen any of this, because it was never published.

ResearchSkills is an attempt to write that knowledge down in a form AI agents can load. The code and the collection live in the [ResearchSkills repository](https://github.com/ktwu01/ResearchSkills), under the ScienceIntelligence organization.

## What a skill is

A skill is a plain markdown file that tools like Claude Code and Codex can read when they need it. Each one captures a piece of expert know-how and says when it applies.

The collection sorts skills by the kind of memory they hold, borrowing the categories from cognitive science:

- **Procedural.** IF-THEN rules for getting unstuck. Subtypes cover a tie between options, a step that changes nothing, a constraint that fails, and an operator that errors.
- **Semantic.** Facts language models lack. Subtypes cover frontier results too new to be in training data, non-public knowledge, and corrections to things models commonly get wrong.
- **Episodic.** Concrete stories from real research: a failure, an adaptation, an anomaly someone noticed.

The split matters because each kind fails differently. A procedural skill is wrong when the rule fires in the wrong situation. A semantic skill goes stale. An episodic skill is only useful if the agent recognizes that its own situation resembles the story.

## Scope

Skills are organized into 8 domains and 155 subcategories that follow the arXiv taxonomy. Physics has the most subcategories at 51, then computer science with 40 and mathematics with 32, followed by quantitative biology, quantitative finance, statistics, electrical engineering, and economics. Every domain is open for expert reviewers, who can promote a skill from draft to reviewed.

## How skills get in

There are three routes.

1. **Auto-extract.** Install the `@scienceintelligence/researchskills-extract` package and run its slash command inside Claude Code or Codex. It reads a research conversation, proposes skills, and asks for consent before anything leaves your machine. A browser page lets you review each one.
2. **Web prompt.** Paste a one-click prompt into ChatGPT, Claude, or Gemini, then submit the result.
3. **Manual.** Write a skill by hand following the submission guide.

Everything is licensed CC BY 4.0, so contributors get credit and anyone can reuse the work.

## What I worry about

The repository's own README carries a warning I agree with: applying a skill can trigger broad edits and heavy token use. A skill is an instruction to an agent, and an instruction written for one lab's setup can do damage in another. That is why the reviewed status matters more than the raw count. A thousand unreviewed skills are a thousand ways to push an agent in a confident wrong direction.

The second worry is incentives. Researchers give tacit knowledge away when it costs little and earns credit. Auto-extraction lowers the cost. Credit is still an open problem, because no hiring committee counts skill contributions yet.

The knowledge that never made it into a paper is the knowledge an agent most needs.

Explore [ResearchSkills.ai](https://researchskills.ai/).
