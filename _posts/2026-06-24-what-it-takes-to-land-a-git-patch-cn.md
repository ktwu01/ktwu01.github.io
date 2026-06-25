---
title: '把一个补丁真正送进 Git 需要什么'
date: 2026-06-24
permalink: /zh/posts/2026/06/what-it-takes-to-land-a-git-patch/
tags:
  - git
  - open-source
  - contribution
  - gitgitgadget
  - reflection
---

在[第一篇文章]({{ site.baseurl }}/zh/posts/2026/06/gitgitgadget-first-pr/)里，我写了怎么通过 GitGitGadget 把补丁发出去，它作为 `v1` 落在了邮件列表上。那篇文章结束在等待 review 的状态。[现在它已经合并了]({{ site.baseurl }}/zh/posts/2026/06/official-git-contributor/)。看完从一个拼写错误到进入 `master` 的完整过程，下面是我觉得真正重要的几点。

> 作者：[Koutian Wu](https://www.linkedin.com/in/ktwu01/)；[GitHub: ktwu01](https://github.com/ktwu01/)

**这个 bug 是它先找上我的，不是我去找它。**

我不是特意去 `.gitattributes` 里找拼写错误来制造一个"第一次贡献"。是因为这个博客自己的仓库带来的一个真实的烦恼。这个仓库最初是我在 Mac 上搭建和维护的。后来我开始在 Windows 机器上对它进行操作，`git status` 里就开始有一堆文件被标成 `modified`，但其实内容根本没人动过。这些文件实际内容并没有变化。Git 把它们标脏，纯粹是因为两个操作系统的换行符规范化方式不一样，Windows 上是 CRLF，Mac/Linux 上是 LF。

我没有就这样放着不管。我把它当成一个真正值得解决的 Git 问题，给这个仓库加了一个 `.gitattributes` 文件（`* text=auto eol=lf`，再加上对每种文本文件类型显式写的 `eol=lf` 规则），强制不管哪个操作系统去碰这个仓库，换行符都统一成 LF。亲手写这些规则的过程，让我把语法记得很清楚：真正能规范化换行符的属性是 `eol=lf`，不是 `eof=lf`。带着这个刚学会的细节，我去看了一个规模更大、历史更久的项目是怎么处理同样问题的，打开了 Git 自己的 `.gitattributes`。结果发现同一类错误，`eof=lf` 本该写成 `eol=lf`，就躺在 `*.pl` 那一行，是这个项目自己的源码里的问题。

**PR 从来不是贡献本身，PR 只是一个翻译步骤。**

GitGitGadget 之所以存在，是因为 Git 真正的 review 流程是 `git@vger.kernel.org` 上的邮件，不是 GitHub 上点一个 merge 按钮。我开的 PR 是给一个翻译器的输入，不是直接请维护者点 "Merge pull request"。我的 commit 能合进去，是因为 Junio 从邮件列表上应用了这个补丁，不是因为谁按了合并按钮。

**权限和补丁本身的正确性，是两道完全独立的关卡。**

在 GitGitGadget 同意 preview 之前，我的补丁就已经是正确的、签过字的、DCO 也通过的。`Error: User ktwu01 is not yet permitted to use GitGitGadget` 是一个反垃圾机制，跟补丁质量没有关系。它只在一个已经有权限的贡献者评论了 `/allow` 之后才打开。一个技术上完美的补丁，如果来自一个全新的身份，仍然需要一个真人先为这个身份做担保。

**diff 之外的小细节，照样能卡住整条流水线。**

`WARNING: ktwu01 has no public email address set on GitHub` 这条 warning 也跟补丁本身无关。没有公开邮箱，GitGitGadget 就无法在邮件列表的讨论里 Cc 我，那就算补丁发出去了，我也永远看不到 review 的反馈。设置公开邮箱只花了五分钟，但跳过这一步，会让我在自己这条讨论线里悄无声息地消失。

**克制范围，恰恰是这个补丁能被接受的原因。**

我没有试图把这个文件里所有换行符相关的问题一次性修完。我只修了一个写错的属性，`eof=lf` 应该是 `eol=lf`，用 `git check-attr` 验证了一下，然后就停在这里。对一个历史这么久的项目，第一次贡献不是去重新设计你还没有资格质疑的约定的地方。

**Signed-off-by 不是装饰。**

我特意没有加 AI co-author。`Signed-off-by` 在 Developer Certificate of Origin 下面，是在声明我理解这个补丁，我有权提交它，我愿意按项目规则为它负责。这和"有工具帮我写了这个"是不同性质的声明，把两者混在一起，就是在补丁责任人这件事上不诚实。

**merge commit 和内容 commit 不是一回事，这一点在读自己历史的时候同样重要。**

我第一次在 GitHub 上看那个合并 commit 的时候，只看到了 Junio，一瞬间以为自己的作者身份消失了。其实没有。merge commit 显示的是执行合并的人；下面那个真正的补丁 commit 上，作者仍然是我，committer 是 Junio，这正是邮件列表应用补丁之后该有的样子。正确读懂 git 历史，本身也是一项和写补丁分开的技能。

这些都不需要很深的 C 语言知识，也不需要一个很大的 diff。需要的是先去读项目已有的约定，而不是想着自己更懂；把人工权限关卡和邮箱可见性的 warning 当成真正的阻塞项而不是噪音；以及在自己签名的时候，清楚自己到底在声明什么。

就这些。技术上的修复，只有一个字符。
