# Kế hoạch thí nghiệm — B5-T02

**Engineering & Research Mentoring Program (Lucero)** · ThS. Đinh Văn Nam (Mr. Lucero Dinh) — Khoa Điện–Điện tử, Trường Kỹ thuật, Đại học Phenikaa

> **File sinh tự động** từ `06_Data/research_packs.json` bằng `scripts/generate_research_packs.py`. Sửa tay sẽ bị ghi đè — muốn đổi nội dung thì sửa JSON rồi chạy lại script.

**Đề tài:** Adaptive decoder chỉ kích hoạt enhanced processing trên frame khó  
**English:** Adaptive Polar Decoding with Selective Enhanced Processing  
**Tên đầy đủ khi đăng ký:** Thiết kế bộ giải mã Polar thích ứng dựa trên độ tin cậy với cơ chế xử lý tăng cường có chọn lọc  
**Mã đối chiếu gói gốc:** T10 · **Track D** — Giải mã Polar thích ứng / hỗ trợ neural

---

## Câu hỏi nghiên cứu

> Selective enhanced processing có thể đạt BLER gần always-on enhanced decoder nhưng giảm average latency/operations/energy trên các frame dễ hay không?

## Baseline

Sinh viên phải mô tả baseline cụ thể — phiên bản, cấu hình và **lý do baseline này là công bằng** — trước khi chạy bất kỳ thí nghiệm nào. Baseline yếu làm cho mọi con số phía sau mất giá trị.

## Danh mục thí nghiệm

- BLER vs SNR
- activation rate vs SNR
- average operations/latency
- threshold sensitivity
- oracle gate upper bound
- always-on enhanced comparison

## Bằng chứng cần sinh ra

- BLER plot
- activation plot
- average-cost table
- threshold Pareto curve
- failure/missed-hard-frame analysis

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
