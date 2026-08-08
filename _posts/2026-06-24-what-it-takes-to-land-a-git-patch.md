---
title: 'What It Actually Takes to Land a Patch in Git'
date: 2026-06-24
permalink: /posts/2026/06/what-it-takes-to-land-a-git-patch/
tags:
  - git
  - open-source
  - contribution
  - gitgitgadget
  - reflection
---

In [my first post on this]({{ site.baseurl }}/posts/2026/06/gitgitgadget-first-pr/) I described sending a patch through GitGitGadget and watching it land on the mailing list as `v1`. That post ended with the patch waiting for review. [It has since merged]({{ site.baseurl }}/posts/2026/06/official-git-contributor/). Now that I have seen the full lifecycle, from typo to `master`, here is what actually mattered.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

**The bug found me, not the other way around.**

I did not go looking for a typo in `.gitattributes` to manufacture a first contribution. I found it because of a real annoyance on this very blog's repository, which I originally set up and maintained on a Mac. When I started operating on it from a Windows machine, `git status` began showing a pile of files as `modified` even though nobody had touched their contents. Nothing in those files had actually changed. Git was flagging them as dirty purely because of line-ending normalization differences between the two OSes, CRLF on Windows versus LF on Mac/Linux.

I did not just live with it. I treated it as a real Git problem worth solving properly, and added a `.gitattributes` file to this repo (`* text=auto eol=lf`, plus explicit `eol=lf` rules for every text file type) to force consistent LF line endings regardless of which OS touched the repo. Writing those rules out by hand is what taught me the exact syntax: `eol=lf` is the attribute that normalizes line endings, not `eof=lf`. With that fresh in my head, I went looking at how a much larger, much older project handled the same problem, and opened Git's own `.gitattributes`. The same class of mistake, `eof=lf` where it should have read `eol=lf`, was sitting in the project's own source, on the `*.pl` line.

**The PR was never the contribution. The PR was a translation step.**

GitGitGadget exists because Git's real review process is email on `git@vger.kernel.org`, not a GitHub merge button. The PR I opened was input to a translator, not a request that a maintainer clicks "merge" on directly. My commit landed because Junio applied the patch from the list, not because anyone pressed "Merge pull request."

**Permission is a separate gate from correctness.**

My patch was already correct, signed off, and DCO-clean before GitGitGadget would even preview it. `Error: User ktwu01 is not yet permitted to use GitGitGadget` is an anti-spam gate, unrelated to the quality of the change. It only opened after an already-permitted contributor commented `/allow`. A technically perfect patch from a brand-new identity still needs a human vouching for that identity first.

**Small details outside the diff still block the pipeline.**

The warning `WARNING: ktwu01 has no public email address set on GitHub` was not about the patch either. Without a public email, GitGitGadget cannot Cc me on the mailing list thread, so I would never see review feedback even after the patch shipped. Setting the public email was a five-minute fix, but skipping it would have silently cut me out of my own thread.

**Scope discipline is what made the patch acceptable in the first place.**

I did not try to fix everything wrong with line-ending handling across the file. I fixed one mistyped attribute, `eof=lf` where the rest of the file used `eol=lf`, verified it with `git check-attr`, and stopped there. A first contribution to a project with this much history is not the place to also restructure conventions you do not yet have standing to question.

**The Signed-off-by is not decoration.**

I deliberately did not add an AI co-author line. `Signed-off-by` under the Developer Certificate of Origin is a statement that I understand the patch, have the right to submit it, and take responsibility for it under the project's rules. That is a different kind of claim than "a tool helped me write this," and conflating the two would have been dishonest about who is accountable for the change.

**The merge commit and the content commit are not the same thing, and that distinction matters even when reading your own history.**

When I first looked at the merge commit on GitHub, I only saw Junio listed, and for a moment that looked like my authorship had vanished. It had not. Merge commits show the person who performed the merge; the actual patch commit underneath it still lists me as author and Junio as committer, which is exactly how mailing-list-applied patches are supposed to look. Reading git history correctly is its own skill, separate from writing the patch.

None of this required deep C knowledge or a large diff. It required reading the project's existing conventions before assuming I knew better than them, treating the human-in-the-loop permission step and the email-visibility warning as real blockers rather than noise, and being precise about what I was actually claiming when I signed my own name.

That is the whole list. The technical fix was one character.

**Related posts:**
- [Sending My First Git Patch to the GitGitGadget Doorstep]({{ site.baseurl }}/posts/2026/06/gitgitgadget-first-pr/), the original submission story.
- [I Am Now an Official Git Contributor]({{ site.baseurl }}/posts/2026/06/official-git-contributor/), the merge announcement with the verified commit links.
- [中文版：把一个补丁真正送进 Git 需要什么]({{ site.baseurl }}/zh/posts/2026/06/what-it-takes-to-land-a-git-patch/)
