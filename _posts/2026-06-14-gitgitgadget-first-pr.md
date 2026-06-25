---
title: 'Sending My First Git Patch to the GitGitGadget Doorstep'
date: 2026-06-14
permalink: /posts/2026/06/gitgitgadget-first-pr/
tags:
  - git
  - open-source
  - contribution
  - gitgitgadget
  - reflection
---

Today I got my first Git patch onto the mailing list.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

Here is how it went.

It started with my own blog's repository, which I originally set up and maintained on a Mac. When I started operating on it from a Windows machine, `git status` began showing a pile of files as `modified` even though nobody had touched their contents. Git was flagging them as dirty purely because of line-ending normalization differences between the two OSes, CRLF on Windows versus LF on Mac/Linux. I did not just live with it. I treated it as a real Git problem worth solving, and added a `.gitattributes` file to that repo to force consistent LF line endings regardless of which OS touched it. Writing those rules by hand is what made the exact syntax stick: `eol=lf` is the attribute that normalizes line endings, not `eof=lf`.

With that fresh in my head, the thing that first caught my eye was a line in the `git/git` repository on GitHub: `pull requests can be turned into patches to the mailing list via GitGitGadget`. That sentence is easy to misread. You might think that opening a PR the way you always do already counts as contributing to Git.

Once I actually looked into it, that turned out not to be the case.

The upstream collaboration model for the Git project is still, at its core, a mailing list. A PR on GitHub is only an entry point. GitGitGadget turns the PR into an email patch and sends it to `git@vger.kernel.org` for review. In other words, this is not a GitHub merge PR in the ordinary sense.

That step matters a lot.

If I had just copied the `.gitattributes` from my personal website over, opened a PR, and announced that I was here to unify line endings for Git, I would have looked very much like an amateur. `git/git` has had its own `.gitattributes` for a long time, and the project has very mature conventions for commit format, commit messages, `Signed-off-by`, and patch threading.

So I stopped and took a look at the real upstream file first.

And I found a small but genuine problem.

In `git/git`'s `.gitattributes`, there is a line that reads like this.

```text
*.pl text eof=lf diff=perl
```

The neighboring lines are `*.perl text eol=lf diff=perl`, `*.pm text eol=lf diff=perl`, and `*.py text eol=lf diff=python`.

The `eof=lf` here looks very much like a typo. Git's line-ending attribute is `eol=lf`, not `eof=lf`. So this rule was supposed to make `.pl` files use LF line endings, but because it was written as `eof`, it never actually did that.

This is a reasonable first patch.

Small, clear, verifiable, no grand theory required, and it does not touch the project's core logic.

The change I made is a single line.

```diff
-*.pl text eof=lf diff=perl
+*.pl text eol=lf diff=perl
```

Then I verified it with `git check-attr`, confirming that `.pl` files now resolve to `eol: lf`. I also ran `git diff --check` to make sure there were no whitespace problems.

Next came the commit.

I deliberately did not add an AI co-author here. The reason is simple. A Git patch needs a `Signed-off-by`, and that is not a decorative signature. It is you saying: I understand this patch, I have the right to submit it, and I am willing to take responsibility for it under the project's rules.

So the commit carries only my own sign-off.

```text
gitattributes: fix eol attribute for Perl scripts

The *.pl pattern currently sets eof=lf, which is not a built-in
attribute used for line-ending normalization.

Use eol=lf instead, matching the neighboring *.perl and *.pm rules, so
Perl scripts are checked out with LF line endings.

Signed-off-by: ktwu01 <ktwu01@gmail.com>
```

Then I created my own fork.

The repository is `ktwu01/git`, the branch is `kw/fix-pl-eol-attribute`, and the commit is `92ba4d499d gitattributes: fix eol attribute for Perl scripts`.

Finally, I opened the PR at the GitGitGadget entry point.

The PR is here.

[https://github.com/gitgitgadget/git/pull/2151](https://github.com/gitgitgadget/git/pull/2151)

At that point the state was as follows.

DCO had passed, which meant the `Signed-off-by` was fine. GitGitGadget's `handle_pr_push` had also passed, which meant the PR entry point itself was recognized.

But when I sent `/preview`, GitGitGadget replied with one line.

```text
Error: User ktwu01 is not yet permitted to use GitGitGadget
```

This was not the patch itself failing. It is GitGitGadget's anti-spam permission mechanism for new users. A first-time user needs someone who is already permitted to comment `/allow` on the PR.

So I left a comment on the PR asking an authorized user to allow me.

And then things actually moved forward.

An already-permitted user (`mmontalbo`) commented `/allow` on the PR, and GitGitGadget replied confirming that `ktwu01` could now use GitGitGadget.

It also gave me a warning.

```text
WARNING: ktwu01 has no public email address set on GitHub
```

The meaning is that I had no public email set on GitHub, and GitGitGadget needs an email address so it can Cc me when the patch goes to the mailing list, so that I receive any review replies.

This step is easy to overlook, but it is actually important. Without it, the patch still goes out, but all the discussion others have about your patch on the mailing list never reaches you.

So I went into my GitHub profile settings and set `ktwu01@gmail.com` as my public email. This is the same address used in my commit's `Signed-off-by`, so the two are consistent.

Only then did the real sending flow begin.

First, `/preview`.

```bash
gh pr comment 2151 --repo gitgitgadget/git --body "/preview"
```

GitGitGadget generated a preview email. I made a point of looking at the preview rather than rushing to submit. The subject was `gitattributes: fix eol attribute for Perl scripts`, the commit message was complete, the diff was exactly the one line changing `eof=lf` to `eol=lf`, and the `Signed-off-by` was there, with no AI co-author. Everything checked out.

Second, once the preview looked right, `/submit`.

```bash
gh pr comment 2151 --repo gitgitgadget/git --body "/submit"
```

This is the step that actually sends the patch to the Git mailing list. GitGitGadget replied.

```text
Submitted as pull.2151.git.1781497525828.gitgitgadget@gmail.com
```

The patch went out as `v1` on `git@vger.kernel.org`. Its address in the mailing list archive is:

[https://lore.kernel.org/git/pull.2151.git.1781497525828.gitgitgadget@gmail.com](https://lore.kernel.org/git/pull.2151.git.1781497525828.gitgitgadget@gmail.com)

Third, wait for review.

The patch is on the mailing list now, so what follows is waiting for replies from the maintainers and others. Because the email is public, GitGitGadget Cc's me, so replies arrive directly in my inbox.

If someone points out a problem, the move is not to append a small fixup commit on top of the original patch. Git's workflow prefers rewriting history and reorganizing the patch series. That means fixing it with `git rebase -i` or `git commit --amend`, force-pushing, and then sending `/submit` again, which GitGitGadget will resend as `v2`.

The biggest takeaway from all this is that open-source contribution is not as simple as clicking a few buttons on GitHub.

Especially for a long-established project like Git, the collaboration culture was not built around web PRs. It was built around email, patches, review threads, and the maintainers' rhythm. You have to respect its system first before you have earned the right to put something into it.

But precisely because of that, the whole process has a very plain engineering feel to it.

It is not about turning everything upside down on day one.

It is about finding a small typo, confirming it is real, writing a small patch, signing your own name, sending it to the right place, and then waiting for others to review.

The patch is now on the Git mailing list as `v1`. If it really does get accepted in the end, that is when I will have taken the first real step toward becoming a Git contributor.

It is not time to brag yet.

But the door is not just knocked on. The patch has crossed the threshold and is sitting on the mailing list, waiting for someone to look at it.

**Update, 2026-06-24: the patch landed.**

Junio C Hamano merged the branch into `master`. The commit is there with my name on it as author.

[https://github.com/git/git/commit/0bf506efd40251ebdc9ed829d8bb90d879d2c7aa](https://github.com/git/git/commit/0bf506efd40251ebdc9ed829d8bb90d879d2c7aa)

```text
Author: Koutian Wu <ktwu01@gmail.com>
Committer: Junio C Hamano <gitster@pobox.com>
```

The merge itself is here.

[https://github.com/git/git/commit/8cf57cbec4de63ad41e8b3c705505771784abf50](https://github.com/git/git/commit/8cf57cbec4de63ad41e8b3c705505771784abf50)

So it is time to say it plainly now. I am a Git contributor.
