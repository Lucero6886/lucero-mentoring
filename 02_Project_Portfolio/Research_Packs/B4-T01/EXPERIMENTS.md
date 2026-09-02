# Kế hoạch thí nghiệm — B4-T01

**Engineering & Research Mentoring Program (Lucero)** · ThS. Đinh Văn Nam (Mr. Lucero Dinh) — Khoa Điện–Điện tử, Trường Kỹ thuật, Đại học Phenikaa

> **File sinh tự động** từ `06_Data/research_packs.json` bằng `scripts/generate_research_packs.py`. Sửa tay sẽ bị ghi đè — muốn đổi nội dung thì sửa JSON rồi chạy lại script.

**Đề tài:** Thiết kế và đánh giá SC-Flip Polar decoder  
**English:** Design and Performance Evaluation of SC-Flip Polar Decoding  
**Tên đầy đủ khi đăng ký:** Thiết kế và đánh giá bộ giải mã Polar SC-Flip hướng đến triển khai phần cứng  
**Mã đối chiếu gói gốc:** T07 · **Track C** — Kiến trúc bộ giải mã Polar

---

## Câu hỏi nghiên cứu

> SC-Flip cải thiện BLER của SC với trade-off average/worst-case latency và complexity như thế nào khi hướng tới phần cứng?

## Baseline

Sinh viên phải mô tả baseline cụ thể — phiên bản, cấu hình và **lý do baseline này là công bằng** — trước khi chạy bất kỳ thí nghiệm nào. Baseline yếu làm cho mọi con số phía sau mất giá trị.

## Danh mục thí nghiệm

- BLER vs SNR
- Tmax sweep
- average attempts vs SNR
- latency distribution
- comparison SC/SCF/strong baseline where feasible

## Bằng chứng cần sinh ra

- BLER curves
- attempt histogram
- average/worst latency table
- candidate-hit diagnostics
- complexity accounting

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
