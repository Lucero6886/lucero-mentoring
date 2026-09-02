# Kế hoạch thí nghiệm — B6-T02

**Engineering & Research Mentoring Program (Lucero)** · ThS. Đinh Văn Nam (Mr. Lucero Dinh) — Khoa Điện–Điện tử, Trường Kỹ thuật, Đại học Phenikaa

> **File sinh tự động** từ `06_Data/research_packs.json` bằng `scripts/generate_research_packs.py`. Sửa tay sẽ bị ghi đè — muốn đổi nội dung thì sửa JSON rồi chạy lại script.

**Đề tài:** Neural-assisted candidate ranking cho SC-Flip Polar decoder  
**English:** Lightweight Neural-Assisted Candidate Ranking for SC-Flip Polar Decoding  
**Tên đầy đủ khi đăng ký:** Xếp hạng ứng viên hỗ trợ mạng neural nhẹ cho bộ giải mã Polar SC-Flip  
**Mã đối chiếu gói gốc:** T13 · **Track D** — Giải mã Polar thích ứng / hỗ trợ neural

---

## Câu hỏi nghiên cứu

> Một learned lightweight ranking function có thể đưa true error lên top-k tốt hơn heuristic reliability và giảm average SC-Flip retries với overhead chấp nhận được hay không?

## Baseline

Sinh viên phải mô tả baseline cụ thể — phiên bản, cấu hình và **lý do baseline này là công bằng** — trước khi chạy bất kỳ thí nghiệm nào. Baseline yếu làm cho mọi con số phía sau mất giá trị.

## Danh mục thí nghiệm

- Top-1/3/5
- BLER
- average attempts
- model-size sweep
- feature ablation
- quantization
- operation/latency cost

## Bằng chứng cần sinh ra

- ranking table
- BLER curve
- attempt histogram
- ablation
- model complexity
- hardware-aware net saving estimate

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
