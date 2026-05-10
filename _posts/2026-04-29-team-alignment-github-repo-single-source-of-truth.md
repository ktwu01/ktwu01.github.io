---
title: 'One Repo to Rule Them All, Why GitHub Is the Only Honest Place to Align a Team'
date: 2026-04-29
permalink: /posts/2026/04/team-alignment-github-repo-single-source-of-truth/
tags:
  - team
  - alignment
  - github
  - engineering
  - workflow
  - knowledge-management
---

A team has too many things, too many open questions, too many half-decisions floating across Slack threads and meeting notes, and the only way I have found to keep that chaos from turning into quiet decay is to force every piece of valuable knowledge into one place, the GitHub repo, and treat everywhere else as a temporary scratchpad.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

I have watched the same failure mode show up in lab groups, in startup teams, in volunteer organizations. Someone asks a sharp question in a meeting, a senior person answers it well, three people nod, and a week later a new member walks in and asks exactly the same question. The answer was alive in the room and then it died in the room, because no one wrote it down in a place that the next person would naturally look. Multiply that by a year and you get a team that confuses motion for progress.

The fix is not more meetings. The fix is a single source of truth.

For an engineering or research team, that single source of truth is the GitHub repo. Not Notion, not Confluence, not a shared Google Drive, not a Slack channel pinned to the top of someone's sidebar. The repo, with its README, its docs folder, its issues, its pull requests, its commit history. Everything else is a feeder system into the repo, or it does not count.

I want to be careful here, because I have seen the obvious objection. People say a repo is for code, that documents and discussions belong somewhere richer, somewhere with comments and emojis and nested pages. I get it. Notion is genuinely pretty. Slack is genuinely fast. But the thing those tools optimize for, ease of writing, is exactly what makes them bad at being a source of truth. Easy to write means easy to write the same thing twice in two different places, and now you have two answers to the same question and no way to tell which one is current.

The repo wins because it is hostile to fragmentation. There is one main branch. There is a commit graph that records who changed what and when. There are pull requests that force a moment of review before a change becomes canon. The friction is the feature. When something has to clear that friction to enter the repo, the team learns implicitly that this is the place where claims become real.

What goes into the repo is not just code. The README is the front door, it tells a new member what this project is and how to run it in five minutes. The docs folder holds the design decisions, the why-we-did-it-this-way notes, the gotchas that everyone keeps rediscovering. The issues track open questions, with labels and assignees and a clear status. Pull requests are where proposals get debated in writing, with diffs you can actually read. Even the commit messages, if you take them seriously, become a running narrative of how the team thinks.

I tell collaborators, if a decision is not in the repo, it did not happen. That sounds harsh. It is meant to. Because the alternative is a culture where the loudest person in the room owns the truth, and that culture punishes the new member, the quiet contributor, the person in a different timezone who was not in the meeting. The repo is the great equalizer, anyone can read it, anyone can open an issue, anyone can submit a PR, the work speaks in a form everyone can inspect.

There is a deeper reason I keep coming back to this. A team is not a single mind, it is a graph of minds with patchy overlap. Every person holds a slightly different version of the project in their head. The repo is the only place where those versions can be reconciled, because it is the only place where reconciliation is forced into a single linear history. Slack lets you live in parallel realities forever. The repo makes you merge.

Day to day, what does this look like? When someone proposes a new direction, they open an issue with the proposal written out, not a Slack message. When a meeting produces a decision, someone writes it into the relevant doc in the repo before the meeting ends, otherwise the decision is provisional. When a new member joins, they are pointed at the README and told to read until they have questions, and their questions become issues that improve the README. When something breaks, the postmortem lives in the repo, not in a Google doc that will be lost in someone's drive in six months.

It is not free. Writing things down is slower than saying them. People resist at first, especially people who built their authority on knowing things others did not. That resistance is information, it tells you who in the team benefits from the fragmentation. The shift to a repo-as-truth culture is, quietly, a shift away from informal power and toward written, reviewable, contestable claims. Some teams cannot make that shift, and those teams stay small or stay confused.

The teams that do make the shift get something valuable in return. They get a project that a new contributor can onboard into in a day instead of a month. They get a memory that survives turnover. They get the ability to look back at last quarter's decisions and ask, honestly, did we do what we said we would, because the record is right there. That last one is the part most teams cannot bring themselves to do, because honest retrospection requires honest records, and the repo is one of the few places where the record cannot quietly be edited to make the past look nicer than it was.

Pick the repo. Make it the only place. Everything else is scratch paper.
