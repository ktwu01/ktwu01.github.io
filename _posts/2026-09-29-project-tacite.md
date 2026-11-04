---
title: "Tacite"
date: 2026-09-29
permalink: /posts/2026/09/project-tacite/
tags:
  - media
  - project
---

[Tacite](https://tacite.ai/) is one of my projects exploring AI products and how people interact with them.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

Every lab and every construction site has someone who knows why the last attempt failed. The fix lives in their head, or in an email thread from two years ago, or in a note scribbled on a drawing. When that person changes shifts or leaves, the team makes the same mistake again. Now add AI agents to the team, and they make the same mistake faster.

Tacite is built for that problem. Its tagline is "Run the physical world on proven know-how." It comes from Knowlytics Inc, a team founded at The University of Texas at Austin, and I work on it as the person responsible for product and AI.

## How it works

The product runs a three-step loop.

1. **Notice.** Tacite is set up with a team and watches for the moments when someone fixes a problem. It pulls from email, drawings, and business systems into one workflow.
2. **Expert approves.** An expert reviews each saved fix before anyone else sees it. Each fix is stored with its reason, its supporting evidence, and the conditions where it applies.
3. **Remind.** While people and AI agents work, Tacite flags when someone is about to repeat a mistake an expert already solved, and shows the approved fix.

The approval step is the design choice I care most about. Automatic knowledge capture is easy to build and easy to pollute. One wrong "fix" that spreads to a whole team is worse than no system at all. Putting an expert in the loop costs a few minutes per fix and keeps the knowledge base something people can trust.

## Who uses it

The early partners show the range: a construction general contractor, UT3 in laser and plasma research, and EarthSpace AI. The site lists uses in R&D labs, construction billing and invoicing, startup operations, and a Quant Co-pilot for investment teams. Pilot areas on the roadmap include bio labs, flood control, and construction site fire safety.

Companies control what gets shared, who approves fixes, and who can see them. Tacite can run in the cloud or on a company's own AI hardware, and AMD provided Ryzen AI Max hardware and support for on-premise deployment. The latest release when I wrote this was v0.17.1, from July 21, 2026.

## Why tacit knowledge

The name comes from tacit knowledge, the kind of expertise people use without writing it down. Papers and manuals record what worked. They rarely record the five things that failed first, or the reason a step that looks optional is the one that matters. That missing record is exactly what new team members and AI agents lack.

Language models made this problem sharper. An agent can read every manual a company has, and it still knows nothing about the shortcut that broke the pump last spring. Tacite's bet is that the most valuable data a team owns is its record of solved mistakes, and that the record only works if an expert vouches for it.

My open question is adoption. Experts are the busiest people on any team, and an approval queue can grow faster than they clear it. The product works only if approving a fix takes less effort than explaining it again to the next new hire.

A team that remembers its fixes stops paying for the same mistake twice.

Visit [Tacite](https://tacite.ai/).
