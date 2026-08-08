---
title: '为什么 `alias rm=trash` 拦不住 AI agent 的 `rm -rf`'
date: 2026-07-11
permalink: /zh/posts/2026/07/why-alias-cannot-stop-an-agent-from-rm-rf/
tags:
  - claude-code
  - codex
  - safety
  - shell
  - agents
---

我问了 Claude Code 一个很具体的问题：能不能只靠把 `rm` alias 成 `trash`，来防止 Codex 意外把文件永久删掉。真实的答案是不能，原因不实测根本看不出来，最后落地的也不是一行配置，而是五层防护。

> 作者：[Koutian Wu](https://www.linkedin.com/in/ktwu01/)；[GitHub: ktwu01](https://github.com/ktwu01/)

**为什么 alias 这个想法看起来对，其实是错的。**

`alias rm='trash'` 是对着终端敲命令的人的标准建议，这个场景下它确实管用。这个想法背后一个没说出口的假设是：AI coding agent 执行命令的方式和人一样，会经过你的交互式 shell，加载你的 `.zshrc`，读到你的 alias。但事实并非如此。在动任何配置之前，我让 Claude Code 先在本机实测，而不是凭记忆推理：

```bash
zsh -c 'alias'          # 只有 2 个内置 alias，我自己定义的一个都没有
bash -c 'shopt expand_aliases'   # 默认是关闭的
```

Codex、Claude Code 这类 agent 执行 shell 命令，走的是 `zsh -c` 或 `bash -c`，也就是非交互式 shell。非交互式 shell 不会加载 `.zshrc`，而非交互式 `bash` 就算加载了，`expand_aliases` 默认也是关的。所以 `alias rm='trash'` 对你原本想防护的那个进程根本不可见。它只能护住你自己在交互式命令行上手滑的那次。

就算它能生效，alias 也只匹配命令行第一个词的字面量。对 `/bin/rm`、`command rm`、`xargs rm`、`find -delete`、`rsync --delete`，或者一句解释器内联代码比如 `python3 -c "shutil.rmtree('x')"`，它完全没有作用。而且它离失效只有一句 `unalias rm` 的距离，这就不满足"需要用户显式操作才能解除"这个底线。

**真正能拦住 agent 的是什么。**

真正管用的那一层，是在 shell 命令真正执行**之前**运行、并且能返回硬拒绝的 hook，而不是一个 agent 执行路径根本看不到的 shell 层面改写。Claude Code 有 `PreToolUse` hook；Codex CLI 有自己的 `execpolicy` 规则系统。两者都位于 shell 的上游，所以不管 alias 表里有没有东西，它们都能看到这条命令。

我写了一个小的 Python `PreToolUse` hook（`~/.claude/hooks/safe_delete_guard.py`），对 Bash 命令的实际文本做模式匹配：命令位置上的 `rm`、`unlink`、`srm`、`shred`（处理了 `sudo`、`xargs`、`bash -c` 包装和绝对路径），加上 `find -delete`、`rsync --delete`、`git clean`、`git reset --hard`、`git checkout --`、`git push --force`、`git branch -D`、`git stash drop/clear`，以及各语言的删除 API（`shutil.rmtree`、`os.remove`、`fs.unlinkSync`、`rimraf`、Ruby 的 `FileUtils.rm*`）。命中就返回 `permissionDecision: "deny"`，这条工具调用根本不会执行。Codex 那边对应的是 `~/.codex/rules/default.rules` 里 `decision="forbidden"` 的前缀规则，再加上 `~/.codex/config.toml` 里的 `sandbox_mode = "workspace-write"` 和 `approval_policy = "on-request"`。

在这两层之下，`rm` 和 `unlink` 本身也被 shim 成转发到 `/usr/bin/trash`（macOS 真正的回收站，而不是删除），通过一个非交互式 shell 也会真正读到的 `PATH` 条目实现，写在 `~/.zshenv` 而不是 `~/.zshrc`，因为 `.zshenv` 是所有 shell（不管交互式还是非交互式）都会读的。交互式的 `alias` 依然保留在最上面，服务于它原本就该服务的场景：接住人自己在命令行上敲错的那一下。

**接着又冒出一个问题：为什么要自己手搓这些，而不是用现成的。**

这套东西搭好之后，用户又让我装一个现成的开源工具 [`destructive_command_guard`](https://github.com/Dicklesworthstone/destructive_command_guard)（`dcg`），一个 Rust 写的、专门解决这个问题的项目，覆盖 Claude Code、Codex CLI、Gemini CLI、Cursor、Hermes。它跑的是同一种"执行前拦截"的 hook，但配了真正的正则/SIMD 引擎、50 多个可选规则包（数据库、Kubernetes、云 CLI、Terraform），还有真正的上下文识别能力：它会拦下 `rm -rf ./src`，但放行 `grep "rm -rf" README.md`，这一点是我自己手写的模式匹配器做不到的。安装脚本自动把它接进了 `~/.claude/settings.json`、`~/.codex/hooks.json`，以及 Gemini/Cursor 对应的配置文件，在同一条 `PreToolUse` 链里排在自定义 hook 前面。

**这些结论是怎么真正验证出来的，而不是断言出来的。**

上面每一条都是拿虚拟文件和虚拟 hook payload 实测出来的，不是照着文档就直接下结论：

- 建了一个用完即扔的文件，通过真实的 Bash 工具对它执行 `rm`，看着它被硬拒绝，`ls -l` 确认文件还在，再用 `/usr/bin/trash` 正确删除它，看着它进了回收站。
- 往自定义 hook 里管道注入了 39 个合成 JSON payload（25 个应该拒绝，14 个应该放行，包括 `git reset HEAD~1` 和 `git reset --hard HEAD~1` 的区分，以及 `npm rm lodash` 和裸 `rm` 的区分），逐条断言判定结果。
- 对 `dcg` 做了同样的事，一次用 Claude 形状的 payload，一次用 Gemini 形状的 payload（`hook_event_name: "BeforeTool"`，`tool_name: "run_shell_command"`），后者是对照 `dcg` 自己的 Rust 源码里 Gemini 分支核实的，不是猜的。
- 确认 `codex execpolicy check --rules <file> git reset --hard HEAD~1` 对着真实的规则文件返回 `"decision":"forbidden"`，而不是对着一份拷贝。

**这件事真正值得记住的地方。**

这类错误有一个通用的形状值得点出来：shell 层面的便利功能（alias、function、`.bashrc` 里的小技巧）保护的是那个在命令行上敲字的人，而它对一个非交互式地和 shell 对话的进程是悄无声息地无效的，而这恰恰就是每一个 coding agent 的工作方式。如果想拦住一个 agent 做破坏性操作，控制点必须放在 agent 执行路径真正会经过的那一层：`PreToolUse` hook、`execpolicy` 规则、沙箱化的写入路径。任何只能通过 `.zshrc` 才能触达的东西，在这个具体的威胁模型下都是一种虚假的安全感，尽管它对"我自己在终端上手滑敲了 `rm -rf`"这个威胁模型来说，仍然是完全正确的建议。

**相关文章：**
- [English version: Why `alias rm=trash` Cannot Stop an AI Agent from `rm -rf`]({{ site.baseurl }}/posts/2026/07/why-alias-cannot-stop-an-agent-from-rm-rf/)
