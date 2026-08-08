---
title: 'Why `alias rm=trash` Cannot Stop an AI Agent from `rm -rf`'
date: 2026-07-11
permalink: /posts/2026/07/why-alias-cannot-stop-an-agent-from-rm-rf/
tags:
  - claude-code
  - codex
  - safety
  - shell
  - agents
---

I asked Claude Code a narrow question: can I protect this machine from Codex accidentally deleting files forever, just by aliasing `rm` to `trash`? The honest answer turned out to be no, for a reason that is not obvious until you actually test it, and the fix ended up being a five-layer setup rather than a one-liner.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

**Why the alias idea feels right and is wrong anyway.**

`alias rm='trash'` is the standard advice for humans typing at a terminal, and it works fine for that. The unstated assumption is that an AI coding agent executes commands the same way you do: through your interactive shell, with your `.zshrc` sourced, your aliases loaded. It does not. Before touching any config, I had Claude Code actually test this on my machine rather than reason about it from memory:

```bash
zsh -c 'alias'          # only 2 built-in aliases, none of mine
bash -c 'shopt expand_aliases'   # off by default
```

Agents like Codex and Claude Code run shell commands through `zsh -c` or `bash -c`, which are non-interactive shells. Non-interactive shells do not load your `.zshrc`, and non-interactive `bash` has `expand_aliases` off even if it did. So `alias rm='trash'` is invisible to the exact process you were trying to protect against. It only guards your own fingers at an interactive prompt.

Even if it were visible, an alias only matches the literal first word of a command line. It does nothing against `/bin/rm`, `command rm`, `xargs rm`, `find -delete`, `rsync --delete`, or an interpreter one-liner like `python3 -c "shutil.rmtree('x')"`. And it is a single `unalias rm` away from being gone, which fails the "requires explicit user action to disable" bar outright.

**What actually intercepts an agent.**

The layer that matters is a hook that runs *before* the shell command executes and can return a hard deny, not a shell-level rewrite that the agent's execution path never sees. Claude Code has `PreToolUse` hooks; Codex CLI has its own `execpolicy` rules system. Both sit upstream of the shell, so they see the command regardless of what alias table exists or does not exist.

I wrote a small Python `PreToolUse` hook (`~/.claude/hooks/safe_delete_guard.py`) that pattern-matches the actual Bash command text: `rm`, `unlink`, `srm`, `shred` in command position (handling `sudo`, `xargs`, `bash -c` wrappers, and absolute paths), plus `find -delete`, `rsync --delete`, `git clean`, `git reset --hard`, `git checkout --`, `git push --force`, `git branch -D`, `git stash drop/clear`, and language-level deletion APIs (`shutil.rmtree`, `os.remove`, `fs.unlinkSync`, `rimraf`, Ruby `FileUtils.rm*`). A match returns `permissionDecision: "deny"` and the tool call never runs. The mirror piece on the Codex side is `~/.codex/rules/default.rules` with `decision="forbidden"` prefix rules, plus `sandbox_mode = "workspace-write"` and `approval_policy = "on-request"` in `~/.codex/config.toml`.

Underneath that, `rm` and `unlink` themselves get shimmed to redirect to `/usr/bin/trash` (macOS's real trash, not deletion) via a `PATH` entry that non-interactive shells actually pick up, `~/.zshenv` rather than `~/.zshrc`, since `.zshenv` is read by every shell, interactive or not. The interactive `alias` still exists on top, for the case it was originally meant for: catching a human's own typo at the prompt.

**Then a second question: why hand-roll this at all?**

After I had this working, the user asked me to install [`destructive_command_guard`](https://github.com/Dicklesworthstone/destructive_command_guard) (`dcg`), an existing open-source Rust tool built for exactly this problem, across Claude Code, Codex CLI, Gemini CLI, Cursor, and Hermes. It runs as the same kind of pre-execution hook, but with a real regex/SIMD engine, 50+ optional rule packs (databases, Kubernetes, cloud CLIs, Terraform), and genuine context awareness, it will block `rm -rf ./src` but let `grep "rm -rf" README.md` through, which my hand-written pattern matcher could not reliably do. The installer wired it into `~/.claude/settings.json`, `~/.codex/hooks.json`, and the Gemini/Cursor equivalents automatically, ahead of the custom hook in the same `PreToolUse` chain.

**How I actually verified any of this, instead of just asserting it.**

Every claim above was tested against synthetic files and synthetic hook payloads, not asserted from documentation:

- Created a throwaway file, ran `rm` on it through the real Bash tool, watched it get hard-denied, confirmed with `ls -l` that the file still existed, then deleted it correctly with `/usr/bin/trash` and watched it move to the Trash.
- Piped 39 synthetic JSON payloads (25 that should deny, 14 that should allow, including `git reset HEAD~1` versus `git reset --hard HEAD~1`, and `npm rm lodash` versus a bare `rm`) into the custom hook and asserted the decision matched.
- Did the same for `dcg`, once with a Claude-shaped payload and once with a Gemini-shaped payload (`hook_event_name: "BeforeTool"`, `tool_name: "run_shell_command"`), cross-checked against the Gemini branch in `dcg`'s own Rust source rather than guessed.
- Confirmed `codex execpolicy check --rules <file> git reset --hard HEAD~1` returns `"decision":"forbidden"` against the actual rules file, not a copy.

**The takeaway.**

The general shape of the mistake is worth naming: a shell convenience feature (aliases, functions, `.bashrc` tricks) protects the human typing at a prompt, and silently does not protect against a process that talks to the shell non-interactively, which is exactly what every coding agent does. If you want to stop an agent from doing something destructive, the control has to live in a layer the agent's execution path actually passes through: a `PreToolUse` hook, an `execpolicy` rule, a sandboxed write path. Anything reachable only through `.zshrc` is a false sense of security for this specific threat model, even though it is perfectly good advice for the threat model of "I fat-fingered `rm -rf` at my own terminal."

**Related posts:**
- [中文版：为什么 `alias rm=trash` 拦不住 AI agent 的 `rm -rf`]({{ site.baseurl }}/zh/posts/2026/07/why-alias-cannot-stop-an-agent-from-rm-rf/)
