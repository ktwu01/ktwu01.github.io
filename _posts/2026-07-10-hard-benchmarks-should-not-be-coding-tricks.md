---
title: 'Hard Benchmarks Should Not Become Coding Tricks'
date: 2026-07-10
permalink: /posts/2026/07/hard-benchmarks-should-not-be-coding-tricks/
tags:
  - AI
  - Benchmark
  - Science
  - Agents
  - Evaluation
  - Reflection
---

The most dangerous failure mode of an AI science benchmark is not that it is too hard, it is that it quietly becomes either a coding trick or a guessing game.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

I had a very interesting argument with my agent today.

The concrete context was small. We were looking at a pull request for a scientific agent benchmark. A reviewer, Allen, asked us to stress-test the task for fairness. Not just whether agents failed. That part was already clear. The sharper question was whether agents failed for the right reason.

This sounds like a subtle distinction, but I think it is the whole game.

A bad benchmark can be hard because it hides arbitrary details. A good benchmark is hard because reality is hard.

At first, my agent did the kind of thing a strong coding agent should do. It read the task files, found a real mismatch, and said the instruction claimed that several cases started from the same physical forcing row when the actual data used five different forcing rows. That was a real bug. Cheap to fix. No drama.

Then it went further.

It started perturbing the oracle. What if a scientifically reasonable solution used a different Michaelis constant? What if it used a Jmax-saturated electron transport form? What if it used a different C4 initial slope? Some of these choices are defensible in plant physiology. Some of them failed the verifier badly.

The agent's first interpretation was basically, this task is guess-the-oracle.

I pushed back pretty hard.

Because the thing I care about here is not making agents comfortable. The point of a science benchmark is not to hand agents a neat little programming exercise with every constant written on the page. If we do that, then the task stops being science. It becomes implementation.

And SOTA agents are already very good at implementation.

This was the sentence I told the agent, and honestly I still stand by it.

> I do think we don’t need to give agents constants. If we give agents constants, then everything becomes a coding trick, and the agents will easily succeed at all of the tasks. If we give them all of the exact parameters, it becomes a trivial coding trick and loses its scientific meaning.
>
> I don’t think this would be good because the task becomes useless. It is not a scientific task anymore because SOTA agents are excellent at coding and will definitely finish all the tasks in one call.
>
> We are here to challenge them, not to design another useless coding trick. Because, you know, even in the exams like HumanLast exam, they do not provide any value sometimes. As for the questions, they do not provide any values; they just let agents answer, because answering the numbers is a part of testing.
>
> We should make the questions hard enough and, here, this is scientifically valid.

I know the wording is a little raw. That is why I like it.

Because this is exactly the fight people keep avoiding when they talk about benchmarks.

If you give the model every equation, every parameter, every tolerance, every special case, every branch condition, and every data convention, then of course Claude Code or Codex or Cursor can write the solver. That is not a scientific reasoning task. That is a coding interview with better variable names.

The hard part of science is often not typing the equation after someone gives it to you.

The hard part is knowing which equation lives in this world.

A real scientist has to know where to look, which literature lineage is being invoked, what assumptions are normal in that subfield, what parameterization belongs to which model family, and which details are part of the physics rather than decorative background. If an agent has internet access, then asking it to recover those things is not unfair. It is the task.

This is why I think the HumanLast exam analogy matters. Those questions often do not give you every number. They ask you to answer. Finding the right missing number, the right theorem, the right historical fact, the right object in the world, is part of the test.

So no, I do not want to paste constants into the prompt.

I really do not.

But here is where the agent said something that changed the shape of the argument.

It corrected itself. After re-reading the task, it realized the oracle was not just random. It was not an arbitrary pile of secret constants. It was a recognizable Collatz and Ball-Berry style parameterization, in the CLM and Bonan lineage. The agent had called it ad hoc too quickly.

That correction mattered.

Then it made a distinction that I think is the cleanest version of the whole debate.

> Hard = a correct expert has to work to pass. Good. Keep it.
>
> Valid = a correct expert who reasons correctly can pass.

This is the knife edge.

A benchmark should absolutely make agents work. It should make them search, read, infer, test, debug, and recover from wrong turns. It should punish shallow pattern matching. It should punish plausible prose that never becomes a working scientific result.

But it should not punish a correct expert for solving a different, equally valid version of an underspecified problem.

That is the difference between hiding the answer and hiding the question.

Hiding the answer is fine. That is what exams do.

Hiding the question is not fine. That is how you accidentally test telepathy.

In this task, the right answer was not to dump Kc, Ko, Q10 values, Ball-Berry intercepts, light conversion details, and solver tolerances into the instruction. That would be giving away the scientific work.

The right answer was much smaller.

Name the model family.

Say that the target is a coupled Collatz style photosynthesis and Ball-Berry stomatal conductance leaf model, in the CLM or Bonan lineage. Do not provide the constants. Do not write the equations. Do not turn it into a recipe. Just tell the agent which scientific object it is supposed to reconstruct.

The agent put it nicely.

> Naming the model is specifying what is asked; it is not giving the answer.

I like that sentence a lot.

Because it preserves the difficulty while removing the unfairness.

If an agent now fails, good. It failed because it did not correctly reconstruct the named scientific model. Maybe it picked the wrong paper. Maybe it found the constants but implemented the coupling incorrectly. Maybe it got the C3 and C4 branches wrong. Maybe it failed to notice the night branch. Maybe it never converged the fixed point. Those are all real failures.

Those are the failures I want to measure.

What I do not want to measure is whether the agent guessed which valid school of plant physiology the hidden oracle silently preferred.

This is where benchmark design becomes strangely philosophical.

You are always choosing what kind of ignorance you want to expose.

Do you want to expose that an agent cannot code a solver once all the scientific content is handed over? That is not very interesting anymore.

Do you want to expose that an agent cannot recover the right model lineage from sparse but fair scientific context? That is interesting.

Do you want to expose that an agent cannot read a paper, translate prose into equations, handle units, couple nonlinear processes, and verify convergence? That is very interesting.

Do you want to expose that an agent cannot guess your private hidden convention? That is just noise.

The annoying part is that all four can produce a failed run.

From the outside, a score of 13 or 55 just looks like failure. But if you care about benchmark quality, you have to ask what kind of failure it was. A failure caused by scientific confusion is signal. A failure caused by an ambiguous prompt is debt.

That was Allen's point, I think.

Not make it easier.

Make it sound.

There is a temptation, especially when building hard tasks, to defend every hidden detail as part of the challenge. I understand that temptation. I have it too. If agents are too strong, every bit of context feels dangerous. You start thinking, if I name the model, maybe they will search it and solve it. If I mention the lineage, maybe the whole thing collapses into code.

But that fear can push you into a bad place.

You start withholding the identity of the scientific object itself.

That is not rigor. That is ambiguity dressed up as difficulty.

The better standard is harsher and cleaner. Give as little context as possible, but give the context needed to make the target unique. Nothing more.

That sentence is probably the whole lesson.

Give as little context as possible, but give the context needed to make the target unique.

For this task, that means minimum fixes only. Fix the factual wording bug about forcing rows. Name the Collatz and Ball-Berry lineage. Clarify whether the PAR field is already the light quantity the model consumes, because otherwise absorbed versus incident light becomes another hidden convention. Keep the constants out. Keep the equations out. Keep the internet on. Re-run the agents and see if they still fail.

If they pass too easily, then the task was never testing science in the first place. It was testing whether they could survive an underspecified prompt.

If they still fail, then good.

Now the failure means something.

I think this is going to become one of the central problems in AI evaluation. As agents get better at coding, the cheap way to make benchmarks hard is to hide more and more details. But that path eventually creates puzzles that only the benchmark author can solve.

The more valuable path is different. Make the task anchored in a real domain object. Make the target uniquely recoverable. Make the route painful. Make the work scientific.

Do not give the constants.

Do not design a useless coding trick.

But do not make the agent read your mind either.

That is the line.
