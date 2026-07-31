---
name: aesthetic-prompt-generator
description: 专门用于生成非色情的唯美大片、平面海报设计、极简杂志插画、Notion线稿、科技信息图、3D轴侧微缩世界、蓝图叠加、照片涂鸦、新中式水墨、高角度时尚摄影与极简线条等 20 大艺术与设计流派提示词生成器。内置大师级视觉七维基因矩阵（主题、媒介、环境、灯光、色彩、情绪、构图）、角色一致性锚定协议与满幅无边框强约束，自动将常规文本转译为顶级美学水准的中英文 Prompt 序列。
---

# 唯美大师级生图提示词生成器 (Aesthetic Masterclass Prompt Generator)

本 Skill 旨在为非色情文本、品牌海报、极简杂志插画、科技信息图、3D 微缩模型、照片涂鸦、新中式水墨、时尚摄影等各类视觉场景生成具备**画廊级美学水准、高信息密度与顶级视觉创造力**的 AI 生图提示词序列（深度优化 Midjourney v6, SDXL, Gemini ImageFX, DALL-E 3 等）。

---

## 🚨 Agent 执行优先协议与 Gemini 网页生图规约 (Agent Execution & Gemini Web Protocol)

1. **生图动词识别与 Google 浏览器 Gemini 网页生图（强制规约）**：
   - 当用户指令包含明确生图动词（如“生图”、“画图”、“生成图片”等）时，Agent **必须一直且统一使用在 Google 浏览器 (Chrome) 中打开的 Gemini 网页 (`https://gemini.google.com/app`) 进行生图**。
   - 生图任务必须联动 `gemini-browser-auto-illustrator`，通过 `uvx browser-harness` 驱动 Google 浏览器控制 Gemini 网页版在线发送 Prompt 生成图片。
   - 严禁优先使用 API 工具（如 `generate_image`），防止额度受限；统一走 Chrome/Gemini 网页端自动化流。
2. **网页控制与降级处置（严禁伪造假图）**：
   - 若浏览器自动化遇到异常，Agent **严禁使用代码程序（如 Python PIL 绘制几何线条）生成假图片充数**。
   - 处置方式：确保将满血画廊级 Prompt 完整呈现，并在 Google 浏览器 Gemini 网页端重新同步或发起重试。
3. **输出格式零例外契约**：
   - Agent 输出 Prompt 文档与交付时，**必须 100% 完整保留模板中的所有板块**（包含标题、全局角色一致性锚点、七维基因对齐、英文提示词代码块），不得随意删减或简化排版。

---

## 🤖 智能内容自适应风格路由器 (Self-Adaptive Style Router)

在接收到用户文本后，系统**绝不套用机械固定模板**，而是通过以下**语义特征匹配表**自动分析文本语义，选择最适配的视觉风格流派：

| 用户文本语义特征 / 领域 | 自动匹配的最佳流派模版 (Auto-Selected Template) | 核心视觉语言特征 |
|:---|:---|:---|
| **古诗词 / 汉服 / 古典人物 / 琴茶金石** | **【16 宋明工笔绢本】** 或 **【11 新中式水墨】** | 绢本墨韵、柔和烛光、青瓷与竹影、静谧雅致 |
| **代码 / 开源项目 / 架构图 / 技术文档** | **【02 GitHub 科技 UI 卡片】** 或 **【03 Notion Mono】** | 卡片式布局、扁平图标、低饱和科技蓝灰、高信息密度 |
| **地标 / 城市天际线 / 建筑设计 / 展览** | **【07 3D 轴侧微缩模型】** 或 **【08 蓝图叠加信息图】** | 3D C4D 景箱、照片叠加白线蓝图、博物馆铭牌排版 |
| **名言金句 / 哲学思考 / 文学隐喻** | **【06 高级概念大字海报】** 或 **【10 WBW 极简涂鸦】** | 巨型中文字体第一视觉、深层隐喻、Wait But Why 讽刺手绘 |
| **穿搭 OOTD / 街拍 / 流行生活方式** | **【04 港风复古胶片】** 或 **【13 高角度时尚摄影】** | 柯达暖调胶片、85mm 俯视特写、时尚杂志大片质感 |
| **趣味表情包 / 3D 卡漫角色 / 动漫** | **【09 3x3 皮克斯 3D 表情包】** 或 **【16 新海诚风动漫】** | 9 宫格不同表情、粘土高光材质、天光云影日系色彩 |
| **深邃历史 / 品牌演进 / 发展进程** | **【05 演化进程信息图海报】** | 递进式阶梯路径、年代标尺、展陈式节点 |

> **注**：若用户显式指定了跨界风格（如“用赛博朋克画李白”），系统将进行**跨领域混搭重组**（主体为李白，媒介/环境为赛博朋克雨夜）。

---

## 🧬 核心工作流与七维视觉基因矩阵 (The 7-Dimensional Visual Matrix)

在生成任何 Prompt 时，除了确定 **艺术流派模版**，必须显式对齐以下 **七大视觉维度 (The 7 Pillars of Visual DNA)**：

| 维度编号 | 视觉基因维度 | 维度分类与关键词库 |
|:---|:---|:---|
| **1. 主体 (Subject)** | 人物 / 动物 / 名人 / 地点地标 / 器物 / 建筑 | `Person, portrait of a lady, wild red fox, ancient temple, antique porcelain, futuristic supercar` |
| **2. 媒介 (Medium)** | 摄影 / 油画 / 水彩 / 工笔 / 雕塑 / 涂鸦 / 挂毯 / 3D渲染 / 矢量 | `35mm photograph, Gongbi silk painting, baroque oil painting, marble sculpture, 3D Octane render` |
| **3. 环境 (Environment)** | 室内 / 庭院 / 城市街道 / 水下 / 月球太空 / 迷雾森林 | `cozy indoor boudoir, rainy city street, underwater coral, lunar surface, snow-covered forest` |
| **4. 灯光 (Lighting)** | 柔和环境光 / 阴天散射光 / 霓虹流光 / 强明暗对照 / 工作室边缘光 / 黄金光辉 | `soft ambient lighting, overcast light, vibrant neon reflections, Caravaggio chiaroscuro, golden hour` |
| **5. 颜色 (Color)** | 莫兰迪中性色 / 鲜艳撞色 / 单色黑白 / 柔和粉彩 / 青橙配色 / 琥珀金色 | `muted Morandi palette, vibrant high-contrast duotone, monochrome B&W, deep teal and orange` |
| **6. 情绪 (Mood)** | 宁静安祥 / 忧郁沉思 / 欢快充沛 / 宏大神秘 / 怀旧复古 / 理性极简 | `peaceful serene mood, melancholic contemplative atmosphere, energetic dynamic, nostalgic retro` |
| **7. 构图 (Composition)** | 肖像特写 / 面部爆头 / 极特写 / 俯视鸟瞰 / 轴侧三维 / 宽幅全景 / 极简留白 | `portrait close-up, extreme macro detail, top-down bird's-eye view, 45-degree isometric, generous white space` |

---

## 👤 角色一致性三层防护协议 (3-Layer Character Consistency Protocol)

为了确保连环画册、故事分镜或连贯大片中**人物面貌、发型、体态与服饰 100% 保持一致，不发生漂移畸变**，本 Skill 强制执行三层防护规则：

### 1. 第一层：角色硬基因锚点 (Verbatim Character Anchor)
在多张分镜生图时，提取角色的**固定生理特征 + 标志性服饰**，生成不可变的标准词块 `[Character Anchor]`。全套 Prompt 必须**逐字无缝复制插入**该词块：
- **示例格式**：  
  `[Li Qingzhao]: 25-year-old Song Dynasty woman, delicate oval face, almond-shaped eyes, dark hair tied in a loose elegant bun with an emerald hairpin, wearing a signature translucent off-white silk robe with crimson inner trim.`

### 2. 第二层：动作与面部分离 (Action & Motion Isolation)
保持 `[Character Anchor]` 锚点文本 100% 冰冻不变，只在锚点后接**动态场景变量**（动作、镜头视角、光影变化）：
- `[Character Anchor] sitting by an antique guqin under moonlight...`
- `[Character Anchor] standing on a snow-covered bridge holding a red plum blossom...`

### 3. 第三层：多视角角色设定图预热 (3x3 Character Sheet Anchor)
若需生成大型多画面绘本，可在第 1 张图先生成 **3x3 角色设定切片图** 作为全局视觉基准：
- **设定图语法**：`Character design sheet of [Character Anchor], 3x3 grid collage showing 9 different emotions and multi-angle views (front, profile, 3/4 view), neutral studio lighting, isolated white background.`

---

## 🎨 二十大艺术与平面设计流派模版库 (The 20 Master Visual Formulations)

| 编号 | 模版流派 | 视觉核心与构图焦点 | 英文 Prompt 核心要素词库 |
|:---|:---|:---|:---|
| **01** | **极简现代杂志插画** | 干净流畅单线、大面积留白、柔和中性色+鲜艳焦点、无文字高端杂志质感 | `minimalist modern magazine illustration, clean flowing lines, vast negative space, soft Morandi neutral tones with vivid accent, elegant balance, editorial graphic style` |
| **02** | **GitHub/科技 UI 卡片** | Notion/Linear 卡片布局、图标化表达、低饱和科技色 | `modern minimalist tech infographic poster, card-based layout, Notion Linear aesthetic, flat vector icons, clean information density, cool blue and grey palette` |
| **03** | **Notion Mono 极简线稿** | 黑白单色线稿、极简形状、微妙手绘感、俏皮表现姿态、纯白背景 | `Notion mono editorial illustration, minimalist black line drawing on pure white background, flat monochrome design, simple geometric shapes, subtle hand-drawn feel` |
| **04** | **照片涂鸦 (Photo Doodling)** | 超写实真实照片 + 2D 黑色火柴人涂鸦互动、基于真实地形与物理交互 | `Christoph Niemann photo doodling style, photorealistic real-world scene combined with flat 2D black stick figure line doodles interacting with real object physical structures` |
| **05** | **演化进程信息图海报** | 空间化阶梯/平台路径、时间演进序列、展陈式节点、博物馆展览级排版 | `process evolution infographic poster, spatialized stepped timeline path, curated display platforms, historical evolution nodes, elegant museum exhibition typography` |
| **06** | **高级概念大字/隐喻海报** | 巨型汉字第一视觉、深刻视觉隐喻、三级文字排版、展览级克制与沉稳 | `high-level conceptual literary poster, massive central Chinese typography as dominant visual, profound metaphor graphic, minimalist exhibition style, dark dramatic mood` |
| **07** | **3D 轴侧微缩模型海报** | C4D/Octane 梦工厂感轴侧微缩景箱、水墨光雾虚空背景、博物馆铭牌排版 | `3D isometric micro-world poster, DreamWorks style Octane render, miniature floating island scene, ethereal mist background, elegant museum plaque typography` |
| **08** | **地标蓝图叠加信息图** | 真实地标照片 + 蓝图式白线条剖面/数据技术注释叠加、教育科技感 | `landmark architectural infographic, real photo overlaid with white chalk blueprint lines, technical measurement annotations, structural load arrows, educational graphic` |
| **09** | **3x3 皮克斯 3D 表情包** | 9 宫格不同姿态表情包、Chibi 比例 3D 角色、纯白背景 PNG 提取感 | `3x3 grid collage, Pixar-style 3D character emoji sticker sheet, 9 different expressive poses and facial emotions, Octane render, isolated white background` |
| **10** | **WBW 极简知识涂鸦** | 极简粗糙单线火柴人、纯白虚空、讽刺哲理思考对话框、Wait But Why 美学 | `Wait But Why style minimalist stick figure doodle, constant monoline black ink lines, unrefined handwritten Chinese text bubbles, pure white void background, humorous philosophy` |
| **11** | **新中式水墨绘本** | 上美影 80s 毛笔触感与宣纸纹理、低饱和矿物色、大巧若拙、极简留白 | `classic Shanghai animation style, 1980s Chinese ink book illustration, raw brushstrokes on textured Xuan paper, muted mineral pigments, elegant negative space` |
| **12** | **黑板报彩色粉笔风** | 黑色黑板背景、彩色粉笔手绘线条、极简卡通图标、高对比易读 | `colored chalk style infographic on dark black chalkboard background, hand-drawn chalk lines and icons, educational chalkboard aesthetic, clean high contrast` |
| **13** | **高角度时尚摄影序列** | 85mm / 俯视高角度人像、真实皮肤纹理、多帧时尚连贯姿态 | `high-angle close-up fashion photography, 85mm lens, subject looking straight up, candid natural sunlight, highly detailed skin textures, high fashion magazine spread` |
| **14** | **极简线条 (Minimal Line)** | 单线画（Continuous line）、莫兰迪色块点缀 | `minimalist continuous line art, elegant single black line drawing on ivory paper, selective color accents, clean vector line aesthetic` |
| **15** | **手绘插画 (Hand-drawn)** | 水彩晕染手绘感、细致铅笔线条肌理、温情绘本 | `warm hand-drawn illustration, soft watercolor wash, delicate pencil sketch lines, textured paper grain, storybook feel` |
| **16** | **宋明工笔绢本** | 水墨绢本、茶道金石、竹影青瓷、琴韵焚香 | `Song Dynasty Gongbi silk painting, subtle ink wash, antique celadon porcelain, misty bamboo forest, golden candlelight` |
| **17** | **大师人文纪实** | 徕卡/哈苏光影、情绪眼神、自然微光 | `shot on Hasselblad 500CM, cinematic 35mm film grain, moody natural sunlight, expressive emotional gaze, photorealistic skin` |
| **18** | **赛博朋克雨夜** | 霓虹流光、湿滑路面倒影、高耸摩天楼 | `cyberpunk metropolis, neon rain reflections, volumetric smog, intricate cybernetic details, futuristic architectural scale` |
| **19** | **暗黑哥特巴洛克油画** | 卡拉瓦乔强明暗对照（Chiaroscuro）、古典厚涂 | `baroque oil painting, Caravaggio chiaroscuro lighting, dramatic deep shadows, rich velvet textures, masterwork oil stroke` |
| **20** | **极简现代建筑光影** | 清水混凝土、安藤忠雄切片光影、极简几何 | `minimalist architecture by Tadao Ando, sharp dramatic shadow geometry, raw concrete texture, bright afternoon sunbeams` |

---

## 🔒 强约束规范 (Mandatory Rules)

1. **无边框强约束 (Borderless Rule)**：  
   所有 Prompt 结尾**必须**包含：`no borders, borderless, no frame, full bleed image`，确保 AI 生图满幅呈现，无黑边/白边/框线遮挡。
2. **纯净无文字 / 无必要不加文字规约 (No Text & Pure Visual Rule)**：  
   除非用户显式要求在画面中生成特定标题或文字（如海报大字、招牌文字等），所有 Prompt **默认必须保持画面纯净，严禁主动添加任何文字、标题、字幕、水印或字母**。提示词中需包含 `no text, no words, clean image without text` 强约束；仅当用户显式要求加字时，才使用中文文字规约（如 `Chinese typography "..."`）。
3. **纯净非色情**：  
   本 Skill 专注展示优雅、极简、平面海报、科技信息图、3D 模组、手绘插画与前沿艺术美学，严禁引入任何暴露或敏感词汇。

---

## 📋 标准结构输出模板 (Mandatory Output Template)

Agent 输出 Prompt 时，**必须 100% 严格遵守以下 Markdown 结构模板**：

```markdown
# [题材/作品名] · 大师级七维与一致性提示词 [流派模版名]

## 全局角色一致性锚点 (Character Consistency Anchors)
- **角色A**: `[Name]: [Facial base features], [Hairstyle], [Eye shape], [Signature attire]`

---

## 画面 01 · [场景名称]

- **七维基因对齐**：
  - 【主体】: [角色A] | 【媒介】: [照片/工笔/3D渲染]
  - 【环境】: [室内/街道/庭院] | 【灯光】: [柔和/霓虹/阳光]
  - 【颜色】: [莫兰迪/青橙/单色] | 【情绪】: [宁静/深沉/活力]
  - 【构图】: [特写/全景/留白]

**【英文提示词 (Midjourney / SD / Gemini 通用)】**
[Medium Spec]. [Character A Anchor] [Action & Environment]. [Lighting, Color & Mood], [Composition & Style Keywords], award-winning masterpiece, no borders, borderless, no frame, full bleed image, 16:9 aspect ratio.
```
