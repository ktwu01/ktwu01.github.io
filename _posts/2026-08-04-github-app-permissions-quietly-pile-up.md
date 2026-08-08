---
title: 'The GitHub Apps You Installed Months Ago Still Have Full Access. Go Check.'
date: 2026-08-04
permalink: /posts/2026/08/github-app-permissions-quietly-pile-up/
tags:
  - AI Agents
  - GitHub
  - Security
  - Cloud Backup
---

I was in the middle of setting up a second Cloudflare backup, verifying one dataset and configuring another, when the AI agent helping me flagged something unrelated: while listing what had access to my GitHub account, one authorization stood out as unusually broad. That single flag turned into an hour of reviewing GitHub's installed-apps list, and it was worth every minute.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

Nothing had been misused. No data was leaked, nothing was deleted. But what I found sitting there, quietly authorized, is common enough that it is worth writing down plainly: two separate categories of GitHub third-party access, each granted once for a specific reason, each still holding far more reach than that reason justified.

## Two different kinds of access, and why the difference matters

GitHub has two related but distinct mechanisms for letting outside tools touch your account, and the distinction matters a lot for how dangerous each one is.

A **GitHub App installation** is scoped to specific repositories you choose, with specific permissions like "write to repository contents" or "read pull requests." You can review and narrow this list at `github.com/settings/installations`.

An **OAuth App authorization** is different and broader. Rather than being scoped to one or more repositories, it can grant a service the ability to act as you, using your own account's permissions, across everywhere your account reaches, including organizations. You review this separately at `github.com/settings/applications`.

Most people, myself included, glance at the first list occasionally and rarely think about the second at all, because it is presented as a one-time login step rather than an ongoing grant of access.

## What I found

An AI coding assistant I use had an OAuth authorization that let it act on my behalf across four separate GitHub accounts, not one. Two were organizations I do not solely control. I had granted this once, for a narrow, specific task, months earlier. It had kept that full reach the entire time since, silently, because nothing about using the tool day to day ever surfaced the scope of what it could still do.

Separately, a deployment integration I had installed roughly six months prior, for a specific one-time setup, still held full read-and-write access to repository administration settings, webhooks, and pull requests, on every repository it could see. I had never gone back to check whether that scope still matched what I actually needed from it, because nothing prompted me to.

Neither of these was caused by anything malicious. They were both just sitting there, doing nothing wrong, the way a spare key sits in a drawer long after the reason you cut it has passed. The risk was not that either app was actively misbehaving. The risk was that I genuinely did not know, until I looked, what could act on my account and how far that reach extended.

## Why this matters more with AI agents in the loop

This same pattern predates AI agents entirely; over-broad OAuth scopes and stale app installations have always been a real risk. What changes with AI agents is the pace at which you accumulate these grants, and how easy it becomes to stop noticing.

When you are moving fast with an agent helping you wire up integrations, connect services, and automate deployments, granting access becomes a small, low-friction click in the middle of getting something else done. You authorize an app to keep the task moving, the task finishes, and the authorization simply outlives its reason for existing. Multiply that by every integration you have ever connected over a year or two of building things, and the two installed-apps pages become a quiet, growing surface that nobody is actively watching.

An agent helping you build things fast is also an agent that will happily click through an OAuth consent screen if you tell it to, because from its point of view that is just unblocking the next step. It has no independent reason to flag "and by the way, this grant will still be here in six months, un-reviewed." That is squarely a human's job, and it is an easy one to skip.

## What to actually check

This does not require deep security expertise, just two pages and a few minutes.

1. Go to `github.com/settings/installations`. For each installed app, check what repositories it can reach and what permissions it has. Narrow anything broader than the app actually needs for what you use it for.
2. Go to `github.com/settings/applications`. This is the one people skip. Check every OAuth authorization for how many accounts and organizations it reaches, not just repositories. Revoke anything you do not clearly remember granting recently, and anything whose reach is broader than the task you originally granted it for.
3. Treat "I set this up months ago and it still works" as a reason to check it, not a reason to leave it alone. Working fine and being appropriately scoped are two different things, and only one of them is visible without looking.

I found real, correctable over-reach in both categories in under an hour, on an account I thought I paid reasonable attention to. The tools themselves were not the problem. The unreviewed default was.
