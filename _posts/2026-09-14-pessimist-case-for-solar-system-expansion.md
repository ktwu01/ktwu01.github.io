---
title: "The Pessimist's Case for the Age of Cosmic Exploration"
date: 2026-09-14
permalink: /posts/2026/09/pessimist-case-for-solar-system-expansion/
tags:
  - space
  - AI
  - reflection
  - ideas
---

A laser lightsail accelerating to one percent of light speed turns about one percent of the beam into motion. The other ninety-nine percent leaves as light and does no work.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

Someone wrote an essay arguing that we live on the eve of conquering the solar system. The argument: AGI removes the local-intelligence bottleneck imposed by communication latency, covering the Moon in solar panels yields 260 TW, that power drives laser lightsail propulsion, 0.01c craft become reasonable to plan for, and the whole thing arrives in 50 to 200 years.

I worked through the numbers. The physics holds up better than I expected. The engineering pathway is where the argument has not been made.

## Give the argument its due

The 260 TW is right. Lunar radius 1,737.4 km gives a surface area of 3.79e13 m². Take 10%, multiply by the 1,361 W/m² solar constant and a 20% conversion efficiency, divide by 4 to average over day, night and incidence angle, and you get 258 TW. The essay says roughly 260 TW. Correct.

The sail thrust is right too. A perfect reflector under 260 TW gets 2P/c, about 1,734 kN. Push a 1,000 kg object with that and you get 177 g of acceleration, 0.01c in under half an hour, over an acceleration run of 0.017 AU. All of this sits inside what physics permits.

The rocket equation critique holds as well. Chemical propulsion cannot take meaningful mass to 0.01c.

So the disagreement is not about whether the energy exists. It is about everything that has to happen between having the energy and having a working industrial system.

## The bill is denominated in square meters

"Cover 10% of the Moon in solar panels" is one assumption in the original. It is also the single largest construction project in the argument.

A tenth of the lunar surface is 3.79 million square kilometers, larger than India.

The twelve module suppliers in InfoLink's 2025 ranking shipped a combined 536 GW ([InfoLink 2025 global module shipment ranking](https://www.infolink-group.com/energy-article/solar-topic-infolink-2025-global-module-shipment-ranking-combined-shipments-reach-536-gw)). That is not world output. Aiko, Risen and First Solar sit outside the ranking, so the global figure is higher and every year count below is an upper bound. At the 20% efficiency the original assumes, roughly 200 W per square meter, 536 GW is about 2.7 billion square meters a year. Hold that rate fixed and covering the area takes about 1,415 years.

I want to be careful about what that number does and does not show, because the obvious reply is a good one and I will come back to it.

The mass side is harder to wave away. Terrestrial modules with glass and frame run over 10 kg/m². Grant the Moon an extravagantly generous 0.1 kg/m², thin film with no glass and no frame, and the total is still 379 million tonnes. The International Space Station masses 420 tonnes. This is roughly 900,000 of them, and none of that counts mounting, wiring, power conditioning or the machines that do the installing.

## Silicon is reduced with carbon, and the Moon has very little

Building panels locally runs into chemistry.

Industrial silicon comes from carbothermic reduction: silica plus carbon at around 1,900 °C yields silicon and carbon monoxide, consuming about 0.855 kg of carbon per kg of silicon. Purification to solar grade then runs the Siemens process, which needs trichlorosilane, hydrogen and chlorine.

Carbon in lunar regolith measures about 100 ppm in bulk Apollo soils, with a range of 1 to 250 ppm, and it is almost entirely implanted by the solar wind. With no atmosphere and no hydrosphere, the Moon has no mechanism to sequester carbon as carbonate rock ([Cannon, Accessible Carbon on the Moon](https://arxiv.org/pdf/2104.13521)).

At 100 ppm, collecting the carbon for one tonne of silicon, once through with no recovery, means processing about 8,550 tonnes of regolith. Polar volatiles are far richer: the LCROSS impact plume implied roughly 5,000 ppm elemental carbon at the site, which improves the ratio to about 171, once you have established a mining industry inside a permanently shadowed crater at 40 K.

Two honest caveats. The reaction does consume the carbon, which leaves as carbon monoxide, but that CO can in principle be reduced and the carbon returned to the furnace, so a closed loop needs far less fresh carbon than once-through operation. The recovery step costs energy and equipment of its own. And carbothermic reduction is not the only route to silicon; molten regolith electrolysis avoids carbon altogether and has been studied for exactly this reason.

What none of those alternatives has done is produce a square meter of working panel from lunar feedstock. The demonstrated state of the art is gram-scale and square-centimeter-scale laboratory samples. The material path to 3.79 million square kilometers is not a detail left to implementation.

## A sail is an energy converter that runs at one percent

Lightsails carry an efficiency term the original omits.

The instantaneous energy efficiency of a photon sail is about 2v/c, and averaged across the whole burn it comes out to approximately v/c. At 0.01c the exact expression gives 0.995%. Round it to one percent. The remaining 99% of the beam energy leaves as light.

So the energy bill per shipment is close to m·c·v/2. Sending 100 tonnes to 0.01c costs 4.49e19 joules, or about 12,500 TWh. Humanity generates roughly 30,000 TWh of electricity per year. One 100-tonne one-way delivery is five months of Earth's entire electrical output.

The 260 TW array produces 2.28 million TWh per year. Spend every photon of it on acceleration and you get about 18,000 tonnes a year to 0.01c. That figure is accelerated mass, sail and vehicle included, with nothing held back for braking at the far end and no allowance for conversion or beam losses, so delivered cargo is some fraction of it. A mid-size bulk carrier holds 50,000 tonnes.

The original gives a range, 0.001c to 0.01c, and the low end is ten times better: roughly 182,000 tonnes a year, because the energy cost scales with the square of the speed while the efficiency penalty scales with the speed. That is a real answer to this objection, and it is the answer I would give in the original's place. It also concedes the point that 0.01c is the expensive choice rather than the natural one.

Which raises the question of what 0.01c buys. The original wants freight measured in days and weeks, and 0.01c delivers exactly that, so the speed is a stated requirement and not an arbitrary one. The question is the price. A Hohmann departure from low Earth orbit is about 3.6 km/s to Mars and about 6.3 km/s to Jupiter; 0.01c is 2,998 km/s, 833 and 476 times those numbers, at an energy cost rising with the square. Buying transit time at that exchange rate pays off only where transit time is the binding constraint. For a cargo run it rarely is. What makes Mars hard is what the cargo arrives to: no power, no repair, no spares and no factory.

The scale of the hardware follows from that choice. Starshot has a real cost model: $8.0B of beam director capital cost, made up of $2.0B of lasers at 200 GW maximum transmitted power, $2.8B of optics at a 2.7 km effective primary diameter, and $3.1B of energy storage, pushing a 3.6 gram sailcraft carrying a 1 gram payload on a 4.1 m sail ([Parkin, Starshot System Model](https://parkinresearch.com/wp-content/uploads/2018/07/starshotmodel.pdf)). That 200 GW is transmitted optical power in a design aimed at 0.2c. The lunar 260 TW is generated electrical power, so comparing them needs a wall-plug efficiency in between. Even at a generous 50% conversion the lunar beam is still more than six hundred times Starshot's.

The sail material does not exist yet either. Atwater's group at Caltech framed this as an open materials problem in Nature Materials in 2018: the sail needs near-zero absorption in the laser band and high enough emissivity to radiate away whatever it does absorb ([Atwater et al., Nature Materials 17, 861-867](https://www.nature.com/articles/s41563-018-0075-8)). Work since has stayed at the scale of thin-film samples.

## What actually killed the hardware was dust

The original's core claim is that communication latency capped local intelligence, AGI removes the latency, and large-scale autonomous construction therefore becomes possible. Grant the whole claim. The machines still have to survive.

InSight's solar panels produced roughly 5,000 watt-hours per sol after landing on Mars in 2018. By spring 2022 dust had cut that to about 500 ([NASA on InSight's power generation](https://science.nasa.gov/resource/insights-power-generation-after-landing-and-spring-2022/)). Ninety percent of the power, gone, to dust settling on glass.

Lunar dust is worse, and the Apollo record is specific about how. NASA sorted the effects into nine categories: vision obscuration, false instrument readings, coating and contamination, loss of traction, clogging of mechanisms, abrasion, thermal control problems, seal failures, and inhalation ([Gaier, NASA TM-2005-213610](https://ntrs.nasa.gov/api/citations/20050160460/downloads/20050160460.pdf)).

The detail that matters for a construction argument is the timescale. Apollo surface stays ran from 21 to 75 hours, and components were already approaching failure. Pete Conrad's suits were more worn after 8 hours of surface activity than his training suits were after 100, worn through the outer layer into the insulation above the boot; one or two more EVAs could have caused a pressure failure. His suit leak rate went from tight to 0.15 psi/min after the first EVA and 0.25 after the second, against a 0.30 safety limit, so a third EVA was doubtful. Gauge dials on Apollo 16 were scratched until they could not be read. The cover gloves used on the core drill were worn through after two EVAs and discarded at the start of the third. Every environmental and gas sample seal failed because of dust, and the samples reached Earth too contaminated to be worth anything.

Dust on radiator surfaces could not be removed. Apollo 12's magnetometer ran about 68 °F hotter than expected because of it, and the Apollo 16 and 17 rover batteries exceeded their temperature limits. John Young spent much of Apollo 16 trying to brush dust off the batteries and later called dust the number one concern in returning to the Moon.

The line in that report I keep returning to: brushing worked much better in ground tests than it did on the Moon. That is the failure mode of the whole optimistic genre. The simulation was fine.

Hours of operation degraded Apollo hardware measurably. The original does not need any single machine to last decades, because it proposes repair and local manufacturing, and that is the right answer to give. What it does need is repair and replacement throughput that stays ahead of a wear rate this high. Every gram of replacement mass, every hour of repair, and every part the local foundry cannot yet make is drawn from the same industrial capacity that is supposed to be covering 3.79 million square kilometers. Better cognition does not reduce the wear, because the wear is in bearings, seals, lubricants and coatings.

## The chip is the hardest thing to deliver

The chain rests on one sentence in the original: carry a chip, and you carry powerful intelligence directly there.

Space processors are generations behind. The RAD5545 runs at 45 nm, draws about 20 W and delivers 3.7 GFLOPS. That is the radiation-tolerant part, not the frontier part, and the distance between them is the point.

I want to state the radiation tradeoff more carefully than I first did. It is true that smaller geometries hold less critical charge per storage node, which all else equal invites more single-event upsets. It is not true that advanced nodes are simply more fragile: FinFET geometries have shown reduced sensitivity to some single-event effects, and modern parts lean on error correction and redundancy. The obstacle sits in the qualification pipeline. Space-rated silicon certifies years behind the commercial process, and running frontier inference on a decade-old node is a different proposition from running it on current hardware.

Cooling is a genuine constraint and I had the geometry backwards on first pass. In vacuum, final heat rejection happens by radiation only. Lunar noon ground runs about 390 K, radiating about 1,312 W/m² as a blackbody and about 1,181 W/m² at the emissivity 0.9 I use for the radiator itself. That is why a vertical radiator facing the ground is the bad configuration: it has a large view factor to the hot surface and needs working fluid above roughly 325 K before it rejects any net heat at all. The fix is geometric and well understood. The upward face of a horizontal radiator has essentially no view of the ground ([NASA lunar radiator study](https://ntrs.nasa.gov/citations/20130013573)). Shaded, facing the sky, a surface at 350 K with emissivity 0.9 rejects about 766 W/m², so a megawatt of compute needs on the order of 1,300 m² of sky-facing radiator.

1,300 square meters per megawatt is not a wall. It is a mass and area budget, and it belongs in the ledger alongside the panels, which is where the original does not put it.

## The strongest version of the optimist's reply

Here is the objection I find hardest, and it is aimed straight at my own arithmetic.

Dividing a fixed target by today's production rate is exactly the denominator trick I accused the original of. Industrial capacity is not fixed. Apply 5% annual growth to solar output and my 1,415 fixed-output years becomes about 88 calendar years. At 3% it is about 128. Both land inside the original's 50 to 200 year window. The whole point of the bootstrapping story is that you ship seed equipment, the seed equipment builds more equipment, bulk material stays local, and only scarce components come from Earth. Under that model, the correct quantity is the net reproduction rate of a lunar industrial system after maintenance and replacement. Total mass over current shipping capacity measures something else.

That reply is correct, and it means the honest version of my thesis is narrower than the one I started with. I cannot show that this is impossible in 50 to 200 years. Nobody can.

What I can say is that the reply relocates the argument rather than winning it. A self-expanding industrial system needs its replacement rate to exceed its wear rate, and every specific thing we know about operating machinery on the lunar surface bears on that one inequality. Apollo hardware degraded measurably in 21 to 75 hours. Brushing failed in the field after working in the lab. The seals failed. That is the number the original needs and never estimates: how much of its own maintenance a lunar factory can cover before it needs another shipment. A terawatt figure does not answer it.

Energy abundance is the part of this story that was never really in doubt. Sunlight has been falling on the Moon for four billion years.

## A 260 TW laser is also a weapon

One thing the original never raises. A directed-energy installation delivering 260 TW focused 0.017 AU downrange would be the most powerful weapon humans have ever built, by a wide margin, and the hardware does not distinguish between a cargo sail and a target.

Article IV of the Outer Space Treaty states that the Moon and other celestial bodies shall be used "exclusively for peaceful purposes," and forbids military bases, installations and fortifications, along with the testing of any type of weapon ([UNOOSA treaty text](https://www.unoosa.org/oosa/en/ourwork/spacelaw/treaties/outerspacetreaty.html)).

The original never says who owns the array, or whether its output is ever concentrated into a single steerable beam. Those details decide whether the thing reads as infrastructure or as armament, the question has no technical answer, and it is a live constraint on whether it gets built at all.

## What would change my mind

The original does name its pieces: fission, communications, robotics, charging, manufacturing, repair, braking at the destination. What it does not do is cost any of them. The binding constraints sit in materials, maintenance throughput, and whether a local industrial base can reproduce itself faster than it wears out.

For scale against present reality: NASA's lunar fission effort was restructured in August 2025 around a target of at least 100 kilowatts electric, ready for launch by late 2029, up from the previous 40 kilowatt design aimed at the mid-2030s ([Scientific American on the directive](https://www.scientificamerican.com/article/nasa-boosts-plans-for-nuclear-reactor-on-the-moon/)). The original assumes a megawatt-class reactor, ten times that minimum. The last time humans went to the Moon was 1972.

Four results would move my estimate substantially.

First, a square-meter-scale solar cell above 10% efficiency made entirely from lunar regolith, with no carbon, chlorine or hydrogen imported from Earth.

Second, a machine operating autonomously on the lunar surface for over an Earth year, across at least 13 lunar nights, with no spare parts shipped from home. That tests bearings, seals and lubricants, and it is the closest thing to a direct measurement of the reproduction-versus-wear inequality.

Third, the gap between radiation-qualified and leading-edge process nodes narrowing to within a generation or two, or a fault-tolerant architecture that sustains large-model inference in the lunar radiation environment.

Fourth, sail absorptivity in the laser band meeting design requirements at meter scale, under the corresponding power density.

Any one of those advances this more than another essay about 260 TW.

The most appealing thing about the original is its faith that whatever physics permits will eventually get built. Physics does permit it. The question the essay skips is the one every actual machine on the lunar surface has answered badly so far: whether the hardware lasts long enough to spend the energy. Whether the energy is there was never the hard part.

**Related posts:**
- [中文版：宇宙大航海时代的悲观论点]({{ site.baseurl }}/zh/posts/2026/09/pessimist-case-for-solar-system-expansion/)
- [Passing On Spiritual Genes]({{ site.baseurl }}/posts/2026/09/passing-on-spiritual-genes/), which discusses Musk wanting to propagate all of human civilization.
