# Kế hoạch thí nghiệm — B6-T01

**Engineering & Research Mentoring Program (Lucero)** · ThS. Đinh Văn Nam (Mr. Lucero Dinh) — Khoa Điện–Điện tử, Trường Kỹ thuật, Đại học Phenikaa

> **File sinh tự động** từ `06_Data/research_packs.json` bằng `scripts/generate_research_packs.py`. Sửa tay sẽ bị ghi đè — muốn đổi nội dung thì sửa JSON rồi chạy lại script.

**Đề tài:** Lightweight neural-assisted unreliable-frame detector  
**English:** Lightweight Neural-Assisted Unreliable-Frame Detector  
**Tên đầy đủ khi đăng ký:** Thiết kế bộ phát hiện frame không tin cậy hỗ trợ mạng neural nhẹ cho giải mã Polar thích ứng  
**Mã đối chiếu gói gốc:** T12 · **Track D** — Giải mã Polar thích ứng / hỗ trợ neural

---

## Câu hỏi nghiên cứu

> Một neural classifier rất nhỏ có thể cải thiện unreliable-frame detection đủ nhiều so với detector heuristic/statistical để justify phần cứng bổ sung hay không?

## Baseline

Sinh viên phải mô tả baseline cụ thể — phiên bản, cấu hình và **lý do baseline này là công bằng** — trước khi chạy bất kỳ thí nghiệm nào. Baseline yếu làm cho mọi con số phía sau mất giá trị.

## Danh mục thí nghiệm

- threshold vs logistic vs tiny MLP
- feature ablation
- model-size sweep
- quantization sweep
- ROC/PR
- end-to-end activation/BLER/average-cost

## Bằng chứng cần sinh ra

- split manifest
- learning curves
- ROC/PR
- ablation table
- parameter/MAC/memory table
- end-to-end adaptive-decoder benefit

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
