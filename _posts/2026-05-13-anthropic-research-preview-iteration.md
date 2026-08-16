---
title: "Anthropic's Most Ruthless Methodology Is Shipping the Worst Version First"
date: 2026-05-13
permalink: /posts/2026/05/anthropic-research-preview-iteration/
tags:
  - Anthropic
  - Claude Code
  - 产品方法论
  - Research Preview
  - AI
  - 创业
---
Anthropic's most ruthless move isn't polishing every product to perfection before release, but daring to throw out a research preview first, then rapidly getting stronger in front of everyone.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

I've been thinking about Anthropic's product cadence these past couple of days.

Not model parameters, not benchmarks, and not those scary-looking bar charts in launch screenshots.

I'm thinking about something plainer: Anthropic seems to be getting better and better at one thing, ship first, watch feedback, then iterate fast.

And it's pretty honest about what it ships.

A lot of things launch explicitly as a research preview.

Those two words are actually quite clever. It's not a very engineering-flavored term like beta, nor is it the marketing-speak of "coming soon." The subtext of research preview is: we ourselves know this thing isn't stable yet. It might make mistakes, it might be expensive, it might baffle you, but you use it first, and your feedback will directly shape what it becomes later.

I think this posture matters a lot.

Because the biggest problem with many AI products today isn't that features aren't strong enough, it's that they're too afraid to lose face. Teams always want to wait until it's as stable as a normal SaaS, until every button has an explanation, until onboarding is silky smooth, until customer-service scripts are ready, before they dare push the thing to users.

But large-model products don't grow like that.

It's more like a very clever but not-yet-socialized child. If you lock it in a lab and train it for six months, of course it gets stronger, but it doesn't know how real-world users will abuse it. Users will throw an entire legacy codebase at it, have it modify a build system nobody dares touch, have it keep fixing bugs when the context window is about to blow, and curse it while continuing to pay it.

None of those scenarios can be simulated in the lab.

Claude Code is a great example.

Strictly by the public timeline, Claude Code was released on [February 24, 2025](https://www.anthropic.com/news/claude-3-7-sonnet) alongside Claude 3.7 Sonnet as a limited research preview. By [May 22, 2025](https://www.anthropic.com/news/claude-4), Anthropic said in the Claude 4 announcement that Claude Code was generally available, roughly three months in between.

So to say "nobody used it for six months" isn't necessarily precise calendar fact; it's more the product person's felt sense.

By feel, it was indeed strange at first.

An agent in the command line that can read your code, change files, run tests, and submit PRs. Sounds fierce, but when you actually open the terminal, your first reaction might be: buddy, do you really dare touch my repo?

I had that feeling the first time I used Claude Code myself.

Not that it was weak, but that I didn't know how to work with it.

Tell it to change whatever it wants and it might change too much. Tell it to look-only and it's like its hands are tied. Give it a vague task and it'll try hard, but likely in the wrong direction. Ask it to run tests and it might gobble up the whole context. Watching that terminal scroll, your heart is half excitement, half "please don't blow things up."

That's the real state of a research preview.

The worst version.

But interestingly, Anthropic doesn't seem afraid to admit this.

In [April 2025](https://www.anthropic.com/engineering/claude-code-best-practices) they published a Claude Code best practices piece that said it plainly: Claude Code is a low-level, scriptable, close-to-raw-model-access power tool with a learning curve. Later versions of the best practices went on to emphasize that good results come from tight feedback loops, correcting early, giving Claude ways to verify its own work, and having it self-check with tests, screenshots, and output results.

This is not the traditional product manager line of "our product is very easy to use."

It's saying: look, this thing right now is a living creature, you have to learn to tame it, and we're learning too.

I actually really like that honesty.

Because the thing agent products should fear isn't roughness; it's pretending to already be mature.

If an agent claims it can do everything, and then can't even read the project structure on the first try, users lose trust instantly. But if it tells you from the start, I'm a research preview right now, and today's version is probably the worst version you'll ever see in your life, and it'll improve rapidly after this, then the user's expectation is completely different.

You're not buying a finished product.

You're participating in a system that will grow up.

On this point I think Anthropic is very different from many companies. Many teams build products by imagining the complete form internally, holding it in for a long time, launching, and praying the market likes it. Anthropic's play is more like putting out something with core capability but still rough edges, and letting real users grind down its boundaries.

Claude Code's subsequent iterations basically follow user pain points.

Users said it was hard to see status in the command line, so later it did a [terminal interface refresh](https://www.anthropic.com/news/enabling-claude-code-to-work-more-autonomously).

Users said they wanted to see diffs in the IDE, so later it did the VS Code extension.

Users said they wanted to roll back after the agent ran too far, so later it did checkpoints.

Users said confirming every step was annoying, so later it did auto mode, but added a permission framework and classifiers.

These features weren't brainstormed in a meeting room; they look clearly like they were yelled out by real users.

I don't mean that as an insult.

Good products are yelled out by real users.

Especially something like Claude Code: it's not a button, not an app, not a pretty interface. It reaches straight into your workflow, into your repo, into your tests, lint, CI, GitHub, terminal, and IDE. Every boundary it touches is a real boundary in the user's work.

So it has to get into real work as early as possible.

If you only look at Claude Code in a demo, it feels like magic. Open a project, write a few sentences of natural language, it auto-changes code, auto-runs tests, auto-files PRs. So satisfying.

But if you really use it for a week, you'll find engineering details behind all the magic.

How to manage context.

How to set permissions.

How to roll back errors.

How to parallelize multiple agents.

When humans should intervene.

How to break tasks into smaller pieces.

Whether to `/clear` after failing twice.

These things look fragmented, but they're the true moat of an agent product.

Model capability matters, of course, but model capability is just the engine. What really lets a car get on the road is the steering wheel, brakes, gauges, seatbelt, and knowing when to pull over.

That's where Anthropic's methodology excels.

It doesn't first spray the paint pretty; it first gets the car on a real road, then listens to users curse that the brakes are too hard, and fixes it fast.

Seriously, this methodology is very illuminating for anyone building AI products.

If you're going to build an agent today, don't wait until it can do everything before releasing.

Because you have no idea what users actually want it to do.

You think users want an assistant that can write code; what they actually want is a colleague who can read an old project, dare to run tests, and push a PR from 0 to 1.

You think users want an assistant that summarizes documents; what they actually want is a person who can shuttle between Slack, Google Drive, Notion, and GitHub on its own and close the loop.

You think users want a pretty chatbox; what they actually want is fewer than 17 tabs open.

These differences only surface after the product is shipped.

And research preview gives the team a good buffer zone.

It allows you to be imperfect.

It also requires you to improve fast.

There's a crucial moral contract here. You can't use research preview as a shield and release something lousy then lie flat. You have to tell users clearly: today's version might genuinely be the worst, but we'll seriously read the feedback, we'll fix it fast, and we'll turn what you curse about into the next version.

Users actually can accept roughness.

What users can't accept is roughness with nobody responding.

Claude Code wasn't a product everyone knew how to use at first. I even suspect many people closed it after the first open, wondering what its relationship with Cursor was and why they were chatting with a model in a terminal.

But once that wheel of "ship, feedback, iterate" started turning, things changed.

Early users started writing best practices, sharing their workflows, wiring it into GitHub, CI, and their own scripts. Anthropic itself wrote up internal usage experience. A tool gradually went from "a thing a few nerds play with" to "part of how the team works."

That's the flywheel.

It didn't blow up all of a sudden one day.

You put out something immature but directionally right, then let the real world knock on it every day. Knock on it to day 100 and it starts to look like a product. Knock on it to day 300 and it starts to look like infrastructure.

Sometimes I think the most counterintuitive thing about the AI era is exactly this.

In the past we always felt product launch was an endpoint. You work for a long time, finally launch, everyone applauds, you post on Product Hunt, post on Twitter, post on WeChat, then watch the numbers.

But for agent products, launch looks more like a starting point.

At the moment of launch, it hasn't even really been born yet.

Its real birth is the first time a user throws it into a dirty real workflow, the first mistake, the first time a user interrupts it, the first time it grows a new feature from feedback.

This reminds me of biological evolution.

A species can't evolve, in a sterile room, to be adapted to the wilderness. It has to enter the environment, be selected, eliminated, and forced to change. Same with products. Especially AI products: if you don't put them into users' chaotic lives, they'll only ever be elegant in a demo.

And real life is never elegant.

Real life is tests failing, dependency conflicts, a repo full of ten-year-old code, the boss wanting a demo tomorrow morning, a user saying this button is too big, CI red again, model context blown, you still watching it run in the terminal at 2am.

Only the things that keep pushing forward under these conditions get a chance to survive.

So I believe more and more that the best release copy for an AI product might not be "we're strong."

It's "This is a research preview. Right now it will be the worst version. Use it first, curse at us, and we'll fix it immediately."

That sounds a bit less dignified, but it's very real.

And it's powerful.

Because it turns users from consumers into people jointly training the system.

Back to Anthropic.

What really earns my respect for Claude Code isn't just how much it can do today, but that from the very start it placed itself in a position that can be shaped by real feedback. Ship first, admit the roughness, watch how users use it, add best practices, add permissions, add the IDE, add rollback, add automation.

That road is hard.

Because you'll be cursed at.

You'll see users say you're expensive, you're slow, you're glitchy, you changed the wrong file, your context management is a mess. You can't hide behind "we're not ready" anymore, because you've already shipped.

But only this way does the product really grow.

I'm increasingly influenced by this thinking when building things myself. Don't always aim for one-shot perfection. First build the core capability, give it to real people, tell them it's just a research preview, tell them today it's at its worst, then catch the feedback.

Catching it is more important than perfection.

What an era, folks.

Going forward, many products may not be designed at all, but used into existence. Whoever dares to enter real scenarios earlier, whoever dares to face ugly feedback sooner, has a better chance of raising an agent from a demo into infrastructure.

That's how simple the takeaway Claude Code gave me is.

Ship first.

Then listen carefully.

Then fix fast.

Thanks for reading my article. Until next time.