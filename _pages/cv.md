---
layout: archive
title: "CV - Koutian Wu | AI4Geoscience PhD Student at UT Austin"
excerpt: "Comprehensive CV of Koutian Wu, PhD student working on AI agents for science: agent evaluation and benchmark design (ESM-bench), land surface modeling, and full-stack engineering."
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

<embed src="https://cdn.jsdelivr.net/gh/ktwu01/resume@main/resume_AI_Koutian_Wu_UTAustin_PhD.pdf" type="application/pdf" width="100%" height="800px" />

Highlights
======
* Research Intern, AI Data Trial (Benchmark Radar), Tencent
* Open-source contributor to repositories totaling 100K+ stars (git/git, multica, ai-agent-book, AionUi, harbor); 10K+ GitHub contributions in the last year
* Open to research internships in AI Agent Development/Test/Evaluation, ML/DL/DS, and Full-Stack Engineering
* 2+ years work experience (US/International); 4+ years research/programming experience
* Invited reviewer for *Planetary and Space Sciences* (Elsevier, Scopus Q2), with further review invitations from IEEE TNNLS, ACM Computing Surveys, ACM Transactions on Sensor Networks, the COLM workshop track, and ACM AgentSkills

Education
======
* **Ph.D. Student in AI for Geosciences**, University of Texas at Austin, 2024 - Expected: May 2029
  * TA for 1,000+ students (Rating: 4.5/5.0)
  * Advisors: Dr. Zong-Liang Yang

* **B.S. with Honors in Geosciences (Honors Class)**, University of Science and Technology of China, 2020 - 2024
  * Nominated for the Highest Honor for USTC undergraduates (one of the two ESS School nominees)
  * Founded one of the largest student clubs, grew from 0 to 1,300+ members. [News]

Work Experience
======
* **Research Intern, AI Data Trial** (Jul 2026 - Aug 2026)
  * Tencent Qingyun Talent Program (top-talent program), Tencent America
  * Built Benchmark Radar, a production-deployed open-source dashboard ranking which benchmarks frontier labs report, across 30+ curated documents from 10 organizations
  * Automated a daily snapshot pipeline that republishes the leaderboard without manual intervention; hardened the audit pipeline after a security/reliability review
  * Audited raw deliveries from AI training-data vendors against a per-task STEM coverage protocol, producing dated, reproducible reports
  * Ran a cross-benchmark vendor-classification audit across three review passes, reconciling a canonical benchmark sheet covering 11 vendor leads

* **Core Founding Team Member** (Jan 2026 - Jul 2026)
  * Starting Point One (SP1), Remote
  * Sourced 100+ talents for Kehan Dong (CEO of SP1, ex-YC China Partner); sent 1,000+ outreach emails supporting post-investment hiring for Mira (raised $6.6M from General Catalyst)

* **Graduate Research Assistant** (Aug 2025 - May 2026)
  * Jackson School of Geosciences, University of Texas at Austin
  * AI for Noah-MP Land Surface Model: implementing rock and wood moisture into the Noah-MP land surface model

* **Project Lead, High-Performance Computing Allocation** (Aug 2025 - Aug 2026)
  * NSF NCAR, Remote
  * Proposed and secured NSF NCAR allocation: 1k GPU + 22k CPU hours.
  * Integrating machine learning parameter calibration for a SOTA physics-based land surface model (Noah-MP).
  * Developing a multi-expert AI agent system for automated parameterization of physics-based climate models.

* **Lead Developer, ESM-bench** (Dec 2025 - Present)
  * UT Austin
  * Designed a 243-task benchmark and multi-model evaluation harness measuring where frontier models fail on real scientific code. [Preprint](https://zenodo.org/records/19802836)

* **AI Intern, AI Agent Knowledge Base Evaluation** (Jul 2025 - Aug 2025)
  * 19Pine.AI (Singapore), Remote
  * Implemented a multi-dimensional evaluation system from scratch for PineAgent's RAG knowledge base.
  * Developed a data sanitization module removing 2,000+ PII entries and noise from 1,000+ call sessions.
  * Extracted 3,000+ Q&A pairs (knowledge/method/strategy) from call sessions to form the evaluation dataset.
  * Deployed concurrent LLM-as-judge + rule-based engine, measuring precision/recall/F1 to enable RLHF optimization.

* **Full-Stack Intern, LLM Text Processing System** (Jun 2025 - Jul 2025)
  * ZaiwenAI.com, Beijing, China
  * Developed a 3-module MVP: LLM-footprint detection, removal, and plagiarism checking for researchers.
  * Built a RESTful backend with FastAPI and an asynchronous task queue with Celery + Redis.
  * Created a Vue.js frontend with 9-format document upload and SSE-based real-time LLM response streaming.

* **AI Consulting Expert** (May 2025 - Jun 2025)
  * Invited by the CEO, Keshi Edu, Remote (Beijing)
  * Designed an architecture for a RAG-based knowledge base to customize student graduate program applications.
  * Identified critical bugs and exposed API keys, helping avoid significant potential losses.

* **Graduate Teaching Assistant** (Aug 2024 - May 2025)
  * The University of Texas at Austin
  * Helped prepare course syllabus, office hours, and grade homework for ~1040 students

* **Scientific Visitor** (Jun 2024 - Aug 2024)
  * Peking University, Beijing, China
  * Hydrology and Water Resources Science, model evaluation of physics-based land surface models; Advisor: Prof. Peirong Lin

* **Visiting Scholar** (Jul 2023 - Dec 2023)
  * NSF NCAR, Boulder, Colorado
  * Research on volcanic perturbations in the MLT region using WACCM-X simulation and meteor radar observations
  * Re-confirmed that a single volcano can send shockwaves around Earth, seen in simulations and observations

* **Student Fellow** (Oct 2021 - Feb 2024)
  * Shenzhen X-Institute (A Shenzhen Government-Tsinghua Univ. Initiative)

Research Interests
======
* **AI Agent Evaluation for Science**: benchmarks and harnesses for whether AI agents understand scientific models and code
* **AI for Land Surface Modeling**: implementing explainable AI/ML to improve physics-based Noah-MP land surface modeling
* **High Performance Computing**: GPU and CPU clusters for large-scale geoscience simulations
* **Model Optimization**: physics-based land surface models including Noah-MP, CTSM, HRLDAS

Skills
======
* **Programming**: Python, JavaScript/TypeScript, MATLAB, Fortran, Shell, SQL
* **AI/ML**: AI Agent Evaluation, LLM-as-a-judge, benchmark design, LLM APIs, Prompt Engineering, PyTorch, LangChain, RAG, HuggingFace
* **Frameworks and Tools**: FastAPI, Celery, Redis, Vue.js, React, Docker, Git, HPC, AWS/GCP
* **Geoscience**: Land Surface Model Development (Noah-MP, CTSM, HRLDAS), WACCM, Model Evaluation

Publications
======
  <ul>{% for post in site.publications reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>

Talks
======
  <ul>{% for post in site.talks reversed %}
    {% include archive-single-talk-cv.html %}
  {% endfor %}</ul>

Teaching
======
  <ul>{% for post in site.teaching reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>

Service and Leadership
======
* **Project Admin**, NCAR/CISL Allocation Project UTAA0012 (Aug 2025 - Present)
  * Technical leadership and implementation of project workflows for "Explainable AI for Improving Physics-Based Noah-MP Land Surface Modeling"
* **President & Founder**, USTC Student Xingyun Poetry Club (Nov 2020 - Jun 2022)
  * Founded USTC's first poetry club, grew to 1,300+ members
  * Organized 25+ cultural events with 202+ attendees
  * Managed team of 8 co-founders and 4 vice presidents
* **Graduate Teaching Assistant**, The University of Texas at Austin (Aug 2024 - May 2025)
  * Course preparation, office hours, and grading for ~1040 students

Research Projects
======
* **Perturbations by the 2022 Hunga-Tonga Volcano Eruption in the MLT Region**
  * Investigated using WACCM-X Simulation and Meteor Radar Observations
  * Abstract: https://ui.adsabs.harvard.edu/abs/2023AGUFMSA33B2892W/abstract
  * Re-confirmed that a single volcano can send shockwaves around Earth

Awards and Honors
======
* **NSF NCAR Computational Resource Allocation** (Aug 2025)
  * 1,000 GPU hours on NSF NCAR Derecho-GPU
  * 20,000 CPU core-hours on NSF NCAR Derecho
  * 2,000 CPU core-hours on Casper
  * 2 TB campaign storage
