# Kế hoạch thí nghiệm — B4-T02

**Engineering & Research Mentoring Program (Lucero)** · ThS. Đinh Văn Nam (Mr. Lucero Dinh) — Khoa Điện–Điện tử, Trường Kỹ thuật, Đại học Phenikaa

> **File sinh tự động** từ `06_Data/research_packs.json` bằng `scripts/generate_research_packs.py`. Sửa tay sẽ bị ghi đè — muốn đổi nội dung thì sửa JSON rồi chạy lại script.

**Đề tài:** Reliability-based candidate ranking cho SC-Flip  
**English:** Reliability-Based Candidate Ranking for SC-Flip Polar Decoding  
**Tên đầy đủ khi đăng ký:** Nghiên cứu phương pháp xếp hạng ứng viên dựa trên độ tin cậy cho bộ giải mã Polar SC-Flip  
**Mã đối chiếu gói gốc:** T08 · **Track C** — Kiến trúc bộ giải mã Polar

---

## Câu hỏi nghiên cứu

> Có thể dùng thông tin độ tin cậy tốt hơn |LLR| đơn thuần để tăng xác suất đưa true error vào top-k candidate và giảm số lần SC-Flip retry hay không?

## Baseline

Sinh viên phải mô tả baseline cụ thể — phiên bản, cấu hình và **lý do baseline này là công bằng** — trước khi chạy bất kỳ thí nghiệm nào. Baseline yếu làm cho mọi con số phía sau mất giá trị.

## Danh mục thí nghiệm

- Top-1/3/5 hit rate
- BLER vs SNR
- average attempts
- metric complexity
- sensitivity to candidate pool/Tmax

## Bằng chứng cần sinh ra

- ranking accuracy table
- BLER curves
- attempt reduction
- failure examples
- operation-count/hardware-cost estimate

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
