# Kế hoạch thí nghiệm — A4-T01

**Engineering & Research Mentoring Program (Lucero)** · ThS. Đinh Văn Nam (Mr. Lucero Dinh) — Khoa Điện–Điện tử, Trường Kỹ thuật, Đại học Phenikaa

> **File sinh tự động** từ `06_Data/research_packs.json` bằng `scripts/generate_research_packs.py`. Sửa tay sẽ bị ghi đè — muốn đổi nội dung thì sửa JSON rồi chạy lại script.

**Đề tài:** Thiết kế một Digital IP từ RTL đến GDSII  
**English:** Design and Evaluation of a Digital IP from RTL to GDSII  
**Tên đầy đủ khi đăng ký:** Thiết kế và đánh giá một IP số từ RTL đến GDSII sử dụng quy trình EDA mã nguồn mở  
**Mã đối chiếu gói gốc:** T01 · **Track A** — Thiết kế IC số mã nguồn mở

---

## Câu hỏi nghiên cứu

> Các lựa chọn kiến trúc và ràng buộc physical design ảnh hưởng như thế nào đến timing, area, power và khả năng đóng thiết kế của một IP số?

## Baseline

Sinh viên phải mô tả baseline cụ thể — phiên bản, cấu hình và **lý do baseline này là công bằng** — trước khi chạy bất kỳ thí nghiệm nào. Baseline yếu làm cho mọi con số phía sau mất giá trị.

## Danh mục thí nghiệm

- Baseline RTL→GDSII
- clock-period sweep
- core-utilization sweep
- architecture hoặc pipeline comparison
- re-run để kiểm tra reproducibility

## Bằng chứng cần sinh ra

- waveform/regression pass
- synthesis report
- STA report
- layout/GDS screenshot
- DRC/LVS summary
- CSV PPA sweep + scripts
- Pareto/summary plots

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
