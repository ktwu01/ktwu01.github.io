---
title: 'komomood - 情侣心情追踪热力图'
date: 2025-08-16
permalink: /posts/2025/08/komomood-cn/
tags:
  - web-app
  - mood-tracking
  - heatmap
  - sqlite
  - nodejs
---

这是一个优雅的情侣心情记录网站，采用自托管后端和 SQLite，以 GitHub contribution graph 风格展示每日心情记录。

## 🌸 功能特点

- **Elegant Pink Theme**：渐变粉色设计，温暖又浪漫
- **GitHub-Style Heatmap**：使用 Cal-Heatmap 展示过去一年加 14 天的日历热力图
- **Responsive Design**：移动端和桌面端都很好看
- **Local Backend API**：前端通过 `/komomood/api/entries` 读写数据，支持同日期覆盖写入

## 📊 数据与后端

生产环境数据存储在 `backend/mood_entries.db`（SQLite），数据表为 `mood_entries`。同时也提供本地 JSON 作为开发环境回退：

```json
[
  {
    "date": "2025-01-15",
    "kokoMood": 4,
    "momoMood": 5,
    "komoScore": 4,
    "note": "Watched a movie together, very happy day"
  }
]
```

### 字段说明

- `date`：YYYY-MM-DD 格式日期
- `kokoMood`：Koko 的心情评分（1-5）
- `momoMood`：Momo 的心情评分（1-5）
- `komoScore`：关系评分（1-5）
- `note`：可选备注文本

## 🎨 配色方案

热力图使用 5 级颜色渐变（蓝 → 粉）：

- Level 0（无数据）：`#E5E7EB`（灰色）
- Level 1：`#3B82F6`（蓝色）
- Level 2：`#60A5FA`（浅蓝）
- Level 3：`#A78BFA`（紫色）
- Level 4：`#F472B6`（粉色）
- Level 5：`#EC4899`（深粉）

颜色等级由 `komoScore` 决定，用来表示当天的关系状态。

## 🚀 本地开发

由于浏览器 CORS 限制，请使用本地服务器：

```bash
# Using Python
python -m http.server 8000

# Or using Node.js
npx serve .

# Or using PHP
php -S localhost:8000
```

然后访问 `http://localhost:8000`

后端（可选）：

```bash
cd backend
npm i
node server.js # or use pm2 for hosting
```

## 📱 部署（当前生产环境）

- 静态资源：Nginx 提供 `/komomood/`（部署在 `/var/www/komomood/`）
- API 代理：`/komomood/api/` → `http://localhost:3002/api/`
- 访问地址：`https://us-south.20011112.xyz/komomood/`

## 🔧 维护说明

- 生产环境不依赖外部 CDN：Cal-Heatmap、Tailwind 等都使用本地构建/本地资源
- 数据库文件纳入版本控制（特殊使用场景）。需要注意文件体积和隐私问题
- 热力图额外 +14 天：如需调整，可修改前端 `numWeeks` 计算方式

## 💕 关于项目

这是一个为情侣设计的私密心情记录工具，用尽量简单的方式记录和回看那些美好的时刻。

---

Made with 💖 for Koko & Momo