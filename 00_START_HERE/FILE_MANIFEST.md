# FILE MANIFEST — Engineering & Research Mentoring Program (Lucero) v1.4

Tác giả: ThS. Đinh Văn Nam (Mr. Lucero Dinh) — Khoa Điện–Điện tử, Trường Kỹ thuật, Đại học Phenikaa.

## 00_START_HERE
- `README.md` — điểm bắt đầu, kiến trúc và quy tắc nguồn chuẩn.
- `IMPLEMENTATION_ROADMAP.md` — lộ trình triển khai hệ thống theo pha.
- `CHANGELOG.md` — lịch sử thay đổi.
- `FILE_MANIFEST.md` — danh mục file này.

## 01_Governance
- `Master_Mentoring_Handbook.docx` — NGUỒN CHUẨN POLICY: triết lý, level, readiness, trách nhiệm, gate, peer mentoring, legacy package.
- `Mentor_Student_Working_Agreement.docx` — thỏa thuận kỳ vọng thầy–trò.
- `AI_and_Academic_Integrity_Policy.docx` — chính sách AI và ownership.
- ~~Readiness_and_Topic_Selection_Forms.docx~~ — bản viết tay v1.0 đã LƯU TRỮ vào `99_Archive/` (v1.3.1); bộ phiếu duy nhất hiện hành là `Phieu_lua_chon_va_danh_gia_de_tai_DATN_HK1_2026_2027.docx` (sinh tự động).
- `Cohort_HK1_2026_2027_Implementation_Guide.docx` — hướng dẫn vận hành cohort DATN 15 tuần.

## 02_Project_Portfolio — VIEW SINH TỰ ĐỘNG (không sửa tay)
- `Master_Project_Portfolio_AB.docx` — master catalog đầy đủ 105 đề tài.
- `Course_Project_Catalog.docx` — view P (bảng tóm tắt, theo thiết kế).
- `Internship_Catalog.docx` — view I (bảng tóm tắt, theo thiết kế).
- `Graduation_Thesis_Catalog.docx` — view T (có chi tiết + MVT).
- `Research_Opportunities_Catalog.docx` — view R (có chi tiết).

## 03_Operations
- `Mentoring_Operating_Procedure_SOP.docx` — SOP tuyển/giao đề tài đến closeout.
- `Weekly_Report_and_Meeting_Template.docx` — báo cáo tuần, meeting record, blocker escalation.
- `Mentoring_Management_Workbook.xlsx` — tracker (TEMPLATE trắng; bản có dữ liệu thật lưu 07_Private/). Sheet Portfolio là view sinh từ 06_Data.

## 04_Project_Template
- `README.md`, `PROJECT_CHARTER_TEMPLATE.md`, `WEEKLY_REPORT_TEMPLATE.md`, `EXPERIMENT_LOG_TEMPLATE.md`,
  `LITERATURE_NOTE_TEMPLATE.md`, `AI_USAGE_LOG.md`, `KNOWN_ISSUES.md`, `NEXT_STEPS.md`.
- `LEGACY_PACKAGE_CHECKLIST.md` — checklist nghiệm thu legacy package tại closeout.

## 05_Claude
- `05_Claude/CLAUDE_MASTER_EXECUTION_DATN_MENTORING.md` — prompt điều hành DATN của tác giả (chuyển từ DATN_mentor về, v1.4).
- `MASTER_PROMPT_CLAUDE.md`, `CLAUDE_PROJECT_CONTEXT.md`, `ACCEPTANCE_CHECKLIST.md`, `QUICK_LAUNCH_PROMPT.txt`.

## 06_Data — NGUỒN CHUẨN DỮ LIỆU (v1.1)
- `project_portfolio.json` — 105 đề tài (16 nhóm; A6/A7 + AB co-design mở từ v1.5.0); schema gồm mvt/tools/status/prereq_codes/career_relevance/cohort_alias/checkpoints_15w/eligibility.
- `readiness_rubrics.json` — TR (0-5, 16 năng lực) + WR (0-4, /20, ngưỡng) + RR (0-4) + lựa chọn kết luận.
- `milestone_gates.json` — Gate 1–6 dạng keyed object.
- `cohort_HK1_2026_2027.json` — dữ liệu cohort: mốc hành chính, lịch tuần, deadline gate, đề tài mở + alias, career guide.

## scripts — TỰ ĐỘNG HÓA
- `validate_portfolio.py` — kiểm tra fail-fast dữ liệu nguồn (chạy trước mọi lần generate).
- `generate_catalogs.py` — sinh Master + 4 catalog + danh mục cohort + phiếu từ 06_Data (`--docx` để xuất docx).
- `generate_site.py` — sinh trang web công khai `docs/index.html` từ 06_Data (chỉ dữ liệu public).
- `generate_ban_do.py` — sinh `Ban_do_de_tai.md/.html` (bản đồ trực quan toàn bộ đề tài) từ `06_Data/`.
- `export_governance_md.py` — sinh bản `.md` đọc-trên-web từ 6 tài liệu chính sách `.docx` (cần pandoc).
- `release_cohort.py` — công cụ xuất 5 tài liệu cohort sang thư mục đích tự chọn (bắt buộc truyền đường dẫn đích, ví dụ USB/thư mục chia sẻ; không còn đích mặc định — `DATN_mentor` đã xóa 23/08/2026).
- `build_release.py` — đóng gói `dist/` + ZIP + MANIFEST theo `VERSION`.

## docs — TRANG WEB CÔNG KHAI (view sinh tự động)
- `index.html` — catalog sinh viên: 105 đề tài có bộ lọc, lịch gate cohort, hướng dẫn chọn đề tài, quy tắc. Deploy GitHub Pages: Settings → Pages → main /docs. Bản online (artifact riêng tư, share được): https://claude.ai/code/artifact/c5d77e76-9f17-4ecb-961f-780daaee8ec3

## File gốc (root)
- `Danh_muc_de_tai_DATN_Nhom_A_B_HK1_2026_2027.docx/.pdf` — danh mục cohort (VIEW sinh tự động; mã chuẩn + alias).
- `Phieu_lua_chon_va_danh_gia_de_tai_DATN_HK1_2026_2027.docx` — phiếu cohort (VIEW sinh tự động; thang chuẩn).
- `AUDIT_REPORT.md` — kiểm toán v1.0 (23/08/2026) + annex trạng thái xử lý.
- `FINAL_SYSTEM_AUDIT.md` — nghiệm thu v1.1.1: 36/36 tiêu chí + hạn chế còn lại.
- `RELEASE_NOTE_HK1_2026_2027.md/.docx` — thông báo phát hành bản v1.1 gửi sinh viên.
- `implementation-notes.md/.html` — **tài liệu hệ thống đầy đủ** (23 mục theo MASTER_PROMPT §18 + phần "Hiểu bản chất hệ thống trong 10 phút" + 2 phụ lục): nguồn chuẩn, kiến trúc, mô hình dữ liệu, script, quyết định thiết kế, hạn chế, tồn đọng và 9 quy trình vận hành. Bản web: https://claude.ai/code/artifact/ec2b8b23-f45b-4850-ba64-509acc4766cf

## tests — DRY-RUN & QA
- `DRY_RUN_A_TRACK_A4-T01.md` — dry-run luồng A (admission → 6 gate → legacy), PASS.
- `DRY_RUN_B_TRACK_B2-T01.md` — dry-run luồng B có kịch bản trượt Gate 3/reduce scope, PASS.

## 07_Private — DỮ LIỆU RIÊNG TƯ (không công khai; bị .gitignore chặn)
## 99_Archive — bản gốc trước regenerate (2026-08-23_v1.0)

## 10_Documentation — HƯỚNG DẪN THEO VAI TRÒ
- `USER-GUIDE.md` — tổng quan, tra nhanh "việc này xem ở đâu".
- `MENTOR-GUIDE.md` — thao tác hằng tuần: giao đề tài, weekly review, gate review, khi SV chậm, extension, bảo vệ, bootcamp.
- `STUDENT-GUIDE.md` — phát cho sinh viên: cái gì tính là evidence, nộp gì mỗi tuần, vì sao baseline quan trọng, dùng AI thế nào.
- `WORKFLOW.md` — quy trình kỹ thuật sửa hệ thống và phát hành, kèm bẫy escape Markdown.

## Gốc repo — bổ sung v1.4.0/v1.5.0
- `README.md` — điểm vào, trả lời 13 câu của MASTER_PROMPT §26.
- `CLAUDE.md` — chỉ dẫn vận hành cho các phiên Claude sau (§0 cảnh báo về prompt master trong DATN_mentor).
- `09_References/READING-LIST.md` — **tài liệu nền tảng theo từng hướng nghiên cứu**: nền chung về tái lập và viết khoa học, trục A (RTL/ASIC/EDA mã nguồn mở), nhánh nhúng & TinyML, trục B (Polar), vùng AB (co-design), kèm hướng dẫn đọc ba vòng và quy tắc kiểm chứng trích dẫn.
- `CITATION.cff` — thông tin trích dẫn chuẩn; GitHub hiển thị nút *Cite this repository*.
- `01_Governance/*.md` · `03_Operations/*.md` — **bản Markdown đọc-trên-web** của các tài liệu chính sách, sinh tự động từ `.docx` bằng `scripts/export_governance_md.py`. Bản `.docx` vẫn là bản gốc để in/ký.
- `10_Documentation/GITHUB-WORKFLOW.md` — **vận hành chương trình trên GitHub**: 3 tầng riêng tư, repo riêng của sinh viên, nhịp tuần + gate review bằng Issue/Milestone, phân quyền, lộ trình 3 giai đoạn.
- `04_Project_Template/student_repo_starter/` — bộ khởi tạo repo cho sinh viên: README mẫu, `.gitignore` cho HDL/FPGA/Python, mẫu Issue báo cáo tuần và gate review.
- `CONTRIBUTING.md` · `LICENSE` · `.github/ISSUE_TEMPLATE/` — bộ file cho repo GitHub công khai.
- `Ban_do_de_tai.md/.html` — **bản đồ trực quan toàn bộ đề tài + 4 kịch bản sử dụng** (giảng dạy / thực tập / mentor DATN / nghiên cứu). VIEW sinh tự động bởi `scripts/generate_ban_do.py` — không sửa tay; kèm bản web chia sẻ được.
- `VERSION` — phiên bản hệ thống, nguồn duy nhất cho `build_release.py`.

## dist — GÓI PHÁT HÀNH (sinh tự động)
- `dist/FINAL-AUDIT.md` — tự kiểm theo §23.
- `DATN-Mentoring-HK1-2026-2027-v<VERSION>/` + `.zip` — sinh bằng `python3 scripts/build_release.py`.

## Nguyên tắc nguồn chuẩn
1. Portfolio/rubrics/milestones/cohort: `06_Data/` là chuẩn; mọi catalog/phiếu/danh mục/sheet Portfolio là view sinh tự động.
2. Policy/triết lý mentoring: `Master_Mentoring_Handbook.docx` là chuẩn.
3. Quy trình thay đổi: sửa nguồn chuẩn → `validate_portfolio.py` (phải PASS) → `generate_catalogs.py --docx --pdf` → `generate_site.py` (nếu sửa dữ liệu đề tài) → CHANGELOG → báo cáo. Chi tiết từng bước: `implementation-notes.md` §20.
4. Dữ liệu sinh viên là private: lưu 07_Private/, không đưa lên website/repo public.

## Cấu trúc một thư mục (từ v1.4)
- Toàn bộ chương trình — kể cả tài liệu cohort DATN — quản lý tại duy nhất `EEE Projects`. Tài liệu phát cho SV nằm ở thư mục gốc; prompt điều hành DATN ở `05_Claude/CLAUDE_MASTER_EXECUTION_DATN_MENTORING.md`.
- Chuỗi lệnh khi sửa dữ liệu: `validate → generate_catalogs --docx [--pdf] → generate_site → CHANGELOG`.
