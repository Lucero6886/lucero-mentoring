# DRY RUN — A-track · `A4-T01` (alias cohort: A1)

**Mục đích:** kiểm tra end-to-end quy trình hệ thống v1.1 trên một sinh viên giả định làm đề tài
**A4-T01 — Thiết kế một Digital IP từ RTL đến GDSII** (DATN HK1 2026-2027, 07/09 → 19/12/2026).
Đây là dry-run GIẤY (bước 8 roadmap, mục F acceptance checklist) — mọi dữ liệu sinh viên là giả định, không có PII thật.

Sinh viên giả định: **SV-A** (năm 4, đã qua Thực tập tốt nghiệp ✔ điều kiện cứng `eligibility_rules.T`).

---

## Giai đoạn 0 — Admission (20/08 → 03/09)

| Bước quy trình (SOP §1, Handbook §7) | Thực hiện trong dry-run | Nguồn/công cụ dùng | OK? |
|---|---|---|---|
| SV nộp Top-3 (Phiếu 1, ghi mã chuẩn) | Top-1 `A4-T01`, Top-2 `A4-T02`, Top-3 `A1-T01` | Phiếu v1.1 — có cột "Mã chuẩn đề tài" | ✔ |
| Self-assessment TR (Phiếu 2, 0–5, 16 mục) | Logic số 4, Verilog 3, Sim/debug 3, Linux/WSL 2, Git 3, còn lại 1–2 | Thang anchors từ `readiness_rubrics.json` | ✔ |
| Kiểm tra prerequisite máy-đọc-được | `A4-T01.prereq_codes = ["A4-P01"]` → SV-A chưa làm A4-P01 nhưng có bằng chứng tương đương (đồ án môn có RTL verified + đã cài WSL/Yosys) → mentor chấp nhận "tương đương có evidence" đúng quy ước pattern | `project_portfolio.json` | ✔ |
| Readiness test 2 tuần (Phiếu 4) | Literature: đọc app note RTL-to-GDSII, trình bày đủ 6 mục ✔ · Mini-task: chạy Yosys synth một FIFO nhỏ, nộp script + netlist report ✔ · Oral 10′: giải thích được vì sao chọn constraint ✔ | Phiếu 4 v1.1 | ✔ |
| Mentor evaluation (Phiếu 5) | WR: 4+3+4+3+3 = **17/20** ≥ 14 (DATN engineering) ✔ · RR: 2–3 (đề tài engineering, RR "cơ bản" đủ) · TR kiểm chứng qua mini-task | Ngưỡng từ rubrics JSON | ✔ |
| Kết luận | **Nhận** (không điều kiện) · min_level 2 ≤ năng lực L2 của SV-A | 4 lựa chọn chuẩn | ✔ |

## Giai đoạn 1 — Onboarding (W1: 07–13/09)

| Việc | Thực hiện | Ghi nhận |
|---|---|---|
| Ký Working Agreement | Điền mục A: Loại = T, Mã = `A4-T01` | ✔ mẫu có đủ chỗ |
| Tạo repo từ `04_Project_Template/` | README + charter + weekly + experiment log + AI log + known issues + next steps + legacy checklist | ✔ đủ 9 file |
| Điền PROJECT_CHARTER | Code `A4-T01`; **MVT chép nguyên từ JSON** (spec+RTL+testbench+regression / synthesis+STA / physical+DRC-LVS / GDSII hoặc physical report / repo tái lập); **Extension:** so sánh 2 constraint — chỉ mở sau baseline sign-off | ✔ charter có mục MVT và Extension riêng |
| Nhập workbook | Students: 1 dòng (Track=T, Assigned=`A4-T01`, MVT rút gọn, Status=Active, Risk=Green) · Milestones: block 6 gate | ✔ |

## Giai đoạn 2 — Vận hành 15 tuần theo gate

Checkpoint per-topic (`checkpoints_15w`) khớp cửa sổ gate — đối chiếu từng gate:

| Gate (deadline cohort) | Checkpoint đề tài | Kịch bản dry-run | Quy tắc kích hoạt | Kết quả |
|---|---|---|---|---|
| G1 (20/09) | W2: spec + test plan | Nộp spec UART-IP 8 trang + test plan; oral check pass | — | **Pass** |
| G2 (11/10) | W5: RTL verified | Regression 14/14 test pass, waveform + log đính kèm; evidence tái lập bằng script | Baseline có → **được phép** mở extension sau này | **Pass** |
| G3 (01/11) | W8: synthesis/STA ổn | Yosys synth sạch; STA còn 2 path âm → SV tự sửa pipeline 1 stage trong tuần 8, mentor không sửa hộ | Đúng nguyên tắc "không làm thay" | **Pass** |
| G4 (22/11) | W11: physical flow/PPA | LibreLane hoàn thành floorplan→route, DRC sạch, LVS sạch, PPA table xong | Sau 22/11 không thêm "kiến trúc mới" — extension so sánh constraint đã chạy trong W9–11 ✔ hợp lệ | **Pass** |
| G5 (06/12) | — | Bản thảo thuyết minh đầy đủ + phân tích PPA | — | **Pass** |
| G6 (19/12) | W15: thesis+demo+repo | Mentor chạy lại flow từ README trên máy khác: tái lập được GDSII; oral defense thử | Legacy checklist 11/11 mục ✔ | **Pass** |

## Giai đoạn 3 — Closeout

- `LEGACY_PACKAGE_CHECKLIST.md`: 11/11 tick, mentor ký. ✔
- Definition of Done (SOP §10): trả lời được 10/10 câu. ✔
- Đánh giá tiếp: SV-A đủ WR/RR để mời làm NCKH `A4-R01`? RR mới ở mức cơ bản → **chưa mời**, gợi ý con đường engineering. Đúng nguyên tắc "không ép mọi SV thành researcher". ✔

## KẾT LUẬN A-TRACK: **PASS** — không có điểm kẹt chặn luồng.

### Ghi nhận (không chặn, đưa vào FINAL_SYSTEM_AUDIT):
1. Charter template không nhắc SV chép `checkpoints_15w` vào phần Milestone gates — mentor nên hướng dẫn chép từ danh mục (đã ghi thành khuyến nghị vận hành, không sửa template trong dry-run).
2. Pattern "tương đương có evidence" cho prereq_codes hoạt động tốt nhưng quyết định tương đương cần được ghi vào Phiếu 5 mục "Prerequisite gaps" — mẫu đã có chỗ. ✔
