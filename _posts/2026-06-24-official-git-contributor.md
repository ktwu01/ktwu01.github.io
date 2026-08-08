---
title: 'I Am Now an Official Git Contributor'
date: 2026-06-24
permalink: /posts/2026/06/official-git-contributor/
tags:
  - git
  - open-source
  - contribution
  - gitgitgadget
---

The patch I [sent to the GitGitGadget doorstep]({{ site.baseurl }}/posts/2026/06/gitgitgadget-first-pr/) ten days ago has been merged into `master`.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

Junio C Hamano, the Git maintainer, merged the branch `kw/gitattributes-typofix` into `master`. The commit carries my name as author.

[https://github.com/git/git/commit/0bf506efd40251ebdc9ed829d8bb90d879d2c7aa](https://github.com/git/git/commit/0bf506efd40251ebdc9ed829d8bb90d879d2c7aa)

```text
Author: Koutian Wu <ktwu01@gmail.com>
Committer: Junio C Hamano <gitster@pobox.com>
Subject: gitattributes: fix eol attribute for Perl scripts
```

The merge itself:

[https://github.com/git/git/commit/8cf57cbec4de63ad41e8b3c705505771784abf50](https://github.com/git/git/commit/8cf57cbec4de63ad41e8b3c705505771784abf50)

The fix was one line. The `.gitattributes` file had `*.pl text eof=lf diff=perl`, where `eof` should have been `eol`. Git's line-ending attribute is `eol=lf`, not `eof=lf`, so the rule never actually normalized line endings for Perl scripts. I changed it to match the neighboring `*.perl` and `*.pm` rules, signed it off under my own name, and sent it through GitGitGadget to the mailing list.

I did not stumble onto this typo by browsing Git's source for fun. I found it because of a real CRLF/LF problem on this very blog's own repository, which I originally set up and maintained on a Mac. Once I started operating on it from a Windows machine, `git status` kept showing a pile of files as `modified` even though nobody had touched their contents, purely because of line-ending normalization differences between the two OSes. I did not just live with it. I added a `.gitattributes` file to this repo to force consistent LF endings, and writing those rules by hand is what taught me the correct syntax, `eol=lf`, not `eof=lf`. That is what let me spot the identical typo sitting in Git's own `.gitattributes` a day later.

That patch is now part of the history that every `git clone` of the canonical repository carries forward.

It was a one-line fix. It still counts.

**Related posts:**
- [Sending My First Git Patch to the GitGitGadget Doorstep]({{ site.baseurl }}/posts/2026/06/gitgitgadget-first-pr/), the original submission story.
- [What It Actually Takes to Land a Patch in Git]({{ site.baseurl }}/posts/2026/06/what-it-takes-to-land-a-git-patch/), the full retrospective on the GitGitGadget process.
- [中文版：我现在是正式的 Git Contributor 了]({{ site.baseurl }}/zh/posts/2026/06/official-git-contributor/)
