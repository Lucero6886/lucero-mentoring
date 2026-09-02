# Kế hoạch thí nghiệm — A2-T02

**Engineering & Research Mentoring Program (Lucero)** · ThS. Đinh Văn Nam (Mr. Lucero Dinh) — Khoa Điện–Điện tử, Trường Kỹ thuật, Đại học Phenikaa

> **File sinh tự động** từ `06_Data/research_packs.json` bằng `scripts/generate_research_packs.py`. Sửa tay sẽ bị ghi đè — muốn đổi nội dung thì sửa JSON rồi chạy lại script.

**Đề tài:** Thiết kế và tối ưu MAC datapath cho FPGA/ASIC  
**English:** Design and Optimization of a Fixed-Point MAC Datapath for FPGA/ASIC  
**Tên đầy đủ khi đăng ký:** Thiết kế MAC datapath và đánh giá ảnh hưởng của bit-width và pipeline đến độ chính xác và chi phí phần cứng  
**Mã đối chiếu gói gốc:** T03 · **Track B** — Kiến trúc phần cứng số

---

## Câu hỏi nghiên cứu

> Bit-width và mức pipeline thay đổi numerical accuracy, latency, throughput, area và power của MAC datapath như thế nào?

## Baseline

Sinh viên phải mô tả baseline cụ thể — phiên bản, cấu hình và **lý do baseline này là công bằng** — trước khi chạy bất kỳ thí nghiệm nào. Baseline yếu làm cho mọi con số phía sau mất giá trị.

## Danh mục thí nghiệm

- bit-width sweep
- fractional-bit allocation
- pipeline-depth sweep
- rounding/saturation comparison
- FPGA/ASIC resource/timing evaluation

## Bằng chứng cần sinh ra

- numerical error plots
- RTL-vs-golden equivalence results
- LUT/FF or area reports
- fmax/latency/throughput table
- Pareto plot

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
