---
title: 'Why I Want AI Actions to Manage My Information Flow'
date: 2026-06-14
permalink: /posts/2026/06/ai-native-document-flow/
tags:
  - AI
  - automation
  - workflow
  - personal-ops
  - writing
---

What I actually want to do today is pull myself out from under a mountain of repetitive work.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

Here is what happened. I had just added a Port Aransas South Jetty article to the website. In theory, it was a small task: add a post, update the media page, and add it to the "Featured in" line on the homepage.

But a real life contains more than a homepage.

When a new project appears, it should not stop in one place. It may need to enter a resume, a CV, a personal website, a portfolio, media coverage, a future grant biography, a project archive, or eventually a chronicle or founder story. Each outlet describes the same person, but each uses a different format.

That is annoying.

Worse, the annoyance repeats. Today it is a media report. Tomorrow it is a new preprint. The next day it is a talk. After that, it may be a GitHub project, an internship, or an award. Every time, I have to think again about where the information belongs, which files need updating, and which versions have become stale.

That is what I mean by information flow.

On the surface, this repository is a personal website. Underneath, it is already an information-flow graph. `_pages/about.md` contains the homepage narrative. `_pages/media.md` contains media evidence. `_pages/cv.md` and `_data/cv.json` hold the resume structure. `_portfolio/` contains projects, `_publications/` contains papers, `_talks/` contains presentations, and `chronicles/` contains longer, evidence-based narratives.

They are not isolated files.

They are different outlets from the same database of a life.

Before I began using Claude Code and Codex for this workflow, GitHub Actions handled the repository automation. After a push, it ran tests, built the website, and deployed it to GitHub Pages. That worked well, but it managed the code lifecycle, not the information lifecycle.

What I want now is AI Actions.

AI Actions would send every new piece of information first to a single source of truth and give Claude Code explicit routes to follow. A new project, for example, would first become a structured node. The node would contain its name, date, role, collaborators, evidence links, impact, and the documents to which it should flow. AI Actions would then move the information from that node to each destination.

A resume needs one short impact bullet, so it generates the short version. A professional dossier needs an evidence chain, so it connects the source, date, role, and impact. A personal website needs a readable narrative, so it writes a post or portfolio entry. The media page needs only one line, so it writes one line.

People should remain responsible for judgment, not manual copying and pasting.

I looked through my old Codex history. Many prompts appear small: change a dashboard, update a scratchpad, add a Google Drive mount, fix Earth Engine authentication, open a pull request, or revise a blog post. Each line looks like an improvised command when read on its own.

But I increasingly believe that a prompt is more than a sentence.

A prompt is a compressed archive of a workflow.

When you ask me to change a dashboard, the request also contains information architecture, user paths, caching rules, component boundaries, and the constraint not to disturb other sections. When you ask me to add a media post, it contains source verification, Jekyll front matter, homepage exposure, media-page classification, article archiving, and evidence that a future CV or project archive may need.

If a person has to unpack all of this from memory every time, the work becomes exhausting.

Repetitive maintenance has worn me down. I want AI to move information automatically through a workflow that has already been defined, leaving prose generation as a secondary use.

I even think the root directory should contain a node graph. It would show where new information enters, where the single source of truth lives, and how the resume, blog, media page, portfolio, publications, talks, and chronicles receive it. Once the graph exists, many tasks stop being vague wishes and become routes an agent can follow.

I am doing this because the problem is basic: each new result still requires the same manual updates.

I do not want to reopen five files and copy information by hand every time I have a new result, worrying as I edit that I have missed a destination. I do not want to discover three months later that one resume is still outdated, a media page is missing a report, or evidence never entered the project archive.

That waste is stupid.

In a genuinely AI-native workflow, I should declare a fact once, and the system should send it to every place where it belongs. The system should come back to me only when judgment, tone, or priority requires a decision.

The rest of the time, let the information flow on its own.

That is what I want to build.

Over time, I want my work, documents, evidence, prompts, and session logs to form one graph. Its purpose would be to keep my career record current without requiring me to move each fact by hand.

Frankly, this may be the AI I want most right now.

An AI that can pull me out from under a mountain of repetitive work.
