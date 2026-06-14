---
title: '我为什么要把自己的信息流交给 AI Actions'
date: 2026-06-14
permalink: /posts/2026/06/ai-native-document-flow-cn/
tags:
  - AI
  - automation
  - workflow
  - personal-ops
  - writing
---

我今天真正想做的事情，其实是把自己从一座 mountains of 重复性的 work 里面捞出来。

> 作者：[Koutian Wu](https://www.linkedin.com/in/ktwu01/)；[GitHub: ktwu01](https://github.com/ktwu01/)

事情是这样的。刚才只是往网站里加一篇 Port Aransas South Jetty 的报道，理论上这是一件小事。加一个 post，更新 media 页面，再把首页 Featured in 那一行补上。

可是你想想看，真正的人生不是只有首页。

一个新的 work project 出现以后，它不应该只停在一个地方。它可能要进 resume，进 CV，进个人网站，进 portfolio，进 media coverage，进 future grant bio，进 project archive，甚至以后还要进某个 chronicle 或者 founder story 里面。每一个地方都在讲同一个人，但是每一个地方又都用不同格式讲这个人。

这就很烦。

更烦的是，这种烦不是一次性的。它会反复出现。今天是一个媒体报道，明天是一个新 preprint，后天是一个 talk，再后面是一个 GitHub project，或者一个实习经历，或者一个奖项。每次都要手动想一遍，这个信息应该去哪几个地方，哪几个文件要改，哪几个版本已经过期。

这就是我说的信息流。

这个 repo 表面上是一个个人网站，里面其实已经是一张信息流图。`_pages/about.md` 是首页叙事，`_pages/media.md` 是媒体证据，`_pages/cv.md` 和 `_data/cv.json` 是简历结构，`_portfolio/` 是项目，`_publications/` 是论文，`_talks/` 是报告，`chronicles/` 是更长的证据化叙事。

它们不是孤立文件。

它们是同一个人生数据库的不同出口。

以前没有 Claude Code 和 Codex 的时候，大家会用 GitHub Actions。push 以后跑测试，build 网站，deploy 到 GitHub Pages。这个很好，但它解决的是代码生命周期的问题，不解决信息生命周期的问题。

现在我想要的是 AI Actions。

不是让 Claude Code 随便发挥，而是让每一个新信息都先进入一个 single source of truth。比如一个新项目，先变成一个结构化节点。这个节点里面有名字、时间、角色、合作者、证据链接、影响、适合流向哪些文档。然后 AI Actions 根据这一个节点，把它流到该去的地方。

resume 需要一句短的 impact bullet，它就生成短的。professional dossier 需要证据链，它就把 source、date、role、impact 串起来。个人网站需要可读的叙事，它就写成 post 或 portfolio entry。media 页面只需要一行，它就只写一行。

人应该保留判断，不应该保留复制粘贴。

我翻了一眼以前的 Codex history，很多 prompt 看起来都很小。改一个 dashboard，更新一个 scratchpad，加一个 Google Drive mount，修一个 Earth Engine auth，写一个 PR，改一个 blog。单看每一句都像临时命令。

但我现在越来越觉得，prompt 不是一句话。

prompt 是一段 workflow 的压缩包。

你让我改 dashboard，其实里面包含了信息架构、用户路径、缓存规则、组件边界、不要乱动其他 section 的约束。你让我加一个 media post，其实里面包含了 source verification、Jekyll front matter、首页曝光、media page 分类、文章归档、未来 CV 和 project archive 可能要用的证据。

这些东西如果每次都靠人脑临时展开，就会把人累死。

说真的，我不是为了炫耀自动化才做这个。我是因为自己已经被这些重复性的 work 烦到了。AI 最有价值的地方，不是帮我多写几段漂亮话，而是把那些本来就应该自动流动的信息流起来。

所以我甚至觉得，root directory 里应该有一张 node graph。新信息从哪里进入，single source of truth 在哪里，resume、blog、media、portfolio、publication、talk、chronicle 分别怎么接收它。这个图一旦画出来，很多事情就不再是模糊的愿望，而是可以被 agent 执行的路线。

我现在做这件事，不是因为它看起来高级。

恰恰相反，是因为它太朴素了。

我不想每次有一个新成果，就重新打开五个文件，手动 copy，一边改一边担心漏掉某个地方。我不想在三个月以后才发现，某个 resume 版本还是旧的，某个 media 页面漏了一篇报道，某个 project archive 证据没有被收进去。

这种损耗太蠢了。

真正 AI-native 的工作方式，应该是我只声明一次事实，然后系统自动把事实送到该去的地方。需要我判断的时候再回来问我。需要我确认语气的时候再回来问我。需要我决定优先级的时候再回来问我。

剩下的，让信息自己流。

我想做的就是这个。

把我的工作、文档、证据、prompt、session log 全部慢慢接成一张图。不是为了做一个好看的 dashboard，而是为了让我的人生履历不再靠手动搬运维持。

坦率的讲，这可能就是我现在最想要的 AI。

一个能把我从 mountains of 重复性的 work 里救出来的 AI。
