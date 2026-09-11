#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sinh bản `.html` cho các tài liệu viết tay dạng Markdown.

Vì sao cần: tài liệu hệ thống trước đây tồn tại ở hai bản — một `.md` và một `.html`
soạn tay — và chúng đã lệch nhau. Bản `.html` còn ghi phiên bản 1.4.0 khi bản `.md`
đã ở 1.5.1. Đó đúng là lỗi mà cả hệ thống này tồn tại để chống.

Từ nay: **`.md` là bản gốc, `.html` là bản sinh.** Sửa nội dung thì sửa `.md` rồi
chạy lại script này. Trang HTML dùng chung phong cách với hai trang web trong
`docs/` (qua `scripts/site_style.py`) nên cả bộ trông như một hệ thống.

Danh sách tài liệu nằm ở `DOCS` bên dưới. Thêm một tài liệu mới thì thêm một dòng,
không phải viết thêm script — và nhớ ghi file `.html` mới vào:
  · `implementation-notes.md` §5.3 (bảng bản sinh)
  · `CLAUDE.md` §3 (danh sách file không sửa tay)

Cách dùng (từ thư mục gốc dự án):
    python3 scripts/generate_notes.py

Yêu cầu: pandoc có trong PATH.
"""
import html, pathlib, posixpath, re, shutil, subprocess, sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from site_style import CSS, FONTS, REPO

BASE = pathlib.Path(__file__).resolve().parents[1]

# src (tương đối gốc dự án) · tiêu đề trang · cấp tiêu đề đưa vào mục lục
DOCS = [
    {"src": "implementation-notes.md",
     "title": "Tài liệu hệ thống — Mentoring Lucero",
     "toc_levels": (2,)},
    {"src": "10_Documentation/SETUP-GUIDE.md",
     "title": "Dựng môi trường làm việc — Mentoring Lucero",
     "toc_levels": (1, 2)},
    {"src": "10_Documentation/GITHUB-WORKFLOW.md",
     "title": "Vận hành trên GitHub — Lucero Mentoring",
     "toc_levels": (2,)},
]

DOC_CSS = """
.wrap{max-width:900px}
.doc h2{scroll-margin-top:64px}
.doc h3{scroll-margin-top:64px}
.doc>p:first-of-type{font-size:16.5px}
.toc{background:var(--surface);border:1px solid var(--line);border-radius:10px;padding:16px 20px;margin:26px 0}
.toc b{font-family:var(--display);font-size:14px;display:block;margin-bottom:8px}
.toc ul{columns:2;column-gap:28px;margin:0;padding:0;list-style:none;font-size:14px}
@media(max-width:640px){.toc ul{columns:1}}
.toc li{margin:3px 0;break-inside:avoid}
.toc li.lv1{margin-top:10px}
.toc li.lv1 a{font-weight:600}
.doc pre{background:var(--surface-2);border:1px solid var(--line);border-radius:8px;
         padding:14px 16px;overflow-x:auto;font-size:12.5px;line-height:1.55;margin:14px 0}
.doc pre code{background:none;padding:0;font-size:inherit}
.doc blockquote{margin:16px 0;padding:12px 18px;background:var(--accent-soft);
                border-left:3px solid var(--accent);border-radius:0 8px 8px 0}
.doc blockquote p{margin:.3em 0}
.doc table{margin:16px 0}
.doc td,.doc th{vertical-align:top}
.doc hr{border:none;border-top:1px solid var(--line);margin:34px 0}
.doc h2{margin-top:38px}
.doc ul,.doc ol{padding-left:22px;margin:10px 0}
.doc li{margin:5px 0}
.tablewrap{overflow-x:auto}
"""


def build(doc, ver):
    """Dựng một trang. Trả về (đường-dẫn-ghi, số-mục-lục, số-bảng) hoặc None nếu thiếu nguồn."""
    src = BASE / doc["src"]
    if not src.is_file():
        print(f"  ! bỏ qua {doc['src']} — không có file")
        return None
    dst = src.with_suffix(".html")

    # thư mục của tài liệu so với gốc dự án: "" với file ở gốc, "10_Documentation" với file con
    subdir = posixpath.dirname(doc["src"])
    up = "../" * len(subdir.split("/")) if subdir else ""

    body = subprocess.run(
        ["pandoc", str(src), "-f", "gfm", "-t", "html5", "--wrap=none"],
        capture_output=True, text=True, encoding="utf-8", check=True).stdout

    # bảng rộng phải cuộn được trên điện thoại thay vì làm tràn cả trang
    body = re.sub(r"<table>", '<div class="tablewrap"><table>', body)
    body = re.sub(r"</table>", "</table></div>", body)

    # link tới file trong kho → trỏ sang GitHub để bấm được từ trang HTML.
    # Link trong .md là tương đối so với CHÍNH file .md đó, nên phải quy về gốc dự án trước.
    def fix(m):
        href = m.group(1)
        if href.startswith(("http", "#", "mailto:")):
            return m.group(0)
        frag = ""
        if "#" in href:
            href, frag = href.split("#", 1)
            frag = "#" + frag
        rel = posixpath.normpath(posixpath.join(subdir, href)) if subdir else posixpath.normpath(href)
        return f'href="{REPO}/blob/main/{rel}{frag}"'
    body = re.sub(r'href="([^"]+)"', fix, body)

    # mục lục sinh từ tiêu đề, giữ đúng thứ tự trong tài liệu
    lv = "".join(str(n) for n in doc["toc_levels"])
    heads = re.findall(rf'<h([{lv}]) id="([^"]+)">(.*?)</h[{lv}]>', body, re.S)
    # tiêu đề cấp 1 đầu tiên chính là tên tài liệu — đã in ở đầu trang, không nhắc lại trong mục lục
    if heads and heads[0][0] == "1":
        heads = heads[1:]
    toc = "".join(
        f'<li class="lv{n}"><a href="#{i}">{re.sub(r"<[^>]+>", "", t).strip()}</a></li>'
        for n, i, t in heads)
    toc_block = f'<div class="toc"><b>Mục lục</b><ul>{toc}</ul></div>'
    # đặt mục lục ngay trước phần thân, sau tiêu đề và bảng dẫn nhập
    if "<hr />" in body:
        body = body.replace("<hr />", toc_block + "\n<hr />", 1)
    else:
        body = toc_block + body

    page = f"""<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{html.escape(doc["title"])}</title>
{FONTS}
<style>{CSS}{DOC_CSS}</style>
</head>
<body>
<nav class="topnav"><div class="wrap">
  <span class="logo">Mentoring Lucero · EEE</span>
  <a href="{up}docs/index.html">Danh mục</a>
  <a href="{up}docs/guide.html">Hướng dẫn chọn đề tài</a>
  <a href="{REPO}">GitHub</a>
</div></nav>
<main class="wrap doc">
{body}
<hr>
<p class="meta">Bản HTML này <b>sinh tự động</b> từ <code>{html.escape(posixpath.basename(doc["src"]))}</code> bằng
<code>scripts/generate_notes.py</code> — sửa nội dung thì sửa bản Markdown rồi chạy lại script.
Phiên bản hệ thống {html.escape(ver)}.</p>
</main>
</body>
</html>"""
    dst.write_text(page, encoding="utf-8")
    return dst, len(heads), body.count("<table>"), len(page)


def main():
    if not shutil.which("pandoc"):
        print("LỖI: không tìm thấy pandoc trong PATH. Cài pandoc rồi chạy lại.")
        return 1

    ver = (BASE / "VERSION").read_text(encoding="utf-8").strip() if (BASE / "VERSION").is_file() else ""
    made = 0
    for doc in DOCS:
        out = build(doc, ver)
        if not out:
            continue
        dst, nheads, ntables, nbytes = out
        made += 1
        print(f"  {dst.relative_to(BASE)} ({nbytes // 1024} KB) — {nheads} mục, {ntables} bảng")

    if not made:
        print("LỖI: không sinh được tài liệu nào — kiểm lại danh sách DOCS.")
        return 1
    print(f"{made}/{len(DOCS)} tài liệu đã sinh.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
