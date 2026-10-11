# Design Resource Navigator · 设计资源导航

![Resources](https://img.shields.io/badge/resources-25-blue) ![Python](https://img.shields.io/badge/python-stdlib-green) ![License](https://img.shields.io/badge/license-MIT-blue)

开发网站或 App 时，让 AI 助手根据页面需求、技术栈和已有设计系统，快速找到合适的设计参考、提示、组件、动效和素材。

A Codex skill for finding design references, AI prompts, UI components, motion patterns, and visual assets across 25 researched websites. Includes a bilingual offline search helper built with Python's standard library.

```text
用 $find-design-resources，为这个 Next.js + shadcn 后台
找地图组件和输入框微交互，沿用现有主题。
```

**资料核验日期：2026-10-11。** 本地检索不联网；选中资源后，助手会按任务需要查看当前条目、依赖和授权。价格、访问条件和网站内容可能变化。

## 能帮你做什么

- 把“需要什么设计”匹配到少量合适的来源，提供具体入口和下一步。
- 按用途和输出格式筛选，区分视觉参考、提示、可集成代码和图片素材。
- 优先沿用项目的组件库与主题，识别 React Web、原生移动端和纯 HTML/CSS 的差异。
- 保留一手来源、付费条件与许可范围；授权未确认的条目明确标注。

## 安装到 Codex

### Git 安装

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
git clone https://github.com/renmu2017/find-design-resources.git \
  "${CODEX_HOME:-$HOME/.codex}/skills/find-design-resources"
```

安装后重新打开 Codex 会话，使用 `$find-design-resources` 调用。目标目录已存在时，`git clone` 不会覆盖；请先确认已有版本。

通过 Git 安装的版本可以在该目录执行 `git pull --ff-only` 更新。

### ZIP 安装

从 [Releases](https://github.com/renmu2017/find-design-resources/releases) 下载 `find-design-resources-v1.0.0.zip`，解压后将 `find-design-resources` 文件夹放入 `${CODEX_HOME:-$HOME/.codex}/skills/`。确认目录内直接包含 `SKILL.md`。

Skill 的调用不依赖 Python；运行下面的本地检索辅助脚本需要 Python 3，无需安装第三方 Python 包。使用资源网站的 MCP/CLI 是可选步骤，本仓库不会自动配置服务或凭证。

## 使用示例

```text
用 $find-design-resources，为品牌官网找极简布局和排版参考。

用 $find-design-resources，为 SwiftUI 健康 App 的引导页
找温暖的视觉参考和手绘插图。

用 $find-design-resources，找不需要 JavaScript 的 SVG 加载动画。

用 $find-design-resources，给现有 DESIGN.md 找配色和字体参考，
保留已有设计规则。
```

助手应给出具体链接、适合的理由、可取得的材料、依赖或许可限制，以及下一步。只有参考需求时提供参考；同时要求开发时，继续完成对应实现与验证。

## 本地快速检索

在仓库根目录执行：

```bash
python3 scripts/search_resources.py "地图 标记 路线" --kind component --format react
python3 scripts/search_resources.py "后台 表单" --limit 4
python3 scripts/search_resources.py "加载" --format svg
python3 scripts/search_resources.py "hand drawn illustration" --kind asset --json
python3 scripts/search_resources.py --limit 25
```

支持中英文关键词匹配；这不是语义搜索。无匹配时不会强行推荐资源。脚本通过自身位置读取索引，也可从其他目录用脚本的完整路径调用。

| 筛选 | 可选值 |
| --- | --- |
| `--kind` | `inspiration`、`prompt`、`design-system`、`component`、`motion`、`asset` |
| `--format` | `screenshot`、`prompt`、`design-md`、`tokens`、`tailwind`、`html-css`、`react`、`image`、`svg`、`javascript` |
| `--limit` | 正整数，默认 5 |
| `--json` | 输出结构化结果 |

格式筛选表示该站至少部分条目提供这种形式，具体条目仍需确认。

## 收录资源

| 需求 | 资源 | 调研资料 |
| --- | --- | --- |
| 网站风格、AI 提示、设计规范 | Jiro Build、Minimal Gallery、Kage、Refero Styles、Component Gallery、AppShot Gallery、DESIGNmd、VibePrompt | [风格与提示](references/inspiration.md) |
| 组件、交互与动画实现 | 21st.dev、Kinetics、shadcn/ui、Aceternity UI、Magic UI、Motion Primitives、Uiverse、UIAble、mapcn、MicroKit UI、Liquid Glass、Anime.js | [组件与动效](references/components.md) |
| 文本、加载、按钮与图像素材 | CSS Text Effects、Circle Loaders、Gradient Buttons、Kitbitz、3dicons | [视觉素材](references/visuals.md) |
| 官方代理接入 | Kage、Jiro、21st.dev、DESIGNmd、Kitbitz | [MCP / CLI 入口](references/agent-access.md) |

每份资料均保留官方链接、适用场景、访问条件和核验范围。部分网站的动态页面通过浏览器读取；没有实际安装或调用所列外部 MCP/CLI。

## 仓库结构

```text
find-design-resources/
├── SKILL.md                       助手入口、需求路由与使用边界
├── agents/openai.yaml             Codex 界面元数据
├── scripts/search_resources.py    中英文离线关键词检索
├── references/resources.json      25 个资源的结构化索引
├── references/inspiration.md      风格、提示与设计规范
├── references/components.md       组件与动效
├── references/visuals.md           视觉素材
└── references/agent-access.md      官方 MCP / CLI 说明
```

## 许可与维护

本仓库原创代码、Skill 指令和研究摘要采用 [MIT License](LICENSE)。该许可不授予外部网站的模板、提示、截图、字体、组件或素材使用权；实际取得的材料按其原作者许可与服务条款处理。本仓库不包含第三方完整提示库、模板包或截图镜像。

维护资源时，同时更新对应资料和 `references/resources.json`，保留事实来源及核验日期。可以提交 Issue 或 Pull Request 补充变化和适用案例。
