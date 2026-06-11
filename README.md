# 游戏日报 Game Digest

每天 08:00 自动抓取游戏行业内容，用 AI 评分筛选，发送到飞书群。

## 功能

- **微信公众号**：通过 [we-mp-rss](https://github.com/rachelos/we-mp-rss) 订阅公众号 RSS，token 每天自动刷新
- **RSS 订阅**：Deconstructor of Fun、Naavik、GameLook 等行业媒体
- **播客**：小宇宙播客（机核、游戏电波等）
- **搜索**：Google News + 自定义关键词
- **AI 评分**：用 Claude 对每篇文章打分（1-10），过滤广告和低质量内容
- **去重**：7 天历史去重，不重复推送
- **飞书推送**：按评分分类发送到指定群

## 效果预览

日报按分类展示，每篇附中文标题、摘要和评分：

```
🎮 休闲游戏分析日报 · 2026年06月11日  共 14 篇

📌 深度拆解
• [9分] Royal Match 关卡设计拆解...
• [8分] 三消游戏元游戏层设计分析...

📰 行业资讯
• [6分] Voodoo Q1 出海增长报告...
```

## 依赖

- Python 3.11+
- [Claude Code CLI](https://claude.ai/code)（用于 AI 评分，需登录 Claude Pro 账号）
- [lark-cli](https://github.com/larksuite/lark-cli)（飞书消息发送）
- [we-mp-rss](https://github.com/rachelos/we-mp-rss)（微信公众号 RSS，可选）

```bash
pip install feedparser requests beautifulsoup4 anthropic
```

## 快速开始

**1. 克隆并配置**

```bash
git clone https://github.com/your-username/game-digest
cd game-digest
cp .env.example .env
# 编辑 .env，填入飞书群 ID 和用户 ID
```

**2. 配置飞书**

在 `.env` 里填写：
- `FEISHU_CHAT_ID`：日报发送的群 ID（在飞书群设置里查看）
- `FEISHU_USER_ID`：你的飞书用户 ID（用于健康检查告警）

**3. 添加微信公众号（可选）**

部署 [we-mp-rss](https://github.com/rachelos/we-mp-rss)，扫码登录后运行：

```bash
python3 sync_wewe_feeds.py       # 从 we-mp-rss 同步公众号列表
python3 digest.py --check-wechat-feeds  # 验证 RSS 可用
```

**4. 自定义内容源**

编辑 `digest.py` 顶部的配置区域：

- `RSS_FEEDS`：添加/删除 RSS 订阅源
- `PODCAST_FEEDS`：小宇宙播客 ID
- `FOCUS_GAMES`：重点关注的游戏（生成搜索关键词）
- `PRIORITY_ACCOUNTS`：优先级微信公众号（评分 +1）

**5. 手动运行**

```bash
python3 digest.py           # 发送今日日报
python3 digest.py --test    # 测试模式（不发送）
python3 digest.py --date 2026-06-10  # 补发指定日期
```

**6. 设置定时任务（macOS）**

创建 `~/Library/LaunchAgents/com.game-digest.daily.plist`：

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.game-digest.daily</string>
    <key>ProgramArguments</key>
    <array>
        <string>/bin/bash</string>
        <string>/path/to/run.sh</string>
    </array>
    <key>StartCalendarInterval</key>
    <dict>
        <key>Hour</key><integer>8</integer>
        <key>Minute</key><integer>0</integer>
    </dict>
</dict>
</plist>
```

```bash
launchctl load ~/Library/LaunchAgents/com.game-digest.daily.plist
```

## 目录结构

```
game-digest/
├── digest.py           # 主脚本
├── sync_wewe_feeds.py  # 从 we-mp-rss 同步公众号列表
├── wechat_feeds.json   # 公众号 RSS 列表（本地生成，不提交）
├── history.json        # 去重历史（本地生成，不提交）
├── archive/            # 每日存档 Markdown（本地生成，不提交）
├── .env                # 敏感配置（不提交）
└── .env.example        # 配置模板
```

## 评分标准

Claude 对每篇文章按以下标准打 1-10 分：

| 分数 | 含义 |
|------|------|
| 8-10 | 深度拆解，有数据、有分析框架 |
| 5-7  | 行业资讯，有信息量 |
| 3-4  | 泛游戏内容，可读 |
| 1-2  | 广告、转载、无实质内容 |

默认只发送 3 分及以上的文章。

## License

MIT
