---
title: "Energy Singularity and the Intelligence Revolution: An In-Depth Research Report on Controlled Nuclear Fusion, Its Principles, Commercialization, and Sam Altman's Strategic Bet"
date: 2026-01-05
permalink: /posts/2026/01/nuclear-fusion-singularity/
tags:
  - energy
  - nuclear-fusion
  - ai
  - sam-altman
  - deep-dive
---
At the end of AI's compute road lies the ultimate solution to energy.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

# Energy Singularity and the Intelligence Revolution: An In-Depth Research Report on Controlled Nuclear Fusion, Its Principles, Commercialization, and Sam Altman's Strategic Bet

## 1. Executive Summary

At the dawn of 2026, the global energy and technology industry stands at a historic crossroads. Controlled Nuclear Fusion, the scientific holy grail once dismissed as "always thirty years away," is undergoing a violent paradigm shift from pure theoretical physics experiments to hard-tech engineering deployment. This report aims to provide a detailed breakdown and analysis of controlled fusion's physical principles, technical paths, engineering bottlenecks, and commercial prospects, while delving deeply into why OpenAI CEO Sam Altman is betting his personal fortune and reputation heavily on this field, and the deeper logic behind that support.

The current R&D landscape of fusion energy shows a clear bifurcation: on one side are the public sectors represented by ITER (the International Thermonuclear Experimental Reactor) and Chinese national projects (like CFETR), committed to conquering the engineering challenges of deuterium-tritium (D-T) fusion in pursuit of large-scale, steady-state baseload power; on the other side are private companies like Helion Energy and Commonwealth Fusion Systems (CFS), which use high-temperature superconductors, advanced algorithms, and novel confinement configurations to attempt a commercial breakthrough through more compact, faster iteration.

The report's core finding holds that Sam Altman's investment in fusion, especially in Helion Energy, is not a purely financial move but an indispensable part of his grand AGI strategy. As model parameters and compute demand grow exponentially, "the cost of intelligence" will eventually converge on "the cost of energy." Altman's heavy support of Helion, reflected in hundreds of millions of dollars of real money and the signing of a Microsoft power purchase agreement, is real and aggressive. However, this bet faces enormous physics and engineering uncertainty, particularly Helion's magneto-inertial confinement and deuterium-helium-3 fuel cycle. Though theoretically offering extremely high economics (direct electrical capture), it still had not fully delivered on its public "net electricity" promise during 2025-2026.

The report is divided into seven major chapters, comprehensively covering every dimension from nuclear physics to the underlying supply chain, and from geopolitical competition to Silicon Valley capital logic.

---

## 2. The Physics and Core Challenges of Controlled Nuclear Fusion

Fusion is the dominant energy-generation mechanism in the universe, powering the stars. Reproducing this process on Earth requires overcoming extreme physical conditions, combining light atomic nuclei into heavier ones while releasing enormous binding energy.

### 2.1 The Basic Physical Mechanism and the Coulomb Barrier

The essence of fusion is applying Einstein's mass-energy equation $$E=mc^2$$ to release energy through mass deficit. The most basic reactions involve hydrogen isotopes. However, atomic nuclei carry positive charge and exert a strong electrostatic repulsion (the Coulomb force) on each other. For fusion to occur, nuclei must approach closely enough (on the Fermi scale, $$10^{-15}$$ meters) for the short-range strong nuclear force to overcome the long-range electromagnetic repulsion.

This requires the fuel to be in a plasma state (electrons detached from nuclei) with extremely high kinetic energy. The criterion for whether fusion occurs is called the **Lawson Criterion**, or the "Triple Product," meaning the product of the following three parameters must exceed a certain threshold:

1. **Density ($$n$$)**: the number of particles per unit volume.

2. **Temperature ($$T$$)**: usually measured in kilo-electronvolts (keV) or hundreds of millions of degrees Celsius.

3. **Energy confinement time ($$\tau_E$$)**: how long energy remains in the plasma.

The goal is to achieve an energy gain factor $$Q > 1$$, i.e., the energy produced by fusion exceeds the input energy needed to sustain the plasma. When $$Q$$ tends to infinity, the alpha particles produced by the fusion reaction suffice to maintain the plasma temperature without external heating; this is called **Ignition**.

### 2.2 Fuel Cycle: The Fork in the Engineering Road

Which fuel combination you choose directly determines the reactor's physical design, engineering difficulty, and economic model. This is the key to understanding the difference between Helion and the mainstream tokamak route.

**Table 1: Comparison of the physical characteristics and engineering impact of major fusion fuel cycles**

|**Fuel cycle**|**Reaction**|**Ignition temperature requirement**|**Neutron yield & energy**|**Pros**|**Cons**|
|---|---|---|---|---|---|
|**Deuterium-tritium (D-T)**|$$^2H + ^3H \rightarrow ^4He + n$$|~150 million °C (15 keV)|**Extremely high** (80% of energy as 14.1 MeV neutrons)|Largest reaction cross-section (easiest to occur); high energy output.|Needs tritium breeding (tritium is naturally scarce); high-energy neutrons severely damage materials; must use a steam turbine cycle.|
|**Deuterium-deuterium (D-D)**|$$^2H + ^2H \rightarrow ^3He + n$$ or $$T + p$$|~500 million °C|Moderate|Extremely abundant fuel source (seawater); no initial tritium needed.|Low reaction cross-section; still produces significant neutron radiation.|
|**Deuterium-helium-3 (D-He3)**|$$^2H + ^3He \rightarrow ^4He + p$$|~600-1000 million °C|**Extremely low** (<5% of energy as neutrons)|**Neutron-free potential**; products are mainly charged protons, enabling **direct electricity generation**; low radiation.|Helium-3 is extremely scarce on Earth; ignition temperature is extremely high and confinement is extremely difficult.|
|**Proton-boron-11 (p-B11)**|$$p + ^{11}B \rightarrow 3 ^4He$$|~1 billion °C|Nearly zero|Abundant fuel; completely neutron-free; clean products.|Physically extremely hard to achieve; bremsstrahlung losses may exceed fusion output.|

_Analysis:_ Currently, ITER, CFS (SPARC), and most Chinese projects adopt the **D-T** route because it has the lowest physical threshold. However, the high-energy neutrons released by the D-T reaction cannot be confined by magnetic fields; they bombard the reactor wall directly, requiring a bulky "breeding blanket" to absorb neutrons and convert heat into steam, which then drives a turbine to generate electricity. This process is extremely complex engineering-wise, and its efficiency is limited by the Carnot cycle. By contrast, Helion chose the **D-He3** route, aiming to use the charged products for magnetically-induced direct electricity generation, which offers enormous system-simplification advantages for large-scale commercialization, but the physical difficulty rises exponentially.

### 2.3 The Evolution of Confinement Methods: From Magnetic to Inertial

#### 2.3.1 Magnetic Confinement Fusion (MCF)

Exploits the property of charged particles to spiral in a magnetic field to confine them within a specific geometry.

- **Tokamak**: shaped like a doughnut (toroidal). Uses an external toroidal magnetic field combined with the poloidal field generated by the plasma's internal current to synthesize a helical magnetic field that confines the plasma.

    - _Status_: the most mature technology; ITER and China's EAST and HL-3 all belong to this category.

    - _Limitation_: the plasma current can cause kink-mode instabilities, triggering "disruptions" that release enormous energy in an instant, potentially damaging the device.

- **Stellarator**: relies entirely on externally twisted coils to produce the helical magnetic field, needing no plasma current.

    - _Status_: represented by Germany's W7-X.

    - _Advantage_: inherently stable, suitable for steady-state operation.

    - _Limitation_: the magnet design and manufacturing process are extremely complex.

#### 2.3.2 Inertial Confinement Fusion (ICF)

Uses high-energy drivers (lasers or ion beams) to bombard tiny fuel pellets, causing their outer layer to ablate and explode instantly, producing a reverse shockwave that compresses the fuel inward to extremely high density.

- _Status_: the US National Ignition Facility (NIF) achieved scientific gain (Q>1) in 2022.

- _Limitation_: extremely low pulse frequency (a few times per day), low laser efficiency, making it hard to convert into continuous electrical power.

#### 2.3.3 Magneto-Inertial Fusion (MIF): The Third Path

Combines MCF's magnetic thermal insulation with ICF's pulsed compression.

- _Principle_: first generate a magnetized plasma blob (like a field-reversed configuration, FRC), then rapidly compress it with magnetic fields.

- _Representative_: **Helion Energy**.

- _Advantage_: can achieve higher density than a tokamak while having longer confinement time than laser fusion. Most critically, the pulsed compression-expansion process is naturally suited to direct electrical-energy recovery.

---

## 3. Global Development Landscape and Geopolitical-Technological Competition

By 2026, fusion is no longer purely scientific collaboration; it has evolved into a complex battlefield of national strategic competition and private capital games.

### 3.1 The National Teams: Giants Advancing and Stalling

**ITER (International Thermonuclear Experimental Reactor)**:

As a giant project involving seven parties (EU, China, US, Russia, and others), ITER aims to validate the engineering feasibility of a fusion reactor.

- _2026 status_: the project is heavily burdened by delays. Although most civil construction and core component installation are complete, the projected deuterium-tritium operation has been pushed back to 2039, and D-D plasma experiments to 2035. ITER's sheer scale makes it unable to match private companies in flexibility, but its foundational research in material irradiation and tritium breeding blanket testing (TBM) remains irreplaceable.

**China's strategic acceleration**:

China treats fusion as the ultimate guarantee of energy security and has set out a clear "three-step" strategy (thermal reactors - fast reactors - fusion reactors) at the national level.

- **Device breakthroughs**: in 2025, the new-generation artificial sun **HL-3 (Huanliu-3)** achieved 1 million amps of current operation, with core ion temperature exceeding 100 million degrees; **EAST (Experimental Advanced Superconducting Tokamak)** set a world record in January 2025 of sustaining plasma operation for 1066 seconds.

- **Institutional innovation**: in mid-2025, China formally established the national platform **China Fusion Energy Co Ltd**, led by CNNC (China National Nuclear Corporation), integrating 25 central state-owned enterprises and research institutions including the Chinese Academy of Sciences and China Three Gorges Corporation, aiming to accelerate construction of **CFETR (China Fusion Engineering Test Reactor)** under the national system. CFETR's goal is to be built between 2030-2035, achieving not only burning plasma but solving the key engineering challenge of tritium self-sufficiency.

- **Hybrid reactor path**: China is reportedly also advancing fusion-fission hybrid projects (like the "Xinghuo" project in Jiangxi), using fusion-generated neutrons to drive fissile materials, seen as a compromise route to earlier commercial application.

### 3.2 The Private Sector (Fusion 2.0): Capital-Driven Agile Development

As of 2025, total funding for global private fusion companies had approached $10 billion. These companies adopt the Silicon Valley "fail fast, iterate fast" model.

**Table 2: Comparison of technology routes and 2026 status of major global private fusion companies**

|**Company**|**HQ**|**Technical route**|**Key differentiator**|**2026 expected status/milestone**|**Notable investors**|
|---|---|---|---|---|---|
|**Helion Energy**|USA|Pulsed magneto-inertial (MIF) + FRC|Deuterium-helium-3 fuel; **direct electricity generation**; no steam cycle; factory mass-production model.|Original 2024 net-power goal not met; Polaris prototype in commissioning; pursuing power for Microsoft by 2028.|Sam Altman, Peter Thiel, Microsoft|
|**Commonwealth Fusion Systems (CFS)**|USA|Compact tokamak (SPARC)|High-temperature superconducting magnets (REBCO); strong field shrinks size; traditional D-T thermal cycle.|SPARC device under assembly; expected first plasma and Q>1 validation in 2026/2027.|Bill Gates, Google, MIT|
|**Tokamak Energy**|UK|Spherical tokamak|High-temperature superconductor; spherical configuration raises beta (efficiency).|Advancing ST80-HTS prototype; magnet technology validation.|UK government, private equity|
|**Zap Energy**|USA|Z-Pinch|No magnet coils; shear-flow stabilization of plasma; extremely simple structure.|Validating "shear-flow stabilization" at higher currents; no expensive magnets needed.|Chevron, Bill Gates|
|**General Fusion**|Canada|Magnetized target fusion (MTF)|Liquid-metal (lead-lithium) liner; piston compression; liquid wall protection.|Building LM26 demonstration unit in the UK; validating liquid-metal compression efficiency.|Jeff Bezos|

---

## 4. Engineering Bottlenecks: From Physical Feasibility to Commercial Feasibility

Even if $$Q>1$$ is achieved physically (as NIF has done), a commercial fusion power plant still faces three "gray rhino"-class engineering challenges. Private companies often downplay these in their marketing, but they are fundamental to success or failure.

### 4.1 The Material "Neutron Nightmare"

In D-T fusion, 80% of the energy is released as 14.1 MeV high-energy neutrons. That's over 10 times the energy of fission reactor neutrons.

- **Atomic displacement (dpa)**: high-energy neutrons strike the lattice atoms of reactor wall materials, displacing them. Over their service life, every atom may be knocked out of place hundreds of times. This causes embrittlement, swelling, and fracture.

- **Activation**: neutron bombardment turns non-radioactive structural materials (like steel) into radioactive waste.

- _Status_: no material currently exists that can survive long-term at the flux required by a commercial fusion reactor. Projects like IFMIF (International Fusion Materials Irradiation Facility) are under construction, but materials science lags severely behind plasma physics.

### 4.2 Tritium Breeding: Closing the Fuel Cycle

Tritium has a half-life of only 12.3 years, and there's almost no natural tritium on Earth. Current tritium mainly comes as a byproduct of heavy-water reactors (CANDU), with a global stock of only about 25-30 kg, and it's extremely expensive (about $30,000 per gram).

- **Breeding blanket**: a commercial D-T reactor must be "self-sufficient," using fusion-generated neutrons reacting with lithium to produce tritium ($$n + ^6Li \rightarrow T + ^4He$$).

- **Challenge**: the tritium breeding ratio (TBR) must be greater than 1. That means not only capturing every neutron but making up for the neutrons lost in structural materials. This technology has never been validated in a full-scale reactor.

- _Note_: this is also the core reason Helion chose the D-He3 route, to try to bypass the tritium breeding and neutron damage problems, though it faces the new problem of the helium-3 source.

### 4.3 Heat Extraction and Economics

A tokamak uses a divertor to exhaust waste heat and helium ash. The divertor target plate faces thermal loads that can exceed $$10-20 MW/m^2$$, several times the thermal load of a space shuttle re-entering the atmosphere, and it must operate continuously. Moreover, to compete with solar-plus-storage, fusion electricity would need to fall below $50/MWh. The enormous capex of a bulky tokamak plus steam turbine system makes companies like CFS pursue extreme compactness, while Helion pursues system simplification through direct electricity generation.

---

## 5. Deep Dive: Sam Altman, Helion Energy, and the Strategic Tie to AI

Sam Altman isn't just an investor in Helion; he's the builder of its business narrative. To understand this support, you must place it within Altman's vision of the future world: an era of both unlimited compute and unlimited energy.

### 5.1 Helion Energy's Technological Distinctiveness

Helion's technical path (magneto-inertial confinement + D-He3 + direct electricity generation) is an absolute outlier in the fusion field.

1. **Field-Reversed Configuration (FRC)**: Helion doesn't use a tokamak's external coils to force confinement. Instead, it generates two plasma blobs (FRCs) like smoke rings that carry their own current and produce their own magnetic field.

2. **Pulsed collision and compression**: the two FRCs collide and merge at the center of the burn chamber at 1 million miles per hour, then are compressed by external magnetic fields to extremely high density and temperature within microseconds.

3. **Direct energy capture**: this is Helion's "killer move." When fusion occurs, the charged products (protons and alpha particles) push the plasma to expand, which pushes back against the magnetic field. By Faraday's law of electromagnetic induction, the changing magnetic flux induces a current in the external coils.

    - _Significance_: this makes electricity generation as efficient as regenerative braking, with a theoretical conversion efficiency of 95%, and no expensive steam turbine or cooling tower needed.

4. **Helium-3 source**: Helion plans to self-produce helium-3 through the D-D side reaction (the D+D reaction has a 50% chance of producing helium-3 and 50% of producing tritium, and tritium decays into helium-3 too). This closes the fuel loop, but it also means early on they still have to handle the neutrons produced by the D-D reaction.

### 5.2 The Deeper Logic of Sam Altman's Support: AI's Physical Limit

Why fusion? Why Helion?

The "why the heavy support" question can be reduced to three core strands of logic:

1. **The compute-energy equivalence thesis**: Altman has stated plainly in Senate hearings and multiple interviews: "Without an energy breakthrough, AGI (artificial general intelligence) cannot be achieved."

    - _Data support_: as model parameter counts and training data grow exponentially, and as inference is applied at scale, AI data-center energy consumption is exploding. A single ChatGPT query consumes 10-100 times the energy of a traditional Google search.

    - _Vision_: Altman believes future intelligence costs will be determined by energy costs. If energy doesn't fall like Moore's Law, AI's proliferation will be blocked.

2. **Manufacturing rather than construction**:

    Another reason Altman prefers Helion is its engineering philosophy.

    - A tokamak (like ITER or CFS) is a civil-engineering project akin to a nuclear power plant, with long construction cycles and complex regulation.

    - Helion's device (Polaris) is the size of a shipping container and consists of thousands of standardized capacitors and magnets. That means they can be mass-produced in a factory, then shipped and installed next to a data center. This fits the Silicon Valley investment logic of "software-defined hardware" and "scalability first."

3. **Matching time windows**: Renewables (wind and solar) are cheap, but even with storage they struggle to meet the 24/7 stability requirement ("Five Nines" reliability) of gigawatt-scale data centers. Fission is stable but approvals and construction take a decade or more. Helion's promised 2028 delivery, though aggressive, is on the timeline the only baseload power source that matches OpenAI's compute-cluster expansion plan.

### 5.3 Did He Really "Heavily Support" It? A Fact Check

**Conclusion: yes, the support is unprecedented, and carries exclusive strategic significance.**

- **Real money invested**:

    - In 2021, Altman personally invested **$375 million** in Helion (Series E). It was at the time his largest single personal investment, far exceeding his stakes in other startups.

    - In January 2025, Helion announced a **$425 million** Series F, and Altman followed on again while continuing to serve as board chair.

- **Reputation bet and business tie-in**:

    - Altman brokered the **Microsoft-Helion power purchase agreement (PPA)**. The agreement requires Helion to deliver 50 MW of power to Microsoft starting in 2028. This isn't just a letter of intent; it's a formal commercial contract with penalty clauses. Microsoft, OpenAI's biggest backer, means this contract effectively ties OpenAI's compute fate to Helion's success or failure through Altman.

    - At the 2025 Senate hearing, Altman publicly endorsed Helion as key infrastructure for America to stay competitive in the AI era.

### 5.4 Status Check: The Gap Between Promise and Reality (2025-2026)

The support is real, but is the technical progress what was hoped?

- **Missed milestone**: Helion loudly promised in 2021 that its 7th-generation prototype **Polaris** would demonstrate "net electricity" in 2024. As of early 2026, that goal **has not been achieved**.

- **Current status**: Polaris was completed at the end of 2024 and began running in mid-2025, producing large FRC plasmas, but has not publicly announced net electrical output.

- **Outside skepticism**: physics circles criticize Helion for never publishing enough data in peer-reviewed journals. The temperature required for D-He3 is far higher than D-T (nearly 1 billion degrees), and FRC stability under such extreme conditions is considered extremely difficult in mainstream plasma physics. Some critics argue Helion's aggressive timeline carries typical "Silicon Valley exaggeration" (like Theranos), exploiting the venture circle's ignorance of physics to fundraise.

- **Defense**: Helion's supporters argue they withhold data to protect intellectual property (preventing competitors from copying it), and that the completion of the Series F shows that, despite the delayed public milestone, the internal data was enough to persuade SoftBank and Altman to keep injecting capital.

---

## 6. Applications and Future Development Prospects

If (a big "if") nuclear fusion, especially compact solutions like Helion's, succeeds, the impact will extend beyond the electricity industry.

### 6.1 Deep Decarbonization and Baseload Power

This is the most direct application. A fusion plant can provide stable baseload power like a coal plant, but with zero carbon emissions. For countries with huge heavy industries (steel, chemicals) and megacities (like China), fusion is the ultimate substitute for fossil energy.

### 6.2 Industrial Heat and Hydrogen Production

High-temperature superconducting tokamaks and Helion's waste heat (even with direct generation there are thermal losses) can be used for high-temperature electrolysis of water into hydrogen or directly driving industrial processes, further replacing natural gas.

### 6.3 Space Propulsion

Helion's technology (magnetically pulsed jet) is essentially a plasma engine. With some modification, it could serve as a high-specific-impulse, high-thrust space thruster, shrinking the human round-trip time to Mars from months to weeks. This is also the long-term vision Helion founder David Kirtley frequently mentions.

### 6.4 Economic Restructuring

Cheap, unlimited energy would make desalination, vertical farming, and carbon capture (direct air capture) economically viable, technologies currently prevented from scaling by their high energy consumption. As Altman puts it, this would lead to "the marginal cost of matter trending toward zero."

---

## 7. Conclusion

Controlled nuclear fusion in 2026 is at the most chaotic moment before dawn.

**Technically**: the physics has been scientifically validated (NIF's ignition, tokamak high-confinement mode), but the engineering gap (materials, tritium, thermal loads) remains bottomless. China is steadily advancing the traditional tokamak route through its national system, offering the highest-certainty fallback; meanwhile, US private companies led by Helion are running a high-risk gamble, trying to dodge engineering problems through innovation in the physical mechanism.

**Altman's role**: Sam Altman's heavy support is beyond doubt. He isn't passively waiting for the tech to mature; he's trying to force-grow a technology with huge capital and market orders. His bet rests on two judgments: first, AI's hunger for energy will soon exhaust the existing grid's potential; second, only a fusion solution like Helion's, which can be factory-manufactured and generates electricity directly, can keep pace with AI's exponential expansion.

**Final outlook**: Helion missed the 2024 deadline, which isn't unusual in hard-tech startups, but it also raises the risk. The next 2-3 years (2026-2028) will be decisive. If Polaris achieves net electricity, or CFS's SPARC achieves Q>1, fusion will instantly become the world's biggest investment hotspot. Conversely, if these projects hit physics' "hard wall," the industry faces a long winter. But either way, humanity's attempt to contain the fire of the stars in a bottle at this scale has entered an irreversible sprint phase.

---

### Table 3: Helion Energy Prototype Iterations and Status

|**Prototype**|**Period**|**Goal/Achievement**|**Status**|
|---|---|---|---|
|**IPA / Venti**|2005-2012|Validated FRC formation and acceleration; validated D-D neutron production.|Retired|
|**Grande**|2013-2014|Validated magnetic compression efficiency; plasma temperature reached keV level.|Retired|
|**Trenta**|2018-2023|Achieved 100 million°C (9 keV) ion temperature; ran over 10,000 pulses; validated energy recovery circuits.|Retired in 2023 to make way for Polaris|
|**Polaris**|2024-present|**Goal:** demonstrate net electricity output.<br><br>  <br><br>**Status:** completed end of 2024, running in 2025, net-power goal not yet announced as achieved.|**Running** (critical validation period)|
|**Antares (planned)**|2028+|First commercial power plant; delivering 50 MW to Microsoft.|Planned; depends on Polaris's success|

_(Note: all data in this report is based on public information and industry analysis available before January 2026.)_

## Sources

- [Helion Energy](https://en.wikipedia.org/wiki/Helion_Energy)
- [What is the difference between inertial and magnetic confinement fusion](https://www.reddit.com/r/askscience/comments/81aevl/what_is_the_difference_between_inertial/)
- [Helion's Unique Approach to Renewable Energy](https://www.reddit.com/r/fusion/comments/1op2ppc/helions_unique_approach_to_renewable_energy/)
- [Commercial Fusion Power Faces 3 More Epic Tech Hurdles](https://www.goldsea.com/article_details/commercial-fusion-power-faces-3-more-decades-of-hurdles)
- [Inertial confinement fusion: Recent results and perspectives](https://www.epj-conferences.org/articles/epjconf/pdf/2024/20/epjconf_lnes2024_00013.pdf)
- [Fusion power](https://en.wikipedia.org/wiki/Fusion_power)
- [More on Helion's pulsed approach to fusion](https://www.helionenergy.com/articles/more-on-helions-pulsed-approach-to-fusion/)
- [Helion: Technology](https://www.helionenergy.com/technology/)
- [ITER](https://en.wikipedia.org/wiki/ITER)
- [Tritium breeding](https://www.iter.org/machine/supporting-systems/tritium-breeding)
- [China sets new records in research of new-generation "artificial sun" HL-3](https://en.cnnc.com.cn/2025-03/31/c_1082798.htm)
- [Experimental Advanced Superconducting Tokamak](https://en.wikipedia.org/wiki/Experimental_Advanced_Superconducting_Tokamak)
- [Fusion energy SOE launched: PRC commentary](https://policycn.com/public/commentaries/fusion-energy-soe-launched-in-shanghai-50172)
- [China Fusion Engineering Test Reactor](https://en.wikipedia.org/wiki/China_Fusion_Engineering_Test_Reactor)
- [China Aims to Operate World's First Hybrid Fusion-Fission Plant by 2030](https://www.nucnet.org/news/china-aims-to-operate-world-s-first-hybrid-fusion-fission-nuclear-plant-by-2030-3-5-2025)
- [The State of the Fusion Energy Industry in 2025](https://www.peaknano.com/blog/the-state-of-the-fusion-energy-industry-in-2025)
- [Materials Challenges for Fusion Energy](https://www.nae.edu/7558/MaterialsChallengesforFusionEnergy)
- [Materials Challenges for Successful Roll-out of Commercial Fusion Reactors](https://scientific-publications.ukaea.uk/wp-content/uploads/UKAEA-CCFE-PR2152.PDF)
- [Tritium Breeding Challenges](https://energy.sustainability-directory.com/term/tritium-breeding-challenges/)
- [Nuclear Fusion Deals: Based on Reality or a Dream?](https://www.energycouncil.com.au/analysis/nuclear-fusion-deals-based-on-reality-or-a-dream/)
- [Helion's approach to fusion: How it works](https://www.youtube.com/watch?v=HlNfP3iywvI)
- [Nuclear Fusion / OpenAI Boss Sam Altman 'Motivated to Invest More'](https://www.nucnet.org/news/openai-boss-sam-altman-motivated-to-invest-more-1-4-2024)
- [OpenAI CEO Altman Says Future of AI Depends on an Energy Breakthrough](https://www.energycentral.com/energy-biz/post/openai-ceo-altman-says-future-ai-depends-energy-breakthrough-PumCqEWpu8jh08z)
- [Sam Altman Says AI Using Too Much Energy](https://futurism.com/sam-altman-energy-breakthrough)
- [Can someone ELI5 Helion's controversy?](https://www.reddit.com/r/fusion/comments/1dlmfu2/can_someone_eli5_helions_controversy/)
- [Sam Altman-backed Helion raises $425M](https://techfundingnews.com/helion-secures-425m-to-advance-fusion-energy/)
- [Sam Altman, SoftBank invest in $425M round for Helion](https://www.cleantechalliance.org/2025/01/29/sam-altman-softbank-invest-in-425m-round-for-helion-a-seattle-area-startup-chasing-fusion-power/)
- [Helion Announces $425M Series F Investment](https://www.helionenergy.com/articles/helion-announces-425m-series-f-investment-to-scale-commercialized-fusion-power/)
- [Helion celebrates smoother path to fusion energy site approval](https://www.heraldnet.com/news/helion-celebrates-smoother-path-to-fusion-energy-site-approval/)
- [Transcript: Sam Altman Testifies at US Senate Hearing on AI Competitiveness](https://www.techpolicy.press/transcript-sam-altman-testifies-at-us-senate-hearing-on-ai-competitiveness/)
- [Helion said Polaris should demonstrate electricity this year](https://www.reddit.com/r/fusion/comments/1ptp513/helion_said_that_polaris_should_demonstrate/)
- [Can we talk about Helion?](https://www.reddit.com/r/fusion/comments/133ttne/can_we_talk_about_helion/)
- [Helion gives behind-the-scenes tour of secretive 60-foot fusion prototype](https://www.geekwire.com/2025/helion-gives-behind-the-scenes-tour-of-secretive-60-foot-fusion-prototype-as-it-races-to-deployment/)
- [Trenta's final fusion test campaign](https://www.helionenergy.com/articles/ending-trenta-operations/)
- [Fusion energy in 2025: six global trends to watch](https://www.iaea.org/newscenter/news/fusion-energy-in-2025-six-global-trends-to-watch)
- [Sam Altman](https://en.wikipedia.org/wiki/Sam_Altman)
- [Sam Altman nuclear fusion startup fundraising](https://observer.com/2025/01/sam-altman-nuclear-fusion-startup-fundraising/)
- [Sam Altman: Age of AI will require an energy breakthrough](https://www.popsci.com/technology/sam-altman-age-of-ai-will-require-an-energy-breakthrough/)
- [Helion: FAQ](https://www.helionenergy.com/faq/)
- [Fusion industry supply chain](https://www.fusionindustryassociation.org/tag/supply-chain/)
- [FIA Supply Chain Report](https://ukaea.maglr.com/supply-chain-aug-2025/fia-supply-chain-report)
- [FIA Supply Chain 2025 Report](https://www.fusionindustryassociation.org/wp-content/uploads/2025/06/FIA-Supply-Chain-2025-Report.pdf)
- [FIA 2025 Year in Review](https://www.fusionindustryassociation.org/wp-content/uploads/2025/12/FIA-2025-Year-in-Review.pdf)
- [Sam Altman: I would expect Helion will show you](https://www.reddit.com/r/fusion/comments/1hv3ugl/sam_altman_i_would_expect_helion_will_show_you/)
- [AI doesn't need more energy; it needs less concentration of power](https://www.techpolicy.press/ai-doesnt-need-more-energy-it-needs-less-concentration-of-power/)
- [Helion announces $500 million fundraise](https://www.helionenergy.com/articles/announcing-500-million-fundraise/)
- [Helion newsletter: progress keeps us on track](https://www.reddit.com/r/fusion/comments/1ow2fte/helion_news_letter_progress_keeps_us_on_track_to/)
- [Polaris: Helion's latest nuclear device](https://www.reddit.com/r/fusion/comments/1pkue34/the_first_look_at_polaris_helions_latest_nuclear/)
- [Helion: Polaris](https://www.helionenergy.com/polaris/)
- [Nuclear fusion energy and AI](https://time.com/7328213/nuclear-fusion-energy-ai/)
- [Sam Altman on the future of AI and humanity](https://www.ted.com/pages/sam-altman-on-the-future-of-ai-and-humanity-transcript)
- [Helion: how fusion technologies are diverging by 2026](https://businesscraft.se/business/helion-cfs-tokamak-energy-tae-how-fusion-technologies-are-diverging-by-2026/)
- [Global approaches to tritium breeding for fusion](https://www.iaea.org/about/organizational-structure/department-of-nuclear-energy/webinars/challenges-and-advances-of-technology-development-for-fusion-energy-webinar-series/global-approaches-to-tritium-breeding-for-fusion)
- [EPRI Fusion Blankets Report 2024](https://www.energy.gov/articles/epri-fusion-blankets-report-2024)
- [Helion (research note)](https://research.contrary.com/company/helion)
- [2025 at Helion](https://www.reddit.com/r/fusion/comments/1q0fcm7/2025_at_helion/)
- [IAEA Fusion Energy Conference contributions](https://conferences.iaea.org/event/406/contributions/)
- [CAS News: HL-3 tokamak achieves high ion temperature](https://english.cas.cn/newsroom/cas_media/202510/t20251015_1089475.shtml)
- [Gov.cn: Fusion energy news](https://english.www.gov.cn/news/202510/20/content_WS68f63030c6d00ca5f9a06eff.html)
- [KSP Forum: Helion Energy discussion](https://forum.kerbalspaceprogram.com/topic/216068-helion-energy/)
- [Talk-Polywell forum: Helion discussion](https://talk-polywell.org/bb/viewtopic.php?t=6499&start=930)
- [Talk-Polywell forum: Helion discussion (earlier)](https://www.talk-polywell.org/bb/viewtopic.php?t=6499&start=855)
- [IAEA: World Fusion Outlook 2025 (PDF)](https://www-pub.iaea.org/MTCD/publications/PDF/p15935-25-02871E_WFO25_web.pdf)
- [Energy Reporters: new fusion breakthrough](https://www.energy-reporters.com/news/scientists-shiver-in-awe-as-new-fusion-breakthrough-ignites-energy-revolution-that-could-change-the-world/)
- [Frontiers in Energy Research: fusion article](https://www.frontiersin.org/journals/energy-research/articles/10.3389/fenrg.2023.1157394/full)
- [Fundación Bankinter: FusionForward 2025 report (PDF)](https://www.fundacionbankinter.org/wp-content/uploads/2025/07/Future-Trends-Forum-Report-Preview-%E2%80%93-FusionForward-2025.pdf)
- [Moomoo: the industry's inaugural year](https://www.moomoo.com/news/post/63408118/the-industry-s-inaugural-year-is-being-driven-by-the)
- [National Academies: fusion report chapter](https://www.nationalacademies.org/read/18288/chapter/4)
- [ResearchGate: China's HL-3 fusion breakthrough paper](https://www.researchgate.net/publication/397082192_Breakthrough_in_China's_Fusion_Energy_HL-3_Tokamak_Achieves_High_Ion_Temperature_and_Fusion_Triple_Product)
- [SCSP: Fusion Commission Fall 2025 Report (PDF)](https://www.scsp.ai/wp-content/uploads/2025/10/Fusion-Commission-Fall-2025-Report-Draft.pdf)
- [The Innovation: fusion article](https://www.the-innovation.org/article/id/691d6fe37a2be313aa3f23c2)