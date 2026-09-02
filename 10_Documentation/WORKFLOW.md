# WORKFLOW — sửa hệ thống và phát hành

Quy trình kỹ thuật để thay đổi bất kỳ nội dung nào của hệ thống. Ai sửa cũng đi đúng chuỗi này.

---

## 1. Nguyên tắc một dòng

**Sửa nguồn chuẩn → validate → generate → release → ghi changelog.**
Không bao giờ sửa tay file sinh tự động — nó bị ghi đè ở lần generate kế tiếp.

## 2. Cái gì là nguồn chuẩn

| Nội dung | Nguồn chuẩn DUY NHẤT |
|---|---|
| Đề tài, family, level, type, MVT, alias, prerequisite | `06_Data/project_portfolio.json` |
| Rubric TR/WR/RR + ngưỡng | `06_Data/readiness_rubrics.json` |
| Gate 1–6 + hard rule | `06_Data/milestone_gates.json` |
| Lịch tuần, deadline gate, đề tài mở, career guide | `06_Data/cohort_<id>.json` |
| Triết lý, chính sách, quy trình | `01_Governance/*.docx` + `03_Operations/Mentoring_Operating_Procedure_SOP.docx` |

Mọi thứ khác — 5 catalog, danh mục cohort, phiếu, trang web, sheet Portfolio — là **view sinh ra**.

## 3. Chuỗi lệnh đầy đủ

```bash
cd "EEE Projects"

python3 scripts/validate_portfolio.py              # 1. BẮT BUỘC PASS trước khi đi tiếp
python3 scripts/generate_catalogs.py --docx --pdf  # 2. sinh 7 view + PDF danh mục
python3 scripts/generate_site.py                   # 3. sinh docs/index.html (khi sửa dữ liệu đề tài)
python3 scripts/build_release.py                   # 5. đóng gói dist/ + ZIP (khi phát hành mốc)
```

Rồi ghi `00_START_HERE/CHANGELOG.md` và cập nhật `implementation-notes.md` **và** `.html`.

**Môi trường:** Python 3 (chỉ stdlib) · `pandoc` cho `--docx`/`--pdf` · Chromium/Chrome/Edge cho `--pdf`.
Trình duyệt không nằm trên PATH thì đặt biến môi trường:

```bash
# Windows PowerShell
$env:CHROME_BIN = "C:\Program Files\Google\Chrome\Application\chrome.exe"
# Linux / macOS
export CHROME_BIN=/usr/bin/chromium
```

## 4. Thêm hoặc sửa một đề tài

1. Mở `06_Data/project_portfolio.json`.
2. `code` không trùng, đúng format `<Family>-<Type><NN>`, khớp field `family` và `type`. 13 field bắt buộc không rỗng.
3. `min_level ≥ 3` → bắt buộc có **cả** `prerequisites` (mô tả) và `prereq_codes` (máy đọc được).
4. `type = T` → bắt buộc có `mvt`.
5. Mở cho cohort hiện tại → thêm `cohort_alias` + `checkpoints_15w` vào record, **và** thêm cặp `{alias, code}`
   vào `topics[]` của `cohort_*.json`. Hai chỗ phải khớp — validator kiểm.
6. Muốn vào bảng gợi ý nghề nghiệp → thêm mã vào `career_guide` của cohort JSON.
7. Chạy chuỗi lệnh mục 3.

> **Không đổi `code` của đề tài đã giao cho SV** — mã là định danh vĩnh viễn trong hồ sơ.
> Gỡ đề tài khỏi lưu hành: đổi `status` thành `archived`, **không xóa record**.

## 5. Mở cohort mới (kỳ sau)

Tạo `06_Data/cohort_<id>.json` mới · thêm `cohort_alias` cho các đề tài mở · chạy chuỗi lệnh mục 3.
Generator tự sinh danh mục + phiếu cho **mọi** file `cohort_*.json` tìm thấy.
**Không sửa file cohort cũ** — hồ sơ SV khóa trước phải tra được.

## 6. Bẫy phải biết khi sửa script

`06_Data` dùng `*` làm ký tự wildcard trong `prereq_codes` (vd `A1-P*` = "bất kỳ đề tài P nào của family A1").
Dấu này trùng cú pháp in nghiêng của Markdown.

**Mọi chuỗi lấy nguyên văn từ JSON đưa vào Markdown phải đi qua `star()`** trong `generate_catalogs.py`.
Không escape thì pandoc nuốt ký tự và làm lệch cả cụm bao quanh — lỗi này từng lọt vào bản phát hành.
`generate_site.py` xuất HTML nên dùng `html.escape()`, không dính bẫy này.

## 7. Kiểm nhanh sau khi generate

- Mở danh mục docx, tìm dòng *"Đầu vào … (mã tham chiếu: `A1-P*`)"* — **dấu `*` phải còn**.
- Số đề tài trong danh mục cohort = số phần tử `topics[]` của cohort JSON.
- Mở phiếu, mục 5.3 có đủ 3 dòng Level.
- Dòng phiên bản trên tài liệu khớp `meta.version` trong `06_Data/*.json` và file `VERSION`.

## 8. Sao lưu và phục hồi

Mọi view sinh lại được 100% từ 4 file JSON → **chỉ cần backup `06_Data/`** là dựng lại được toàn bộ tầng tài liệu.

Cần backup riêng (không sinh lại được): `01_Governance/` · `03_Operations/` · `04_Project_Template/` ·
`05_Claude/` · `07_Private/` · `tests/` · `10_Documentation/` · `implementation-notes.*`.

Generate ra kết quả sai → **không sửa tay file view**. Khôi phục JSON từ bản sao → validate → generate lại.
Bản gốc v1.0 lưu tại `99_Archive/2026-08-23_v1.0/`.

## 9. Làm việc song song

Nhiều phiên (người hoặc AI) cùng sửa repo sẽ ghi đè lẫn nhau — đã xảy ra. Trước khi ghi đè một file,
kiểm thời gian sửa gần nhất của nó. Sau mỗi lần sửa lớn, chạy lại `validate_portfolio.py` để chắc nguồn chuẩn còn nhất quán.
