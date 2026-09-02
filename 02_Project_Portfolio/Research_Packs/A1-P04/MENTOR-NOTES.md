# Ghi chú cho mentor — A1-P04

**Engineering & Research Mentoring Program (Lucero)** · ThS. Đinh Văn Nam (Mr. Lucero Dinh) — Khoa Điện–Điện tử, Trường Kỹ thuật, Đại học Phenikaa

> **File sinh tự động** từ `06_Data/research_packs.json` bằng `scripts/generate_research_packs.py`. Sửa tay sẽ bị ghi đè — muốn đổi nội dung thì sửa JSON rồi chạy lại script.

**Đề tài:** Thiết kế UART transmitter/receiver bằng RTL  
**English:** RTL Design of a UART Transmitter/Receiver  
**Tên đầy đủ khi đăng ký:** Thiết kế và đánh giá kiến trúc UART tham số hóa có khả năng tái sử dụng cho hệ thống số trên FPGA  
**Mã đối chiếu gói gốc:** T04 · **Track B** — Kiến trúc phần cứng số

---

## Câu hỏi nghiên cứu

> Thiết kế UART tham số hóa có thể duy trì độ tin cậy như thế nào dưới clock mismatch, sampling uncertainty hoặc error injection với chi phí phần cứng thấp?

## Bốn câu hỏi trọng tâm

1. Tại sao UART vẫn nhận được khi hai clock không giống hệt nhau?
2. Oversampling cải thiện gì và tốn gì?
3. Noise model có thực tế không?
4. Kết quả có vượt mức project thông thường để thành research chưa?

## Ngưỡng công bố

Chỉ mở paper nếu có robustness study có hệ thống, comparison với kiến trúc/sampling baseline, quantitative boundary và insight; nếu không thì giữ ở training/engineering output.

**Tiềm năng đánh giá ban đầu:** Thấp, trừ khi làm thêm khảo sát độ bền

## Phụ thuộc

Không phụ thuộc đề tài nào — có thể mở ngay.

## Cảnh báo sớm

- Sinh viên chạy proposed trước baseline.
- Chỉ đưa screenshot mà không có raw data/config.
- Metric thay đổi giữa các phương pháp.
- Kết luận dựa vào 1 run/1 SNR/1 seed khi bài toán cần thống kê.
- AI-generated code nhưng sinh viên không giải thích được.
- Không phân biệt implementation result với research contribution.

## Sau mỗi mốc

Ghi lại vào `04_Project_Template/MENTOR_LESSONS_LEARNED.md`: sinh viên hiểu sai chỗ nào, thiếu kiến thức tiên quyết nào, cách giải thích nào có tác dụng, thí nghiệm nào gây hiểu nhầm, tài liệu nào tốt nhất, và lần sau nên đổi gì.

## Checklist tuần

`03_Operations/MENTOR_WEEKLY_CHECKLIST.md` · Thang chấm: `03_Operations/PASS_FAIL_RUBRIC.md`
