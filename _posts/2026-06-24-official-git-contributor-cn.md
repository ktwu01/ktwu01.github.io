---
title: '我现在是正式的 Git Contributor 了'
date: 2026-06-24
permalink: /zh/posts/2026/06/official-git-contributor/
tags:
  - git
  - open-source
  - contribution
  - gitgitgadget
---

十天前我[送到 GitGitGadget 门口的那个补丁]({{ site.baseurl }}/zh/posts/2026/06/gitgitgadget-first-pr/)，现在已经合并进 `master` 了。

> 作者：[Koutian Wu](https://www.linkedin.com/in/ktwu01/)；[GitHub: ktwu01](https://github.com/ktwu01/)

Git 的维护者 Junio C Hamano 把分支 `kw/gitattributes-typofix` 合并进了 `master`。commit 上挂的作者是我。

[https://github.com/git/git/commit/0bf506efd40251ebdc9ed829d8bb90d879d2c7aa](https://github.com/git/git/commit/0bf506efd40251ebdc9ed829d8bb90d879d2c7aa)

```text
Author: Koutian Wu <ktwu01@gmail.com>
Committer: Junio C Hamano <gitster@pobox.com>
Subject: gitattributes: fix eol attribute for Perl scripts
```

合并的那个 commit 在这里：

[https://github.com/git/git/commit/8cf57cbec4de63ad41e8b3c705505771784abf50](https://github.com/git/git/commit/8cf57cbec4de63ad41e8b3c705505771784abf50)

这个修复只有一行。`.gitattributes` 里原来写的是 `*.pl text eof=lf diff=perl`，`eof` 应该是 `eol`。Git 的换行符属性是 `eol=lf`，不是 `eof=lf`，所以这条规则其实从来没有真正对 Perl 脚本生效。我把它改成和旁边的 `*.perl`、`*.pm` 一致，用自己的名字签了字，通过 GitGitGadget 发到了邮件列表。

这个补丁现在是规范仓库历史的一部分，每一次 `git clone` 都会带着它。

只是一行修复。但它确实算数。
