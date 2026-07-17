---
title: 'AI Can Plan the Trip. It Still Cannot Get the Car to Move.'
date: 2026-07-18
permalink: /posts/2026/07/ai-travel-and-the-return-of-the-high-end-secretary/
tags:
  - AI agents
  - international travel
  - payments
  - human-in-the-loop
  - operations
---

The last mile of an AI-generated travel plan may be one missing **Retry** button.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

I recently arrived in Singapore with a large suitcase, a heavy backpack, and somewhere I needed to be. AI could compare hostels, reason about lockers, map a route to NUS, check the weather, estimate when I should leave for a 7:00 a.m. flight, and explain which Grab option would accept my luggage.

Then I tried to pay for the ride.

Grab submitted a card-not-present transaction to my Chase Sapphire Preferred card. Chase blocked it and texted me to ask whether the charge was mine. I replied that it was. But Grab offered no way to retry the failed transaction. Starting again produced another rejection and another approval request.

Every component was behaving somewhat rationally:

- Chase was trying to prevent fraud.
- Grab treated a declined payment as final for that attempt.
- The text message authenticated me after the transaction had already died.
- I had a valid card and enough credit.

The system as a whole was useless.

What I needed was not merely an alternative way to pay for that one taxi ride. The most direct way to **activate the CSP for use in Singapore** was to insert the physical card into a card reader and complete a card-present transaction. Once activated that way, the same CSP could be used normally across Singapore, instead of repeatedly falling into the Chase–Grab online-payment loop. I could not perform that activation inside Grab; in the end, I used WeChat Pay to complete the ride.

This was not a knowledge problem. It was an **execution problem across incompatible systems**.

## What AI can already do well in international travel

Travel is an unusually good environment for AI. It involves a large number of small research and reasoning tasks:

- comparing routes, prices, baggage rules, and cancellation conditions;
- translating addresses, forms, and conversations;
- checking weather, transit schedules, airport terminals, and border requirements;
- constructing a timetable backward from a flight departure;
- remembering preferences such as low price, secure luggage storage, and proximity to a university;
- proposing backup plans when a hostel sells out or a train stops running.

Modern AI is already better than a mediocre human assistant at many of these tasks. It is fast, patient, multilingual, and able to search across more possibilities than a person would normally consider.

But a trip is not completed when the plan is correct. It is completed when the traveler and the suitcase arrive.

## The failures AI faces today are often between systems

An AI may know exactly what should happen and still be unable to make it happen.

The hardest failures increasingly live at the boundaries:

1. **Identity boundaries.** A bank recognizes the cardholder, but the merchant does not receive that updated trust signal.
2. **State boundaries.** One system changes its decision, while another system has already closed the transaction and exposes no retry path.
3. **Interface boundaries.** The solution requires tapping a phone, inserting a physical card, speaking to a taxi dispatcher, or showing a passport.
4. **Authority boundaries.** An AI can recommend a purchase but may not be authorized to spend, sign, rebook, or disclose identity documents.
5. **Physical boundaries.** Luggage size, a locked hostel door, a missing adapter, or an airport pickup zone cannot be resolved by better prose.
6. **Liability boundaries.** When immigration, money, or a missed international flight is involved, someone must decide which risk to accept.

These are not edge cases. International travel is a chain of airlines, banks, payment processors, hotels, immigration agencies, telecom providers, taxis, and local apps. A trip succeeds only if every critical link works at the right time.

An AI agent can call ten APIs and still be defeated by the eleventh organization having no API at all.

## Why a high-end secretary is still extremely useful

This experience changed how I think about the future of personal assistance. AI will reduce the value of someone whose only job is to search Google, copy information into a calendar, or produce a neat itinerary.

It may increase the value of a truly capable secretary.

A high-end secretary is not merely a person who knows the flight time. The useful person can:

- notice that an automated workflow has entered a dead loop;
- call the bank while simultaneously keeping the ride or reservation alive;
- know when to abandon the app and move to a physical counter;
- communicate with a driver, hotel, airline, or immigration officer in the relevant language;
- use delegated authority without exceeding it;
- protect passports, payment details, and sensitive messages;
- improvise when the official policy and the actual local practice differ;
- take responsibility for closing the loop.

The premium is not for information. It is for **judgment, access, trust, and execution**.

This is especially important in international travel. A domestic inconvenience may cost an hour. A failure abroad may strand a traveler without local payment methods, mobile data, language ability, lodging, or permission to enter the next country. The person helping must understand not only the nominal rule but also the traveler's exact constraints and the consequences of being wrong.

## The winning model is AI plus an empowered human

The future high-end secretary should not compete with AI at reading hotel listings or calculating transit time. AI should handle the broad search, constant monitoring, translation, memory, and first-pass reasoning.

The human should intervene where the world becomes discontinuous:

- an account is locked;
- a transaction is approved but cannot be retried;
- a reservation exists in one system but not another;
- the traveler is exhausted and must make a high-stakes decision;
- the only solution is a phone call, a negotiation, or a physical action.

This division of labor also suggests a useful design principle for AI agents: do not merely report failure. Preserve context, identify the exact broken boundary, propose the cheapest alternative channel, and prepare a clean handoff to a human who has the authority to act.

In my Singapore case, the plan did not need more intelligence. The durable solution was to activate the CSP through a physical card reader, after which it could work throughout Singapore. But Grab could not provide that activation path and could not retry the approved online charge, so WeChat Pay became the immediate way out.

The lesson is simple: AI can make international travel dramatically easier, but reality still has counters, card readers, phone calls, locked doors, and institutions that do not share state. Until agents can reliably cross those boundaries, a first-rate human secretary remains not an obsolete luxury, but an execution layer.

**Related post:**

- [中文版：AI 能规划旅程，却还不能让车真正开起来]({{ site.baseurl }}/zh/posts/2026/07/ai-travel-and-the-return-of-the-high-end-secretary/)
