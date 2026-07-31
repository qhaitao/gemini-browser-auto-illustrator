import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent
IMAGES_DIR = ROOT / 'images'
README_PATH = ROOT / 'README.md'

IMAGE_EXTS = {'.png', '.jpg', '.jpeg', '.webp', '.gif'}


def detect_category(name: str) -> str:
    lower = name.lower()
    if lower.startswith('gemini'):
        return 'Gemini AI 创作'
    if 'handan' in lower:
        return '邯郸梦境'
    if 'mudan' in lower or '牡丹' in lower:
        return '露滴牡丹'
    if 'peach' in lower or '柳绿' in lower or '桃红' in lower:
        return '桃红柳绿'
    if 'moonlight' in lower or 'study' in lower:
        return '书房月影'
    if 'poetry' in lower or lower.startswith('p') and any(ch.isdigit() for ch in lower):
        return '含蓄情致'
    if 'erotic' in lower or '古典' in lower or 'tang' in lower or 'gongbi' in lower:
        return '古典工笔'
    return '其他作品'


def build_readme(images):
    grouped = {}
    for img in images:
        category = detect_category(img.name)
        grouped.setdefault(category, []).append(img)

    order = [
        'Gemini AI 创作',
        '邯郸梦境',
        '露滴牡丹',
        '桃红柳绿',
        '书房月影',
        '含蓄情致',
        '古典工笔',
        '其他作品',
    ]
    sections = []
    for category in order:
        if category in grouped:
            items = sorted(grouped[category], key=lambda p: p.name.lower())
            rows = []
            for i in range(0, len(items), 3):
                chunk = items[i:i+3]
                cells = []
                for item in chunk:
                    rel = item.relative_to(ROOT).as_posix()
                    name = item.name
                    short = name
                    if len(short) > 24:
                        short = short[:21] + '...'
                    cells.append(
                        f'<img src="{rel}" alt="{name}" width="240" /><br><small>{short}</small>'
                    )
                while len(cells) < 3:
                    cells.append('&nbsp;')
                rows.append('| ' + ' | '.join(cells) + ' |')
            table = ['| 图片 | 图片 | 图片 |', '|---|---|---|'] + rows
            sections.append(f'### {category}\n\n' + '\n'.join(table) + '\n')

    return f'''# 🎨 AI 图片库

这是一个适合 GitHub 直接浏览的 Markdown 画廊。点击图片即可查看原图。

## 统计
- 图片总数：{len(images)}
- 分类数：{len(grouped)}
- 仓库位置：`images/`

## 分类浏览

{''.join(sections)}
'''


def main():
    images = []
    for path in sorted(IMAGES_DIR.iterdir()):
        if path.is_file() and path.suffix.lower() in IMAGE_EXTS:
            images.append(path)
    README_PATH.write_text(build_readme(images), encoding='utf-8')


if __name__ == '__main__':
    main()
