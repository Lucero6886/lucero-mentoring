# Changelog

## v1.5.1 (bổ sung) — Nâng chuẩn học thuật cho bản công khai · 2026-08-27

Repo đã lên GitHub (`Lucero6886/lucero-mentoring`, public). Đợt này bổ sung ba thứ khiến kho đạt chuẩn học thuật và dễ dùng hơn cho người đọc bên ngoài:

**Tài liệu chính sách đọc được ngay trên web.** GitHub không hiển thị nội dung `.docx` — người đọc phải tải về. Thêm `scripts/export_governance_md.py` sinh bản `.md` từ 6 tài liệu (`Master_Mentoring_Handbook`, `Mentor_Student_Working_Agreement`, `AI_and_Academic_Integrity_Policy`, `Cohort_HK1_2026_2027_Implementation_Guide`, `Mentoring_Operating_Procedure_SOP`, `Weekly_Report_and_Meeting_Template`). Giữ đúng kiến trúc hệ thống: `.docx` là **bản gốc** để in/ký, `.md` là **view sinh tự động** — mỗi file mang ghi chú cấm sửa tay. Script tự dọn mũi tên, hạ bậc tiêu đề và đổi hộp nhấn mạnh của Word thành trích dẫn.

**`CITATION.cff`.** Thông tin trích dẫn chuẩn (CFF 1.2.0) — GitHub hiển thị nút *Cite this repository*, xuất APA/BibTeX. Ghi rõ tác giả, đơn vị, phiên bản, hai giấy phép và 13 từ khóa chuyên ngành.

**`09_References/READING-LIST.md`.** Danh mục tài liệu nền tảng theo từng hướng: nền chung (tái lập nghiên cứu, viết khoa học), trục A (RTL coding style, STA, OpenROAD/LibreLane/SKY130), nhánh nhúng & IoT (RTOS, TinyML, MLPerf Tiny), trục B (Arıkan 2009, Tal–Vardy, SC-Flip, SCL theo LLR, kiến trúc SC bán song song, 3GPP TS 38.212), vùng AB (Sze và cộng sự, Horowitz ISSCC 2014). Mỗi mục kèm một dòng *đọc để làm gì, đọc lúc nào*; thêm phương pháp đọc ba vòng và quy tắc bắt buộc kiểm chứng trích dẫn từ nguồn gốc.

`README.md` và `00_START_HERE/FILE_MANIFEST.md` cập nhật theo; chuỗi lệnh sinh tài liệu nay có thêm bước `export_governance_md.py`. Nguồn chuẩn `06_Data/` không đổi (105 đề tài, v1.5.1) nên không regenerate các view khác.

## v1.5.1 (bổ sung) — Đưa chương trình lên GitHub · 2026-08-23

Chuẩn bị publish repo công khai để sinh viên đọc, chọn đề tài và thảo luận.

**Repo công khai (`lucero-mentoring`, Public):**
- `git init -b main` ngay trong thư mục dự án; commit đầu `858c9b8` (67 file, 1,2 MB), `git fsck` sạch.
- `.gitignore` chặn: `07_Private/`, `05_Claude/`, `CLAUDE.md`, `AUDIT_REPORT.md`, `FINAL_SYSTEM_AUDIT.md`, `99_Archive/`, `build/`, `dist/`, `_to_delete/`. Đã kiểm chứng: không file nội bộ nào được theo dõi.
- `README.md` viết lại thành trang chủ hướng sinh viên (3 bước chọn đề tài, bảng định hướng nghề nghiệp, 6 gate, phần mentor phía dưới); gỡ mục "Hai thư mục — đừng gộp" đã lỗi thời.
- Mới: `CONTRIBUTING.md` (ranh giới dữ liệu cá nhân, kênh nào cho việc gì, cách hỏi, đề xuất đề tài, chính sách PR) · `LICENSE` (tài liệu CC BY-NC-SA 4.0 + `scripts/` MIT + sản phẩm sinh viên tách riêng) · `.github/ISSUE_TEMPLATE/` 4 mẫu · `docs/.nojekyll`.
- GitHub Pages phục vụ `docs/index.html` (catalog 105 đề tài) — link duy nhất gửi sinh viên.

**Vận hành:**
- `10_Documentation/GITHUB-WORKFLOW.md` — mô hình 3 tầng riêng tư (công khai / repo riêng từng sinh viên / `07_Private` không lên mạng), quy tắc phân loại một câu *"nói về đề tài thì công khai, nói về con người thì không"*, nhịp tuần bằng Issue, gate review bằng Milestone + checklist, bảng điều khiển mentor bằng GitHub Projects, phân quyền theo vai trò, 6 điều tuyệt đối không làm, lộ trình 3 giai đoạn.
- `04_Project_Template/student_repo_starter/` — bộ khởi tạo repo sinh viên: hướng dẫn 3 bước, README mẫu (chạy lại thế nào, kết quả chính, hạn chế, bước tiếp cho người kế thừa), `.gitignore` cho HDL/Vivado/Quartus/OpenLane/Python, 2 mẫu Issue (báo cáo tuần · gate review).

Nguồn chuẩn `06_Data/` **không đổi** (vẫn 1.5.1, 105 đề tài) nên không regenerate view.

## v1.5.1 — Gỡ thông tin hành chính cohort khỏi mọi tài liệu · 2026-08-23

Quyết định chủ dự án ("gỡ khỏi mọi nơi"): khối **Mốc hành chính** (đăng ký QLĐT, nộp học phí, phiếu giao đồ án tại VP Trường Kỹ thuật, hạn Khoa chốt danh sách) và **Điều kiện đăng ký** (quy tắc Thực tập tốt nghiệp trước Đồ án) không nằm trong bộ tài liệu dài hạn nữa:

- `06_Data/cohort_HK1_2026_2027.json`: xóa `admin_milestones` + `eligibility` · `06_Data/project_portfolio.json`: xóa `eligibility_rules`; gỡ cụm "qua Thực tập tốt nghiệp" khỏi prerequisites/career của 8 đề tài A6/A7/AB mới. Meta 4 file + `VERSION` → **1.5.1**.
- `scripts/generate_catalogs.py`: danh mục cohort bỏ bảng Mốc hành chính + dòng Điều kiện quan trọng + dòng "Thời gian thực hiện dự kiến"; Graduation_Thesis_Catalog bỏ dòng Điều kiện đăng ký. `scripts/generate_site.py`: trang cohort bỏ banner ngày + Điều kiện đăng ký + bảng Mốc hành chính. `scripts/generate_ban_do.py`: §3.2 bỏ câu quy tắc đăng ký.
- Toàn bộ view sinh lại in **1.5.1**, kiểm tra 0 vết còn sót trên danh mục/phiếu/site/bản đồ. **Giữ nguyên**: lịch 15 tuần + 6 gate và hạn gate (xương sống sư phạm, không phải thông tin hành chính); "Điều kiện cứng" an toàn theo từng đề tài (PCB, pin).
- Tài liệu vận hành (`implementation-notes`, guides): mốc ngày hành chính thay bằng mô tả trung tính ("theo hạn Khoa công bố", "cửa sổ đăng ký của Khoa"); R6 giữ nguyên bản chất, bỏ ngày cụ thể. `01_Governance/Cohort_HK1_2026_2027_Implementation_Guide.docx` gỡ mục mốc hành chính. Nhãn 7 docx + release note → 1.5.1. Validator **PASS 105**.

## v1.5.0 — Mở nhánh Nhúng & IoT + co-design định hướng luận án · 2026-08-23

Quyết định chủ dự án: chương trình phục vụ **dài hạn, nhiều học kỳ** (không chỉ HK1 2026-2027) và bổ sung danh mục chuẩn hóa hướng **vi mạch × Nhúng/IoT × co-design** theo định hướng nghiên cứu luận án. Ba lựa chọn đã chốt: mở rộng trục A (không tách trục riêng) · co-design cả hai hướng (vi mạch × nhúng/IoT và Polar × IoT) · đợt đầu 20–24 đề tài đủ 4 bậc P/I/T/R.

**Dữ liệu nguồn chuẩn (`06_Data/project_portfolio.json`, meta 1.5.0):**
- **A6 — Embedded Systems & SoC Integration** (8 đề tài): firmware bare-metal `A6-P01`, RTOS `A6-P02`, HW-SW trên SoC FPGA `A6-P03`, Linux nhúng `A6-P04`, thực tập `A6-I01`, DATN hệ nhúng hoàn chỉnh `A6-T01`, DATN tích hợp accelerator `A6-T02`, nghiên cứu phân hoạch HW/SW `A6-R01`.
- **A7 — IoT Systems & Edge Intelligence** (8 đề tài): node MQTT `A7-P01`, năng lượng pin `A7-P02`, TinyML `A7-P03`, BLE/LoRa `A7-P04`, thực tập IoT đầu-cuối `A7-I01`, DATN hệ giám sát đa nút `A7-T01`, DATN edge-AI `A7-T02`, nghiên cứu accuracy-energy-latency `A7-R01`.
- **AB mở rộng co-design** (5 đề tài): nhập môn 3 nền tảng `AB-P01`, tăng tốc AI biên trên SoC FPGA `AB-T05`, decoder SC Polar tiết kiệm năng lượng cho IoT `AB-T06`, và hai đề tài R định hướng luận án: co-design truyền thông tin cậy ở biên `AB-R02`, nền tảng biên tích hợp truyền thông + suy luận `AB-R03`. Purpose nhóm AB cập nhật tương ứng.
- Tổng: **105 đề tài / 16 nhóm** (42 P · 15 I · 34 T · 14 R); mọi đề tài T mới có MVT; 82 đề tài có `prereq_codes`, 24 dùng wildcard. Danh mục DATN HK1 **không đổi nội dung** (vẫn 21 đề tài mở), chỉ in nhãn 1.5.0.

**Script:** `validate_portfolio.py` mở rộng regex `A[0-5]` → `A[0-7]` (3 chỗ); `generate_catalogs.py`/`generate_site.py` thêm A6, A7 vào FAM_ORDER; `generate_ban_do.py` chuyển sang đếm động (không còn số ghi cứng), thêm blurb A6/A7/AB mới, khung dài hạn nhiều học kỳ, con đường luận án, và đổi tên đầu ra thành `Ban_do_de_tai.md/.html` (tên cũ `Ban_do_84_de_tai.*` đưa vào `_to_delete/`).

**View sinh lại toàn bộ từ 1.5.0:** 5 catalog `02_Project_Portfolio/`, danh mục + phiếu HK1 (docx/pdf, 21 đề tài, wildcard nguyên vẹn), `docs/index.html` + artifact (105 card), workbook sheet `Portfolio` (106×17), `Ban_do_de_tai.md/.html`. `VERSION` = 1.5.0; nhãn 7 docx chính sách/vận hành + release note đồng bộ 1.5.0; `validate_portfolio.py` **PASS 105 topics** trên cloud và trên máy chủ dự án.

**Khung tài liệu dài hạn:** README gốc, `00_START_HERE/README.md`, QUICK_LAUNCH, USER-GUIDE, MENTOR-GUIDE (bootcamp nhúng-IoT), `implementation-notes` (tài liệu 2.3) cập nhật: chương trình nhiều học kỳ, cohort HK1 chỉ là cohort hiện tại.

## v1.4.0 (bổ sung) — Bản đồ trực quan 84 đề tài · 2026-08-23

Theo yêu cầu chủ dự án ("đọc implementation-notes mà chưa hình dung ra từng project và cách vận hành"):

- **`Ban_do_84_de_tai.md/.html`** (gốc repo) — tài liệu diễn giải bằng ngôn ngữ đời thường: 14 nhóm đề tài là gì, từng đề tài trong 84 đề tài làm ra cái gì (bảng đầy đủ mã chuẩn/loại/sàn level/mã HK1/sản phẩm), 4 kịch bản sử dụng (giảng dạy loại P · thực tập loại I · mentor DATN 15 tuần 6 gate kèm ví dụ A4-T01 · nghiên cứu loại R + extension), 4 bước chọn đề tài kèm bảng định hướng nghề nghiệp.
- **`scripts/generate_ban_do.py`** — script sinh tài liệu trên từ `06_Data/` (đây là VIEW: sửa dữ liệu → chạy lại script, không sửa tay file đầu ra).
- Bản web chia sẻ được (mở từ điện thoại): https://claude.ai/code/artifact/68a2de47-bc1e-41cc-b588-cd34ffd90c90
- `implementation-notes.md/.html`: thêm dòng trỏ tới bản đồ trong bảng "Mở file nào khi nào".

## v1.4.0 (bổ sung cùng ngày — đồng bộ nhãn phiên bản) - 2026-08-23

Rà soát hoàn thiện toàn dự án phát hiện nhãn phiên bản cũ còn sót trên tài liệu hiện hành (danh mục/phiếu sinh tự động đã in 1.4.0 nhưng tài liệu chính sách còn in 1.3) — đã đồng bộ toàn bộ về **1.4.0**:

- 6 docx đổi nhãn "Version 1.3" → "Version 1.4.0": `01_Governance/Master_Mentoring_Handbook.docx`, `01_Governance/Mentor_Student_Working_Agreement.docx`, `01_Governance/AI_and_Academic_Integrity_Policy.docx`, `01_Governance/Cohort_HK1_2026_2027_Implementation_Guide.docx`, `03_Operations/Mentoring_Operating_Procedure_SOP.docx`, `03_Operations/Weekly_Report_and_Meeting_Template.docx`.
- `RELEASE_NOTE_HK1_2026_2027.md/.docx`: "hệ thống v1.3" và "Phiên bản 1.3" → v1.4.0.
- `00_START_HERE/README.md`: tiêu đề v1.3.1 → v1.4.0 · `05_Claude/QUICK_LAUNCH_PROMPT.txt`: v1.3.1 → v1.4.0.
- **Ghi nhận dọn dẹp:** chủ dự án đã xóa xong thư mục `DATN_mentor` (kiểm tra 23/08 — không còn tồn tại). Việc xóa tay còn lại duy nhất: `EEE Projects/_to_delete/`. `00_START_HERE/FILE_MANIFEST.md` cập nhật mô tả `scripts/release_cohort.py` (không còn đích mặc định).
- `implementation-notes.md/.html` → tài liệu 2.2 (cập nhật các đoạn "in Phiên bản 1.3", R7/R8, UNRESOLVED-6/7).
- Dựng lại gói `dist/DATN-Mentoring-HK1-2026-2027-v1.4.0/` + ZIP để gói bàn giao mang đúng tài liệu đã đồng bộ nhãn. `validate_portfolio.py` PASS 84 topics sau toàn bộ thay đổi.

## v1.4.0 - 2026-08-23
Thực thi `05_Claude/CLAUDE_MASTER_EXECUTION_DATN_MENTORING.md` như một bảng kiểm Definition of Done (§33) trên hệ thống **đã có**, không dựng lại. Bù 16 hạng mục còn thiếu, đóng 3 lỗi MAJOR.

**Template hồ sơ sinh viên (§5, §11, §12):**
- `04_Project_Template/STUDENT_PROFILE.md` — hồ sơ theo data model §5, tách **tự chấm** khỏi **kiểm chứng** bằng 5 trạng thái `SELF_REPORTED`/`EVIDENCE_VERIFIED`/`PARTIAL`/`MISSING`/`UNKNOWN` (§2.3 cấm gộp cả hồ sơ thành một số trung bình).
- `04_Project_Template/EVIDENCE_LEDGER.md` — sổ cái bằng chứng, 5 trạng thái kiểm chứng, kèm bảng truy vết claim → evidence dùng ở Gate 5–6.
- `04_Project_Template/DECISION_LOG.md` — nhật ký quyết định, không sửa đè dòng cũ.

**Template extension và bảo vệ (§13, §14):**
- `04_Project_Template/EXTENSION_PROPOSAL_TEMPLATE.md` — 8 điều kiện tiên quyết + 7 câu hỏi + phần riêng cho đề tài ML-assisted family B6.
- `04_Project_Template/THESIS_REVIEW_CHECKLIST.md` — rà kỹ thuật theo §14, có 3 cảnh báo cứng của track A.
- `04_Project_Template/DEFENSE_QUESTIONS.md` — 10 câu Definition of Done + câu theo artifact + câu phản thực + 4 mức ownership.

**Tài liệu (§26, §27, §28):**
- `10_Documentation/{USER-GUIDE,MENTOR-GUIDE,STUDENT-GUIDE,WORKFLOW}.md` — 4 guide phân theo vai trò, link chéo thay vì lặp nội dung.
- `CLAUDE.md` — chỉ dẫn vận hành repo cho phiên Claude sau; §0 cảnh báo rõ prompt master không nêu tên thư mục, chạy mù sẽ dựng hệ thống trùng lặp.
- `README.md` ở gốc — trả lời đủ 13 câu của §26.

**Đóng gói (§21, §23, §24, §25, §29):**
- `VERSION` = 1.4.0 · `scripts/build_release.py` · `dist/FINAL-AUDIT.md` · gói `dist/DATN-Mentoring-HK1-2026-2027-v1.4.0/` (65 file) + ZIP 787 KB, có MANIFEST và sha256.

**Ba lỗi MAJOR đã đóng:**
- **F1** `06_Data/*.json` `meta.version` = 1.3 trong khi CHANGELOG = 1.3.1 → tài liệu phát cho SV in "Phiên bản 1.3", mentor tra sổ thấy 1.3.1. Thống nhất cả 4 JSON + VERSION + mọi tài liệu về **1.4.0**.
- **F2** Sau khi bump, docx in 1.4.0 còn PDF vẫn 1.3 vì máy không có Chromium → hai bản phát cho SV lệch nhau. Sinh PDF ở môi trường có Chromium, kiểm chứng khớp docx (21 đề tài, wildcard `A1-P*` nguyên vẹn, 13 trang).
- **F3** `build_release.py` dùng `shutil.rmtree` → `PermissionError` trên thư mục mount, không đóng gói lại được lần hai. Bỏ `rmtree`, ghi đè bằng `copy2` và liệt kê file thừa; ZIP chỉ đóng gói file của lần build này.

**Khôi phục:** `scripts/release_cohort.py` bị dồn nhầm vào `_to_delete/` lúc 12:31 — 8 tài liệu đang trỏ tới nó. Đã khôi phục về `scripts/` và chạy thử lại thành công.

**Lệch có chủ ý so với §4:** không tạo `07_Research_Extension/` (trùng số với `07_Private/` đang có) và `08_Thesis_and_Defense/` (repo đã gom template theo sinh viên). Bốn file liên quan đặt trong `04_Project_Template/`. Lý do ghi ở `dist/FINAL-AUDIT.md` §2 F5–F6.

**Validation:** 13/13 PASS — xem `implementation-notes.md` §9 và `dist/FINAL-AUDIT.md` §3.

## v1.4 - 2026-08-23
**Gộp về MỘT thư mục duy nhất** theo quyết định của chủ dự án (thay quyết định tách bạch v1.3 — để dễ quản lý và theo dõi):
- `EEE Projects` là thư mục duy nhất của toàn bộ chương trình, bao gồm cả tài liệu cohort DATN HK1 2026-2027 (vốn được sinh và nằm sẵn ở thư mục gốc).
- `05_Claude/CLAUDE_MASTER_EXECUTION_DATN_MENTORING.md` — chuyển prompt điều hành DATN của tác giả về cùng chỗ với các prompt Claude khác.
- `scripts/release_cohort.py` nghỉ hưu (không còn thư mục thứ hai để phát hành) — chuỗi lệnh chuẩn rút gọn còn: `validate → generate_catalogs --docx [--pdf] → generate_site → CHANGELOG`.
- `DATN_mentor` ngừng sử dụng: chỉ còn README chỉ đường + `_to_delete/` (bản sao trùng lặp, đã đối chiếu giống hệt bản EEE) — **xóa tay cả thư mục khi yên tâm**.
- Đối chiếu trước khi gộp: danh mục hai bên giống hệt từng byte; không mất nội dung nào.

## v1.3.1 - 2026-08-23
Khắc phục các nguồn gây hiểu lầm còn lại (rà soát theo yêu cầu chủ dự án):
- **Đồng nhất phiên bản:** meta.version cả 4 file `06_Data/` → **1.3**; regenerate toàn bộ view — header mọi tài liệu phát hành nay ghi "Phiên bản 1.3 · 2026-08-23", hết cảnh danh mục ghi v1.1 trong khi sổ tay ghi v1.3.
- **Một bộ phiếu duy nhất (đóng UNRESOLVED-2):** `01_Governance/Readiness_and_Topic_Selection_Forms.docx` (bản viết tay v1.0, trùng tên "Phiếu 1–5" với phiếu sinh tự động) chuyển vào `99_Archive/2026-08-23_v1.0/` — hết rủi ro in nhầm mẫu cũ.
- **Release note đổi tên bỏ số phiên bản:** `RELEASE_NOTE_v1.1_*` → `RELEASE_NOTE_HK1_2026_2027.md/.docx`, nội dung cập nhật theo v1.3 và nhấn "một bộ phiếu duy nhất"; `release_cohort.py` cập nhật danh sách; bản tên cũ dồn vào `_to_delete/`.
- **Handbook §5.2 (đóng UNRESOLVED-3):** thêm ghi chú "Nguồn chuẩn của ngưỡng: 06_Data/readiness_rubrics.json — nếu hai nơi lệch nhau, JSON thắng."
- **Nhãn version (đóng UNRESOLVED-4):** 6 docx chính sách (Handbook, Agreement, AI Policy, Cohort Guide, SOP, Weekly template) đổi nhãn "Version 1.0" → "Version 1.3".
- Workbook Rubrics: ghi chú nguồn chuẩn bỏ ghim "v1.1" (trỏ meta.version hiện hành).
- `QUICK_LAUNCH_PROMPT.txt` viết lại cho đúng trạng thái hiện tại (hệ thống đã xây xong; phiên mới đọc implementation-notes trước, tuân thủ chuỗi validate → generate → release; nhận biết hai dự án tách bạch).
- VALIDATION PASS 84 topics sau toàn bộ thay đổi; PDF danh mục regenerate bằng lệnh `--pdf` chuẩn.

## v1.3 - 2026-08-23
**Tách bạch hai dự án** theo quyết định của chủ dự án (đảo lại phần gom v1.2.3 — hai thư mục là HAI DỰ ÁN KHÁC PHẠM VI, không phải một dự án hai chỗ):
- `EEE Projects` = dự án TỔNG: quản lý toàn bộ NCKH, luận án, hướng dẫn sinh viên nghiên cứu, thực tập tốt nghiệp và mentor cộng đồng IC design — chứa nguồn chuẩn `06_Data/` (84 đề tài P/I/T/R), scripts, governance, operations, workbook, website. Mọi chỉnh sửa nội dung diễn ra ở đây.
- `DATN_mentor` = dự án CON: chỉ vận hành cohort Đồ án tốt nghiệp HK1 2026-2027 — `05_Claude/CLAUDE_MASTER_EXECUTION_DATN_MENTORING.md` + danh mục (docx/pdf) + phiếu + release note + `README.md` (mới, nêu quan hệ hai dự án).
- Khôi phục toàn bộ hệ thống (bản mới nhất, 61 file + build) về `EEE Projects`; kiểm chứng tại chỗ: `validate_portfolio.py` **PASS 84 topics**.
- Mới: `scripts/release_cohort.py` — copy 5 tài liệu cohort từ `EEE Projects` sang `DATN_mentor` sau mỗi lần regenerate; `DATN_mentor` không bao giờ là nơi sửa nội dung.
- Cập nhật `implementation-notes.md/.html` (§1 đường dẫn, §4 lịch sử, §12 R7/UNRESOLVED-6, §20 lệnh, §23 changelog) và FILE_MANIFEST.
- **Cần xóa tay:** `EEE Projects/_to_delete/` và `DATN_mentor/_to_delete/` (phiên làm việc không có quyền xóa file).

## v1.2.3 - 2026-08-23
Gom dự án về **một thư mục duy nhất**.
- Trước đây dự án nằm ở `C:\Users\admin\Downloads\EEE Projects`, trong khi `DATN_mentor` — thư mục kết nối với phiên làm việc — chỉ có prompt master + 3 tài liệu phát hành. Hai nơi, không nơi nào đầy đủ.
- Đã chuyển toàn bộ 61 file sang `DATN_mentor`: đối chiếu danh sách file (không thiếu file nào) + checksum (5 file `02_Project_Portfolio/*.docx` khác byte do vừa regenerate, nội dung trích xuất giống hệt).
- **Kiểm chứng tại vị trí mới:** `validate_portfolio.py` PASS 84 topics · `generate_catalogs.py --docx` sinh đủ 7 view (docx đổ đúng vào `02_Project_Portfolio/` và thư mục gốc) · `generate_site.py` sinh `docs/index.html` 128 KB · wildcard `A1-P*` còn nguyên trong docx sinh lại. Script không phải sửa dòng nào — `BASE` lấy từ thư mục cha của `scripts/`.
- Máy có sẵn `python3` 3.10 + `pandoc` + `git`; **không có Chromium** nên `--pdf` phải chạy nơi khác hoặc cài trình duyệt rồi đặt `CHROME_BIN`. PDF danh mục hiện tại là bản v1.2.1, vẫn đúng nội dung.
- Bản cũ dồn vào `EEE Projects/_to_delete/` (61 file) kèm file `ĐÃ_CHUYỂN_SANG_DATN_mentor.md` ở thư mục gốc — **cần xóa tay**, phiên làm việc không có quyền xóa file trên máy. Ghi thành R7 / UNRESOLVED-6 trong `implementation-notes.md`.
- Cập nhật mọi tham chiếu đường dẫn trong `implementation-notes.md/.html` (§1 thư mục dự án, §2 phạm vi repo, §4 cây thư mục, §20 lệnh `cd`). `AUDIT_REPORT.md` giữ nguyên tên cũ vì là bản ghi lịch sử.

## v1.2.2 - 2026-08-23
Tài liệu hệ thống — thực thi `05_Claude/CLAUDE_MASTER_EXECUTION_DATN_MENTORING.md` §17–§20.
- `implementation-notes.md/.html` viết lại thành **tài liệu hệ thống 23 mục** theo §18, thay cho sổ tay vận hành 10 mục: kiểm kê nguồn có cột thẩm quyền · mô hình dữ liệu đầy đủ (hệ mã, schema, 84 đề tài theo family/type/level, rubric, gate, cohort, workbook) · 9 tính năng · đặc tả từng script kèm failure mode · danh sách file cấm sửa tay · bảng validation + negative test · 12 quyết định thiết kế kèm phương án đã loại · 8 hạn chế · sổ rủi ro đầy đủ + 5 tồn đọng · 9 quy trình vận hành (thêm SV, sửa đề tài, weekly review, gate review, mở extension, closeout, regenerate, backup, phát hành).
- **Gộp** phần mở đầu "★ Hiểu bản chất hệ thống trong 10 phút" (từ điển 12 khái niệm, một học kỳ diễn ra thế nào, 4 nhịp công việc, mở file nào khi nào), roadmap 9 bước, 10 nguyên tắc bất biến, prompt cho Claude (Phụ lục A), nguyên tắc riêng tư (Phụ lục B) từ bản sổ tay v1.3 viết song song — không mất nội dung nào.
- `implementation-notes.html`: dựng lại từ bản .md bằng converter (đảm bảo tương đương nội dung — đã đối chiếu theo từ), mục lục dính lề, anchor cho mọi heading, callout phân biệt quy tắc/cảnh báo/ghi chú, badge thẩm quyền CHUẨN/SINH/SỔ/LƯU trong bảng, dark mode, print A4 28 trang có lặp dòng tiêu đề bảng.
- Bản web (artifact riêng tư, share được): https://claude.ai/code/artifact/ec2b8b23-f45b-4850-ba64-509acc4766cf
- **Ba tồn đọng mới phát hiện** khi kiểm kê toàn repo, ghi ở `implementation-notes.md` §12: **UNRESOLVED-2** `01_Governance/Readiness_and_Topic_Selection_Forms.docx` (v1.0, viết tay) xung đột cấu trúc với phiếu sinh tự động v1.2.1 — cả hai đều tự gọi là "Phiếu 1–5", rủi ro in nhầm; **UNRESOLVED-3** Handbook §5.2 chép cứng ngưỡng WR trùng `readiness_rubrics.json`; **UNRESOLVED-4** 5 file governance còn nhãn "Version 1.0".
- **Đã sửa:** `FILE_MANIFEST.md` — chuỗi lệnh regenerate cập nhật thành `validate → generate_catalogs --docx --pdf → generate_site → CHANGELOG` (trước đây thiếu `--pdf` và bước sinh trang web), và mô tả lại vai trò của implementation-notes.

## v1.2.1 - 2026-08-23
Sửa lỗi render và bổ sung 3 khoảng trống phát hiện khi rà soát độc lập bản phát hành (các audit trước chưa bắt được).

**Lỗi render — có mặt trong tài liệu sinh viên:**
- `scripts/generate_catalogs.py`: dấu `*` của mã pattern wildcard (`A1-P*`) bị pandoc hiểu là cú pháp in nghiêng, làm mất ký tự wildcard và để lại một dấu `*` lạc không chú giải (danh mục cohort hiển thị "(mã tham chiếu: A1-P)\*"). Ảnh hưởng 3/21 đề tài cohort (`A1-T01`, `A3-T01`, `B2-T01`) và 19/84 đề tài toàn portfolio. Sửa: thêm `star()` escape mọi văn bản lấy nguyên văn từ nguồn chuẩn + bọc mã trong code span. `generate_site.py` không dính lỗi này (dùng HTML escaping).
- Thêm dòng chú giải quy ước mã tham chiếu (`meta.prereq_codes_convention`) vào danh mục cohort, Master Portfolio và 4 catalog P/I/T/R — trước đây nghĩa của `*` không được giải thích ở đâu.

**Research Readiness — dead data đưa vào sử dụng:**
- `readiness_rubrics.json`: `research_readiness.expectations` (kỳ vọng RR theo loại hoạt động) trước nay không generator nào đọc. Chuyển sang list có `key`/`label`/`expectation`, thêm `max_total: 20` và `note`. Phiếu 5.2 nay có tổng `/20` và bảng kỳ vọng RR — trước đó mentor không có quy tắc quyết định nào cho RR trong khi WR có 6 ngưỡng. **Không đặt ngưỡng số cho RR** vì nguồn chuẩn chỉ định nghĩa định tính.

**Phiếu 5:**
- Thêm 3 dòng Level vào 5.3 (level đánh giá của SV · level tối thiểu của đề tài · đối chiếu đạt sàn) kèm bảng tra L0–L5. Trước đây `min_level` có ở mọi đề tài nhưng phiếu không có chỗ ghi để đối chiếu.
- Ngưỡng WR: "Advanced B6/AB-R" → "Advanced (đề tài family `B6`, hoặc đề tài loại R của family `AB`)" + ghi chú phân biệt family `B6` với mã ngắn cohort `B6`.
- Thêm cảnh báo thang điểm: Phiếu 2 (TR) chấm 0–5; Phiếu 5.1/5.2 (WR/RR) chấm 0–4.

**Validator:**
- `validate_portfolio.py` thêm cross-check: mỗi `gate_deadlines[g]` phải trùng ngày cuối tuần kết thúc gate đó; `week_calendar` phải liền mạch và khớp `start_date`/`end_date`; RR `max_total` = 5 × `scale.max`; `expectations` phải phủ đủ các loại hoạt động có ngưỡng WR. Đã kiểm bằng negative test (cố tình làm lệch → FAIL đúng chỗ).

**Reproducibility:**
- `generate_catalogs.py` thêm cờ `--pdf`: pandoc → HTML (print CSS A4, lặp dòng tiêu đề bảng qua trang) → Chromium/Chrome/Edge headless `--print-to-pdf`. Trước đây PDF danh mục được in thủ công, không có lệnh tái lập. Đặt `CHROME_BIN` nếu trình duyệt không nằm trên PATH.

**Regenerate:** 5 view portfolio + danh mục cohort (docx + pdf, 13 trang) + phiếu. Diff so với v1.1: danh mục chỉ khác đúng 4 dòng (1 dòng chú giải mới + 3 dòng wildcard được sửa), phiếu chỉ thêm/sửa các mục nêu trên — không mất nội dung nào. VALIDATION PASS 84 topics.

## v1.2 - 2026-08-23
Hoàn tất bước 7 roadmap (lớp web công khai — mục tùy chọn cuối cùng):
- Mới: `scripts/generate_site.py` — sinh trang catalog sinh viên từ 06_Data (CHỈ dữ liệu public, không dữ liệu SV).
- Mới: `docs/index.html` — trang tĩnh self-contained, sẵn sàng GitHub Pages (Settings → Pages → branch main, folder /docs): danh mục 84 đề tài có bộ lọc theo loại/nhóm/level + tìm kiếm, lịch gate DATN HK1 2026-2027 với hạn chót theo ngày, hướng dẫn chọn đề tài + readiness test, quy tắc chương trình. Hỗ trợ dark mode, mobile.
- Trang cũng được xuất bản dạng Claude Artifact (link riêng tư của mentor, có thể share cho SV): https://claude.ai/code/artifact/dcd9e447-b4e7-4fba-ace9-32544ea94cc7
- QA: đủ 84/84 mã đề tài, 21 nhãn cohort, 6 hạn gate; quét chuỗi nhạy cảm: sạch.

## v1.1.1 - 2026-08-23
Hoàn tất bước 8-9 roadmap (dry-run + nghiệm thu):
- Sửa lỗi numbering Handbook §9 (danh sách nay khởi động lại 1-5, không nối tiếp §6) — đóng finding C7.
- `tests/DRY_RUN_A_TRACK_A4-T01.md` + `tests/DRY_RUN_B_TRACK_B2-T01.md`: dry-run giấy 2 luồng, PASS; luồng B diễn tập trượt Gate 3 → reduce scope + warning ladder hoạt động đúng.
- `05_Claude/ACCEPTANCE_CHECKLIST.md`: nghiệm thu 36/36 mục (kèm ghi chú 2 mục "đạt có điều kiện vận hành").
- Mới: `FINAL_SYSTEM_AUDIT.md` — bằng chứng nghiệm thu theo nhóm A-G + hạn chế còn lại.
- Mới: `RELEASE_NOTE_v1.1_HK1_2026_2027.md/.docx` — thông báo phát hành cho sinh viên (bảng đối chiếu mã cũ ↔ mã chuẩn, phiếu mới, MVT).
- QA bổ sung: xác nhận workbook không chứa dữ liệu SV thật; mọi file tham chiếu trong FILE_MANIFEST tồn tại; validation PASS.

## v1.1 - 2026-08-23
Chuẩn hóa toàn hệ thống sau AUDIT_REPORT.md (các quyết định CR-1/CR-2/CR-3 do mentor ủy quyền 23/08/2026).

**06_Data (nguồn chuẩn):**
- `project_portfolio.json` → 84 đề tài (thêm `A2-T03` Adder PPA, `B5-T03` Adaptive co-design — trước đây chỉ có trong danh mục cohort dưới mã A8/B11). Mở rộng schema: `mvt` (bắt buộc cho T), `tools` per-topic, `status`, `prereq_codes` (máy đọc được), `career_relevance`, `cohort_alias`, `checkpoints_15w`, `eligibility` (A0 hands-on rule); sửa lỗi tham chiếu `A5-T2` → `A5-T02`; thêm `eligibility_rules` (điều kiện Thực tập tốt nghiệp trước DATN) và `meta`.
- `readiness_rubrics.json` → bổ sung đầy đủ: 16 năng lực TR + anchors; WR 0-4 (/20) + ngưỡng ≥10/12/14/15/16/17; RR 0-4; các lựa chọn kết luận của mentor. (Đóng C2, C3, H3.)
- `milestone_gates.json` → chuyển sang object có key (gate/name/weeks/pass_criteria/fail_rule).
- Mới: `cohort_HK1_2026_2027.json` — mốc hành chính, lịch tuần, deadline gate theo ngày thật, 21 đề tài mở + alias, career guide. (Đóng M3, H5-eligibility.)

**Scripts (mới):** `scripts/validate_portfolio.py` (fail-fast; PASS 84 topics), `scripts/generate_catalogs.py` (sinh mọi view từ 06_Data).

**Views regenerate từ nguồn chuẩn:** Master Portfolio + 4 catalog P/I/T/R (02_Project_Portfolio/), `Danh_muc_de_tai_DATN_Nhom_A_B_HK1_2026_2027.docx/.pdf` (mã chuẩn + alias cohort — đóng C1, H1), `Phieu_lua_chon_va_danh_gia_de_tai_DATN_HK1_2026_2027.docx` (thang chuẩn — đóng C2). Bản gốc v1.0 lưu tại `99_Archive/2026-08-23_v1.0/`.

**Governance/Operations:** Handbook §7 tinh chỉnh invariant B6 theo nhánh detection/ranking (đóng M1, C4); CLAUDE_PROJECT_CONTEXT cập nhật tương ứng; workbook: sheet Portfolio rebuild 84 đề tài (+MVT/Status/Alias/Career), sửa công thức Total students, nới Weekly_Status 1500 dòng, Milestones 100 SV, ghi chú nguồn chuẩn ở Rubrics (đóng C3, L3); template weekly report thêm header định danh; mới `LEGACY_PACKAGE_CHECKLIST.md`; mới `07_Private/` + `.gitignore` (đóng H5).

**Danh tính chương trình:** tên thống nhất "Engineering & Research Mentoring Program (Lucero)"; tác giả ThS. Đinh Văn Nam (Mr. Lucero Dinh), Khoa Điện–Điện tử, Trường Kỹ thuật, Đại học Phenikaa (đóng C6/L1 — "Lucero" là bút danh tác giả, không phải bất nhất).

## v1.0 - 2026-08-23
- Khởi tạo master portfolio A/B/AB, governance, operations, templates và Claude handoff.
