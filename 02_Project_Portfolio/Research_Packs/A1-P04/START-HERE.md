# START HERE — A1-P04

**Engineering & Research Mentoring Program (Lucero)** · ThS. Đinh Văn Nam (Mr. Lucero Dinh) — Khoa Điện–Điện tử, Trường Kỹ thuật, Đại học Phenikaa

> **File sinh tự động** từ `06_Data/research_packs.json` bằng `scripts/generate_research_packs.py`. Sửa tay sẽ bị ghi đè — muốn đổi nội dung thì sửa JSON rồi chạy lại script.

**Đề tài:** Thiết kế UART transmitter/receiver bằng RTL  
**English:** RTL Design of a UART Transmitter/Receiver  
**Tên đầy đủ khi đăng ký:** Thiết kế và đánh giá kiến trúc UART tham số hóa có khả năng tái sử dụng cho hệ thống số trên FPGA  
**Mã đối chiếu gói gốc:** T04 · **Track B** — Kiến trúc phần cứng số

---

## Câu hỏi nghiên cứu

> Thiết kế UART tham số hóa có thể duy trì độ tin cậy như thế nào dưới clock mismatch, sampling uncertainty hoặc error injection với chi phí phần cứng thấp?

Đây là câu em phải trả lời được bằng **bằng chứng**, không phải bằng một bản cài đặt chạy được.

## Trước khi gõ dòng code đầu tiên — phải đọc

- UART framing
- baud-rate generation
- FSM
- synchronizers/metastability concepts
- oversampling
- error detection
- FPGA verification

Tài liệu cụ thể xem `09_References/READING-LIST.md`. Sau mỗi tài liệu, trả lời 10 câu trong `READING-QUESTIONS` ở cuối file này.

## Phải hiểu được (không nhìn tài liệu)

- TX/RX timing
- why async serial needs sampling strategy
- clock mismatch budget
- framing/parity errors
- synchronizer role
- functional vs robustness testing

## Phải dựng

- UART TX
- UART RX
- baud generator
- optional oversampling receiver
- error detector
- self-checking TB + FPGA demo

## Phải chạy thí nghiệm

- nominal loopback
- baud mismatch sweep
- sampling offset sweep
- error/noise injection
- oversampling-factor comparison
- resource/timing evaluation

## Bằng chứng bắt buộc nộp

- waveforms
- pass/fail robustness boundary
- BER/framing-error plots
- resource report
- FPGA demonstration

## Khi nào mới đủ điều kiện nghĩ tới một bài báo

Chỉ mở paper nếu có robustness study có hệ thống, comparison với kiến trúc/sampling baseline, quantitative boundary và insight; nếu không thì giữ ở training/engineering output.

Tiềm năng công bố mentor đánh giá cho đề tài này: **Thấp, trừ khi làm thêm khảo sát độ bền**. Đây là ước lượng ban đầu, không phải lời hứa — quyết định thật nằm ở Gate G7.

## Bốn câu mentor sẽ hỏi đi hỏi lại

1. Tại sao UART vẫn nhận được khi hai clock không giống hệt nhau?
2. Oversampling cải thiện gì và tốn gì?
3. Noise model có thực tế không?
4. Kết quả có vượt mức project thông thường để thành research chưa?

Nếu tuần nào em cũng trả lời được bốn câu này bằng bằng chứng của chính mình, đề tài đang đi đúng.

## Bốn quy tắc không thương lượng

1. Không có baseline thì không có phương pháp đề xuất.
2. Không có bằng chứng thì không có kết luận.
3. Không tái lập được thì đề tài chưa hoàn thành ở mức nghiên cứu.
4. Không so sánh công bằng thì không được tuyên bố trong bài báo.

## READING-QUESTIONS — trả lời sau mỗi tài liệu

1. Bài này giải quyết vấn đề gì?
2. Baseline của họ là gì?
3. Giả định nào là quan trọng?
4. Họ dùng metric nào?
5. Kết quả chính là gì?
6. Giới hạn của bài là gì?
7. Phần nào tái lập được?
8. Phần nào liên quan trực tiếp tới câu hỏi nghiên cứu của em?
9. Có kết luận nào cần kiểm chứng độc lập không?
10. Nếu chỉ lấy được một insight cho đề tài, đó là gì?

---

*Lộ trình từng tuần: `ROADMAP.md` · Điều kiện qua từng cửa: `MILESTONE-GATES.md` · Thí nghiệm: `EXPERIMENTS.md`*
