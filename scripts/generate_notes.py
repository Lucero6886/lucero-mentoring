#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sinh implementation-notes.html từ implementation-notes.md.

Vì sao cần: tài liệu hệ thống trước đây tồn tại ở hai bản — một `.md` và một `.html`
soạn tay — và chúng đã lệch nhau. Bản `.html` còn ghi phiên bản 1.4.0 khi bản `.md`
đã ở 1.5.1. Đó đúng là lỗi mà cả hệ thống này tồn tại để chống.

Từ nay: **`.md` là bản gốc, `.html` là bản sinh.** Sửa nội dung thì sửa `.md` rồi
chạy lại script này. Trang HTML dùng chung phong cách với hai trang web trong
`docs/` (qua `scripts/site_style.py`) nên cả ba trông như một hệ thống.

Cách dùng (từ thư mục gốc dự án):
    python3 scripts/generate_notes.py

Yêu cầu: pandoc có trong PATH.
"""
import html, pathlib, re, shutil, subprocess, sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from site_style import CSS, FONTS, REPO

BASE = pathlib.Path(__file__).resolve().parents[1]
SRC = BASE / "implementation-notes.md"
DST = BASE / "implementation-notes.html"

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


def main():
    if not shutil.which("pandoc"):
        print("LỖI: không tìm thấy pandoc trong PATH. Cài pandoc rồi chạy lại.")
        return 1
    if not SRC.is_file():
        print(f"LỖI: thiếu bản gốc {SRC.name}")
        return 1

    body = subprocess.run(
        ["pandoc", str(SRC), "-f", "gfm", "-t", "html5", "--wrap=none"],
        capture_output=True, text=True, encoding="utf-8", check=True).stdout

    # bảng rộng phải cuộn được trên điện thoại thay vì làm tràn cả trang
    body = re.sub(r"<table>", '<div class="tablewrap"><table>', body)
    body = re.sub(r"</table>", "</table></div>", body)

    # link tới file .md trong kho → trỏ sang GitHub để bấm được từ trang HTML
    def fix(m):
        href = m.group(1)
        if href.startswith(("http", "#", "mailto:")):
            return m.group(0)
        return f'href="{REPO}/blob/main/{href}"'
    body = re.sub(r'href="([^"]+)"', fix, body)

    # mục lục sinh từ các tiêu đề cấp 2
    heads = re.findall(r'<h2 id="([^"]+)">(.*?)</h2>', body, re.S)
    toc = "".join(f'<li><a href="#{i}">{re.sub(r"<[^>]+>", "", t).strip()}</a></li>'
                  for i, t in heads)
    toc_block = f'<div class="toc"><b>Mục lục</b><ul>{toc}</ul></div>'
    # đặt mục lục ngay trước phần thân, sau tiêu đề và bảng "đọc theo nhu cầu"
    if "<hr />" in body:
        body = body.replace("<hr />", toc_block + "\n<hr />", 1)
    else:
        body = toc_block + body

    title = "Tài liệu hệ thống — Mentoring Lucero"
    ver = (BASE / "VERSION").read_text(encoding="utf-8").strip() if (BASE / "VERSION").is_file() else ""
    page = f"""<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{html.escape(title)}</title>
{FONTS}
<style>{CSS}{DOC_CSS}</style>
</head>
<body>
<nav class="topnav"><div class="wrap">
  <span class="logo">Mentoring Lucero · EEE</span>
  <a href="docs/index.html">Danh mục</a>
  <a href="docs/guide.html">Hướng dẫn chọn đề tài</a>
  <a href="{REPO}">GitHub</a>
</div></nav>
<main class="wrap doc">
{body}
<hr>
<p class="meta">Bản HTML này <b>sinh tự động</b> từ <code>implementation-notes.md</code> bằng
<code>scripts/generate_notes.py</code> — sửa nội dung thì sửa bản Markdown rồi chạy lại script.
Phiên bản hệ thống {html.escape(ver)}.</p>
</main>
</body>
</html>"""
    DST.write_text(page, encoding="utf-8")
    print(f"implementation-notes.html ({len(page)//1024} KB) — {len(heads)} mục, "
          f"{body.count('<table>')} bảng")
    return 0


if __name__ == "__main__":
    sys.exit(main())
