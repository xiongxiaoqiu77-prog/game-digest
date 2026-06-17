---
name: game-digest
description: 游戏行业日报 — 每天自动聚合微信公众号、海外媒体、播客、Google News 的游戏行业内容，用 AI 评分筛选后推送。使用时拉取中心化 feed，无需任何 API key。当用户说"看游戏日报"、"今天有什么游戏资讯"、"拉取游戏日报"或执行 /game-digest 时使用。
---

# 游戏行业日报 Game Digest

每天聚合游戏行业内容，AI 评分筛选，覆盖：

- 75 个微信公众号（游戏分析、出海、买量、产品拆解）
- 海外游戏媒体 RSS（Deconstructor of Fun、Naavik、GameLook 等）
- 小宇宙播客
- Google News + 关键词搜索

## 使用方式

### 拉取今日日报

```bash
curl -s https://raw.githubusercontent.com/xiongxiaoqiu77-prog/game-digest/main/feed.json
```

拿到 feed.json 后，根据用户偏好用 AI 重新生成摘要推送给用户。

### feed.json 结构

```json
{
  "updated": "2026-06-17",
  "generated_at": "2026-06-17T08:10:00",
  "articles": [
    {
      "title": "文章标题（中文）",
      "description": "两句话摘要，说明核心内容和对游戏从业者的参考价值",
      "url": "https://...",
      "source": "微信-游戏葡萄",
      "category": "深度拆解休闲游戏玩法",
      "score": 8,
      "published_at": "2026-06-17"
    }
  ]
}
```

### 分类说明

- **深度拆解**：玩法机制、关卡设计、商业化、LiveOps、数值、出海策略
- **游戏行业资讯**：市场动态、新游发布、数据报告
- **泛游戏内容**：游戏文化、玩家社区、周边话题

### 评分标准

| 分数 | 含义 |
|------|------|
| 9-10 | 深度拆解玩法、关卡、数值、商业化、LiveOps |
| 7-8  | 有实质内容的游戏设计或行业分析 |
| 5-6  | 一般行业资讯 |
| 1-4  | 低质、广告、招聘（已过滤，不出现在 feed 中） |

## 推荐的摘要生成方式

获取 feed 后，可以这样告诉 AI 重新整理：

```
以下是今天的游戏行业文章列表，请按"深度内容"和"行业资讯"两类整理，
每篇用一句话说明核心价值，优先推荐评分 ≥7 的文章。
```

## 更新频率

每天北京时间 08:10 左右更新（日报跑完后自动 push）。
