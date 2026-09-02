# Nhóm A2 — Số học số và phần cứng DSP

**Engineering & Research Mentoring Program (Lucero)** · ThS. Đinh Văn Nam (Mr. Lucero Dinh) — Khoa Điện–Điện tử, Trường Kỹ thuật, Đại học Phenikaa

> **File sinh tự động** từ `06_Data/research_packs.json` bằng `scripts/generate_research_packs.py`. Sửa tay sẽ bị ghi đè — muốn đổi nội dung thì sửa JSON rồi chạy lại script.

**Digital Arithmetic & DSP Hardware** · 9 đề tài

## Nền chung của cả nhóm

Mọi đề tài trong nhóm này đều đi qua bốn mục dưới đây. Trang của từng đề tài chỉ thêm
**sản phẩm riêng** mà đề tài đó phải làm ra.

**Phải đọc**

- fixed-point arithmetic
- overflow/rounding/saturation
- adder/multiplier/MAC/FIR architectures
- pipelining và PPA

**Phải hiểu**

- accuracy vs bit-width
- latency vs throughput
- resource sharing vs parallelism
- Pareto trade-off

**Phải dựng**

- golden numerical model
- parameterized RTL
- bit-exact tests
- FPGA/ASIC reports

**Thí nghiệm mặc định**

- bit-width sweep
- pipeline/architecture sweep
- numerical-error analysis
- resource/Fmax/area/timing/power comparison

**Câu hỏi mentor**

1. Metric accuracy là gì?
2. Pipeline tăng register nhưng lợi gì?
3. Hai architecture có functional equivalence không?
4. Điểm Pareto nào đáng chọn và vì sao?

**Bước đi tiếp:** A3/A4 → A2-R01 hoặc AB

## Danh sách đề tài

| Mã | Tên | Loại | Sàn | Sản phẩm phải làm ra |
|---|---|---|---|---|
| [`A2-P01`](A2-P01.md) | Thiết kế và so sánh các kiến trúc bộ cộng số | P | L1 | RTL nhiều architecture; functional tests; synthesis comparison |
| [`A2-P02`](A2-P02.md) | Thiết kế multiplier fixed-point | P | L1 | Reference model; RTL; overflow/truncation tests; synthesis |
| [`A2-P03`](A2-P03.md) | Thiết kế Multiply-Accumulate datapath | P | L1 | MAC RTL; pipeline tests; resource/timing report |
| [`A2-P04`](A2-P04.md) | Thiết kế bộ lọc FIR bằng RTL | P | L1 | Floating reference; RTL; fixed-point test; waveform |
| [`A2-I01`](A2-I01.md) | Thiết kế và triển khai datapath DSP fixed-point trên FPGA | I | L2 | Golden model; RTL; FPGA synthesis; resource/Fmax/latency; report |
| [`A2-T01`](A2-T01.md) | Thiết kế bộ lọc FIR fixed-point trên FPGA và khảo sát ASIC | T | L2 `A3` | Reference; quantization; RTL; FPGA results; ASIC synthesis/physical evidence; analysis |
| [`A2-T02`](A2-T02.md) | Thiết kế và tối ưu MAC datapath cho FPGA/ASIC | T | L2 `A9` | Multiple configurations; PPA/resource/timing; accuracy; report · 📘 hồ sơ sâu |
| [`A2-T03`](A2-T03.md) | Thiết kế và đánh giá PPA của các kiến trúc bộ cộng số học | T | L2 `A8` | RCA/CLA/carry-select/optional parallel-prefix; equivalence tests; synthesis/STA cùng const… |
| [`A2-R01`](A2-R01.md) | Hardware design-space exploration cho fixed-point datapath | R | L4 | Reproducible sweep; Pareto analysis; research report/paper-ready figures |

---

*[← Bản đồ 16 nhóm](../README.md)*
