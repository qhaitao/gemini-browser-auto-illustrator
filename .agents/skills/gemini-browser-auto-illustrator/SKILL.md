---
name: gemini-browser-auto-illustrator
description: 当用户命令中包含生图或提到配图、画图、生成图片时触发此Skill。自动化高级感生图工作流，若识别到情色、香艳等关键词则跨Skill调用erotic-prompt-generator转译，否则调用aesthetic-prompt-generator。提示词文件保存至D盘AI目录，并通过browser-harness调动Chrome Gemini网页在线生图，禁止使用内置generate_image工具。
---

# Gemini Browser Auto-Illustrator Skill

本 Skill 规定了从**用户文本输入 ➔ 场景分镜拆解 ➔ 关键词识别与跨 Skill 香艳转译 ➔ 提示词文件保存 (D:\AI\image\prompt\) ➔ browser-harness 自动化控制 Gemini 在线生图 ➔ 页面生成监测与 Markdown 排版**的全流程规范。

---

## 触发条件与引擎强制规则（Trigger & Engine Rules）
- **显式触发词**：当用户输入的命令或请求中包含 **`生图`** 关键词时，必须自动触发并执行本 Skill 工作流。
- **隐式触发词**：包含“画图”、“配图”、“生成图片”、“为以下文字配图”等相关表达时触发。
- **强制生图引擎**：所有生图任务**必须且只能使用在 Google 浏览器 (Chrome) 中打开的 Gemini 网页版 (`https://gemini.google.com/app`)**。禁止优先或直接使用本地 API 工具（如 `generate_image`），必须由 `browser-harness` 驱动 Chrome 浏览器在线发送 Prompt 并出图。

---

## 核心工作流（Workflow SOP）

### 1. 文本分析与分镜拆解
- 提取用户文本的核心隐喻、情节高潮与情绪基调。
- 将长文本拆解为 3~4 个具有视觉冲击力与叙事深度的核心场景。

### 2. 智能路由与跨 Skill 组合调用 (Smart Routing & Skill Chaining)

#### 2.1 智能双轨路由协议 (Smart Dual-Track Routing Protocol)
在生成提示词前，**必须检测用户意图类型与特征关键词**：
- **分支 A：香艳/情色领域**（当输入包含`情色`、`色情`、`香艳`、`艳情`、`秘戏`、`春宫`、`解裳`、`娇喘`等）：
  - 自动触发调用 [`erotic-prompt-generator`](file:///D:/AI/image/.agents/skills/erotic-prompt-generator/SKILL.md) 技能，执行安全合规香艳转译。
- **分支 B：非色情/唯美/国风/写实/科幻领域**（当输入为通用生图、风雅、风景、人物纪实、科幻奇幻等）：
  - 自动触发调用 [`aesthetic-prompt-generator`](file:///D:/AI/image/.agents/skills/aesthetic-prompt-generator/SKILL.md) 技能，套用大师级四要素（镜头相机参数、高级感光影、材质渲染、满幅无边框）生成顶级画面提示词。


#### 2.2 香艳转译与过审安全网 (erotic-prompt-generator Integration)
当触发跨 Skill 调用时，必须严格执行以下四步转译：
1. **人物一致性锚点 (Character Consistency Anchors)**：
   - 提取角色面容、体态、发型与服饰，生成固定描述标示 `[Character Anchor]`，确保连环画册全套出图人物高度统一。
2. **五大转译手法应用 (The 5 Erotic Translation Principles)**：
   - **湿纱贴体 (Translucent Silk)**：用 `translucent white silk robe clinging to damp skin` 替代裸体，随呼吸起伏展示肢体线条。
   - **肢体张力特写 (Body Tension)**：用紧抓床柱/竹席（`white-knuckled grip`）、脚趾蜷曲、发丝甩弧、咬唇仰首、汗珠/水滴沿锁骨滑落表现快感与动势。
   - **影子与水影折射 (Shadow & Reflection)**：用纸窗巨影（`rhythmic shadow cast on paper lattice`）与铜盆/水面波纹折射表现动态交合。
   - **器物与温度双关 (Material Metaphors)**：用摇扇、倾倒瓷杯水流、散落花瓣、红丝脚带双关情致。
   - **残妆与事后余韵 (Aftermath & Ruins)**：用眼角晕妆（`kohl smear`）、微喘嘴唇、半遮罗扇表现消魂余韵。
3. **风险评级与自动降级 (Risk Rating & Auto-Downgrade Safety)**：
   - 标注 🟢 **安全级** (远景/氛围)、🟡 **香艳中高风险级** (湿纱贴体/肌理/神态特写) 与 🔴 **高风险拦截级** (直白体态碰撞)。
   - **拦截防护**：对 🔴 高风险画面，**必须自动执行 🟡 降级替换**（如切换为水影波纹/倾倒水流/手部发白抓握特写/纸窗影子律动），确保 100% 顺畅通过 Gemini 生图安全审核。

#### 2.3 大师级视觉四要素（常规场景）
在生成英文 Prompt 时，通用场景必须包含：
- **镜头与相机参数**：指定镜头与光圈（如 `shot on 35mm Leica M10 lens, f/1.4 aperture, cinematic depth of field`）。
- **光影与氛围调色**：指定高级感光影（如 `volumetric lighting, warm tungsten ambient light, deep cyan and amber gold palette`）。
- **渲染器与材质**：指定顶级渲染器与细节（如 `Octane Render, Unreal Engine 5 render, photorealistic textures`）。
- **画面规格**：`award-winning photograph, 8k resolution, 16:9 aspect ratio`。

---

### 3. 提示词文件保存规范、无边框约束与中文文字规约 (Save, Borderless & Chinese Typography Rules)
- **无边框约束（强规则）**：所有提示词必须自动追加无边框约束词：`no borders, borderless, no frame, full bleed image`，确保生成的画面无黑边/白边/相框遮挡。
- **纯净无文字规约（强规则）**：除非用户显式要求在画面中加字（如海报标题、店铺招牌），生图提示词默认必须包含 `no text, no words, clean image without text`，严格禁止画面出现无意义的杂乱字母、乱码或无关文字；仅在用户明确指定加字时才使用中文文字规范。
- **指定存储目录**：所有生成的提示词 Markdown 文件**统一保存至 `D:\AI\image\prompt\`**。
- **命名规范**：`<YYYYMMDD_HHMM>_<题材/风格>_<关键词>_<N>图提示词.md`（例如：`D:\AI\image\prompt\20260731_0926_明代工笔艳情_半榻清风书斋幽会_6图提示词.md`）。日期时间取自生成时的本地时间，格式为年月日_时分。


---

### 4. 固化自动化执行流程 (Standardized Execution Workflow)
Agent **无需在对话中现场编写/拼接临时 Python 代码**，直接通过标准命令运行组件内固化的脚本组件：

```bash
python D:\AI\image\.agents\skills\gemini-browser-auto-illustrator\scripts\run_gemini.py --markdown "D:\AI\image\prompt\<生成的提示词文件名>.md"
```

#### 固化脚本自动具备能力：
1. **自动任务排队互斥锁 (Task Queue Lock)**：内置 `.gemini_runner.lock` 互斥文件锁。若前序生图任务尚未完成，后续任务自动入队轮询等待，待前序任务释放锁后**自动按顺序接替执行**，彻底避免并发打字冲突。
2. **自动提取提示词与无边框补全**：自动解析 Markdown 文件中的英文 Prompt 序列并校验无边框标签（`no borders, borderless, no frame`）。
3. **标签页智能定位**：自动匹配已在 Chrome 打开的 Gemini 标签页（`https://gemini.google.com/app`）。
4. **安全输入与 DOM 监测**：使用 `execCommand` 安全填入文本，监测 `<img>` 节点变动。
5. **异常自动重试**：失败时检索 `Regenerate/重试` 按钮，自动发起重试机制（上限 2 次）。
6. **静置控速**：每张图生成完毕后强制静置 5 秒，确保流式状态稳健。


---

### 5. 纯在线呈现与免下载规范 (No Download & Online Presentation SOP)
- **免下载规则**：生成完成后，**无需将图片提取或下载到本地磁盘**（无需 Canvas 转 DataURL/保存 PNG 到本地）。
- **浏览器驻留**：生成的全套高清大图直接保留在 Chrome 的 Gemini 控制台对话树中供实时浏览。
- **回复交付**：在对话中呈现提示词文件的保存路径、精心排版的文章与 Prompt 序列。


---

## 自动化 Python 执行模板 (含生图监控与重做机制)

```python
import subprocess, os, sys, json, time

env = os.environ.copy()
env['PYTHONIOENCODING'] = 'utf-8:surrogateescape'

code = '''
import sys, time, json

tabs = list_tabs()
gemini_tab = next((t for t in reversed(tabs) if "gemini.google.com" in t.get("url", "")), None)
if not gemini_tab:
    new_tab("https://gemini.google.com/app")
    wait(4)
else:
    tid = gemini_tab.get("targetId") or gemini_tab.get("target_id")
    if tid:
        try: switch_tab(tid)
        except: pass

prompts = [...] 

def get_img_count():
    try:
        res = js("""
        (() => {
            const imgs = Array.from(document.querySelectorAll('img')).filter(img => 
                (img.naturalWidth > 300 || img.width > 300) && 
                (img.src.startsWith('blob:') || img.src.includes('googleusercontent'))
            );
            return imgs.length;
        })()
        """)
        return res if res else 0
    except:
        return 0

def check_and_click_retry():
    try:
        return js("""
        (() => {
            const btn = document.querySelector('button[aria-label*="Regenerate"]') ||
                        document.querySelector('button[aria-label*="重试"]') ||
                        document.querySelector('button[aria-label*="重新生成"]');
            if (btn && !btn.disabled) {
                btn.click();
                return true;
            }
            return false;
        })()
        """)
    except:
        return False

def send_prompt_text(ptext):
    js_code = f"""
    (() => {{
        const el = document.querySelector('div[contenteditable="true"]') || document.querySelector('[role="textbox"]');
        if (el) {{
            el.focus();
            document.execCommand('selectAll', false, null);
            document.execCommand('insertText', false, {json.dumps(ptext)});
            el.dispatchEvent(new Event('input', {{ bubbles: true }}));
            return true;
        }}
        return false;
    }})()
    """
    js(js_code)
    wait(1.5)
    js("""
    (() => {
        const btn = document.querySelector('button[aria-label*="Send"]') || 
                    document.querySelector('button[aria-label*="发送"]') || 
                    document.querySelector('button.send-button') ||
                    document.querySelector('.send-button-container button');
        if (btn && !btn.disabled) {
            btn.click();
            return 'clicked_btn';
        }
        const el = document.querySelector('div[contenteditable="true"]') || document.querySelector('[role="textbox"]');
        if (el) {
            el.dispatchEvent(new KeyboardEvent('keydown', { key: 'Enter', code: 'Enter', keyCode: 13, which: 13, bubbles: true }));
            return 'dispatched_enter';
        }
        return 'not_found';
    })()
    """)

for idx, ptext in enumerate(prompts):
    print(f"--- Sending Prompt {idx + 1}/{len(prompts)} ---")
    current_imgs = get_img_count()
    send_prompt_text(ptext)
    
    # 监控图片生成状态
    success = False
    start_t = time.time()
    while time.time() - start_t < 75:
        wait(4)
        try: js("window.scrollTo(0, document.body.scrollHeight)")
        except: pass
        if get_img_count() > current_imgs:
            success = True
            print("图片生成成功！")
            break
            
    # 若生成失败，触发重做机制 (Regenerate / Retry)
    if not success:
        print("未检测到新图片，触发自动重做机制...")
        for retry in range(2):
            print(f"执行第 {retry + 1} 次重做操作...")
            if check_and_click_retry():
                print("已点击重新生成/重试按钮")
            else:
                send_prompt_text(ptext)
                
            retry_start = time.time()
            while time.time() - retry_start < 75:
                wait(4)
                try: js("window.scrollTo(0, document.body.scrollHeight)")
                except: pass
                if get_img_count() > current_imgs:
                    success = True
                    print("重试重做成功！")
                    break
            if success:
                break
                
    wait(5) # 静置 5 秒
'''

process = subprocess.Popen(
    ['uvx', 'browser-harness'],
    stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
    text=True, encoding='utf-8', errors='replace', env=env
)
```
