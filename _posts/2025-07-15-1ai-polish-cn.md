---
title: '1AI-polish - AI 学术写作润色系统'
date: 2025-07-15
permalink: /posts/2025/07/1ai-polish-cn/
tags:
  - ai
  - academic-writing
  - deepseek
  - fastapi
  - nlp
---
学术写作的严谨性不仅在于数据，更在于表达的精准，而 1AI-polish 通过集成 DeepSeek-R1 的推理能力，为研究者提供了一套集文本润色与 AI 检测于一体的深度协作系统，旨在让复杂的科研思想以更专业、更透明的方式呈现。

> 作者：[Koutian Wu](https://www.linkedin.com/in/ktwu01/)；[GitHub: ktwu01](https://github.com/ktwu01/)

## 核心功能

- **多风格文本润色**：支持 academic、formal、casual、creative 等写作风格
- **AI Detection**：分析文本由 AI 生成的概率
- **Thinking Process Display**：展示 DeepSeek-R1 的推理过程
- **Hybrid Deployment**：GitHub Pages 前端 + 本地 FastAPI 后端
- **Complete API**：提供带 Swagger 文档的 RESTful API

## 技术栈

- **Backend**：FastAPI, Python 3.9+
- **AI Model**：DeepSeek-R1 via Volcano Engine API
- **Frontend**：HTML/CSS/JavaScript
- **Deployment**：GitHub Pages + Local Server

## 快速开始

### 后端部署

```bash
# Clone repository
git clone https://github.com/ktwu01/1AI-polish.git
cd 1AI-polish

# Create virtual environment
python -m venv fastapi_env
source fastapi_env/bin/activate

# Install dependencies
pip install -r requirements.txt

# Configure API key
echo "ARK_API_KEY=your-api-key-here" > .env

# Start server
uvicorn app.main_production:app --reload --host 0.0.0.0 --port 8000
```

### 访问前端

- **Online**: https://ktwu01.github.io/1AI-polish/
- **Local**: 在浏览器中打开 `docs/index.html`

## API 接口

### 文本润色
```bash
POST /api/v1/process
{
  "content": "Your text here",
  "style": "academic"
}
```

### AI 检测
```bash
POST /api/v1/detect
{
  "content": "Text to analyze"
}
```

### 支持的风格

| Style | Description | Use Case |
|-------|-------------|----------|
| `academic` | 专业、严谨 | 论文、学术写作 |
| `formal` | 正式、庄重 | 商务文档、正式场合 |
| `casual` | 简洁、清晰 | 科普、一般阅读 |
| `creative` | 新颖、有趣 | 创意写作、营销文案 |

## 架构

**Hybrid Deployment**：
- 前端托管在 GitHub Pages（免费、快速）
- 后端本地运行（保护 API key 安全）
- 前端自动连接本地 API

## 项目结构

```
1AI-polish/
├── app/                    # 后端应用
│   ├── api/v1/            # API routes
│   ├── services/          # 业务逻辑
│   └── models/            # 数据模型
├── docs/                  # 前端文件
├── tests/                 # 测试文件
└── requirements.txt       # 依赖
```

## 性能

- 处理时间：10-30 秒（DeepSeek-R1）
- 支持批量处理
- 实时 AI 概率检测

## 链接

- **Live Demo**: https://ktwu01.github.io/1AI-polish/
- **GitHub**: https://github.com/ktwu01/1AI-polish
- **API Docs**: http://localhost:8000/docs （运行后可访问）

---

*为学术写作者而做，带着 💖*
