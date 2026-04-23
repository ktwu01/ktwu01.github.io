---
title: '我们在倒腾一个AI时代的亚历山大图书馆，顺便想冲一下Nature'
date: 2026-04-22
permalink: /zh/posts/2026/04/research-skills-nature-call/
tags:
  - AI
  - Research
  - Claude
  - Open Source
---

只要你在用AI辅助科研，敲一行命令就能把你脑子里的「隐性经验」变成能发Nature的资本。
> 作者：[Koutian Wu](https://www.linkedin.com/in/ktwu01/)；[GitHub: ktwu01](https://github.com/ktwu01/)

这两天我们在搞一个挺离谱，但也挺牛逼的事。

说实话，每次看大家发 paper，我总觉得最精华的东西其实都不在 paper 里。那些怎么调参、怎么避坑的直觉，怎么跟导师周旋的经验，随着你毕业或换方向，可能就彻底失传了，想想其实挺可惜的。

所以我们在倒腾一个叫 ResearchSkills 的开源共建项目，其实就是一个 AGI 时代的「亚历山大图书馆」。

简单来说，我们想把你大脑里那些宝贵的科研技能提取出来，变成像 Claude Code 或者 Codex 这些 AI Agent 能直接读取和复用的格式。

这玩意听起来可能有点玄乎，但我们做了一个完全本地化的提取工具。如果你平时也在用 Claude Code 写代码搞研究，直接敲一行命令，它就能自动扫描并总结你的科研规则和未公开的技巧。

这块需要注意一下，全程都在本地跑，必须你自己点确认才会上传，完全不用担心隐私泄露。

比较骚的是，我们准备把这个史上最大规模的学术合作项目，直接去冲一下 Nature。

只要你提交了平时积攒的科研技能，就有机会直接变成合著者。而且你懂的，交得多、质量好，名字在作者列表里的排位就越靠前。

不仅是为了发文章，提取出来的这些技能会优先在你的本地生效。也就是说，你的 Claude 会立刻掌握你这个领域的独家绝活，越用越顺手。

我自己这几天也一直在跑提取。搞科研的朋友们，反正都是平时敲代码顺手的事，花两分钟试一下，没准就混上一篇 Nature 了。

安装和使用都极其简单，你在终端跑一句，
npm install -g @scienceintelligence/researchskills-extract

然后在你的 Claude Code 里敲 /researchskills-extract 就行了。如果你是 Codex 用户，带权限启动后敲 $researchskills-extract。

习惯用网页版的朋友，也可以直接去官网 researchskills.ai/submit-manually 手动提。

搞科研本来就挺苦的，不如把这些带不走的经验存下来，变成未来 AI 科学家的思维基石。

以上，既然看到这里了，如果觉得不错，随手点个赞、在看、转发三连吧，如果想第一时间收到推送，也可以给我们点个关注⭐～

谢谢你看我的文章，我们，下次再见。
