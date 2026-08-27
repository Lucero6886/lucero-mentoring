#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Đóng gói bản phát hành (MASTER_PROMPT §24) — dist/<name>-v<VERSION>/ + ZIP.

Cách dùng (chạy từ gốc repo):
    python3 scripts/build_release.py

Quy tắc:
- Phiên bản đọc từ file VERSION ở gốc repo — không truyền tay, không đoán.
- Chỉ đóng gói thứ cần để dựng lại và vận hành hệ thống.
- KHÔNG đóng gói: 07_Private (dữ liệu sinh viên), 99_Archive, build/, _to_delete/,
  file tạm Office, cache, file ẩn.
- Chỉ đọc và ghi vào dist/ — không sửa gì trong repo.
"""
import hashlib
import pathlib
import shutil
import sys
import zipfile

BASE = pathlib.Path(__file__).resolve().parents[1]
DIST = BASE / "dist"
NAME = "DATN-Mentoring-HK1-2026-2027"

# (nguồn trong repo, đích trong gói)
INCLUDE_DIRS = [
    ("06_Data", "data"),
    ("scripts", "scripts"),
    ("01_Governance", "docs/governance"),
    ("03_Operations", "docs/operations"),
    ("04_Project_Template", "templates"),
    ("10_Documentation", "docs/guides"),
    ("05_Claude", "docs/claude"),
    ("tests", "validation"),
    ("02_Project_Portfolio", "catalogs"),
    ("00_START_HERE", "docs/start_here"),
]
INCLUDE_FILES = [
    "README.md", "CLAUDE.md", "VERSION",
    "implementation-notes.md", "implementation-notes.html",
    "AUDIT_REPORT.md", "FINAL_SYSTEM_AUDIT.md",
    "Danh_muc_de_tai_DATN_Nhom_A_B_HK1_2026_2027.docx",
    "Danh_muc_de_tai_DATN_Nhom_A_B_HK1_2026_2027.pdf",
    "Phieu_lua_chon_va_danh_gia_de_tai_DATN_HK1_2026_2027.docx",
    "RELEASE_NOTE_HK1_2026_2027.md",
    "RELEASE_NOTE_HK1_2026_2027.docx",
]
SKIP_NAMES = {"__pycache__", ".DS_Store", "Thumbs.db"}


def keep(p: pathlib.Path) -> bool:
    if p.name in SKIP_NAMES or p.name.startswith("~$") or p.name.startswith("."):
        return False
    return p.suffix.lower() not in {".tmp", ".pyc", ".bak"}


def main() -> int:
    vf = BASE / "VERSION"
    if not vf.is_file():
        print("LỖI: thiếu file VERSION ở gốc repo."); return 1
    version = vf.read_text(encoding="utf-8").strip()
    if not version:
        print("LỖI: file VERSION rỗng."); return 1

    root = DIST / f"{NAME}-v{version}"
    root.mkdir(parents=True, exist_ok=True)
    # Không xóa cây cũ: một số môi trường (thư mục mount của Cowork) không cho xóa file.
    # Ghi đè bằng copy2 rồi báo lại file thừa để người dùng tự xử lý.
    before = {f.relative_to(root).as_posix() for f in root.rglob("*") if f.is_file()}

    n_files = 0
    manifest_rows = []
    written = set()

    for src_rel, dst_rel in INCLUDE_DIRS:
        src = BASE / src_rel
        if not src.is_dir():
            print(f"  bỏ qua (không có): {src_rel}/"); continue
        for f in sorted(src.rglob("*")):
            if not f.is_file() or not keep(f):
                continue
            if any(part in SKIP_NAMES or part.startswith(".") for part in f.relative_to(src).parts[:-1]):
                continue
            dst = root / dst_rel / f.relative_to(src)
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(f, dst)
            n_files += 1
            rel = f"{dst_rel}/{f.relative_to(src).as_posix()}"
            written.add(rel)
            manifest_rows.append((rel, src_rel))

    # FINAL-AUDIT.md nằm sẵn trong dist/ — copy vào gói như một file phát hành
    fa = DIST / "FINAL-AUDIT.md"
    if fa.is_file():
        shutil.copy2(fa, root / "FINAL-AUDIT.md")
        n_files += 1
        written.add("FINAL-AUDIT.md")
        manifest_rows.append(("FINAL-AUDIT.md", "dist/"))

    for name in INCLUDE_FILES:
        f = BASE / name
        if not f.is_file():
            print(f"  bỏ qua (không có): {name}"); continue
        shutil.copy2(f, root / name)
        n_files += 1
        written.add(name)
        manifest_rows.append((name, "(gốc repo)"))

    # MANIFEST của gói — nêu rõ file nào sửa trực tiếp, file nào sinh lại
    gen_prefixes = ("catalogs/", "Danh_muc", "Phieu_lua_chon", "RELEASE_NOTE", "implementation-notes.html")
    lines = [
        f"# MANIFEST — {NAME} v{version}", "",
        f"Tổng: **{n_files} file**. Cột Loại: `AUTHORITATIVE` sửa trực tiếp · "
        "`GENERATED` sinh lại được, không sửa tay · `MAINTAINED` duy trì thủ công.", "",
        "| Đường dẫn trong gói | Nguồn trong repo | Loại | Tái tạo |",
        "|---|---|---|---|",
    ]
    for path, origin in sorted(manifest_rows):
        if path.startswith("data/"):
            typ, how = "AUTHORITATIVE", "Sửa trực tiếp — đây là nguồn chuẩn"
        elif path.startswith(gen_prefixes):
            typ, how = "GENERATED", "`validate_portfolio.py` → `generate_catalogs.py --docx --pdf`"
        elif path.startswith("scripts/"):
            typ, how = "AUTHORITATIVE", "Mã nguồn tự động hóa"
        else:
            typ, how = "MAINTAINED", "Cập nhật thủ công"
        lines.append(f"| `{path}` | `{origin}` | {typ} | {how} |")
    lines += [
        "", "## Không có trong gói (cố ý)", "",
        "- `07_Private/` — hồ sơ thật của sinh viên; không bao giờ đóng gói.",
        "- `99_Archive/` — bản lưu trữ trước regenerate.",
        "- `build/` — trung gian, sinh lại được.",
        "- `docs/index.html` — trang web sinh lại bằng `generate_site.py`.",
        "- `_to_delete/` — bản thừa chờ xóa.", "",
        "## Cập nhật gói ở lần sau", "",
        "1. Sửa `06_Data/*.json` trong repo · 2. `validate_portfolio.py` (PASS) · "
        "3. `generate_catalogs.py --docx --pdf` · 4. `generate_site.py` · 5. `release_cohort.py` · "
        "6. sửa `VERSION` · 7. `build_release.py`.",
    ]
    (root / "MANIFEST.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    n_files += 1
    written.add("MANIFEST.md")

    stale = sorted(before - written)
    if stale:
        print(f"  ! {len(stale)} file thừa từ lần đóng gói trước (không tự xóa được — xóa tay nếu cần):")
        for s_ in stale[:10]:
            print("      ", s_)
        if len(stale) > 10:
            print(f"       … và {len(stale)-10} file nữa")

    # ZIP xác định, không phụ thuộc thứ tự duyệt thư mục
    # Chỉ đóng gói file của lần build này — không quét cả thư mục, tránh nuốt file thừa.
    zpath = DIST / f"{NAME}-v{version}.zip"
    with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as z:   # "w" ghi đè, không cần xóa trước
        for rel in sorted(written):
            z.write(root / rel, f"{root.name}/{rel}")

    sha = hashlib.sha256(zpath.read_bytes()).hexdigest()
    print(f"gói   : {root.relative_to(BASE)}  ({n_files} file)")
    print(f"zip   : {zpath.relative_to(BASE)}  ({zpath.stat().st_size/1024:.0f} KB)")
    print(f"sha256: {sha}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
