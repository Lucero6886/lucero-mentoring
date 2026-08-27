# Engineering & Research Mentoring Program (Lucero) — v1.7.0

Tác giả: ThS. Đinh Văn Nam (Mr. Lucero Dinh) — Khoa Điện–Điện tử, Trường Kỹ thuật, Đại học Phenikaa.

Bộ hồ sơ này là **nguồn chuẩn (single source of truth)** để vận hành mentoring cho:

- Project môn học (P)
- Thực tập / thực tập tốt nghiệp (I)
- Đồ án tốt nghiệp (T)
- Nghiên cứu khoa học (R)

Bộ hồ sơ phục vụ **dài hạn, nhiều học kỳ** — cohort DATN HK1 2026-2027 chỉ là cohort đầu tiên. Các trục chuyên môn:

1. **A - Electronic Hardware -> Digital Design -> FPGA -> ASIC**
2. **B - Hardware-Aware Polar Code Decoding**;
3. **Nhánh Nhúng & IoT (A6, A7)** — firmware, RTOS, SoC, kết nối IoT, edge AI *(mở từ v1.5.0)*;
4. Vùng giao thoa **AB — co-design**: Digital IC × Polar × ràng buộc nhúng/IoT, theo định hướng nghiên cứu luận án.

## Nguyên tắc kiến trúc

- Backend chung: `06_Data/` (portfolio 105 đề tài + rubric + milestone + cohort). Kiểm tra bằng `scripts/validate_portfolio.py`, sinh view bằng `scripts/generate_catalogs.py --docx`.
- Frontend riêng: catalog P/I/T/R trong `02_Project_Portfolio/`.
- Quản trị mentor: `01_Governance/` + `03_Operations/`.
- Mỗi sinh viên/project dùng template trong `04_Project_Template/`.
- Khi làm việc với Claude, bắt đầu bằng `05_Claude/MASTER_PROMPT_CLAUDE.md`.

## Thứ tự đọc đề xuất

1. `01_Governance/Master_Mentoring_Handbook.docx`
2. `02_Project_Portfolio/Master_Project_Portfolio_AB.docx`
3. Catalog tương ứng P/I/T/R
4. `03_Operations/Mentoring_Operating_Procedure_SOP.docx`
5. `03_Operations/Mentoring_Management_Workbook.xlsx`
6. `05_Claude/MASTER_PROMPT_CLAUDE.md`

## Quy tắc mã đề tài

`<Family>-<Type><Number>`; ví dụ `A4-T01` = ASIC family, Đồ án tốt nghiệp, đề tài 01.

- P = Course Project
- I = Internship
- T = Graduation Thesis
- R = Research

## Nguyên tắc không thay đổi

- Interest là nguyện vọng, **readiness mới quyết định scope**.
- Baseline trước novelty.
- Không baseline ở Gate 2 thì không mở research extension.
- Khi trễ tiến độ: ưu tiên **reduce scope**, không cứu bằng cách mentor làm thay.
- `Cannot explain = Not completed` đối với sản phẩm có AI hỗ trợ.
- Mỗi project phải để lại **Project Legacy Package**.
- Không phải mọi sinh viên đều phải trở thành researcher; engineering excellence và research excellence đều có giá trị.
