# Nhóm B3 — Lượng tử hóa và tối ưu theo phần cứng

**Engineering & Research Mentoring Program (Lucero)** · ThS. Đinh Văn Nam (Mr. Lucero Dinh) — Khoa Điện–Điện tử, Trường Kỹ thuật, Đại học Phenikaa

> **File sinh tự động** từ `06_Data/research_packs.json` bằng `scripts/generate_research_packs.py`. Sửa tay sẽ bị ghi đè — muốn đổi nội dung thì sửa JSON rồi chạy lại script.

**Hardware-Aware Quantization & Optimization** · 5 đề tài

## Nền chung của cả nhóm

Mọi đề tài trong nhóm này đều đi qua bốn mục dưới đây. Trang của từng đề tài chỉ thêm
**sản phẩm riêng** mà đề tài đó phải làm ra.

**Phải đọc**

- LLR dynamic range
- quantization
- saturation/clipping
- fixed-point Polar decoding
- hardware cost metrics

**Phải hiểu**

- quantization error propagation
- BLER sensitivity
- integer/fractional allocation
- accuracy-cost Pareto

**Phải dựng**

- floating baseline
- quantized model
- parameterized implementation
- hardware cost extraction

**Thí nghiệm mặc định**

- 3/4/5/6+ bit sweep
- clipping/saturation
- BLER vs Eb/N0
- resource/timing/energy proxy

**Câu hỏi mentor**

1. Overflow xảy ra ở đâu?
2. BLER loss tại SNR nào quan trọng?
3. Precision optimum ổn định theo N/K không?
4. Savings có đủ justify degradation không?

**Bước đi tiếp:** B4/B5/AB → B3-R01/AB-R01

## Danh sách đề tài

| Mã | Tên | Loại | Sàn | Sản phẩm phải làm ra |
|---|---|---|---|---|
| [`B3-P01`](B3-P01.md) | Khảo sát quantization của LLR | P | L1 | Floating vs 3/4/5/6-bit results; plots; explanation |
| [`B3-I01`](B3-I01.md) | Fixed-point implementation của Polar processing elements | I | L2 | Fixed-point reference; RTL/synthesizable model; error tests; resource |
| [`B3-T01`](B3-T01.md) | Phân tích lượng tử hóa LLR cho hardware-efficient Polar decoding | T | L3 `B4` | BLER/BER vs bit-width; complexity/hardware proxy; controlled analysis; thesis |
| [`B3-T02`](B3-T02.md) | Tối ưu fixed-point cho SC Polar decoder | T | L3 | LLR/intermediate widths; saturation/clipping; BLER; resource/timing estimates · 📘 hồ sơ sâu |
| [`B3-R01`](B3-R01.md) | Adaptive-precision Polar decoding | R | L4 | Baseline fixed precision; adaptation rule; BLER/average-cost analysis; reproducible experi… |

---

*[← Bản đồ 16 nhóm](../README.md)*
