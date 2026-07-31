---
name: erotic-prompt-generator
description: 专门用于将古典艳情文学段落（如《花营锦阵》《金瓶梅》《肉蒲团》等）或各类香艳露骨文本，转译为高艺术水准、活色生香且符合AI生图与生视频审查规范的中英文提示词序列（含生图 Prompt 与 Sora/Runway Gen-3/Kling/Hailuo/Seedance 等视频场景提示词），包含人物一致性锚点、镜头语言与风险降级方案。
---

# 香艳视觉提示词生成器 (Erotic Image & Video Prompt Generator)

本 Skill 旨在解决古典艳情文学或露骨香艳描写在 AI 生图（Midjourney, SD, DALL-E 3 等）与 AI 生视频（Sora, Runway Gen-3, Kling 可灵, Luma, Hailuo 海螺, Volcengine Seedance 等）中因敏感词/直白行为导致被拦截或动作畸变的问题。通过**明代工笔绢本 / 影视级写实风格**与**五大艺术转译手法**，在不出现直白生殖器官或硬性交动作前提下，将文本转译为肉感拉满、活色生香、镜头流畅、人物统一且符合审核规范的生图与视频场景提示词。

---

## 模式选择 (Modes)

根据用户需求，本 Skill 支持两种输出模式：
1. **模式一：生图提示词序列 (Multi-Shot Static Image Prompts)** - 适用于连环分镜绘图、绘本画册。
2. **模式二：动态视频场景提示词 (Dynamic Video Scene Prompts)** - 包含运镜轨迹、动态变化、时长控制、帧率与主流 AI 视频模型兼容格式。

---

## 六大古典香艳场景模版 (The 6 Conceptual Erotic Master Formulations)

为了避免生图提示词同质化、缺乏创造性，本 Skill 提取古典诗词典籍（如《春宵十咏》《风月十绝》《山歌》）中的六大情致意象：

| 场景模版 | 古典诗词意象典源 | 画面构图与视觉创造性焦点 | 英文 Prompt 特色词集 |
|:---|:---|:---|:---|
| **1. 酥融流彩 (沐浴/肌理与温度)** | *“浴罢檀郎扪弄处，灵华凉沁紫葡萄”* / *“衣褪半含羞，似芙蓉怯素秋”* | **清池出浴 / 湿发与膏脂**。聚焦水珠顺着玉肌滑落、红绡湿透贴肤、散落花瓣与青铜水镜。 | `steaming bath, translucent wet red silk clinging to porcelain shoulders, water droplets glistening on golden skin, scattered rose petals on amber water` |
| **2. 锦被翻浪 (暗香与重床复榻)** | *“纱橱月上，顾不得鬓乱钗横，红绫被翻波滚浪”* | **床榻张力 / 乱帛与肢体**。聚焦交错的云鬓金钗、蜷曲的纤足、抓紧绣花绫被的发白手指、斜侧的红烛倒影。 | `tangled dark hair across embroidered crimson satin quilt, red silk ankle ribbon, white-knuckled grip on bed frame, disheveled hairpins scattered` |
| **3. 洞房幽月 (纸窗巨影与折射)** | *“半夜牙床戛玉鸣，小桃枝上宿流莺”* / *“花兵月阵暗交攻”* | **光影重叠 / 剪影与虚实**。前景聚焦摇曳的竹影与倾倒的金酒杯，背景透光的雕花纸窗上映出缠绵的庞大阴影。 | `rhythmic silhouette cast on glowing paper lattice screen, fallen gold chalice spilling dark wine, dappled moonlight and candle dapples` |
| **4. 醉卧花房 (酒晕与残妆消魂)** | *“脸红暗染胭脂汗，面白误污粉黛油”* / *“一夜情浓似酒，香汗渍鲛绡”* | **酒晕酡红 / 醉卧与呼吸**。聚焦微肿的绛唇、眼角晕开的墨痕、微微敞开的薄纱与急促起伏的胸膛。 | `flushed cheeks, swollen rose-red lips, kohl smear under half-closed seductive eyes, unbuttoned sheer robe, deep shallow breathing` |
| **5. 眉黛春山 (梳妆与窥探双关)** | *“淡月弯弯浅效颦，低头想是思张敞”* / *“手里金鹦鹉，偷眼暗形相”* | **梳妆隐喻 / 窥视与含羞**。通过青铜镜折射半露的香肩与顾盼含情的眼神，半掩的罗扇与屏风遮挡。 | `reflection in antique bronze mirror, half-revealed bare shoulder, peeking behind a painted silk screen, delicate lace fan blocking half face` |
| **6. 冰碗红杏 (器物隐喻与体液双关)** | *“葡萄软软蛰酥胸，零零湛露滴真珠”* / *“浅酒人前共，软玉灯边拥”* | **感官器物 / 露珠与冷暖对比**。聚焦冰碗里微裂的红桃/葡萄、流淌的水珠、悬挂的红丝脚带与热气腾腾的幽阁氛围。 | `glistening dew droplets on ripe split peaches, ice bowl with dark grapes, crimson silk ankle thread suspended, contrast of cool jade and warm skin` |

---

## 核心工作流 (Workflow)


当用户输入一段香艳文本并要求输出提示词时，按以下 5 步执行：

1. **文本提炼与分镜规划**：
   - 提取原著场景的关键动势、器物隐喻、人物互动与情感高潮。
   - 按照叙事弧线（前奏 $\rightarrow$ 相遇 $\rightarrow$ 戏谑 $\rightarrow$ 高潮 $\rightarrow$ 极处 $\rightarrow$ 余韵）划分 4 ~ 8 个画面或视频镜头。

2. **锁定人物一致性锚点 (Character Consistency Anchors)**：
   - 提取主要角色（女主、男主、侍婢等）的面部、发型、体态、皮肤质感、经典服饰与标志性道具。
   - 格式化为英文 Prompt 的固定插入语句。

3. **套用五大转译手法 (The 5 Erotic Translation Principles)**：
   - 规避直白器官与硬动作，用肢体张力、感官细节与光影摇曳替代。

4. **强制满幅无边框约束 (Borderless & No-Frame Constraint)**：
   - 所有生成的 Prompt 结尾必须显式加入 `no borders, borderless, no frame, full bleed image` 词组，确保 AI 生图满幅展现、无卡牌/画框边框干扰。

5. **强制中文文字渲染规约 (Mandatory Chinese Typography Rule)**：
   - 若画面涉及出现任何文字（如榻案诗卷、海报大字、竹匾铭牌、招牌标语等），必须统一指定使用中文文字（如 `Chinese calligraphy "日啖荔枝三百颗"`），严禁输出英文或拼音。

6. **标注风险评级与备选方案 (Risk Rating & Fallbacks)**：
   - 🟢 **安全级** (静物/气氛/远景)
   - 🟡 **香艳中高风险级** (湿纱贴体/身体弧线/神态特写/动态轻喘)
   - 🔴 **高风险拦截级** (强烈体态碰撞) $\rightarrow$ **必须附带 🟡 动态降级替换方案**（如水面倒影波纹/壁上巨大起伏阴影/手部抓席特写）。

7. **生成标准结构输出**（中英对照、含视频运镜参数与模型通用格式）。


---

## 五大转译手法 (The 5 Erotic Translation Principles)

| 手法 | 替代对象 | 视觉/动态呈现公式 |
|:---|:---|:---|
| **1. 湿纱贴体 (Translucent Silk)** | 裸体/解衣 | `translucent white silk robe cling to skin`, 湿透布料如墨染宣纸，随呼吸微弱起伏贴合 |
| **2. 肢体张力特写 (Body Tension)** | 生殖动作 | `white-knuckled grip on wooden frame`, 抓紧竹席、脚趾蜷曲、发丝甩弧、咬唇仰首、汗珠沿锁骨滑落 |
| **3. 影子与水面折射 (Shadow & Reflection)** | 直白交合 | `large, rhythmic shadow cast on paper lattice wall`, `water reflection shattered into amber ripples`, 用铜盆水波折射与纸窗巨影表现慢速动势 |
| **4. 器物与温度双关 (Material Metaphors)** | 性器官/体液 | 大红睡鞋、冰碗黄李、酒液沿肌肤流淌、红丝脚带悬挂晃动、散落的湿白巾帕 |
| **5. 残妆与事后余韵 (Aftermath & Ruins)** | 射精/高潮收尾 | `kohl smear beneath one eye`, `swollen rose-stained lips`, 慢速推远镜头、梳妆废墟、落日余晖披衣 |

---

## 动态视频生成专章 (Video Scene Guidelines)

### 1. 视频运镜语法 (Camera Motion Syntax)
AI 视频模型对清晰明确的运镜指令响应最佳，推荐包含以下关键词：
- **Slow push-in / zoom-in**: 缓慢推近特写（聚焦双唇微张、眼波流转、汗珠滑动）。
- **Slow pull-back / zoom-out**: 缓慢拉远（展示从微观张力到整体环境余韵）。
- **Slow-motion tracking shot**: 慢镜头跟随（跟踪手指抓紧木架发白、湿纱微风摆动）。
- **Rack focus**: 焦距转换（从背景摇摇欲坠的红烛转换至前景蜷曲的脚趾）。
- **Paper lattice shadow pan**: 摇镜观影（镜头缓慢过潘，记录墙窗上缠绵的阴影节奏）。

### 2. 视频模型提示词通用结构 (Universal Video Prompt Template)
```text
[Camera Movement] + [Subject & Micro Motion] + [Dynamic Environment & Lighting] + [Art Style Anchor] + [Specs & Quality]
```

### 3. 主流视频模型兼容参数
- **Kling / Runway Gen-3 / Hailuo**: `Slow motion 60fps, smooth motion, high motion intensity`
- **Sora / Luma Dream Machine**: `Cinematic tracking shot, fluid realistic motion, physics compliant`
- **Volcengine Seedance**: `Ming Dynasty gongbi style animation, warm dynamic lighting, 16:9`

---

## 视频场景输出格式标准

```markdown
# [题材/书名·章节] · 香艳视频场景提示词 (Video Prompts)

> **原典出处**：...
> **视觉风格与光影基调**：...

---

## 全局人物一致性锚点 (Character Anchors)
- **角色A**: `[Name]: [Facial features], [Body shape], [Signature attire]`
- **角色B**: `[Name]: [Facial features], [Attire details]`

---

## 镜头 01 · [镜头名称] [风险等级 🟢/🟡/🔴]

- **对应情节**：*原著文本*
- **运镜方式**： Slow push-in close-up / Rack focus
- **动态核心**： [描述从 T0 到 T1 的微动作与光影变化]
- **建议时长**： 5秒 / 慢动作 (Slow-motion 60fps)

**【英文视频提示词 (Sora / Gen-3 / Kling / Seedance 通用)】**
[Slow motion close-up push-in shot]. [Character Anchor] lying on a woven bamboo mat. Her translucent white silk robe moves gently with her rapid shallow breathing, clinging tightly to her glistening wet skin. Dappled afternoon golden sunlight shifts dynamically across her flushed face as leaves sway outside. Her cherry-red lips part slightly in a soft exhale, and a tiny droplet of sweat glslides down her porcelain neck. Classical Chinese gongbi silk painting style, fluid natural movement, cinematic warm lighting, extremely detailed, masterpiece quality, 16:9 aspect ratio.

**【中文译文与镜头解析】**
【运镜】慢速推近特写镜头。【画面动态】[人物描述] 仰卧于竹席上。薄如蝉翼的白丝罗衫随着她急促浅快的呼吸轻轻起伏，紧紧贴在她湿润发亮的肌肤上。斑驳的金色午后阳光随着窗外树叶摇曳在绯红的脸庞上动态晃动。樱桃红唇微张吐出轻喘，一粒细微的汗珠沿瓷白颈项滑落。【风格】古典中国工笔绢本动画风格，流畅自然动势，电影感暖光，极其精致，16:9 比例。

**(若风险等级为 🔴，在此附带 🟡 降级替换镜头说明)**
```
