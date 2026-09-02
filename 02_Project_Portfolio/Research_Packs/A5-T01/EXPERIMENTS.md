# Kế hoạch thí nghiệm — A5-T01

**Engineering & Research Mentoring Program (Lucero)** · ThS. Đinh Văn Nam (Mr. Lucero Dinh) — Khoa Điện–Điện tử, Trường Kỹ thuật, Đại học Phenikaa

> **File sinh tự động** từ `06_Data/research_packs.json` bằng `scripts/generate_research_packs.py`. Sửa tay sẽ bị ghi đè — muốn đổi nội dung thì sửa JSON rồi chạy lại script.

**Đề tài:** Xây dựng quy trình ASIC tái lập sử dụng LibreLane + Nix  
**English:** Reproducible ASIC Workflow Using LibreLane and Nix  
**Tên đầy đủ khi đăng ký:** Xây dựng và đánh giá quy trình RTL-to-GDSII mã nguồn mở có khả năng tái lập phục vụ đào tạo thiết kế vi mạch số  
**Mã đối chiếu gói gốc:** T02 · **Track A** — Thiết kế IC số mã nguồn mở

---

## Câu hỏi nghiên cứu

> Làm thế nào xây dựng một RTL-to-GDSII environment mà người học khác có thể tái lập kết quả một cách ổn định trên các máy/môi trường khác nhau?

## Baseline

Sinh viên phải mô tả baseline cụ thể — phiên bản, cấu hình và **lý do baseline này là công bằng** — trước khi chạy bất kỳ thí nghiệm nào. Baseline yếu làm cho mọi con số phía sau mất giá trị.

## Danh mục thí nghiệm

- Fresh install test
- multi-machine or multi-environment rerun
- version/config sensitivity
- benchmark suite run
- runtime + PPA consistency

## Bằng chứng cần sinh ra

- setup time log
- success/failure matrix
- version manifest
- PPA/run-time variance
- clean-clone demonstration
- student reproduction checklist

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
