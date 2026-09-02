# Kế hoạch thí nghiệm — B3-T02

**Engineering & Research Mentoring Program (Lucero)** · ThS. Đinh Văn Nam (Mr. Lucero Dinh) — Khoa Điện–Điện tử, Trường Kỹ thuật, Đại học Phenikaa

> **File sinh tự động** từ `06_Data/research_packs.json` bằng `scripts/generate_research_packs.py`. Sửa tay sẽ bị ghi đè — muốn đổi nội dung thì sửa JSON rồi chạy lại script.

**Đề tài:** Tối ưu fixed-point cho SC Polar decoder  
**English:** Fixed-Point Optimization of an SC Polar Decoder  
**Tên đầy đủ khi đăng ký:** Tối ưu biểu diễn fixed-point cho bộ giải mã Polar Successive Cancellation theo ràng buộc phần cứng  
**Mã đối chiếu gói gốc:** T06 · **Track C** — Kiến trúc bộ giải mã Polar

---

## Câu hỏi nghiên cứu

> Có thể giảm precision của LLR/processing trong SC decoder tới mức nào mà BLER degradation nhỏ trong khi hardware cost giảm đáng kể?

## Baseline

Sinh viên phải mô tả baseline cụ thể — phiên bản, cấu hình và **lý do baseline này là công bằng** — trước khi chạy bất kỳ thí nghiệm nào. Baseline yếu làm cho mọi con số phía sau mất giá trị.

## Danh mục thí nghiệm

- total-bit sweep
- fractional/integer split sweep
- rounding/saturation study
- BLER vs Eb/N0
- resource/fmax/power vs precision

## Bằng chứng cần sinh ra

- floating vs fixed BLER curves
- quantization error diagnostics
- bit-exact logs
- hardware cost table
- accuracy–cost Pareto plot

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
