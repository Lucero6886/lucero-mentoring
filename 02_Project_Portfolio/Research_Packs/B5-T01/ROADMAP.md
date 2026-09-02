# Lộ trình theo tuần — B5-T01

**Engineering & Research Mentoring Program (Lucero)** · ThS. Đinh Văn Nam (Mr. Lucero Dinh) — Khoa Điện–Điện tử, Trường Kỹ thuật, Đại học Phenikaa

> **File sinh tự động** từ `06_Data/research_packs.json` bằng `scripts/generate_research_packs.py`. Sửa tay sẽ bị ghi đè — muốn đổi nội dung thì sửa JSON rồi chạy lại script.

**Đề tài:** Phát hiện frame không tin cậy cho adaptive Polar decoding  
**English:** Unreliable-Frame Detection for Adaptive Polar Decoding  
**Tên đầy đủ khi đăng ký:** Phát hiện frame không tin cậy cho giải mã Polar thích ứng dựa trên đặc trưng độ tin cậy  
**Mã đối chiếu gói gốc:** T09 · **Track D** — Giải mã Polar thích ứng / hỗ trợ neural

---

Mọi mốc dưới đây tính theo **số tuần kể từ ngày sinh viên chính thức nhận đề tài** — khung này dùng chung cho mọi khóa, không gắn với một học kỳ cụ thể. Khóa hiện tại bắt đầu **07/09/2026**, nên tuần 1 là 07/09/2026–13/09/2026 và ngày tương ứng của từng mốc được ghi kèm.

> Được phép kéo dài một mốc, **không được bỏ một cửa nào**. Mọi buổi review bắt đầu từ bằng chứng, không từ lời kể.

| Tuần | Mốc | Sinh viên làm | Nộp bằng chứng | Mentor hỏi | Điều kiện qua |
|---:|---|---|---|---|---|
| 1 | Nhận đề tài · nền khái niệm | Đọc START-HERE, chốt phạm vi, kiểm tra tiên quyết, dựng môi trường; tự viết glossary. | Sơ đồ vấn đề một trang + glossary + trả lời câu hỏi sẵn sàng. | Giải thích đề tài trong 2 phút, không slide, không AI: đầu vào, đầu ra, baseline, metric là gì? Label có leakage không? | G0 đạt. |
| 2 | Tài liệu · câu hỏi nghiên cứu | Hoàn thành bảng so sánh tài liệu; phát biểu vấn đề, câu hỏi nghiên cứu, giả thuyết, phạm vi và non-goals. | Literature matrix 8–15 nguồn + problem statement + RQ. | Bài nào gần câu hỏi của em nhất? Khoảng trống nào là thật, khoảng trống nào chỉ là chưa ai cài đặt? | **Gate 1 đạt** (G0 + G1). <br>_hạn 20/09/2026_ |
| 3 | Thiết kế baseline | Chốt baseline, đầu vào/đầu ra, metric và giao thức thí nghiệm. | Baseline spec + test plan. | Baseline này đã đủ mạnh và công bằng chưa? Feature này có sẵn trước khi quyết định activate không? | Mentor duyệt tính công bằng của baseline. |
| 4 | Cài đặt baseline | Cài đặt hoặc chuẩn hóa baseline; viết unit test cho phần dễ sai nhất. | Code + test chạy xanh. | Unit test nào có thể bắt được lỗi logic nguy hiểm nhất? | Các unit test cốt lõi đều qua. |
| 5 | Baseline chạy đầu-cuối · kiểm chứng | Chạy đầu-cuối, sanity check, đối chiếu với vector đã biết hoặc tài liệu. | Log baseline + hình đầu tiên + ghi chú kiểm chứng. | Nếu baseline lệch tài liệu, em đã loại trừ những nguyên nhân nào? Kiểm chứng độc lập nào cho thấy cài đặt đúng chứ không chỉ tự nhất quán? | **Gate 2 đạt** (G2). Chưa đạt thì không mở phần mở rộng nghiên cứu. <br>_hạn 11/10/2026_ |
| 6 | Phương pháp đề xuất v1 | Cài đặt kiến trúc hoặc phương pháp cần khảo sát. | Block diagram/pseudocode + code v1. | Phương pháp mới thay đổi đúng **một** cơ chế nào so với baseline? | G3 một phần. |
| 7 | Hoàn thiện · trường hợp biên | Hoàn thiện cài đặt, xử lý trường hợp biên. | Kết quả regression. | Trường hợp biên nào có thể làm hỏng thiết kế này? | Regression không phá baseline. |
| 8 | Chốt phương pháp đề xuất | Đóng băng phiên bản đem đi đo; ghi rõ chi phí phát sinh so với baseline. | Bản v2 + bảng so sánh chi phí. | Chi phí mới sinh ra ở đâu? False negative gây hậu quả gì? | **Gate 3 đạt** (G3). <br>_hạn 01/11/2026_ |
| 9 | Khóa ma trận thí nghiệm | Khóa biến độc lập, biến kiểm soát, metric, số seed/mẫu/frame **trước khi chạy**. | EXPERIMENT-PLAN với Experiment ID. | Thí nghiệm này trả lời đúng một câu hỏi nghiên cứu nào? Biến nào bắt buộc giữ cố định? | Mentor duyệt giao thức. |
| 10 | Thí nghiệm chính · đợt 1 | Chạy sweep/thí nghiệm chính; lưu kết quả thô, không ghi đè. | Kết quả thô + log + config. | Kết quả hiện tại có thể do yếu tố gây nhiễu nào thay vì do phương pháp đề xuất? | Không chọn lọc kết quả; chạy lại được. |
| 11 | Sensitivity · chiều thứ hai | Chạy chiều biến thứ hai hoặc khảo sát độ nhạy. | Kết quả thô + kết quả đã xử lý. | Xu hướng có ổn định khi đổi seed, SNR, config hoặc kích thước không? | **Gate 4 đạt** (G4). Sau tuần này không thêm thuật toán lớn mới. <br>_hạn 22/11/2026_ |
| 12 | Phân tích · failure case | Giải thích xu hướng bằng nguyên nhân; tìm và mô tả failure case. | 2–4 hình/bảng + phân tích. | Failure case quan trọng nhất là gì? Operating point nào tối ưu cho decoder chứ không chỉ classifier? | G5 đạt. |
| 13 | Bản thảo · phát biểu đóng góp | Viết kết luận, đóng góp và giới hạn; mỗi kết luận trỏ tới một hình/bảng/log. | Bản thảo báo cáo/khóa luận + ghi chú nghiên cứu 2 trang. | Nếu chỉ được giữ một kết luận, kết luận nào có bằng chứng mạnh nhất? | **Gate 5 đạt**. <br>_hạn 06/12/2026_ |
| 14 | Tái lập | Clone sạch và chạy lại từ README; script tạo lại hình chính; tách kết quả thô/đã xử lý. | Checklist tái lập + script sinh hình. | Người khác có thể clone và tạo lại hình chính mà không hỏi em không? | G6 đạt. |
| 15 | Bảo vệ · bàn giao · chuyển giao giảng dạy | Dọn repository, chuẩn bị slide/demo, viết Teaching Transfer Note, bàn giao cho khóa sau. | Repo cuối + slide + teaching note. | Điều gì của đề tài này nên trở thành tài sản dùng lại cho khóa sau và cho bài giảng? | **Gate 6 đạt** — kết thúc đề tài. <br>_hạn 20/12/2026_ |

## Sau tuần 15 — cửa mở rộng G7

Chỉ mở khi đề tài có tiềm năng công bố và mentor đồng ý. Xem `PAPER-READINESS.md`.

## Quy tắc dừng

- Gate 2 chưa đạt thì không chuyển sang phương pháp đề xuất.
- Giả thuyết sai thì ghi nhận là kết quả — không uốn dữ liệu để cứu giả thuyết.
- Phương pháp đề xuất không tạo lợi ích ròng thì cân nhắc đổi hướng hoặc dừng, thay vì cố viết bài.
- Sinh viên không giải thích được đoạn code do AI sinh ra thì mốc tuần đó không đạt.
