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

# 只要你在用AI辅助科研，敲一行命令就能把你脑子里的「隐性经验」变成能发Nature的资本

这两天我们在搞一个挺离谱，但也挺牛逼的事。

说实话，每次看大家发 paper，我总觉得最精华的东西其实都不在 paper 里。那些怎么调参、怎么避坑的直觉，怎么跟导师周旋的经验，随着你毕业或换方向，可能就彻底失传了，想想其实挺可惜的。

所以我们在倒腾一个叫 ResearchSkills.ai的开源共建项目，其实就是一个 AGI 时代的「亚历山大图书馆」。

简单来说，我们把你大脑里那些宝贵的科研技能提取出来，变成像 Claude Code 或者 Codex 这些 AI Agent 能直接读取和复用的格式。

这件事情意义重大，我们计划把这个开源学术合作项目，直接投给 *Nature*，并且成立非盈利组织来持续运营，有望成为史上最大规模的科研合作项目。

这玩意听起来可能有点玄乎，但我们做了一个完全本地化的提取工具。如果你平时也在用 Claude Code 写代码搞研究，直接敲2行命令，它就能自动扫描并总结你的科研规则和未公开的技巧。

这块需要注意一下，全程都在本地跑，必须你自己点确认才会上传，完全不用担心隐私泄露。

1. 只要你贡献科研技能，就有机会成为合著者！而且，提交 Skill 数量越多、质量越高的研究者，在作者列表中的排名就会越靠前。
2. 提取的技能会优先本地生效。你的 Claude / Cursor 会立刻掌握你这个领域的独家科研绝活，越用越顺手。

我自己这几天也一直在跑提取。搞科研的朋友们，反正都是平时敲代码顺手的事，花两分钟试一下，没准就混上一篇 
*Nature* 了。

安装和使用只需几分钟，不用手敲，可以在我们的官网
researchskills.ai复制下面的这些指令：
`npm install -g @scienceintelligence/researchskills-extract` 就可以安装这个skill（只需30秒）。

然后在你的 Claude Code 里敲 `/researchskills-extract` （只需10秒）。如果你是 Codex 用户，带权限启动后敲 
`$researchskills-extract`。

习惯用网页版ChatGPT/Gemini/Claude 的朋友，也可以直接去我们的官网
researchskills.ai/submit-manually 按照我们给的提示流程来提交（大概只需5分钟）。

搞科研本来就挺苦的，不如把这些带不走的经验存下来，变成未来 AI 科学家的思维基石。

以上，既然看到这里了，如果觉得不错，就开始行动吧。

谢谢你看我的文章，我们，下次再见。
