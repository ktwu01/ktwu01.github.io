---
title: "“We Don't Train on Your Data” Is a Promise. “Your Data Never Left Your Computer” Is a Fact."
date: 2026-09-08
permalink: /posts/2026/09/your-data-never-left-your-computer/
tags:
  - AI
  - Privacy
  - Local AI
  - Research
---

The Navier-Stokes fight is not proof that anyone stole anything. It is proof that the person whose work was at stake had no way to check.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

## The moment the question got real

Imagine spending a year on a result nobody has seen.

It is not on arXiv. It is not in a public GitHub repository. It is not in the scientific literature. It exists in your notes, in your collaborator's messages, and inside the AI assistant you have been pasting drafts into every day for months.

That last location is the one worth thinking about.

On September 7, 2026, NYU mathematician Tristan Buckmaster published a statement about what happened as he and Levent Alpöge, a researcher at Anthropic, finished a set of results on finite-time blowup in fluid equations, work that sits on the road to the Navier-Stokes Millennium Prize Problem. The mathematics may end up being historic. Buckmaster calls it "a Deep Blue-Kasparov moment" for his field.

But buried in his account is a paragraph that has nothing to do with fluid dynamics and everything to do with how all of us now work:

> "I asked whether the model had been trained on, or had access to, our sessions in Codex, into which we had been putting all our drafts for the whole of this project. I was told the model did not look up user data. I asked again, about training, and I did not get an answer."

Read that again, because the important word is *asked*.

He had to ask. And from where he sat, the answer he received was the only evidence available to him.

## What each side actually said

It is worth being precise here, because the precision is the whole argument.

Buckmaster is careful. Strikingly careful, given the circumstances. His statement includes an explicit disclaimer:

> "I have not seen OpenAI's proof. I do not know what their model did, or how. I do not know whether our data was used. I am not accusing anyone of anything."

OpenAI responded publicly, and its response is also careful:

> "We (the researchers and the agents) did not see any of their work through any means until they released it publicly, in particular, no specific user data was accessed in order to solve this problem."

And then, in the same statement:

> "While unlikely, we cannot rule out that de-identified data derived from their usage of our products helped improve our models."

OpenAI's Chief Research Officer, Mark Chen, described the general practice plainly: yes, the company uses user feedback and de-identified data to improve ChatGPT and Codex, and, in his words, so does every LLM company.

So: no accusation on one side, a narrowly scoped denial plus a voluntary caveat on the other. On the evidence that is public, there is no proof of wrongdoing about the data.

One more thing worth separating out, because it is easy to blur. Buckmaster's statement also describes a dispute over credit and authorship, including a proposal that his collaborator be dropped from a paper. That dispute is serious, it is contested, and it is not what this piece is about. Everything below concerns only the narrower question of data.

What there is, is something more uncomfortable.

## The problem is not theft. The problem is that nobody outside can check.

Set aside who is right about the mathematics. Look only at the information structure.

One party is in a position to go and find out what flowed through its systems: which logs existed, what was retained, what fed which training run, who had access to what and when. The other party, the customer, the person whose unpublished work was sitting in those sessions, sees almost none of that directly.

That gap is not a scandal. It is the normal, expected, by-design condition of using someone else's computer.

Enterprise contracts narrow it, and they are worth having. A large customer can get administrative logs, configurable retention, contractual commitments, private networking, and in some cases third-party audit reports. But all of those describe the perimeter. None of them lets you run the query yourself inside the provider's systems. When you want to know what happened to one specific session, the move available to you is to ask, and then to weigh the answer you get. Buckmaster asked. He got a partial answer.

This is what security people call an information asymmetry, and it is baked into the architecture, not into anyone's ethics.

## Opt-out fixes a policy problem, not a trust problem

Here is where most privacy discussions go wrong.

Somebody says "just turn off training." And that is genuinely useful advice. Consumer AI products offer training toggles. Business, Enterprise, and API tiers are excluded from training by default. OpenAI's own developer documentation states that "data sent to the OpenAI API is not used to train or improve OpenAI models (unless you explicitly opt in to share data with us)."

These are real protections. I am not waving them away.

But notice what they are: rules about what a company will do with data it already has.

The same OpenAI documentation says abuse-monitoring logs "may contain certain customer content, such as prompts and responses," and that these logs are "generated for all API feature usage and retained for up to 30 days" by default. The same page lists exceptions in both directions: a few endpoints keep no abuse-monitoring logs at all, and retention can run longer where law or harm-prevention requires it. Approved customers can apply for Zero Data Retention, and even then the docs note that some endpoints "may still store application state," and that images flagged by child-safety screening are "retained for manual review" regardless. The docs also point out that remote tool servers you connect have their own retention policies, which are not the model provider's to promise.

I am quoting the API rules as an illustration of how these systems are structured, not as a claim about Buckmaster's own sessions. Which product tier and which rules covered those, I do not know.

None of that is sinister. Every one of those mechanisms exists for a defensible reason: stopping abuse, debugging, keeping the product working, complying with law.

The point is simply this:

**"Not used for training" and "never processed, never stored, never touched" are different claims.** Opt-out gives you the first. Only architecture gives you the second.

So the sharp version of the argument is not "OpenAI cannot be trusted." It is:

> Opting out solves a training-policy problem. It does not remove the third-party from your trust model.

## What local AI actually changes

A model running on hardware you control has a different property, and it is not a better promise. It is the absence of a promise being needed.

Your prompt does not leave the machine. Your source tree is not uploaded into someone else's agent sandbox. Your unpublished theorem does not cross an organizational boundary. Your search index and your long-term memory stay on disk you own. There is no retention window to ask about, because there is no third-party system doing the retaining.

The strongest privacy control was never a checkbox. It is not generating the data transfer in the first place.

This is one of the oldest ideas in computer security: reduce the number of parties who have to be trusted. Every party you remove is a set of policies you no longer have to read, a set of logs you no longer have to wonder about, and a set of future policy changes that can no longer affect you.

Local AI removes one very large party.

## What local AI does not do, and I want to be honest about this

Removing a party is not the same as removing risk. If I only made the flattering half of the argument, I would be doing exactly the thing I am complaining about.

The word "local" is doing a lot of work, and it is often false in practice. An assistant that runs its model on your machine but calls a web search, a remote tool server, a package registry, or a hosted sandbox has already sent your context somewhere. Many tools marketed as local do exactly this. The boundary is the whole chain of things your prompt touches, not the place where the matrix multiplication happens.

The model file itself is a supply chain. You downloaded weights, a runtime, and a stack of dependencies from strangers. Any of them can phone home, and an update can change behavior after you stopped paying attention.

And your own machine is now the weakest link. An unencrypted laptop, an unattended screen, a cloud backup you forgot was running, a crash dump, a search index, a coworker with admin rights: none of these are hypothetical, and all of them were somebody else's problem when the data lived in a hardened data center. There is a real argument that a well-run provider protects data better than an individual researcher's laptop does.

So the honest claim is narrower than the slogan. Local inference gives you a stronger boundary against one specific risk, provider-side access and retention, and only if the whole toolchain is genuinely offline or you have checked what it talks to. It hands you a different set of duties in exchange.

## The best counterargument, and what I think it misses

Someone who works on these systems would answer roughly like this:

"You are comparing a consumer chat window against an idealized offline setup. That is not the real comparison. A serious enterprise deployment gives you no-training commitments in a contract, configurable retention, encryption, access governance, private networking, audit events, and an approved zero-retention mode. Meanwhile your local stack has weaker models, unverified weights, and a user who will misconfigure it. Trust is not binary, and a well-governed provider can be more trustworthy than you are."

That is a strong argument, and for most organizations most of the time it wins. I would use it myself.

What it does not answer is the specific case where the information is so valuable, or so time-sensitive, that even a small residual probability is unacceptable, and where you would want to be able to demonstrate afterward what happened rather than cite a policy. Contracts give you a remedy after the fact. They do not give you the ability to check. For a Millennium Prize proof, a patent filing before the priority date, or an unannounced acquisition, "we would have a legal claim" is a weaker position than "the information was never there."

## Not "local only." Hybrid, with a rule.

I am not going to pretend the frontier models are replaceable today. They are not. For hard problems, the capability gap is real and often worth paying for, including paying for it in trust.

Buckmaster himself used both Claude and Codex, paid OpenAI out of his own research funds, and says the collaboration between a mathematician and a model compressed a year of work into a month. That is the actual headline. The tools worked.

So the useful architecture is hybrid, and it comes with a rule you decide *before* you paste anything:

Run the routine and the confidential locally. Keep your private retrieval database and your persistent project memory on your own machine. Send a problem to a frontier cloud model when, and only when, the extra capability is worth moving that specific information across the boundary. And when you send it, send the minimum: the abstracted question, not the whole draft.

The question has quietly changed. For three years it was:

**Which model is smartest?**

It is now also:

**Which of my information should ever leave this machine?**

Most people using AI for confidential work have never explicitly answered the second one. Buckmaster had to answer it retroactively, in public, after the fact, with no ability to verify. That is a bad time to start thinking about it.

## The line worth remembering

> **"We don't train on your data" is a policy. Policies are written by people, and people can change them, reinterpret them, or carve out exceptions you will never see.**
>
> **"Your data never left your computer" is an architecture. Architecture does not need to be trusted. It just needs to be true.**

Whatever happened between Buckmaster, Alpöge, and OpenAI, the enduring lesson is not about any one company. It is that AI has moved inside the lab, inside the codebase, inside the deal room, and inside the legal file, months before the outside world sees any of it.

If the information is valuable enough that you would be upset to learn its exact path through someone else's infrastructure, the right move is not to read the privacy policy more carefully.

It is to not send it.

## Sources

- [Tristan Buckmaster, public statement (PDF, NYU Courant)](https://cims.nyu.edu/~tristanb/statement.pdf)
- [Hacker News discussion of the statement](https://news.ycombinator.com/item?id=49605915)
- [OpenAI's public response](https://x.com/OpenAI/status/2097375276384567642)
- [Axios: OpenAI's math solution overshadowed by credit controversy](https://www.axios.com/2026/09/08/openai-math-solution-navier-stokes-credit)
- [Fortune: OpenAI says it cracked Navier-Stokes](https://fortune.com/2026/09/08/openai-says-it-cracked-navier-stokes-math-grand-challenge-buckmaster-accusation-cheating-intimidation-tao-lament/)
- [OpenAI API data controls and retention](https://developers.openai.com/api/docs/guides/your-data)
- [OpenAI: how your data is used to improve model performance](https://help.openai.com/en/articles/5722486-how-your-data-is-used-to-improve-model-performance)
