# Why Did They All Move to AI Labs?

## The sharpest minds see more than money

> Research date: 2026-07-24
> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)
> Field: artificial intelligence, research institutions, talent migration, technological power
> Subject: the evolution of AI paradigms from 1943 to 2026, and talent flows in frontier labs in 2026
> Methodology: Horizontal-Vertical Analysis (横纵分析法)

On February 9, 2026, in [《The Cognitive Mindset of Disruptive Innovators》](/posts/2026/02/mindset-of-disruptive-innovators/), I asked: what exactly do people like Jobs and Musk see that others don't?

About five and a half months later, this question got a new set of protagonists.

Jelani Nelson, the overall EECS chair at UC Berkeley, stepped back from the university to join Anthropic's pre-training team; Andrej Karpathy, OpenAI co-founder and former head of AI at Tesla, paused his educational startup and returned to frontier model R&D; AlphaFold's lead, Nobel Chemistry laureate John Jumper, left Google DeepMind for Anthropic; Google's Gemini co-lead Noam Shazeer joined OpenAI. Mathematicians, physicists, economists, and philosophers have also appeared on the rosters of frontier labs.

Read together, the headlines easily form a grand story: the smartest people have seen a future ordinary people haven't; they are no longer satisfied with papers, companies, or wealth, but are chasing the highest level of intelligence, and through it, the highest level of power.

This intuition captures part of the truth, and flattens another part.

## One-sentence conclusion

> What they see is AI turning from a technology into "the technology that produces new technologies," from an object of study into the infrastructure that decides the speed, direction, and entry rights of research. What top talent are contending over isn't a more respectable job, but which side of this feedback loop they stand on.

AI can indeed bring unprecedented cognitive leverage, action leverage, and agenda-setting power. But it won't automatically convert into "supreme power." Those who control frontier models still depend on chips, energy, capital, organizations, law, states, and social trust. A researcher entering a lab only gets closer to the machinery of power; it doesn't mean he personally owns it.

## Research scope: unpacking the "all went" in the headlines first

This report defines "top talent" as four categories of people:

- those who once led frontier models, key algorithms, or large technical organizations;
- those with established research standing in disciplines such as mathematics, physics, biology, economics, and philosophy;
- those who hold research or technical agenda-setting power, such as university department chairs, research center heads, and CTOs;
- those whose career choices have been confirmed by themselves, their school, company, or reliable media.

"Joining a frontier AI lab" isn't a single state either. It includes at least permanent departure, industrial leave, academic sabbatical, part-time roles, visiting researcher positions, and startup teams merging into a platform. Writing all of these as "resigning" would exaggerate how irreversible the migration is.

The clearest example is Jelani Nelson. Berkeley's [official announcement](https://eecs.berkeley.edu/news/changing-of-the-guard-welcoming-ana-arias-as-eecs-department-chair/) says he stepped down as EECS chair to begin an industrial leave; Anthropic confirmed he entered the pre-training team. An accurate description is "former Berkeley EECS chair temporarily left the university to join Anthropic," not "permanently resigned his professorship."

This report separates public facts, the parties' own statements, and analytic inference. Talent movement can prove labs are attractive and reflect these people's subjective beliefs; it cannot prove their technical predictions are necessarily correct. People who join frontier labs were always more likely to believe a turning point is near; there's a clear selection effect here.

# Vertical analysis: how intelligence went from a philosophical problem to an industrial process

Today's migration is not a fad that suddenly appeared in 2026. It is a curve spanning more than eighty years that has crossed several overlapping thresholds in recent years.

## 1943-1956: intelligence first becomes a manufacturable object

In 1943, McCulloch and Pitts abstracted neural activity into logical computation. In 1950, Alan Turing stopped arguing about whether machines really "have minds" and recast the question as an observable imitation game. The [Dartmouth proposal](https://www-formal.stanford.edu/jmc/history/dartmouth/dartmouth.html) of 1955 was more direct: every aspect of learning and intelligence can in principle be precisely described so that a machine can simulate it.

These three steps completed a conceptual migration:

| Old question | New question |
|---|---|
| What is the mind | Which behaviors can be computed |
| Why are people intelligent | Which mechanisms can be learned |
| Is intelligence mysterious | Can intelligence be described, trained, and manufactured |

From birth, AI was not a small subfield of the software industry. It unified logic, language, neuroscience, control, learning, creativity, and scientific discovery into a single research program. For mathematicians, physicists, and philosophers, it engages precisely the deepest questions of each discipline: whether the world can be compressed into representations, whether reasoning can be mechanized, how knowledge forms, and how action arises from judgment.

During this period, research centers were mainly universities, government-funded projects, and a few corporate research institutes. The scarce resources were theory, talent, and patience; a researcher with pen, paper, and limited computing could still push the frontier.

## 1960-1989: two winters left behind not failure, but criteria for screening

Expert systems once demonstrated that human knowledge could be encoded as rules. DENDRAL helped analyze chemical structures; MYCIN could give diagnostic advice in closed medical scenarios. But entering each new domain required re-interviewing experts, organizing rules, and adding exceptions; capability grew roughly linearly with manually entered knowledge, while maintenance costs could rise faster.

Perceptrons, machine translation, and general robotics also endured collisions between high hopes and capability ceilings. The retreat of funding produced two so-called "AI winters." This history left later generations an extremely important criterion:

> A stunning demo is not an extensible paradigm. A system genuinely worth long-term bets must keep improving with data, compute, and training, rather than relying on humans to write rules indefinitely.

The same criterion still holds when evaluating large models today. A beautiful math answer or a demo that operates a browser cannot by itself prove that general intelligence has arrived. A more testable object of observation is whether the capability curve can be reproduced across tasks, continue growing through feedback, and save more time than it creates trouble in real work.

## 1986-2011: from "writing intelligence" to "training intelligence"

In 1986, Rumelhart, Hinton, and Williams published the [backpropagation research](https://www.nature.com/articles/323533a0), showing how multi-layer networks adjust parameters from error and form the internal representations needed to complete a task in their hidden layers.

This change looked like a mere algorithmic improvement, but it actually rewrote the human's role. Previously, engineers had to tell machines "what an edge is," "what a syntax is," and "what rules correspond to what conclusions"; now, people more often define the objective, the data, and the training process, letting representations emerge through optimization. The mode of producing intelligence moved from handcraft workshop toward reproducible training.

From convolutional networks to LSTMs to deep belief networks, much foundational accumulation happened in years when deep learning was not fashionable. Researchers like Hinton, LeCun, Bengio, and Sutton long maintained a community of low prestige, low funding, but high coherence. After 2012, what companies competed for was not a few papers, but the research taste, engineering intuition, and failure experience accumulated by a school over decades.

This also reminds us that "seeing the future" is rarely a sudden epiphany. Jobs's product judgment depended on decades of maturity in graphical interfaces, touch, materials, chips, and supply chains; AI's leap also depended on long-term accumulation suddenly converging on data, GPUs, and algorithms. Foresight looks more like reading, earlier than others, when constraints loosen, than receiving oracles from the void.

## 2012-2017: the first wave of professors joining companies, trading GPUs, data, and deployment

In 2012, [AlexNet](https://proceedings.neurips.cc/paper/2012/hash/c399862d3b9d6b76c8436e924a68c45b-Abstract.html), using GPUs and large-scale labeled data, decisively won the ImageNet competition. Hinton, Alex Krizhevsky, and Ilya Sutskever then founded DNNresearch, acquired by Google. Hinton still kept his identity at the University of Toronto at the time, forming an early exchange: universities supplied theory and talent, companies supplied data, compute, and product feedback, while papers remained widely public.

In 2013, Yann LeCun entered Facebook to build FAIR. In 2015, Uber recruited about forty people from Carnegie Mellon's robotics center, triggering the first widely known "drain" dispute between universities and industry. In the same year, when OpenAI was founded, it still promised to encourage researchers to publish papers and to share code and patents.

In 2016, AlphaGo defeated Lee Sedol; in 2017, AlphaGo Zero, starting only from rules and self-play, discovered strategies humans had not directly taught it. That same year, Google researchers published [Transformer](https://arxiv.org/abs/1706.03762), making sequence-model training highly parallel.

This stage produced three signals that kept amplifying afterward:

1. the same learning mechanism can transfer across domains, not just solve one hand-defined task;
2. self-play, search, and automatic evaluation can generate new training feedback, so capability is no longer fully bounded by the limit of human samples;
3. complete experiments increasingly depend on the data, compute, and engineering systems that companies hold.

Corporate labs in 2013 still looked like universities' wealthy neighbors. Researchers could hold dual roles, papers were the currency of prestige, and key methods were often made public. Labs in 2026 are closer to a new institution: research institute, supercomputing center, product company, and safety body layered together.

## 2019-2022: Scaling turned exploratory research into a financeable industrial program

In 2019, Rich Sutton summarized in *The Bitter Lesson*: in the long run, general methods that exploit ever-increasing computation tend to beat methods relying on human handcrafted knowledge. That same year, when explaining its new organizational structure, OpenAI stated directly that frontier systems might require billions of dollars in cloud computing, talent, and supercomputing infrastructure.

The 2020 [Scaling Laws](https://arxiv.org/abs/2001.08361) research showed that, within the observed range, language-model loss follows an empirical power law with model size, data, and compute. GPT-3 demonstrated that a single large model can adapt to many tasks from few examples; research like Chinchilla began answering how to allocate resources more efficiently between parameters and training data.

A systemic turning point happened here. If capability growth bears a partially predictable relation to resource input, intelligence research no longer must wait for occasional genius breakthroughs; it can be written into capital budgets, data-center plans, and multi-year infrastructure contracts. The research question expanded from "is some idea useful" to "where will the curve go if we invest ten times the compute and improve the data and training methods."

A scaling law is not a law of nature, nor does it guarantee capability grows forever. Data quality, energy, chips, algorithms, and reliability can all form new bottlenecks. But it sufficed to change organizational behavior: venture capital is willing to bet, cloud vendors are willing to build clusters, labs are willing to pay scarce talent far beyond university prices, and researchers are willing to go to the only place certain experiments can be run.

A [study](https://bfi.uchicago.edu/insights/attention-and-money-is-all-you-need-why-universities-are-struggling-to-keep-ai-talent/) based on US Census Bureau employer-employee data tracking about 42,000 AI researchers found that in its US sample, by 2019 about 68% of researchers worked in industry. After a permanent move to industry, researchers' income and patents rose significantly while paper output fell clearly. The shift of knowledge-production centers predated the generative-AI boom; 2026 is merely its most conspicuous phase.

## 2020-2024: AI goes from object of study to scientific instrument

AlphaFold2 is another curve. It didn't just make existing work faster; it crossed a long-standing bottleneck in protein structure prediction. In 2024, Demis Hassabis and John Jumper shared the [Nobel Prize in Chemistry](https://www.nobelprize.org/prizes/chemistry/2024/press-release/b/) for related work. This gave industry frontier labs a form of institutional legitimacy resembling the modern Bell Labs: a company's model research can reach directly into the highest honor system of fundamental science.

Similar signals then appeared in algorithms, materials, weather, mathematics, and physics:

- AlphaDev uses reinforcement learning to find faster sorting programs;
- GraphCast uses learned systems to produce fast weather forecasts;
- FunSearch combines language models with automatic evaluators to search for new mathematical constructions;
- [AlphaEvolve](https://deepmind.google/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/) wires models, program generation, and automated verification into algorithm and chip optimization;
- theoretical scientists are beginning to have models generate derivations, code, and candidate proofs, which humans then check.

Xi Yin, a theoretical physicist at Harvard, described to the *Harvard Crimson* a strong personal sensation: work that might once have taken years of programming has been drastically compressed by AI. UCLA mathematician Terence Tao's 2026 judgment was more restrained: models still waste time, but have entered the stage where they "save more time than they waste."

These two claims don't conflict. AI as a scientific instrument already has real value, yet it is still not an automatic scientist. Anthropic itself admits in its [science blog](https://www.anthropic.com/research/introducing-anthropic-science) that models perform strongly on some research processes but also hallucinate, pander to users, and get stuck on questions domain experts find easy. The real bottleneck is shifting from "executing every step" to "choosing problems, designing verification, detecting false results, and taking responsibility."

For mathematicians and physicists, the appeal of this change is very direct. They aren't leaving science for some other industry; they are moving closer to an instrument that might amplify all of science.

## 2025-2026: the most tempting threshold is AI beginning to help improve AI

Frontier labs now openly discuss a stronger feedback loop: using AI to help research, evaluate, and train the next generation of AI.

The team Karpathy leads after joining Anthropic has, as one goal, using Claude to accelerate pre-training research. Explaining his decision, he said the next few years are especially critical for frontier large models, and that he wanted to return to R&D. OpenAI's plan [published in June 2026](https://openai.com/index/built-to-benefit-everyone-our-plan/) lists "automating AI researchers" as one of three goals and says its internal judgment is that by March 2028, a substantial share of research may be done jointly by AI systems and human researchers.

Anthropic's [analysis of internal R&D](https://www.anthropic.com/institute/recursive-self-improvement) points in a similar direction: models already generate a lot of engineering code and improve quickly on well-defined, verifiable experimental optimization tasks; but humans still hold advantages in problem selection, research taste, and judging trustworthiness, and recursive self-improvement has not been achieved nor is it pre-ordained.

This is exactly the time value of "joining now." If AI were just one generation of better software, joining three years late might only mean missing a product cycle; if AI can accelerate AI research, even just organizational-level acceleration, an early advantage may compound repeatedly through models, talent, data, and feedback. What top talent see is a window for defining participation that may be closing.

This vertical axis can be compressed into five transformations:

| Stage | Role of intelligence | Scarce resource | Research center |
|---|---|---|---|
| 1943-1985 | a describable philosophical and engineering problem | theory, rules, long-term funding | universities, government, corporate research institutes |
| 1986-2011 | a system trainable from data | algorithms, data, GPUs | university-company cooperation |
| 2012-2018 | a capability extensible across tasks | big data, clusters, engineering talent | large tech companies |
| 2019-2024 | cognitive production scalable by capital | supercomputing, energy, training systems | a few frontier labs |
| 2025-2026 | a meta-tool that may accelerate science and its own R&D | frontier models, verification loops, research taste, governance | a "lab-platform-infrastructure" complex |

# Horizontal analysis: where did talent actually flow in 2026

## Look at the people first, not the slogans

As of July 24, 2026, public evidence supports the following representative affiliations. The table clearly separates 2026's new flows from relationships formed earlier that continue into 2026:

| Person | Previous position | Time and relationship type | The question it best illustrates |
|---|---|---|---|
| Jelani Nelson | Berkeley EECS chair, professor of theoretical CS | 2026-07, industrial leave; joined Anthropic pre-training | university administration enters core model training while retaining a return option |
| Andrej Karpathy | Eureka Labs founder; former OpenAI, Tesla AI head | 2026-05, joined Anthropic pre-training | he publicly judged the next few years critical, so paused his educational startup and returned to R&D |
| Peter Bailis | Workday CTO; former Stanford professor, Google Cloud VP | 2026-03, left Workday, joined Anthropic as Member of Technical Staff | management titles can be exchanged for frontline RL engineering; salary and personal motives undisclosed |
| John Jumper | DeepMind AlphaFold head, Nobel Chemistry laureate | 2026-06, left DeepMind, joined Anthropic; role undisclosed | AI-for-Science talent began flowing between labs |
| Noam Shazeer | Google VP, Gemini co-lead, Transformer/MoE pioneer | 2026-06, left Google, joined OpenAI | top compute cannot eliminate talent flow between labs; he will lead AI architecture research |
| Weijie Su | Wharton statistics professor | 2026-05, joined OpenAI during academic sabbatical | math and statistics talent enters model training sites |
| Alex Lupsasca | Vanderbilt black-hole theoretical physicist | from 2025-10, dual role as OpenAI researcher and Vanderbilt professor | "professor or company" is not the only option; hybrid identities are increasing |
| Anca Dragan | Berkeley professor, robotics and HRI researcher | moved in earlier; leading Google DeepMind safety and alignment research in 2026 | those worried about risk must enter the inside to access frontier models, data, and budgets |
| Chad Jones, Anton Korinek | Stanford, UVA economics professors | 2026, sabbatical to join the Anthropic Institute | labs need not just model engineering but economic and institutional reasoning |

The affiliations in the table synthesize [Berkeley announcement](https://eecs.berkeley.edu/news/changing-of-the-guard-welcoming-ana-arias-as-eecs-department-chair/), [Karpathy coverage](https://techcrunch.com/2026/05/19/openai-co-founder-andrej-karpathy-joins-anthropics-pre-training-team/), [Bailis coverage](https://www.theinformation.com/briefings/workday-cto-joins-anthropic-amid-startups-push-build-hr-apps), [Jumper coverage](https://techcrunch.com/2026/06/20/nobel-laureate-john-jumper-is-leaving-deepmind-for-rival-anthropic/), [Shazeer coverage](https://ca.finance.yahoo.com/news/googles-gemini-co-lead-noam-002742523.html), [Weijie Su's mirror of his public post](https://digg.com/tech/suyqtzrk), [Lupsasca's personal profile](https://lupsasca.com/), [Anthropic Institute announcement](https://www.anthropic.com/news/the-anthropic-institute), Chad Jones's [mirror of his public post](https://digg.com/tech/qn64s2zb), and *The Atlantic*'s cross-institution investigation. For people whose specific roles were not disclosed, this report does not infer their duties.

This table deliberately avoids pursuing "the longest list is best." Harvard physicist Xi Yin has been reported in connection with OpenAI, but as of the research date there is no clear confirmation of his role status from himself, Harvard, or OpenAI, so this report only cites his public discussion of AI research experience and does not write "joined OpenAI" as fact.

[*The Atlantic*](https://www.theatlantic.com/technology/2026/07/ai-companies-hiring-academics/688002/) counts at least eighty current or former professors across OpenAI, Anthropic, Meta, Google DeepMind, and other institutions, and considers that still an undercount. This number shows the scale of the migration, but it cannot fold everyone's motives into one type. Some go for frontier training, some for safety, some for scientific tools, some study AI's impact on the economy and society, and some are just on a one-year sabbatical.

The same pool of talent does not face a single kind of lab. The core exchanges at each destination can be placed in a matrix:

| Destination | Core promise to talent | Unique leverage | Main cost or uncertainty |
|---|---|---|---|
| Anthropic | advance frontier, safety, and social research in a critical window | pre-training internal data; safety mission; interdisciplinary Institute | tension between commercial goals and safety mission; private governance |
| OpenAI | let AI help make the next AI, and deploy fast | product distribution; architecture, science, and automation R&D | governance and commercialization changes; boundaries of open research |
| Google DeepMind | long-term science of the AlphaFold type plus general models | TPUs, Google engineering and data; mature research tradition | big-company coordination cost; personal agenda shaped by organizational strategy |
| Meta | build teams fast with heavy capital and massive distribution | social-product reach; whole-team absorption; infrastructure investment | rapid route and organizational change; team stability |
| xAI | pursue "understanding the universe" with supercomputing and engineering speed | Colossus, engineering synergy, strong mission narrative | founder-team attrition; governance and research culture still untested |
| independent labs and universities | keep route control, open research, or critical distance | founder autonomy; academic community; public accountability | dependence on funding and compute; weaker frontier access |

## Anthropic: turning "the critical moment" into an organizational narrative

Anthropic's appeal to interdisciplinary talent comes from a three-layer combination.

One layer is frontier training. The pre-training team holds checkpoints, training curves, failure modes, data recipes, and expensive training runs; outside researchers can only see published product slices. Nelson and Karpathy entered precisely this layer.

One layer is the safety mission. Anthropic, in [Claude's Constitution](https://www.anthropic.com/constitution), describes its position as a kind of "calculated bet": if powerful AI is coming anyway, keeping a safety-focused lab at the frontier is better than leaving the frontier entirely to developers less concerned with safety. This narrative is very attractive to people who believe a turning point is near and also worry about runaway and concentrated power.

One layer is expanding the lab into a small university. The Anthropic Institute absorbs economists and social scientists; science programs connect physics, biology, chemistry, and mathematics. In 2026 the company proposed a "compressed twenty-first century," making decades of scientific progress happen in a shorter time. From public statements and choices, one can infer that for some researchers, the position also carries an identity: participating in interpreting and shaping a possible civilizational-level transition.

This narrative also has internal contradictions: safety research needs access to the strongest models, so the people most worried about concentrated risk flock to the institutions concentrating it most; commercial success funds the safety research even as it subjects publication boundaries and research agendas to private governance.

## OpenAI: its strongest pull is "letting AI help make the next AI"

OpenAI's organizational promise is more direct: automate AI researchers, accelerate science and the economy, and give everyone a personal AGI. Noam Shazeer enters architecture research; math, statistics, and physics researchers enter science and safety teams, reflecting that model competition has expanded from "hiring more ML engineers" to "absorbing the reasoning structures of many disciplines into model R&D."

Physicist Alex Lupsasca is a case where you can watch a motive form. He had been skeptical of models. According to OpenAI's [interview with him](https://academy.openai.com/en/public/blogs/alex-lupsasca-gpt-5-pro-black-hole-physics-hidden-symmetries), GPT-5 Pro quickly completed graduate-level derivations in a test he designed and reproduced hidden-symmetry generators he had previously found. This case offers valuable expert observation, but it comes from a company interview of its own employee, so it cannot yet count as an independently verified new scientific discovery.

OpenAI also has a resource universities lack: product distribution. A paper may take years to influence a field; a model update can enter the workflows of hundreds of millions of users and many organizations immediately. Research, product, user feedback, and the next training round sit in the same system, so the lab holds both the right to produce knowledge and the right to deploy.

## Google DeepMind, Meta, xAI: three organizational answers in one magnetic field

Google DeepMind is closest to a mature version of the modern Bell Labs. AlphaGo, AlphaFold, weather, and materials research have already shown that a company lab can produce fundamental science; Google's TPUs, data, engineering platform, and distribution also provide a complete experimental apparatus. Anca Dragan, explaining part of her reason for moving into a lab, stressed the data, compute, and budget needed to advance safety at the frontier.

But a mature platform also has coordination costs. Shazeer and Jumper's departures show that holding top compute is not enough to eliminate talent flow between labs; public information is insufficient to attribute their decisions to research autonomy, team structure, compensation, or any single motive.

Meta's answer is capital, distribution, and whole-team absorption. Researchers like [Dawn Song and colleagues](https://www.techradar.com/pro/the-goal-is-not-to-replace-humans-new-meta-ai-research-chief-dawn-song-says-the-next-frontier-is-ai-agents-that-are-economically-valuable) first built Virtue AI out of a university, then the team entered Meta Superintelligence Labs. This is not simply "the university loses to big tech"; it's a "university-startup-platform" three-stage flow. Meta can give agents reach to billions of users and offer extremely generous terms; the cost is that organizational routes are centralized and adjust fast, making personal agendas more likely to be rewritten by platform strategy.

xAI, meanwhile, puts supercomputing, SpaceX-style engineering speed, and the slogan "understand the universe" together. It has strong aesthetic appeal to physicists and first-principles engineers, but the [mass departures from its founding team](https://techcrunch.com/2026/03/28/elon-musks-last-co-founder-reportedly-leaves-xai/) at least show that compute and grand missions alone don't guarantee core talent retention. Whether the specific departures stem from governance, organizational trust, or research culture, public evidence remains limited.

## Those who stay in universities or choose to found are just as important

"It's true that top talent don't found companies anymore" is not consistent with the facts.

[Yann LeCun left Meta to found AMI Labs](https://apnews.com/article/313159512bb9961f324e0c93bccf4cf5), in part because he disagreed with the mainstream LLM route; Ilya Sutskever founded [SSI](https://ssi.inc/), setting safe superintelligence as a single goal; Mira Murati and John Schulman and others chose [Thinking Machines Lab](https://thinkingmachines.ai/news/). Many so-called "startups" are simply frontier AI labs of a different form: they need billions in capital, long research timelines, and chip and cloud partnerships, and they compete for the same talent as the giants.

Terence Tao still works in academia while publicly using and evaluating AI. He supports the 2026 [Leiden Declaration](https://leidendeclaration.ai/), driven by the mathematical community and endorsed by the International Mathematical Union, which demands disclosure of AI tool use, retains human responsibility for correctness, builds public computing facilities independent of industry, and warns of corporate incentives to overstate capabilities.

Four career paths represent different combinations of rights and should not be ranked as "progress" versus "conservatism":

| Path | What it gains | What it gives up or bears |
|---|---|---|
| Join a frontier lab | strongest models, compute, talent density, deployment feedback | publication freedom, agenda autonomy, weaker public accountability |
| Found a frontier AI lab | direction and cultural control, huge equity upside | reliance on funding and compute, organizational survival risk |
| Stay in a university or public institution | long-horizon problems, public publication, talent training, critical distance | hard to reach largest training runs, slower feedback |
| Sabbatical, part-time, joint affiliation | keep a return option, bridge two institutions | conflicts of interest, split attention, opaque boundaries |

What's really happening isn't "labs defeated startups"; it's that frontier startups are being lab-ified, top academic research is being infrastructure-ified, and the boundary between them is blurring.

# Crossing (I): why now

## 1. Compute has become like a particle accelerator, not a personal computer

Stanford's [2026 AI Index](https://hai.stanford.edu/ai-index/2026-ai-index-report/research-and-development) shows that in 2025, over 90% of important AI models came from industry; since 2022, global AI computing power has grown about 3.3 times per year, reaching roughly 17.1 million H100-equivalent cards. The US has 5,427 data centers, and leading chips depend heavily on a few design companies, cloud vendors, and one major wafer foundry.

This experimental apparatus cannot be independently replicated on a single professor's funding. Outside researchers can call APIs but cannot see weights, training data, internal checkpoints, failure logs, or next-generation models. For people who study frontier capability and safety, entering a lab makes some experiments that were previously impossible become possible.

## 2. Models have entered experts' own work, not just public demos

Top scholars don't merely look at leaderboards. They use models to attack the tasks they know best, the ones hardest to fool with marketing.

When mathematicians watch research exploration speed up severalfold, physicists watch years of accumulated derivations get quickly reconstructed by models, and biologists watch AlphaFold change structure prediction, they get "local but high-confidence" private evidence. A model may still fail on common-sense questions, yet already cross the net-positive line in some high-value workflows.

This unevenness explains the outside world's confusion: ordinary users may only see a smoother chat, while domain experts see a junior research collaborator that can generate code, search hypotheses, call tools, and accept automatic verification.

## 3. Talent density becomes self-reinforcing

Strong researchers want to work with strong researchers. Each time a lab gathers more pre-training experts, systems engineers, mathematicians, safety researchers, and scientists, important work is more likely to happen there; the more concentrated the important work, the stronger the reason for the next talent to leave a university or another company to enter that lab.

This isn't just a bidding war for compensation; it's an accumulation of tacit knowledge. Many judgments in large-scale training can't be fully written into papers: when to stop a run, how to detect data contamination, which anomaly portends a capability jump, and which evaluation is being over-optimized. People who participate in real runs accumulate this experience faster.

## 4. Feedback speed rewrote "research efficiency"

University research requires applying for grants, queuing for compute, hiring students, submitting papers, and peer review; these mechanisms protect openness and quality while also making the complete cycle take months or years. A frontier lab can make multiple round-trips between researchers, engineering systems, model evaluation, and product data in a single day.

Speed itself isn't correctness. A fast-running closed team can also collectively head the wrong way. But when a problem has clear automatic feedback, whether code passes tests, whether a proof can be formally verified, whether a chip layout improves a metric, rapid iteration creates a huge advantage.

## 5. "AI helping research AI" raises the option value of an early position

If models can take on more coding, experimentation, and search, researchers can try more hypotheses per unit of time; more experiments produce training and evaluation data that help the next generation of models. This loop needn't reach a sci-fi "intelligence explosion" to let a leading organization compound by organizational efficiency.

The people in frontier labs know the loop isn't complete. Humans still set goals, choose evaluation functions, and judge whether results are trustworthy. Precisely because the answer is undecided, researchers are more willing to enter now: if the key norms, architecture, and safety habits solidify over the next three years, discussing ethics and governance a decade later may already leave very little room to influence anything.

## 6. Mission, risk, identity, and money are priced together

An already-successful professor, Nobel laureate, or CTO still cares about money. High pay and equity compensate career risk, provide security for family, and preserve the ability to later found, fund research, or exit the organization. Deleting money from the explanation would write real people as saints.

But money cannot independently explain every choice:

- some move from C-suite titles to ordinary technical roles;
- some pause their own company to return to pre-training R&D;
- some choose a safety-emphasizing lab over the highest bidder;
- some keep a professorship and probe the frontier from sabbatical;
- some abandon giant resources to found a new lab on a different route.

From public statements and career paths, one can only infer a shared set of variables: compute access, research leverage, peer density, historical window, mission identification, compensation and equity, loss of autonomy, and organizational risk. They aren't a computable formula but mutually binding thresholds. If the research question requires an internal model, compute access is near zero and nothing else can fully compensate; if the organization loses trust, no number of GPUs will necessarily keep people.

# Crossing (II): what exactly did they see

The vertical axis showed how AI became scalable cognitive production; the horizontal axis showed why talent concentrates in the few organizations that can run this production system. Where the two lines cross, five more specific judgments appear.

## They saw "the industrialization of cognitive activity"

The industrial revolution didn't invent a stronger arm; it organized energy conversion, machines, factories, and capital into a replicable production system. Frontier AI is doing something similar to part of cognitive labor: reading, coding, searching, comparing, generating candidates, calling tools, and receiving feedback are being packed into a single scalable process.

The key here isn't whether the model is human-like, but whether cognitive work can for the first time be copied, parallelized, measured, and continuously updated. A good researcher's time has only twenty-four hours a day; a model can help thousands of teams simultaneously. If quality reaches a usable threshold, even without omnipotence it will rewrite the cost structure of research and organizations.

Jobs didn't see a better phone screen; he saw fingers, software, content, and supply chains about to fuse into a new personal-computing interface. These talents don't see "how many more points the chatbot will score"; they see models, tools, verification, compute, and distribution fusing into a new cognitive infrastructure.

## They saw "the upstream of all science"

Traditional research tools serve one field: the telescope observes the universe, the sequencer reads genes, the particle accelerator probes high-energy physics. What's distinctive about a general model is that it can simultaneously read papers, write programs, design analyses, call simulations, propose candidate explanations, and migrate across mathematics, physics, biology, and engineering.

It is still far from a complete scientist, but it may become a shared upstream tool for many sciences. Whoever improves this tool may raise the research speed of many disciplines at once. For someone who wants to understand the world, that is more tempting than advancing a step further on any single problem.

This is also why mathematics and physics talent get fought over. Mathematics provides an environment with automatically checkable feedback and is a proving ground for training general reasoning; physics connects symbolic reasoning, simulation, experiment, and world models. Labs don't just need the answers they already have; they need them to define what counts as a deep problem, strong evidence, and trustworthy reasoning.

## They saw "the window for defining participation"

When a technology first enters society, many default settings aren't fixed yet: what objective the model pursues, how it obeys humans, what content it refuses, how research is made public, how gains are distributed, who can audit, and how government and companies coordinate.

A researcher joining a lab now gets not only a front-row seat on the capability curve, but a chance to influence these default settings. Safety researchers face a paradox: from the outside they can keep critical distance but find it hard to reach the strongest systems; from the inside they can observe and intervene in real risk, but are constrained by an employer's agenda, secrecy rules, and commercial pressure.

"I have to be inside to change the direction" can be a sincere mission or a self-rationalization. To judge whether it's credible, watch whether the researcher can still dissent publicly, whether the organization allows independent evaluation, and whether governance has external checks, rather than listening only to mission slogans.

## They saw "the compounding of capability," but not a certain AGI

Talent, compute, data, deployment, and AI-assisted R&D can form compounding advantages. This judgment has a factual basis: models already reduce some R&D time, and labs list automated research as an explicit route.

The stronger conclusion, that recursive self-improvement is inevitable and superhuman general intelligence will appear within years, remains a prediction. The 2026 [International AI Safety Report](https://internationalaisafetyreport.org/publication/international-ai-safety-report-2026) still stresses that existing systems show clear limits in long-horizon autonomous action, reliability, and real-world control. [Real-software development evaluations](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/) also find that experienced developers sometimes overestimate AI's help, and can even slow down due to verification and error-fixing.

Talent inflow is a signal, not proof. It shows that a set of people best positioned to observe the frontier consider the probability high enough to bet a career on it; it doesn't show the bet has won.

## They saw "getting closer to the source of power"

"Knowledge is power" tells only half the story. For knowledge to become real-world influence, it also needs execution, resources, institutions, and legitimacy. AI shortens the distance between knowledge generation and scaled action, so it raises the ceiling of several kinds of power:

| Power layer | What a frontier lab can do | What still constrains it |
|---|---|---|
| epistemic power | decide which problems get searched, verified, and explained faster | facts, peer review, domain experts, open reproduction |
| infrastructure power | allocate access to compute, models, data, and internal tools | chips, energy, cloud supply chain, capital |
| economic power | wire models into products and organizations, reorganize labor and profit | markets, competition, antitrust, customer trust |
| normative power | define model behavior through training, model constitutions, and policy | law, cultural differences, public oversight |
| agenda power | decide research budgets, public scope, and risk priorities | boards, employees, government, the public |
| coercive power | AI can amplify network, intelligence, military, and administrative capability | state monopoly on legitimate violence, legal process, international relations |

From here, "AI equals power" can be written more precisely:

> AI first amplifies **power to**, the ability to get things done; when this ability combines with model control, deployment authority, capital, coercive resources, or institutional position, it can also convert into de facto **power over**. AI won't automatically confer legitimacy, but it can significantly lower the cost of domination, manipulation, and centralized control.

Even a researcher with the strongest model cannot alone manufacture advanced chips, dispatch the grid, tax legally, or compel society to comply. Actual power belongs to a set of interdependent actors: lab governance, research teams, capital, cloud and chip companies, energy systems, states, deploying institutions, and users.

But this doesn't justify underestimating concentration risk. As frontier models substitute for more of people's coordination and execution, small groups may depend on fewer collaborators. Anthropic's Claude constitution even lists "AI or a small group, including Anthropic itself, seizing power illegally with AI" among its most severe risks; OpenAI's 2026 plan also acknowledges that a transformative technology can both concentrate and diffuse power. When the builders themselves discuss things in the language of "power," the users' intuition is not idle fantasy.

# Crossing (III): the public cost of lab-ification

## Universities lose more than the number of professors

When a professor leaves for a year, more is lost than one paper. He may mentor one fewer doctoral cohort, teach one fewer advanced course, join one fewer peer review, and maintain one fewer research direction that can endure a decade of failure. Companies preferentially invest in problems that improve models, products, safety, or policy advantage; disciplines that cannot quickly enter the training and deployment loop may find resources harder to come by.

Jennifer Chayes, dean of Berkeley's computing school, voiced a precise concern to *The Atlantic*: a university department might survive, but whether the open innovation system survives is uncertain. If the strongest models, training data, and verification results are all held by a few companies, other scientists can only see the slices companies choose to make public, and the scientific community turns from co-producer into a user of a controlled interface.

## Private research speeds discovery, and narrows the visible range

Industrial research isn't low-quality research. AlphaFold already showed a company lab can produce epochal results; concentrating engineering capability can also accomplish enormous projects universities find hard to coordinate.

The problem lies in choice: which negative results go unpublished, which safety findings stay secret, which data can't be reviewed, and which models are open only to paying customers. The Stanford AI Index points out that the strongest models have simultaneously become the most opaque; parameter counts, training data, code, and training timelines are often no longer disclosed. The stronger the research capability, the weaker the external verification, which forms an epistemic single point of failure.

## The mathematical community's warning isn't anti-technology; it's a fight over institutional design

The Leiden Declaration doesn't ask mathematicians to reject AI. It requires disclosing tool use, retaining human responsibility for correctness and citation, upholding peer review, building public computing facilities, and reminding governments not to listen only to corporate briefings.

This is an important counter-line: some top talent enter labs, while others stay outside building checking mechanisms. Both can be serious responses to the same change. If all critics enter companies, society loses independent verification; if all the cautious refuse to touch the frontier, their judgments may lag behind real capability.

A healthy system needs three roles to exist at once:

1. those who build and understand frontier systems from inside;
2. those who independently reproduce, critique, and train the next generation in universities and public institutions;
3. those who translate technical capability into rules and public choices in government, media, and social organizations.

With only the first role, AI is strong but not necessarily accountable; with only the second, public research may be right but lack experimental apparatus; with only the third, governance easily legislates around outdated imaginings.

# Scenario extrapolation: three futures and observable signals

## Baseline scenario: the lab-university hybrid persists long-term

The most likely near-to-mid-term form is increased two-way flow rather than the disappearance of universities: professors take sabbaticals into labs, researchers return to teach, companies and public bodies jointly build compute, academia takes on basic theory, talent training, and independent evaluation, and enterprises take on the largest training and deployment.

Observable signals include:

- whether industrial leaves and joint affiliations outnumber permanent departures;
- whether companies keep publishing reproducible research rather than only capability announcements;
- whether universities can obtain public computing resources and audit rights over frontier models;
- whether doctoral training still produces independent agendas that don't depend on a single company.

## Optimistic scenario: cognitive leverage diffuses rather than concentrating at the center

Model capability spreads through open weights, low-cost interfaces, public compute, and transparent evaluation; individuals and small teams gain research capability that used to belong only to large institutions. Labs keep competitive advantages while accepting external audits, incident reports, and public governance. AI accelerates science while letting more people into science.

Early signals would be:

- the capability gap between frontier and open models keeps narrowing;
- public research clouds and international computing facilities actually come into operation;
- automated results can be independently reproduced, with training data and tool use clearly disclosed;
- AI raises new researchers' output rather than only amplifying existing stars and platforms.

## Dangerous scenario: cognitive infrastructure becomes a private toll gate

A few labs control the strongest models, chip contracts, energy, talent, and distribution, and keep more AI R&D results internal. Universities cannot verify capability claims, and governments depend on the same companies for technical advice and systems. Models help central organizations act faster while weakening the bargaining power of employees, the public, and other institutions.

Warning signals include:

- training and evaluation information for important models keeps shrinking;
- key safety results appear only as abstracts that independent researchers cannot inspect;
- the gains of AI-assisted R&D mainly convert into faster closed iteration;
- professor attrition causes a sustained decline in courses, mentorship, and public papers;
- labs' safety governance depends on founder promises without enforceable external checks;
- governments bind model procurement and AI policy long-term to a very small number of vendors.

These three scenarios can coexist at different levels. Open models may diffuse everyday capability while the most frontier training stays highly concentrated; scientific tools may reach everyone while military and intelligence capability stays tightly closed. What should really be tracked is not a single "has AGI arrived," but who owns the models, who can verify, who can exit, who bears failure, and whether power has checks.

# Back to the original question: what did they see?

What they see is not a completed answer but a set of constraints changing at once:

- part of intelligence can already be trained, copied, and scaled;
- natural language is becoming the general interface connecting knowledge, code, tools, and action;
- AI has already crossed the net-benefit threshold in some expert work;
- frontier experiments increasingly depend on the complete infrastructure a few labs hold;
- AI participating in AI R&D may let organizational advantages accumulate faster;
- the next few years remain the window for defining model goals, safety norms, research institutions, and the distribution of gains.

They go to frontier labs not necessarily because "the highest intelligence" is already there, but because that is where the machine that makes the next generation of intelligence is closest at hand; not necessarily because each of them yearns to rule, but because understanding the world, changing the world, avoiding error, and gaining influence suddenly stack together at this position.

Money is real, mission is real, the appetite for power may exist, and right and wrong are not yet settled. The thing most worth taking seriously isn't their aura, but the probability judgment their career choices transmit: even if AGI is not a certain event, the probability that AI becomes the new cognitive infrastructure of science, organizations, and states is already high enough that the people with the most choices are rearranging their lives around it.

The Jobs-like "seeing" isn't knowing everything; it's seeing, while most people still think in old categories, that several originally separate systems are about to be connected. Before 2007, telephones, music, the internet, and touch still looked like different products; today, models, code, science, capital, compute, and governance are still filed in different news sections.

What this cohort is betting on is that they already belong to one story.

---

# Primary sources

## History and paradigms

1. McCulloch & Pitts, [A Logical Calculus of the Ideas Immanent in Nervous Activity](https://doi.org/10.1007/BF02478259), 1943.
2. Alan Turing, [Computing Machinery and Intelligence](https://academic.oup.com/mind/article/LIX/236/433/986238), 1950.
3. Dartmouth, [A Proposal for the Dartmouth Summer Research Project on Artificial Intelligence](https://www-formal.stanford.edu/jmc/history/dartmouth/dartmouth.html), 1955.
4. Rumelhart, Hinton & Williams, [Learning representations by back-propagating errors](https://www.nature.com/articles/323533a0), 1986.
5. Krizhevsky, Sutskever & Hinton, [ImageNet Classification with Deep Convolutional Neural Networks](https://proceedings.neurips.cc/paper/2012/hash/c399862d3b9d6b76c8436e924a68c45b-Abstract.html), 2012.
6. University of Toronto, [Google acquires University of Toronto deep learning startup](https://www.utoronto.ca/news/google-acquires-u-t-neural-networks-company), 2013.
7. Vaswani et al., [Attention Is All You Need](https://arxiv.org/abs/1706.03762), 2017.
8. OpenAI, [Introducing OpenAI](https://openai.com/index/introducing-openai/), 2015; [OpenAI LP](https://openai.com/index/openai-lp/), 2019.
9. Kaplan et al., [Scaling Laws for Neural Language Models](https://arxiv.org/abs/2001.08361), 2020.
10. Nobel Prize, [The Nobel Prize in Chemistry 2024](https://www.nobelprize.org/prizes/chemistry/2024/press-release/b/).

## 2026 talent, organization, and capability

11. UC Berkeley EECS, [Changing of the Guard: Welcoming Ana Arias as EECS Department Chair](https://eecs.berkeley.edu/news/changing-of-the-guard-welcoming-ana-arias-as-eecs-department-chair/), 2026-07-02.
12. SFGATE, [UC Berkeley AI expert leaves for Anthropic](https://www.sfgate.com/tech/article/jelani-nelson-anthropic-22329383.php), 2026-07.
13. TechCrunch, [Andrej Karpathy joins Anthropic's pre-training team](https://techcrunch.com/2026/05/19/openai-co-founder-andrej-karpathy-joins-anthropics-pre-training-team/), 2026-05-19.
14. TechCrunch, [John Jumper leaves DeepMind for Anthropic](https://techcrunch.com/2026/06/20/nobel-laureate-john-jumper-is-leaving-deepmind-for-rival-anthropic/), 2026-06-20.
15. Reuters, [Google Gemini co-lead Noam Shazeer leaves for OpenAI](https://ca.finance.yahoo.com/news/googles-gemini-co-lead-noam-002742523.html), 2026-06.
16. The Atlantic, [Where Did All the Computer-Science Professors Go?](https://www.theatlantic.com/technology/2026/07/ai-companies-hiring-academics/688002/), 2026-07-21.
17. OpenAI, [Built to benefit everyone: our plan](https://openai.com/index/built-to-benefit-everyone-our-plan/), 2026-06-08.
18. Anthropic, [Introducing our Science Blog](https://www.anthropic.com/research/introducing-anthropic-science), 2026-03-23; [Claude's Constitution](https://www.anthropic.com/constitution).
19. Stanford HAI, [2026 AI Index - Research and Development](https://hai.stanford.edu/ai-index/2026-ai-index-report/research-and-development), 2026.
20. UChicago BFI, [Attention and Money Is All You Need? Why Universities Are Struggling to Keep AI Talent](https://bfi.uchicago.edu/insights/attention-and-money-is-all-you-need-why-universities-are-struggling-to-keep-ai-talent/).
21. Harvard Crimson, [AI Wrote a Harvard Physicist's Most Recent Paper](https://www.thecrimson.com/article/2026/4/24/artificial-intelligence-theoretical-science-reckoning/), 2026-04-24.
22. OpenAI Academy, [Alex Lupsasca: black hole physics and hidden symmetries](https://academy.openai.com/en/public/blogs/alex-lupsasca-gpt-5-pro-black-hole-physics-hidden-symmetries); [Terence Tao: AI is ready for primetime in math and theoretical physics](https://academy.openai.com/en/public/blogs/terence-tao-ai-is-ready-for-primetime-in-math-and-theoretical-physics-2026-03-06).
23. Leiden Declaration, [Leiden Declaration on Artificial Intelligence and Mathematics](https://leidendeclaration.ai/), 2026-06.
24. International AI Safety Report, [International AI Safety Report 2026](https://internationalaisafetyreport.org/publication/international-ai-safety-report-2026), 2026.
25. METR, [Early-2025 AI experienced open-source developer study](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/); [Time Horizon 1.1](https://metr.org/blog/2026-1-29-time-horizon-1-1/).
26. The Information, [Workday CTO Joins Anthropic](https://www.theinformation.com/briefings/workday-cto-joins-anthropic-amid-startups-push-build-hr-apps), 2026-04.
27. Anthropic, [Introducing The Anthropic Institute](https://www.anthropic.com/news/the-anthropic-institute); [AI, R&D, and the possibility of recursive self-improvement](https://www.anthropic.com/institute/recursive-self-improvement), 2026.

> All web sources accessed on 2026-07-24. For new 2026 appointments, priority went to statements by the individual, the school, or the company; where first-hand confirmation was unavailable, two reliable media outlets were cross-checked or uncertainty was explicitly flagged.

# Methodology note

This report uses horizontal-vertical analysis:

- **Vertical analysis** traces how intelligence research was produced from 1943 to 2026: from hand-written rules, trainable representations, to scaling, AI for Science, and AI-assisted AI R&D, identifying how scarce resources and research centers changed after each paradigm shift.
- **Horizontal analysis** compares the resources, missions, talent paths, and institutional costs of Anthropic, OpenAI, Google DeepMind, Meta, xAI, startup labs, and universities in 2026.
- **Cross analysis** checks whether the two lines together explain "why these people, why now," and breaks the proposition "AI equals supreme power" into epistemic, infrastructure, economic, normative, agenda, and coercive power.

There are three research limitations. Public rosters miss undisclosed appointments and easily miswrite sabbaticals as permanent departures; companies' statements about capability and mission carry recruitment, fundraising, and policy-communication motives; and many 2026 events are still developing and cannot be verified by long-term outcomes. So the report's firm conclusions concentrate on talent flows and infrastructure changes that have already happened, and it makes only conditional judgments about automated science, recursive R&D, and AGI timelines.