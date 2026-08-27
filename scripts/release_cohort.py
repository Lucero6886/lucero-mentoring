#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Xuất 5 tài liệu cohort DATN sang một thư mục ngoài (USB, thư mục chia sẻ...).

Từ v1.4 dự án quản lý trong MỘT thư mục duy nhất (EEE Projects) — script này là công cụ
xuất TÙY CHỌN, không nằm trong chuỗi lệnh bắt buộc, và KHÔNG còn đích mặc định.

Cách dùng (chạy từ gốc EEE Projects):
    python3 scripts/release_cohort.py "D:/duong/dan/dich"

Script chỉ copy, không xóa gì ở đích. Nguồn chuẩn và mọi chỉnh sửa: 06_Data/ tại repo này.
"""
import pathlib, shutil, sys

BASE = pathlib.Path(__file__).resolve().parents[1]
if len(sys.argv) < 2:
    print("Cách dùng: python3 scripts/release_cohort.py <thư_mục_đích>")
    print("(Từ v1.4 không còn đích mặc định — DATN_mentor đã ngừng sử dụng.)")
    sys.exit(1)
TARGET = pathlib.Path(sys.argv[1])

RELEASE_FILES = [
    "Danh_muc_de_tai_DATN_Nhom_A_B_HK1_2026_2027.docx",
    "Danh_muc_de_tai_DATN_Nhom_A_B_HK1_2026_2027.pdf",
    "Phieu_lua_chon_va_danh_gia_de_tai_DATN_HK1_2026_2027.docx",
    "RELEASE_NOTE_HK1_2026_2027.md",
    "RELEASE_NOTE_HK1_2026_2027.docx",
]

def main() -> int:
    if not TARGET.is_dir():
        print(f"LỖI: không thấy thư mục đích {TARGET} — tạo thư mục hoặc truyền đường dẫn đúng.")
        return 1
    missing = [f for f in RELEASE_FILES if not (BASE / f).is_file()]
    if missing:
        print("LỖI: thiếu file nguồn (chạy generate_catalogs trước?):")
        for f in missing: print("  ✗", f)
        return 1
    for f in RELEASE_FILES:
        shutil.copy2(BASE / f, TARGET / f)
        print("  →", TARGET / f)
    print(f"ĐÃ PHÁT HÀNH {len(RELEASE_FILES)} tài liệu cohort sang {TARGET}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
