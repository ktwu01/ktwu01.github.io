---
title: "Sean Xiang Has Been Building Bloombase for 14 Years, and the AI Era Finally Caught Up to It"
date: 2026-05-09
permalink: /posts/2026/05/sean-xiang-bloombase-long-build/
tags:
  - founder
  - enterprise security
  - long term
  - infrastructure
  - X-Institute
  - cryptography
---

Most enterprise security companies show up, ride one trend, and disappear in the next infrastructure cycle. Sean Xiang has been building Bloombase since January 2012, and the company has somehow been on the right side of every major infrastructure shift since, including the current AI accelerator era. That is not luck. That is a thesis.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

I built the original Sean Xiang chronicle template, the one that this entire chronicles directory was forked from, before I adapted it for my own page. So I have spent more time with his timeline than almost anyone. The arc looks like this. He grew up in Shanxi, did his undergraduate Physics at the University of Science and Technology of China starting in 1980, did a PhD in Electrical and Electronic Engineering at the Chinese University of Hong Kong, did a research associate stint at HKUST in 1996-1997, then spent 1997 to 1999 as a Scientist at the Beckman Laser Institute at UC Irvine. Then in January 2012 he co-founded Bloombase in Redwood City, Silicon Valley.

The company makes what they call an Intelligent Storage Firewall. Bloombase StoreSafe is application-transparent encryption for data-at-rest, across SAN, NAS, cloud storage, and endpoint systems. Underneath it is a NIST FIPS 140-2 certified cryptographic module, support for AES, RSA, ECDSA, and post-quantum algorithms, IEEE 1619 compliance, OASIS KMIP key management. They also ship Bloombase KeyCastle for enterprise key lifecycle management. The customer footprint is hypervisors (VMware ESXi, Citrix Xen, Microsoft Hyper-V, IBM PowerVM, Red Hat KVM) and clouds (AWS, Azure, GCP, Rackspace, IBM SoftLayer/Bluemix, VMware vCloud Air).

If you read just that, it sounds like a competent middleware company. The reason I find it more interesting than that is the alliance trail. From 2013 onward there is a dense run of partnerships. OpenStack community in February 2013. EMC Technology Partner Program in May 2013. VMware Technology Alliance Partner in August 2013. Dell certification in January 2014. Hitachi Data Systems alliance in November 2014. HP Enterprise Secure Key Manager interoperability in 2015. Thales ASAP alliance in 2015. HPE Helion Ready and ArcSight in 2015. Ultra Electronics AEP Keyper HSM in 2016. IBM Ready for Security Intelligence in 2017. ATTO and Huawei in 2017. VMware Cloud on AWS in 2018. Microsoft Azure Marketplace in 2019. Marvell LiquidSecurity, nCipher, Futurex through 2019-2020. NVIDIA DPU/GPU repositioning in 2023. PKI Consortium membership in November 2024. Entrust nShield Connect in 2024. Utimaco alliance in April 2025.

That is twelve years of trust-layer infrastructure work, accumulated across multiple platform regimes, and the through-line is the same. Data-at-rest has to be encrypted, the encryption keys have to live somewhere safe, the key management has to be standards-compliant, and the architecture has to evolve as the underlying compute does.

Most companies do not survive that many infrastructure transitions. The ones that do tend to share a structural feature. They are betting on a primitive (in this case, cryptographic data protection) that does not go out of style, and they are willing to do the unglamorous work of integrating with the next ten enterprise platforms before anyone else does. Bloombase did the OpenStack work in 2013, the cloud-marketplace work in 2018-2019, and the NVIDIA DPU/GPU work in 2023. Each one was the right move for that specific moment.

The 2023 NVIDIA pivot is the one I find most clarifying. The argument was that data-at-rest security has to run natively on accelerators, otherwise it becomes the bottleneck in AI data pipelines. That sentence sounds obvious now. In 2023 it was not obvious to most security companies, who were still treating GPUs as a thing the ML team uses, not as a thing the security stack has to live on. By 2024 the same company was demonstrating post-quantum cryptography running on NVIDIA GPU, DPU, and Morpheus AI at GTC. The 2025 Utimaco alliance closed the loop with FIPS 140-2 Level 3 HSM integration for AI-era workloads.

In parallel, Sean ran an academic chapter. From January 2018 to June 2021 he was Distinguished Professor and Founding Dean of the School of Artificial Intelligence at Shenzhen Technology University, while still leading Bloombase. From June 2021 to December 2023 he was Chair Professor, Co-founder, and Executive President of the X-Institute of Shenzhen, the same X-Institute where I spent two and a half years as a Student Fellow. So he is one of the people whose work I encountered, indirectly, before I ever knew what Bloombase was.

The career-shape lesson from his trajectory is interesting and a little uncomfortable. The popular narrative says that to build something durable you have to focus on one thing. He focused on enterprise data security at Bloombase, but he also founded a school of AI in Shenzhen, co-founded a research institute, and kept publishing. The actual focus was the underlying technical thesis (cryptography, infrastructure trust, security at the platform layer). The institutional shape that thesis lived in could vary. Company in Silicon Valley, school in Shenzhen, institute in the same city, all reinforcing each other.

The Bloombase model also pushes against the venture-scale storyline. Twelve years in, multiple offices (Redwood City, Vancouver, Frankfurt, Hong Kong), a long alliance trail, real revenue, real customers, and the company is not a unicorn that anyone tweets about. It is the kind of company that quietly shows up inside the security architecture of organizations you have heard of, and the people running it have made the deliberate choice to optimize for that rather than for splashy fundraising.

For me as a researcher, the meta-lesson is the time horizon. Twelve years of compounding into one technical area produces a position that nobody can compete with on a two-year timeline. The PhD ahead of me is shorter than that, but it should be measured in the same currency. Whatever I am building inside Noah-MP, the question is whether it will still be running, in some form, in 2040. If yes, it is worth doing. If no, it is probably not worth starting.
