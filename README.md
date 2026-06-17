# 游戏行业日报 Game Digest

每天自动聚合游戏行业内容，AI 评分筛选，直接推送到你的通讯工具或在对话中显示。

**理念：** 信息太多，时间有限。日报帮你把值得看的内容先捞出来，你只需要从一份干净的列表开始看。

## 你会得到什么

每日更新的内容，覆盖：

- **微信公众号**：75 个游戏行业公众号（游戏分析、出海、买量、产品拆解）
- **海外媒体**：Deconstructor of Fun、Naavik、GameLook 等行业 RSS
- **播客**：小宇宙游戏类播客
- **搜索**：Google News + 重点游戏关键词

每篇文章附中文标题、两句话摘要、来源和分类，已过滤广告和低质量内容。分类包括：深度拆解、行业资讯、泛游戏内容。

## 工作原理

1. 中心化 feed 每天北京时间 08:10 更新，聚合所有信息源的最新内容
2. 你的 agent 获取 feed——一次 HTTP 请求，不需要 API key
3. 你的 agent 根据你的偏好将内容整理为摘要
4. 摘要推送到你的通讯工具，或直接在对话中显示

## 安装 Skill

```bash
git clone https://github.com/xiongxiaoqiu77-prog/game-digest.git ~/.claude/skills/game-digest
```

安装后，在 Claude Code 中说"看今天的游戏日报"或执行 `/game-digest` 即可。

不需要任何 API key，也不需要部署任何服务。
