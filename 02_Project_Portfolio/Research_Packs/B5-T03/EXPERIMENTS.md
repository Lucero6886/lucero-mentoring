# Kế hoạch thí nghiệm — B5-T03

**Engineering & Research Mentoring Program (Lucero)** · ThS. Đinh Văn Nam (Mr. Lucero Dinh) — Khoa Điện–Điện tử, Trường Kỹ thuật, Đại học Phenikaa

> **File sinh tự động** từ `06_Data/research_packs.json` bằng `scripts/generate_research_packs.py`. Sửa tay sẽ bị ghi đè — muốn đổi nội dung thì sửa JSON rồi chạy lại script.

**Đề tài:** Đồng thiết kế thuật toán - phần cứng cho bộ giải mã Polar thích ứng  
**English:** Algorithm-Hardware Co-Design of an Adaptive Polar Decoder  
**Tên đầy đủ khi đăng ký:** Đồng thiết kế thuật toán–phần cứng cho bộ giải mã Polar thích ứng trên FPGA  
**Mã đối chiếu gói gốc:** T11 · **Track D** — Giải mã Polar thích ứng / hỗ trợ neural

---

## Câu hỏi nghiên cứu

> Làm thế nào ánh xạ adaptive Polar decoding thành kiến trúc phần cứng để lợi thế average-case của thuật toán vẫn tồn tại sau fixed-point, control, memory và interface overhead?

## Baseline

Sinh viên phải mô tả baseline cụ thể — phiên bản, cấu hình và **lý do baseline này là công bằng** — trước khi chạy bất kỳ thí nghiệm nào. Baseline yếu làm cho mọi con số phía sau mất giá trị.

## Danh mục thí nghiệm

- bit-exact verification
- resource-sharing alternatives
- fmax/latency/throughput
- activation-dependent average latency
- power/energy estimate
- ASIC-feasibility synthesis if available

## Bằng chứng cần sinh ra

- architecture diagram
- bit-exact logs
- resource/timing reports
- average/worst latency
- power/energy table
- comparison with non-adaptive hardware baseline

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
