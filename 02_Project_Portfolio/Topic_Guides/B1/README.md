# Nhóm B1 — Khối phần cứng cho Polar

**Engineering & Research Mentoring Program (Lucero)** · ThS. Đinh Văn Nam (Mr. Lucero Dinh) — Khoa Điện–Điện tử, Trường Kỹ thuật, Đại học Phenikaa

> **File sinh tự động** từ `06_Data/research_packs.json` bằng `scripts/generate_research_packs.py`. Sửa tay sẽ bị ghi đè — muốn đổi nội dung thì sửa JSON rồi chạy lại script.

**Polar Hardware Building Blocks** · 7 đề tài

## Nền chung của cả nhóm

Mọi đề tài trong nhóm này đều đi qua bốn mục dưới đây. Trang của từng đề tài chỉ thêm
**sản phẩm riêng** mà đề tài đó phải làm ra.

**Phải đọc**

- SC f/g operations
- partial sums
- fixed-point basics
- RTL microarchitecture
- co-verification

**Phải hiểu**

- algorithm operation→hardware cycle
- exact/min-sum differences
- bit growth
- module interface dependencies

**Phải dựng**

- reference function
- RTL PE/unit
- self-checking TB
- synthesis/FPGA evidence

**Thí nghiệm mặc định**

- exhaustive/random vector tests
- bit-width sweep
- exact vs approximation
- resource/timing

**Câu hỏi mentor**

1. PE này thực hiện công thức nào?
2. Mismatch do sign/scale hay control?
3. Approximation ảnh hưởng BLER thế nào?
4. Bit-width nào là đủ?

**Bước đi tiếp:** B2 → B3/AB

## Danh sách đề tài

| Mã | Tên | Loại | Sàn | Sản phẩm phải làm ra |
|---|---|---|---|---|
| [`B1-P01`](B1-P01.md) | Thiết kế Polar Encoder RTL | P | L1 | RTL encoder; golden vectors; testbench; synthesis |
| [`B1-P02`](B1-P02.md) | Thiết kế f Processing Element | P | L1 | Reference f; RTL; exhaustive/random tests; synthesis |
| [`B1-P03`](B1-P03.md) | Thiết kế g Processing Element | P | L1 | Reference g; RTL; tests; synthesis |
| [`B1-P04`](B1-P04.md) | Thiết kế Partial-Sum Unit | P | L2 | Architecture; RTL; tests; synthesis |
| [`B1-I01`](B1-I01.md) | Thiết kế và kiểm chứng f/g Processing Elements trên FPGA | I | L2 | Golden co-verification; FPGA synthesis; resource/Fmax; report |
| [`B1-T01`](B1-T01.md) | Thiết kế Polar Encoder trên FPGA | T | L2 `B2` | Architecture; RTL; verification; FPGA; resource/Fmax/latency/throughput |
| [`B1-T02`](B1-T02.md) | Thiết kế và đánh giá f/g Processing Elements cho Polar Decoder | T | L2 `B5` | Exact/min-sum/reference; fixed-point RTL; timing/area/resource; BLER impact via model |

---

*[← Bản đồ 16 nhóm](../README.md)*
