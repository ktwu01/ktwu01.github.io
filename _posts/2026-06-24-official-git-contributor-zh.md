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

我不是闲着没事翻 Git 源码才碰到这个拼写错误的。我是因为这个博客自己的仓库上的一个真实的 CRLF/LF 问题才发现它的。这个仓库最初是我在 Mac 上搭建和维护的，后来我开始在 Windows 机器上对它进行操作，`git status` 就开始把一堆内容根本没变的文件标成 `modified`，纯粹是因为两个操作系统的换行符规范化方式不一样。我没有就这样放着不管，给这个仓库加了一个 `.gitattributes` 文件，强制统一成 LF 换行。亲手写这些规则的过程，让我学会了正确的写法，是 `eol=lf`，不是 `eof=lf`。这才让我在一天后，认出了同样的拼写错误，原来就躺在 Git 自己的 `.gitattributes` 里。

这个补丁现在是规范仓库历史的一部分，每一次 `git clone` 都会带着它。

只是一行修复。但它确实算数。

**相关文章：**
- [我把第一个 Git 补丁送到了 GitGitGadget 门口]({{ site.baseurl }}/zh/posts/2026/06/gitgitgadget-first-pr/)，最初提交的完整故事。
- [把一个补丁真正送进 Git 需要什么]({{ site.baseurl }}/zh/posts/2026/06/what-it-takes-to-land-a-git-patch/)，关于 GitGitGadget 流程的完整回顾。
- [English version: I Am Now an Official Git Contributor]({{ site.baseurl }}/posts/2026/06/official-git-contributor/)
