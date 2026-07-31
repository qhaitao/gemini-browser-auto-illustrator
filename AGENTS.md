# 生图指令强制路由规则 (Image Generation Mandatory Routing Rule)

当用户请求中包含以下任意关键词时：「生图」「画图」「配图」「生成图片」「出图」「绘图」

**必须执行以下操作，不得跳过任何步骤：**

1. **【绝对禁止】** 直接调用内置 `generate_image` 工具！此工具仅用于非生图场景的辅助图片生成（如 UI 设计稿）。
2. **【强制第一步】** 立即读取并执行 Skill 文件：
   `D:\AI\image\.agents\skills\gemini-browser-auto-illustrator\SKILL.md`
3. **按照该 Skill 的完整 SOP 工作流执行**：生成提示词 → 保存到 `D:\AI\image\prompt\` → 运行 `run_gemini.py` 驱动 Chrome 浏览器在 Gemini 网页端在线生图。

这是一条不可覆盖的硬性规则 (non-negotiable hard rule)。任何情况下不得绕过。
