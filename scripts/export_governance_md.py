#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sinh bản Markdown đọc-được-trên-web từ các tài liệu chính sách .docx.

Vì sao cần: GitHub không hiển thị nội dung file .docx — người đọc phải tải về
mới xem được. Bản .md sinh ra ở đây hiện ngay trên trang repo, nên sinh viên
và đồng nghiệp đọc được chính sách mà không cần tải gì.

Nguyên tắc: **.docx là bản gốc** (dùng để in, ký, nộp); **.md là view sinh
tự động** — không sửa tay. Sửa nội dung thì sửa .docx rồi chạy lại script này.

Cách dùng (từ thư mục gốc dự án):
    python3 scripts/export_governance_md.py

Yêu cầu: pandoc có trong PATH.
"""
import pathlib, re, shutil, subprocess, sys

BASE = pathlib.Path(__file__).resolve().parents[1]

# (đường dẫn .docx, tiêu đề hiển thị)
DOCS = [
    ("01_Governance/Master_Mentoring_Handbook.docx",            "Sổ tay quản trị chương trình mentoring"),
    ("01_Governance/Mentor_Student_Working_Agreement.docx",     "Thỏa thuận làm việc giữa mentor và sinh viên"),
    ("01_Governance/AI_and_Academic_Integrity_Policy.docx",     "Quy tắc sử dụng AI và liêm chính học thuật"),
    ("01_Governance/Cohort_HK1_2026_2027_Implementation_Guide.docx", "Hướng dẫn triển khai cohort HK1 2026-2027"),
    ("03_Operations/Mentoring_Operating_Procedure_SOP.docx",    "Quy trình vận hành mentoring (SOP)"),
    ("03_Operations/Weekly_Report_and_Meeting_Template.docx",   "Mẫu báo cáo tuần và biên bản buổi gặp"),
]

GEN_NOTE = ("> **File này được sinh tự động** từ `{src}` bằng `scripts/export_governance_md.py`.\n"
            "> Bản `.docx` là bản gốc dùng để in, ký và nộp — **mọi chỉnh sửa nội dung phải làm trên `.docx`**,\n"
            "> rồi chạy lại script để cập nhật bản này. Sửa tay file `.md` sẽ bị ghi đè ở lần sinh sau.\n")


def tidy(md: str) -> str:
    """Dọn các dấu vết chuyển đổi để bản Markdown đọc tự nhiên."""
    # Mũi tên: pandoc thoát thành '-\>'
    md = md.replace(r"-\>", "→").replace("->", "→")
    # Bảng một ô (hộp nhấn mạnh trong Word) → trích dẫn cho dễ đọc
    def unbox(m):
        text = m.group(1).strip()
        text = re.sub(r"\s+", " ", text)
        return "> " + text + "\n"
    md = re.sub(r"^\|([^|\n]+)\|\n\|[-: ]+\|\n", unbox, md, flags=re.M)
    # Hạ một bậc tiêu đề: tiêu đề tài liệu ở trên đã là H1
    md = re.sub(r"^(#{1,5}) ", r"#\1 ", md, flags=re.M)
    # Bỏ dòng trắng thừa liên tiếp
    md = re.sub(r"\n{3,}", "\n\n", md)
    return md.strip() + "\n"


def main() -> int:
    if not shutil.which("pandoc"):
        print("LỖI: không tìm thấy pandoc trong PATH. Cài pandoc rồi chạy lại.")
        return 1

    made, missing = [], []
    for rel, title in DOCS:
        src = BASE / rel
        if not src.is_file():
            missing.append(rel)
            continue
        dst = src.with_suffix(".md")
        out = subprocess.run(
            ["pandoc", str(src), "-f", "docx", "-t", "gfm", "--wrap=none"],
            capture_output=True, text=True, encoding="utf-8", check=True).stdout

        header = (f"# {title}\n\n"
                  "**Engineering & Research Mentoring Program (Lucero)** · "
                  "ThS. Đinh Văn Nam (Mr. Lucero Dinh) — Khoa Điện–Điện tử, Trường Kỹ thuật, Đại học Phenikaa\n\n"
                  + GEN_NOTE.format(src=src.name) + "\n---\n\n")
        dst.write_text(header + tidy(out), encoding="utf-8")
        made.append(f"{dst.relative_to(BASE)}  ({len(header + out)//1024} KB)")

    for m in made:
        print("  sinh:", m)
    for m in missing:
        print("  ✗ thiếu nguồn:", m)
    print(f"XONG — {len(made)} bản Markdown đọc-trên-web.")
    return 1 if missing else 0


if __name__ == "__main__":
    sys.exit(main())
