#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sinh 00_START_HERE/FILE_MANIFEST.md từ chính cây thư mục thật.

Vì sao cần: bản manifest trước đây viết tay, và sau vài phiên bản nó liệt kê những
file đã bị xóa trong khi bỏ sót cả một lớp tài liệu mới. Một danh mục file viết tay
luôn thua cây thư mục thật — nên từ nay nó được **sinh ra**.

Phần duy nhất viết tay là *mục đích* của mỗi thư mục (dict PURPOSE bên dưới): máy
đếm được file, nhưng không biết thư mục đó tồn tại để làm gì.

Cách dùng (từ thư mục gốc dự án):
    python3 scripts/generate_manifest.py
"""
import json, pathlib, sys

BASE = pathlib.Path(__file__).resolve().parents[1]
DST = BASE / "00_START_HERE" / "FILE_MANIFEST.md"

SIG = ("**Engineering & Research Mentoring Program (Lucero)** · "
       "ThS. Đinh Văn Nam (Mr. Lucero Dinh) — Khoa Điện–Điện tử, Trường Kỹ thuật, Đại học Phenikaa")

# thư mục → (mục đích, có phải bản sinh tự động không)
PURPOSE = [
    ("06_Data", "**NGUỒN CHUẨN DUY NHẤT.** Danh mục đề tài, lớp thực thi, cửa kiểm soát, thang sẵn sàng, dữ liệu từng khóa.", False),
    ("scripts", "Kiểm tra tính nhất quán và sinh toàn bộ tài liệu dẫn xuất từ nguồn chuẩn.", False),
    ("00_START_HERE", "Điểm vào: lịch sử thay đổi, bản đồ file, lộ trình triển khai.", False),
    ("01_Governance", "Chính sách gốc. Bản `.docx` là gốc dùng để in và ký; bản `.md` cạnh nó là bản sinh.", False),
    ("02_Project_Portfolio", "Danh mục theo loại hoạt động, trang hướng dẫn từng đề tài, hồ sơ thực thi chiều sâu.", True),
    ("03_Operations", "Quy trình vận hành, checklist tuần, thang chấm, định nghĩa \"xong\", workbook theo dõi.", False),
    ("04_Project_Template", "Biểu mẫu hồ sơ dự án của từng sinh viên và bộ khởi tạo repo.", False),
    ("07_Private", "Dữ liệu cá nhân sinh viên. **Bị `.gitignore` chặn — không bao giờ lên kho công khai.**", False),
    ("09_References", "Tài liệu nền theo hướng nghiên cứu và các đề xuất đang cân nhắc.", False),
    ("10_Documentation", "Hướng dẫn theo vai trò: sinh viên, mentor, vận hành, GitHub, track nghiên cứu.", False),
    ("docs", "Trang web công khai (GitHub Pages).", True),
    ("tests", "Bài diễn tập toàn quy trình, dùng để kiểm hệ thống trước mỗi phát hành.", False),
    ("05_Claude", "Prompt và ngữ cảnh cho các phiên làm việc với AI.", False),
    ("99_Archive", "Bản cũ đã ngừng dùng, giữ lại để tra cứu. Không phải nguồn chuẩn.", False),
]

# file ở gốc → mô tả ngắn
ROOT = {
    "README.md": "Trang bìa của kho — điểm vào cho sinh viên và đồng nghiệp.",
    "implementation-notes.md": "**Tài liệu hệ thống cho người vận hành** — từ bản chất tới triển khai.",
    "implementation-notes.html": "Bản web của tài liệu trên (sinh tự động).",
    "CLAUDE.md": "Ràng buộc cho các phiên làm việc với AI.",
    "CONTRIBUTING.md": "Cách góp ý, đề xuất đề tài, báo lỗi tài liệu.",
    "LICENSE": "CC BY-NC-SA 4.0 cho tài liệu · MIT cho mã nguồn.",
    "CITATION.cff": "Thông tin trích dẫn kho (nút *Cite this repository* trên GitHub).",
    "VERSION": "Phiên bản hệ thống — nguồn chuẩn cho mọi nhãn phiên bản.",
    "Ban_do_de_tai.md": "Bản đồ đề tài kể chuyện, dành cho người mới (sinh tự động).",
    "Ban_do_de_tai.html": "Bản web của bản đồ đề tài (sinh tự động).",
    "index.html": "Chuyển hướng sang `docs/index.html` — lưới an toàn cho cấu hình GitHub Pages.",
    "guide.html": "Chuyển hướng sang `docs/guide.html` — lưới an toàn cho cấu hình GitHub Pages.",
}

SKIP_DIRS = {".git", "build", "dist", "_to_delete", "lucero-mentoring", "__pycache__", ".github"}


def count(p, pattern="*"):
    return sum(1 for f in p.rglob(pattern) if f.is_file() and not (set(f.parts) & SKIP_DIRS))


def listing(d, limit=24):
    """Liệt kê file trực tiếp trong thư mục; thư mục con chỉ ghi số lượng."""
    files = sorted(f for f in d.iterdir() if f.is_file() and f.name not in (".nojekyll",))
    subs = sorted(x for x in d.iterdir() if x.is_dir() and x.name not in SKIP_DIRS)
    out = []
    if len(files) <= limit:
        out += [f"`{f.name}`" for f in files]
    else:
        exts = {}
        for f in files:
            exts[f.suffix or "(không đuôi)"] = exts.get(f.suffix or "(không đuôi)", 0) + 1
        out += [f"{n} file `{e}`" for e, n in sorted(exts.items(), key=lambda kv: -kv[1])]
    for s in subs:
        out.append(f"`{s.name}/` — {count(s, '*')} file")
    return out


def main():
    ver = (BASE / "VERSION").read_text(encoding="utf-8").strip()
    port = json.loads((BASE / "06_Data" / "project_portfolio.json").read_text(encoding="utf-8"))
    upd = port["meta"]["updated"]

    rows = []
    for name, purpose, gen in PURPOSE:
        d = BASE / name
        if not d.is_dir():
            continue
        tag = " · **bản sinh tự động**" if gen else ""
        rows.append(f"\n### `{name}/` — {count(d)} file{tag}\n\n{purpose}\n")
        rows.append("- " + "\n- ".join(listing(d)))

    root_files = sorted(f.name for f in BASE.iterdir()
                        if f.is_file() and not f.name.startswith(".")
                        and f.suffix in (".md", ".html", ".docx", ".pdf", ".cff", "") and f.name != "VERSION")
    root_rows = []
    for f in ["README.md", "implementation-notes.md", "implementation-notes.html", "VERSION",
              "CLAUDE.md", "CONTRIBUTING.md", "LICENSE", "CITATION.cff",
              "Ban_do_de_tai.md", "Ban_do_de_tai.html", "index.html", "guide.html"]:
        if (BASE / f).is_file():
            root_rows.append(f"| `{f}` | {ROOT.get(f, '')} |")
    extra = sorted(f for f in root_files if f not in ROOT and f != "VERSION")
    for f in extra:
        root_rows.append(f"| `{f}` | — |")

    total = sum(count(BASE / n) for n, _, _ in PURPOSE if (BASE / n).is_dir())
    body = f"""# Bản đồ file — toàn bộ kho

{SIG}
Phiên bản hệ thống **{ver}** · cập nhật **{upd}**

> **File này sinh tự động** từ chính cây thư mục bằng `scripts/generate_manifest.py`.
> Sửa tay sẽ bị ghi đè. Bản viết tay trước đây đã liệt kê file đã xóa và bỏ sót cả một
> lớp tài liệu mới — đó là lý do nó được chuyển sang sinh tự động.

Kho có **{total} file** trong {len([1 for n, _, _ in PURPOSE if (BASE / n).is_dir()])} thư mục chính.

## Quy tắc đọc bản đồ này

- Thư mục đánh dấu **bản sinh tự động** chứa file bị ghi đè mỗi lần chạy script — đừng sửa tay.
- Muốn biết *vì sao* mỗi thư mục tồn tại và sửa ở đâu thì an toàn, đọc
  [`implementation-notes.md`](../implementation-notes.md) §3 và §5.

## File ở thư mục gốc

| File | Là gì |
|---|---|
{chr(10).join(root_rows)}

## Thư mục
{chr(10).join(rows)}

---

*Lịch sử thay đổi: [`CHANGELOG.md`](CHANGELOG.md) · Tài liệu hệ thống: [`implementation-notes.md`](../implementation-notes.md)*
"""
    DST.write_text(body, encoding="utf-8")
    print(f"00_START_HERE/FILE_MANIFEST.md — {total} file trong "
          f"{len([1 for n, _, _ in PURPOSE if (BASE / n).is_dir()])} thư mục")
    return 0


if __name__ == "__main__":
    sys.exit(main())
