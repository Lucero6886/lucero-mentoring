# Kế hoạch thí nghiệm — A1-P04

**Engineering & Research Mentoring Program (Lucero)** · ThS. Đinh Văn Nam (Mr. Lucero Dinh) — Khoa Điện–Điện tử, Trường Kỹ thuật, Đại học Phenikaa

> **File sinh tự động** từ `06_Data/research_packs.json` bằng `scripts/generate_research_packs.py`. Sửa tay sẽ bị ghi đè — muốn đổi nội dung thì sửa JSON rồi chạy lại script.

**Đề tài:** Thiết kế UART transmitter/receiver bằng RTL  
**English:** RTL Design of a UART Transmitter/Receiver  
**Tên đầy đủ khi đăng ký:** Thiết kế và đánh giá kiến trúc UART tham số hóa có khả năng tái sử dụng cho hệ thống số trên FPGA  
**Mã đối chiếu gói gốc:** T04 · **Track B** — Kiến trúc phần cứng số

---

## Câu hỏi nghiên cứu

> Thiết kế UART tham số hóa có thể duy trì độ tin cậy như thế nào dưới clock mismatch, sampling uncertainty hoặc error injection với chi phí phần cứng thấp?

## Baseline

Sinh viên phải mô tả baseline cụ thể — phiên bản, cấu hình và **lý do baseline này là công bằng** — trước khi chạy bất kỳ thí nghiệm nào. Baseline yếu làm cho mọi con số phía sau mất giá trị.

## Danh mục thí nghiệm

- nominal loopback
- baud mismatch sweep
- sampling offset sweep
- error/noise injection
- oversampling-factor comparison
- resource/timing evaluation

## Bằng chứng cần sinh ra

- waveforms
- pass/fail robustness boundary
- BER/framing-error plots
- resource report
- FPGA demonstration

## Trước mỗi thí nghiệm — bảy bước bắt buộc

1. Viết giả thuyết.
2. Xác định biến độc lập.
3. Khóa biến kiểm soát.
4. Chốt metric.
5. Chốt số mẫu / frame / seed.
6. Đặt Experiment ID.
7. Không đổi giao thức sau khi đã thấy kết quả — nếu buộc phải đổi thì ghi rõ lý do vào nhật ký.

## Sau mỗi thí nghiệm — năm mục bắt buộc

- **Quan sát** — con số nói gì.
- **Diễn giải** — vì sao lại thế.
- **Cách giải thích khác** — điều gì khác cũng tạo ra kết quả này.
- **Failure case** — chỗ nào không hoạt động.
- **Thí nghiệm tiếp theo** — và nó trả lời câu hỏi nào.

Mẫu ghi chép: `04_Project_Template/EXPERIMENT_LOG_TEMPLATE.md`.
