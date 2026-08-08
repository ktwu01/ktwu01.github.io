---
title: 'If Jobs Were Building Today, He Would Toss Most multiAgent Products in the Trash'
date: 2026-02-09
permalink: /posts/2026/02/jobs-multiagent-saas-end/
tags:
  - ai
  - multi-agent
  - saas
  - steve-jobs
  - startup
  - product
  - jony-ive
  - knowledge-navigator
---

Lay out every hyped multiAgent product on a table in front of Steve Jobs and he would probably squint, frown, and ask one question, why on earth are you showing the user any of this.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

I have been chewing on this for weeks. The whole industry is hyped right now, orchestrators, toolboxes, agent collaboration graphs, CrewAI, LangGraph, AutoGen, every flavor of multi-agent framework you can imagine. I have built a few myself, a router agent up top with billing, search, and email agents below, fanning out and coming back. Works fine.

But something about it has been bugging me.

Then I went back and watched the Jobs interview from 1994, the laundry object passage, and it just clicked. He was explaining object-oriented programming. He said, suppose I am your laundry object. You hand me your dirty clothes and send me a message, please get my laundry done. I happen to know where the best laundry place in San Francisco is, I speak English, I have dollars in my pocket. I go out, I hail a cab, I take the laundry, I bring it back clean. You have no idea how I did it. **All of the complexity is hidden inside me.**

Read that again. Slowly.

That is what an agent should be. **All of the complexity, hidden inside.**

Now look at almost every multiAgent product shipping today. They do the exact opposite. They show you every step. Calling weather tool. Switching to search agent. Routing to code reviewer. Agent A handing off to Agent B. The whole thing narrates itself, like an enthusiastic intern reading their KPIs out loud.

That is engineers performing for engineers. It is not a product.

Engineers love it because it makes the internals visible. Users do not care. Users want clean clothes.

## Friction is the real enemy

Jobs spent his whole life going to war with friction.

When he killed the floppy drive on the Mac, the industry called him crazy. When he killed every non-USB port on the iMac, they called him crazy again. When he killed the keyboard on the iPhone, same chorus. Each time, what looked like a feature to everyone else looked like friction to him.

A power button is friction. A toggle is friction. A UI you have to learn is the biggest friction of all.

Now look at what we are shipping in AI today. Where is the worst friction?

**It is the user being forced to play prompt engineer.**

Open Claude. Open ChatGPT. Open any agent platform. You have to think, how should I word this, do I need a role prompt, should I break it into steps, which model do I pick. Every one of those moves is friction.

And the SaaS world is even more brutal. A friend of mine in sales lives across Salesforce, Notion, Slack, Gmail, Zoom, Calendly, and HubSpot. Every product has its own UI, its own shortcuts, its own navigation logic. A simple intent, follow up with last week's customer, becomes a hopscotch across four or five surfaces with copy-paste in between.

Look at that pattern. It is the same shape as the nine-inch floppy and the clunky desktop mouse Jobs was staring at decades ago.

**The UI itself is the friction now.**

## SaaS UIs go first

Here is the call. It might sound a bit harsh, but I am genuinely convinced, **within the next five years, most traditional SaaS frontends become a piece of legacy clutter.**

Not the SaaS, the panel.

The logic is simple. SaaS panels were designed for humans. The next generation of primary users is agents. Agents do not need your beautifully crafted dashboard, they need an API. Agents do not need your slick dropdown menu, they need a structured endpoint and a clean schema.

This shift is already underway. The rise of MCP, Model Context Protocol, is the early signal. What Anthropic is really admitting with MCP is that AI should not be using our UI, AI should have its own protocol layer.

So what does that mean, or rather, where does it land. It means every SaaS company that built its moat on a pretty frontend, a slick UX, a smooth interaction layer, is watching that moat quietly drain. If your only real value is a good-looking panel, you are agent-ecosystem cannon fodder.

What survives is the boring stuff. **The most reliable APIs. The deepest data. The most deterministic execution.** Those services do not get opened by users. They get hit ten thousand times a day by agents and the user never feels a thing.

Cold reality. Also a giant opening.

## Knowledge Navigator already saw this coming

In 1987, Apple shot a concept video called Knowledge Navigator.

In it there is a digital assistant named Phil, a little bow-tied face that lives in a folding screen. A professor sits sipping coffee, talking to Phil, asking it to pull a paper, synthesize data, prep tomorrow's lecture. Phil quietly hits databases, checks colleagues' calendars, organizes research. No app. No window. No switching. Just a conversation.

That video came out under Sculley but Jobs himself made similar predictions. In a 1983 talk he said, one day we will build a tool that captures a person's worldview, that you can just ask questions and it gives you answers.

That was almost forty years ago.

What are we doing today? We are shipping app after app and asking users to bounce between them. Our agents still narrate every move, calling weather tool, switching agent, terrified the user might not realize we are working hard.

We are nowhere near Phil.

The technology is not the bottleneck. The **mindset** is. The whole industry is still stuck on showing AI at work, instead of letting AI just quietly finish.

## What Jobs would design

If Jobs were sitting in a meeting room at Apple Park today, working on an AI product, here is what I think he would do.

First, he would kill every visible agent UI. All those fancy collaboration graphs, chain-of-thought displays, intermediate-step replays. Gone, every one of them. Users should feel the result, not the process. The process is the engineer's problem, not the user's.

Second, he would redefine the input. Right now we hand users a text box and tell them to write a prompt. That is already a failure. Jobs killed the physical keyboard on the iPhone with multi-touch because he saw the keyboard as a wall between human and machine. The text box is the new keyboard. He would find a new medium.

Not a coincidence, his old design partner Jony Ive is now working with Sam Altman on new AI hardware. Nobody knows the form factor yet, but whatever those two ship, the direction is clearly **kill the screen**. The screen is this era's wall, just like the keyboard was the wall between user and Mac.

Third, he would do tight hardware-software integration. No app to download, no workflow to configure, no model to pick. Turn it on and it works. It just works. All the complexity hidden inside.

Fourth, and this one I really want to underline, he would refuse to ship a toolbox.

A lot of startups today are basically pitching, we will give you a platform, you assemble the agents, you configure the workflows, you pick the tools. Sounds flexible, sounds powerful, right?

Jobs would call this **a failure of product design.**

He never let users assemble. When the Mac came out, the industry mocked Apple as closed. You could not stick an IBM card in. You could not swap the drive. You could not roll your own. Jobs's answer was, yes, because we already thought it through for you. You do not assemble, you open it and use it.

Apply that to agents and the conclusion is brutally clear. **An AI product where the user has to design workflows, pick agents, and write prompts, is a product that is not finished yet.**

## Founders, what should you actually do

A few honest words for the startup folks reading this.

I am still figuring this out myself. Some of these takes might not be fully cooked. But here is where I have landed, sharing in case it helps.

One, **stop building a better UI, build deeper execution.** If SaaS frontends are going to get bypassed by agents, pouring effort into a prettier panel is wasted motion. Pour the same effort into API reliability, exclusive data, deterministic execution. In the agent ecosystem, the API that does not break wins. What is scarce in this era is not pretty products, it is **services you can actually rely on.**

Two, **find one high-value vertical and wrap it end to end.** Do not build a platform, build a scenario. Pick something concrete, monetizable, painful. Monthly financial reports for SMB owners. Patient follow-ups for solo physicians. Product research for cross-border sellers. Then take all the complexity behind that scenario, every tool call, every intermediate step, and seal it inside one simple entry point. The user comes in, says one sentence, and the result lands. No thinking. No configuring. No picking.

Three, **chase zero friction.** Make a list of every place in your product where the user has to think a little about how to use it, then go kill those places one by one. It is painful, because you will discover that many of your favorite features are actually friction in disguise. That is the path.

Four, accept a counter-intuitive truth, **the more your product looks like an agent, the less it looks like a product.** The more you expose internal mechanics to users, the worse the experience gets. The truly elite agent product is one where the user cannot feel the agent at all.

Honestly, the biggest opportunity in this AI wave is not who builds the smartest agent, it is who uses agents to build something that feels truly **invisible.**

Let users feel the result, not the process.

Let all the complexity hide inside.

Let it just work.

## The bicycle, take two

Jobs has this metaphor that has been quoted forever, **computers are a bicycle for the mind.**

He said he saw a study ranking the locomotion efficiency of different animals. Condor first, humans somewhere mid-pack. But put a human on a bicycle and they instantly leap to the top of the chart. A computer, he said, should be that. A tool that lets thought move at speeds it could never reach unaided.

Sometimes I think the last forty years of bicycle building did not go that well.

We built bicycles loaded with buttons, dense dashboards, training required. Some specialists got faster. Most people climbed on, looked around, and felt like walking would have been less work.

AI gives us a chance to redesign the bike from scratch.

And the multiAgent paradigm, if it stops at toolboxes and orchestrators, is essentially **a bicycle with even more buttons.** What we need is not more buttons. We need to take all the buttons off, and let the thing just move.

Back to the laundry object.

I want the next generation of AI products to be that laundry object. I hand it dirty clothes, it hands me back clean ones. I never have to know how many cabs it took, which laundromat it used, how many dollars it spent. I just know it gets the job done.

That is a product.

That is what Jobs would have built.
