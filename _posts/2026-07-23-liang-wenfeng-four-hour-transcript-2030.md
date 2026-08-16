---
title: 'Revisiting Liang Wenfeng''s Four-Hour Transcript From a 2030 Vantage Point'
date: 2026-07-23
permalink: /posts/2026/07/liang-wenfeng-four-hour-transcript-2030/
tags:
  - AI
  - DeepSeek
  - 梁文锋
  - LLM
  - '2030'
---

Original source | Tencent Tech; transcript edited | Gu Lingyu; original editors | Xu Qingyang, Su Yang; 2030 annotations and second edit | Koutian Wu

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

## Before reading Liang Wenfeng: establish a 2030 coordinate

By 2030, models will still get stronger, but simply selling model capability will get harder. Falling inference prices, open-source models catching up, and enterprises calling on multiple vendors at once will all make models easier to replace. Value will shift to what lies beyond the model: a company's own context, feedback formed from real results, workflows already embedded in the business, channels that reach customers, and the people and institutions willing to take responsibility when something goes wrong.

The deeper change is AI moving from "giving an answer" to "entering a system to get things done." It will read materials, call tools, update records, and hand an action off to the next system. Whether a single answer is fluent can't prove it works over the long term. The real dividing line is whether it can remember constraints, accept continued correction, keep evidence, and make fewer mistakes over months of operation.

This path is still bound by the physical world. Chips must be manufactured and packaged, data centers need land, cooling, and grid interconnection capacity, and electricity must travel through power plants, transformers, and transmission lines. A single inference that uses fewer resources can also be offset by more agents, longer tasks, and more frequent calls. Software capability spreads fast, but the infrastructure beneath it won't expand at the same speed.

So the main risk isn't that AI stays unintelligent, but that organizations plug automation into real processes faster than they can verify, halt, and assign accountability. An agent can execute errors in bulk within minutes, and can scatter responsibility among the model, the platform, the deployer, and the operator. Whoever can restrict permissions, spot anomalies, withdraw actions, and designate a final signatory is the one qualified to hand AI high-value tasks.

> Reading Liang Wenfeng with this 2030 coordinate in mind, what's truly worth asking isn't just "is he right," but: where will his technical route push value, which premises haven't yet held, and what signals over the next three years will prove or overturn these judgments.

According to Tencent Tech, DeepSeek completed its first external financing round since founding, exceeding 50 billion yuan, with Liang Wenfeng, Tencent, CATL, and others participating. The financing marks a reversal of Liang's earlier position of "no financing, no IPO, no commercialization," and has outsiders re-examining DeepSeek's commercialization path. The nearly four-hour investor communication subsequently released mainly covered organizational culture, open-source logic, technical route, and industry competition.

This piece uses the nearly-four-hour communication transcript obtained and collated by Tencent Tech as its base. Liang Wenfeng's remarks follow the original's topic classifications, 118 items in all, keeping the original intent as much as possible; this version adds item-by-item "2030 annotations" and does a second edit of the guide and interpretation layers.

> **How to read these annotations** The content below explains Liang Wenfeng's words using only the *LLM After the World 2030 Cross-Analysis Report* and the *LLM Application Opportunities Cross-Analysis Report*. LLM is the abbreviation for Large Language Model, called "large language model" in Chinese; DeepSeek is one such AI that can read and write text. Ordinary "2030 notes" clarify the original statement; "2030 core notes" are reserved only for judgments that truly determine the future landscape, and continue to unpack their causal chains, hidden premises, beneficiaries, failure conditions, and signals observable from 2027 to 2029. This piece does not verify whether the communication itself really happened.

01

Vision and restraint

1. When we set out to build this company, the original intent wasn't about how much money I'd end up making, reaching capital markets, going public, or any of that. The first few dozen people never thought this way; if they had, they wouldn't have come.

> **2030 note** The earliest joiners were betting on a long-term technical goal, not waiting for the company to IPO and pay out. This can screen for people willing to endure long-term failure, but it doesn't mean the company won't need to make money later. By 2030, a founding vision still has to become stable services and real results to leave value behind.

2. We came at this with enormous goodwill toward the world. We think this is useful for humanity, that this is something beyond money. The intent we started from, our vision, and the vision we've kept to this day, weren't shaped by maximizing commercial interests.

> **2030 note** Goodwill is an inner motive; outsiders can't see it, only its consequences can be seen. Whether ordinary people can afford it, whether a real person is handed over when AI answers wrongly, and whether it can be traced who approved an error afterwards, these are the standards checkable by 2030. Good intentions don't automatically equal safety.

3. Managing a big company doesn't rely on your rules and regulations, it relies on vision. A vision isn't a slogan hung on the wall; a vision is how you do things, not how you say things, that is, how you actually operate.

> **2030 note** A vision is like a compass, telling the team which direction to go. Rules are more like traffic regulations, dictating who can spend money, who can see information, and how to roll back after an error. A compass can't replace the brakes; the bigger a company gets, the more it needs both used together.

4. We have no organization, we're vision-driven, organized around a single vision. We don't operate on "I want to hit some KPI, there's no assessment"; there is only vision.

> **2030 core note** KPI is the abbreviation for Key Performance Indicator, that is, a standard set in advance to judge work by numbers. There's a hidden premise in Liang's approach: the team is small, its members are highly capable, trust each other, and already share a common judgment about "what research is worth doing." In such an environment, setting fewer metrics avoids researchers abandoning unpredictable breakthroughs in order to hit numbers.
>
> As people and AI agents multiply, the problem flips. A vision tells everyone where to go, but it can't tell an agent what materials it may see, how many chips a single experiment may spend, what counts as failure, or who halts it when it goes wrong. By 2030, truly advanced organizations won't simply be "without KPI"; they'll shift metrics from assessing busyness to checking task completion rate, error rate, reversibility, and resource cost. During 2027 to 2029, if DeepSeek begins publishing clearer evaluation, permission, and incident-handling mechanisms, it will mean it's turning a small team's tacit understanding into a scalable institution; if it still relies mainly on a few people reading each other's minds, vision-driven operation will become the bottleneck on scaling.

5. This vision isn't even written down; nothing was ever written out. This vision lives in how we do things and in our attitude toward the world.

> **2030 note** A few dozen people who have worked together a long time may know from a glance which things are off-limits. As people multiply, new employees and AI can't read that tacit understanding. By 2030, a company has to write it down, for example, that the payroll table can't be viewed, and that medical advice must be signed by a physician.

6. We don't have many other advantages. We have no special abilities, we're not richer than others, and it's not that our people are better than other companies' people. In fact we don't have that. When we founded the company two years ago, we had little money, few cards, no fame, and no pull; we were just a group of very ordinary people.

> **2030 note** Early success isn't necessarily because the people are smarter; it can also be because the team used its limited chips only on a few key experiments. Scrimping can narrow the gap, but it can't conjure up more chips and electricity out of nothing. By 2030, clever engineering methods and real resources still have to be counted together.

7. The more restrained you are, the easier it is to succeed, or at least that's been borne out so far, it's explainable so far. Otherwise there's no way to explain how we succeeded: we had no weapons, an extremely low starting point, very few resources, and our people were just a random group of ordinary people.

> **2030 note** Restraint here isn't "the fewer resources the more impressive"; it's betting on fewer routes. If ten projects each get a bit of your people, none may go deep. Focusing people and chips on the single most important problem improves the odds of success, but can also miss other opportunities if the bet is wrong.

8. AI is too big, the stakes are too big. We are very restrained; as long as we get it done, the eventual stakes will be enormous. Whatever portion you take, it's already huge, so there's no need at all to think about which part of the stakes to take or how; I don't think you need to think about it at all, because the stakes are big enough.

> **2030 note** This big business isn't one cake; it's a whole table of dishes. Some train models, some rent out the computers that run models, some put AI into office software, some make it handle insurance claims, and some just watch over a crowd of AIs so they don't run amok. Every layer can make money, but sticking in a chopstick casually doesn't mean you'll really eat.

9. Last spring festival we suddenly had lots of users, but we didn't chase keeping those users, monetizing off them, or grabbing this commercial value by cashing in on users. We didn't fight for users and didn't make money, but we tried hard to serve them well.

> **2030 note** When users suddenly multiply, serving them without crashes first and then thinking about how to charge wins trust. But many users doesn't mean the business is established. By 2030, people will care more about whether AI can remember their own affairs, finish tasks, and have someone handle errors after they happen.

10. We have no such thought as making the next super-app, competing with someone, becoming the next ByteDance, the next Tencent. Not at all. I think the AGI opportunity ahead is very large, and it will always be very large.

> **2030 core note** AGI is the abbreviation for Artificial General Intelligence, an AI whose goal is to handle many different mental tasks in one system. Behind Liang's rejection of the "next super-app" is a kind of industrial stratification: a few companies train general models, cloud and office platforms hold accounts, permissions, and distribution, and vertical companies wire models into the real processes of law, healthcare, customer service, and programming. A model can be very general, yet it can't simultaneously have every hospital's records permissions, every company's approval rules, and every industry's license to take responsibility.
>
> So in 2030, power doesn't belong only to "the smartest model"; it also belongs to those who control work entry points and result feedback. If DeepSeek only offers general capability, it will get enormous call volume but may leave the thicker profits to application companies that hold customers, processes, and responsibility. Conversely, if it later enters too many applications itself, it will fight the partners it wants to support today for the same customers. Over 2027 to 2029, the thing to watch isn't whether it builds a bigger chat window, but whether it becomes underlying capability that many different systems are willing to call and can conveniently replace.

11. Restraint is a strategy. Sometimes you give something up to trade for more other things. Not open-sourcing is the same; it can be regarded as our pressure, or as our concession.

> **2030 note** The original's "not open-sourcing" conflicts with insisting on open-sourcing several times later, possibly a transcription issue. Open source means making trained model files public for others to use. If "open sourcing" was intended here, what's surrendered is exclusivity, and what's gained is more people using it and helping improve it. If it really meant not open-sourcing, the logic is exactly reversed.

12. This restraint, as I understand it, can in the long run increase our odds of building AGI. When considering anything, I have no doubt AGI carries enormous commercial value. On that basis, my first priority isn't how to add a bit of share, how to take a bit more share; my first priority is how to increase my odds of success.

> **2030 note** This is a betting order: raise the chance of building general AI first, then think about splitting profit. It doesn't guarantee success by 2030. Even before the full goal is reached, AIs that can search materials, open software, and complete few-step tasks will enter real work first.

13. We have always been very restrained and don't want to be a rival to any major internet company or small business. I want to empower them, or help everyone do this thing, and hope to help everyone do this thing.

> **2030 note** The concrete division of labor is that DeepSeek supplies general models and other companies wire them into customer service, office, or hospital systems. It's a bit like a power plant that only supplies electricity while factories decide how to use it themselves. The analogy stops there: electricity doesn't fabricate wrong answers, but models do, so partners still have to check results.

14. I think maintaining this attitude hasn't actually made us take less of anything; it's not because of open source, goodwill, or helping others that we ended up taking less. If anything it may be a plus. This seems counterintuitive, but it's true.

> **2030 core note** After open-sourcing, many companies can offer the same model and undercut each other, so models will move faster from scarce product to common commodity. On the surface, DeepSeek gave up exclusive pricing; deeper, it's compressing all model vendors' pricing power so more developers build software, adapt, and accumulate usage habits around its model. Open source is therefore both a concession and a way to change the battlefield: model files get cheaper, while low-cost operation, stable service, update speed, and ecosystem compatibility become more valuable.
>
> Who benefits and who is hurt is also clear. Application companies and customers get more choice, and closed models' high margins come under pressure; DeepSeek, meanwhile, may use scale, standards, and engineering efficiency to earn back influence. But "didn't take less of anything" can't be proven, because no one can see the alternative history of not open-sourcing. Through 2027 to 2029, three signals can be watched: whether third-party deployment volume keeps rising, whether the official service can still retain paying customers on cost and stability, and whether application companies can conveniently switch to another model. If the first two are strong and the third is also strong, open source enlarged the market but didn't give DeepSeek firm customer lock-in.

15. We aim at AGI, but we've been doing commercialization all along, which is how we have C-end users and B-end revenue. From historical experience, this strategy works.

> **2030 note** The C in C-end stands for Consumer, ordinary consumers. The B in B-end stands for Business, enterprise customers. Ordinary users expose the most common errors; enterprises push models to face internal materials, approvals, and accountability, and also bring revenue. Research goals and commercialization can feed each other.

02

AGI roadmap

16. If you can describe a problem very clearly, give it complete context and instructions, it already surpasses humans. But there's a definition here, a premise: you give it complete context and complete instructions.

> **2030 note** Context is the background material needed to complete a task. In reality it's scattered across email, meetings, databases, past decisions, and the heads of veteran employees, and people themselves often can't state the goal clearly. By 2030, a genuinely good system shouldn't wait for a perfect instruction; it should look up materials within its permissions, cite sources, tell people what's missing, and write results back into business systems. The difficulty here is no longer conversational skill but who holds a business's data entry points and permissions.

17. AI can't replace your employees. But if AI had continuous learning, came into your company and studied for two months like an employee, it could replace everyone under heaven, which is why we're still a step away, missing continuous learning.

> **2030 core note** Continuous learning means AI corrected today remembers the fix tomorrow for similar tasks. Liang pins "whether it can replace employees" on this single capability, but jobs won't disappear as a whole because of one technical switch. Work will first be cut into tasks like collecting, drafting, verifying, executing, and signing; the parts that are easy to verify and whose errors are reversible go to AI first, while high-risk judgment and final responsibility stay with humans.
>
> What truly changes a company isn't just that a model learns, but whether it can learn "how this company does things." A general model can know what insurance is, but not which claims a particular company has rejected in the past or which exceptions must be escalated to a manager. As such correction records accumulate, they get harder for latecomers to copy, and value shifts from the general model to the organization's own data and processes. The failure conditions are just as clear: if the model learns errors, mixes different customers' memories, or employees can't find out why it changed, continuous learning can turn one error into a long-term bad habit. From 2027 to 2029, watch whether enterprises really let AI keep audited experience across months, and whether that experience can be viewed, deleted, and rolled back, rather than only looking at demos where it "remembered me."

18. AI development can be understood as a ladder. Last year's rung was chain of thought. Because we found that, through chain of thought, intelligence can reach a higher level.

> **2030 note** Chain of Thought, abbreviated CoT, is getting the model to break a hard problem into steps. Even with steps written out fully, the answer can still be wrong. In real work, databases, code tests, and raw evidence are more reliable than a passage of clever-looking reasoning.

19. This year's rung is Agent. We found that with the Agent method, even more things can be done, its capability range is larger, and its intelligence ceiling is higher. Agents use CoT, and CoT uses the previous rung, which is the language model; so no step has been wasted.

> **2030 core note** Agent, often called "intelligent agent" in Chinese, refers to AI that doesn't just answer questions but breaks down steps, opens software, and does things itself. The real change isn't a few more buttons in the chat window; it's a new unit of execution appearing in the company: one that can search materials in parallel, edit files, run tests, and write back to systems. Management questions change from "how many people does this position need" to "how many people, how many agents, what permissions, and how many approval checkpoints does this goal need."
>
> The higher an agent's capability ceiling, the larger its radius of error. Getting one sentence wrong might only be a bad experience; getting an automatic refund, a code change, or a sent file wrong becomes real loss. So the enterprise bottleneck shifts from "whether the model can do it" to "whether the company dares to let it do it": does it have an independent identity, is it given only the materials and buttons needed to complete the task, and are there budget caps, action logs, human escalation, and one-click rollback? Through 2027 to 2029, the strong signal is an agent becoming the default executor of a process, able to stop and hand off to a human automatically on anomaly; employees still copy-pasting it alongside an old process is only a tool upgrade, not yet an organizational reconfiguration.

20. After Agent, the problem we think should be solved is continuous learning: how to make the model keep learning, rather than needing a very strong training session. It should be able, like a person, to do continuous learning over a long period.

> **2030 core note** If a customer-service agent messes up a refund rule today and a human corrects it, tomorrow it should automatically apply the fix to similar orders; that's what it looks like for an employee to grow. But continuous learning isn't simply stuffing every conversation into memory. The system must judge whose corrections are trustworthy, which category of customers a rule applies to, when it expires, and whether new experience breaks old capabilities; otherwise one malicious user or one misjudgment can pollute everything that comes after.
>
> The commercial key is the "feedback flywheel." The more an agent does, the more real results the company gets; results, once reviewed by humans, make it understand the company better; the more reliable it is, the more the company dares to hand it more tasks. Once this loop turns, the moat is no longer a model anyone can download, but the tasks, exceptions, corrections, and final results accumulated over years. Through 2027 to 2029, the real progress signal isn't that memory gets longer, but whether similar errors keep falling, whether old rules get version records, and whether different companies' experience is strictly isolated.

21. After continuous learning, we may reach a singularity. This singularity is that, once the model can keep learning, it can already do everything a human can. It can develop its own next version, research by itself, then develop its next version, develop even more advanced AI models.

> **2030 core note** The singularity here means AI starts reading papers, writing code, and running experiments on its own, then uses the results to improve the next version of AI, making research speed roll up. Yet this causal chain skips several levels: remembering experience isn't the same as posing a worthwhile research question; writing experimental code isn't the same as having correct test standards; and one local improvement isn't the same as safely modifying a whole training system. Continuous learning may be necessary, but it isn't sufficient for "doing everything a human can."
>
> What's more likely is gradual self-acceleration: AI first takes over material sorting and routine experiments while humans choose directions, allocate compute, inspect anomalies, and decide whether to adopt results. It first expands a few elite researchers' capability rather than immediately removing humans from research. A strong signal to watch from 2027 to 2029 is whether new methods proposed by AI can be independently reproduced and complete several rounds of valid experiments in succession without step-by-step human direction; a weak signal is only that it can write research plans or edit a section of training code. Treating a weak signal as a singularity would overestimate speed and undervalue the value of verification and governance.

22. This singularity isn't a singularity; it's also a gradual process. This process may also be a fairly long gradient, not a sudden change. But out of habit, we all think of it as a singularity.

> **2030 note** For ordinary people, change is more likely to come as batches of small tasks handed to AI little by little. Today fewer first drafts, next year less material searching, and later one person supervising several agents at once. Job titles may stay the same while what's done inside them day to day has already changed.

23. This is our speculation, our sense of the timeline: first solve learning-to-learn, then reach the intelligence singularity, the self-iterating singularity, and only then embodied intelligence. After embodied intelligence, it steps into the real world, can do chores for you, and can provide elderly care.

> **2030 note** Embodied intelligence means AI has a machine body and can move things, do chores, or care for the elderly in the real world. The two reports only extrapolated screen-based agents, predicting they enter programming, customer service, and company operations first; they did not predict which year household robots mature.

24. If we first solve continuous learning, then the self-iterating singularity, then embodied intelligence, this path becomes easy. Because later on, you can use the earlier technologies to help develop the later ones.

> **2030 note** The earlier step can indeed help the later one; agents can write robot code, filter materials, and analyze experiments. But help isn't automatic solution. Each round of testing still uses chips and electricity, robots still have to prove in real environments they won't run amok, and the earlier AI can also carry its errors into the next step.

25. We only do the main line of AGI. The AI field is broad, and there are many things we think aren't on this main line, such as 3D and video generation; I think they may not have much to do with the main line of intelligence, and we won't do them.

> **2030 note** 3D is content that can express length, width, and height. DeepSeek not doing 3D and video is drawing a boundary for the company, not saying these businesses have no value. By 2030, one company can focus on building general models while another uses that model to make videos or design products, each earning different money.

26. Video generation was very hot as soon as it came out, as if this was a must-do, as if you weren't an AI company if you didn't do it. So I found it strange; if you really think about it, it has nothing to do with the intelligence roadmap.

> **2030 note** Video generation proves AI can produce one kind of content; it doesn't directly prove it can remember experience long-term, plan on its own, and complete complex tasks. It may well become a great creative product. Being hot commercially and being a key rung toward general AI are two different questions.

27. Commercially, it's a good business, it's a good business commercially. But it has nothing to do with intelligence. We won't do it because it's a good business; we'll only do it if it's something on the intelligence roadmap.

> **2030 note** This separates company mission from money-making opportunities. DeepSeek only does what it judges to be on its intelligence main line; that doesn't mean video, design, or healthcare applications won't grow big companies. What's genuinely hard for the latter to copy is understanding industry rules, integrating with customer systems, and putting results into customers' hands.

28. From our judgment, world models and intelligence aren't yet what matters most at this stage. The most important thing is AI training, and how to solve continuous learning after AI training. That's our company's judgment; of course every company's judgment is different.

> **2030 note** A world model lets AI simulate in its head how reality will change, for example, which way a cup will tip after you push it. DeepSeek chooses to do continuous learning first and this kind of simulation second; it's a bet on research sequencing. The two reports show long-term correction records will be more valuable, but can't prove this technical route will definitely win.

29. We now quite believe in a narrative: AI can accelerate AI research. That is, it's not linear, because you can use AI to accelerate your own research, so later it may be nonlinear.

> **2030 core note** The complete chain of nonlinear acceleration is: AI shortens the time to read papers, write code, and analyze failures, so the same group of researchers can run more experiments; more experiments produce more results, and the results are used to improve the next generation of AI; stronger AI further shortens the research cycle. What's genuinely amplified isn't the abstract number "smarts" but the quantity of reliably verified experiments per unit of time.
>
> This also explains why compute, evaluation, and human judgment won't automatically lose value. If AI proposes ten times more approaches but lacks ten times more chips to run them, the bottleneck moves to computing resources; if experiments only chase the wrong score, it will steer the whole research direction astray faster; if no one independently rechecks results, speed is just manufacturing more plausible-looking noise. Through 2027 to 2029, watch whether the cycle from idea to reproducible experiment visibly shortens and whether the share of AI-proposed suggestions that actually enter later models rises, rather than merely counting how much code was generated.

30. I think embodied intelligence definitely needs to come in, ultimately embodied. Because for a normal person, their need isn't a computer, right? Normal people eat, drink, play, and live; they don't need a computer. What they need is, so they still need embodied intelligence to solve concrete labor needs.

> **2030 note** The original sentence is clearly missing a section after "what they need is," seeming like a transcription gap. What's certain is that Liang separated screen-based information work from real-world physical labor. The two reports only predict change for the former through 2030 and give no timeline for household robots.

31. What do we hope AGI can do? It can help me iterate the next version of the model; help me iterate the next version of the model, as it were. If we have embodied intelligence, what we hope it does is also this, let it iterate the next version of embodied intelligence, let it make the next version of the robot.

> **2030 note** The original says "help me iterate the next version of the model" twice in a row, also looking like transcription duplication. What it wants to express is two rounds of self-improvement: AI helps build the next generation of AI, and robots help design the next generation of robots. Humans still have to decide what to change, how to test, and whether dangerous changes can be released.

32. The core capability of the next-generation model must include continuous learning; only then can it be called the next-generation model. Before that, all we can do is costs, then better results and faster speed. But for a big breakthrough, it should have continuous learning.

> **2030 core note** Only getting faster and cheaper is swapping in a better general-purpose tool, and competitors' new models will catch up quickly. Continuous learning, though, may turn the tool into a "digital employee that understands this company better the more it works." Commercial value therefore shifts: base models provide initial capability, while the enterprise's own historical tasks, correction records, approval habits, and result data determine whether it later becomes competent.
>
> There's also an easily overlooked issue of power here. If long-term memory is held by the model vendor, switching models is like making an employee who knows the company for years lose his memory, giving the vendor strong lock-in; if memory stays in the customer's own system in open format, the model itself remains replaceable and profits flow more to the platforms managing data, permissions, and workflows. Through 2027 to 2029, whether continuous learning truly constitutes a breakthrough depends on whether it reduces similar errors over long time spans, can explain what it learned, and whether customers can migrate with their own "experience archive" to another model.

33. Today's Agent capability is limited because it can't continuously learn; it can't effectively continuously learn. If we can finish continuous learning first, AI's capability will be very strong, and it can greatly improve the efficiency of our own research.

> **2030 note** An agent that gets it wrong today may well get it wrong again tomorrow; if it can remember fixes over the long term, research speeds up a lot. But continuous learning has a governance paradox: an agent that can't learn repeats mistakes, while an agent that learns but can't be audited may learn bad habits increasingly firmly. Every thing it learned, on whose authority, from which version the change started, and how to undo it, must be findable by humans.

34. Once continuous learning is built first, general intelligence may become easy; using it makes it easy. This is a result we'd rather see, it saves us effort and makes us relaxed. Otherwise, to build general intelligence manually now is tiring, hard, data-intensive, and labor-intensive work with poor cost-performance.

> **2030 note** Continuous learning may reduce the manual work of organizing materials and repeatedly tuning models, but it isn't a guarantee of general AI. AI can still learn wrong, still spends chips and electricity, and still needs humans to set the goal. Liang saying it will be easy is a hope, not proven completion.

03

Team and talent

35. The lesson from our earlier experience is that the AGI vision is very powerful. This talent advantage isn't that my people are smarter than his; it's how I organize these people, how I motivate them, and then how they collaborate.

> **2030 note** Many smart people don't automatically make a strong team. If one researcher spots a problem, an engineer can immediately fix the code, and a product person can bring back errors users hit, only then does knowledge become progress. By 2030, you also have to assign tasks to agents, check their results, and step in when they go wrong.

36. Gathering smart people together isn't magic; they don't naturally collaborate and naturally become passionate about charging at a goal and completing it, which is why you need a vision.

> **2030 note** A shared goal is like a map, letting research, engineering, and product know what to do first and what to give up. By 2030, agents can do many things at once; if the goal is vague, they'll just be busier working at cross-purposes. The vision has to land as two clear questions: what to do, and what counts as done.

37. Our biggest core interest is maintaining team stability. This is our biggest core interest, which can even be regarded as our only core interest. As long as I can maintain team stability, I will definitely get it done, definitely build AGI, that simple.

> **2030 note** Core team staying keeps failure experience and working tacit knowledge that isn't written in documents, which are harder to copy than a model file. But team stability only raises the odds of success, not a guarantee. Wrong direction, insufficient chips, or results that can't be checked can still stall things.

38. Money definitely isn't a problem, resources aren't a problem, and the other factors are easy to obtain. For us, there's only one core interest, one thing that can't be conceded: we must maintain team stability.

> **2030 note** Money can buy chips but can't buy back the tacit understanding a group forms through years of trial and error; that's the part of this statement that holds. But read alongside the later "compute is the biggest bottleneck," resources are clearly still a problem. Team and compute aren't an either-or; lacking either side slows things down.

39. This is also a very big challenge we face, or rather, I think it's the biggest risk. Of course, this risk was substantially alleviated by our recent financing. Because everyone got quite a lot of options, with fairly large amounts.

> **2030 note** Options are a right a company gives employees to acquire shares at an agreed price once agreed conditions are met. The more the company is worth, the more money the shares may yield, giving employees one more reason to stay for that payoff. But the company can also fail, and money can't automatically buy collaboration and judgment.

40. On team stability, as long as the most important, oldest employees are stable, the others aren't very likely to leave. Even if the others have fewer options and lower income, they won't leave. Because they're not all in it for money; everyone hopes to do this in an environment that can build AGI.

> **2030 note** If senior employees stay, others believe the direction hasn't changed and can keep learning unrecorded experience from them. But a company can't rely on a few people as living dictionaries forever. By 2030, these judgments have to become experimental records, inspection standards, and operating steps; otherwise one person's departure creates a gap.

41. Everything else is a matter of time; at most it makes us half a year, a year late, but it won't mean we can't build it. We certainly don't lack money, certainly don't lack resources; in fact none of these are lacking.

> **2030 note** This is strong confidence rather than a proven result. Wrong direction, chips that never come, or a system that keeps making unacceptable errors aren't just half a year late; they may force the company to change route.

42. The gap between us and America is mainly in resources, and in people it's not big. In people there's almost no gap, because they're the same people, possibly Chinese. When Chinese go abroad, some stay domestic, some stay abroad, some go abroad; it's not that the smart ones went abroad. No.

> **2030 note** How smart someone is and how many chances they get to try by doing are two different things. With the same researchers, one side gets to run experiments repeatedly while the other always queues for chips; years later the accumulated experience naturally widens the gap.

43. Talent isn't the bottleneck; resources are the biggest bottleneck. Resources first affect talent development, because with little compute we can run fewer experiments, so overall our talent lags America. The talent gap is essentially a compute gap.

> **2030 core note** New people don't grow only by reading papers; they also have to run experiments into the ground with their own hands, find the cause, and start over. Compute is therefore not just production equipment but a training ground for talent: teams with more chips can try more routes in parallel and distinguish more quickly which intuitions are reliable; successes and failures then settle into the next generation of researchers' experience, so the resource gap keeps being amplified through talent development.
>
> AI-assisted research may narrow part of the gap: it can write routine code and filter obviously wrong approaches, putting limited compute on more worthwhile experiments; but it can also widen the gap, because teams with more chips can let more agents explore in parallel. What really determines the catch-up speed is "how much verified new knowledge each unit of compute produces," not just the total chip count. From 2027 to 2029, if resource-poor teams can keep producing near-frontier models at lower training and inference cost, engineering efficiency is offsetting scale; if the leading side's experiment cycles instead keep shortening, resources will compound through learning speed.

44. The shortage of AI talent is also temporary, and we've already seen it substantially eased. Because AI people really aren't scarce; every company will train people quickly, and training people is fast.

> **2030 note** People who use off-the-shelf models may soon become as common as people who use a computer today. What's genuinely rare is another kind of person: those who can ask new questions, design ways to check answers, and handle the strange situations that rules don't cover, which can't be learned in a few days of class.

45. Domestically there are too many companies doing models now, too many. America may have three; China has too many doing foundation models. In the end, definitely not that many people are needed to do foundation models; it will definitely converge.

> **2030 note** Training the most frontier general models burns too much money and needs too many chips, so the truly long-term participants may shrink. But available models won't shrink to just a few: the open-source route of public model files, models running only locally, and companies focused on specific tasks like contracts and insurance will still be numerous.

46. Our company management is actually two lines: one from top to bottom, one from bottom to top. Bottom-up means everyone does what they want, on their own, with no one managing them and no KPIs.

> **2030 note** The top tells everyone the destination, and researchers find their own route. AI can try more ideas in parallel, but how many chips each experiment can spend, which internal materials can be seen, and when it must stop still have to be specified in advance.

47. Generally we want employees to have half their time unscheduled, doing whatever they want. This is a research scope that lets them explore on their own, exploring what they think is important, with no preconditions.

> **2030 note** Setting aside half the time free is a bet on questions whose answers aren't yet known. Most attempts will fail; a few may open new directions. Later one researcher can let several AIs try ideas simultaneously, but how much compute was spent and why it failed must still be recorded.

48. We generally don't work overtime either. Overtime has two reasons. The first is that doing research requires a fairly relaxed environment. If you force it tightly, you can't do research. Because you have to have the interest yourself and think about these questions in your own time, you can only explore in a fairly relaxed environment.

> **2030 note** The hardest part of research is often finding the right question to ask, not typing a few more hours. AI can search materials, write drafts, and run routine experiments; the time people save should be spent designing experiments and checking whether the answers are right.

49. The second is that we are very focused. Being very focused means we have to do very few things. If I have fewer things to do, I don't need to work overtime. This is consistent with the earlier restraint.

> **2030 note** Focus isn't accelerating all ten projects; it's simply not doing nine of them. The same goes for application companies: first make one small task in contract review or insurance claims fully reliable, then expand slowly along the steps customers actually take every day.

50. Our company as a whole is built on consensus; I'm not saying I alone decide everything, but I seek consensus. My authority and influence within the company are built on consensus.

> **2030 note** This kind of authority comes from people genuinely agreeing on a judgment, not a boss imposing it by position. Research direction can be discussed, but once AI is already refunding customers, changing code, or sending messages for the company, someone must be able to press stop, and someone must answer for errors.

51. This decision mechanism is a consensus-seeking mechanism. It's not that I can push something forward; it must be consensus before I can push it through, and only then will I push it.

> **2030 note** Discussing until people genuinely agree reduces the problem of agreeing in words but objecting in hearts. But with more people, waiting for everyone to nod becomes slow. By 2030, the big direction can be set together, while small daily decisions still have to be made by a designated person.

52. As people increase, we'll make this adjustment. We probably have to make it right away, because I'm already making it. Without making this adjustment, a lot of things can't move forward. Indeed, many departments should have organizational structure.

> **2030 core note** This sentence is the most important self-correction in the whole organizational narrative: a few dozen people can form consensus through trust and the founder's direct influence, but with several hundred people, information gaps, waiting-for-decisions, and blurred accountability appear. Organizational structure isn't the opposite of vision; it's the machine that translates vision into "who has the authority to decide what."
>
> By 2030, this problem gets sharper with agents. One slow person with limited permissions normally affects only a few things on error; a crowd of agents can simultaneously read materials, change code, send messages, and execute transactions, amplifying vague authority at high speed. What truly needs building is a control plane: each agent's identity, accessible materials, budget, approval checkpoints, action logs, pause, and rollback must all be inspectable. If, from 2027 to 2029, enterprises start managing agents the way they manage employee accounts, and treat incident rates and recovery time as core metrics, the organization is genuinely changing; if they only buy a few more chat accounts, productivity gains will stay piecemeal.

04

Compute and resources

53. How many cards do we need? Right now, definitely the more the better. Within what we can afford, definitely the more cards the better, that's beyond doubt. So our current strategy is, at a reasonable price, buy as many cards as we can.

> **2030 core note** The "cards" here are the computing chips for training and running AI. "The more the better" reveals the physical base of model competition: algorithms are written on a screen, but capability growth must pass through chips, packaging, machine rooms, cooling, the grid, and long-term capital spending. Money can buy these resources, but it can't make short-supply chips or grid power that can't yet be interconnected appear instantly, which is why there's a long construction chain between the financing amount and usable compute.
>
> By 2030, competition also expands from "who buys the most cards" to "who makes the whole system do the most useful work per kilowatt-hour." A single inference becoming cheaper doesn't guarantee total electricity falls, because the lower the price, the longer and more often agents may run, try multiple rounds, and enter more tasks. The beneficiaries aren't just model companies, but chips, data centers, electricity, and regions that can quickly build infrastructure; resource-poor teams depend more on algorithmic efficiency and open-source supply. From 2027 to 2029, three signals beyond training scale can be observed: total energy consumption per complete task, machine-room delivery time, and whether compute begins to be constrained by the grid rather than the chips themselves.

54. In fact, spending all this money is not easy at all; you can't buy that many cards, they're hard to buy and the price is also high, and you can't pay an extremely high price; you have to ensure the price is reasonable. If we could spend twenty billion this year, our procurement department would have done an awesome job.

> **2030 note** Raising money doesn't mean more usable compute appears the next day. Chips wait for factories to produce them, machine rooms must be built, and cooling and the grid must be connected; any one link's delay leaves expensive equipment idle. By 2030, being able to buy, build, interconnect, and deliver a whole system on time is itself a model company's competitiveness.

55. The biggest gap between us and America is in resources. On the compute side, one aspect is that cards aren't available domestically, and another is that our capital investment is less than America's. We're far behind on capital investment, and talent salaries take up only a small share. You see they offer salaries of one hundred million dollars, but when you count it up, talent salaries are still a small share; the big head is compute.

> **2030 note** Star researchers' salaries are eye-catching, but in a company's total ledger, tens of thousands of chips, machine rooms, and electricity bills are often larger. Compute determines how many times you can try; researchers determine whether those experiments are worth doing, and neither side can be missing.

56. Every difference we see, including talent differences, model capability differences, and application differences, can be regarded as resulting from compute resource differences.

> **2030 note** Attributing every gap to compute is overreaching. Compute determines experiment counts and model capability ceilings, but it can't automatically make a legal AI find the right evidence, or decide whether a doctor dares to sign on results. Model-layer gaps may be mainly resource-driven, but application-layer gaps also come from real materials, process restructuring, inspection steps, customer trust, and responsible parties; this also forms a boundary with article 43's "talent gap comes from compute."

57. The gap between us and America might be twelve months behind, twelve to eighteen months, or six to twelve months. In short, two years behind, and we did it with a twentieth of America's compute.

> **2030 note** This passage says six to twelve months, twelve to eighteen months, and two years at once; the three metrics don't match and can't be used for precise catch-up dates. What can be read is only a rough picture: a Chinese team used far less compute and produced near-comparable capability somewhat later. Exactly how much later, even this passage itself can't reliably say.

58. This narrative is being one to two years behind but using a twentieth of its compute. In the future we want to rewrite this narrative: we use a fraction of its compute while shrinking the time gap to six months, three months. I think that's a goal.

> **2030 note** The goal is actually two things: get more chips on one side, raising from a twentieth of the competitor's to a fraction, and shrink the catch-up period to three to six months on the other. If we still spend less than the competitor yet produce comparable capability, more companies can afford it.

59. We believe in Scaling; for sure, the bigger the better, unlocking more capabilities. What stops our Scaling is actually compute; it's not that we don't want to Scaling, it's that we don't have that much compute to do this Scaling.

> **2030 core note** Scaling is scaling up, here meaning feeding the model more data, making it bigger, and letting more chips train longer. Liang believes scale will unlock new capabilities, which explains why foundation-model companies still invest enormous compute; but "model capability keeps rising" and "economic value rises at the same rate" are two different curves. A model scoring higher on exams doesn't mean it can already read enterprise materials, act within permissions, roll back after errors, or that customers will pay much more for a marginal gain.
>
> The beneficiaries of Scaling are layered. The most frontier experiments need huge resources, possibly concentrating a few model companies; once capability spreads via API or open source, it lets masses of application companies get formerly expensive intelligence cheaply. So the more concentrated upstream is, the more prosperous downstream may become. From 2027 to 2029, judging whether Scaling is still the main line can't rely only on model size; watch whether added compute keeps unlocking new tasks that weren't possible, whether unit cost per complete task falls, and how long a capability lead lasts. If a lead is quickly caught up, Scaling still has technical value but may not create durable pricing power.

60. We train such a large model not because I think such a large model is enough, but because I happen to have this many resources. I calculate based on my resources how large a model I can accept and train; that's how it's calculated, not that this model size is enough.

> **2030 note** How big the model is is worked out backward from the chips and budget on hand, not because science has proven this size is enough. Designing more efficiently lets the same chip count train a larger model, or answer more people at once.

61. When Silicon Valley says Scaling has hit its ceiling, that's for Silicon Valley; for Chinese people, we're still far from there, we simply haven't Scaled to that degree. This Scaling includes data Scaling, model-scale Scaling, then training cost.

> **2030 note** Silicon Valley finding continued scaling slowing doesn't mean resource-poor teams have exhausted this path. But piling on chips isn't a universal answer either. Even if AI gets better at answering, it still has to read a company's real materials, be caught when it errs, and have someone accountable.

05

Domestic chips and ecosystem

62. NVIDIA CUDA's moat is collapsing fast. On one hand there's now AI, and with AI it's much easier to build this ecosystem than before, because AI can write code.

> **2030 note** CUDA is the abbreviation for Compute Unified Device Architecture; you can think of it as NVIDIA's graphics-card toolbox, allowing programmers to tell chips how to compute. AI can help engineers port old programs to new chips, but tools, tutorials, and years of usage habits won't move over overnight.

63. The computing-card market is already bigger than the gaming-card market, so there's no reason these two need to stay coupled. The current trend is that they won't be coupled anymore. Specialized chips, whether Huawei's or NVIDIA's own, will all be specialized chips later, not the old ones.

> **2030 note** Gaming cards both render game graphics and do computing. Once the AI market is big enough, vendors can build chips that serve only model learning and answering, then link many chips together. By 2030, what everyone compares is how much one whole machine can do per hour and how much electricity it uses.

64. Domestic AI chip substitution now has a historic opportunity. We believe that within the next year we'll see one thing verified: the domestic chip ecosystem has no problem at all. It was previously thought to have problems, thought unusable and hard to use, but I think within the next year we can reverse this perception, or reverse it with facts.

> **2030 note** The ecosystem here isn't just the chip itself; it includes the software, tools, tutorials, and engineers who can fix problems that make the chip work. The original doesn't give the communication date, so "the next year" can't be directly converted to a specific year. Being usable also doesn't mean speed, stability, and user experience have all closed the gap.

65. Domestic AI chip hardware and ecosystem both have no problem; the only problem is insufficient production capacity. In adapting domestic cards there's no obstacle; NVIDIA can't block it. If we were in a normal business environment where I could buy NVIDIA cards, domestic substitution would be hard; but when NVIDIA cards can't be bought, everyone is forced to use domestic chips.

> **2030 core note** Unable to buy imported chips, teams have to use domestic ones. Forced adoption starts a "fix it as you use it" loop: more users, real training exposes more problems; engineers fix compilers, communications, and tools; better software attracts more users. The ecosystem isn't complete first and then used; it grows out of masses of failure, adaptation, and accumulated documentation. The restriction itself may therefore speed up domestic ecosystem maturation.
>
> But "it can run" is only the first gate; it doesn't mean equal substitution commercially. Customers ultimately have to calculate how many machines, how much electricity, and how many engineers of debugging one equivalent training run needs, whether it faults midway, and whether enough units can be bought on time. If four cards do the work of one, production capacity, electricity, and machine rooms may eat up the software gains. From 2027 to 2029, the most convincing signals aren't a single demo or peak parameter, but whether mainstream models can train on domestic stacks over the long term, whether different frameworks migrate with little code change, whether the total cost of buying and running long-term is close, and whether supply keeps up. Ecosystem, single-card performance, and capacity must all hold at once; missing any one means it's not complete substitution.

66. When V3 was trained, it still used NVIDIA's cards, but no longer used NVIDIA's ecosystem. V3 used NVIDIA's cards but not NVIDIA's ecosystem; instead we first wrote a high-level compiler called TileLang, and completed everything else on top of the TileLang ecosystem, so we already barely depend on NVIDIA's ecosystem.

> **2030 note** V3 is a generation of DeepSeek's models. In training it, the machines still held NVIDIA chips, but TileLang acts like an interpreter, translating the model's computational needs into instructions chips understand. If this interpreter can adapt to multiple chips, switching vendors later won't require rewriting programs from scratch.

67. I'm fairly optimistic about domestic compute. I think on this point NVIDIA is digging its own grave. Huawei's supernodes, the Huawei 950 supernode, can fully replace NVIDIA's GB200 and GB300 in performance and price.

> **2030 note** A supernode links many chips and high-speed networks into one big computer. GB200 and GB300 are NVIDIA's data-center computing systems. Whether the two big machines substitute each other depends on how fast the same task runs, how much it costs, how much electricity it uses, and how often it faults, not just the highest number in the ad.

68. Four Huawei cards equal one NVIDIA card.

> **2030 note** This sentence actually admits a single domestic chip may be considerably slower. But the original doesn't say which two chips are compared, what task, or how much electricity, so the four-to-one can't be applied everywhere. Adding more cards can compensate for speed but also takes more machine-room space and electricity.

69. On the chip gap between us and America, I think the ecosystem won't have a gap anymore, but in chips it's four times plus two years.

> **2030 note** This sentence wants to separate two things: complementary software may close the gap first, while chips themselves are still slower and later. But the objects of "four times" and "two years" aren't specified, and the two can't be added up. By 2030, use the same task to compare speed, cost, electricity, and deliverable volume.

70. We mainly cooperate with Huawei right now. Huawei adapts themselves, but we participate in the ecosystem ourselves and get deeply involved in Huawei. Huawei's problem is still insufficient capacity.

> **2030 note** When DeepSeek really trains on Huawei chips, it will hit stalling, errors, and slowness, then hand those problems to Huawei to fix. Such back-and-forth trial use is more useful than merely claiming compatibility on paper. But once the software is fixed, there also have to be enough machines to hand to customers.

71. I don't quite believe that five years from now we'll still be stuck on the capacity problem. Right now we're certainly stuck on capacity; this year, next year, and the year after, I think we may still be stuck on capacity, but in five years, I think maybe not; I'm still fairly optimistic.

> **2030 note** Five years later must be counted from the actual speaking date, but the article doesn't give the communication date. If we take only the two reports' July 2026 as reference, five years later is near 2031, which can't be read as resolved by 2030 for sure. After chips increase, electricity and machine rooms may become the next threshold.

06

Competitive landscape and industry judgment

72. The gap in final model performance across the various players should be comprehensive. To compare model performance, you definitely have to compare at the same cost for it to be meaningful. Because if you compare two cars, you also compare cars at the same price.

> **2030 core note** A fair comparison isn't how many cents one answer costs, but how much a matter costs in total to complete reliably. Complete cost at least includes model calls, runtime, integrating internal systems, human inspection, failure retries, and the payouts and trust loss after errors. AI that is cheap but often reworks may be more expensive than a system that costs more but completes in one pass; likewise, the smartest model, if it must be line-checked sentence by sentence by senior experts, may have no economic advantage.
>
> This framing changes the 2030 competitive ranking. Foundation-model companies habitually compare token prices and exam scores; enterprises should compare how much each "qualified contract," "correctly resolved customer-service case," or "safe release" costs. Value moves from generating text to completing results, proving evidence, and handling exceptions. If, from 2027 to 2029, purchasing contracts start pricing by task success rate, human-handoff rate, incident cost, and outcome rather than only by seats or tokens, the market will have shifted from buying models to buying production capability.

73. Is Anthropic now surpassing OpenAI, is that long-term? I don't think that's long-term; it's certainly temporary. OpenAI and Google will likely still alternate climbing in the future.

> **2030 core note** This is Liang's guess about company rankings, not a technical law. A leaderboard squeezes competition into one line, but the real market has several different axes: OpenAI may be strong in mass-market entry and productization, Anthropic in code and enterprise trust, Google in search, phones, office software, and cloud. Leading a benchmark by a few months may not wrest away the usage habits, enterprise purchasing relationships, and data permissions another company already holds.
>
> So a model lead increasingly looks like winning an offensive opportunity rather than permanent occupation. The leader must use the window to turn capability into users, workflows, and feedback data; otherwise when the next-generation model catches up, the advantage disappears. From 2027 to 2029, look at four things at once: how long frontier capability leads last, whether users leave long-term context in the product, whether enterprises wire key processes in, and how costly switching models actually is. If the top spot keeps changing yet customers rarely migrate, the center of competition has shifted from model capability to distribution and process.

74. In the global division of labor in AI, Chinese companies are likely to play the role of the largest producer. Conventionally, our production capacity is the largest, including chips, we may have the largest chip capacity, and we have the most electricity.

> **2030 note** This is Liang's prediction, not a fact the two reports have proven. China may act like a power plant, offering huge volumes of chips, compute, and electricity. Largest production only means abundant supply, not the highest profits. Companies that directly serve hospitals and sales teams, if they hold customer data and control the software customers open every day, may capture more profit.

75. Chinese people will make this product the cheapest, and then on effectiveness, after all, for many foreign goods, domestic-made and American-made products aren't that different now. Maybe AI will be like that in the future, but Chinese-made AI may be cheaper. This cheapness may be systematically low, just as Chinese services in other industries are cheaper.

> **2030 core note** The low-cost route first changes not who earns the most but who can still charge high prices. If Chinese teams produce near-comparable capability with fewer chips and accept thinner margins, they will force global model prices down, letting small companies that used to be unable to afford AI call it at scale. Models therefore become more like base materials: cheapness expands the total market, yet also pushes profit from "owning the model" toward "turning the model into results."
>
> The risk of this route is mistaking output for capture of value. Hospitals, law firms, and financial institutions won't just buy the cheapest answers; they need evidence, permissions, audit, system connection, and a final signatory. Application and platform companies controlling these links may use cheap Chinese models as the base layer while taking higher profit. From 2027 to 2029, if model call volume grows fast while profit per call keeps thinning, and vertical software increasingly charges per case or per result, a division of labor of "Chinese production, applications capture value" is forming. Whether Chinese companies can move up into workflows rather than only serving as lowest-cost suppliers will determine how much profit the cost advantage can keep.

76. The ultimate gap should be in three aspects: cost, time, and user experience. Beyond that, there may be no gap.

> **2030 note** Cost is how much a refund costs in total to complete; time is who first gets it truly into production; and experience is far more than whether the chat flows well. Real experience includes whether it remembers the work context, whether it can call real systems, whether errors are easy to spot, whether actions are constrained by permissions, and who is responsible when the task ends. Seen this way, the three gaps the original states have already buried data, workflows, and responsibility in the word "experience."

77. Cost is definitely a differentiator; I think cost is probably ranked first. Then second is time, when you can do it. Being a few months earlier or later, it's different.

> **2030 note** A model launching a few months earlier first gets users and real use records. A low price makes it survivable to run heavily every day. But in an enterprise, wiring AI into order, contract, and payment systems and arranging people to check errors is often more expensive than the model itself.

78. From the start, OpenAI thought it could really monopolize the world, but in fact it will meet many challengers. Meeting challenges, it won't be so easy. America will meet challenges, and in the future it may also meet China's challenge, because Chinese people are willing to take less and can still provide this service.

> **2030 core note** Low price and open source do weaken a single model's monopoly: customers can switch APIs or deploy the open model on their own machines, making it hard for the leader to keep charging for scarce technology. But the AI industry isn't only the model layer. Enterprises' email, files, identity accounts, approval records, and customer relationships already sit in existing platforms, and moving those is far harder than changing a model connection.
>
> So "challenging OpenAI" may happen, but it doesn't mean any low-cost model company will take over the entire value chain. Power at the model layer will fall, while Microsoft, Google, Salesforce, or industry software holding distribution, permissions, and workflows may instead grow stronger, because they can choose among base models. DeepSeek's strategic dilemma lies here too: making its model replaceable helps break others' monopolies, but also makes itself easier to replace. From 2027 to 2029, if enterprises commonly use multiple models and routing systems switch automatically by cost and task while accounts, data, and approvals stay on the original platforms, the monopoly hasn't vanished; it has just moved from the model layer to workflow control points.

79. Those who take more will be defeated by those who take less. You don't even need to actually take more; if the vision is to take more, you'll be defeated by one whose vision is to take less. In fact nobody has taken the money; it's only a vision. If your vision is to take more, you lose first, and you face greater difficulty.

> **2030 note** If customers can switch models just by changing a connection address, setting the price too high pushes people to the cheap or open-source version, and models slowly become similar commodities. But being willing to earn less isn't enough; if service keeps going down, technology stops advancing, or nobody knows you exist, cheapness alone can't win.

80. For us, it's not about taking the most profit or pricing for revenue maximization; we only earn a reasonable return. That's an explanation. I believe this; I'm not finding excuses for it, because there's no need.

> **2030 note** This pricing is like water utilities, earning a bit less per use to let more people safely use it over the long term. The analogy only explains the pricing method; AI's answers can be wrong, and water doesn't make up stories. A "reasonable profit" has to at least cover buying chips, paying electricity, maintaining service, and being able to afford your own errors.

81. I think in many experience aspects, we may be able to do better than America. In product, product capability isn't necessarily worse than America's. Cost should also be lower than America's, so China will still be competitive.

> **2030 note** Chinese teams can first master Chinese expression and local work habits, then push prices down. But good experience can't be judged only by whether the chat flows; watch whether AI can open a local order system and finish the task, and whether a human can take over right away after it errors.

82. Cost is easy to understand, because they don't have to do it, so they don't develop this capability. They certainly don't value this like we do. We can treat it as a very important thing, but for them it's unimportant.

> **2030 note** With fewer chips and less money, teams find ways to make each chip work harder, which trains money-saving capability. But it won't forever belong only to Chinese companies. Once price becomes the focus of a global competition, resource-rich companies will also learn to economize.

83. Large models may not need two big companies and two small companies; that may already be enough. The gap has only two things: time and cost. So no one will have windfall profits; I don't think anyone will. Whoever controls cost well earns a bit more; whoever controls cost poorly earns a bit less. That's all.

> **2030 core note** "Only a few model companies needed" describes the most expensive frontier-training layer, not the whole AI market. Enormous compute will concentrate the most frontier general models among a few players; open source, local deployment, national-sovereignty needs, and industry differences will keep supply diverse. Both "a few upstream giants" and "a mass of downstream models and applications" may hold at once; they don't conflict.
>
> Whether windfall profits vanish also depends on which layer you look at. When model capability converges and switching is easy, pure token-selling margins are squeezed flat by price wars; companies holding enterprise data, approval flows, distribution entry points, and responsibility relationships may instead command stronger pricing power. Liang narrows the difference to time and cost, underestimating the friction and trust of customer switching. From 2027 to 2029, if model prices keep falling, enterprises call multiple models at once, and vertical applications' renewal and unit-price still rise, then "intelligence commoditized, workflows appreciate" has happened.

07

Model R&D and technology

84. Maybe half our company, usually half our people think OpenAI is better. Anthropic does have first-mover advantage, but that first-mover advantage should be gone soon; it's not an advantage it can hold long-term. All three are very strong; of the three, the most efficient, the one spending the least cost and burning the least money, is probably the winner.

> **2030 note** The original doesn't say which three companies, or who spends the least, so this passage can't build a ranking. What can be kept is only one judgment: leading by a few months first isn't hard; what's hard is years of continually producing new models while squeezing the cost of each training run.

85. We've been doing multimodal all along. For products, it matters a lot; for C-end user products, it matters a lot. But for the intelligence ceiling, it's a component, not the main line itself.

> **2030 note** Multimodal means one model doesn't just read text but can see images, hear sound, and read files. By 2030, it may become as ordinary as a phone's built-in camera. This analogy only says the feature will spread; it doesn't mean seeing more kinds of materials makes you smarter.

86. We should release the related models; V4 and its successors will support native multimodal. But to us, multimodality, for intelligence, is a component; we don't treat it as intelligence itself.

> **2030 note** V4 is the version name of DeepSeek's next-generation model. Native multimodal means these abilities grow directly into the model rather than being added as a later plugin. It can read a contract while looking at a table and a screenshot, but if it can't write results back into the company's system, the matter still isn't done.

87. On language-model Scaling, I don't see a ceiling right now. Neither our current intelligence level, nor even America's intelligence level, has shown a ceiling.

> **2030 note** Not seeing a ceiling only means capability growth hasn't been observed to stop yet, not proof it can grow forever. The original's "or causing America's" also looks like a transcription error. Even as models improve, chips, electricity bills, error rates, and who's accountable still limit how big a thing they can do.

88. Many people inside think this way: first it has to be useful to ourselves, first use it for ourselves. Then this is the fastest way to AGI. When we find it useful ourselves, that may mean others find it useful too, but first we have to ensure it's useful to us.

> **2030 note** Using it for one's own researchers first has the advantage of extremely short feedback distance: have the model read papers, edit code, and run experiments the same day, and see that same day whether it saved time or made errors. Real use, results, corrections, and next-version improvement form a closed loop, closer to research value than chasing exam scores. If this small flywheel keeps turning, internal use itself becomes data others can't buy.

89. The first goal of the models we build isn't that everyone uses them well, but that we use them well. First, useful to ourselves. Once useful to ourselves, I'll be faster at developing the next version.

> **2030 note** What's special about self-use is that the model's first customer is the model's maker. If it helps researchers read papers, write code, and run experiments today, those people can feed the findings into the next version tomorrow, forming a "use, result, correct, improve, more use" loop. Whether the flywheel works depends on whether errors and real results truly return to training; accumulating more chat logs doesn't automatically produce progress.

90. We call this "scratching a lottery ticket." The threshold is low; anyone can scratch one, but what anyone scratches out, maybe I don't know if it's talent or what. Here we don't need to allocate resources. The difference from other companies is just that we spend time discussing this problem, thinking about it, and treating it as an important thing.

> **2030 note** This passage doesn't say what's being scratched, so you can't infer a specific technical route from it. A more reasonable reading is that many people can try unverified new ideas. But one lucky success isn't a result; others have to reproduce it, and it has to pass testing before it can go into a product.

08

Commercialization and pricing

91. Our API pricing is a reasonable profit, roughly buying a batch of equipment on the market and recovering cost in ten months; I think that's a reasonable profit.

> **2030 note** API is the abbreviation for Application Programming Interface, which lets other software call the model without a chat page. Ten months to payback, by the original's accounting, means the equipment purchase money is earned back in about ten months; but the original doesn't say whether it's calculated on operating revenue or net profit, so it can't be treated as a precise return rate.

92. If we maximized profits, we'd set the price higher. Because in this price range, user demand is inelastic; whether I double the price or raise it by another half, token consumption barely changes.

> **2030 note** A token is a small piece a model cuts text into; billing counts these pieces, which don't necessarily equal one Chinese character. Here, even doubling the price hardly reduces the text pieces users consume, showing customers don't currently mind this price difference. By 2030, with more replaceable models, this may not hold.

93. For one of our models, at first we worried about too much demand, so we set the price fairly high, which made the team unhappy. Later I lowered it to a quarter, and everyone was happy.

> **2030 note** Lowering to a quarter means a call that cost 4 yuan now costs 1; but the original gives no actual price, it's just a proportion. Cheaper lets developers dare to try more times. If enterprises really want to use it, AI also has to read the right materials, be told which buttons it may press, and have someone inspect important results.

94. The ceiling of To B business should still be demand; under this generation of AGI and AI technology, To B demand should be limited. It will grow fast, but it isn't an infinite thing; it's ultimately constrained by demand, not compute.

> **2030 core note** B in To B stands for Business, selling services to enterprises. The ceiling on enterprise demand isn't how many questions employees can ask, but how many real processes are worth rebuilding. Companies buy a batch of chat accounts quickly; organizing data, connecting systems, dividing permissions, changing approvals, training employees, and absorbing errors go slowly, so AI's individual adoption speed can be high while organizational productivity doesn't jump in step.
>
> This also shows "limited demand" isn't a small market; demand simply has to pass a return-on-investment filter. The earliest to land will be high-frequency, high-value, easy-to-verify, reversible-error tasks; medical final review, major loans, and complex legal judgments, even higher in value, will be slower because responsibility is heavier. If a model company only sells call volume, it will hit a ceiling of many enterprise trials and few production deployments; an application company that can deliver a work segment on time and auditably can instead expand payable demand. From 2027 to 2029, watch task completion volume in production environments, human-handoff rates, and customer renewals, not just seats purchased and demo counts.

95. If I can get it done, I think we should take it all. Say this year I have several hundred million dollars of B-end revenue, plus C-end users, then that itself is already some commercial foundation. If next year we have B-end revenue and this demand can grow, the company isn't far from net profit, and may already be at net profit.

> **2030 note** "Taking what we can get done" isn't clear about what it refers to. The revenue and profit afterward all carry "if," "say," and "may," so they can't be treated as money already earned. Even if it turns profitable in the short term, after models get cheaper by 2030, a company still has to retain customers on lower cost and more stable service.

96. In the worst case, selling API may support a listed company. If there's no new technical progress and our technology freezes here, then in the end we'd sell API with full force and serve well, and I think that's enough.

> **2030 note** Selling only interface calls may support a model company; that's the worst-case scenario the original envisions. But as models get cheaper, customers prefer to pay for complete results, for example, not buying a piece of insurance advice, but an audited claims result with evidence, reviewed by a human, ready to submit.

97. Under current conditions, I think the most reasonable move is to go all-in on a general Agent; other agents have lower priority, including finance and doctor agents. Do Coding first, because the Coding Agent can do a lot, and there are many vertical agents. At this stage, I think the most important thing is still the Coding Agent.

> **2030 core note** The Coding Agent is the intelligent agent that writes code. Code has an advantage other knowledge work rarely has: once generated it can run immediately, tests give relatively clear feedback, and on failure it can keep revising based on errors. It is both the earliest monetizable agent and a proving ground for training "model calls tools, executes multi-step tasks, self-corrects"; the planning, memory, and tool use learned here may transfer to research, operations, and other fields.
>
> But code being testable doesn't mean software is safe. Tests only cover conditions humans wrote; complex systems have implicit dependencies, long-term maintenance, and real post-release risk. It also reshapes talent development: senior engineers can manage multiple agents and enlarge their output radius; beginners' small learning tasks, once automated, may narrow the ladder into advanced work. From 2027 to 2029, the real progress signal isn't how much code AI wrote, but whether it can independently complete a long task from understanding the repo, editing, testing, to submitting, whether the defect rate is controllable, and whether the company finds new ways to train newcomers.

98. I think low cost is first a result. Our models have indeed been moving toward lower cost in model architecture all along; this is related to our vision. There are many more algorithmic methods we have; cost can keep going down.

> **2030 note** Saving money isn't a temporary discount after listing, but doing fewer useless computations while building the model so the same chip works harder. Cost lowered this way is hard to take away with one promotion, and lets small companies use capabilities only big companies could previously afford.

99. Another reason cost goes down is that the lower the cost, the larger the model I can train, the more I can afford a bigger model. On the same compute, with limited compute, if my computational efficiency is higher, I can afford a bigger model.

> **2030 note** With the same money, computing fewer useless steps lets you train a bigger model. But one run being cheaper doesn't mean total electricity falls: once prices are low, companies let more agents work longer and try more rounds, and the added usage may eat all the savings. Low cost simultaneously drives AI adoption and new energy demand; that's the counterintuitive result of efficiency gains.

09

Open-source strategy

100. I think we will open-source, and our strongest model may also be open-sourced. Because I don't see the benefit of closed source, no inevitable benefit. ByteDance's model is closed source; what benefit does it have? I don't see any benefit.

> **2030 core note** Open source means publishing trained model files for others to download. It does three things at once: pushes model prices down, gives customers worried about vendor cut-off or data outflow an insurance policy of "can run myself," and makes developers more willing to build tools and adaptations around this model. DeepSeek gives up some exclusivity to make its model a broader base material and de facto standard.
>
> This is a strategy of "making the thing you use with others cheaper." The cheaper the model, the more demand for deployment, chips, cloud services, industry software, and enterprise retrofit; if DeepSeek always runs cheaper and more stably on official service, it can still earn from the enlarged total market. The risks are direct: competitors can take the same model and undercut for customers, the community may shift to a more open standard, and security updates are harder to unify. Through 2027 to 2029, watch whether the open model forms an ecosystem across chips and tools, whether official service still has a cost advantage, and whether enterprises treat open source as a real production solution. Many downloads but few production deployments only shows spreading success, not success of the business model.

101. Even if the model is open-sourced and you tell others everything, the threshold is very high. For others to use it, the threshold is very high. For him to use it is hard; second, he also has to make costs very low to use it, which is very very hard, not so easy.

> **2030 note** Publishing the model file isn't handing over the training data, tuning methods, and acceleration tricks. After download, others still need to find suitable chips, make the model run stably, fix security problems in time, and control electricity bills. Having a recipe doesn't mean you can immediately run a good restaurant.

102. Open source won't affect revenue. Open source, I think, has no effect on our business model at all.

> **2030 note** With the files public, convenient services can still charge. DeepSeek can prepare machines for customers, keep service online, and update new versions; customers don't have to keep their own team of engineers. Open source changes the reason for charging without guaranteeing revenue is entirely unaffected.

103. I don't worry about others deploying our model and competing with us; not at all. We even hope they deploy it. We help the open-source community as much as we can, helping everyone deploy our model.

> **2030 note** Helping others deploy makes more programs and products grow around DeepSeek and makes the model more like a common standard. But the people helped may also turn around and grab customers. For DeepSeek to truly not worry, it must keep running cheaper, more stable, and updating faster.

104. In dealing with the outside world, our attitude is: we only do the main line of AGI. In dealing with the outside world, we're very willing to help anyone, even our competitors, including Alibaba, Zhipu, and Moonshot, do better. Because we don't lose anything; we're open-sourced anyway.

> **2030 note** By 2030, some train models, some rent the computers that run them, some put AI into office software, and some specialize in medical, legal, or customer service. DeepSeek, Alibaba, Zhipu, and Moonshot can each continue their own models while application companies wire them into concrete work. There's overlap and cooperation; one company needn't do everything.

105. Is the open-source model we give out the same as the model we deploy ourselves? It's the same. We won't open-source an inferior model and then use a better one ourselves. No; it's the same.

> **2030 note** Being the same at most shows the publicly downloadable model file and the official one are the same version; it doesn't mean the product experience is identical. Chips, latency, which materials are checked before answering, permissions and interception rules, version compatibility, queuing at busy times, error rollback, and audit all change results. By 2030, much of the charging falls precisely on these invisible services that make enterprises willing to hand over tasks.

10

Data and post-training

106. Data should almost equal half the model. There's also the problem of data labeling before that. In data labeling, it's related to our capital investment. With our capital-investment structure, we can't support the cost of that much high-quality data labeling, because the cost is high.

> **2030 core note** Data equals half the model doesn't literally mean a 50/50 split; it emphasizes that models won't progress by algorithms alone out of thin air. Two kinds of data should be separated: public articles and human labels teach models general patterns; whether a suggestion was adopted in the end, whether a bug was actually fixed, and which exceptions were rejected by experts teach an agent how this company works. The second kind of data grows attached to real outcomes and is harder to copy than collecting more web text.
>
> So the 2030 data moat won't just be "who saved the most text," but who occupies real workflows and can keep seeing inputs, actions, results, and expert corrections. Application companies may not be able to train the largest general models, but by holding closed-loop feedback on a certain class of contracts, claims, or diagnoses, they can build deeper barriers. The risk is that historical decisions carry bias and stale rules; a data flywheel that records only successes and not failures will amplify old problems. From 2027 to 2029, watch whether error rates fall with real use, whether each correction keeps its evidence, and whether customers can control how their proprietary data is used.

107. The cost of American data labeling is no different from Chinese data labeling. China doesn't have a cost advantage in labeling; especially in labeling high-end data there's no cost advantage, which makes it hard for us to invest in labeling like America. This path is hard in China, because labeling is really too expensive, whether outsourced or done by ourselves.

> **2030 note** Writing "cat" or "dog" on ordinary pictures is something many people can do. Judging whether a medical record missed a diagnosis or which clause in a contract is risky requires doctors or lawyers, and the cost doesn't automatically drop just because it's in China. A cheaper approach is to have experts leave the right answers and evidence while doing their normal review work.

108. Right now we're basically walking on two legs. It's not that we can't label at all; it's that some labeling is low-cost and some is high-cost. We label the low-cost ones first.

> **2030 note** Labeling cheap, easy-to-judge data first lets limited money cover a wide area. But the most expensive is often the rare, dangerous anomalous cases, which precisely can't be skipped forever. By 2030, important conclusions in medical, legal, and financial contexts still need expert materials, checkable evidence, and human signatures.

109. You can also think of it as our company having half its people labeling data right now. Half of the core researchers, the most important people, half are labeling. We focus on labeling. Solving the AI problem at this stage depends on labeling.

> **2030 note** The original first says half the whole company, then says half the core researchers; the two ranges differ, so you can't conclude a whole-company figure of 50%. What's certain is that many key researchers are personally selecting materials and judging right from wrong. This shows model progress at this stage still needs lots of human labor.

110. The bottleneck of high-quality data labeling, I think, is time, because time is needed. Because for OpenAI, for abroad, for Anthropic, they all started earlier, have more capital, and more cards.

> **2030 core note** "The bottleneck is time" isn't only about annotators writing slowly; it's that high-quality feedback has ordering. AI must first participate in real tasks, wait for real results, and then experts judge what's right, what's wrong, and the evidence; capital can buy more people, but can't buy in one day results that won't be known for years.
>
> This creates compounding for whoever enters real workflows first: more records, fewer similar errors; more reliable systems, more daring customers; more tasks, still more feedback. Latecomers can buy the same general model but not this continuous history. But the flywheel can also spin backward: stale data, biased feedback, or a system collecting only easy successes all make the model more confidently repeat old errors. From 2027 to 2029, the most critical signal isn't how many items were labeled, but whether, as time-in-use grows, the failure rate and human-handoff rate of real tasks keep declining.

111. The hallucination problem of large models affects the user experience quite a lot. Hallucination also has a method to be solved, but it's a long proposition. Hallucination can be regarded as something solvable through better post-training; it's a solvable, improvable problem.

> **2030 core note** Post-training means, after the model reads vast general materials, continuing to tune it with human demonstrations and corrections. It can reduce the probability of AI confidently fabricating wrong answers, but can't turn a probabilistic system into an error-proof calculator. More importantly, hallucination left in a chat window is only an experience problem; once an agent can refund money, change code, approve, or write results back into a system, the same error becomes an operational, legal, and safety problem.
>
> So solving hallucination can't rely on a single technical route; the whole work system must be designed: important conclusions show evidence and uncertainty, agents see only the materials and press only the buttons needed for the task, high-risk actions pass human approval, all actions are logged, and anomalies can halt and roll back. The model is responsible for bringing the error rate down; the institution is responsible for capping the loss of the remaining errors. From 2027 to 2029, if enterprises only advertise automation rates without disclosing human handoff, incidents, and recovery mechanisms, they may be becoming "high-speed error machines"; the signal genuinely approaching a 2030 production system is people daring to hand a well-bounded, always-recallable responsibility to a machine.

11

Organization and company positioning

112. First, we have no object to imitate. Every step, we start from our actual situation, seek truth from facts, make decisions from the actual situation, and find what we should do. So it's a product of its era, or a response to the real situation; it's not a result of imitation.

> **2030 note** Having no object to imitate, more accurately, means DeepSeek, given its few chips and its need to compete globally, chose low cost, open source, and doing fewer things. This choice attracts users and developers today. By 2030, if models converge, it will also have to keep customers on stability and continuous updates.

113. We clearly intend to commercialize. In the end we have to survive; we're a company after all, and the government won't give us a cent.

> **2030 note** A company must have revenue to keep buying chips, paying server electricity bills, and paying researchers' salaries; ideals can't replace bills. By 2030, model prices may keep falling, and whoever can provide uninterrupted service at lower cost is more likely to survive.

114. We're still essentially a company; it's just that we make trade-offs in which money to earn, when to earn it, how much, and on what. Many great companies have a pursuit beyond profit. That pursuit, far from hurting their commercialization, in the end lets them commercialize better.

> **2030 note** This isn't about not making money; it's about not raising each call's price to the maximum customers can bear. DeepSeek can earn from low cost and high call volume, while partner companies wire models into insurance, customer service, or healthcare and charge for completing concrete work. Open source and commercialization don't conflict.

115. For partners, our financing was carefully selected. First, I think interests are fairly aligned, most aligned with us, least hostile to us, and most hoping we succeed. Not everyone hopes we succeed, because we've harmed many other people's interests.

> **2030 note** An investor brings more than money. It may help buy chips, find machine rooms, reach customers, or demand the company go where it wants. "Aligned interests" means picking a partner willing to let DeepSeek keep making models for the long term, rather than using the investment to force it to protect another business.

116. AI now doesn't lack taste and intuition; it lacks the ability to continuously learn. AI's taste and intuition are fine. Ask it to write an article; its taste and intuition, I think, are fine.

> **2030 note** Writing smoothly doesn't mean holding down a job long-term. AI may write beautifully yet state facts wrong, or get corrected yesterday and repeat the same mistake today. By 2030, what truly needs filling is whether it can remember long-term experience, let people verify answers, and find who's accountable when it errs.

117. We hope to only do one piece. I think AI is very big; there's no need for me to, I only do one piece. If we focus, and I think the business stakes here are already big enough, if the AI era spawns many trillion-level companies, I think we're one of them.

> **2030 note** Doing only models can still serve tens of thousands of companies, just as a power plant doesn't need to make every refrigerator itself. The analogy stops there: electricity doesn't make things up, but models do, so DeepSeek also has to solve price, speed, and reliability at once. Trillion-level is only Liang's goal, not a proven result.

118. We hope to lift up more people, but we don't have that much energy. We have the willingness, and there's no conflict of interest, but whether we do it is another matter. At least there's no conflict of interest here; we hope for win-win cooperation.

> **2030 note** An open model lets other companies build industry applications on it, reducing some business conflict, but it can't have zero conflict; they may still compete over enterprise customers and service prices. Really helping more people also can't be done by employees visiting each customer; you have to make manuals, installation tools, and unified connection methods so others can use it themselves.