---
title: 'earth-space-ai.org：面向地球与空间系统模型的渐进式披露技能包'
date: 2026-05-27
permalink: /zh/posts/2026/05/earth-space-ai-org-skill-packages/
tags:
  - earth-system-models
  - ai-agents
  - skill-packages
  - climate-modeling
  - heliophysics
  - open-science
---

数十年来积累的地球系统建模判断散落在 PDF、邮件列表和资深研究者的头脑里，AI 编程智能体无法直接加载这些知识。earth-space-ai.org 试图解决这个问题。

> 作者：[Koutian Wu](https://www.linkedin.com/in/ktwu01/)；[GitHub: ktwu01](https://github.com/ktwu01/)
>
> 项目主页：[earth-space-ai.org](https://github.com/earth-space-ai) · 主页仓库：[earth-modeling-agent-homepage](https://github.com/ktwu01/earth-modeling-agent-homepage)

## 这是什么

机理型地球系统模型，包括 CESM、E3SM、WRF、MOM6、Noah-MP、CTSM、JULES 及其他同类模型，在源代码树、构建系统和口耳相传的调试经验中承载了数十年的科学判断。这些知识大多存在于 PDF、邮件列表、AGU 海报和资深研究者的头脑里。AI 编程智能体无法直接加载它们。

[earth-space-ai.org](https://github.com/earth-space-ai) 试图解决这个问题。这个 GitHub 组织为地球、行星和空间系统模型托管经过整理、采用渐进式披露方式的**技能包**。每个仓库都采用以下设计：

- 可由 AI 编程智能体加载，包括 Claude Code、Codex、Cursor、Aider、Cline 和 LingTai；
- 可供研究者和开发者作为长期参考资料阅读；
- 与其对应的上游模型同步维护；
- 清楚处理许可证与署名，避免损害上游社区。

组织简介用一句话概括了目标：

> 借助人工智能，让地球与空间科学建模更加普及。

## 技能包的结构

技能包不是教程，而是具有固定结构的知识包：

```
<model>-skill/
├── SKILL.md       ← routing hub (read first)
├── README.md      ← human-facing front matter, disclaimer, install
└── reference/     ← deep-dive docs loaded on demand
    ├── getting-started.md
    ├── architecture.md
    ├── running-single-point.md
    ├── running-2d-domain.md
    ├── custom-output.md
    ├── contributing-pr.md
    └── debugging.md
```

`SKILL.md` 是路由中心，包含决策树、仓库结构、快速入门和必须遵守的规则。智能体一开始只需读取这一个文件。随后，它只加载当前步骤所需的 `reference/*.md` 页面。

在实际使用中，智能体把索引保留在上下文中，每次只按需读取一个章节。这套结构借鉴了 [laps-skill](https://github.com/huangzesen/laps-skill) 和 xhelio 系列项目，最初在日球物理领域得到验证。

## 当前版图：8 个领域，约 30 个技能

这些技能仓库按科学领域分组。截至本文发布时，该组织及合作仓库列出了八组、约三十个技能。主页仓库中的 [`lib/skills.ts`](https://github.com/ktwu01/earth-modeling-agent-homepage/blob/main/lib/skills.ts) 是这份列表的单一事实来源。

**01 · 地球系统与耦合模型。** [cam-skill](https://github.com/earth-space-ai/cam-skill)（Community Atmosphere Model）、[cesm-skill](https://github.com/earth-space-ai/cesm-skill)（CESM superproject）、[e3sm-skill](https://github.com/earth-space-ai/e3sm-skill)（Energy Exascale Earth System Model）、[noresm-skill](https://github.com/earth-space-ai/noresm-skill)、[fms-skill](https://github.com/earth-space-ai/fms-skill)（GFDL Flexible Modeling System），以及 Tian Zhou 和合作者的 [ESFlow 预印本](https://egusphere.copernicus.org/preprints/2026/egusphere-2026-2237/)与 [Zenodo 记录](https://zenodo.org/records/19350842)。

**02 · 大气。** [wrf-skill](https://github.com/earth-space-ai/wrf-skill)、[waccm-skill](https://github.com/earth-space-ai/waccm-skill)、[waccmx-skill](https://github.com/earth-space-ai/waccmx-skill)、[gfdl-fv3-skill](https://github.com/earth-space-ai/gfdl-fv3-skill)、[openifs-skill](https://github.com/earth-space-ai/openifs-skill)、[regcm-skill](https://github.com/earth-space-ai/regcm-skill)、[geos-chem-skill](https://github.com/earth-space-ai/geos-chem-skill)。

**03 · 陆面与水文。** [noahmp-skill](https://github.com/earth-space-ai/noahmp-skill)（Noah-MP + HRLDAS）、[ctsm-skill](https://github.com/earth-space-ai/ctsm-skill)（CTSM / CLM）、[jules-skill](https://github.com/earth-space-ai/jules-skill)、[summa-skill](https://github.com/earth-space-ai/summa-skill)、[vic-skill](https://github.com/earth-space-ai/vic-skill)、[parflow-skill](https://github.com/earth-space-ai/parflow-skill)。

**04 · 海洋。** [mom6-skill](https://github.com/earth-space-ai/mom6-skill)、[mitgcm-skill](https://github.com/earth-space-ai/mitgcm-skill)、[fesom2-skill](https://github.com/earth-space-ai/fesom2-skill)、[roms-skill](https://github.com/earth-space-ai/roms-skill)。

**05 · 海冰。** [cice-skill](https://github.com/earth-space-ai/cice-skill)。

**06 · 固体地球与有限断层。** [wasp-finitefault-skill](https://github.com/liuwei1997/wasp-finitefault-skill)，由 UCLA 的 Liuwei Xu 维护。

**07 · 日球物理与空间物理模型。** [laps-skill](https://github.com/huangzesen/laps-skill)（LAPS，即 UCLA 的伪谱三维 Hall-MHD 代码）、上游 [LAPS](https://github.com/chenshihelio/LAPS) 仓库，以及 [lingtai-batsrus-skill](https://github.com/huangzesen/lingtai-batsrus-skill)（BATS-R-US，即 SWMF 核心的 MHD 求解器），均由 Zesen Huang 维护。

**08 · 日球物理观测与数据访问。** [xhelio-cdaweb](https://github.com/huangzesen/xhelio-cdaweb)（NASA CDAWeb）、[xhelio-spice](https://github.com/huangzesen/xhelio-spice)（SPICE toolkit）、[xhelio-pds](https://github.com/huangzesen/xhelio-pds)（NASA PDS），由 Zesen Huang 维护。

技能被标记为 `complete` 或 `scaffold`。`scaffold` 已具备基本结构和路由中心，但内容仍在补充；`complete` 表示智能体至少已经用它完成过一次标准运行的端到端流程。

## 一个技能的结构：Noah-MP

[noahmp-skill](https://github.com/earth-space-ai/noahmp-skill) 是陆面类别中标记为 `complete` 的项目。下面以它为例说明此类技能的结构。

它同时面向两个对象：重构后的 Version 5 模块化 Fortran 代码库 [NCAR/noahmp](https://github.com/NCAR/noahmp)，以及离线驱动 [HRLDAS](https://github.com/NCAR/hrldas)。这个技能指导智能体安装、编译、运行、修改和调试模型，并向上游贡献代码。它的 `reference/` 目录包含多个专门章节，分别讲解如何把信息不完整的用户需求设计成可运行的模拟（例如“Texas 土壤湿度、12.5 km、在 TACC 上运行”）、如何运行 Bondville 单点模拟、如何运行 CONUS 二维 NLDAS-2 模拟、如何沿完整 IO 链添加新的输出变量，以及如何向上游提交能正确处理子模块的 pull request。

`noahmp-skill` 中有两项可以推广到整个组织的设计：

1. **技能不取代上游教程，而是为其提供机器可读的封装。** Cenlin He 编写的 [NCAR/hrldas 教程 notebooks](https://github.com/NCAR/hrldas/tree/master/tutorial) 是标准参考。技能的 README 明确写道：“如果本技能中的检查点、namelist 值或物理选项与 NCAR 教程冲突，以 NCAR 教程为准。”技能增加了面向 AI 的执行方式、机器可读的验证脚本、针对 TACC 的依赖探测，以及用于视觉验证的参考图。它不会把自己的优先级置于专家之上。
2. **验证是技能本身的一部分，不依赖用户盲目信任。** 每次运行后，智能体都必须调用 `examples/check_run_outputs.sh` 来发现无声失败，例如只有文件头的 `LDASOUT`、`START_DATE` 漂移、全零的潜热字段和缺失的自定义变量。对于 Bondville 单点运行，仓库还提供参考图 `bondville_LH_ncview.png`，便于将智能体输出与已知正确的结果进行目视比较。

技能开头的免责声明也承担实际作用：“AI 可能出错（路径错误、行号漂移、namelist 字段过期、臆造的选项）。采取行动前，务必对照上游 `NCAR/noahmp`、`NCAR/hrldas` 和技术说明进行核查。”一个声称自己绝不会出错的技能包，比一个明确说明自身可能在哪里出错的技能包更不可靠。

## 主页

该组织有一个[主页](https://github.com/ktwu01/earth-modeling-agent-homepage)，它是适合静态部署的 Next.js 15 网站，使用 App Router、React 18 和 TypeScript，没有后端。这个单页锚点式网站承担三项任务：

1. **按领域列出所有技能仓库**，为每个仓库提供一句简介和上游仓库链接。`lib/skills.ts` 是单一事实来源，主页、导航栏和页脚都由这个文件生成。新增技能只需改一行。
2. **解释技能包结构**，也就是 `SKILL.md` 与 `reference/` 的组合，让新贡献者在提出新仓库之前先理解统一结构。
3. **展示参与者。** `/teams` 页面列出 Scientific Committee，其中包括 BU 的 Chuanfei Dong，以及 UCLA 的 Vassilis Angelopoulos、Jacob Bortnik 和 Marco Velli 等 faculty PI；Executive Committee 包括 UCLA 的 Zesen Huang 和 UT Austin 的 Koutian Wu；Scholars 则来自 UCLA、Caltech、UMich、Oxford、Meta、ETH Zürich 和 UIUC。组织以贡献为依据，而非单位隶属关系。

网站从 `main` 分支部署到 Vercel。它没有后端、数据库、身份验证或环境变量。仓库有意保持简单，让贡献新技能所需的操作只剩下编辑一个 TypeScript 数组。

## 为什么采用这种结构

渐进式披露用于应对三项实际约束：

- **上下文窗口有限。** 即使模型支持百万 token，上下文若在每一轮都载入 CESM 的全部文档，大多数 token 也会被无关内容占用。路由中心与按需加载的章节让每一轮只围绕智能体当下需要的页面展开。
- **PDF 无法可靠传承流程性知识。** “先推送 noahmp 子模块，再推送 hrldas superproject”这类规则往往只存在于一位资深研究者的头脑中，直到外部贡献者的 pull request 在凌晨 2 点破坏构建，才会出现在一条 Slack 消息里。技能包把这种规则编码为机器可检查的阶段块，而不是放进无人阅读的 PDF 段落。
- **上游维护者希望教程得到引用，许可证受到尊重。** 该组织的每个技能包都保留上游许可证，并列出维护者，包括 Noah-MP 的 Cenlin He、HRLDAS 的 NCAR 团队、LingTai LAPS 与 BATS-R-US 封装的 Zesen Huang，以及 WASP 的 Liuwei Xu。每个技能包还明确说明，内容有分歧时以上游教程为准。技能是封装，不是 fork。

## 如何使用技能

如果你是智能体操作者，也就是使用 Claude Code、Codex 或 Cursor 的研究者，可以按以下步骤操作：

1. 将技能仓库克隆到你的技能库中，然后刷新。
2. 用一句话向智能体说明需求。例如：“从全新登录环境开始，在 TACC ls6 上配置 Noah-MP，直到构建出 `hrldas.exe`。”“规划一次 Texas 12.5 km NLDAS-2 运行。”“把 `BTRANXY` 加入 LDASOUT。”
3. 让智能体读取 `SKILL.md`，沿决策树执行，加载正确的 `reference/*.md`，遵守 USER GATE 标记，并完成任务。USER GATE 是智能体应当暂停并向你提问的唯一位置。
4. 每次运行结束后，先让智能体执行验证脚本，再宣布成功。跳过验证可能让静默失败留到后续环节才被发现。

如果你是希望自己的模型被该组织收录的模型开发者，流程相反：在 [earth-space-ai](https://github.com/earth-space-ai) 提交 issue，说明模型以及你与上游维护者的关系，并提出维护者人选。如果尚未告知上游社区，我们不会添加第三方技能封装。

## 接下来

按照目前的设想，2026 年路线图有三条主线：

1. **完善 scaffolds。** 大部分大气和海洋条目，包括 CESM、MITgcm、FESOM2、ROMS、OpenIFS、RegCM、WACCM、WACCM-X、GEOS-Chem、GFDL FV3、FMS 和 NorESM，目前仍是 scaffold。每个项目都需要完成第一次标准运行，建立验证工具，并由真正运行该模型的人担任维护者。
2. **开展跨模型评估。** 一个技能包负责教智能体驱动一个模型。更难的问题在于，智能体能否跨模型推理，例如回答必须同时使用 Noah-MP 与 MOM6 的问题，或发现 CAM 与 CTSM 之间的耦合不一致。[ESM-bench](https://koutian.is-a.dev/posts/2026/04/esm-bench-ai-agents-earth-system-models/) 和 ESFlow 预印本将在这里发挥作用。
3. **明确贡献路径。** 组织层级的 `CONTRIBUTING.md`、模板技能仓库和轻量审核流程，可以避免上游维护者突然发现别人已为自己的模型制作了第三方封装。

## 结语

earth-space-ai.org 背后的判断具体而有限：AI 辅助地球与空间科学建模的瓶颈，在于缺少结构化、可加载、机器可读的流程性知识，而这个领域实际依赖的十多个旧式 Fortran 代码库正需要这类知识。如果判断成立，技能包可以补充 benchmark 和论文通常没有记录的操作流程；即使判断不成立，整理后的 README 仍可供维护者和用户参考。

无论如何，可以从[组织页面](https://github.com/earth-space-ai)开始了解项目。贡献入口是在 [`lib/skills.ts`](https://github.com/ktwu01/earth-modeling-agent-homepage/blob/main/lib/skills.ts) 中做一次修改，并新建一个名为 `<model>-skill` 的仓库。

## 资源

- 组织：https://github.com/earth-space-ai
- 主页源码：https://github.com/ktwu01/earth-modeling-agent-homepage
- 参考技能（Noah-MP）：https://github.com/earth-space-ai/noahmp-skill
- 结构先例（日球物理）：https://github.com/huangzesen/laps-skill
- ESFlow 预印本（Tian Zhou et al., 2026）：https://egusphere.copernicus.org/preprints/2026/egusphere-2026-2237/
- ESFlow Zenodo 记录：https://zenodo.org/records/19350842
- NCAR Noah-MP：https://github.com/NCAR/noahmp
- NCAR HRLDAS 教程 notebooks：https://github.com/NCAR/hrldas/tree/master/tutorial
