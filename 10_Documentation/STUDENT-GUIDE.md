# Hướng dẫn cho sinh viên

**Engineering & Research Mentoring Program (Lucero)** · GVHD: ThS. Đinh Văn Nam (Mr. Lucero Dinh)
Khoa Điện–Điện tử, Trường Kỹ thuật, Đại học Phenikaa

Trang này dùng cho **mọi khóa** của chương trình — mọi mốc dưới đây tính theo **số tuần kể từ ngày em chính thức nhận đề tài**, không gắn với một học kỳ cụ thể. Ngày dương lịch tương ứng của khóa em do mentor công bố khi giao đề tài.

Đọc hết trang này một lần trước tuần 1. Nó trả lời: cái gì được tính là tiến độ, nộp gì mỗi tuần, và điều gì khiến một đồ án được xác nhận hoàn thành.

---

## 1. Đồ án của em được đánh giá bằng gì

Ba trục, thiếu một trục là chưa xong:

| Trục | Nghĩa |
|---|---|
| **Technical completion** | Phần lõi (MVT) chạy đúng và có kết quả định lượng |
| **Reproducibility** | Người khác cầm repo của em, làm theo README, chạy ra kết quả tương tự |
| **Ownership** | Em giải thích được mọi thành phần chính bằng lời của mình |

**Không có trục "chăm chỉ".** Bỏ nhiều thời gian mà không ra evidence thì vẫn là chưa có tiến độ — và đó là tín hiệu để em đổi cách làm sớm, không phải để lo lắng.

## 2. Cái gì được tính là evidence

**Được tính:** code · commit · testbench · waveform · log mô phỏng · synthesis/STA report · bảng PPA ·
file cấu hình thí nghiệm · script · notebook · hình · bảng số · số liệu đo · demo · technical note · giải thích bằng lời.

**Không được tính:** "em đã đọc" · "em đã tìm hiểu" · "em đã hiểu rồi" · "code chạy được" (không kèm log/kết quả) · "gần xong".

Đây không phải sự khắt khe. Một tuần đọc tài liệu là việc thật — nhưng nó chỉ trở thành tiến độ khi biến thành một technical note nêu được *problem – input – output – method – metric – chỗ chưa hiểu*. Viết ra chính là lúc em phát hiện mình chưa hiểu chỗ nào.

## 3. Nộp gì mỗi tuần

Dùng `WEEKLY_REPORT_TEMPLATE.md` trong thư mục project của em, **nộp trước buổi gặp**:

Goal tuần trước → Completed → **Evidence (link)** → Cái gì hỏng → Chẩn đoán của em → Em đã thử gì → Đề xuất bước tiếp → Câu hỏi cho mentor → AI đã dùng thế nào.

Buổi gặp không dùng để kể lại cả tuần — mentor đọc report trước. Buổi gặp để gỡ vướng và chốt việc.

**Hai điều tạo khác biệt lớn nhất:**
- Đến buổi gặp với **đề xuất bước tiếp của chính em**, thay vì hỏi "em làm gì tiếp ạ?".
- Khi kẹt, mô tả theo mẫu: *em định làm gì → kỳ vọng gì → thực tế ra gì → đã kiểm những gì → em nghĩ nguyên nhân là gì*. Nói "em chạy không được" không đủ để ai giúp em.

## 4. Vì sao baseline quan trọng đến thế

Quy tắc trung tâm: **Correctness → Baseline → Measurement → Analysis → Improvement → Research Extension.**

Baseline là phiên bản đơn giản, đúng, chạy được, đo được. Chưa có nó thì mọi "cải tiến" đều vô nghĩa — em không có gì để so, và không biết con số mới là tốt hơn hay chỉ là lỗi khác.

**Chưa qua Gate 2 (hết tuần 5) thì phần mở rộng nghiên cứu đóng.** Không thương lượng. Đây là cơ chế bảo vệ em khỏi việc tiêu hết học kỳ vào phần hào nhoáng rồi không có lõi để nộp.

## 5. Sáu gate — và điều gì xảy ra nếu trễ

| Gate | Tuần | Hạn nộp | Cần có |
|---|---|---|---|
| 1 · Problem & Foundation | 1–2 | hết tuần 2 | Hiểu bài toán, I/O, baseline, metric, lỗ hổng kiến thức |
| 2 · Baseline | 3–5 | hết tuần 5 | Baseline chạy được + tái lập được |
| 3 · Core Implementation | 6–8 | hết tuần 8 | Phần lõi + kết quả định lượng trung gian |
| 4 · Experiments | 9–11 | hết tuần 11 | Thực nghiệm chính, bảng/hình chính |
| 5 · Analysis & Draft | 12–13 | hết tuần 13 | Phân tích + bản thảo đầy đủ |
| 6 · Reproducibility & Defense | 14–15 | hết tuần 15 | Chạy lại sạch, slides, demo, gói bàn giao |

*Ngày dương lịch tương ứng của khóa em nằm trong danh mục đề tài được phát và trong trang catalog.*

Trễ Gate 3 → **thu nhỏ đề tài**. Đây là cơ chế bảo vệ chất lượng, **không phải hình phạt** và không làm giảm điểm một cách tự động. Cái bị cắt là phần mở rộng, sweep tham số, số kiến trúc. Cái **không bao giờ** bị cắt: phần lõi, kiểm chứng, khả năng tái lập, và việc em phải hiểu sản phẩm của mình.

Sau tuần 11 không thêm thuật toán lớn mới — thời gian còn lại dành cho phân tích và viết.

## 6. Dùng AI thế nào cho đúng

**Được:** giải thích khái niệm, brainstorm từ khóa, gợi ý cấu trúc code/testbench, giả thuyết debug, viết lại câu chữ sau khi em đã hiểu nội dung, tạo checklist tự kiểm.

**Không được:** copy code/báo cáo mà không hiểu · tạo citation không kiểm chứng · bịa dữ liệu, hình, log, kết quả · dùng AI để che phần chưa làm.

Ghi lại vào `AI_USAGE_LOG.md`: dùng công cụ gì, để làm gì, và **em đã kiểm chứng phần đó bằng cách nào**.

Quy tắc gói lại trong một câu: **cannot explain = not completed.** Mentor có thể chỉ vào bất kỳ dòng code, công thức hay hình nào và hỏi "vì sao". Không giải thích được thì phần đó coi như chưa xong và em làm lại — không phải bị quy kết gian lận, mà là chưa đạt.

## 7. Cuối kỳ em nộp gì

Gói bàn giao (`LEGACY_PACKAGE_CHECKLIST.md`, 11 mục): README + hướng dẫn chạy lại · source code + config/môi trường ·
tests chạy pass · kết quả + hình + dữ liệu truy được về script · literature notes · `KNOWN_ISSUES.md` ·
`NEXT_STEPS.md` · báo cáo/slides bản cuối · `AI_USAGE_LOG.md` · một người khác chạy lại được · em giải thích được.

Gói này để khóa sau kế thừa, không phải làm lại từ đầu. Đồ án của em trở thành điểm xuất phát của người tiếp theo.

## 8. Trách nhiệm hai bên

**Mentor chịu trách nhiệm:** hướng kỹ thuật, phạm vi, chuẩn chất lượng, milestone, phản biện, điều chỉnh scope khi cần.

**Sinh viên chịu trách nhiệm:** đọc, học, code, debug, thí nghiệm, deadline, tài liệu, trình bày.

Mentor **không** làm thay phần thực thi. Nếu em thấy mình đang chờ mentor gỡ hộ một lỗi hàng tuần, đó là tín hiệu cần báo sớm — không phải chờ tới cuối kỳ.

---

*Chi tiết chính sách: `01_Governance/Master_Mentoring_Handbook.docx` và `AI_and_Academic_Integrity_Policy.docx`.
Danh mục đề tài và phiếu đăng ký: xem bản phát hành kèm thông báo.*
