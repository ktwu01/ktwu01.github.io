---
title: "Ashley Matheny Treats Trees as Pumps, and That Changes the Whole Model"
date: 2026-05-09
permalink: /posts/2026/05/ashley-matheny-trees-as-pumps/
tags:
  - ecohydrology
  - plant hydraulics
  - PhD
  - UT Austin
  - Noah-MP
  - vegetation
---

Most land surface models treat a tree like a passive straw. Water comes in at the roots, water leaves at the leaves, end of story. Ashley Matheny's research basically says no, a tree is an active hydraulic system with storage, capacitance, and a strategy, and if you do not model it that way you are going to be wrong about drought.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

Ashley grew up in a small town on the Ohio River in West Virginia, water skiing and canoeing and camping. She did her undergraduate in Civil Engineering at Ohio State, then her PhD at Ohio State in Civil, Environmental, and Geodetic Engineering with Gil Bohrer, finishing in 2016. The dissertation title is the giveaway, "Development of a Novel Plant-Hydrodynamic Approach for Modeling of Forest Transpiration During Drought and Disturbance." She came to UT Austin as Assistant Professor in 2017. By 2021 she had won the NSF CAREER Award, in 2022 the AMS Outstanding Early Career Award in Agricultural and Forest Meteorology, and along the way the Knebel Distinguished Teaching Award from the Jackson School.

The story she tells about why she is in this field is that she was working for the U.S. Army Corps of Engineers in 2010, studying how water interacts with dams, and she watched a hydraulic jump on the Ohio River. That single observation rerouted her career toward hydrology. I think about that a lot. One specific moment in front of one specific river, and an entire research program follows.

What she actually does is measure water inside trees. Real measurements, not simulations. She and Pete Marchetto at Conservify developed novel capacitance sensors that can track tree water content over time. She has field sites at the University of Michigan Biological Station, in the Texas Hill Country with Ashe juniper and live oak, in the Valles Caldera in New Mexico, and in mangrove ecosystems on the Texas Gulf Coast and out to Australia, Panama, Abu Dhabi, Jamaica. Different ecosystems, different water strategies, same fundamental question. How does this species manage water under stress.

Here is the part that connects to my PhD. The Li, Yang, Matheny et al. 2021 paper in JAMES on "Development of plant hydraulics in the Noah-MP Land Surface Model" is essentially the bridge between her field measurements and the modeling community I am now part of. The argument is that if you put real plant hydraulics into a land surface model, the predictions about drought response and transpiration get qualitatively better. Different species have different hydraulic strategies. Some are isohydric, meaning they shut down stomata aggressively to protect their water column. Some are anisohydric, meaning they keep transpiring and risk hydraulic failure. A model that does not know the difference is going to predict the wrong thing in a drought year.

I am going to admit, I did not fully appreciate this until I started running the simulations myself. You can read papers about plant hydraulics and nod along. It is different to actually configure Noah-MP with and without a hydraulics module and watch the soil moisture and ET timeseries diverge. The trees in the model start behaving like trees, not like straws.

The other thing about Ashley's lab is the international mangrove work. Mangroves are halophytes, salt-tolerant plants, and the standard plant hydraulics models were never built to handle the osmotic side of water uptake under high salinity. She has been extending the models to do exactly that. This sounds like a niche extension until you remember that mangrove ecosystems are some of the most carbon-dense on Earth and they sit at the climate-vulnerable coast. Getting their water and carbon balance right is not optional.

Working with her on the AMS 2026 paper, what I have noticed is the rigor about what the model is actually capable of saying. Modeling people, myself included, can get carried away with what the simulation produces. She will look at an output and ask, OK but what would the sap flux sensor at UMBS actually show? If your simulation says a thing the sensor would not show, your simulation is wrong, and no amount of fancy postprocessing fixes that.

There is a deeper lesson in her trajectory that I am only starting to absorb. The novel capacitance sensors, the long-term sap flux records, the multi-species comparisons, the international mangrove sites. None of these are quick wins. You build a sensor, you put it in a tree, you wait three years, then you have data. The publishing-on-AI-twitter rhythm is incompatible with what she does. The good news is the data she generates will outlast every quick AI paper from the same period, because the underlying biology is not going anywhere.

For me, the practical lesson is, when I claim Noah-MP plus ML produces a better simulation of plant-rock-water interactions, the proof has to live in Ashley's data, not in my training loss curve. Otherwise I am just curve-fitting to my own assumptions.
