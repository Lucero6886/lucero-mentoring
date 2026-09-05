# Bản đồ file — toàn bộ kho

**Engineering & Research Mentoring Program (Lucero)** · ThS. Đinh Văn Nam (Mr. Lucero Dinh) — Khoa Điện–Điện tử, Trường Kỹ thuật, Đại học Phenikaa
Phiên bản hệ thống **1.10.0** · cập nhật **2026-09-04**

> **File này sinh tự động** từ chính cây thư mục bằng `scripts/generate_manifest.py`.
> Sửa tay sẽ bị ghi đè. Bản viết tay trước đây đã liệt kê file đã xóa và bỏ sót cả một
> lớp tài liệu mới — đó là lý do nó được chuyển sang sinh tự động.

Kho có **335 file** trong 14 thư mục chính.

## Quy tắc đọc bản đồ này

- Thư mục đánh dấu **bản sinh tự động** chứa file bị ghi đè mỗi lần chạy script — đừng sửa tay.
- Muốn biết *vì sao* mỗi thư mục tồn tại và sửa ở đâu thì an toàn, đọc
  [`implementation-notes.md`](../implementation-notes.md) §3 và §5.

## File ở thư mục gốc

| File | Là gì |
|---|---|
| `README.md` | Trang bìa của kho — điểm vào cho sinh viên và đồng nghiệp. |
| `implementation-notes.md` | **Tài liệu hệ thống cho người vận hành** — từ bản chất tới triển khai. |
| `implementation-notes.html` | Bản web của tài liệu trên (sinh tự động). |
| `VERSION` | Phiên bản hệ thống — nguồn chuẩn cho mọi nhãn phiên bản. |
| `CLAUDE.md` | Ràng buộc cho các phiên làm việc với AI. |
| `CONTRIBUTING.md` | Cách góp ý, đề xuất đề tài, báo lỗi tài liệu. |
| `LICENSE` | CC BY-NC-SA 4.0 cho tài liệu · MIT cho mã nguồn. |
| `CITATION.cff` | Thông tin trích dẫn kho (nút *Cite this repository* trên GitHub). |
| `Ban_do_de_tai.md` | Bản đồ đề tài kể chuyện, dành cho người mới (sinh tự động). |
| `Ban_do_de_tai.html` | Bản web của bản đồ đề tài (sinh tự động). |
| `index.html` | Chuyển hướng sang `docs/index.html` — lưới an toàn cho cấu hình GitHub Pages. |
| `guide.html` | Chuyển hướng sang `docs/guide.html` — lưới an toàn cho cấu hình GitHub Pages. |
| `Danh_muc_de_tai_DATN_HK1_2026_2027.docx` | — |
| `Danh_muc_de_tai_DATN_HK1_2026_2027.pdf` | — |
| `Phieu_lua_chon_va_danh_gia_de_tai_DATN_HK1_2026_2027.docx` | — |
| `RELEASE_NOTE_HK1_2026_2027.docx` | — |
| `RELEASE_NOTE_HK1_2026_2027.md` | — |

## Thư mục

### `06_Data/` — 5 file

**NGUỒN CHUẨN DUY NHẤT.** Danh mục đề tài, lớp thực thi, cửa kiểm soát, thang sẵn sàng, dữ liệu từng khóa.

- `cohort_HK1_2026_2027.json`
- `milestone_gates.json`
- `project_portfolio.json`
- `readiness_rubrics.json`
- `research_packs.json`

### `scripts/` — 14 file

Kiểm tra tính nhất quán và sinh toàn bộ tài liệu dẫn xuất từ nguồn chuẩn.

- `build_release.py`
- `cohort_schedule.py`
- `export_governance_md.py`
- `generate_ban_do.py`
- `generate_catalogs.py`
- `generate_guide.py`
- `generate_manifest.py`
- `generate_notes.py`
- `generate_research_packs.py`
- `generate_site.py`
- `release_cohort.py`
- `site_style.py`
- `sync_docx_version.py`
- `validate_portfolio.py`

### `00_START_HERE/` — 4 file

Điểm vào: lịch sử thay đổi, bản đồ file, lộ trình triển khai.

- `CHANGELOG.md`
- `FILE_MANIFEST.md`
- `IMPLEMENTATION_ROADMAP.md`
- `README.md`

### `01_Governance/` — 8 file

Chính sách gốc. Bản `.docx` là gốc dùng để in và ký; bản `.md` cạnh nó là bản sinh.

- `AI_and_Academic_Integrity_Policy.docx`
- `AI_and_Academic_Integrity_Policy.md`
- `Cohort_HK1_2026_2027_Implementation_Guide.docx`
- `Cohort_HK1_2026_2027_Implementation_Guide.md`
- `Master_Mentoring_Handbook.docx`
- `Master_Mentoring_Handbook.md`
- `Mentor_Student_Working_Agreement.docx`
- `Mentor_Student_Working_Agreement.md`

### `02_Project_Portfolio/` — 232 file · **bản sinh tự động**

Danh mục theo loại hoạt động, trang hướng dẫn từng đề tài, hồ sơ thực thi chiều sâu.

- `Course_Project_Catalog.docx`
- `Graduation_Thesis_Catalog.docx`
- `Internship_Catalog.docx`
- `Master_Project_Portfolio_AB.docx`
- `Research_Opportunities_Catalog.docx`
- `Research_Packs/` — 105 file
- `Topic_Guides/` — 122 file

### `03_Operations/` — 9 file

Quy trình vận hành, checklist tuần, thang chấm, định nghĩa "xong", workbook theo dõi.

- `DEFINITION_OF_DONE.md`
- `MENTOR_WEEKLY_CHECKLIST.md`
- `Mentoring_Management_Workbook.xlsx`
- `Mentoring_Operating_Procedure_SOP.docx`
- `Mentoring_Operating_Procedure_SOP.md`
- `PASS_FAIL_RUBRIC.md`
- `STATUS_BOARD.md`
- `Weekly_Report_and_Meeting_Template.docx`
- `Weekly_Report_and_Meeting_Template.md`

### `04_Project_Template/` — 27 file

Biểu mẫu hồ sơ dự án của từng sinh viên và bộ khởi tạo repo.

- `AI_USAGE_LOG.md`
- `DECISION_LOG.md`
- `DEFENSE_QUESTIONS.md`
- `EVIDENCE_LEDGER.md`
- `EXPERIMENT_LOG_TEMPLATE.md`
- `EXTENSION_PROPOSAL_TEMPLATE.md`
- `KNOWN_ISSUES.md`
- `LEGACY_PACKAGE_CHECKLIST.md`
- `LITERATURE_MATRIX_TEMPLATE.md`
- `LITERATURE_NOTE_TEMPLATE.md`
- `MENTOR_LESSONS_LEARNED.md`
- `NEXT_STEPS.md`
- `PAPER_READINESS_TEMPLATE.md`
- `PROJECT_CHARTER_TEMPLATE.md`
- `README.md`
- `REPRODUCIBILITY_STANDARD.md`
- `STUDENT_PROFILE.md`
- `TEACHING_TRANSFER_NOTE.md`
- `THESIS_REVIEW_CHECKLIST.md`
- `WEEKLY_REPORT_TEMPLATE.md`
- `student_repo_starter/` — 7 file

### `07_Private/` — 1 file

Dữ liệu cá nhân sinh viên. **Bị `.gitignore` chặn — không bao giờ lên kho công khai.**

- `README.md`

### `09_References/` — 2 file

Tài liệu nền theo hướng nghiên cứu và các đề xuất đang cân nhắc.

- `READING-LIST.md`
- `TITLE-REVIEW-v2.md`

### `10_Documentation/` — 7 file

Hướng dẫn theo vai trò: sinh viên, mentor, vận hành, GitHub, track nghiên cứu.

- `GITHUB-WORKFLOW.html`
- `GITHUB-WORKFLOW.md`
- `MENTOR-GUIDE.md`
- `RESEARCH-TRACKS.md`
- `STUDENT-GUIDE.md`
- `USER-GUIDE.md`
- `WORKFLOW.md`

### `docs/` — 3 file · **bản sinh tự động**

Trang web công khai (GitHub Pages).

- `guide.html`
- `index.html`

### `tests/` — 2 file

Bài diễn tập toàn quy trình, dùng để kiểm hệ thống trước mỗi phát hành.

- `DRY_RUN_A_TRACK_A4-T01.md`
- `DRY_RUN_B_TRACK_B2-T01.md`

### `05_Claude/` — 5 file

Prompt và ngữ cảnh cho các phiên làm việc với AI.

- `ACCEPTANCE_CHECKLIST.md`
- `CLAUDE_MASTER_EXECUTION_DATN_MENTORING.md`
- `CLAUDE_PROJECT_CONTEXT.md`
- `MASTER_PROMPT_CLAUDE.md`
- `QUICK_LAUNCH_PROMPT.txt`

### `99_Archive/` — 16 file

Bản cũ đã ngừng dùng, giữ lại để tra cứu. Không phải nguồn chuẩn.

- `AUDIT_REPORT_2026-08-23.md`
- `FINAL_SYSTEM_AUDIT_2026-08-23.md`
- `2026-08-23_v1.0/` — 14 file

---

*Lịch sử thay đổi: [`CHANGELOG.md`](CHANGELOG.md) · Tài liệu hệ thống: [`implementation-notes.md`](../implementation-notes.md)*
