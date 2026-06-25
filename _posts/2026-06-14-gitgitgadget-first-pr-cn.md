---
title: '我把第一个 Git 补丁送到了 GitGitGadget 门口'
date: 2026-06-14
permalink: /zh/posts/2026/06/gitgitgadget-first-pr/
tags:
  - git
  - open-source
  - contribution
  - gitgitgadget
  - reflection
---

今天我差一点，就把自己的第一个 Git 项目补丁送进邮件列表了。

> 作者：[Koutian Wu](https://www.linkedin.com/in/ktwu01/)；[GitHub: ktwu01](https://github.com/ktwu01/)

事情是这样的。

起点是我自己这个博客的仓库。这个仓库最初是我在 Mac 上搭建和维护的。后来我开始在 Windows 机器上对它进行操作，`git status` 里就开始有一堆文件被标成 `modified`，但其实内容根本没人动过。Git 把它们标脏，纯粹是因为两个操作系统的换行符规范化方式不一样，Windows 上是 CRLF，Mac/Linux 上是 LF。我没有就这样放着不管，而是把它当成一个真正值得解决的 Git 问题，给那个仓库加了一个 `.gitattributes` 文件，强制不管哪个操作系统去碰它，换行符都统一成 LF。亲手写这些规则的过程，让我把语法记得很清楚：真正能规范化换行符的属性是 `eol=lf`，不是 `eof=lf`。

带着这个刚学会的细节，我一开始看到的是 GitHub 上 `git/git` 仓库里的那句话，`pull requests can be turned into patches to the mailing list via GitGitGadget`。这句话很容易让人误解，以为只要像平时一样开一个 PR，就算是在给 Git 做贡献。

但真正看进去之后才发现，不是这么回事。

Git 这个项目的上游协作方式，本质上还是邮件列表。GitHub 上的 PR 只是一个入口，GitGitGadget 会把 PR 转成邮件补丁，送到 `git@vger.kernel.org` 上接受 review。也就是说，这不是普通意义上的 GitHub merge PR。

这一步非常关键。

如果一上来就把个人网站里的 `.gitattributes` 直接搬过去，开个 PR 说我来帮 Git 统一换行符，大概率会显得非常外行。因为 `git/git` 自己早就有 `.gitattributes` 了，而且这个项目对提交格式、commit message、Signed-off-by、patch 线程都有非常成熟的规范。

于是我先停下来，看了一眼真正的上游文件。

然后发现了一个很小，但很真实的问题。

在 `git/git` 的 `.gitattributes` 里，有一行是这样的。

```text
*.pl text eof=lf diff=perl
```

旁边几行是 `*.perl text eol=lf diff=perl`，`*.pm text eol=lf diff=perl`，`*.py text eol=lf diff=python`。

这里的 `eof=lf` 看起来非常像一个拼写错误。Git 的换行符属性是 `eol=lf`，不是 `eof=lf`。所以这个规则本来应该让 `.pl` 文件用 LF 换行，但由于写成了 `eof`，它实际上没有起到这个作用。

这就是一个比较合适的 first patch。

小，明确，可验证，不需要发明大理论，也不会碰项目核心逻辑。

我做的改动只有一行。

```diff
-*.pl text eof=lf diff=perl
+*.pl text eol=lf diff=perl
```

然后我用 `git check-attr` 验证了一下，`.pl` 文件现在确实能解析出 `eol: lf`。也跑了 `git diff --check`，确保没有空白问题。

接下来是提交。

这一步我特意没有加 AI co-author。原因很简单，Git 的补丁需要 `Signed-off-by`，它不是一个装饰性的署名，而是你在说，这个补丁我理解，我有权提交，我愿意按项目规则负责。

所以 commit 里只有我自己的签名。

```text
gitattributes: fix eol attribute for Perl scripts

The *.pl pattern currently sets eof=lf, which is not a built-in
attribute used for line-ending normalization.

Use eol=lf instead, matching the neighboring *.perl and *.pm rules, so
Perl scripts are checked out with LF line endings.

Signed-off-by: ktwu01 <ktwu01@gmail.com>
```

然后我创建了自己的 fork。

仓库是 `ktwu01/git`，分支是 `kw/fix-pl-eol-attribute`，commit 是 `92ba4d499d gitattributes: fix eol attribute for Perl scripts`。

最后，我把 PR 开到了 GitGitGadget 的入口。

PR 地址在这里。

[https://github.com/gitgitgadget/git/pull/2151](https://github.com/gitgitgadget/git/pull/2151)

现在的状态是这样的。

DCO 已经通过了，说明 `Signed-off-by` 这一关没问题。GitGitGadget 的 `handle_pr_push` 也过了，说明这个 PR 入口本身是被识别的。

但我发 `/preview` 的时候，GitGitGadget 回了一句。

```text
Error: User ktwu01 is not yet permitted to use GitGitGadget
```

这不是补丁本身失败，而是 GitGitGadget 对新用户有一个反垃圾权限机制。第一次使用的人，需要一个已经被允许使用 GitGitGadget 的用户在 PR 里评论 `/allow`。

所以我已经在 PR 里留言，请 authorized user 帮我 allow。

然后，事情真的往前走了。

一个已经有权限的用户（`mmontalbo`）在 PR 里评论了 `/allow`，GitGitGadget 随即回复，确认 `ktwu01` 现在可以使用 GitGitGadget 了。

不过它同时给了我一个 warning。

```text
WARNING: ktwu01 has no public email address set on GitHub
```

意思是，我在 GitHub 上没有设置公开邮箱，而 GitGitGadget 需要一个邮箱地址，才能在补丁发到邮件列表时把我 Cc 进去，让我能收到 review 的回信。

这一步很容易被忽略，但其实很重要。如果不设置，补丁是能发出去的，但别人在邮件列表上对你这个补丁的所有讨论，你自己反而收不到。

所以我去 GitHub 的 profile 设置里，把 `ktwu01@gmail.com` 设成了公开邮箱。这个邮箱和我 commit 里 `Signed-off-by` 用的是同一个，前后一致。

接下来才进入真正的发送流程。

第一步，发 `/preview`。

```bash
gh pr comment 2151 --repo gitgitgadget/git --body "/preview"
```

GitGitGadget 生成了一封预览邮件。我特意先看预览，而不是急着 submit。subject 是 `gitattributes: fix eol attribute for Perl scripts`，commit message 完整，diff 就是那一行 `eof=lf` 改成 `eol=lf`，`Signed-off-by` 也在，没有 AI co-author。一切正常。

第二步，预览确认没问题之后，发 `/submit`。

```bash
gh pr comment 2151 --repo gitgitgadget/git --body "/submit"
```

这一步才是真正把补丁发到 Git 邮件列表。GitGitGadget 回复了。

```text
Submitted as pull.2151.git.1781497525828.gitgitgadget@gmail.com
```

补丁就这样作为 `v1` 上了 `git@vger.kernel.org`。它在邮件列表归档里的地址是：

[https://lore.kernel.org/git/pull.2151.git.1781497525828.gitgitgadget@gmail.com](https://lore.kernel.org/git/pull.2151.git.1781497525828.gitgitgadget@gmail.com)

第三步，等 review。

现在补丁已经在邮件列表上了，接下来就是等维护者和其他人的回信。因为邮箱已经公开，GitGitGadget 会把我 Cc 进去，回信会直接到我邮箱。

如果有人指出问题，就不要在原补丁后面追加一个修修补补的 commit。Git 的流程更倾向于改历史，重新整理 patch series。也就是用 `git rebase -i` 或 `git commit --amend` 修好，再 force-push，然后发 `/submit`，GitGitGadget 会把它作为 `v2` 重新发一遍。

这件事给我的最大感受是，开源贡献并不是在 GitHub 上点几个按钮那么简单。

尤其是 Git 这种老牌项目，它的协作文化不是围绕网页 PR 建立的，而是围绕邮件、patch、review thread、维护者节奏建立的。你必须先尊重它的系统，才有资格往里面放东西。

但也正因为这样，整个过程反而有一种非常朴素的工程感。

不是要一上来改天换地。

就是发现一个小拼写错误，确认它是真的，写一个小补丁，签上自己的名字，送到正确的地方，然后等别人 review。

现在补丁已经作为 `v1` 发到了 Git 邮件列表上。如果它最后真的被接收，我才算真正迈出了成为 Git contributor 的第一步。

还没到能吹的时候。

但门不只是敲响了，补丁已经迈过了门槛，躺在邮件列表上等人来看。

**更新，2026-06-24：补丁合并了。**

Junio C Hamano 把这个分支合并进了 `master`。commit 上挂着我的名字，作者就是我。

[https://github.com/git/git/commit/0bf506efd40251ebdc9ed829d8bb90d879d2c7aa](https://github.com/git/git/commit/0bf506efd40251ebdc9ed829d8bb90d879d2c7aa)

```text
Author: Koutian Wu <ktwu01@gmail.com>
Committer: Junio C Hamano <gitster@pobox.com>
```

合并的那个 commit 在这里。

[https://github.com/git/git/commit/8cf57cbec4de63ad41e8b3c705505771784abf50](https://github.com/git/git/commit/8cf57cbec4de63ad41e8b3c705505771784abf50)

所以现在可以说得明白一点了。我是 Git 的 contributor 了。
