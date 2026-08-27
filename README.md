# Engineering & Research Mentoring Program (Lucero)

Chương trình hướng dẫn sinh viên làm **Project môn học · Thực tập · Đồ án tốt nghiệp · Nghiên cứu khoa học**
trong lĩnh vực **thiết kế vi mạch số (Digital IC/FPGA/ASIC) · hệ nhúng & IoT · giải mã Polar · co-design thuật toán–phần cứng**.

**Tác giả & mentor:** ThS. Đinh Văn Nam (Mr. Lucero Dinh)
Khoa Điện–Điện tử, Trường Kỹ thuật, Đại học Phenikaa

`105 đề tài` · `16 nhóm chuyên môn` · `4 loại hoạt động P/I/T/R` · `phiên bản 1.7.0`

> **📚 Danh mục đề tài — bản web tra cứu nhanh (lọc theo nhóm, mức độ, loại hoạt động):**
> **https://lucero6886.github.io/lucero-mentoring/**

Đây là chương trình **dài hạn, chạy qua nhiều học kỳ** — không phải danh mục của riêng một kỳ.
Mỗi học kỳ mở một đợt (cohort) lấy đề tài từ kho chung này.

---

## 🎓 Nếu bạn là sinh viên — bắt đầu từ đây

### Bước 1 · Xem có những đề tài gì

| Cách xem | Mở |
|---|---|
| **Nhanh nhất** — lọc, tìm kiếm trên web | [Trang danh mục](https://lucero6886.github.io/lucero-mentoring/) |
| **Hiểu bản chất từng nhóm đề tài** — mỗi nhóm dạy gì, mỗi đề tài làm ra sản phẩm gì | [`Ban_do_de_tai.md`](Ban_do_de_tai.md) |
| **Danh mục đồ án tốt nghiệp kỳ hiện tại** (bản in được) | [`Danh_muc_de_tai_DATN_HK1_2026_2027.pdf`](Danh_muc_de_tai_DATN_HK1_2026_2027.pdf) |
| **Nên đọc gì trước khi bắt đầu** — tài liệu nền tảng theo từng hướng | [`09_References/READING-LIST.md`](09_References/READING-LIST.md) |
| **Toàn bộ catalog theo loại** (P / I / T / R) | [`02_Project_Portfolio/`](https://github.com/Lucero6886/lucero-mentoring/tree/main/02_Project_Portfolio) — 5 file Word tải về |

### Bước 2 · Hiểu chương trình chạy thế nào trước khi chọn

Đọc **[`10_Documentation/STUDENT-GUIDE.md`](10_Documentation/STUDENT-GUIDE.md)** — 10 phút, trả lời đúng những
câu quyết định kết quả của bạn: *cái gì được tính là tiến độ · nộp gì mỗi tuần · vì sao phải có baseline trước ·
dùng AI thế nào cho đúng · cuối kỳ nộp gì.*

Ba trục đánh giá, thiếu một trục là chưa xong:

| Trục | Nghĩa |
|---|---|
| **Technical completion** | Phần lõi chạy đúng, có kết quả định lượng |
| **Reproducibility** | Người khác cầm repo của bạn, làm theo README, chạy ra kết quả tương tự |
| **Ownership** | Bạn giải thích được mọi thành phần chính bằng lời của mình |

> **Không có trục "chăm chỉ".** Bỏ nhiều thời gian mà không ra bằng chứng thì chưa tính là tiến độ —
> đó là tín hiệu để đổi cách làm sớm, không phải để lo lắng.

### Bước 3 · Chọn đề tài theo hướng nghề nghiệp bạn muốn đi

| Bạn muốn đi hướng | Đề tài nên xem trước | Bước tiếp theo |
|---|---|---|
| Digital IC / RTL Verification | `A1-T01` · `A4-T01` · `A4-T02` | `B1-T01` · `B2-T01` |
| FPGA / DSP Hardware | `A2-T01` · `A3-T01` · `A2-T02` | `B1-T01` · `B2-T01` |
| ASIC Physical Flow / PPA | `A4-T01` · `A4-T02` · `A2-T03` | `AB-T01` |
| EDA infrastructure / DevOps phần cứng | `A5-T01` · `A5-T02` | `AB-T01` |
| **Hệ nhúng & IoT** | `A6-T01` · `A7-T01` · `A7-T02` | `A6-T02` · `AB-T05` |
| Nghiên cứu thuật toán Polar | `B0-T01` · `B3-T01` · `B4-T01` | `B5-T01` · `B4-T02` |
| AI hỗ trợ bộ giải mã | `B5-T01` · `B4-T02` | `B6-T02` |
| **Co-design thuật toán – phần cứng** | `A6-T02` · `AB-T05` · `AB-T06` | `AB-R02` · `AB-R03` |

Rồi nộp **3 nguyện vọng theo thứ tự** (ghi **mã chuẩn**, ví dụ `A4-T01`) bằng phiếu
[`Phieu_lua_chon_va_danh_gia_de_tai_DATN_HK1_2026_2027.docx`](Phieu_lua_chon_va_danh_gia_de_tai_DATN_HK1_2026_2027.docx),
gửi trực tiếp cho mentor theo kênh đã thông báo.

> ⚠️ **Đừng đăng phiếu, họ tên, mã số sinh viên hay điểm số lên repo công khai này.**
> Thông tin cá nhân chỉ gửi riêng cho mentor.

### Ba điều nên biết trước khi chọn

1. **Nguyện vọng quyết định hướng — mức sẵn sàng quyết định độ lớn.** Bạn thích đề tài khó không có nghĩa
   được giao ngay phạm vi lớn nhất. Mỗi đề tài ghi *sàn năng lực* và *kiến thức đầu vào* — hãy đọc kỹ hai dòng đó.
2. **Chưa qua bài kiểm tra năng lực (readiness test) thì chưa chốt phạm vi.** Đây là bài nhỏ 4–10 giờ chạm đúng
   kỹ năng quan trọng nhất của đề tài bạn chọn — để cả hai bên biết chắc trước khi bắt đầu.
3. **Có thể đổi phạm vi giữa kỳ, và điều đó bình thường.** Trễ tiến độ ở Gate 3 thì đề tài được **thu nhỏ**,
   không phải bị đánh trượt. Cái bị cắt là phần mở rộng — cái không bao giờ bị cắt là phần lõi, kiểm chứng,
   khả năng tái lập và việc bạn phải hiểu sản phẩm của mình.

---

## 🧭 Sáu trạm kiểm soát tiến độ (gate) trong 15 tuần

Mọi sinh viên đi qua cùng một khuôn — nhờ vậy mentor theo dõi được nhiều người cùng lúc mà không ai bị bỏ rơi.

| Gate | Tuần | Điều kiện qua | Luật cứng nếu chưa đạt |
|---|---|---|---|
| **1** · Problem & Foundation | 1–2 | Hiểu bài toán, input/output, baseline, metric, lỗ hổng kiến thức | Điều chỉnh đề tài hoặc kế hoạch học |
| **2** · Baseline | 3–5 | Baseline chạy được + bằng chứng tái lập | **Đóng phần mở rộng nghiên cứu** |
| **3** · Core Implementation | 6–8 | Phần lõi + kết quả định lượng trung gian | **Thu nhỏ phạm vi** |
| **4** · Experiments | 9–11 | Thực nghiệm chính, bảng/hình chính | Không thêm thuật toán lớn mới |
| **5** · Analysis & Draft | 12–13 | Phân tích + bản thảo đầy đủ | Không dùng viết lách che lỗ hổng |
| **6** · Reproducibility & Defense | 14–15 | Chạy lại sạch, slides, demo, gói bàn giao | Chỉ xác nhận hoàn thành khi đủ **technical + reproducibility + ownership** |

Khung này **tính theo số tuần kể từ ngày sinh viên nhận đề tài**, dùng chung cho mọi khóa — không gắn với một học kỳ cụ thể.
Mỗi khóa chỉ khai một ngày bắt đầu trong [`06_Data/cohort_HK1_2026_2027.json`](06_Data/cohort_HK1_2026_2027.json);
lịch từng tuần và hạn từng gate được suy ra tự động bằng [`scripts/cohort_schedule.py`](scripts/cohort_schedule.py).

---

## 👩‍🏫 Nếu bạn là mentor / giảng viên

| Việc | Mở |
|---|---|
| Hiểu toàn hệ thống trong 10 phút | [`implementation-notes.md`](implementation-notes.md) — mục ★ đầu tài liệu |
| Thao tác hằng tuần: nhận sinh viên, chạy gate, xử lý chậm tiến độ | [`10_Documentation/MENTOR-GUIDE.md`](10_Documentation/MENTOR-GUIDE.md) |
| **Vận hành trên GitHub**: cái gì công khai/riêng tư, nhịp tuần, gate review, phân quyền | [`10_Documentation/GITHUB-WORKFLOW.md`](10_Documentation/GITHUB-WORKFLOW.md) |
| Sửa đề tài / thang điểm / lịch rồi sinh lại tài liệu | [`10_Documentation/WORKFLOW.md`](10_Documentation/WORKFLOW.md) |
| Tra nhanh toàn bộ | [`10_Documentation/USER-GUIDE.md`](10_Documentation/USER-GUIDE.md) |
| Chính sách gốc: triết lý, thang đánh giá, mức tham gia | [`01_Governance/Master_Mentoring_Handbook.md`](01_Governance/Master_Mentoring_Handbook.md) |
| Quy tắc dùng AI và liêm chính học thuật | [`01_Governance/AI_and_Academic_Integrity_Policy.md`](01_Governance/AI_and_Academic_Integrity_Policy.md) |
| Thỏa thuận làm việc mentor–sinh viên | [`01_Governance/Mentor_Student_Working_Agreement.md`](01_Governance/Mentor_Student_Working_Agreement.md) |
| Quy trình vận hành (SOP) và mẫu báo cáo tuần | [`03_Operations/`](https://github.com/Lucero6886/lucero-mentoring/tree/main/03_Operations) |
| Biểu mẫu hồ sơ từng sinh viên | [`04_Project_Template/`](https://github.com/Lucero6886/lucero-mentoring/tree/main/04_Project_Template) |

---

## 🗂 Cấu trúc kho tài liệu

```
06_Data/              ← NGUỒN CHUẨN: 105 đề tài, thang đánh giá, 6 gate, dữ liệu từng đợt (JSON)
scripts/              ← Sinh mọi tài liệu từ nguồn chuẩn + kiểm tra tính nhất quán
02_Project_Portfolio/ ← Catalog theo loại hoạt động (sinh tự động)
01_Governance/        ← Chính sách: sổ tay, thỏa thuận làm việc, quy tắc dùng AI
03_Operations/        ← Quy trình vận hành + workbook theo dõi
04_Project_Template/  ← 15 biểu mẫu hồ sơ dự án của từng sinh viên
09_References/        ← Tài liệu nền tảng nên đọc, phân theo hướng nghiên cứu
10_Documentation/     ← Hướng dẫn theo vai trò (sinh viên / mentor / vận hành / GitHub)
docs/                 ← Trang web danh mục (GitHub Pages)
tests/                ← Hai bài chạy thử toàn quy trình (A-track và B-track)
```

**Quy tắc quan trọng nhất của kho này:** `06_Data/*.json` là **nguồn chuẩn duy nhất**.
Mọi danh mục, phiếu, trang web đều là **bản sinh tự động** từ đó — sửa tay các bản sinh sẽ bị ghi đè ở lần
phát hành sau. Muốn đổi nội dung: sửa JSON → chạy lại script.

```bash
python3 scripts/validate_portfolio.py              # phải PASS trước
python3 scripts/generate_catalogs.py --docx --pdf  # sinh catalog + danh mục + phiếu
python3 scripts/generate_site.py                   # sinh docs/index.html
python3 scripts/generate_ban_do.py                 # sinh Ban_do_de_tai.md/.html
python3 scripts/export_governance_md.py            # sinh bản .md đọc-trên-web từ .docx chính sách
```

---

## 💬 Hỏi đáp, thảo luận, đề xuất

- **Hỏi về một đề tài cụ thể**, làm rõ phạm vi, xin gợi ý tài liệu → mở **Issue** (dùng mẫu có sẵn) hoặc **Discussions**.
- **Đề xuất đề tài mới** hoặc góp ý cải tiến mô tả đề tài → Issue với mẫu *Đề xuất đề tài mới*.
- **Báo lỗi tài liệu** (sai chính tả, link hỏng, số liệu lệch) → Issue.
- **Nộp nguyện vọng, hồ sơ cá nhân, điểm số** → **không dùng repo này**, gửi riêng cho mentor.

Chi tiết cách tham gia: [`CONTRIBUTING.md`](CONTRIBUTING.md).
Cách cả chương trình vận hành trên GitHub — repo riêng của em, báo cáo tuần, gate review:
[`10_Documentation/GITHUB-WORKFLOW.md`](10_Documentation/GITHUB-WORKFLOW.md).

---

## ⚖️ Giấy phép và trích dẫn

Tài liệu (mọi file `.md`, `.docx`, `.pdf`, `.html`, dữ liệu trong `06_Data/`) phát hành theo
**CC BY-NC-SA 4.0**; mã nguồn trong `scripts/` theo **MIT**. Chi tiết: [`LICENSE`](LICENSE).

Repo có sẵn file [`CITATION.cff`](CITATION.cff) — bấm **Cite this repository** ở cột phải trang GitHub
để lấy trích dẫn dạng APA hoặc BibTeX. Cách ghi nguồn đề xuất:

> Đinh Văn Nam (Lucero Dinh), *Engineering & Research Mentoring Program (Lucero)*,
> Khoa Điện–Điện tử, Trường Kỹ thuật, Đại học Phenikaa, 2026.

---

## Nguyên tắc không thay đổi

Nguyện vọng là mong muốn — **mức sẵn sàng quyết định phạm vi** · **Baseline trước cái mới** ·
Không có baseline ở Gate 2 → không mở phần nghiên cứu mở rộng · Trễ tiến độ → **thu nhỏ phạm vi, không hạ chuẩn** ·
Mentor không làm thay phần thực thi · **Không giải thích được = chưa hoàn thành** ·
Mỗi dự án để lại **gói bàn giao** cho khóa sau · Kỹ sư giỏi và nhà nghiên cứu giỏi **ngang giá trị nhau**.
