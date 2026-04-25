---

title: "ESM-bench, Testing Whether AI Agents Understand Climate Model Physics"
date: 2026-04-24
permalink: /posts/2026/04/esm-bench-ai-agents-earth-system-models/
tags:
  - ESM-bench
  - AI
  - Climate
  - EarthSystemModels
  - Benchmark
---

The scary part is not that AI agents fail on climate model code, but that they can fail while looking almost right.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

I have been thinking about this problem for a while. We have many AI coding benchmarks now, and some of them are genuinely useful. They tell us whether a model can fix a Python bug, pass a unit test, or recover a patch from a real software repository.

But Earth System Models are a different beast.

A climate model is not just a pile of code. It is a computational form of physics. It has mass, energy, momentum, water, radiation, turbulence, soil, snow, vegetation, ocean circulation, and a terrifying amount of Fortran sitting between an equation in a paper and a number in a simulation output.

So when an AI agent edits this kind of code, the question is not only, does it compile.

The better question is, does it understand what physical world this code is trying to preserve.

That is the motivation behind ESM-bench.

ESM-bench is a benchmark for testing whether AI agents can modify Earth System Model code while respecting both the software structure and the physical logic encoded inside it. The current paper draft defines 576 tasks across four categories, physics-based bug fixes, process representation modifications, parameterization scheme selection, and parameter optimization. The benchmark is designed around production ESM repositories such as Noah-MP, CLM5, SUMMA, ParFlow, MOM6, VIC, WRF, and E3SM.

The thing I like about this setup is that it does not pretend scientific code is the same as normal app code.

In a normal software benchmark, a patch passes if the tests pass. That is already hard enough. But in climate modeling, a patch can be syntactically clean and still be physically wrong. It can edit the wrong routine. It can use the wrong sign on a flux. It can break a conservation correction. It can keep the code looking reasonable while quietly pushing the model into a non-physical state.

Honestly, that is the nightmare scenario.

Not the model crashing. Crashing is loud. The real danger is the patch that runs, looks plausible, and slowly injects bad physics into a system that people use to reason about the planet.

This is why ESM-bench separates exact patch recovery from physics-aware review. Exact match asks whether the agent reproduced the developer diff. Review asks whether the submitted patch targets the right code, addresses the stated physical issue, stays locally consistent with the physics, remains likely to compile, covers the required edits, and avoids obvious numerical hazards.

I think this distinction matters a lot.

A model may understand the rough physical problem but write a structurally different patch. A model may also produce something that looks like a patch but misses the actual physical mechanism. Those two failures should not be collapsed into one vague score. If we want scientific agents to become useful, we need to know whether the bottleneck is file localization, code generation, or actual domain reasoning.

So ESM-bench uses two tracks.

Track A asks whether the agent can find the right file from a physics description. This sounds simple until you remember that ESM repositories can be huge, old, modular, and full of domain-specific naming conventions that only make sense after you have lived with the code for a while.

Track B asks whether the agent can produce a patch once it has the relevant source context. This is where things get much more interesting, because the agent has to move from a scientific objective to a repository-valid code change.

The early numbers are humbling.

In the paper's preliminary minimal-prompt evaluation, the strongest model reaches only 6.7 percent average structural F1 on Noah-MP, and all evaluated frontier models get 0 percent exact match. That does not mean the agents are useless. Some of them partially identify the right physical issue, especially for physics-based bug fixes. But parameterization changes and implementation-heavy tasks remain mostly unsolved.

That feels like the right kind of benchmark result.

Not a leaderboard where every model is already at 90 percent and we are arguing about decimal points. Not a toy task where the agent only has to write a small Python function. A real frontier should have failure in it. It should tell us where the models are still brittle.

I also published a live leaderboard snapshot here, [ESM Leaderboard](/esm-leaderboard.html). The April 24, 2026 snapshot includes both repository localization and physics-aware patch synthesis results. One row I find especially revealing is the newer code-level hint run, where Claude Opus 4.7 reaches 0.312 structural F1 under the most assisted v4 Noah-MP setting, while exact match is still 0 percent.

That number is useful because it tells a more nuanced story than AI is bad at climate code.

With enough code-level scaffolding, the model can move closer. It can parse the file. It can often touch the right place. It can recover fragments of the intended change. But even when the task is narrowed, the agent still struggles to reproduce the exact developer modification, and the hardest physics categories stay near zero.

To me, that is the real research signal.

We are not only measuring intelligence in the abstract. We are measuring whether an agent can respect a scientific system where a local edit has physical consequences. That is a much higher bar than autocomplete. It is closer to asking whether the model can become a junior scientific software collaborator who knows when a line of code is also a statement about the world.

There is also a practical reason I care about this.

Earth System Model development is slow because the work sits at the intersection of domain science, numerical methods, legacy Fortran, HPC, and a lot of tacit knowledge. If agents can help even a little, the leverage is enormous. They could search large codebases, draft candidate patches, check local physical consistency, and help experts move faster.

But if they help without physics-aware review, they can also make the work more dangerous.

That is why I do not think the answer is just bigger models. We probably need agents with specialized verification tools. We need conservation-law checkers, unit and sign sanity checks, codebase-specific context, and review workflows where the model is not treated as an oracle. The goal is not to replace domain scientists. The goal is to build tools that make expert review sharper and faster.

ESM-bench is still a first step. The current release focuses on reviewable patch-local evidence, not full long-horizon simulation audits. That is a real limitation. A static diff can reveal wrong targets, wrong mechanisms, local unit errors, and missing safeguards, but it cannot prove that a modified model preserves water balance over ten simulated years.

Still, I think this is the right place to start.

Before we ask AI agents to run climate science, we should ask whether they can change one piece of climate model code without breaking the physics hiding inside it.

And right now, the answer is, not reliably yet.

That is exactly why the benchmark is worth building.
