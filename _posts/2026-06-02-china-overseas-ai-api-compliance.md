---
title: 'Calling Overseas AI APIs from China: 5 Fatal Compliance Traps (Including Criminal Risk) + How to Do It Legally'
date: 2026-06-02
permalink: /posts/2026/06/china-overseas-ai-api-compliance/
tags:
  - ai
  - startup
  - 创业
  - security
  - compliance
---

Many Chinese teams building embodied AI or AI applications hit the same real-world problem: the domestic models aren't enough, and they want to call the APIs of foreign models like OpenAI and Anthropic directly. That's why a swarm of "relay," "recharge," and "one OpenAI-compatible interface for you" businesses has sprung up.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

I recently helped someone evaluate this kind of business, going through the legal framework, compliance clauses, and lawyer opinions, and the conclusion is: **the risk here is far greater than most people assume.** And you have to distinguish two completely different kinds of risk:

- **Administrative violations** (licenses, cross-border data): consequences are being summoned, ordered to shut down, confiscation of illegal gains, and huge fines, which can kill your business.
- **Criminal risk** (fund flows, content violations): consequences are the loss of personal liberty, the kind that genuinely puts people in prison.

To make it worse, many people think "sign a disclaimer contract and you're fine" is the safety net, and this is the biggest misconception. Below I'll spell out the five traps, then say, in one breath, what the legal way actually looks like.

> Disclaimer upfront: this is a popular-science primer, not legal advice; it reflects my own understanding from my research and consultations. China's data and cybersecurity regulation is changing fast, and this article is based on the rules in force and industry practice as of June 2026, so don't treat it as carved in stone. **Before you scale, find a practicing lawyer who specializes in cross-border data export, cybersecurity, and criminal compliance and get a formal memo from them**; don't rely on a blog post as your basis.

## Trap 1 (Administrative): no license, providing services into China, even to a single customer

This is the most counterintuitive one. Many people think, "I'm not opening public registration; I only serve one company, it's B2B, so it should be fine, right?"

The conclusion the lawyers I consulted gave was blunt: **as long as you provide this kind of service from outside China to a company inside China, even to a single customer, and you don't hold the national operating license, it's illegal.**

The license requirement **doesn't look at how many customers you serve or whether you're open to the public.** The "I'm just B2B, not open to the public" defense is invalid against the license requirement. What's involved may be a value-added telecom business license, may be the record-filing or licensing related to generative AI, or may be both.

In nature this is usually an **administrative violation**: you face being summoned, ordered to shut down, confiscation of illegal gains, and huge fines, enough to kill the business outright. You think "small scale, single customer" is a safe zone, but at the license layer, scale isn't even part of the consideration.

## Trap 2 (Administrative): data crossing the border may need a security assessment, and a contract can't replace that

As long as data is transmitted overseas (when you call a foreign API, your prompts and data leave the country), the cross-border data regulations may apply.

Here I need to be precise and not overstate it: under the CAC's 2024 *Regulations on Promoting and Regulating Cross-Border Data Flows*, if the data crossing the border **contains no personal information** and **isn't "important data"** (for example, ordinary code debugging or generic business copywriting), it can be **exempt** from the security assessment, standard-contract filing, and similar procedures.

But the reverse is also true: once your prompts contain users' personal information, or involve "important data" from a specific industry, you **must** by law carry out the cross-border data security assessment or filing. This is a mandatory precondition under administrative law. Many people think they're only transmitting ordinary text, but the system has no data-masking mechanism at all, and once personal information or sensitive data is leaked en masse, this line gets crossed.

A lot of relay contracts will include a clause saying "the client bears the compliance responsibility for data export," trying to offload the obligation. But as the lawyers point out: **this kind of "allocation of responsibility" can't replace a statutory procedure.** The security assessment is the legal obligation of the party actually transmitting the data; having the client sign a promise doesn't make the procedure disappear, and it doesn't exempt your own liability.

## Trap 3 (Criminal): how money crosses borders, and one wrong step becomes illegal business / facilitating crime

From this one on, the nature changes, these are **criminal traps that genuinely cost you your freedom**.

You collect yuan inside China while your costs are abroad (you have to pay OpenAI in dollars), and the **cross-border settlement of those funds** in between is itself a trap:

- If you use personal accounts and underground banks to exchange currency at scale, it may constitute the **crime of illegal business operations (illegal foreign-exchange trading)**.
- If you use personal WeChat, Alipay, or personal bank cards for large-scale collections, it may be characterized as **illegal business operations / operating a payment-clearing business without a license (colloquially "second clearing")**.
- Even if your purpose is entirely legitimate, if the fund flows are found to be "pass-through bookkeeping" for upstream and downstream parties, the funds side alone can trigger liability, and may even implicate the **crime of aiding information network criminal activities (the "aiding crime")**.

And the trigger threshold on the funds side is **far lower than you'd think.** Anti-money-laundering risk control on personal accounts, upon seeing the pattern of "frequent large flows in, immediately exchanged and out," will flag an alert. **Card freezing is minute-level and irreversible, and it doesn't look at whether your use is legal, only at the fund-flow pattern.** Remember that sentence.

## Trap 4 (Criminal, easiest to overlook): relaying foreign output unchanged, and content violations trip the criminal line

This is the one technical people most easily miss, and also **one of the core reasons people get locked up for running relays**.

The "data export" discussed above is the risk of prompts going out; but there's also a risk in the opposite direction, **the model's generated responses coming back into China.** The values and content boundaries of overseas large models aren't controlled by domestic regulators, and China's *Interim Measures for the Management of Generative AI Services* makes extremely strict demands on generated content.

If your domestic clients (or their end users) generate content involving politics, pornography, or violent terrorism through your relay interface and it spreads inside China, the police, once they trace it back to your interface, will likely hold you criminally responsible as the channel: it may touch the **crime of illegally using information networks** and the **crime of picking quarrels and provoking trouble**, and in the worst cases even national-security-level charges.

The key point: if you simply **pass through** the overseas model's output unchanged, without domestic keyword interception and value alignment, then the moment a red line is crossed, **the disclaimer clauses in your contract become worthless paper at exactly that instant.**

## Trap 5 (Cognitive): thinking "a disclaimer contract = a get-out-of-jail-free card"

Underneath the four traps above sits a more fundamental cognitive error: **a lot of people spend serious money having someone write an airtight "purpose limitation and compliance disclaimer" clause, believing that with this contract they're safe.**

A contract is genuinely useful: it can fix the mutual agreement on the purpose, serve as evidence that you've fulfilled your review duty, and clarify the relative responsibility between you and your client. These things all have value when you're fighting the "presumed knowledge" of the aiding crime.

But a contract **can't change whether the conduct itself is legal.** If the business model itself (unlicensed cross-border AI + data export without assessment + unchanged content pass-through) has already tripped the earlier traps, then however beautifully the contract is written, it's just negotiating "how you and your client split the blame after something goes wrong."

In one sentence: **a contract can stop clients from coming after your money (civil damages), but it can't stop the state machinery from coming after you (administrative and criminal liability). It's a blame-allocation tool, not a get-out-of-jail-free card.**

## So how do you actually do it legally?

Having laid out all these risks, I'm not saying you should never touch this; I'm saying **don't touch it by gray-area means.** The legal path usually looks like this:

1. **Find the right lawyer first.** Not any civil-litigation lawyer you casually ask, but a practicing lawyer specializing in **cross-border data export, cybersecurity, generative-AI regulation, and criminal compliance**, and get a formal memo. Treat the traps above as your consultation checklist and go through them one by one.

2. **Consider an offshore business structure, but don't fool yourself.** If your target clients are themselves going overseas, or you're able to set up an independent operating entity offshore (collection, servers, and personnel all outside China), this is a business transaction between overseas entities and faces naturally different domestic compliance constraints. But whether this structure can truly isolate onshore risk **must be vetted by a lawyer penetrating through the controlling persons' nationalities and the data interaction chain**; don't improvise a "shell company" and fool yourself.

3. **Do the legitimate cross-border assessment.** If your business does involve the export of personal information or important data, go through the cybersecurity review / cross-border data export security assessment / standard-contract filing properly and complete the statutory procedures, instead of using contract clauses to pretend you're passing it off to your client.

4. **Intercept and align on the content side.** Don't pass through the overseas model's output unchanged; do keyword interception, value alignment, and keep logs according to domestic requirements. This is the key to reducing "content criminal risk."

5. **Move funds through corporate accounts and real trade backgrounds.** Use the onshore company's corporate account, sign a real technology-service contract, and remit cross-border through proper channels like services-trade remittance or ODI. Never do large-scale collection via personal accounts plus currency-exchange pass-through bookkeeping.

6. **Finally, do the math.** After factoring in all the compliance costs (license, lawyers, content review, legitimate settlement), see whether the business is still profitable. Often you'll find that once compliance is done, the margins can't support these costs and risks, so the answer is obvious: **not doing it is the most robust choice.**

## A final word

From my own assessment, that kind of **shabby relay operation that takes money through personal Alipay and sells off a rented overseas VPS** is a textbook inversion of risk and reward: the upside is maybe a few thousand dollars a month, capped; the downside is administrative violation plus potential criminal charges, irreversible. Staking a small, capped amount of money on a bottomless, major risk is, rationally, a no.

There genuinely are legitimate options on the market, with proper cross-border dedicated lines, licenses, and compliant settlement; they aren't cheap, but what they buy is real sleep at night.

If you're a legitimate AI application company that genuinely needs overseas compute, the real value of this article is: **know where these traps are earlier, and use a legal structure to get it right earlier, so you don't go looking for a lawyer only after your card is frozen, your account is banned, or you've been "invited in for tea."**

Compliance isn't a cost; it's the precondition for being able to keep doing this thing over the long term.