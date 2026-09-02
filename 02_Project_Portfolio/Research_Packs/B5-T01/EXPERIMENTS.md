# Kế hoạch thí nghiệm — B5-T01

**Engineering & Research Mentoring Program (Lucero)** · ThS. Đinh Văn Nam (Mr. Lucero Dinh) — Khoa Điện–Điện tử, Trường Kỹ thuật, Đại học Phenikaa

> **File sinh tự động** từ `06_Data/research_packs.json` bằng `scripts/generate_research_packs.py`. Sửa tay sẽ bị ghi đè — muốn đổi nội dung thì sửa JSON rồi chạy lại script.

**Đề tài:** Phát hiện frame không tin cậy cho adaptive Polar decoding  
**English:** Unreliable-Frame Detection for Adaptive Polar Decoding  
**Tên đầy đủ khi đăng ký:** Phát hiện frame không tin cậy cho giải mã Polar thích ứng dựa trên đặc trưng độ tin cậy  
**Mã đối chiếu gói gốc:** T09 · **Track D** — Giải mã Polar thích ứng / hỗ trợ neural

---

## Câu hỏi nghiên cứu

> Có thể nhận biết sớm frame SC có nguy cơ sai bằng một detector độ phức tạp thấp để tránh kích hoạt enhanced decoding trên mọi frame hay không?

## Baseline

Sinh viên phải mô tả baseline cụ thể — phiên bản, cấu hình và **lý do baseline này là công bằng** — trước khi chạy bất kỳ thí nghiệm nào. Baseline yếu làm cho mọi con số phía sau mất giá trị.

## Danh mục thí nghiệm

- feature distribution correct vs error frames
- ROC/PR
- threshold sweep
- activation rate vs miss rate
- end-to-end BLER when coupled to oracle/enhanced path

## Bằng chứng cần sinh ra

- dataset manifest
- feature histograms
- ROC/PR plots
- confusion matrix
- activation/BLER trade-off

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
