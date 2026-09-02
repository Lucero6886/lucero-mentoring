# Nhóm A3 — Thiết kế hệ thống trên FPGA

**Engineering & Research Mentoring Program (Lucero)** · ThS. Đinh Văn Nam (Mr. Lucero Dinh) — Khoa Điện–Điện tử, Trường Kỹ thuật, Đại học Phenikaa

> **File sinh tự động** từ `06_Data/research_packs.json` bằng `scripts/generate_research_packs.py`. Sửa tay sẽ bị ghi đè — muốn đổi nội dung thì sửa JSON rồi chạy lại script.

**FPGA System Design** · 6 đề tài

## Nền chung của cả nhóm

Mọi đề tài trong nhóm này đều đi qua bốn mục dưới đây. Trang của từng đề tài chỉ thêm
**sản phẩm riêng** mà đề tài đó phải làm ra.

**Phải đọc**

- FPGA synthesis/place-route flow
- clock constraints
- I/O interfacing
- on-board debug

**Phải hiểu**

- Fmax/resource/latency/throughput
- timing constraint và critical path
- simulation vs hardware behavior
- interface synchronization

**Phải dựng**

- FPGA project/constraints
- RTL integration
- hardware test harness
- measurement/report

**Thí nghiệm mặc định**

- resource/Fmax baseline
- clock or pipeline sweep
- peripheral stress test
- hardware/software agreement

**Câu hỏi mentor**

1. Timing closure nghĩa là gì ở thiết kế này?
2. Kết quả trên board có bằng chứng gì ngoài demo?
3. Bottleneck là logic, memory hay I/O?
4. Metric nào đủ để so architecture?

**Bước đi tiếp:** A4/A5 → A4-R01/AB

## Danh sách đề tài

| Mã | Tên | Loại | Sàn | Sản phẩm phải làm ra |
|---|---|---|---|---|
| [`A3-P01`](A3-P01.md) | Triển khai một Digital IP trên FPGA | P | L1 | Bitstream/project; hardware demo; resource/Fmax; README |
| [`A3-P02`](A3-P02.md) | FPGA interfacing với peripheral | P | L1 | Interface RTL; board demo; tests; documentation |
| [`A3-P03`](A3-P03.md) | Hệ thống xử lý tín hiệu số trên FPGA | P | L2 | Working DSP pipeline; resource/timing; hardware test |
| [`A3-I01`](A3-I01.md) | Xây dựng hệ thống FPGA tích hợp nhiều IP | I | L2 | Integrated system; interface tests; demo; documentation |
| [`A3-T01`](A3-T01.md) | Thiết kế hệ thống xử lý dữ liệu số pipelined trên FPGA | T | L2 `A5` | Architecture; RTL; verification; FPGA; LUT/FF/DSP/Fmax/latency/throughput analysis |
| [`A3-T02`](A3-T02.md) | Hardware/software co-verification cho hệ thống FPGA | T | L2 | Golden model; vector generation; RTL/FPGA agreement; automated comparison; report |

---

*[← Bản đồ 16 nhóm](../README.md)*
