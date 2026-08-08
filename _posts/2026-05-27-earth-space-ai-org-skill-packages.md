---
title: 'earth-space-ai.org: progressive-disclosure skill packages for Earth and space system models'
date: 2026-05-27
permalink: /posts/2026/05/earth-space-ai-org-skill-packages/
tags:
  - earth-system-models
  - ai-agents
  - skill-packages
  - climate-modeling
  - heliophysics
  - open-science
---

Decades of Earth-system modeling judgment live in PDFs, mailing lists, and senior researchers' heads, and none of it is loadable by an AI coding agent. earth-space-ai.org is an attempt to fix that.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)
>
> Project home: [earth-space-ai.org](https://github.com/earth-space-ai) · Homepage repo: [earth-modeling-agent-homepage](https://github.com/ktwu01/earth-modeling-agent-homepage)

## What this is

Mechanistic Earth-system models, CESM, E3SM, WRF, MOM6, Noah-MP, CTSM, JULES, and their cousins, carry decades of scientific judgment in their source trees, build systems, and debug folklore. Most of that knowledge lives in PDFs, mailing lists, AGU posters, and the heads of senior researchers. None of it is loadable by an AI coding agent.

[earth-space-ai.org](https://github.com/earth-space-ai) is an attempt to fix that. It is a GitHub organization that hosts curated, progressive-disclosure **skill packages** for Earth, planetary, and space system models. Each repo is structured to be:

- loaded by AI coding agents (Claude Code, Codex, Cursor, Aider, Cline, LingTai),
- read as a durable human reference by researchers and developers,
- maintained alongside the upstream model it covers,
- licensed and credited cleanly so the upstream community is not stepped on.

The organization tagline puts the goal in one line:

> Democratizing Earth and Space Sciences Modeling with Artificial Intelligence.

## The skill package layout

A skill package is not a tutorial. It is a knowledge package with a fixed shape:

```
<model>-skill/
├── SKILL.md       ← routing hub (read first)
├── README.md      ← human-facing front matter, disclaimer, install
└── reference/     ← deep-dive docs loaded on demand
    ├── getting-started.md
    ├── architecture.md
    ├── running-single-point.md
    ├── running-2d-domain.md
    ├── custom-output.md
    ├── contributing-pr.md
    └── debugging.md
```

`SKILL.md` is the routing hub: a decision tree, the repo layout, a quick start, and critical rules. It is the only file an agent must read up front. From there, the agent loads exactly the `reference/*.md` page it needs for the current step, no more.

This is what "progressive disclosure" means in practice: the agent never holds the full corpus in context. It holds the index, and pulls one chapter at a time. The layout is borrowed from [laps-skill](https://github.com/huangzesen/laps-skill) and the xhelio family, where it was first validated in heliophysics.

## The current map: 8 domains, ~30 skills

The skill repos are grouped by scientific domain. As of this post, the org and its partner repos list around thirty skills across eight groups (the source of truth is [`lib/skills.ts`](https://github.com/ktwu01/earth-modeling-agent-homepage/blob/main/lib/skills.ts) in the homepage repo).

**01 · Earth-system / coupled.** [cam-skill](https://github.com/earth-space-ai/cam-skill) (Community Atmosphere Model), [cesm-skill](https://github.com/earth-space-ai/cesm-skill) (CESM superproject), [e3sm-skill](https://github.com/earth-space-ai/e3sm-skill) (Energy Exascale Earth System Model), [noresm-skill](https://github.com/earth-space-ai/noresm-skill), [fms-skill](https://github.com/earth-space-ai/fms-skill) (GFDL Flexible Modeling System), plus pointers to the [ESFlow preprint](https://egusphere.copernicus.org/preprints/2026/egusphere-2026-2237/) and [Zenodo record](https://zenodo.org/records/19350842) by Tian Zhou and collaborators.

**02 · Atmosphere.** [wrf-skill](https://github.com/earth-space-ai/wrf-skill), [waccm-skill](https://github.com/earth-space-ai/waccm-skill), [waccmx-skill](https://github.com/earth-space-ai/waccmx-skill), [gfdl-fv3-skill](https://github.com/earth-space-ai/gfdl-fv3-skill), [openifs-skill](https://github.com/earth-space-ai/openifs-skill), [regcm-skill](https://github.com/earth-space-ai/regcm-skill), [geos-chem-skill](https://github.com/earth-space-ai/geos-chem-skill).

**03 · Land surface and hydrology.** [noahmp-skill](https://github.com/earth-space-ai/noahmp-skill) (Noah-MP + HRLDAS), [ctsm-skill](https://github.com/earth-space-ai/ctsm-skill) (CTSM / CLM), [jules-skill](https://github.com/earth-space-ai/jules-skill), [summa-skill](https://github.com/earth-space-ai/summa-skill), [vic-skill](https://github.com/earth-space-ai/vic-skill), [parflow-skill](https://github.com/earth-space-ai/parflow-skill).

**04 · Ocean.** [mom6-skill](https://github.com/earth-space-ai/mom6-skill), [mitgcm-skill](https://github.com/earth-space-ai/mitgcm-skill), [fesom2-skill](https://github.com/earth-space-ai/fesom2-skill), [roms-skill](https://github.com/earth-space-ai/roms-skill).

**05 · Sea ice.** [cice-skill](https://github.com/earth-space-ai/cice-skill).

**06 · Solid Earth / finite fault.** [wasp-finitefault-skill](https://github.com/liuwei1997/wasp-finitefault-skill), maintained by Liuwei Xu at UCLA.

**07 · Heliophysics / space physics models.** [laps-skill](https://github.com/huangzesen/laps-skill) (LAPS, the UCLA pseudo-spectral 3D Hall-MHD code), the upstream [LAPS](https://github.com/chenshihelio/LAPS) repository, and [lingtai-batsrus-skill](https://github.com/huangzesen/lingtai-batsrus-skill) (BATS-R-US, the MHD solver at the core of SWMF), all maintained by Zesen Huang.

**08 · Heliophysics observation / data access.** [xhelio-cdaweb](https://github.com/huangzesen/xhelio-cdaweb) (NASA CDAWeb), [xhelio-spice](https://github.com/huangzesen/xhelio-spice) (SPICE toolkit), [xhelio-pds](https://github.com/huangzesen/xhelio-pds) (NASA PDS), maintained by Zesen Huang.

Skills are tagged `complete` or `scaffold`. A scaffold has the structure and the routing hub but is still being filled in; a complete skill has been used end-to-end by an agent at least through a canonical run.

## Anatomy of one skill: Noah-MP

The [noahmp-skill](https://github.com/earth-space-ai/noahmp-skill) is the most fleshed-out land-surface entry and a fair representative of what a "complete" skill looks like.

It targets two things at once: the refactored Version 5 modular Fortran codebase of [NCAR/noahmp](https://github.com/NCAR/noahmp) and the [HRLDAS](https://github.com/NCAR/hrldas) offline driver. The skill teaches an agent how to install, compile, run, modify, debug, and contribute to the model. Its `reference/` tree has dedicated chapters for designing a runnable simulation from an underspecified user request ("soil moisture over Texas, 12.5 km, on TACC"), for running a single-point Bondville simulation, for running a CONUS 2D NLDAS-2 simulation, for adding a new output variable through the full IO chain, and for filing a submodule-aware pull request upstream.

Two design choices in `noahmp-skill` are worth calling out because they generalize across the org:

1. **The skill is not a replacement for the upstream tutorials. It is a machine-readable wrapper.** The [NCAR/hrldas tutorial notebooks](https://github.com/NCAR/hrldas/tree/master/tutorial) by Cenlin He are the gold-standard reference. The skill's README states this explicitly: "When a checkpoint, namelist value, or physics option in this skill disagrees with the NCAR tutorials, the NCAR tutorials win." The skill adds AI-native execution, machine-readable verification scripts, TACC-specific dependency probes, and a reference figure for visual validation. It does not try to outrank the experts.
2. **Verification is part of the skill, not part of the user's faith.** After any run, the agent is required to call `examples/check_run_outputs.sh` to catch silent failures: header-only `LDASOUT`, `START_DATE` drift, all-zero latent-heat fields, missing custom variables. For the Bondville single-point run, a reference `bondville_LH_ncview.png` is shipped so the agent's output can be eyeball-compared against a known-good result.

The disclaimer at the top of the skill is also load-bearing: "AI can make mistakes (wrong paths, drifted line numbers, stale namelist fields, hallucinated flags). Always cross-check against upstream `NCAR/noahmp` and `NCAR/hrldas` and the tech note before acting." A skill package that pretends to be infallible is a worse skill package than one that says where it might lie.

## The homepage

The org has a [homepage](https://github.com/ktwu01/earth-modeling-agent-homepage) built as a static-friendly Next.js 15 site (App Router, React 18, TypeScript, no backend). It is a single-page anchored layout with three jobs:

1. **List every skill repo by domain** with a one-line description and a link out to the upstream repo. The source of truth is `lib/skills.ts`; both the home page and the nav/footer regenerate from that one file. Adding a new skill is a one-line edit.
2. **Explain the skill package layout** (the `SKILL.md` + `reference/` shape) so a new contributor understands the shape before they propose a new repo.
3. **Surface the people.** A `/teams` page lists the Scientific Committee (faculty PIs like Chuanfei Dong at BU; Vassilis Angelopoulos, Jacob Bortnik, Marco Velli at UCLA; Tian Zhou at PNNL), the Executive Committee (Zesen Huang at UCLA, Koutian Wu at UT Austin), and Scholars across UCLA, Caltech, UMich, Oxford, Meta, ETH Zürich, and UIUC. Contribution is the organizing principle, not affiliation.

Deployment is Vercel from `main`. No backend, no database, no auth, no environment variables. The repository is intentionally simple so that the friction of contributing a new skill is editing one TypeScript array.

## Why this shape

The progressive-disclosure shape was not picked by aesthetic preference. It is a response to three real constraints:

- **Context windows are finite.** Even with million-token models, an agent that loads CESM's entire docs corpus into context every turn is wasting most of those tokens on irrelevant material. The routing hub plus on-demand chapters keeps each turn focused on the page the agent actually needs.
- **Procedural knowledge does not survive in PDFs.** "Push the noahmp submodule before the hrldas superproject" is the kind of rule that lives in one senior person's head and surfaces as a 2 AM Slack message after a stranger's pull request breaks the build. Skill packages encode that rule as a machine-checkable phase block, not a paragraph in a PDF that nobody reads.
- **Upstream maintainers do not want to be replaced.** They want their tutorials cited and their licenses respected. Every skill package in this org carries the upstream license, names the maintainer (Cenlin He for Noah-MP, the NCAR HRLDAS team for HRLDAS, Zesen Huang for the LingTai LAPS and BATS-R-US wrappers, Liuwei Xu for WASP), and says explicitly that the upstream tutorials win when there is disagreement. The skill is a wrapper, not a fork.

## How to use a skill

If you are an agent operator (a researcher with Claude Code, Codex, or Cursor), the pattern is:

1. Clone the skill repo into your skills library and refresh.
2. Tell the agent your request in one sentence. "Set up Noah-MP on TACC ls6 from a fresh login through a built `hrldas.exe`." "Plan a Texas 12.5 km NLDAS-2 run." "Add `BTRANXY` to LDASOUT."
3. Let the agent read `SKILL.md`, follow the decision tree, load the right `reference/*.md`, honor the USER GATE markers (the only points at which the agent should stop and ask you), and execute.
4. After any run, let the agent run the verification script before declaring success. Do not skip this step. Silent failures are the most expensive failure mode in Earth system modeling.

If you are a model developer who wants their model represented in the org, the pattern is the inverse: open an issue at [earth-space-ai](https://github.com/earth-space-ai), describe the model and your relationship to the upstream maintainer, and propose a maintainer name. We will not add a skill that the upstream community has not been told about.

## What is next

The 2026 roadmap, as currently understood, has three threads:

1. **Filling in the scaffolds.** Most of the atmosphere and ocean entries (CESM, MITgcm, FESOM2, ROMS, OpenIFS, RegCM, WACCM, WACCM-X, GEOS-Chem, GFDL FV3, FMS, NorESM) are scaffolds. Each needs a canonical first run, a verification harness, and a maintainer who actually runs the model.
2. **Cross-model evaluation.** A skill package teaches an agent how to drive one model. The harder question is whether the agent can reason across models, can it answer a question that requires both Noah-MP and MOM6, can it spot a coupling inconsistency between CAM and CTSM? This is where [ESM-bench](https://koutian.is-a.dev/posts/2026/04/esm-bench-ai-agents-earth-system-models/) and the ESFlow preprint plug in.
3. **A clearer contribution path.** A `CONTRIBUTING.md` at the org level, a template skill repo, and a lightweight review process that protects upstream maintainers from being surprised by a third-party wrapper of their model.

## Closing

The bet behind earth-space-ai.org is small and specific: that the bottleneck in AI-assisted Earth and space science modeling is not model capability, it is the absence of structured, loadable, machine-readable procedural knowledge for the dozen-or-so legacy Fortran codebases that the field actually depends on. If that bet is right, a well-shaped skill package is more useful than another benchmark and more durable than another paper. If it is wrong, at least the readmes get better.

Either way, the right place to start is [the org page](https://github.com/earth-space-ai). The right place to contribute is a single edit to [`lib/skills.ts`](https://github.com/ktwu01/earth-modeling-agent-homepage/blob/main/lib/skills.ts) and a new repo named `<model>-skill`.

## Resources

- Organization: https://github.com/earth-space-ai
- Homepage source: https://github.com/ktwu01/earth-modeling-agent-homepage
- Reference skill (Noah-MP): https://github.com/earth-space-ai/noahmp-skill
- Layout precedent (heliophysics): https://github.com/huangzesen/laps-skill
- ESFlow preprint (Tian Zhou et al., 2026): https://egusphere.copernicus.org/preprints/2026/egusphere-2026-2237/
- ESFlow Zenodo record: https://zenodo.org/records/19350842
- NCAR Noah-MP: https://github.com/NCAR/noahmp
- NCAR HRLDAS tutorial notebooks: https://github.com/NCAR/hrldas/tree/master/tutorial
