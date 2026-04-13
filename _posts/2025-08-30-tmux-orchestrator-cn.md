---
title: 'Tmux Orchestrator - 让 AI agents 7×24 小时持续工作'
date: 2025-08-30
permalink: /posts/2025/08/tmux-orchestrator-cn/
tags:
  - ai
  - agents
  - tmux
  - automation
---
Tmux Orchestrator 让 Claude agents 能够自主工作、自己安排 check-in，并在多个项目之间协同推进——这是一个我探索过、也从中学到很多的项目。

> 作者：[Koutian Wu](https://www.linkedin.com/in/ktwu01/)；[GitHub: ktwu01](https://github.com/ktwu01/)

## 🤖 核心能力与自治特性

- **Self-trigger** - Agent 可以自己安排后续 check-in，并持续自主推进工作
- **Coordinate** - 项目经理可以跨多个代码库给工程师分发任务  
- **Persist** - 即使你合上电脑，工作也能继续进行
- **Scale** - 可以同时运行多个团队，并行处理不同项目

## 🏗️ 架构

Tmux Orchestrator 使用三层层级结构来突破 context window 限制：

```
┌─────────────┐
│Orchestrator │  你在这里交互
└──────┬──────┘
       │ 监控并协调
       │
┌─────────────┐    ┌─────────────┐
│ Project     │    │ Project     │
│ Manager 1   │    │ Manager 2   │  分配任务、约束规范
└──────┬──────┘    └──────┬──────┘
       │                  │
       │                  │
┌─────────────┐    ┌─────────────┐
│Engineer 1   │    │Engineer 2   │  写代码、修 bug
└─────────────┘    └─────────────┘
```

### 为什么要拆分多个 Agent？
- **上下文窗口有限** - 每个 agent 只专注自己的角色
- **专业分工明确** - PM 管理，工程师编码
- **并行工作** - 多个工程师可以同时推进
- **更好的记忆效果** - 更小的上下文通常意味着更好的召回与稳定性

## 📸 使用示例

### 项目经理协调
![Initiate Project Manager](/images/tmux-orchestrator/Examples/Initiate%20Project%20Manager.png)
*Orchestrator 创建并 brief 一个新的项目经理 agent*

### 状态汇报与监控
![Status Reports](/images/tmux-orchestrator/Examples/Status%20reports.png)
*多个 agent 并行工作时的实时状态更新*

### Tmux 通信
![Reading TMUX Windows and Sending Messages](/images/tmux-orchestrator/Examples/Reading%20TMUX%20Windows%20and%20Sending%20Messages.png)
*Agent 如何在 tmux 窗口和 session 之间通信*

### 项目完成
![Project Completed](/images/tmux-orchestrator/Examples/Project%20Completed.png)
*所有任务完成、验证并提交后的成功示例*

使用本仓库前，建议先安装 Tmux： https://github.com/tmux/tmux/wiki/Installing

## 🎯 快速开始

### 方案 1：基础配置（单项目）

```bash
# 1. Create a project spec
cat > project_spec.md << 'EOF'
PROJECT: My Web App
GOAL: Add user authentication system
CONSTRAINTS:
- Use existing database schema
- Follow current code patterns  
- Commit every 30 minutes
- Write tests for new features

DELIVERABLES:
1. Login/logout endpoints
2. User session management
3. Protected route middleware
EOF

# 2. Start tmux session
tmux new-session -s my-project

# 3. Start project manager in window 0
claude

# 4. Give PM the spec and let it create an engineer
"You are a Project Manager. Read project_spec.md and create an engineer 
in window 1 to implement it. Schedule check-ins every 30 minutes."

# 5. Schedule orchestrator check-in
./schedule_with_note.sh 30 "Check PM progress on auth system"
```

### 方案 2：完整 Orchestrator 配置

```bash
# Start the orchestrator
tmux new-session -s orchestrator
claude

# Give it your projects
"You are the Orchestrator. Set up project managers for:
1. Frontend (React app) - Add dashboard charts
2. Backend (FastAPI) - Optimize database queries
Schedule yourself to check in every hour."
```

## 关键特性

### 🔄 可自我调度的 Agent
Agent 可以通过以下命令自己安排后续 check-in：
```bash
./schedule_with_note.sh 30 "Continue dashboard implementation"
```

### 👥 多 Agent 协同
- 项目经理与工程师沟通
- Orchestrator 监控所有项目经理
- 支持跨项目知识共享

### 💾 自动 Git 备份
- 每工作 30 分钟自动 commit
- 为稳定版本打 tag
- 为实验性工作创建 feature branch

### 📊 实时监控
- 可以看到每个 agent 在做什么
- 需要时可随时介入
- 可统一回顾多个项目的进展

## 📋 最佳实践

### 如何写更有效的规格说明

```markdown
PROJECT: E-commerce Checkout
GOAL: Implement multi-step checkout process

CONSTRAINTS:
- Use existing cart state management
- Follow current design system
- Maximum 3 API endpoints
- Commit after each step completion

DELIVERABLES:
1. Shipping address form with validation
2. Payment method selection (Stripe integration)
3. Order review and confirmation page
4. Success/failure handling

SUCCESS CRITERIA:
- All forms validate properly
- Payment processes without errors  
- Order data persists to database
- Emails send on completion
```

### Git 安全规则

1. **开始任务之前**
   ```bash
   git checkout -b feature/[task-name]
   git status  # Ensure clean state
   ```

2. **每 30 分钟**
   ```bash
   git add -A
   git commit -m "Progress: [what was accomplished]"
   ```

3. **任务完成时**
   ```bash
   git tag stable-[feature]-[date]
   git checkout main
   git merge feature/[task-name]
   ```

## 🚨 常见坑与解决方案

| Pitfall | Consequence | Solution |
|---------|-------------|----------|
| 模糊指令 | Agent 漂移、浪费算力 | 写清晰具体的 spec |
| 不做 git commits | 工作丢失、开发者崩溃 | 强制执行 30 分钟 commit 规则 |
| 一次塞太多任务 | 上下文过载、容易混乱 | 一个 agent 一次只做一个任务 |
| 没有书面规格 | 结果不可预测 | 永远从 written spec 开始 |
| 缺少 checkpoint | Agent 停止推进 | 安排定期 check-in |

## 🛠️ 工作原理

### Tmux 的关键作用
Tmux（terminal multiplexer）之所以是关键，是因为它：
- 即使断开连接也能保留终端 session
- 允许一个 session 内有多个窗口/面板
- Claude 运行在终端里，因此可以控制其他 Claude 实例
- 命令可以被程序化地发往任意窗口

### 💬 更简化的 Agent 通信

现在我们统一使用 `send-claude-message.sh` 脚本进行 agent 通信：

```bash
# Send message to any Claude agent
./send-claude-message.sh session:window "Your message here"

# Examples:
./send-claude-message.sh frontend:0 "What's your progress on the login form?"
./send-claude-message.sh backend:1 "The API endpoint /api/users is returning 404"
./send-claude-message.sh project-manager:0 "Please coordinate with the QA team"
```

这个脚本会自动处理时序细节，使 agent 通信更稳定、更一致。

### 安排 Check-ins
```bash
# Schedule with specific, actionable notes
./schedule_with_note.sh 30 "Review auth implementation, assign next task"
./schedule_with_note.sh 60 "Check test coverage, merge if passing"
./schedule_with_note.sh 120 "Full system check, rotate tasks if needed"
```

**重要提示**：Orchestrator 需要知道自己运行在哪个 tmux 窗口中，才能正确为自己安排 check-in。如果调度失效，请确认它能正确识别当前窗口：
```bash
echo "Current window: $(tmux display-message -p "#{session_name}:#{window_index}")"
```

## 🎓 高级用法

### 多项目编排
```bash
# Start orchestrator
tmux new-session -s orchestrator

# Create project managers for each project
tmux new-window -n frontend-pm
tmux new-window -n backend-pm  
tmux new-window -n mobile-pm

# Each PM manages their own engineers
# Orchestrator coordinates between PMs
```

### 跨项目协同 intelligence
Orchestrator 可以在不同项目之间共享洞见：
- “Frontend 已经在使用 /api/v2/users，请同步更新 backend”
- “Project A 的鉴权方案已经跑通，可以在 Project B 复用同样模式”
- “共享库中发现性能问题，请在所有项目里统一修复”

## 📚 核心文件

- `send-claude-message.sh` - 简化的 agent 通信脚本
- `schedule_with_note.sh` - 自我调度功能
- `tmux_utils.py` - Tmux 交互工具
- `CLAUDE.md` - Agent 行为说明
- `LEARNINGS.md` - 累积的经验库

## 🤝 贡献与优化

Orchestrator 会随着社区的新发现和优化不断演进。参与贡献时：

1. 将新的 tmux 命令与模式记录到 CLAUDE.md
2. 分享新的使用场景与 agent 协调策略
3. 提交对 Claude 同步机制的优化
4. 保持命令参考文档与最新发现同步
5. 在多个 session 中测试改进效果

重点优化方向：
- Agent 通信模式
- 跨项目协作
- 新型自动化工作流

## 📄 License

MIT License - 可以自由使用，但请理性使用。记住：强大的自动化，也意味着更大的责任。

---

*"The tools we build today will program themselves tomorrow"* - Alan Kay, 1971
