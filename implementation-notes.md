# IMPLEMENTATION NOTES — Tài liệu hệ thống Mentoring

**Engineering & Research Mentoring Program (Lucero)**
Phiên bản tài liệu: **2.4** · Phiên bản hệ thống: **v1.6.0** · Cập nhật: **23/08/2026**
Tác giả & mentor chương trình: **ThS. Đinh Văn Nam (Mr. Lucero Dinh)** — Khoa Điện–Điện tử, Trường Kỹ thuật, Đại học Phenikaa

> **Tài liệu này để làm gì.** Đây là tài liệu hệ thống đầy đủ: đọc hết một lượt là nắm được *cái gì là nguồn chuẩn, cái gì là dẫn xuất, mỗi script làm gì, dữ liệu có cấu trúc ra sao, đã quyết định gì và vì sao, còn hạn chế gì*, và **9 quy trình vận hành** viết dưới dạng làm-theo-được. Bản HTML tương đương: `implementation-notes.html`.
>
> Bản web (link riêng tư, mở từ điện thoại/máy khác, share được): https://claude.ai/code/artifact/ec2b8b23-f45b-4850-ba64-509acc4766cf
>
> Tài liệu này **không phải nguồn chuẩn** — nó trỏ về nguồn chuẩn. Khi mâu thuẫn, `06_Data/` và `Master_Mentoring_Handbook.docx` thắng.

**Đọc theo nhu cầu:**

| Bạn muốn… | Đọc mục |
|---|---|
| Biết ngay tuần này phải làm gì | §0 |
| **Chưa biết gì về hệ thống** | ★ (10 phút) |
| Hiểu hệ thống từ đầu | §1 → §5 |
| Sửa một đề tài / rubric / lịch | §15, §20, §7 |
| Vận hành cohort hằng tuần | §13, §16, §17 |
| Biết hệ thống còn yếu ở đâu | §11, §12 |
| Bàn giao cho người khác | §2, §3, §4, §8, §21, §22 |
| Nhờ Claude sửa hệ thống | Phụ lục A |

---

## ★ Hiểu bản chất hệ thống trong 10 phút (đọc phần này trước tiên)

### Hệ thống này là gì, giải quyết vấn đề gì?

Một giảng viên hướng dẫn nhiều sinh viên làm project / thực tập / đồ án / NCKH cùng lúc thường gặp 3 vấn đề: **(1)** thông tin nằm rải rác trong trí nhớ và tin nhắn chat; **(2)** mỗi lần sửa một đề tài phải sửa tay nhiều tài liệu, lâu dần chúng "lệch nhau" (chính audit ngày 23/08 đã bắt được lỗi kiểu này); **(3)** sinh viên chọn đề tài theo tên nghe hay chứ không theo năng lực thật. Bộ hồ sơ này giải cả ba: mọi thứ ghi thành văn bản có cấu trúc — không phụ thuộc trí nhớ; mọi dữ liệu chỉ sống ở **một nơi duy nhất** (thư mục `06_Data/`), các tài liệu khác được "in ra" tự động từ đó nên không bao giờ lệch nhau nữa; và có quy trình đánh giá năng lực đầu vào **trước khi** giao đề tài.

### Từ điển 12 khái niệm (tra nhanh khi đọc bất kỳ tài liệu nào)

| Thuật ngữ | Nghĩa đơn giản |
|---|---|
| **P / I / T / R** | 4 loại hoạt động: **P**roject môn học · thực tập (**I**nternship) · đồ án tốt nghiệp (**T**hesis) · nghiên cứu khoa học (**R**esearch). |
| **Family** (A0–A5, B0–B6, AB) | 14 "dòng chuyên môn". Nhóm A = phần cứng số (PCB → RTL → FPGA → ASIC); nhóm B = giải mã Polar Code; AB = giao thoa hai nhóm. |
| **Mã chuẩn / mã ngắn** | `A4-T01` = family A4, loại T, đề tài số 01 — dùng trong mọi giấy tờ, không bao giờ đổi. "A1", "B3"… chỉ là tên gọi tắt để đọc nhanh trong kỳ này. |
| **Level L0–L5** | Thước đo độ trưởng thành của SV: L0 mới khám phá → L2 tự làm engineering → L4 làm được nghiên cứu. Mỗi đề tài ghi level **tối thiểu** cần có. |
| **Readiness (TR/WR/RR)** | 3 thước đo trước khi giao đề tài: **TR** kỹ thuật (16 kỹ năng, thang 0–5) · **WR** thái độ làm việc (5 phẩm chất, 0–4, tổng /20, có ngưỡng: vd đồ án cần ≥14) · **RR** tư chất nghiên cứu (5 tiêu chí, 0–4, đánh giá định tính). |
| **Readiness test 2 tuần** | "Thử việc" trước khi chốt: đọc 1 tài liệu + làm 1 bài kỹ thuật nhỏ 4–10 giờ + trình bày 5–10 phút. Giao đề tài dựa trên kết quả này, không dựa trên lời hứa. |
| **MVT vs Extension** | **MVT** = phần LÕI bắt buộc, đủ để tốt nghiệp chuẩn kỹ thuật. **Extension** = phần mở rộng nghiên cứu, KHÔNG bắt buộc, chỉ mở khi phần lõi chạy tốt đúng hạn. |
| **Gate 1–6** | 6 trạm kiểm soát rải trong 15 tuần. Hai luật cứng: trượt **Gate 2** (baseline, hết tuần 5) → đóng phần mở rộng; trượt **Gate 3** (hạn 01/11) → thu nhỏ đề tài — thu nhỏ là cơ chế bảo vệ chất lượng, không phải hình phạt. |
| **Evidence** | Bằng chứng công việc nhìn thấy được: code, kết quả đo, waveform, bảng số liệu, demo… "Em đã đọc / đã tìm hiểu" không được tính là tiến độ. |
| **Legacy Package** | Gói bàn giao cuối kỳ (code + hướng dẫn chạy lại + lỗi đã biết + việc kế tiếp) để khóa sau làm tiếp, không phải làm lại từ đầu. |
| **Nguồn chuẩn vs View** | `06_Data/` là **bản gốc**; danh mục, phiếu, workbook, trang web là **bản in tự động**. Muốn sửa → sửa bản gốc rồi chạy script in lại (§20). Không bao giờ sửa bản in. |
| **Cannot explain = not completed** | SV được dùng AI thoải mái để học và làm, nhưng nộp sản phẩm mà không giải thích được thì coi như chưa hoàn thành. |

### Một học kỳ diễn ra như thế nào (kể ngắn, 5 đoạn)

1. **Trước học kỳ (bây giờ):** anh phát danh mục đề tài; SV nộp 3 nguyện vọng + tự chấm kỹ năng; SV làm bài thử việc 2 tuần; anh chấm Phiếu 5 và quyết định *nhận ai — đề tài gì — phạm vi nào*, rồi nộp danh sách cho Khoa theo hạn Khoa công bố.
2. **Tuần 1 (từ 07/09):** gặp từng SV: ký thỏa thuận làm việc, tạo thư mục làm việc từ bộ template, chốt bằng văn bản phần lõi (MVT) và phần mở rộng.
3. **Hằng tuần (15 lần):** SV nộp báo cáo *trước* buổi gặp kèm bằng chứng; buổi gặp chỉ bàn vướng mắc và chốt việc tuần sau; sau buổi gặp anh ghi vài dòng vào workbook. Sáng thứ Hai liếc cột Risk 1 phút để biết ai đang ổn/không ổn.
4. **Mỗi 2–3 tuần một trạm gate:** đối chiếu SV với điều kiện qua trạm. Ai trễ thì áp thang cảnh báo (nhắc → cảnh báo chính thức + kế hoạch phục hồi → thu nhỏ đề tài). Anh không bao giờ phải "làm hộ" — hệ thống được thiết kế để điều đó không xảy ra.
5. **Cuối kỳ (tuần 14–15):** kiểm tra người khác chạy lại được không + SV giải thích được không → tick 11 mục checklist bàn giao → xong. Ai có tư chất thì mời làm tiếp NCKH kỳ sau.

### Việc của anh gói lại chỉ có 4 nhịp

- **Mỗi kỳ một lần:** phát tài liệu, đánh giá đầu vào, giao đề tài (bộ tài liệu HK1 đã sẵn sàng).
- **Mỗi tuần ~30 phút:** đọc báo cáo trước buổi gặp + ghi sổ sau buổi gặp + liếc Risk sáng thứ Hai.
- **Mỗi trạm gate một buổi:** rà từng SV theo bảng có sẵn.
- **Khi muốn sửa nội dung** (thêm đề tài, đổi mô tả, đổi ngưỡng): sửa 1 file trong `06_Data/` → chạy 3 lệnh (§20) → mọi tài liệu tự cập nhật. Hoặc đơn giản là nhờ Claude làm (prompt sẵn ở Phụ lục A).

### Mở file nào khi nào

| Anh muốn… | Mở |
|---|---|
| Xem tổng quan + việc cần làm | File này (`implementation-notes.html` dễ đọc hơn bản .md) |
| **Hình dung từng đề tài + cách dùng cho giảng dạy/mentor/nghiên cứu** | `Ban_do_de_tai.html` — bản đồ trực quan toàn bộ đề tài, sinh bởi `scripts/generate_ban_do.py` |
| Phát tài liệu cho SV | 3 file ở thư mục gốc: `Danh_muc_...docx/pdf` + `Phieu_...docx` (bản hiện hành in “Phiên bản 1.5.0”, chưa phát cho ai; khi phát gửi kèm `RELEASE_NOTE_HK1_2026_2027.docx`); hoặc share link trang web (§6, tính năng F6) |
| Theo dõi SV hằng tuần | `03_Operations/Mentoring_Management_Workbook.xlsx` — khi có dữ liệu thật, lưu bản làm việc vào `07_Private/` |
| Đọc triết lý/quy tắc gốc | `01_Governance/Master_Mentoring_Handbook.docx` |
| Sửa đề tài/rubric/lịch | `06_Data/*.json` + `scripts/` (hoặc nhờ Claude — Phụ lục A) |
| Đối chiếu hồ sơ kiểm định | `AUDIT_REPORT.md`, `FINAL_SYSTEM_AUDIT.md` — chỉ đọc khi cần |

### Ba việc trước mắt, nói thật đơn giản

1. **Gửi cho sinh viên** danh mục + phiếu + release note (bản hiện hành ở thư mục gốc, in “Phiên bản 1.5.1”) — trong cửa sổ đăng ký của Khoa.
2. **Khi phiếu nộp về:** chấm theo Phiếu 5, quyết định nhận ai/đề tài gì, nộp danh sách cho Khoa **theo hạn Khoa công bố**.
3. **Từ 07/09:** buổi gặp tuần 1 — ký thỏa thuận, chốt MVT/extension cho từng em.

*(Một câu hỏi vận hành đang chờ anh quyết — dòng R6 ở §12: lịch thử việc 2 tuần không kịp trọn vẹn trước hạn Khoa chốt danh sách. Hai cách xử lý đã ghi sẵn ở đó, chọn cách nào cũng chỉ mất 1 câu trả lời.)*

---

## 0. Việc cần làm NGAY (cửa sổ 23/08 → 07/09/2026)

Bối cảnh: sinh viên đang trong cửa sổ đăng ký học phần của Khoa. Danh mục + phiếu **v1.5.1** đã sẵn sàng phát, chưa phát cho ai.

| # | Hạn | Việc | Trạng thái |
|---|-----|------|-----------|
| 1 | — | Chốt 3 quyết định CR-1/CR-2/CR-3 | ✅ 23/08 |
| 2 | — | Regenerate danh mục + phiếu theo mã chuẩn & thang chuẩn | ✅ 23/08 (v1.2.1) |
| 3 | Cửa sổ đăng ký | **Phát danh mục + phiếu** cho sinh viên | ☐ |
| 4 | Cửa sổ đăng ký | Thu Top-3 nguyện vọng + self-assessment (ghi **mã chuẩn**, vd `A4-T01`) | ☐ |
| 5 | **Cần quyết trước 25/08** | **Chốt phương án readiness test** — lịch hiện tại không kịp (§12, UNRESOLVED-1) | ⚠ |
| 6 | Theo hạn Khoa | Nhắc SV hoàn tất thủ tục hành chính với Khoa (học phí, phiếu giao đồ án) | ☐ |
| 7 | Trước hạn Khoa chốt | Hoàn tất Phiếu 5 (mentor evaluation) từng SV → danh sách giao đề tài cho Khoa | ☐ |
| 8 | 07–13/09 (W1) | Onboarding: ký Working Agreement, tạo repo từ `04_Project_Template/`, chốt MVT + Extension tách biệt, đăng Project Charter | ☐ |
| 9 | Song song | Điền sheet Students/Readiness; có dữ liệu thật → lưu bản làm việc vào `07_Private/` | ☐ |

**Quy tắc vàng:** *Interest là nguyện vọng — readiness mới quyết định scope. Không xác nhận đề tài advanced trước khi có evidence từ readiness test.*

---

## 1. Trạng thái dự án

| Mục | Giá trị |
|---|---|
| Giai đoạn hiện tại | **Vận hành** — hệ thống đã xây và nghiệm thu xong; việc còn lại là chạy cohort |
| Trạng thái tổng thể | `COMPLETE WITH DOCUMENTED LIMITATIONS` (§11) — 1 tồn đọng cần mentor quyết (§12) |
| Phiên bản hệ thống | **v1.6.0** (khung tiến độ chuyển sang **tương đối theo tuần**, dùng chung mọi khóa; v1.5.1 gỡ mốc hành chính; v1.5.0 mở nhánh Nhúng & IoT A6/A7 + co-design AB, 105 đề tài) |
| Validation | `validate_portfolio.py` **PASS** — 105 topics · rubrics · gates · 1 cohort file · 0 lỗi |
| Nghiệm thu | `ACCEPTANCE_CHECKLIST.md` **36/36** (2 mục "đạt có điều kiện vận hành") |
| Dry-run | 2 luồng A/B **PASS** (`tests/`) |
| Cohort đang chạy | HK1 2026–2027 · DATN (type T) · 21 đề tài mở · bắt đầu 07/09/2026, khung 15 tuần |
| Đã phát cho SV | **Chưa** — nên bản v1.5.0 thay thế trực tiếp; RELEASE_NOTE_HK1_2026_2027 dùng khi phát |
| Thư mục dự án | `C:\Users\admin\Downloads\EEE Projects` — **thư mục DUY NHẤT** cho toàn bộ chương trình (NCKH · luận án · hướng dẫn nghiên cứu · thực tập tốt nghiệp · mentor cộng đồng IC design · cohort DATN HK1 2026-2027). Thư mục `DATN_mentor` cũ **đã được chủ dự án xóa** (23/08/2026) |

### Lịch sử phiên bản

| Ver | Ngày | Nội dung |
|---|---|---|
| **v1.5.1** | 23/08 | **Gỡ mốc hành chính + điều kiện đăng ký** khỏi nguồn chuẩn và mọi view (quyết định chủ dự án — thông tin hành chính theo kỳ không nằm trong tài liệu dài hạn) |
| **v1.5.0** | 23/08 | **Mở nhánh Nhúng & IoT (A6, A7) + mở rộng co-design AB theo định hướng luận án** — 21 đề tài mới, tổng 105/16 nhóm; validator A[0-7]; mọi view regenerate |
| v1.0 | 23/08 | Bộ hồ sơ thiết kế tay: governance, catalog, workbook, template. Không có script, không có nguồn chuẩn máy-đọc-được. |
| v1.1 | 23/08 | Chuẩn hóa sau `AUDIT_REPORT.md`: 06_Data 84 đề tài schema đầy đủ, 2 script validate/generate, mọi view regenerate. Đóng C1/C2/C3/H1–H5/M1–M3. |
| v1.1.1 | 23/08 | Nghiệm thu: dry-run A/B, acceptance 36/36, `FINAL_SYSTEM_AUDIT.md`, release note. |
| v1.2 | 23/08 | Lớp web công khai: `generate_site.py` → `docs/index.html` (GitHub Pages + artifact). |
| **v1.4.0** | 23/08 | Thực thi MASTER_PROMPT như bảng kiểm §33: bù 16 hạng mục (6 template, 4 guide, CLAUDE.md, README, VERSION, build_release, dist + FINAL-AUDIT); đóng 3 lỗi MAJOR (lệch phiên bản JSON↔tài liệu, PDF lệch docx, rmtree không chạy được trên mount); khôi phục `release_cohort.py` bị dồn nhầm vào `_to_delete/`. |
| v1.2.1 | 23/08 | Sửa bug escape Markdown làm mất wildcard `A1-P*` trong bản phát hành; RR expectations vào Phiếu 5.2; ô Level vào Phiếu 5.3; validator cross-check lịch gate; `--pdf` để tái lập PDF. |

### Roadmap xây dựng — 9/9 bước đã xong

| Bước | Nội dung | Trạng thái |
|---|---|---|
| 1 | `AUDIT_REPORT.md` | ✅ 23/08 |
| 2 | Chuẩn hóa dữ liệu nguồn (schema v1.1, rubrics đầy đủ, gates keyed, cohort JSON, sửa A5-T02) | ✅ 23/08 |
| 3 | `scripts/validate_portfolio.py` + `scripts/generate_catalogs.py` — VALIDATION PASS 84 topics | ✅ 23/08 |
| 4 | Regenerate 5 view + danh mục cohort (docx+pdf) + phiếu — đã kiểm chứng khớp nguồn 100% | ✅ 23/08 |
| 5 | Template SV + Legacy workflow (`LEGACY_PACKAGE_CHECKLIST.md`, weekly header) | ✅ 23/08 |
| 6 | Tracker mentor: Portfolio sheet 84 đề tài + MVT/Status/Alias, sửa công thức, nới capacity (100 SV / 1500 dòng tuần), quy ước 07_Private | ✅ 23/08 |
| 7 | Lớp web công khai: `scripts/generate_site.py` → `docs/index.html` (84 đề tài + bộ lọc + lịch gate; chỉ dữ liệu public). Link online cho SV: https://claude.ai/code/artifact/c5d77e76-9f17-4ecb-961f-780daaee8ec3 — mở share từ menu trang khi muốn phát cho SV. GitHub Pages: đẩy repo → Settings → Pages → main `/docs` | ✅ 23/08 |
| 8 | Dry-run 2 luồng: A-track (`A4-T01`) + B-track (`B2-T01`, có kịch bản trượt G3) — `tests/` | ✅ 23/08 PASS |
| 9 | Acceptance 36/36 → `FINAL_SYSTEM_AUDIT.md` (kèm hạn chế còn lại) | ✅ 23/08 |

---

## 2. Nguồn đã rà soát

Toàn bộ repo `EEE Projects` — dự án tổng (65 file, chưa kể `build/` sinh tạm). Cột **Thẩm quyền**: `CHUẨN` = nguồn chuẩn, sửa trực tiếp · `SINH` = view sinh tự động, **không sửa tay** · `SỔ` = tài liệu duy trì thủ công · `LƯU` = lưu trữ, chỉ đọc.

| Nguồn | Vai trò | Thẩm quyền | Ghi chú |
|---|---|---|---|
| `06_Data/project_portfolio.json` | 105 đề tài + family/level/type | **CHUẨN** | 85 KB. Trái tim hệ thống. |
| `06_Data/readiness_rubrics.json` | Rubric TR/WR/RR + ngưỡng | **CHUẨN** | Sửa v1.2.1: RR có `max_total` + `expectations` dạng list. |
| `06_Data/milestone_gates.json` | Gate 1–6 + hard rule | **CHUẨN** | Ngày cụ thể nằm ở file cohort. |
| `06_Data/cohort_HK1_2026_2027.json` | Lịch 15 tuần, deadline gate, 21 đề tài mở, career guide | **CHUẨN** | Mỗi kỳ tạo một file `cohort_*.json` mới. Mốc hành chính đã gỡ (v1.5.1, quyết định chủ dự án). |
| `01_Governance/Master_Mentoring_Handbook.docx` | Triết lý, level, readiness, gate, peer mentoring, legacy | **CHUẨN** (policy) | Viết tay, **không** sinh từ 06_Data → §12 UNRESOLVED-3. |
| `01_Governance/AI_and_Academic_Integrity_Policy.docx` | Chính sách AI, ownership check, AI usage log | **CHUẨN** (policy) | Viết tay. |
| `01_Governance/Mentor_Student_Working_Agreement.docx` | Thỏa thuận thầy–trò, thang cảnh báo | **CHUẨN** (policy) | Viết tay, có chỗ ký. |
| `01_Governance/Cohort_HK1_2026_2027_Implementation_Guide.docx` | Hướng dẫn vận hành cohort 15 tuần | **SỔ** | Trùng một phần với `cohort_*.json`. |
| `01_Governance/Readiness_and_Topic_Selection_Forms.docx` | Bộ phiếu 1–5 bản v1.0 | ⚠ **LƯU** | **Xung đột với phiếu sinh tự động** → §12 UNRESOLVED-2. |
| `02_Project_Portfolio/*.docx` (5 file) | Master + catalog P/I/T/R | **SINH** | Từ `generate_catalogs.py --docx`. |
| `03_Operations/Mentoring_Operating_Procedure_SOP.docx` | SOP tuyển → closeout, 10 mục | **CHUẨN** (quy trình) | Viết tay. |
| `03_Operations/Weekly_Report_and_Meeting_Template.docx` | Weekly report, meeting record, blocker escalation | **SỔ** | Bản .md tương ứng ở `04_Project_Template/`. |
| `03_Operations/Mentoring_Management_Workbook.xlsx` | Tracker 8 sheet | **SỔ** (template trắng) | Sheet Portfolio là view của 06_Data. Bản có dữ liệu thật → `07_Private/`. |
| `04_Project_Template/*.md` (9 file) | Template repo cho từng SV | **SỔ** | SV copy khi onboard. |
| `05_Claude/MASTER_PROMPT_CLAUDE.md` | Chỉ dẫn cho Claude ở phiên sau | **SỔ** | |
| `05_Claude/CLAUDE_PROJECT_CONTEXT.md` | 10 invariant bất biến | **CHUẨN** (invariant) | Đọc trước khi để AI sửa hệ thống. |
| `05_Claude/ACCEPTANCE_CHECKLIST.md` | 36 tiêu chí nghiệm thu | **SỔ** | |
| `scripts/*.py` (3 file) | validate + generate catalog + generate site | **CHUẨN** (code) | |
| `Danh_muc_de_tai_DATN_*.docx/.pdf` | Danh mục cohort phát cho SV | **SINH** | |
| `Phieu_lua_chon_va_danh_gia_*.docx` | Phiếu cohort phát cho SV | **SINH** | |
| `docs/index.html` | Trang web công khai | **SINH** | Từ `generate_site.py`. |
| `AUDIT_REPORT.md` | Kiểm toán v1.0 + annex xử lý | **LƯU** | Lịch sử, không cập nhật nữa — còn nhắc tên thư mục cũ `EEE Projects/`, giữ nguyên như bản ghi thời điểm đó. |
| `FINAL_SYSTEM_AUDIT.md` | Nghiệm thu v1.1.1 | **LƯU** | ⚠ Mục 3.4 và 3.7 đã lỗi thời — xem §11. |
| `tests/DRY_RUN_*.md` (2 file) | Diễn tập giấy luồng A và B | **LƯU** | |
| `99_Archive/2026-08-23_v1.0/` (13 file) | Bản gốc trước regenerate | **LƯU** | Đối chiếu lịch sử. |
| `07_Private/` | Dữ liệu thật của SV | — | `.gitignore` chặn. Hiện chỉ có README. |
| `05_Claude/CLAUDE_MASTER_EXECUTION_DATN_MENTORING.md` | Prompt xây hệ thống | **LƯU** | Chuyển về `05_Claude/` khi gộp một thư mục (v1.4). Đặc tả gốc; tài liệu này là sản phẩm của nó. |

---

## 3. Quyết định nguồn chuẩn

### 3.1 Các vùng thẩm quyền

| Loại nội dung | Nguồn chuẩn DUY NHẤT | Mọi thứ khác là… |
|---|---|---|
| Danh mục đề tài, family, level, type, MVT, alias, prerequisite | `06_Data/project_portfolio.json` | View sinh: Master docx, 4 catalog P/I/T/R, sheet Portfolio, danh mục cohort, `docs/index.html` |
| Rubric TR/WR/RR + ngưỡng | `06_Data/readiness_rubrics.json` | Handbook §5, phiếu, sheet Rubrics |
| Gate 1–6 + hard rule | `06_Data/milestone_gates.json` | Handbook §10, sheet Milestones, danh mục §2 |
| Dữ liệu cohort (mốc hành chính, lịch tuần, deadline, đề tài mở, career guide) | `06_Data/cohort_HK1_2026_2027.json` | Danh mục cohort docx/pdf, Cohort Guide, trang web |
| Triết lý, chính sách, quy trình | `Master_Mentoring_Handbook.docx` + `SOP.docx` + `AI_Policy.docx` | README, implementation-notes |
| Invariant cho AI | `05_Claude/CLAUDE_PROJECT_CONTEXT.md` | `MASTER_PROMPT_CLAUDE.md`, `QUICK_LAUNCH_PROMPT.txt` |

### 3.2 Ba quyết định canonical (chốt 23/08/2026, mentor ủy quyền theo khuyến nghị `AUDIT_REPORT.md`)

**CR-1 — Hệ mã đề tài.** Danh mục cohort dùng **mã chuẩn** `<Family>-<Type><NN>` làm định danh chính, kèm **mã ngắn cohort** (alias `A1`…`B12`) chỉ để đọc nhanh.
*Vấn đề đã giải:* bản v1.0 dùng hai hệ mã xung đột trực tiếp — root-`A4` nghĩa là "UART/SPI/FIFO IP" trong khi chuẩn-`A4` là family "ASIC Design". SV ghi "A4" vào phiếu rồi mentor tra workbook sẽ ra **sai family hoàn toàn**.
*Cách giữ:* alias sống trong `cohort_alias` của portfolio JSON; validator bắt lệch alias giữa cohort file và portfolio.

**CR-2 — Thang điểm readiness.** TR 0–5 trên 16 năng lực; WR 0–4 trên 5 phẩm chất (tổng /20) + 6 ngưỡng; RR 0–4 trên 5 tiêu chí (tổng /20, **không** ngưỡng số).
*Vấn đề đã giải:* workbook và phiếu v1.0 dùng thang khác nhau → không so sánh được giữa SV.

**CR-3 — Hai đề tài "mồ côi".** Thêm `A2-T03` (Adder PPA) và `B5-T03` (Adaptive co-design) vào portfolio; ánh xạ B12 → `AB-T01`.
*Vấn đề đã giải:* hai đề tài đã công bố trong danh mục v1.0 nhưng không tồn tại trong nguồn chuẩn.

### 3.3 Quy tắc bất di bất dịch khi sửa

1. Không đổi tên mã đề tài chuẩn — mã là định danh vĩnh viễn trong mọi hồ sơ.
2. Không sửa tay file `SINH` — sẽ bị ghi đè ở lần generate kế tiếp.
3. Không thay nội dung nguồn bằng kiến thức chung của AI. Thiếu thông tin thì đánh dấu `UNRESOLVED`, không đoán.
4. Không đưa dữ liệu cá nhân SV ra khỏi `07_Private/`.

### 3.4 Mười nguyên tắc bất biến (không thương lượng khi sửa hệ thống)

1. Một portfolio → nhiều view; không nuôi các danh sách viết tay song song.
2. Interest là input, readiness quyết định scope.
3. Baseline trước novelty.
4. DATN phải có MVT tách khỏi Research Extension.
5. Gate 2 không có baseline → không mở extension. Gate 3 trễ → reduce scope.
6. Mentor không cứu bằng cách làm thay execution.
7. AI được dùng, lệ thuộc AI thì không: **cannot explain = not completed**.
8. Mỗi project để lại Project Legacy Package (checklist: `04_Project_Template/LEGACY_PACKAGE_CHECKLIST.md`).
9. Tài liệu public và hồ sơ private phải tách biệt (07_Private + .gitignore).
10. Engineering và Research là hai đích đến ngang giá trị.

---

## 4. Kiến trúc repository

```text
EEE Projects/
├── 00_START_HERE/          Điểm vào: README, roadmap, manifest, changelog
├── 01_Governance/          NGUỒN CHUẨN POLICY (5 docx viết tay)
├── 02_Project_Portfolio/   VIEW SINH: master + 4 catalog P/I/T/R
├── 03_Operations/          SOP, mẫu báo cáo tuần, workbook tracker (template trắng)
├── 04_Project_Template/    Template repo cho từng sinh viên (9 md)
├── 05_Claude/              Prompt, invariant, checklist nghiệm thu
├── 06_Data/                NGUỒN CHUẨN DỮ LIỆU (4 JSON)
├── 07_Private/             Dữ liệu thật của SV — .gitignore chặn
├── 99_Archive/             Bản gốc v1.0 trước regenerate
├── docs/                   VIEW SINH: trang web công khai (GitHub Pages)
├── scripts/                validate + 2 generator
├── tests/                  Dry-run giấy luồng A và B
├── build/                  Trung gian Markdown — .gitignore chặn, sinh lại được
└── (root)                  Danh mục + phiếu cohort (SINH), audit, notes, release note
```

### Vì sao mỗi thư mục tồn tại

| Thư mục | Lý do tồn tại | Ai xem |
|---|---|---|
| `00_START_HERE/` | Người mới — hoặc chính mentor sau 6 tháng — cần một điểm vào duy nhất, không phải đoán bắt đầu từ đâu | Mentor + AI |
| `01_Governance/` | Chính sách phải ổn định và ký được. Tách khỏi dữ liệu vì hai thứ đổi theo nhịp khác nhau: policy đổi theo năm, dữ liệu đề tài đổi theo kỳ | Mentor; một phần phát cho SV |
| `02_Project_Portfolio/` | SV chỉ nên thấy catalog đúng giai đoạn của mình (P/I/T/R), không thấy toàn bộ research roadmap nội bộ | SV |
| `03_Operations/` | Công cụ chạy hằng tuần. Tách khỏi governance vì đây là "cách làm", không phải "luật" | Mentor |
| `04_Project_Template/` | Mỗi SV bắt đầu từ cùng một bộ khung → legacy package đồng nhất, cohort sau kế thừa được | SV copy khi onboard |
| `05_Claude/` | Ràng buộc AI khi sửa hệ thống: invariant + prompt + checklist. Không có nó, mỗi phiên AI sẽ tự phát minh lại kiến trúc | Mentor + AI |
| `06_Data/` | **Một nơi duy nhất** giữ sự thật về đề tài/rubric/gate. Đây là thay đổi kiến trúc lớn nhất giữa v1.0 và v1.1 | Mentor + script |
| `07_Private/` | Tách cứng dữ liệu cá nhân khỏi mọi thứ có thể công khai | Chỉ mentor |
| `99_Archive/` | Regenerate là thao tác phá hủy — phải có đường lùi | Tham khảo |
| `docs/` | GitHub Pages phục vụ SV mà không cần gửi file | Công khai |
| `scripts/` | Biến "kỷ luật đồng bộ" từ thói quen thành cơ chế cưỡng chế | Mentor + AI |
| `tests/` | Chứng minh quy trình chạy được **trước khi** áp lên SV thật | Mentor |

---

## 5. Mô hình dữ liệu

### 5.1 Hệ mã đề tài

```
<Family>-<Type><NN>        vd  A4-T01  ·  B0-P03  ·  AB-R01
   │        │    └── số thứ tự trong (family, type)
   │        └─────── P=Project môn học · I=Thực tập · T=ĐATN · R=NCKH
   └──────────────── A0–A5 · B0–B6 · AB
```

**16 family, 105 đề tài** (A6/A7 mở từ v1.5.0)**:**

| Family | Tên | Số đề tài | P/I/T/R |
|---|---|---|---|
| A0 | Hands-on Electronics & PCB | 7 | 6/1/0/0 |
| A1 | Digital Logic & RTL Design | 7 | 5/1/1/0 |
| A2 | Digital Arithmetic & DSP Hardware | 9 | 4/1/3/1 |
| A3 | FPGA System Design | 6 | 3/1/2/0 |
| A4 | ASIC Design & Physical Implementation | 6 | 2/1/2/1 |
| A5 | Verification, EDA & Reproducible Hardware Dev | 6 | 2/1/2/1 |
| B0 | Polar Fundamentals & Software Baseline | 5 | 3/1/1/0 |
| B1 | Polar Hardware Building Blocks | 7 | 4/1/2/0 |
| B2 | SC Polar Decoder Hardware | 4 | 0/1/2/1 |
| B3 | Hardware-Aware Quantization & Optimization | 5 | 1/1/2/1 |
| B4 | SC-Flip & Reliability-Aware Decoding | 6 | 2/1/2/1 |
| B5 | Adaptive Polar Decoding | 6 | 1/1/3/1 |
| A6 | Embedded Systems & SoC Integration *(v1.5.0)* | 8 | 4/1/2/1 |
| A7 | IoT Systems & Edge Intelligence *(v1.5.0)* | 8 | 4/1/2/1 |
| B6 | Neural-Assisted Polar Decoding | 5 | 0/1/2/2 |
| AB | Co-Design (IC × Polar × Nhúng/IoT) | 10 | 1/0/6/3 |
| | **Tổng** | **105** | **42/15/34/14** |

**Level tối thiểu (L0–L5):** phân bố 8 / 25 / 34 / 19 / 15 / 4.

| L | Tên | Nghĩa |
|---|---|---|
| 0 | Explorer | Chưa có evidence; đang khám phá hướng |
| 1 | Beginner Engineer | Làm được task nhỏ có hướng dẫn |
| 2 | Independent Engineering Student | Tự thực hiện engineering task, debug, báo cáo |
| 3 | Research-Ready Undergraduate | Đọc paper, xây baseline, thiết kế experiment cơ bản |
| 4 | Undergraduate Researcher | Sở hữu research question và thực nghiệm có kiểm soát |
| 5 | Advanced Research Student | Research ownership cao; đủ sức co-design/advanced research |

> `min_level` là **sàn**, không phải trần. Một số DATN advanced (family B6, AB) yêu cầu L4 dù L4 thường gắn với NCKH.

### 5.2 Schema một đề tài

```json
{
  "code": "A4-T01",              // BẮT BUỘC — định danh vĩnh viễn
  "family": "A4",                // BẮT BUỘC — phải khớp tiền tố của code
  "type": "T",                   // BẮT BUỘC — phải khớp ký tự type trong code
  "title_vi": "...",             // BẮT BUỘC
  "title_en": "...",             // BẮT BUỘC
  "min_level": 2,                // BẮT BUỘC — 0..5
  "prerequisites": "...",        // BẮT BUỘC — mô tả cho người đọc
  "prereq_codes": ["A4-P01"],    // BẮT BUỘC khi min_level>=3 — máy đọc được
  "outputs": "...",              // BẮT BUỘC
  "scope": "...",                // BẮT BUỘC
  "extension": "...",            // BẮT BUỘC
  "tools": "...",                // BẮT BUỘC
  "career_relevance": "...",     // BẮT BUỘC
  "status": "active",            // active | candidate | archived
  "mvt": "...",                  // BẮT BUỘC với type T (28/28 có)
  "cohort_alias": {"HK1_2026_2027": "A1"},   // chỉ đề tài mở trong cohort (21)
  "checkpoints_15w": "W2: ... W15: ...",     // chỉ đề tài cohort (21)
  "eligibility": "..."           // điều kiện cứng (7 đề tài A0 hands-on)
}
```

**Độ phủ field trên 105 đề tài:** 13 field bắt buộc đủ 105/105 · `prereq_codes` 82/105 · `mvt` 34/105 (đúng 34 đề tài T) · `cohort_alias` + `checkpoints_15w` 21/105 · `eligibility` 8/105.

### 5.3 Chuỗi tiền đề — hai dạng mã

| Dạng | Ví dụ | Nghĩa |
|---|---|---|
| Mã chính xác | `A4-P01`, `B0-P03`, `B4-I01` | Phải hoàn thành đúng đề tài đó, hoặc năng lực tương đương **có evidence** |
| Pattern wildcard | `A1-P*`, `B1-P*`, `AB-T*` | Hoàn thành **ít nhất một** đề tài loại đó trong family, hoặc năng lực tương đương có evidence |

24/105 đề tài dùng wildcard. Validator kiểm cả hai dạng: mã chính xác phải tồn tại, pattern phải khớp ít nhất một đề tài thật.

> ⚠ **Bẫy đã gặp:** dấu `*` của wildcard trùng cú pháp in nghiêng Markdown. Xem §7.2 và §10 DEC-7.

**Chuỗi tiền đề chuyên môn** (từ `CLAUDE_PROJECT_CONTEXT.md`):

- A4 yêu cầu RTL đã verify + hiểu Linux/synthesis.
- B4 yêu cầu SC baseline.
- B5 yêu cầu SC/SCF baseline.
- B6 nhánh *detection* yêu cầu baseline B5; nhánh *candidate-ranking* yêu cầu SCF/B4 ổn định. Cả hai nhánh cần ML cơ bản + research maturity.
- AB yêu cầu nền của **cả** track A và track B.

### 5.4 Rubric readiness

| Rubric | Thang | Số tiêu chí | Tổng | Ngưỡng |
|---|---|---|---|---|
| **TR** Technical Readiness | 0–5 | 16 năng lực | — (dùng trung bình) | Không có ngưỡng cứng — kiểm chứng bằng mini-task |
| **WR** Working Readiness | 0–4 | 5 phẩm chất | /20 | 6 ngưỡng gợi ý |
| **RR** Research Readiness | 0–4 | 5 tiêu chí | /20 | **Không có ngưỡng số** — chỉ kỳ vọng định tính |

**16 năng lực TR:** Điện tử cơ bản · Logic số · Verilog/SystemVerilog · Simulation/debug waveform · FPGA · Python · MATLAB · Linux/WSL · Git/GitHub · DSP · Truyền thông số · Xác suất · Coding theory · Polar Codes · Đọc tài liệu tiếng Anh · Technical writing.

**Thang TR:** 0 chưa biết · 1 biết tên · 2 hiểu cơ bản · 3 làm được có hướng dẫn · 4 tự làm được · 5 có thể giải thích/mentor người khác.

**5 phẩm chất WR:** Cam kết & kỷ luật · Kiên trì · Trung thực · Chủ động · Tư duy phản biện.

**Ngưỡng WR (/20):** Project ≥10 · Internship ≥12 · DATN engineering ≥14 · DATN research-oriented ≥15 · NCKH ≥16 · Advanced (đề tài family `B6`, hoặc đề tài loại R của family `AB`) ≥17.

**5 tiêu chí RR:** Literature comprehension · Baseline discipline · Experimental design · Interpretation · Research ownership.

**Kỳ vọng RR theo loại hoạt động:** P không bắt buộc · I không bắt buộc · DATN engineering *cơ bản* · DATN research-oriented *khá* · NCKH *bắt buộc, tốt* · Advanced (family B6 / AB-R) *rất tốt*.

> Ngưỡng là **gợi ý, không phải luật máy móc**. Mentor được override nhưng **phải ghi lý do vào hồ sơ**.
> RR cố ý không có ngưỡng số — xem §10 DEC-9.

### 5.5 Mô hình 6 gate / 15 tuần

| Gate | Tuần | Hạn (HK1 26–27) | Điều kiện qua | Hard rule nếu trượt |
|---|---|---|---|---|
| 1 · Problem & Foundation | 1–2 | hết tuần 2 | Hiểu problem, I/O, baseline, metric, prerequisite gaps | Điều chỉnh đề tài hoặc learning plan |
| 2 · Baseline | 3–5 | hết tuần 5 | Baseline/chức năng cơ sở **chạy được** + evidence tái lập | **Không baseline ở tuần 5 → không mở research extension** |
| 3 · Core Implementation | 6–8 | hết tuần 8 | Core implementation + kết quả định lượng trung gian | **Reduce scope** — không cứu bằng cách mentor làm thay |
| 4 · Experiments | 9–11 | hết tuần 11 | Thực nghiệm chính xong; table/figure chính hình thành | **Sau tuần 11 không thêm thuật toán lớn mới** |
| 5 · Analysis & Draft | 12–13 | hết tuần 13 | Phân tích kết quả + bản thảo đầy đủ | Ưu tiên hoàn thiện core, **không polish che lỗ hổng** |
| 6 · Reproducibility & Defense | 14–15 | hết tuần 15 | Người khác chạy lại được; slides/demo; legacy package | Chỉ xác nhận hoàn thành khi **ownership và reproducibility** đạt |

> **Khung này là tương đối** — cột hạn đếm theo tuần kể từ ngày sinh viên nhận đề tài, dùng chung cho mọi khóa.
> Ngày dương lịch của một khóa suy ra từ `start_date` trong `06_Data/cohort_*.json` bằng `scripts/cohort_schedule.py`;
> không lưu ngày ở bất kỳ đâu khác nên không thể có hai lịch lệch nhau.
> Từ v1.2.1 validator bắt buộc mỗi `gate_deadlines[g]` trùng ngày cuối của tuần kết thúc gate đó.

### 5.6 Dữ liệu cohort

`cohort_HK1_2026_2027.json` giữ mọi thứ đổi theo kỳ:

- `activity_type: "T"` — cohort này chỉ mở đề tài DATN. Validator từ chối mọi đề tài không phải type T.
- `duration_weeks: 15` · `start_date` 2026-09-07 · `end_date` 2026-12-19.
- `admin_milestones` — 4 mốc hành chính của Trường.
- `week_calendar` — 15 tuần, mỗi tuần có `start`/`end` cụ thể.
- `gate_deadlines` — 6 ngày, phải khớp `week_calendar`.
- `topics` — 21 cặp `{alias, code}`: 9 nhóm A (A1–A9), 12 nhóm B (B1–B12). Level: 9 đề tài L2, 10 đề tài L3, 2 đề tài L4.
- `career_guide` — 7 mục tiêu nghề nghiệp → đề tài ưu tiên + lộ trình tiếp.

**Mở cohort mới:** tạo `cohort_<id>.json` mới, không sửa file cũ. Generator tự sinh danh mục + phiếu cho mọi `cohort_*.json` tìm thấy.

### 5.7 Hồ sơ sinh viên — workbook 8 sheet

| Sheet | Kích thước | Vai trò |
|---|---|---|
| `Portfolio` | 106 × 17 | View 105 đề tài từ 06_Data (Code…Career Relevance) |
| `Students` | 101 × 18 | 1 dòng/SV: Top-3, Status, Risk, Assigned Topic, MVT, Extension, Last Evidence, Next Deliverable, Next Deadline |
| `Readiness` | 101 × 33 | 16 cột TR + `TR Avg` · 5 cột WR + `WR Total` · 5 cột RR + `RR Avg` · Mentor Decision. Có công thức tự tính. |
| `Weekly_Status` | 301 × 17 | Nhật ký tuần: Goal/Completed/Evidence/Failure/Diagnosis/Tried/Next/Question/AI Use/Risk/Decision |
| `Milestones` | 601 × 10 | 6 dòng gate × 100 SV, prefill Requirement từ `milestone_gates.json` |
| `Rubrics` | 22 × 10 | Bảng tra WR + ngưỡng theo loại hoạt động |
| `Dashboard` | 14 × 8 | KPI: tổng SV, phân bố risk |
| `Instructions` | 17 × 6 | Hướng dẫn dùng từng sheet |

Sức chứa: **100 SV · 1500 dòng weekly · 100 block gate** — giới hạn tĩnh của template (§11.5).

---

## 6. Tính năng đã triển khai

### F1 · Nguồn chuẩn máy-đọc-được cho danh mục đề tài
**Mục đích:** một sự thật duy nhất về 105 đề tài; mọi tài liệu là view.
**File:** `06_Data/project_portfolio.json`.
**Cách hoạt động:** mỗi đề tài là một record 13–18 field; `generate_catalogs.py` lọc theo `type`/`family`/`cohort_alias` để sinh 7 view khác nhau.
**Vì sao thiết kế thế này:** ở v1.0, cùng một đề tài tồn tại trong 4–6 bản sao (master docx, catalog, danh mục cohort, workbook). Sửa một chỗ là 5 chỗ còn lại trôi. JSON + generator biến đồng bộ từ *kỷ luật* thành *cơ chế*.
**Kiểm chứng:** validator PASS 105 topics; số mã trong docx sinh ra khớp JSON 100%.

### F2 · Hệ mã chuẩn + alias cohort
**Mục đích:** một định danh vĩnh viễn, đồng thời giữ mã ngắn dễ đọc cho SV trong kỳ.
**File:** `code` + `cohort_alias` trong portfolio JSON; `topics[]` trong cohort JSON.
**Kiểm chứng:** validator bắt lệch alias giữa hai file; 21/21 khớp.

### F3 · Rubric readiness có cấu trúc
**Mục đích:** so sánh công bằng giữa SV; phiếu và workbook không được tự đặt thang riêng.
**File:** `06_Data/readiness_rubrics.json`.
**Kiểm chứng:** validator ép TR đúng 16 năng lực, WR 5 phẩm chất, RR 5 tiêu chí, `max_total = 5 × scale.max`, mọi ngưỡng WR nằm trong [1, 20], và `expectations` của RR phủ đủ các loại hoạt động có ngưỡng WR.

### F4 · Mô hình gate tách khỏi lịch
**Mục đích:** logic gate ổn định qua các kỳ, chỉ ngày tháng đổi.
**File:** `milestone_gates.json` (logic) + `cohort_*.json` (ngày).
**Kiểm chứng:** validator ép Gate 1..6 liên tục, không hở tuần, tổng 15 tuần, và mỗi deadline khớp `week_calendar`.

### F5 · Bảy view sinh tự động
Master Portfolio · 4 catalog P/I/T/R · danh mục cohort · phiếu cohort. Mỗi view có mức chi tiết riêng: P/I là bảng tóm tắt (theo thiết kế — SV giai đoạn đó chưa cần MVT), T/R có chi tiết + MVT.

### F6 · Trang web công khai
`generate_site.py` → `docs/index.html` self-contained: 105 đề tài dạng card có bộ lọc theo type/family/level + tìm kiếm, lịch gate, hướng dẫn chọn đề tài, quy tắc chương trình. Dark mode, responsive. Deploy: GitHub Pages → Settings → Pages → branch `main`, folder `/docs`. Chỉ chứa dữ liệu public.

### F7 · Tách public/private bằng cơ chế
`07_Private/` + `.gitignore` chặn `07_Private/`, `99_Archive/`, `build/`, file tạm Office. Workbook trong `03_Operations/` là template trắng (đã kiểm bằng script: 0 dòng dữ liệu SV).

### F8 · Bộ template repo cho sinh viên
9 file trong `04_Project_Template/`: README · PROJECT_CHARTER · WEEKLY_REPORT · EXPERIMENT_LOG · LITERATURE_NOTE · AI_USAGE_LOG · KNOWN_ISSUES · NEXT_STEPS · LEGACY_PACKAGE_CHECKLIST. Mục đích: mọi SV để lại legacy package cùng cấu trúc → cohort sau kế thừa được.

### F9 · Ràng buộc cho AI ở các phiên sau
`CLAUDE_PROJECT_CONTEXT.md` giữ 10 invariant; `MASTER_PROMPT_CLAUDE.md` + `QUICK_LAUNCH_PROMPT.txt` chuẩn hóa cách khởi động phiên. Không có lớp này, mỗi phiên AI sẽ tự phát minh lại kiến trúc.

---

## 7. Script và tự động hóa

Cả ba script **chỉ dùng thư viện chuẩn Python** (+ `pandoc` và một trình duyệt cho bước xuất file). Không framework, không dependency ngoài.

### 7.1 `scripts/validate_portfolio.py`

| Mục | Nội dung |
|---|---|
| Lệnh | `python3 scripts/validate_portfolio.py` |
| Input | 4 file JSON trong `06_Data/` |
| Output | Báo cáo ra stdout · exit 0 = PASS, exit 1 = FAIL kèm danh sách lỗi |
| Phụ thuộc | stdlib (`json`, `re`, `sys`, `pathlib`, `datetime`) |

**Kiểm gì:**

- *Portfolio:* mã trùng · format `<Family>-<Type><NN>` · field `family`/`type` khớp mã · family tồn tại · field bắt buộc không rỗng · `status` hợp lệ · `min_level` trong bảng levels · đề tài T bắt buộc có `mvt` · `min_level ≥ 3` bắt buộc có `prerequisites` và `prereq_codes` · mọi `prereq_codes` resolve (mã chính xác tồn tại; pattern khớp ít nhất một đề tài).
- *Rubrics:* TR đúng 16 năng lực · WR 5 phẩm chất · WR `max_total = 5 × scale.max` · ngưỡng WR trong khoảng hợp lệ · RR 5 tiêu chí · RR `max_total = 5 × scale.max` *(v1.2.1)* · RR `expectations` là list đủ field và phủ đủ loại hoạt động có ngưỡng WR *(v1.2.1)*.
- *Gates:* đúng Gate 1..6 theo thứ tự · tuần liên tục không hở · đủ 4 field mô tả · tổng 15 tuần (cảnh báo nếu khác).
- *Cohort:* alias không trùng · alias trỏ mã tồn tại · đề tài đúng `activity_type` · alias khớp `cohort_alias` trong portfolio · `career_guide` chỉ tham chiếu mã tồn tại · `week_calendar` đủ và liên tục · đủ 6 `gate_deadlines` · **(v1.2.1)** tuần liền mạch từng ngày, khớp `start_date`/`end_date`, và mỗi `gate_deadlines[g]` trùng ngày cuối tuần kết thúc gate.

**Failure mode:** JSON hỏng hoặc thiếu file → báo lỗi và dừng, không generate. Fail-fast có chủ ý.

### 7.2 `scripts/generate_catalogs.py`

| Mục | Nội dung |
|---|---|
| Lệnh | `python3 scripts/generate_catalogs.py [--docx] [--pdf]` |
| Input | 4 file JSON trong `06_Data/` |
| Output | 7 file Markdown vào `build/` · với `--docx` xuất 7 docx · với `--pdf` xuất PDF danh mục cohort |
| Phụ thuộc | stdlib · `pandoc` (cho `--docx`/`--pdf`) · Chromium/Chrome/Edge (cho `--pdf`) |

| File Markdown (`build/`) | Đích với `--docx` |
|---|---|
| `Master_Project_Portfolio_AB.md` | `02_Project_Portfolio/Master_Project_Portfolio_AB.docx` |
| `Course_Project_Catalog.md` | `02_Project_Portfolio/Course_Project_Catalog.docx` |
| `Internship_Catalog.md` | `02_Project_Portfolio/Internship_Catalog.docx` |
| `Graduation_Thesis_Catalog.md` | `02_Project_Portfolio/Graduation_Thesis_Catalog.docx` |
| `Research_Opportunities_Catalog.md` | `02_Project_Portfolio/Research_Opportunities_Catalog.docx` |
| `Danh_muc_de_tai_DATN_Nhom_A_B_<cohort>.md` | `<root>/Danh_muc_de_tai_DATN_Nhom_A_B_<cohort>.docx` |
| `Phieu_lua_chon_va_danh_gia_de_tai_DATN_<cohort>.md` | `<root>/Phieu_lua_chon_va_danh_gia_de_tai_DATN_<cohort>.docx` |

**Hàm cần biết khi sửa script:**

- `star(s)` — **escape dấu `*` trong mọi chuỗi lấy nguyên văn từ JSON.** Bắt buộc. Không có nó, pandoc hiểu `*` của wildcard `A1-P*` là cú pháp in nghiêng, nuốt ký tự và làm lệch cả cụm bao quanh. Lỗi này từng lọt vào bản v1.1 phát hành.
- `esc(s)` — `star()` + thay `|` thành `/` + gộp xuống dòng; dùng cho ô bảng.
- `prereq_ref(t)` — bọc từng mã tiền đề vào code span để dấu `*` an toàn.
- `PREREQ_NOTE` — dòng chú giải quy ước wildcard, chèn vào Master + 4 catalog + danh mục cohort.
- `find_browser()` — tìm trình duyệt in PDF; ưu tiên `CHROME_BIN`, rồi PATH, rồi đường dẫn mặc định Windows/Linux.

**Failure mode:**
- Thiếu `pandoc` → `--docx`/`--pdf` lỗi; Markdown trong `build/` vẫn sinh bình thường.
- Không tìm thấy trình duyệt → `--pdf` thoát kèm thông báo chỉ cách đặt `CHROME_BIN`.
- Thiếu thư mục đích (`02_Project_Portfolio/`) → pandoc báo không ghi được file.

### 7.3 `scripts/generate_site.py`

| Mục | Nội dung |
|---|---|
| Lệnh | `python3 scripts/generate_site.py` |
| Input | 4 file JSON trong `06_Data/` |
| Output | `docs/index.html` (~140 KB, self-contained) + `build/site_artifact.html` |
| Phụ thuộc | stdlib |

Đọc `technical_readiness` và `working_readiness` từ rubrics (không đọc RR expectations). Escape bằng `html.escape()` nên **không dính bẫy `*`** của Markdown.

### 7.4 `scripts/release_cohort.py`

| Mục | Nội dung |
|---|---|
| Lệnh | `python3 scripts/release_cohort.py <thư_mục_đích>` — **bắt buộc nêu đích** |
| Input | 5 tài liệu cohort ở gốc repo |
| Output | Copy sang thư mục đích bất kỳ (USB, thư mục chia sẻ…) — **không còn đích mặc định**, `DATN_mentor` đã ngừng dùng (v1.4) |
| Phụ thuộc | stdlib |

Chỉ copy, **không xóa gì ở đích**. Báo lỗi rõ nếu thiếu file nguồn (chưa chạy generate) hoặc không thấy thư mục đích.

> Ghi chú v1.4: sau khi gộp một thư mục, script này chỉ còn là **công cụ xuất tùy chọn** (không nằm trong chuỗi bắt buộc). Từng bị cho nghỉ hưu rồi khôi phục trong cùng ngày — nay giữ lại với yêu cầu nêu rõ thư mục đích.

### 7.5 `scripts/build_release.py`

| Mục | Nội dung |
|---|---|
| Lệnh | `python3 scripts/build_release.py` |
| Input | `VERSION` + các thư mục/file trong danh sách `INCLUDE_*` |
| Output | `dist/DATN-Mentoring-HK1-2026-2027-v<VERSION>/` + `.zip` + `MANIFEST.md` + sha256 |
| Phụ thuộc | stdlib |

Phiên bản **đọc từ file `VERSION`** — không truyền tay, không đoán.
Không đóng gói `07_Private/`, `99_Archive/`, `build/`, `_to_delete/`, file tạm Office, file ẩn.

**Không dùng `rmtree`** — thư mục mount của Cowork không cho xóa file. Script ghi đè bằng `copy2` và **liệt kê file thừa** từ lần build trước để người dùng tự xử lý. ZIP chỉ đóng gói đúng danh sách file của lần build này, không quét cả thư mục.

### 7.6 Thứ tự chạy bắt buộc

```bash
python3 scripts/validate_portfolio.py               # 1. phải PASS
python3 scripts/generate_catalogs.py --docx --pdf   # 2. regenerate view
python3 scripts/generate_site.py                    # 3. nếu sửa dữ liệu đề tài
python3 scripts/build_release.py                    # 4. đóng gói dist/ + ZIP (khi phát hành mốc)
# (tùy chọn) xuất tài liệu cohort ra ngoài: python3 scripts/release_cohort.py <thư_mục_đích>
```

Không bao giờ chạy bước 2 khi bước 1 FAIL.

---

## 8. File sinh tự động — TUYỆT ĐỐI KHÔNG SỬA TAY

Mọi file dưới đây bị **ghi đè hoàn toàn** ở lần generate kế tiếp. Sửa tay = mất công.

| File | Sinh bởi | Sửa ở đâu thay thế |
|---|---|---|
| `02_Project_Portfolio/Master_Project_Portfolio_AB.docx` | `generate_catalogs.py --docx` | `06_Data/project_portfolio.json` |
| `02_Project_Portfolio/Course_Project_Catalog.docx` | nt | nt |
| `02_Project_Portfolio/Internship_Catalog.docx` | nt | nt |
| `02_Project_Portfolio/Graduation_Thesis_Catalog.docx` | nt | nt |
| `02_Project_Portfolio/Research_Opportunities_Catalog.docx` | nt | nt |
| `Danh_muc_de_tai_DATN_Nhom_A_B_HK1_2026_2027.docx` | nt | portfolio + cohort JSON |
| `Danh_muc_de_tai_DATN_Nhom_A_B_HK1_2026_2027.pdf` | `generate_catalogs.py --pdf` | nt |
| `Phieu_lua_chon_va_danh_gia_de_tai_DATN_HK1_2026_2027.docx` | `generate_catalogs.py --docx` | `readiness_rubrics.json` + cohort JSON |
| `docs/index.html` | `generate_site.py` | 4 file JSON |
| `build/*.md`, `build/*.html`, `build/print.css` | cả hai generator | — (trung gian, xóa được) |
| Sheet `Portfolio` trong workbook | Rebuild thủ công từ JSON | `project_portfolio.json` |

**File duy trì thủ công (sửa trực tiếp được):** mọi thứ trong `01_Governance/` · `03_Operations/` (trừ sheet Portfolio) · `04_Project_Template/` · `05_Claude/` · `00_START_HERE/` · `tests/` · `implementation-notes.*`.

Dấu hiệu nhận biết: mọi file sinh tự động đều mang dòng đầu *"File này được sinh tự động từ `06_Data/` (scripts/generate_catalogs.py). KHÔNG sửa tay."*

---

## 9. Validation và kiểm thử

### 9.1 Kiểm chứng bằng máy (23/08/2026)

| Kiểm tra | Kỳ vọng | Thực tế | Kết quả |
|---|---|---|---|
| `validate_portfolio.py` | exit 0 | 105 topics · rubrics · gates · 1 cohort · 0 lỗi | ✅ PASS |
| Không trùng mã đề tài | 105 mã duy nhất | 105 duy nhất | ✅ |
| `prereq_codes` resolve | 100% | 62/62 đề tài có prereq đều resolve | ✅ |
| Đề tài T có MVT | 28/28 | 28/28 | ✅ |
| Alias cohort khớp portfolio | 21/21 | 21/21 | ✅ |
| `career_guide` trỏ mã tồn tại | 100% | 0 mã lạ | ✅ |
| Gate deadline khớp `week_calendar` | 6/6 | 6/6 | ✅ |
| Generate 7 view | thành công | 7/7 | ✅ |
| Wildcard sống sót trong docx | ≥3 mã | `A1-P*`, `A3-P*`, `B1-P*` | ✅ |
| Wildcard sống sót trong PDF | ≥3 mã | như trên, 13 trang | ✅ |
| Wildcard sống sót trong `docs/index.html` | 10 mã | 10 mã | ✅ |
| Danh mục vẫn đủ 21 đề tài × 8 trường | 21 | 21 | ✅ |
| Workbook không chứa dữ liệu SV thật | 0 dòng | Students/Readiness/Weekly_Status đều 0 | ✅ |
| File tham chiếu trong FILE_MANIFEST tồn tại | 38/38 | 38/38 | ✅ |

### 9.2 Negative test cho validator (v1.2.1)

Cố tình làm hỏng dữ liệu để chứng minh validator thật sự bắt lỗi:

| Phá hoại | Kỳ vọng | Kết quả |
|---|---|---|
| `gate_deadlines['3']` = 2026-11-05 (lệch) | FAIL | ✅ *"Gate 3 deadline=2026-11-05 nhưng hết tuần 8 là 2026-11-02"* |
| `week_calendar[7].end` lệch 1 ngày | FAIL | ✅ *"week 9 bắt đầu…, không nối tiếp ngay sau…"* |
| RR `max_total` = 25 | FAIL | ✅ *"RR max_total=25 phải bằng 5 x scale.max=4"* |
| Xóa `expectations` key `R` | FAIL | ✅ *"RR expectations thiếu loại hoạt động có ngưỡng WR: ['R']"* |
| Khôi phục nguyên trạng | PASS | ✅ |

### 9.3 Dry-run quy trình (diễn tập giấy)

| Test | Nội dung | Kết quả |
|---|---|---|
| `tests/DRY_RUN_A_TRACK_A4-T01.md` | Luồng A sạch: admission → charter → 6 gate → legacy package | ✅ PASS |
| `tests/DRY_RUN_B_TRACK_B2-T01.md` | Luồng B có kịch bản **trượt Gate 3** → reduce scope → warning ladder | ✅ PASS |

**Ba điều dry-run phát hiện** (khuyến nghị vận hành, không chặn luồng):

1. Khi onboard, hướng dẫn SV chép `checkpoints_15w` của đề tài (in trong danh mục) vào mục "Milestone gates" của Project Charter.
2. Điều kiện probation hiện ghi ở cột `Notes` của sheet Students — cohort đông thì nên thêm cột `Conditions` riêng.
3. Khi reduce scope: phải cập nhật MVT ở **cả** charter lẫn cột MVT của Students.

### 9.4 Nghiệm thu

`05_Claude/ACCEPTANCE_CHECKLIST.md` — **36/36 mục ĐẠT**, chia 7 nhóm A–G. Hai mục ghi *"đạt có điều kiện vận hành"*: tách public/private, và trải nghiệm mentor — công cụ đầy đủ nhưng hiệu lực phụ thuộc kỷ luật sử dụng hằng tuần. Bằng chứng từng mục: `FINAL_SYSTEM_AUDIT.md`.

---

## 10. Quyết định thiết kế

| ID | Quyết định | Phương án khác đã cân nhắc | Lý do chọn | Ảnh hưởng |
|---|---|---|---|---|
| DEC-1 | JSON + script sinh view, thay vì soạn tay từng tài liệu | Giữ docx viết tay và dựa vào kỷ luật đồng bộ | v1.0 có 4–6 bản sao của cùng dữ liệu; lần sửa đề tài đầu tiên là chúng trôi khỏi nhau. Đây là rủi ro bảo trì nghiêm trọng nhất mà audit ghi nhận | 7 view + trang web sinh từ 1 nguồn |
| DEC-2 | Markdown/JSON + Python stdlib; không database, không framework | SQLite, static site generator, CMS | Một mentor bảo trì. Mọi file phải đọc/sửa được bằng editor thường và diff được bằng Git | Không dependency ngoài `pandoc` |
| DEC-3 | Mã chuẩn `<Family>-<Type><NN>` là định danh chính; alias cohort chỉ để đọc | Chỉ dùng mã ngắn cho SV dễ nhớ | Mã ngắn đổi theo kỳ; hồ sơ SV sống nhiều năm. Xung đột hai hệ mã ở v1.0 là finding Critical | Mọi phiếu/tracker/script ghi mã chuẩn |
| DEC-4 | Tách `milestone_gates.json` (logic) khỏi `cohort_*.json` (ngày) | Gộp một file | Logic gate ổn định qua nhiều kỳ; chỉ ngày đổi. Mở cohort mới = thêm 1 file, không đụng gate | Cohort mới không có rủi ro hồi quy |
| DEC-5 | Catalog P/I là bảng tóm tắt; T/R có chi tiết + MVT | Cho mọi catalog cùng độ chi tiết | SV giai đoạn P/I chưa cần MVT; thông tin thừa gây chọn đề tài vượt readiness | Catalog P/I gọn, dễ đọc |
| DEC-6 | Tách `07_Private/` bằng `.gitignore`, không mã hóa | Mã hóa file, hoặc dựa vào cẩn thận thủ công | Cơ chế đơn giản, không quên được; mã hóa thêm rào cản mà mentor không cần | Dữ liệu SV không lọt repo public |
| DEC-7 | Escape `*` ở **tầng render** (`star()`), không sửa dữ liệu nguồn | Bỏ `*` khỏi `prereq_codes`, đặt quy ước khác | `*` là ngữ nghĩa thật của dữ liệu (wildcard). Lỗi nằm ở chỗ Markdown trùng cú pháp — phải sửa đúng nơi phát sinh | Mọi chuỗi từ JSON đi qua `star()` |
| DEC-8 | Bọc mã tiền đề trong code span thay vì chữ thường | In nghiêng như cũ | Code span vừa bảo vệ `*`, vừa cho người đọc tín hiệu "đây là mã, không phải văn xuôi" | Danh mục dễ đọc hơn |
| DEC-9 | RR **không** có ngưỡng số, chỉ tổng /20 + kỳ vọng định tính | Đặt ngưỡng số song song WR (vd ≥12 cho research-oriented) | Nguồn chuẩn chỉ định nghĩa RR định tính. Đặt ngưỡng số sẽ là **chính sách tự chế**, không suy ra được từ nguồn — vi phạm quy tắc "không thay nội dung nguồn bằng suy đoán" | Mentor kết luận RR bằng nhận định + evidence |
| DEC-10 | PDF in bằng Chromium headless từ HTML, không dùng LaTeX | `pandoc --pdf-engine=xelatex` | LaTeX cần cài đặt nặng và hay vỡ với tiếng Việt; Chromium đã có sẵn trên hầu hết máy | PDF tái lập được bằng 1 lệnh |
| DEC-11 | Bảng dài được phép ngắt trang, lặp dòng tiêu đề (`thead` group) | `break-inside: avoid` cả bảng | Để nguyên khối thì bảng lớn bị đẩy sang trang mới và để lại nửa trang trắng | PDF 13 trang, không trang trống |
| DEC-12 | Giữ `99_Archive/2026-08-23_v1.0/` thay vì xóa | Xóa vì đã có Git | Repo chưa chắc luôn ở trong Git; regenerate là thao tác phá hủy nên cần đường lùi độc lập | 13 file lưu trữ, `.gitignore` chặn |

---

## 11. Hạn chế đã biết (chấp nhận được, cần biết)

1. **Định dạng docx sinh tự động đơn giản hơn bản thiết kế tay.** Dùng style mặc định của pandoc — sạch, in tốt, nhưng không có letterhead/thiết kế như bản v1.0 (`99_Archive/`). Nội dung đã kiểm chứng khớp nguồn 100%. Muốn đẹp hơn: thêm `--reference-doc` cho pandoc, không ảnh hưởng dữ liệu.
2. **Dry-run mới là diễn tập giấy.** Hệ thống chưa chạy qua một cohort thật. Nghiệm thu nhóm E xác nhận *công cụ*, chưa xác nhận *thói quen sử dụng*. Vòng thật đầu tiên là HK1 2026–2027.
3. **Validator kiểm cấu trúc, không kiểm học thuật.** Nó bắt được mã trùng, field rỗng, lịch lệch — không bắt được một đề tài có scope sai chuyên môn hay MVT không khả thi. Tính đúng đắn kỹ thuật vẫn thuộc trách nhiệm mentor.
4. **Governance docx viết tay, không sinh từ 06_Data.** Handbook §5.2 chép cứng ngưỡng WR (≥10/12/14/15/16/17) trùng với `readiness_rubrics.json`. Sửa ngưỡng trong JSON **không** tự cập nhật Handbook → §12 UNRESOLVED-3.
5. **Sức chứa workbook là giới hạn tĩnh:** 100 SV · 1500 dòng weekly · 100 block gate. Đủ cho nhiều cohort, nhưng vượt thì phải mở rộng template thủ công.
6. **PDF sinh bằng Chromium headless.** Cần bản in chính thức có header/footer của Khoa thì mở docx trong Word rồi export.
7. **`FINAL_SYSTEM_AUDIT.md` có hai mục đã lỗi thời:** mục 3.4 nói "website public chưa xây" (đã xây ở v1.2) và mục 3.7 nói PDF in thủ công (đã tự động hóa ở v1.2.1). Giữ nguyên như bản ghi lịch sử; tài liệu này là bản cập nhật.
8. **Nhiều phiên AI có thể chạy song song trên repo.** Đã xảy ra ngày 23/08. Luôn kiểm thời gian sửa file trước khi ghi đè.

---

## 12. Sổ rủi ro và tồn đọng

### 12.1 Sổ rủi ro — toàn bộ lịch sử

Mọi finding từ `AUDIT_REPORT.md` (C/H/M/L) và từ lượt rà soát v1.2.1 (R1–R6). Chi tiết các mục còn mở nằm ngay dưới bảng.

| ID | Mức | Rủi ro | Trạng thái |
|---|---|---|---|
| C1 | 🔴 Critical | Hai hệ mã đề tài xung đột | ✅ **Đã đóng** — danh mục v1.1 dùng mã chuẩn + alias (CR-1) |
| C2 | 🔴 Critical | Hai thang readiness mâu thuẫn | ✅ **Đã đóng** — phiếu v1.1 theo rubrics JSON (CR-2) |
| C3 | 🟠 High | Workbook tự đặt thang RR | ✅ **Đã đóng** — RR 0–4 chuẩn hóa vào JSON |
| H1 | 🟠 High | root-A8/B11 không có trong nguồn chuẩn | ✅ **Đã đóng** — thêm `A2-T03`, `B5-T03` (CR-3) |
| H2 | 🟠 High | JSON thiếu MVT/tools/eligibility/career/status | ✅ **Đã đóng** — schema v1.1, 28/28 đề tài T có MVT |
| H3 | 🟠 High | rubrics JSON thiếu ngưỡng + 16 năng lực TR | ✅ **Đã đóng** |
| H4 | 🟠 High | Chưa có script validate/generate | ✅ **Đã đóng** — 2 script hoạt động, VALIDATION PASS |
| H5 | 🟠 High | Public/private chưa tách cơ chế | ✅ **Đã đóng (cơ chế)** — `07_Private/` + `.gitignore`; ⚠ kỷ luật sử dụng: dữ liệu thật phải lưu vào 07_Private |
| M1 | 🟡 Medium | Invariant B6 vs B6-T02 | ✅ **Đã đóng** — Handbook + CONTEXT tách nhánh detection/ranking |
| M2 | 🟡 Medium | JSON positional | ✅ **Đã đóng** — keyed objects |
| M3 | 🟡 Medium | Mốc hành chính lặp; điều kiện cứng ngoài nguồn chuẩn | ✅ **Đã đóng** — `cohort_HK1_2026_2027.json` |
| L | ⚪ Low | "Lucero" | ✅ **Đã đóng** — là bút danh tác giả (Mr. Lucero Dinh = ThS. Đinh Văn Nam); tên chương trình thống nhất "Engineering & Research Mentoring Program (Lucero)" |
| L | ⚪ Low | COUNTIF Dashboard; capacity sheet | ✅ **Đã đóng** — COUNTA; 100 SV / 1500 dòng tuần / 600 dòng gate |
| L | ⚪ Low | Numbering continuation trong Handbook (§6→§9) | ✅ **Đã đóng (v1.1.1)** — danh sách §9 khởi động lại 1–5 (sửa numbering override trong docx) |
| R1 | 🟠 High | Bug escape Markdown nuốt wildcard `A1-P*` trong danh mục/portfolio đã phát hành | ✅ **Đã đóng (v1.2.1)** — `star()` + code span; regenerate 7 view |
| R2 | 🟡 Medium | `research_readiness.expectations` là dead data → RR không có quy tắc quyết định | ✅ **Đã đóng (v1.2.1)** — Phiếu 5.2 có tổng /20 + bảng kỳ vọng |
| R3 | 🟡 Medium | Phiếu không có ô ghi Level → không đối chiếu được `min_level` của đề tài | ✅ **Đã đóng (v1.2.1)** — 3 dòng Level trong Phiếu 5.3 |
| R4 | 🟡 Medium | Validator không cross-check `gate_deadlines` với `week_calendar` → lịch dễ trôi khi sửa | ✅ **Đã đóng (v1.2.1)** — có negative test |
| R5 | ⚪ Low | PDF danh mục in thủ công, không có lệnh tái lập | ✅ **Đã đóng (v1.2.1)** — `generate_catalogs.py --pdf` |
| R8 | 🟠 Theo dõi | Prompt master từng nằm cạnh README mâu thuẫn trong `DATN_mentor` → phiên mới dựng trùng hệ thống | ✅ **Đã đóng (v1.4)** — prompt chuyển về `05_Claude/`; cảnh báo trong `CLAUDE.md` §0 + QUICK_LAUNCH; `DATN_mentor` đã xóa (23/08/2026) |
| R7 | 🟠 Theo dõi | Cần xóa tay: `EEE Projects/_to_delete/` và toàn bộ thư mục `DATN_mentor` (đã ngừng dùng) | ⏳ **Mở một nửa** — ✅ `DATN_mentor` đã xóa (23/08/2026); còn `EEE Projects/_to_delete/` chờ xóa tay. Xem UNRESOLVED-6 |
| R6 | 🟡 Theo dõi | Readiness test 2 tuần không kịp trước hạn Khoa chốt danh sách đề tài | ⏳ **Mở — cần mentor quyết**: hoặc "nhận có điều kiện" trước hạn Khoa rồi hoàn tất readiness test trong tuần 1–2 (hợp nhất vào Gate 1), hoặc nén mini-task xuống 4–6h để kịp hạn nộp hồ sơ. Chưa sửa tài liệu nào theo hướng nào |
| — | 🟡 Theo dõi | Bản v1.0 của danh mục/phiếu có thể đã phát cho một số SV | ⏳ Mở — **release note đã soạn sẵn** (`RELEASE_NOTE_HK1_2026_2027.docx`, có bảng đối chiếu mã); mentor chỉ cần gửi kèm khi phát bản hiện hành (tài liệu in "Phiên bản 1.4.0") |

### 12.2 Chi tiết các mục còn mở

### UNRESOLVED-1 · ⚠ Xung đột lịch readiness test — cần mentor quyết trước 25/08

Quy trình bắt buộc readiness test **2 tuần** (Phiếu 4: literature task + mini-task 4–10h + oral check) *trước* bước giao đề tài. Nhưng Khoa chốt danh sách giao đề tài trước ngày nhập học. Khởi động muộn thì readiness test xong **sau hạn**.

| Phương án | Nội dung | Đánh đổi |
|---|---|---|
| A | "Nhận có điều kiện" trước hạn Khoa dựa trên Phiếu 1–3 + oral check ngắn; readiness test đầy đủ chạy trong tuần 1–2 và hợp nhất vào Gate 1 | Giữ nguyên chất lượng đánh giá, nhưng phải có quy tắc đổi đề tài rõ ràng nếu readiness không đạt ở tuần 2 |
| B | Nén mini-task xuống 4–6 giờ để kịp hạn nộp hồ sơ | Kịp hạn hành chính, nhưng evidence mỏng hơn — rủi ro giao nhầm đề tài advanced |

**Trạng thái:** chưa sửa tài liệu theo hướng nào. Chọn xong thì cập nhật §0 và Phiếu 4 (qua `generate_catalogs.py`).

### UNRESOLVED-2 (✅ ĐÃ ĐÓNG ở v1.3.1 — phiếu cũ đã lưu trữ vào 99_Archive) · ⚠ Hai bộ phiếu readiness cùng tồn tại

`01_Governance/Readiness_and_Topic_Selection_Forms.docx` (v1.0, viết tay) và `Phieu_lua_chon_va_danh_gia_de_tai_DATN_HK1_2026_2027.docx` (v1.2.1, sinh tự động) **đều tự gọi mình là "Phiếu 1–5"** nhưng khác nhau về cấu trúc:

| | Bản governance v1.0 | Bản sinh tự động v1.2.1 |
|---|---|---|
| Phiếu 1 | Cột "Mã đề tài" | Cột "**Mã chuẩn** đề tài" |
| Phiếu 2 | Năng lực ghi tiếng Anh (*Digital Communications*, *Probability*) | Tiếng Việt, khớp `readiness_rubrics.json` |
| Phiếu 3 | = Working Readiness (lưới 0–4) | = Cam kết thời gian; WR nằm ở 5.1 |
| Phiếu 4 | Không có cột "Kết quả" | Có ô Đạt/Chưa đạt |
| Phiếu 5 | Không có dòng Level, không có ngưỡng WR | Có 3 dòng Level + bảng kỳ vọng RR |

Bản sinh tự động ghi rõ *"bản duy nhất, thang điểm chuẩn. Không dùng các bản phiếu cũ"* — nhưng `FILE_MANIFEST.md` vẫn liệt kê bản governance một cách trung tính là *"bộ phiếu governance (Phiếu 1–5)"*. **Rủi ro thật: in nhầm phiếu.**

**Khuyến nghị:** chuyển `Readiness_and_Topic_Selection_Forms.docx` vào `99_Archive/`, hoặc đổi tên thành `..._SUPERSEDED_v1.0.docx` và sửa dòng mô tả trong FILE_MANIFEST. Chưa làm vì đây là file governance có thể còn dùng cho P/I/R (không chỉ DATN) — cần mentor xác nhận.

### UNRESOLVED-3 (✅ ĐÃ ĐÓNG ở v1.3.1 — Handbook đã có ghi chú nguồn chuẩn) · Trùng lặp giữa Handbook và `readiness_rubrics.json`

Handbook §5.2 và sheet `Rubrics` của workbook đều chép cứng ngưỡng WR. Sửa JSON không tự lan sang hai chỗ đó.

**Ba hướng:** (a) chấp nhận, thêm ghi chú *"nguồn chuẩn: readiness_rubrics.json"* vào Handbook — rẻ nhất; (b) sinh phần §5 của Handbook từ JSON — đúng kiến trúc nhưng Handbook là docx thiết kế tay; (c) bỏ số khỏi Handbook, chỉ trỏ sang phiếu. **Hiện đang ngầm theo (a)** nhưng ghi chú chưa được viết vào Handbook.

### UNRESOLVED-4 (✅ ĐÃ ĐÓNG ở v1.3.1 — nhãn Version 1.3 trên 6 docx; từ 23/08 đồng bộ tiếp lên 1.4.0) · Governance docx còn ghi "Version 1.0"

Cả 5 file trong `01_Governance/` mang nhãn *"Version 1.0 | 23/08/2026"* trong khi hệ thống đã ở v1.2.1. Nội dung policy chưa đổi nên không sai, nhưng người đọc dễ tưởng tài liệu cũ. Cần một lượt cập nhật nhãn phiên bản.

### UNRESOLVED-7 · ✅ Prompt master mâu thuẫn với README — ĐÃ ĐÓNG ở v1.4

`DATN_mentor/CLAUDE_MASTER_EXECUTION_DATN_MENTORING.md` **không nêu tên thư mục nào** — chỉ nói *"Start by recursively inspecting the full working directory"*, liệt kê `06_Data/` và `scripts/` là đầu vào, rồi §35 ra lệnh *"implement missing project components… until Definition of Done"*.

Phiên Claude mở `DATN_mentor` sẽ thấy thiếu toàn bộ hệ thống và **dựng lại một bản trùng lặp ngay tại đó** — trong khi `README.md` cùng thư mục nói ngược lại. **Đã xảy ra một lần ngày 23/08 và phải đảo ngược.**

**Đã đóng (v1.4):** prompt chuyển về `05_Claude/CLAUDE_MASTER_EXECUTION_DATN_MENTORING.md` (nội dung giữ nguyên — tài liệu của tác giả); `CLAUDE.md` §0 và `QUICK_LAUNCH_PROMPT.txt` cảnh báo rõ đây là đặc tả xây dựng, không phải lệnh dựng lại; `DATN_mentor` đã xóa (23/08/2026) nên không còn ngữ cảnh gây dựng trùng.

### UNRESOLVED-6 · ⚠ Còn rác chờ xóa tay

Sau ba lần tái cấu trúc cùng ngày 23/08 (gom nhầm v1.2.3 → tách v1.3 → **gộp một thư mục v1.4, quyết định cuối của chủ dự án**), mọi nội dung đã nằm đủ và duy nhất trong `EEE Projects` (đã đối chiếu từng byte trước khi dọn).

**Việc cần làm (xóa tay — phiên làm việc không có quyền xóa):**
1. Xóa thư mục `EEE Projects/_to_delete/`.
2. ~~Xóa **toàn bộ thư mục `C:\Users\admin\Downloads\DATN_mentor`**~~ — ✅ **ĐÃ XONG** (chủ dự án xóa 23/08/2026, đã kiểm tra lại: thư mục không còn tồn tại).

⚠ TUYỆT ĐỐI KHÔNG xóa thư mục `EEE Projects` — đó là toàn bộ dự án.

### UNRESOLVED-5 · ✅ `FILE_MANIFEST.md` ghi lệnh regenerate cũ — đã sửa 23/08

Mục "Nguyên tắc nguồn chuẩn" điểm 3 ghi `generate_catalogs.py --docx`, thiếu `--pdf` và bước `generate_site.py` — mâu thuẫn với §7.4 và §20 của tài liệu này. **Đã cập nhật FILE_MANIFEST** thành chuỗi đầy đủ `validate → generate_catalogs --docx --pdf → generate_site → CHANGELOG`, kèm trỏ về §20.

---

## 13. Vận hành hệ thống — quy trình chuẩn

### 13.1 Chu trình một tuần (lặp 15 lần)

1. **Trước meeting** — SV nộp Weekly Report (header định danh + link evidence + AI use). Mentor skim, đánh dấu blocker/decision cần xử lý. *Không đọc lại lịch sử chat để đoán tiến độ.*
2. **Trong meeting** — SV trình theo trục **Goal → Evidence → Failure → Diagnosis → Proposed next step → Question**. Mentor dùng teach-back/oral check để xác nhận hiểu, không hỏi "em hiểu chưa?". Tranh luận kỹ thuật giải bằng literature hoặc experiment nhỏ, không bằng thẩm quyền.
3. **Cuối meeting** — chốt **1–3** deliverable + deadline thực tế. Ghi Meeting Record + risk Green/Yellow/Red.
4. **Sau meeting** — mọi decision/scope change vào workbook (`Weekly_Status` + `Milestones`). SV tự cập nhật action item. *Mentor không giữ task trong trí nhớ riêng.*

### 13.2 Kiểm tra "dưới 1 phút" mỗi sáng thứ Hai

Mở workbook → sheet **Students** → nhìn 4 cột: `Risk`, `Last Evidence`, `Next Deliverable`, `Next Deadline`.
Ai **Yellow/Red** hoặc evidence quá **7 ngày** → mở `Weekly_Status` của SV đó → hành động theo thang cảnh báo.

### 13.3 Thang cảnh báo

| Mức | Kích hoạt | Hành động |
|---|---|---|
| Nhắc | 1 chu kỳ thiếu update | Nhắn hỏi blocker, xác nhận lại deadline |
| Formal warning | 2 chu kỳ liên tiếp thiếu evidence | Warning + recovery plan ngắn có thời hạn |
| Scope review | Trượt Gate 2 hoặc Gate 3 | Chẩn đoán 3 biến — *task difficulty × time allocation × learning strategy* → reduce scope, giữ chuẩn kỹ thuật |
| Dừng extension / chuyển track | Tiếp tục disengage sau warning + support | Theo quy định đơn vị; **không cứu ở phút cuối** |

### 13.4 Phân bổ thời gian mentor

**Common mentoring 50–60%** (Git, literature, report, AI, experiment, presentation — dạy một lần cho cả nhóm) · **Theme mentoring 25–35%** (nhóm A hoặc nhóm B chia sẻ vấn đề chung) · **Individual 15–20%** (algorithm khó, bug khó, scope, research decision).

> Nếu thấy mình đang debug hộ một SV hàng giờ → sai nhịp. Quay lại thang cảnh báo.

### 13.5 Khẩu quyết đánh giá evidence

"Đã đọc / đã tìm hiểu" **không phải** tiến độ. Evidence = code · commit · schematic · PCB · đo đạc · waveform · log · figure · bảng số · test · report · demo.
Sản phẩm có AI hỗ trợ mà SV không giải thích được = **chưa hoàn thành**, giao làm lại.

---

## 14. Quy trình: thêm một sinh viên mới

1. **Thu Phiếu 1–3** — thông tin, Top-3 nguyện vọng (**ghi mã chuẩn**), TR tự đánh giá, cam kết thời gian.
2. **Giao readiness test** (Phiếu 4) — literature task + technical mini-task 4–10h + oral check 5–10 phút. Chọn mini-task chạm đúng prerequisite quan trọng nhất của đề tài Top-1.
3. **Chấm Phiếu 5** — WR (/20), RR (/20 + nhận định), TR đã kiểm chứng bằng mini-task, **Level của SV**, đối chiếu với `min_level` của đề tài đề xuất.
4. **Đối chiếu prerequisite** — mở đề tài trong danh mục, đọc dòng *"Đầu vào … (mã tham chiếu: …)"*. Mã có `*` nghĩa là "ít nhất một đề tài loại đó trong family, hoặc năng lực tương đương **có evidence**".
5. **Kết luận** — Nhận / Nhận có điều kiện / Đổi scope-đề tài / Chưa nhận. Ghi lý do. *Override ngưỡng được phép nhưng bắt buộc ghi lý do.*
6. **Onboarding tuần 1** — ký Working Agreement · tạo repo từ `04_Project_Template/` · chép `checkpoints_15w` của đề tài vào Project Charter · chốt **MVT và Research Extension tách biệt** · đăng charter.
7. **Nhập workbook** — sheet `Students` (1 dòng) + sheet `Readiness` (điểm TR/WR/RR) + `Milestones` (6 dòng gate).
8. **Lưu riêng tư** — workbook đã có dữ liệu thật → `07_Private/`. Phiếu giấy đã điền (email/SĐT) → một nơi duy nhất do mentor giữ.

---

## 15. Quy trình: thêm hoặc sửa một đề tài

1. **Mở `06_Data/project_portfolio.json`.**
2. **Thêm/sửa record** theo schema §5.2. Bắt buộc: `code` không trùng, đúng format, khớp `family`+`type`; 13 field bắt buộc không rỗng; `min_level` trong 0–5.
3. **Nếu `min_level ≥ 3`:** bắt buộc có `prerequisites` (mô tả) **và** `prereq_codes` (máy đọc được). Mã chính xác phải tồn tại; pattern `X-Y*` phải khớp ít nhất một đề tài thật.
4. **Nếu type = T:** bắt buộc có `mvt`.
5. **Nếu mở cho cohort hiện tại:** thêm `cohort_alias` + `checkpoints_15w` vào record, **và** thêm cặp `{alias, code}` vào `topics[]` của `cohort_*.json`. Hai chỗ phải khớp — validator kiểm.
6. **Nếu muốn đưa vào bảng gợi ý nghề nghiệp:** thêm mã vào `career_guide` trong cohort JSON.
7. **Chạy `validate_portfolio.py`** — phải PASS. Đọc kỹ thông báo lỗi, chúng chỉ đích danh field.
8. **Regenerate** theo §20.
9. **Ghi CHANGELOG** — mã nào, đổi gì, vì sao.

> **Không bao giờ đổi `code` của đề tài đã giao cho SV.** Muốn đổi tên hiển thị thì sửa `title_vi`/`title_en`; mã là định danh vĩnh viễn trong hồ sơ.
> **Gỡ đề tài khỏi lưu hành:** đổi `status` thành `archived`, **không xóa record** — hồ sơ SV cũ vẫn phải tra được.

---

## 16. Quy trình: chạy weekly review

**Chuẩn bị (10 phút):** đọc Weekly Report của SV; mở `Weekly_Status` xem tuần trước chốt gì; kiểm evidence link có mở được không.

**Trong buổi (30–45 phút nhóm, hoặc 15–20 phút cá nhân):**

| Bước | Hỏi gì | Dấu hiệu cần chú ý |
|---|---|---|
| 1. Goal | Tuần trước chốt gì? | SV không nhớ → quy trình ghi chép hỏng |
| 2. Evidence | Cho xem, không kể lại | Chỉ có lời nói, không có artifact → chưa có tiến độ |
| 3. Failure | Cái gì không chạy? | "Mọi thứ ổn" liên tục nhiều tuần → nghi ngờ |
| 4. Diagnosis | Vì sao em nghĩ nó hỏng? | Không có giả thuyết → thiếu kỹ năng chẩn đoán, cần dạy |
| 5. What tried | Đã thử gì để kiểm chứng? | Không thử gì → kiên trì (WR) thấp |
| 6. Next step | Em đề xuất làm gì tiếp? | Hỏi ngược "em làm gì tiếp?" → chủ động (WR) thấp |
| 7. Ownership | Giải thích dòng code/công thức/figure bất kỳ | Không giải thích được → task **chưa đạt**, làm lại |

**Kết thúc:** chốt tối đa 3 deliverable + deadline · gán risk Green/Yellow/Red · ghi Meeting Record · cập nhật `Weekly_Status`.

---

## 17. Quy trình: chạy gate review

1. **Mở `Milestones`** của SV, tìm dòng gate đang tới hạn. Cột `Requirement` đã prefill từ `milestone_gates.json`.
2. **Đối chiếu evidence với `pass_criteria`** — dùng đúng câu chữ trong nguồn, không nới ngầm.
3. **Kết luận** một trong: `PASS` · `CONDITIONAL_PASS` (kèm điều kiện + hạn) · `FAIL` · `NOT_ENOUGH_EVIDENCE`.
4. **Áp hard rule tương ứng:**

| Gate | Nếu không đạt |
|---|---|
| 1 | Điều chỉnh đề tài hoặc learning plan |
| 2 | **Research extension đóng.** Không thương lượng — đây là quy tắc trung tâm của chương trình |
| 3 | **Reduce scope.** Thứ tự cắt: bỏ extension → giảm parameter sweep → giảm số kiến trúc → thu nhỏ subsystem → **giữ nguyên** MVT, verification, reproducibility, ownership |
| 4 | Không thêm thuật toán lớn mới sau tuần 11 |
| 5 | Ưu tiên hoàn thiện core; không dùng writing polish che lỗ hổng kỹ thuật |
| 6 | Chỉ xác nhận hoàn thành khi **đủ cả ba**: technical completion + reproducibility + student ownership |

5. **Ghi vào `Milestones`:** Status, Evidence, Decision/Action, Reviewed Date. Scope change phải ghi cả ở charter và cột MVT của `Students`.

> **Nguyên tắc:** khi trễ tiến độ, **giảm scope — không hạ chuẩn kỹ thuật, không để mentor làm thay.** Một khóa luận đúng, hoàn chỉnh và SV hiểu sâu tốt hơn một khóa luận "đẹp" nhưng ownership thấp.

---

## 18. Quy trình: mở research extension

Extension mặc định **CLOSED**. Chỉ mở khi đủ **cả 8** điều kiện:

- [ ] Baseline đã verify (Gate 2 PASS)
- [ ] Core implementation ổn định
- [ ] Lịch còn dư địa (thường nghĩa là trước tuần 9)
- [ ] Câu hỏi nghiên cứu rõ ràng
- [ ] Giả thuyết hoặc mục tiêu so sánh rõ ràng
- [ ] Metric quyết định kết quả đã định nghĩa
- [ ] SV thể hiện research ownership (đối chiếu RR)
- [ ] **Extension thất bại không phá vỡ tính hợp lệ của DATN core**

**Đề xuất extension phải trả lời 7 câu:**

1. Câu hỏi nghiên cứu là gì?
2. Baseline là gì?
3. Cái gì thay đổi?
4. Cái gì được giữ cố định (controlled)?
5. Metric nào quyết định kết quả?
6. Evidence nào có thể **bác bỏ** giả thuyết?
7. Fallback là gì nếu extension thất bại?

**Riêng đề tài ML-assisted (family B6):** không chấp nhận kết quả neural nếu thiếu so sánh với heuristic/classical baseline tương ứng. Đây là invariant, không phải khuyến nghị.

---

## 19. Quy trình: chuẩn bị bảo vệ và closeout

**Gate 6 (tuần 14–15)** yêu cầu đủ ba trục: **technical completion + reproducibility + student ownership**.

**Reproducibility check:** một người khác (hoặc mentor) chạy lại từ hướng dẫn sạch, không hỏi miệng. Không pass = chưa xong.

**Legacy package — 11 mục** (`04_Project_Template/LEGACY_PACKAGE_CHECKLIST.md`):
README + hướng dẫn chạy lại · source code + config/environment (pinned version) · tests/regression pass · results + figures + data traceable về script · literature notes · `KNOWN_ISSUES.md` · `NEXT_STEPS.md` (câu hỏi kỹ thuật cụ thể, không chung chung) · report/thesis/slides bản cuối · `AI_USAGE_LOG.md` · reproducibility check PASS · oral check ownership PASS.

**10 câu Definition of Done** (SOP §10) — SV phải trả lời trôi chảy:
Bài toán là gì? · Tại sao nó tồn tại? · Baseline là gì? · Em đã xây gì? · Làm sao biết nó đúng? · Metric nào? · Kết quả nói lên điều gì? · Limitation là gì? · Người khác chạy lại được không? · Nếu thêm 3 tháng, next step là gì?

**Sau bảo vệ:** đánh giá nên mời SV tiếp tục NCKH hay chuyển hướng engineering/industry. *Không ép mọi SV thành researcher — engineering excellence và research excellence đều có giá trị.*

---

## 20. Quy trình: regenerate toàn bộ đầu ra

```bash
cd "EEE Projects"

# 1. Kiểm nguồn chuẩn — BẮT BUỘC PASS trước khi đi tiếp
python3 scripts/validate_portfolio.py

# 2. Sinh 7 view (Markdown → docx) + PDF danh mục cohort
python3 scripts/generate_catalogs.py --docx --pdf

# 3. Sinh trang web công khai (khi có sửa dữ liệu đề tài)
python3 scripts/generate_site.py
```

**Yêu cầu môi trường:** Python 3 (stdlib) · `pandoc` cho `--docx`/`--pdf` · Chromium/Chrome/Edge cho `--pdf`.
Trình duyệt không nằm trên PATH → đặt biến môi trường:

```bash
# Windows (PowerShell)
$env:CHROME_BIN = "C:\Program Files\Google\Chrome\Application\chrome.exe"
# Linux / macOS
export CHROME_BIN=/usr/bin/chromium
```

**Sau khi regenerate — kiểm nhanh:**

- Mở danh mục docx, tìm dòng *"Đầu vào … (mã tham chiếu: `A1-P*`)"* — dấu `*` **phải còn**.
- Đếm số đề tài trong danh mục cohort = số phần tử `topics[]` của cohort JSON.
- Mở phiếu, kiểm mục 5.3 có đủ 3 dòng Level.
- Ghi `00_START_HERE/CHANGELOG.md`.

---

## 21. Sao lưu và phục hồi

**Trước mỗi lần thay đổi lớn:**

1. Nếu repo trong Git: commit trạng thái sạch trước khi sửa.
2. Nếu không: copy 4 file `06_Data/*.json` sang thư mục có ngày tháng.
3. Bản gốc v1.0 đã lưu tại `99_Archive/2026-08-23_v1.0/` (13 file: 4 JSON cũ + 8 docx/xlsx + 1 pdf).

**Phục hồi khi generate ra kết quả sai:** không sửa tay file view. Khôi phục JSON từ bản sao → `validate_portfolio.py` → generate lại. Mọi view sinh lại được 100% từ 4 file JSON, nên **chỉ cần backup `06_Data/`** là đủ để dựng lại toàn bộ tầng tài liệu sinh tự động.

**Cần backup riêng (không sinh lại được):** `01_Governance/` · `03_Operations/` · `04_Project_Template/` · `05_Claude/` · `07_Private/` · `tests/` · `implementation-notes.*`.

**Nhiều phiên làm việc song song:** trước khi ghi đè, kiểm thời gian sửa gần nhất của file. Việc này đã cứu một lần vào 23/08 khi hai phiên cùng chạm repo.

---

## 22. Đóng gói và phát hành

**Phát cho sinh viên — chỉ 3 thứ:**

1. `Danh_muc_de_tai_DATN_Nhom_A_B_HK1_2026_2027.pdf` — dễ đọc trên điện thoại
2. `Phieu_lua_chon_va_danh_gia_de_tai_DATN_HK1_2026_2027.docx` — SV điền Phiếu 1–4
3. Link `docs/index.html` (GitHub Pages hoặc artifact) — tra cứu có bộ lọc

**Tuyệt đối không phát:** workbook có dữ liệu · nội dung `07_Private/` · Master Portfolio đầy đủ (chứa cả research roadmap nội bộ) · `AUDIT_REPORT.md` / `FINAL_SYSTEM_AUDIT.md` / `implementation-notes.*` (tài liệu nội bộ của mentor).

**Trước khi phát — kiểm 5 điểm:**

- [ ] `validate_portfolio.py` PASS
- [ ] Danh mục và phiếu vừa regenerate từ nguồn chuẩn hiện tại
- [ ] Số phiên bản + ngày trên tài liệu là mới nhất
- [ ] Không có tên/email/điểm SV nào trong file định phát
- [ ] Nếu bản trước đã đến tay SV → gửi kèm release note có bảng đối chiếu thay đổi

**Mở cohort mới (kỳ sau):** tạo `06_Data/cohort_<id>.json` mới · thêm `cohort_alias` cho các đề tài mở · validate · generate — generator tự sinh danh mục + phiếu cho mọi file `cohort_*.json`. **Không sửa file cohort cũ** — hồ sơ SV khóa trước phải tra được.

---

## 23. Changelog tài liệu

### 23/08/2026 — v1.5.1: gỡ thông tin hành chính cohort

Quyết định chủ dự án: khối "Mốc hành chính" (đăng ký QLĐT, học phí, phiếu giao đồ án, hạn Khoa chốt) và "Điều kiện đăng ký" gỡ khỏi **mọi nơi** — xóa `admin_milestones` + `eligibility` khỏi cohort JSON, xóa `eligibility_rules` khỏi portfolio JSON, generator không in các khối này nữa; các mốc ngày hành chính trong tài liệu vận hành thay bằng mô tả trung tính ("theo hạn Khoa công bố"). Lịch 15 tuần + 6 gate giữ nguyên (xương sống sư phạm, không phải thông tin hành chính). Validator PASS 105.

### 23/08/2026 — v1.5.0: mở nhánh Nhúng & IoT + co-design luận án (tài liệu 2.3)

Quyết định chủ dự án: chương trình phục vụ dài hạn nhiều học kỳ, không chỉ HK1 2026-2027; bổ sung danh mục chuẩn hóa hướng vi mạch × nhúng/IoT × co-design. Thêm **A6** (Embedded & SoC, 8 đề tài) và **A7** (IoT & Edge Intelligence, 8 đề tài) vào trục A; **AB** nới phạm vi co-design (Polar/edge-AI × ràng buộc IoT) thêm 5 đề tài — AB-T05 (tăng tốc AI biên), AB-T06 (decoder Polar tiết kiệm năng lượng cho IoT), AB-R02/R03 (đề tài R định hướng luận án). Tổng 105 đề tài / 16 nhóm (42 P · 15 I · 34 T · 14 R); mọi đề tài T mới có MVT; validator mở rộng `A[0-7]`, PASS 105. Toàn bộ view sinh lại (catalog, danh mục+phiếu HK1 in 1.5.0, site 105 card, PDF, workbook Portfolio, bản đồ `Ban_do_de_tai` — đổi tên từ `Ban_do_84_de_tai` cho bền theo thời gian). Danh mục HK1 vẫn đúng 21 đề tài mở.

### 23/08/2026 — hoàn thiện v1.4.0: đồng bộ nhãn phiên bản (tài liệu 2.2)

Rà soát hoàn thiện phát hiện 6 docx chính sách/vận hành còn in "Version 1.3" và release note còn ghi "hệ thống v1.3" trong khi danh mục/phiếu sinh tự động đã in 1.4.0 — đúng loại lệch hai-phiên-bản hệ thống này chống. Đã đồng bộ **Version 1.4.0** lên 4 docx `01_Governance/` + SOP + Weekly template, `RELEASE_NOTE_HK1_2026_2027.md/.docx`, `00_START_HERE/README.md`, `05_Claude/QUICK_LAUNCH_PROMPT.txt`. Ghi nhận chủ dự án **đã xóa xong `DATN_mentor`** — việc xóa tay còn lại duy nhất là `EEE Projects/_to_delete/`. Đóng gói `dist/` được dựng lại cùng nhãn. Validator PASS 84 topics sau toàn bộ thay đổi.

### 23/08/2026 — v1.4: gộp về một thư mục duy nhất
Chủ dự án quyết định quản lý tất cả trong `EEE Projects` cho dễ theo dõi (thay quyết định tách bạch v1.3 cùng ngày). Prompt điều hành DATN chuyển về `05_Claude/`; `release_cohort.py` nghỉ hưu; chuỗi lệnh rút còn `validate → generate --docx [--pdf] → generate_site → CHANGELOG`; `DATN_mentor` chỉ còn README chỉ đường + `_to_delete/` chờ xóa. Đối chiếu byte trước khi gộp: không mất nội dung.

### 23/08/2026 — v1.3.1: khắc phục các nguồn hiểu lầm
- Đồng nhất phiên bản: meta.version 4 file 06_Data → **1.3**; mọi tài liệu phát hành nay in "Phiên bản 1.3".
- **UNRESOLVED-2 ✅ đóng:** bộ phiếu viết tay cũ (`Readiness_and_Topic_Selection_Forms.docx`) lưu trữ vào `99_Archive/` — chỉ còn MỘT bộ phiếu (sinh tự động).
- **UNRESOLVED-3 ✅ đóng:** Handbook §5.2 có ghi chú "nguồn chuẩn của ngưỡng là readiness_rubrics.json; lệch nhau thì JSON thắng".
- **UNRESOLVED-4 ✅ đóng:** 6 docx chính sách đổi nhãn Version 1.0 → 1.3.
- Release note đổi tên bỏ số phiên bản: `RELEASE_NOTE_HK1_2026_2027.md/.docx`; bản tên cũ vào `_to_delete/`.
- QUICK_LAUNCH_PROMPT.txt viết lại cho phiên Claude mới (không audit lại; nhận biết 2 dự án; chuỗi lệnh chuẩn).

### 23/08/2026 — v1.3: tách bạch hai dự án (quyết định của chủ dự án)
Làm rõ đây là **hai dự án khác phạm vi**, không phải một dự án hai chỗ:
- **`EEE Projects`** = dự án TỔNG: quản lý toàn bộ NCKH, luận án, hướng dẫn sinh viên nghiên cứu, thực tập tốt nghiệp và mentor cộng đồng IC design — chứa nguồn chuẩn `06_Data/` (84 đề tài P/I/T/R), scripts, governance, operations, website. **Mọi chỉnh sửa nội dung diễn ra ở đây.**
- **`DATN_mentor`** = dự án CON: chỉ vận hành cohort Đồ án tốt nghiệp HK1 2026-2027 — giữ đúng bộ file gốc: `CLAUDE_MASTER_EXECUTION_DATN_MENTORING.md` *(nay ở `05_Claude/`)* + danh mục (docx/pdf) + phiếu + release note (+ README nêu quan hệ hai dự án).
- Đảo lại phần "gom về một thư mục" (v1.2.3): khôi phục toàn bộ hệ thống bản mới nhất về `EEE Projects`, kiểm chứng tại chỗ (`validate_portfolio.py` PASS 84 topics). Phần thừa ở `DATN_mentor` dồn vào `DATN_mentor/_to_delete/`.
- Cơ chế nối hai dự án: **`scripts/release_cohort.py`** — sau mỗi lần regenerate, copy 5 tài liệu cohort từ `EEE Projects` sang `DATN_mentor`. `DATN_mentor` không bao giờ là nơi sửa nội dung.
- Cần xóa tay (Claude không có quyền xóa): `EEE Projects/_to_delete/` và `DATN_mentor/_to_delete/`.

### 23/08/2026 — thực thi MASTER_PROMPT (hệ thống v1.4.0)
Chạy `05_Claude/CLAUDE_MASTER_EXECUTION_DATN_MENTORING.md` như **bảng kiểm Definition of Done §33 trên hệ thống đã có**, không dựng lại. Bù 16 hạng mục: 6 template (`STUDENT_PROFILE`, `EVIDENCE_LEDGER`, `DECISION_LOG`, `EXTENSION_PROPOSAL_TEMPLATE`, `THESIS_REVIEW_CHECKLIST`, `DEFENSE_QUESTIONS`), 4 guide trong `10_Documentation/`, `CLAUDE.md`, `README.md`, `VERSION`, `scripts/build_release.py`, gói `dist/` + ZIP + `dist/FINAL-AUDIT.md`. Đóng 3 lỗi MAJOR: lệch phiên bản JSON↔tài liệu, PDF lệch docx, `rmtree` không chạy được trên thư mục mount. Khôi phục `scripts/release_cohort.py` bị dồn nhầm vào `_to_delete/`. Validation 13/13 PASS. Chi tiết: `dist/FINAL-AUDIT.md`.

### 23/08/2026 — gom về một thư mục (ĐÃ ĐẢO LẠI ở v1.3)
Toàn bộ dự án chuyển từ `EEE Projects` sang **`DATN_mentor`** (thư mục kết nối với phiên làm việc). Đã đối chiếu checksum từng file, chạy lại `validate_portfolio.py` (PASS 84 topics) và cả 3 generator tại vị trí mới. Bản cũ dồn vào `EEE Projects/_to_delete/` chờ xóa tay — xem §12 UNRESOLVED-6.

### 23/08/2026 — implementation-notes v2.0
- Viết lại theo `05_Claude/CLAUDE_MASTER_EXECUTION_DATN_MENTORING.md` §18: 23 mục tài liệu hệ thống đầy đủ, thay cho sổ tay vận hành 10 mục của v1.2.
- Bổ sung mới: kiểm kê nguồn có cột thẩm quyền (§2) · mô hình dữ liệu đầy đủ kèm schema và số liệu 84 đề tài (§5) · 9 tính năng (§6) · đặc tả từng script kèm failure mode (§7) · danh sách file cấm sửa tay (§8) · bảng validation + negative test (§9) · 12 quyết định thiết kế kèm phương án đã loại (§10) · 8 hạn chế (§11) · 5 tồn đọng, 1 đã đóng ngay (§12) · 9 quy trình vận hành (§13–§22) · 2 phụ lục.
- Phát hiện mới trong lượt rà soát này: **UNRESOLVED-2** (hai bộ phiếu readiness xung đột), **UNRESOLVED-4** (governance docx còn nhãn v1.0), **UNRESOLVED-5** (FILE_MANIFEST ghi lệnh regenerate cũ).
- Giữ nguyên §0 và toàn bộ nội dung vận hành của v1.2, đưa vào §13–§19.
- **Gộp từ bản sổ tay v1.3** (viết song song cùng ngày): phần mở đầu **★ Hiểu bản chất hệ thống trong 10 phút** (từ điển 12 khái niệm, một học kỳ diễn ra thế nào, 4 nhịp công việc, mở file nào khi nào) · roadmap 9 bước (§1) · 10 nguyên tắc bất biến (§3.4) · sổ rủi ro đầy đủ C/H/M/L/R (§12.1) · prompt cho Claude (Phụ lục A) · nguyên tắc riêng tư (Phụ lục B). Không mất nội dung nào của bản v1.3.

### 23/08/2026 — hệ thống v1.2.1
Sửa bug escape Markdown nuốt wildcard `A1-P*` trong tài liệu phát hành · RR expectations vào Phiếu 5.2 · 3 dòng Level vào Phiếu 5.3 · ngưỡng "Advanced family B6 / AB-R" rõ nghĩa · cảnh báo thang điểm TR 0–5 vs WR/RR 0–4 · validator cross-check lịch gate + RR · cờ `--pdf`. Chi tiết: `00_START_HERE/CHANGELOG.md`.

### 23/08/2026 — hệ thống v1.2
Lớp web công khai: `generate_site.py` → `docs/index.html`.

### 23/08/2026 — hệ thống v1.1.1
Nghiệm thu: dry-run A/B PASS, acceptance 36/36, `FINAL_SYSTEM_AUDIT.md`, release note.

### 23/08/2026 — hệ thống v1.1
Chuẩn hóa sau audit: 06_Data 84 đề tài, 2 script, mọi view regenerate. Đóng C1/C2/C3/H1–H5/M1–M3.

---

## Phụ lục A · Prompt sẵn dùng cho các phiên Claude sau

- **Sửa/thêm đề tài hoặc rubric:**
  > Đọc `05_Claude/MASTER_PROMPT_CLAUDE.md` và `implementation-notes.md`. Sửa [nội dung] trong `06_Data/…json`, chạy `scripts/validate_portfolio.py` (phải PASS), chạy `scripts/generate_catalogs.py --docx --pdf`, cập nhật CHANGELOG, báo cáo files changed. Không đổi mã chuẩn, không sửa tay file view.

- **Trước một buổi review gate:**
  > Đọc workbook sheet Students + Weekly_Status + Milestones, đối chiếu `06_Data/milestone_gates.json` và `cohort_HK1_2026_2027.json`. Liệt kê SV có nguy cơ trượt Gate N kèm evidence còn thiếu và đề xuất recovery plan theo SOP §6–7. Không đề xuất mentor làm thay.

- **Dry-run hệ thống (bước 8 roadmap):**
  > Thực hiện dry-run giấy cho một SV giả định làm `A4-T01` và một SV làm `B2-T01`: charter từ template → MVT/extension từ JSON → 6 gate theo `cohort_HK1_2026_2027.json` → legacy package theo `LEGACY_PACKAGE_CHECKLIST.md`. Ghi lại chỗ nào thiếu/kẹt trong quy trình.

- **Cuối kỳ:**
  > Chạy nghiệm thu theo `05_Claude/ACCEPTANCE_CHECKLIST.md`, đối chiếu thực trạng repo, viết `FINAL_SYSTEM_AUDIT.md` ghi rõ mục đạt/chưa đạt kèm bằng chứng.

Quy ước chung: luôn yêu cầu Claude **audit trước, sửa sau**; mọi output phải nêu *files changed / decisions made / unresolved issues / next action*.

---

## Phụ lục B · Nguyên tắc riêng tư (nhắc nhanh)

- Workbook có dữ liệu thật (tên/email/điểm/cảnh báo) → lưu vào `07_Private/`, **không bao giờ** gửi cho SV hoặc đưa lên repo public (`.gitignore` đã chặn 07_Private và 99_Archive).
- SV cần xem danh mục → dùng catalog trong `02_Project_Portfolio/` hoặc danh mục cohort.
- Phiếu giấy đã điền (SĐT/email): lưu một nơi duy nhất do mentor giữ; bản scan (nếu có) → `07_Private/`.
- Không đưa dữ liệu cá nhân SV vào công cụ AI bên ngoài khi chưa được phép (AI Policy §2).

---

*Tài liệu này là file dẫn xuất phục vụ vận hành và bàn giao. Khi nội dung mâu thuẫn với `06_Data/` hoặc `Master_Mentoring_Handbook.docx`, **nguồn chuẩn thắng**. Cập nhật tài liệu mỗi khi đóng một tồn đọng, chốt một quyết định, hoặc qua một gate.*
