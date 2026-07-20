---
title: 'AI Can Plan My International Trip, but It Still Cannot Clear the Payment Gate'
date: 2026-07-18
permalink: /posts/2026/07/ai-international-travel-secretary/
tags:
  - AI
  - travel
  - automation
  - assistants
  - reflection
---

The thing that almost stranded me on this international trip was not a typhoon, but several unrelated systems deciding at the same time that they did not trust me.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

My route was Chengdu, Shenzhen, Singapore, Vancouver, and Austin. A few days before departure, I tried to use Chase Travel and my Sapphire Preferred card to handle the long-haul segment from Singapore to the United States. Chase Travel was unavailable, and Air Canada had placed security restrictions on my account during the login and booking process. I switched to the [Air Canada website](https://www.aircanada.com/) and tried to pay as a guest.

The problem did not end on the website. Air Canada locked my Aeroplan frequent-flyer account for no apparent reason. I called to resolve it, waited for an hour, and still did not reach an available agent. AI can generate troubleshooting steps and a call script, but it cannot make an airline put a human being on the phone.

It sounds simple, right?

I selected my CSP as the payment method and entered my United MileagePlus number because Air Canada and United are both part of Star Alliance. Then the payment page froze.

Not a clear failure. Not a clear success.

The page kept loading. I did not know whether the card request had reached the payment gateway, or whether the ticket had been issued. There was no confirmation email. The bank app might show a pending authorization, but an authorization is not an e-ticket. The most dangerous thing to do at that moment would have been to refresh the page, submit again, and discover several minutes later that I had bought two tickets.

This is the first kind of problem AI will meet in the real world. A model can understand booking rules and tell me not to submit the payment twice. It cannot magically know the state of the airline's order system. It does not hold the ticket, and it does not see the payment gateway's internal state. It can only reconstruct an incomplete world from a webpage, an email inbox, and a banking notification.

Humans are not much smarter in that moment. My first reaction was to curse at the website and keep checking whether the page had moved. The useful response was much more boring. Stop clicking. Check the email and the bank record. Let the system settle. Then ask the airline to confirm whether the ticket exists.

That experience made me rethink the boundary of an AI assistant.

AI is good at decomposing travel into search, comparison, calculation, and reminders. It can estimate whether thunderstorms in Shenzhen might affect an inbound flight. It can translate a 9-hour-30-minute connection into a delay tolerance. It can remind me that a seven-hour Vancouver connection leaves room for immigration and baggage handling. It can compare Chase Travel, the airline website, and an online travel agency in seconds.

But whether I actually get on the plane depends on identity, payment, permissions, network access, and responsibility.

Those things do not live in one system.

Chase may mark a transaction as risky. Approving one attempt by text does not guarantee that the next attempt will pass. Grab may not offer a retry path after a failed payment. Air Canada may lock an account without preventing guest checkout. A payment page may keep loading even though the airline has created an order, or even though it has created nothing at all.

Every system is protecting itself. None of them is responsible for explaining the whole story to me.

I saw the same pattern when taking a ride in Singapore. Chase locked the CSP again and again. Approving the transaction by text did not solve the loop, and Grab did not offer a useful retry path. My friend Junyuan later explained that the direct activation path was not to bypass Chase separately for every payment. It was to insert the same physical CSP into a real card-present terminal once, so Chase could receive a card-present transaction signal. In my case, after that activation step, the CSP started working across other situations in Singapore. Grab still did not offer a useful retry path, so I used WeChat Pay for that ride first.

That is absurd in a very specific way. Someone with a U.S. credit history, travel points, and phone verification still had to return to a physical card and a local payment network to complete a small ride payment.

This is why I do not think high-end human secretaries will lose their value simply because AI exists.

I am not talking about someone who only books meeting rooms and edits spreadsheets. I mean a person who can move across systems. Someone who knows when to continue automating and when to stop clicking. Someone who can distinguish a credit-card authorization from a ticket issuance, and knows whether to call the bank, the airline, or the travel agency. Someone who can change devices, networks, and payment methods when the connection is poor, and can explain the problem in the local language to the party that can actually fix it.

That used to be called secretarial experience. Today it looks more like orchestration in the physical world.

The hard part for AI is not only insufficient reasoning. It is that the model often cannot see the real state. It sees a webpage, an API response, an email, or a button that looks successful. The real world is made of systems with different permissions, delays, and failure modes.

The model saying that payment succeeded does not mean the ticket was issued. The model saying that an account is locked does not mean guest checkout is impossible. The model saying that a 24-hour cancellation rule exists does not mean it applies when departure is less than seven days away. Every conclusion has to be reconciled with the actual order state.

That is why I do not think the endpoint of the AI assistant is a chatbot that talks more smoothly. A useful system needs to maintain a cross-platform state table. It needs to know what has been confirmed, what is only inferred, and what requires a phone call. Before a consequential action, it needs to expose uncertainty and hand the decision back to a person.

Travel makes this especially clear. International travel compresses payments, visas, baggage, flights, time zones, language, and local transportation into one timeline. When one system enters an unknown state, every later plan can drift with it.

AI can design the route.

A high-end secretary keeps the route alive in the real world.

I still want an AI that can search flights, compare protection, fill forms, monitor delays, and prepare phone scripts. I also want it to know when it lacks permission, when it should not trust a green button, and when it needs to tell me not to click a second time.

The last mile of international travel may always need a human being.

Perhaps the most valuable secretary of the future will not be the person AI replaces. It will be the person who can coordinate AI, banks, airlines, payment networks, and local reality into one working plan.
