---
title: "Benchmark Radar 第十五天：社交媒体流水线与微信集成"
date: 2026-08-10
permalink: /zh/posts/2026/08/benchmark-radar-day15/
tags: [benchmark-radar, social-media, wechat, pipeline, github-issues]
---


你好，我是 Koutian。第十五天，雷达第一次学会主动对外说话，不再只是等你来翻。

> 作者：[Koutian Wu](https://www.linkedin.com/in/ktwu01/)；[GitHub: ktwu01](https://github.com/ktwu01/)

**Benchmark Radar 已上线。** 每天追踪新的 AI 基准测试、数据集与排行榜：[打开仪表盘](https://benchmark-radar.org/) 或 [在 GitHub 上 Star](https://github.com/ktwu01/benchmark-radar)。

我们上线了「每日社交媒体帖文生成」模块。它会把当天的内容自动写成能直接发的帖子。你不用自己总结，它替你写好发圈文案。

微信渠道的检查清单和发布文案模板备好了。往微信发东西，有了现成的步骤和模板。你每次发，照着清单走就不会漏。

我们停用了「每日 GitHub Issue 机制」。以前雷达每天开一个 issue（issue 就是一个待办或 bug 单）来放社交素材，现在改了。社交素材不再走 issue，而是作为构建产物（build artifact，就是跑完流程产出的文件）直接分发。仓库（repo，就是放代码的地方）里清爽了，只管代码，不再被每日帖文刷屏。

合并日期的 items.json 生成好了。就是把同一天的数据归并到一个文件里。你翻历史时，一天一个文件，好找。

渠道每日标记修好了。每条内容标对了它属于哪个渠道、哪一天。你不会看到标错平台的帖子。

问答标识符的片段处理好了。带问答标记的内容，截断位置对了。你读到的问答是完整的。

README 更新了。使用说明跟上新功能。你照着文档能玩转新东西。

为什么值得你关心。

社交媒体流水线是雷达第一个对外通道。以前所有产出都躺在那儿等你来。现在它主动把内容推到微信这种平台，更多人能看见。你的关注者不用专门跑来网站，也能收到更新。

停掉每日 issue，是给仓库减负。社交素材不再塞进 issue，仓库就不天天被无关帖文刷屏。它回归本职，只管代码。你提 issue 时，看到的都是真问题，不是每日灌水。

解决的问题。

- Issue #180
- Issue #181
- Issue #182

> 想跟进 Benchmark Radar？[在 GitHub 上 Star 仓库](https://github.com/ktwu01/benchmark-radar) 获取每日更新，或 [打开实时仪表盘](https://benchmark-radar.org/) 浏览扫描结果。
