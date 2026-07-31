import os
import json
import glob
from datetime import datetime

IMAGE_DIR = r"D:\AI\image\images"
OUTPUT_HTML = r"D:\AI\image\index.html"
OUTPUT_SERVER = r"D:\AI\image\server.py"

def get_category(filename):
    fname = filename.lower()
    if fname.startswith("gemini_generated_image"):
        return "Gemini AI 创作", "gemini", "#8b5cf6"
    elif "handan" in fname:
        return "邯郸梦境系列", "handan", "#ec4899"
    elif "ludi_mudan" in fname:
        return "露滴牡丹系列", "mudan", "#f43f5e"
    elif "peach_willow" in fname:
        return "桃红柳绿系列", "peach", "#10b981"
    elif "study_moonlight" in fname:
        return "书房月影系列", "moonlight", "#3b82f6"
    elif "tang_lady" in fname or "erotic" in fname:
        return "古典工笔插画", "classical", "#eab308"
    elif fname.startswith("p1_") or fname.startswith("p2_") or fname.startswith("p3_") or fname.startswith("p4_") or fname.startswith("p5_"):
        return "含蓄情致系列", "poetry", "#06b6d4"
    else:
        return "其他艺术作品", "other", "#64748b"

files = os.listdir(IMAGE_DIR)
image_files = [f for f in files if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp', '.gif'))]

images_data = []
total_bytes = 0

for fname in sorted(image_files):
    fpath = os.path.join(IMAGE_DIR, fname)
    stat = os.stat(fpath)
    size_bytes = stat.st_size
    total_bytes += size_bytes
    mtime = datetime.fromtimestamp(stat.st_mtime).strftime('%Y-%m-%d %H:%M:%S')
    cat_name, cat_slug, cat_color = get_category(fname)
    
    images_data.append({
        "name": fname,
        "rel_path": f"images/{fname}",
        "abs_path": fpath,
        "size_bytes": size_bytes,
        "size_formatted": f"{size_bytes / (1024*1024):.2f} MB",
        "mtime": mtime,
        "category": cat_name,
        "slug": cat_slug,
        "color": cat_color
    })

print(f"Total images processed: {len(images_data)}, total size: {total_bytes / (1024*1024):.2f} MB")

images_json = json.dumps(images_data, ensure_ascii=False, indent=2)

html_content = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>AI 视觉艺术大 me & 图库画廊 | AI Image Gallery</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
  <style>
    :root {{
      --bg-primary: #090a0f;
      --bg-secondary: #121520;
      --bg-card: rgba(22, 27, 42, 0.65);
      --bg-card-hover: rgba(30, 37, 58, 0.85);
      --border-color: rgba(255, 255, 255, 0.08);
      --border-hover: rgba(139, 92, 246, 0.4);
      --text-main: #f3f4f6;
      --text-muted: #9ca3af;
      --accent-purple: #8b5cf6;
      --accent-pink: #ec4899;
      --accent-cyan: #06b6d4;
      --accent-emerald: #10b981;
      --accent-amber: #f59e0b;
      --glass-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.4);
      --transition-base: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    body {{
      font-family: 'Plus Jakarta Sans', 'Outfit', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      background-color: var(--bg-primary);
      color: var(--text-main);
      min-height: 100vh;
      overflow-x: hidden;
      background-image: 
        radial-gradient(circle at 15% 15%, rgba(139, 92, 246, 0.12) 0%, transparent 40%),
        radial-gradient(circle at 85% 80%, rgba(6, 182, 212, 0.1) 0%, transparent 45%),
        radial-gradient(circle at 50% 50%, rgba(236, 72, 153, 0.05) 0%, transparent 60%);
      background-attachment: fixed;
    }}

    /* Header & Hero */
    header {{
      position: sticky;
      top: 0;
      z-index: 100;
      backdrop-filter: blur(20px);
      -webkit-backdrop-filter: blur(20px);
      background: rgba(9, 10, 15, 0.75);
      border-bottom: 1px solid var(--border-color);
      padding: 1rem 2rem;
    }}

    .header-container {{
      max-width: 1700px;
      margin: 0 auto;
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 1.5rem;
      flex-wrap: wrap;
    }}

    .logo-area {{
      display: flex;
      align-items: center;
      gap: 0.8rem;
    }}

    .logo-badge {{
      width: 42px;
      height: 42px;
      border-radius: 12px;
      background: linear-gradient(135deg, var(--accent-purple), var(--accent-pink));
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.4rem;
      box-shadow: 0 4px 16px rgba(139, 92, 246, 0.4);
    }}

    .logo-title {{
      font-family: 'Outfit', sans-serif;
      font-size: 1.4rem;
      font-weight: 700;
      letter-spacing: -0.02em;
      background: linear-gradient(135deg, #ffffff 30%, #a5b4fc);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }}

    .logo-subtitle {{
      font-size: 0.75rem;
      color: var(--text-muted);
      letter-spacing: 0.05em;
    }}

    /* Stats bar */
    .stats-pills {{
      display: flex;
      align-items: center;
      gap: 1rem;
    }}

    .stat-pill {{
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid var(--border-color);
      padding: 0.4rem 0.9rem;
      border-radius: 30px;
      font-size: 0.82rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
      color: #d1d5db;
    }}

    .stat-pill span {{
      font-weight: 700;
      color: #fff;
    }}

    /* Controls Bar */
    .controls-section {{
      max-width: 1700px;
      margin: 1.5rem auto 0 auto;
      padding: 0 2rem;
      display: flex;
      flex-direction: column;
      gap: 1.2rem;
    }}

    .search-sort-row {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 1rem;
      flex-wrap: wrap;
    }}

    .search-box {{
      position: relative;
      flex: 1;
      min-width: 280px;
      max-width: 500px;
    }}

    .search-box input {{
      width: 100%;
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: 14px;
      padding: 0.75rem 1rem 0.75rem 2.8rem;
      color: #fff;
      font-size: 0.92rem;
      outline: none;
      transition: var(--transition-base);
      backdrop-filter: blur(10px);
    }}

    .search-box input:focus {{
      border-color: var(--accent-purple);
      box-shadow: 0 0 0 3px rgba(139, 92, 246, 0.2);
      background: rgba(26, 32, 50, 0.85);
    }}

    .search-icon {{
      position: absolute;
      left: 1rem;
      top: 50%;
      transform: translateY(-50%);
      color: var(--text-muted);
      font-size: 1.1rem;
      pointer-events: none;
    }}

    .filter-group {{
      display: flex;
      align-items: center;
      gap: 0.8rem;
      flex-wrap: wrap;
    }}

    .category-pills {{
      display: flex;
      gap: 0.5rem;
      flex-wrap: wrap;
      align-items: center;
    }}

    .cat-btn {{
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid var(--border-color);
      color: var(--text-muted);
      padding: 0.45rem 0.95rem;
      border-radius: 20px;
      font-size: 0.83rem;
      cursor: pointer;
      transition: var(--transition-base);
      display: flex;
      align-items: center;
      gap: 0.4rem;
    }}

    .cat-btn:hover {{
      background: rgba(255, 255, 255, 0.09);
      color: var(--text-main);
      border-color: rgba(255, 255, 255, 0.2);
    }}

    .cat-btn.active {{
      background: linear-gradient(135deg, rgba(139, 92, 246, 0.25), rgba(236, 72, 153, 0.25));
      border-color: var(--accent-purple);
      color: #ffffff;
      font-weight: 600;
      box-shadow: 0 2px 12px rgba(139, 92, 246, 0.3);
    }}

    .view-mode-toggle {{
      display: flex;
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid var(--border-color);
      padding: 0.25rem;
      border-radius: 12px;
      gap: 0.25rem;
    }}

    .view-btn {{
      background: transparent;
      border: none;
      color: var(--text-muted);
      padding: 0.4rem 0.7rem;
      border-radius: 8px;
      cursor: pointer;
      transition: var(--transition-base);
      font-size: 0.9rem;
    }}

    .view-btn.active {{
      background: rgba(255, 255, 255, 0.15);
      color: #fff;
    }}

    .sort-select {{
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      color: var(--text-main);
      padding: 0.5rem 0.9rem;
      border-radius: 12px;
      font-size: 0.85rem;
      outline: none;
      cursor: pointer;
    }}

    /* Gallery Grid Layouts */
    main {{
      max-width: 1700px;
      margin: 1.5rem auto 4rem auto;
      padding: 0 2rem;
    }}

    /* Masonry Grid */
    .grid-masonry {{
      column-count: 5;
      column-gap: 1.2rem;
    }}

    @media (max-width: 1500px) {{ .grid-masonry {{ column-count: 4; }} }}
    @media (max-width: 1100px) {{ .grid-masonry {{ column-count: 3; }} }}
    @media (max-width: 768px) {{ .grid-masonry {{ column-count: 2; }} }}
    @media (max-width: 480px) {{ .grid-masonry {{ column-count: 1; }} }}

    .grid-standard {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
      gap: 1.2rem;
    }}

    .grid-list {{
      display: flex;
      flex-direction: column;
      gap: 0.8rem;
    }}

    /* Image Card */
    .img-card {{
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: 16px;
      overflow: hidden;
      margin-bottom: 1.2rem;
      break-inside: avoid;
      transition: var(--transition-base);
      position: relative;
      cursor: pointer;
      backdrop-filter: blur(10px);
    }}

    .grid-standard .img-card {{
      margin-bottom: 0;
      height: 100%;
      display: flex;
      flex-direction: column;
    }}

    .img-card:hover {{
      transform: translateY(-6px) scale(1.01);
      border-color: var(--border-hover);
      box-shadow: var(--glass-shadow), 0 0 20px rgba(139, 92, 246, 0.2);
    }}

    .img-wrapper {{
      width: 100%;
      position: relative;
      overflow: hidden;
      background: #050608;
    }}

    .grid-standard .img-wrapper {{
      height: 240px;
    }}

    .img-card img {{
      width: 100%;
      height: auto;
      display: block;
      transition: transform 0.5s ease;
      object-fit: cover;
    }}

    .grid-standard .img-card img {{
      height: 100%;
    }}

    .img-card:hover img {{
      transform: scale(1.05);
    }}

    .card-badge {{
      position: absolute;
      top: 0.8rem;
      left: 0.8rem;
      background: rgba(0, 0, 0, 0.6);
      backdrop-filter: blur(8px);
      border: 1px solid rgba(255, 255, 255, 0.15);
      color: #fff;
      padding: 0.25rem 0.65rem;
      border-radius: 20px;
      font-size: 0.72rem;
      font-weight: 500;
      z-index: 2;
    }}

    .card-overlay {{
      position: absolute;
      inset: 0;
      background: linear-gradient(to top, rgba(9, 10, 15, 0.85) 0%, transparent 60%);
      opacity: 0;
      transition: opacity 0.3s ease;
      display: flex;
      align-items: flex-end;
      padding: 1rem;
    }}

    .img-card:hover .card-overlay {{
      opacity: 1;
    }}

    .card-info {{
      padding: 0.9rem 1rem;
      background: rgba(15, 18, 28, 0.6);
    }}

    .card-title {{
      font-size: 0.88rem;
      font-weight: 600;
      color: #f3f4f6;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
      margin-bottom: 0.3rem;
    }}

    .card-meta {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 0.75rem;
      color: var(--text-muted);
    }}

    /* List View Specific */
    .grid-list .img-card {{
      display: flex;
      flex-direction: row;
      align-items: center;
      height: 90px;
      margin-bottom: 0;
    }}

    .grid-list .img-wrapper {{
      width: 120px;
      height: 100%;
      flex-shrink: 0;
    }}

    .grid-list .img-card img {{
      height: 100%;
      width: 100%;
      object-fit: cover;
    }}

    .grid-list .card-info {{
      flex: 1;
      display: flex;
      justify-content: space-between;
      align-items: center;
      background: transparent;
      padding: 1rem 1.5rem;
    }}

    .grid-list .card-title {{
      font-size: 1rem;
    }}

    /* Lightbox Modal */
    .modal-backdrop {{
      position: fixed;
      inset: 0;
      background: rgba(4, 5, 8, 0.92);
      backdrop-filter: blur(24px);
      z-index: 1000;
      display: flex;
      opacity: 0;
      pointer-events: none;
      transition: opacity 0.3s ease;
    }}

    .modal-backdrop.active {{
      opacity: 1;
      pointer-events: auto;
    }}

    .modal-container {{
      width: 100%;
      height: 100%;
      display: flex;
      position: relative;
    }}

    .modal-main {{
      flex: 1;
      height: 100%;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      position: relative;
      padding: 2rem;
      overflow: hidden;
    }}

    .modal-img-container {{
      max-width: 90%;
      max-height: 85vh;
      display: flex;
      align-items: center;
      justify-content: center;
      position: relative;
      cursor: grab;
    }}

    .modal-img-container:active {{
      cursor: grabbing;
    }}

    .modal-img {{
      max-width: 100%;
      max-height: 85vh;
      object-fit: contain;
      border-radius: 12px;
      box-shadow: 0 20px 60px rgba(0, 0, 0, 0.8);
      transition: transform 0.1s ease-out;
    }}

    .modal-sidebar {{
      width: 380px;
      background: rgba(14, 18, 28, 0.95);
      border-left: 1px solid var(--border-color);
      padding: 2rem;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      z-index: 10;
      overflow-y: auto;
    }}

    @media (max-width: 900px) {{
      .modal-container {{ flex-direction: column; }}
      .modal-sidebar {{ width: 100%; height: 300px; border-left: none; border-top: 1px solid var(--border-color); }}
    }}

    .sidebar-header {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 1.5rem;
    }}

    .sidebar-title {{
      font-size: 1.1rem;
      font-weight: 700;
      word-break: break-all;
    }}

    .info-group {{
      display: flex;
      flex-direction: column;
      gap: 1.2rem;
    }}

    .info-item {{
      background: rgba(255, 255, 255, 0.03);
      border: 1px solid var(--border-color);
      border-radius: 12px;
      padding: 0.9rem;
    }}

    .info-label {{
      font-size: 0.75rem;
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.05em;
      margin-bottom: 0.3rem;
    }}

    .info-value {{
      font-size: 0.92rem;
      color: #fff;
      font-weight: 500;
      word-break: break-all;
    }}

    .modal-nav-btn {{
      position: absolute;
      top: 50%;
      transform: translateY(-50%);
      background: rgba(255, 255, 255, 0.1);
      border: 1px solid rgba(255, 255, 255, 0.2);
      color: #fff;
      width: 50px;
      height: 50px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.5rem;
      cursor: pointer;
      transition: var(--transition-base);
      z-index: 5;
    }}

    .modal-nav-btn:hover {{
      background: rgba(139, 92, 246, 0.6);
      border-color: var(--accent-purple);
      scale: 1.1;
    }}

    .modal-prev {{ left: 1.5rem; }}
    .modal-next {{ right: 1.5rem; }}

    .modal-close {{
      position: absolute;
      top: 1.5rem;
      right: 1.5rem;
      background: rgba(255, 255, 255, 0.1);
      border: 1px solid rgba(255, 255, 255, 0.2);
      color: #fff;
      width: 40px;
      height: 40px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.2rem;
      cursor: pointer;
      transition: var(--transition-base);
      z-index: 10;
    }}

    .modal-close:hover {{
      background: rgba(239, 68, 68, 0.6);
    }}

    .action-btn {{
      width: 100%;
      background: linear-gradient(135deg, var(--accent-purple), var(--accent-pink));
      border: none;
      color: #fff;
      padding: 0.85rem;
      border-radius: 12px;
      font-weight: 600;
      cursor: pointer;
      transition: var(--transition-base);
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 0.5rem;
      margin-top: 1rem;
    }}

    .action-btn:hover {{
      opacity: 0.9;
      transform: translateY(-2px);
      box-shadow: 0 4px 20px rgba(236, 72, 153, 0.4);
    }}

    .sec-btn {{
      background: rgba(255, 255, 255, 0.08);
      border: 1px solid var(--border-color);
    }}

    .sec-btn:hover {{
      background: rgba(255, 255, 255, 0.15);
      box-shadow: none;
    }}

    /* Empty state */
    .empty-state {{
      text-align: center;
      padding: 5rem 2rem;
      color: var(--text-muted);
    }}

    .empty-icon {{
      font-size: 3rem;
      margin-bottom: 1rem;
    }}
  </style>
</head>
<body>

  <header>
    <div class="header-container">
      <div class="logo-area">
        <div class="logo-badge">🎨</div>
        <div>
          <h1 class="logo-title">AI Image Master Gallery</h1>
          <div class="logo-subtitle">D:\AI\image\images 全高清作品展示图</div>
        </div>
      </div>

      <div class="stats-pills">
        <div class="stat-pill">🖼️ 总图数 <span id="stat-total">{len(images_data)}</span></div>
        <div class="stat-pill">💾 占用容量 <span id="stat-size">{total_bytes / (1024*1024):.1f} MB</span></div>
        <div class="stat-pill">📂 系列分组 <span id="stat-cats">7</span></div>
      </div>
    </div>
  </header>

  <div class="controls-section">
    <div class="search-sort-row">
      <div class="search-box">
        <span class="search-icon">🔍</span>
        <input type="text" id="search-input" placeholder="搜索文件名或标签 (例如: gemini, handan, 牡丹, png)...">
      </div>

      <div style="display: flex; gap: 1rem; align-items: center;">
        <select id="sort-select" class="sort-select">
          <option value="default">默认排序</option>
          <option value="name-asc">文件名 (A - Z)</option>
          <option value="name-desc">文件名 (Z - A)</option>
          <option value="size-desc">文件大小 (从大到小)</option>
          <option value="size-asc">文件大小 (从小到大)</option>
        </select>

        <div class="view-mode-toggle">
          <button class="view-btn active" data-mode="masonry" title="瀑布流视图">🧱 瀑布流</button>
          <button class="view-btn" data-mode="grid" title="标准网格视图">📊 卡片</button>
          <button class="view-btn" data-mode="list" title="列表视图">📄 列表</button>
        </div>
      </div>
    </div>

    <div class="filter-group">
      <div class="category-pills" id="category-pills">
        <button class="cat-btn active" data-slug="all">✨ 全部作品 ({len(images_data)})</button>
        <button class="cat-btn" data-slug="gemini">🎨 Gemini AI</button>
        <button class="cat-btn" data-slug="handan">🌸 邯郸梦境</button>
        <button class="cat-btn" data-slug="mudan">🌺 露滴牡丹</button>
        <button class="cat-btn" data-slug="peach">🌿 桃红柳绿</button>
        <button class="cat-btn" data-slug="moonlight">🌙 书房月影</button>
        <button class="cat-btn" data-slug="classical">🏮 古典工笔</button>
        <button class="cat-btn" data-slug="poetry">📜 含蓄情致</button>
      </div>
    </div>
  </div>

  <main>
    <div id="gallery-grid" class="grid-masonry"></div>
    <div id="empty-state" class="empty-state" style="display: none;">
      <div class="empty-icon">🔍</div>
      <h3>未找到匹配的图片</h3>
      <p style="margin-top: 0.5rem;">请尝试调整搜索关键词或切换标签分类。</p>
    </div>
  </main>

  <!-- Lightbox Modal -->
  <div id="modal" class="modal-backdrop">
    <button class="modal-close" id="modal-close">✕</button>
    <button class="modal-nav-btn modal-prev" id="modal-prev">‹</button>
    <button class="modal-nav-btn modal-next" id="modal-next">›</button>

    <div class="modal-container">
      <div class="modal-main">
        <div class="modal-img-container" id="img-container">
          <img id="modal-img" class="modal-img" src="" alt="Preview">
        </div>
      </div>

      <div class="modal-sidebar">
        <div>
          <div class="sidebar-header">
            <span class="card-badge" id="modal-cat-badge" style="position: static;">分类</span>
            <span style="font-size: 0.8rem; color: var(--text-muted);" id="modal-index-counter">1 / 100</span>
          </div>
          <h2 class="sidebar-title" id="modal-title">图片标题</h2>

          <div class="info-group" style="margin-top: 1.5rem;">
            <div class="info-item">
              <div class="info-label">文件路径</div>
              <div class="info-value" id="modal-path">D:\AI\image\images\...</div>
            </div>
            <div class="info-item">
              <div class="info-label">文件大小</div>
              <div class="info-value" id="modal-size">0 MB</div>
            </div>
            <div class="info-item">
              <div class="info-label">分辨率尺寸</div>
              <div class="info-value" id="modal-dim">加载中...</div>
            </div>
            <div class="info-item">
              <div class="info-label">修改时间</div>
              <div class="info-value" id="modal-mtime">2026-07-31</div>
            </div>
          </div>
        </div>

        <div>
          <button class="action-btn" id="btn-download">
            <span>📥 下载原图</span>
          </button>
          <button class="action-btn sec-btn" id="btn-copy-path">
            <span>📋 复制本地路径</span>
          </button>
        </div>
      </div>
    </div>
  </div>

  <script>
    const IMAGES_DATA = {images_json};
    
    let currentFiltered = [...IMAGES_DATA];
    let currentCategory = 'all';
    let currentSearch = '';
    let currentSort = 'default';
    let currentViewMode = 'masonry';
    let activeModalIndex = 0;

    // DOM Elements
    const galleryGrid = document.getElementById('gallery-grid');
    const emptyState = document.getElementById('empty-state');
    const searchInput = document.getElementById('search-input');
    const sortSelect = document.getElementById('sort-select');
    const categoryPills = document.getElementById('category-pills');
    const statTotal = document.getElementById('stat-total');

    // Render Gallery
    function renderGallery() {{
      // 1. Filter
      currentFiltered = IMAGES_DATA.filter(img => {{
        const matchesCat = currentCategory === 'all' || img.slug === currentCategory;
        const searchLower = currentSearch.toLowerCase();
        const matchesSearch = !currentSearch || 
          img.name.toLowerCase().includes(searchLower) || 
          img.category.toLowerCase().includes(searchLower);
        return matchesCat && matchesSearch;
      }});

      // 2. Sort
      if (currentSort === 'name-asc') {{
        currentFiltered.sort((a, b) => a.name.localeCompare(b.name));
      }} else if (currentSort === 'name-desc') {{
        currentFiltered.sort((a, b) => b.name.localeCompare(a.name));
      }} else if (currentSort === 'size-desc') {{
        currentFiltered.sort((a, b) => b.size_bytes - a.size_bytes);
      }} else if (currentSort === 'size-asc') {{
        currentFiltered.sort((a, b) => a.size_bytes - b.size_bytes);
      }}

      statTotal.textContent = currentFiltered.length;

      if (currentFiltered.length === 0) {{
        galleryGrid.style.display = 'none';
        emptyState.style.display = 'block';
        return;
      }} else {{
        galleryGrid.style.display = currentViewMode === 'masonry' ? 'block' : currentViewMode === 'grid' ? 'grid' : 'flex';
        emptyState.style.display = 'none';
      }}

      galleryGrid.className = `grid-${{currentViewMode}}`;

      galleryGrid.innerHTML = currentFiltered.map((img, index) => `
        <div class="img-card" onclick="openModal(${{index}})">
          <div class="img-wrapper">
            <span class="card-badge" style="border-color: ${{img.color}};">${{img.category}}</span>
            <img src="${{img.rel_path}}" alt="${{img.name}}" loading="lazy">
            <div class="card-overlay">
              <span style="color: #fff; font-size: 0.8rem; font-weight: 600;">🔍 放大预览</span>
            </div>
          </div>
          <div class="card-info">
            <div class="card-title" title="${{img.name}}">${{img.name}}</div>
            <div class="card-meta">
              <span>💾 ${{img.size_formatted}}</span>
              <span>⚡ PNG</span>
            </div>
          </div>
        </div>
      `).join('');
    }}

    // Filter & Event Handlers
    categoryPills.addEventListener('click', (e) => {{
      const btn = e.target.closest('.cat-btn');
      if (!btn) return;
      document.querySelectorAll('.cat-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      currentCategory = btn.dataset.slug;
      renderGallery();
    }});

    searchInput.addEventListener('input', (e) => {{
      currentSearch = e.target.value.trim();
      renderGallery();
    }});

    sortSelect.addEventListener('change', (e) => {{
      currentSort = e.target.value;
      renderGallery();
    }});

    document.querySelectorAll('.view-btn').forEach(btn => {{
      btn.addEventListener('click', () => {{
        document.querySelectorAll('.view-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        currentViewMode = btn.dataset.mode;
        renderGallery();
      }});
    }});

    // Lightbox Modal Logic
    const modal = document.getElementById('modal');
    const modalImg = document.getElementById('modal-img');
    const modalTitle = document.getElementById('modal-title');
    const modalPath = document.getElementById('modal-path');
    const modalSize = document.getElementById('modal-size');
    const modalDim = document.getElementById('modal-dim');
    const modalMtime = document.getElementById('modal-mtime');
    const modalCatBadge = document.getElementById('modal-cat-badge');
    const modalIndexCounter = document.getElementById('modal-index-counter');
    const btnDownload = document.getElementById('btn-download');
    const btnCopyPath = document.getElementById('btn-copy-path');

    function openModal(index) {{
      activeModalIndex = index;
      const imgData = currentFiltered[index];
      if (!imgData) return;

      modalImg.src = imgData.rel_path;
      modalTitle.textContent = imgData.name;
      modalPath.textContent = imgData.abs_path;
      modalSize.textContent = imgData.size_formatted;
      modalMtime.textContent = imgData.mtime;
      modalCatBadge.textContent = imgData.category;
      modalCatBadge.style.borderColor = imgData.color;
      modalIndexCounter.textContent = `${{index + 1}} / ${{currentFiltered.length}}`;

      modalDim.textContent = '计算中...';
      const tempImg = new Image();
      tempImg.src = imgData.rel_path;
      tempImg.onload = () => {{
        modalDim.textContent = `${{tempImg.naturalWidth}} × ${{tempImg.naturalHeight}} px`;
      }};

      modal.classList.add('active');
    }}

    function closeModal() {{
      modal.classList.remove('active');
    }}

    document.getElementById('modal-close').addEventListener('click', closeModal);
    document.getElementById('modal-prev').addEventListener('click', () => {{
      if (activeModalIndex > 0) openModal(activeModalIndex - 1);
      else openModal(currentFiltered.length - 1);
    }});

    document.getElementById('modal-next').addEventListener('click', () => {{
      if (activeModalIndex < currentFiltered.length - 1) openModal(activeModalIndex + 1);
      else openModal(0);
    }});

    document.addEventListener('keydown', (e) => {{
      if (!modal.classList.contains('active')) return;
      if (e.key === 'Escape') closeModal();
      if (e.key === 'ArrowLeft') document.getElementById('modal-prev').click();
      if (e.key === 'ArrowRight') document.getElementById('modal-next').click();
    }});

    btnDownload.addEventListener('click', () => {{
      const imgData = currentFiltered[activeModalIndex];
      const link = document.createElement('a');
      link.href = imgData.rel_path;
      link.download = imgData.name;
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
    }});

    btnCopyPath.addEventListener('click', () => {{
      const imgData = currentFiltered[activeModalIndex];
      navigator.clipboard.writeText(imgData.abs_path).then(() => {{
        alert(`已复制路径到剪贴板:\n${{imgData.abs_path}}`);
      }});
    }});

    // Initialize
    renderGallery();
  </script>
</body>
</html>
'''

with open(OUTPUT_HTML, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"Gallery HTML written successfully to {OUTPUT_HTML}")
