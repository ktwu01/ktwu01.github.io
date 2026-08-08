---
title: 'Why Your Brand-New WD Drive Is Read-Only on a Mac (It''s Not the Drive)'
date: 2026-07-02
permalink: /posts/2026/07/ntfs-drive-read-only-on-mac/
tags:
  - macos
  - windows
  - filesystems
  - hardware
  - troubleshooting
---

I plugged a Western Digital external drive full of data into a MacBook Air, tried to copy a file onto it, and nothing happened. No error dialog, no progress bar, just a drive that would let me read everything and write nothing. My first instinct was that something was broken, or that I needed to fix permissions. Both were wrong, and chasing the wrong explanation almost led me to permanently downgrade the security of the whole laptop.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

**The drive is fine. Even the newest, most expensive drive would do exactly the same thing.**

This is the part that surprised me and is worth saying plainly: cross-platform read/write has nothing to do with the drive hardware. A hard drive is just a box of storage. What decides whether both macOS and Windows can write to it is the *filesystem* it was formatted with, which is a software decision made at format time, not a capability baked into the metal. There is no "state-of-the-art" drive that fixes this, because there is nothing on the drive to fix. Buy the fanciest WD, SanDisk, or Samsung enclosure you want; if it ships formatted as NTFS, it will be read-only on your Mac out of the box, same as a ten-dollar thumb drive.

**NTFS is a Microsoft format, and Apple only licenses the reading half.**

Most external drives, including nearly all of WD's, ship pre-formatted as NTFS because Windows is the larger market and NTFS is Windows' native format. macOS can *read* NTFS perfectly well. It just won't *write* to it, on purpose. Microsoft owns NTFS and doesn't license a supported write driver to Apple, so Apple ships read-only support and stops there. This is why `chmod` and the permissions tab do nothing: it isn't a permissions problem or a bug, it's a missing driver at the operating-system level. The write is refused before "who's allowed to do this" is ever a question.

**The rabbit hole: getting NTFS write on a Mac means loading a kernel extension.**

The free route people reach for is macFUSE plus ntfs-3g, installed via Homebrew. It works, but on an Apple Silicon Mac (mine is an M4) macFUSE is a *kernel extension*, and Apple Silicon refuses to load third-party kernel extensions unless you boot into Recovery and switch the machine to Reduced Security in the Startup Security Utility. Read that again: to write to one USB drive, you are asked to permanently lower the boot-time security of the entire laptop. That is a genuine tradeoff, not a checkbox, and it's a lot of ceremony for what should be a simple file copy. Paragon NTFS for Mac (paid, ~$20) is more polished, but on Apple Silicon it still wants you to approve a system extension and reboot, so it doesn't really escape the same fundamental step.

**The better fixes don't touch the Mac's security at all.**

Once you understand that this is a format problem, the good options get obvious. If the drive is already mounted read/write somewhere else, for example on the Windows PC it came from, just do the writing there; Windows handles NTFS natively and no Mac driver is involved. If you need ongoing access from the Mac, share the drive from the Windows machine over the network (SMB) and let Windows do the NTFS writes while the Mac just does normal network file operations. Neither of these downgrades anything.

**The real long-term fix is to reformat to exFAT, the format that exists precisely for this.**

exFAT is read/write natively on *both* macOS and Windows, no drivers, no Recovery mode, no reboots. It's not an accident that it works everywhere: Microsoft created exFAT and both companies support it specifically so drives can move between the two systems. If I had reformatted the drive to exFAT the day I bought it, none of the above would have happened. The catch is that reformatting erases the drive, so the move is: copy the data off to another disk or the Windows PC, reformat to exFAT, copy it back. After that it simply works on both, forever. One thing I would *not* do is the old `/etc/fstab` trick that force-enables Apple's built-in NTFS write, because that write path is experimental and has a real reputation for corrupting data, which is the last thing you want on a full drive.

None of this is exotic knowledge, but it's the kind of thing that's invisible until it bites you, and when it does, the obvious-looking fix (install a driver, approve the extension, reboot) is exactly the wrong direction. The drive was never the problem. The format was, and the format is the one thing you actually get to choose.

**Related posts:**
- [中文版：为什么你崭新的 WD 移动硬盘在 Mac 上只能读不能写（问题不在硬盘）]({{ site.baseurl }}/zh/posts/2026/07/ntfs-drive-read-only-on-mac/)
