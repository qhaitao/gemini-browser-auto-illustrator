# 🎨 Gemini 浏览器自动化高级生图项目 (D:\AI\image)

本项目是一个基于 **Google Antigravity Agent** 驱动的**自动化高级感生图与感官美学提示词工作流**。通过将 AI 提示词生成、安全审查规避转译、Markdown 文档存档与 Chrome 浏览器自动化控制结合，实现**自然语言输入 ➔ 自动化分镜与提示词生成 ➔ 驱动 Chrome/Gemini 网页端在线生成连环画册**的全自动流程。

---

## 🛠️ 环境依赖与安装指南 (Prerequisites & Installation)

在运行本项目前，请确保您的 Windows 系统已准备好以下环境依赖：

### 1. 必备基础软件
- **Python 3.10+** (推荐 Python 3.11/3.12)
  - 检查命令：`python --version`
- **uv / uvx** (高速 Python/Rust 工具运行器，用于免配置即时调用 `browser-harness`)
  - 安装命令（若未安装）：`pip install uv` 或 `winget install astral-sh.uv`
  - 检查命令：`uvx --version`
- **browser-harness** (开源 Chrome 浏览器自动化控制工具)
  - 官方项目：[browser-use/browser-harness (GitHub)](https://github.com/browser-use/browser-harness)
  - **无需手动安装**：项目中 `run_gemini.py` 脚本使用 `uvx browser-harness` 命令，`uv` 会在首次运行时自动下载并按需加载；如需离线或手动全局安装，也可执行 `pip install browser-harness`。
- **Google Chrome 浏览器**
  - 请确保 Chrome 已安装，并且在 Chrome 中已登录您的 Google 账号，能正常打开使用 [Gemini 网页版](https://gemini.google.com/app)。
- **Google Antigravity (AGY) CLI / IDE**
  - 本项目的核心 Agent 运行平台。

### 2. 浏览器准备 (启动要求)
在进行自动化生图前：
- **强烈推荐**：提前在 Chrome 中打开并切到 `https://gemini.google.com/app` 页面。
- 自动化脚本 `run_gemini.py` 会通过 `uvx browser-harness` 自动定位已打开的 Gemini 标签页；若未打开，脚本会自动新建标签页并导航至 Gemini。

---

## 📂 项目目录结构 (Directory Architecture)

```text
D:\AI\image\
├── README.md                           ← 本项目使用说明文档
├── AGENTS.md                           ← 项目级强制硬规则（拦截生图并路由至技能）
├── .agents/skills/                     ← 项目专属技能库 (Skills Matrix)
│   ├── gemini-browser-auto-illustrator/
│   │   ├── SKILL.md                    ← 自动化生图主控编排规范
│   │   └── scripts/run_gemini.py       ← 驱动 Chrome/Gemini 的核心 Python 脚本
│   ├── erotic-prompt-generator/
│   │   └── SKILL.md                    ← 古典香艳/露骨文本转译与审查规避技能
│   └── aesthetic-prompt-generator/
│       └── SKILL.md                    ← 20大视觉流派/非色情美学提示词生成技能
├── prompt/                             ← 自动保存生成的提示词 Markdown 文件 (YYYYMMDD_HHMM_*.md)
├── images/                             ← 本地保存或整理的生成的图片文件
└── videos/                             ← 生成的动态视频成果
```

---

## 🚀 使用流程与工作说明 (Workflow & Usage)

### 1. 触发方式（全自动自然语言）
在新会话中将工作目录定位至 `D:\AI\image`，直接向 Agent 发送指令即可，**无需记忆复杂命令**：

- **通用生图示例**：
  > “生图，杜甫《绝句》两个黄鹂鸣翠柳”
  > “画图，新中式水墨风格的苏州园林雨景”
- **香艳/古典情致生图示例**：
  > “生图，情色 座上香盈果满车，谁家年少润无瑕...”

### 2. 自动化执行逻辑 (Behind the Scenes)
当输入包含 `生图`、`画图`、`配图`、`生成图片` 等触发词时：
1. **硬规则拦截**：`AGENTS.md` 阻止 Agent 调用本地短路工具 `generate_image`。
2. **智能双轨路由**：
   - 识别到`情色` / `香艳` 关键词 $\rightarrow$ 跨 Skill 调用 `erotic-prompt-generator` 执行安全隐喻转译（湿纱贴体、肢体张力特写、影子折射、器物双关）。
   - 通用风雅 / 写实场景 $\rightarrow$ 跨 Skill 调用 `aesthetic-prompt-generator` 注入相机参数、高级光影与渲染器。
3. **保存 Markdown**：自动将提示词保存至 `D:\AI\image\prompt\YYYYMMDD_HHMM_<主题>_<N>图提示词.md`。
4. **浏览器自动化出图**：后台自动运行：
   ```bash
   python D:\AI\image\.agents\skills\gemini-browser-auto-illustrator\scripts\run_gemini.py --markdown "D:\AI\image\prompt\<文件名>.md"
   ```
   脚本通过 `browser-harness` 自动定位 Chrome 中的 Gemini 标签页，以“发送Prompt ➔ 监测生成 ➔ 静置5秒 ➔ 下一张”的节奏在线完成整套画册出图。

---

## ❓ 常见问题与故障排查 (Troubleshooting)

### Q1: 提示 `[任务排队中...] 检测到前序生图任务仍在运行`？
- **原理**：脚本内置了文件排队锁 `prompt/.gemini_runner.lock`，防止多个生图任务同时向 Gemini 输入打字导致冲突。
- **解决**：等待前序任务完成即可自动接替；若前序任务异常中断锁未释放，锁会在 10 分钟后自动超时清理，也可手动删除 `D:\AI\image\prompt\.gemini_runner.lock` 文件。

### Q2: 为什么生成完后本地目录没有下载 PNG 图片？
- **规范说明**：本项目遵循**纯在线呈现与免下载规范**。生图全部在 Chrome 的 Gemini 官方页面中渲染，直接保留在 Chrome 控制台中供放大浏览，避免下载大量临时图片占用本地空间（若需要某些图片可直接在网页右键保存）。

### Q3: 修改或自定义技能规则该去哪里？
- 若需要修改生图核心脚本与节奏 $\rightarrow$ 编辑 `D:\AI\image\.agents\skills\gemini-browser-auto-illustrator\scripts\run_gemini.py`
- 若需要调整触发生图的规则逻辑 $\rightarrow$ 编辑 `D:\AI\image\AGENTS.md` 与 `SKILL.md`
