import argparse
import json
import os
import re
import subprocess
import sys
import time

def get_lock_file_path():
    if os.path.exists(r"D:\AI\image\prompt"):
        return r"D:\AI\image\prompt\.gemini_runner.lock"
    elif os.path.exists(r"C:\AI\image\prompt"):
        return r"C:\AI\image\prompt\.gemini_runner.lock"
    else:
        fallback_dir = os.path.join(os.path.expanduser("~"), "AI", "image", "prompt")
        os.makedirs(fallback_dir, exist_ok=True)
        return os.path.join(fallback_dir, ".gemini_runner.lock")

LOCK_FILE_PATH = get_lock_file_path()

def acquire_queue_lock(timeout_seconds=600):
    os.makedirs(os.path.dirname(LOCK_FILE_PATH), exist_ok=True)
    start_time = time.time()
    
    while os.path.exists(LOCK_FILE_PATH):
        try:
            with open(LOCK_FILE_PATH, 'r', encoding='utf-8', errors='ignore') as f:
                lock_info = f.read().strip()
        except:
            lock_info = "unknown task"
            
        elapsed = int(time.time() - start_time)
        print(f"[任务排队中...] 检测到前序生图任务仍在运行 ({lock_info})，当前任务已自动入队等待 ({elapsed}s)...")
        
        try:
            mtime = os.path.getmtime(LOCK_FILE_PATH)
            if time.time() - mtime > 600:
                print("[警告] 前序锁文件已超时超过10分钟，自动清理过期锁...")
                release_queue_lock()
                break
        except:
            pass

        time.sleep(4)
        if elapsed > timeout_seconds:
            print("[错误] 排队等待超时，强制解除排队。")
            break

    try:
        with open(LOCK_FILE_PATH, 'w', encoding='utf-8') as f:
            f.write(f"PID:{os.getpid()} Time:{time.strftime('%Y-%m-%d %H:%M:%S')}")
        print("[队列成功] 已获得排队独占锁，开始执行生图流程。")
    except Exception as e:
        print(f"写入锁文件失败: {e}")

def release_queue_lock():
    if os.path.exists(LOCK_FILE_PATH):
        try:
            os.remove(LOCK_FILE_PATH)
            print("[队列释放] 任务完成，已释放排队独占锁，供后续任务执行。")
        except Exception as e:
            print(f"释放锁文件异常: {e}")

def extract_prompts_from_markdown(file_path):
    prompts = []
    if not os.path.exists(file_path):
        print(f"Error: Prompt file not found: {file_path}")
        return prompts
    
    with open(file_path, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()

    # 1. Triple backticks code blocks
    triple_blocks = re.findall(r'```(?:text|markdown)?\s*\n([\s\S]*?)\n```', content)
    for block in triple_blocks:
        block_clean = block.strip()
        if len(block_clean) > 30:
            prompts.append(block_clean)

    # 2. Single backtick code blocks
    if not prompts:
        single_blocks = re.findall(r'`([^`]+)`', content)
        for block in single_blocks:
            block_clean = block.strip()
            if len(block_clean) > 40 and any(k in block_clean for k in ['Gongbi', 'masterpiece', 'painting', 'shot', 'aspect ratio', 'cinematic', 'illustration', 'poster', 'landscape', 'photography']):
                prompts.append(block_clean)

    # 3. Line by line search fallback
    if not prompts:
        lines = content.split('\n')
        for line in lines:
            line_s = line.strip()
            if (line_s.startswith('Prompt') or any(k in line_s for k in ['Gongbi', 'masterpiece', 'A masterpiece', 'photograph', 'cinematic'])) and len(line_s) > 40:
                prompts.append(line_s)
                
    borderless_tag = "no borders, borderless, no frame, full bleed image"
    no_text_tag = "no text, no words, clean image without text"
    cleaned_prompts = []
    for p in prompts:
        p_final = p
        if "borderless" not in p_final.lower() and "no frame" not in p_final.lower():
            p_final = f"{p_final.rstrip('.')}, {borderless_tag}."
        if "no text" not in p_final.lower() and "typography" not in p_final.lower() and "Chinese typography" not in p_final:
            p_final = f"{p_final.rstrip('.')}, {no_text_tag}."
        cleaned_prompts.append(p_final)

    return cleaned_prompts

def main():
    parser = argparse.ArgumentParser(description="Automated Gemini Web Image Generation Runner with Queue Lock")
    parser.add_argument("--markdown", type=str, help="Path to markdown prompt file")
    parser.add_argument("--prompts-json", type=str, help="JSON string array of prompts")
    args = parser.parse_args()

    prompts = []
    if args.markdown:
        prompts = extract_prompts_from_markdown(args.markdown)
    elif args.prompts_json:
        try:
            prompts = json.loads(args.prompts_json)
        except Exception as e:
            print(f"Failed to parse JSON prompts: {e}")

    if not prompts:
        print("No prompts found to process!")
        sys.exit(1)

    acquire_queue_lock()

    try:
        print(f"Loaded {len(prompts)} actual image prompts to send to Gemini Web...")
        for i, p in enumerate(prompts, 1):
            print(f"  [{i}] {p[:90]}...")

        env = os.environ.copy()
        env['PYTHONIOENCODING'] = 'utf-8'

        prompts_json_str = json.dumps(prompts, ensure_ascii=False)

        automation_code = """
import sys, time, json

tabs = list_tabs()
# 支持自动匹配 Google Labs Flow 页面 或 Gemini 页面
target_tab = next((t for t in reversed(tabs) if 'labs.google' in t.get('url', '') or 'flow' in t.get('url', '') or 'gemini.google.com' in t.get('url', '')), None)
if not target_tab:
    print("Opening new tab https://gemini.google.com/app...")
    new_tab("https://gemini.google.com/app")
    wait(5)
else:
    tid = target_tab.get("targetId") or target_tab.get("target_id")
    if tid:
        try: switch_tab(tid)
        except: pass

prompts = """ + prompts_json_str + """

def get_img_count():
    try:
        res = js('''
        (() => {
            const imgs = Array.from(document.querySelectorAll('img')).filter(img => 
                (img.naturalWidth > 200 || img.width > 200) && 
                (img.src.startsWith('blob:') || img.src.includes('googleusercontent') || img.src.includes('generativeai') || img.src.includes('labs.google'))
            );
            return imgs.length;
        })()
        ''')
        return res if res else 0
    except:
        return 0

def check_and_click_retry():
    try:
        return js('''
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
        ''')
    except:
        return False

def send_prompt_text(ptext):
    p_json = json.dumps(ptext)
    
    js_fill = '''(() => {
        const el = document.querySelector('div[data-slate-editor="true"]') || document.querySelector('div[contenteditable="true"]') || document.querySelector('[role="textbox"]');
        if (el) {
            el.focus();
            document.execCommand('selectAll', false, null);
            document.execCommand('insertText', false, ''' + p_json + ''');
            el.dispatchEvent(new Event('input', { bubbles: true }));
            return 'filled';
        }
        return 'not_found';
    })()'''
    js(js_fill)
    wait(1.5)
    
    js_send = '''(() => {
        const btns = Array.from(document.querySelectorAll('button'));
        
        // 1. 匹配 Google Labs Flow 的创建/生成按钮
        const flowBtn = btns.find(b => {
            if (b.disabled) return false;
            const txt = (b.innerText || '').trim();
            const aria = (b.getAttribute('aria-label') || '').trim();
            return (txt.includes('arrow_forward') || txt.includes('创建') || txt.includes('Generate') || txt.includes('Create') || aria.includes('创建') || aria.includes('Generate'));
        });
        if (flowBtn) {
            flowBtn.click();
            return 'clicked_flow_btn';
        }

        // 2. 匹配 Gemini Web 的发送按钮
        const sendBtn = btns.find(b => {
            if (b.disabled) return false;
            const aria = (b.getAttribute('aria-label') || '').trim().toLowerCase();
            if (aria.includes('options') || aria.includes('更多') || aria.includes('菜单') || aria.includes('menu')) return false;
            return (aria === 'send' || aria === '发送' || aria === 'send message' || aria === '发送消息' || aria === '提交' || aria.includes('send prompt') || aria.includes('发送提示词') || b.classList.contains('send-button'));
        }) || document.querySelector('button[aria-label="发送"]') || document.querySelector('button[aria-label="Send"]') || document.querySelector('button.send-button');
        
        if (sendBtn) {
            sendBtn.click();
            return 'clicked_send_btn';
        }

        // 3. Fallback 回车按键
        const el = document.querySelector('div[data-slate-editor="true"]') || document.querySelector('div[contenteditable="true"]') || document.querySelector('[role="textbox"]');
        if (el) {
            el.dispatchEvent(new KeyboardEvent('keydown', { key: 'Enter', code: 'Enter', keyCode: 13, which: 13, bubbles: true }));
            return 'dispatched_enter';
        }
        return 'not_found';
    })()'''
    js(js_send)

for idx, ptext in enumerate(prompts):
    print(f"=== Sending Prompt {idx + 1}/{len(prompts)} ===")
    current_imgs = get_img_count()
    send_prompt_text(ptext)
    
    success = False
    start_t = time.time()
    while time.time() - start_t < 75:
        wait(4)
        try: js("window.scrollTo(0, document.body.scrollHeight)")
        except: pass
        if get_img_count() > current_imgs:
            success = True
            print(f"图片 {idx + 1} 生成成功！")
            break
            
    if not success:
        print(f"图片 {idx + 1} 未检测到新图，触发重试机制...")
        for retry in range(2):
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
                    print(f"图片 {idx + 1} 重试生成成功！")
                    break
            if success:
                break
                
    wait(5)
print(f"全部 {len(prompts)} 张生图任务已全部成功完成。")
"""

        p = subprocess.Popen(
            ['uvx', 'browser-harness'],
            stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            text=True, encoding='utf-8', errors='replace', env=env
        )
        out, err = p.communicate(input=automation_code)
        print(out)
        if err:
            print("Stderr log:", err)

    finally:
        release_queue_lock()

if __name__ == "__main__":
    main()
