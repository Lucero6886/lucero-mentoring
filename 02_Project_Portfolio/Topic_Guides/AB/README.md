# Nhóm AB — Vùng giao: IC số × Polar × Edge co-design

**Engineering & Research Mentoring Program (Lucero)** · ThS. Đinh Văn Nam (Mr. Lucero Dinh) — Khoa Điện–Điện tử, Trường Kỹ thuật, Đại học Phenikaa

> **File sinh tự động** từ `06_Data/research_packs.json` bằng `scripts/generate_research_packs.py`. Sửa tay sẽ bị ghi đè — muốn đổi nội dung thì sửa JSON rồi chạy lại script.

**Digital IC × Polar / Edge Co-Design** · 10 đề tài

## Nền chung của cả nhóm

Mọi đề tài trong nhóm này đều đi qua bốn mục dưới đây. Trang của từng đề tài chỉ thêm
**sản phẩm riêng** mà đề tài đó phải làm ra.

**Phải đọc**

- cross-platform benchmarking
- FPGA vs ASIC metrics
- energy/latency accounting
- algorithm-hardware co-design
- multi-objective optimization

**Phải hiểu**

- fair cross-platform comparison
- proxy vs measured energy
- algorithmic vs implementation gain
- Pareto dominance

**Phải dựng**

- shared golden workload
- FPGA/ASIC/SoC implementations or estimates
- automated metric extraction
- trade-off analysis

**Thí nghiệm mặc định**

- platform/architecture sweep
- bit-width/pipeline sweep
- BLER/accuracy vs PPA/energy
- multi-objective Pareto

**Câu hỏi mentor**

1. Comparison có cùng workload và precision không?
2. Metric nào measured, metric nào proxy?
3. Gain tồn tại sau hardware overhead không?
4. Điểm Pareto nào có ý nghĩa hệ thống?

**Bước đi tiếp:** AB-R01/R02/R03 → manuscript/publication/PhD research line

## Danh sách đề tài

| Mã | Tên | Loại | Sàn | Sản phẩm phải làm ra |
|---|---|---|---|---|
| [`AB-P01`](AB-P01.md) | Đo chi phí một thuật toán trên ba nền tảng: MCU, FPGA, ASIC ước lượng | P | L2 | Same processing block on MCU/FPGA/ASIC estimate; cycles/energy/resource/Fmax/area/timing; … |
| [`AB-T01`](AB-T01.md) | ASIC feasibility study cho Polar Processing Element | T | L3 `B12` | Verified PE; synthesis; STA; physical implementation; PPA; analysis |
| [`AB-T02`](AB-T02.md) | FPGA-to-ASIC evaluation của Polar Encoder | T | L3 | FPGA metrics + ASIC PPA; methodology comparison; report |
| [`AB-T03`](AB-T03.md) | FPGA-to-ASIC evaluation của SC Polar Decoder | T | L4 | Selected decoder/core; FPGA and ASIC evidence; trade-off analysis |
| [`AB-T04`](AB-T04.md) | PPA optimization cho fixed-point Polar Processing Element | T | L4 | Bit-width/pipeline configurations; BLER/numerical impact; ASIC PPA; Pareto analysis |
| [`AB-T05`](AB-T05.md) | Tăng tốc phần cứng cho suy luận AI biên trên SoC FPGA | T | L3 `C5` | CPU-only baseline; RTL accelerator; end-to-end latency/energy/resource; speedup analysis |
| [`AB-T06`](AB-T06.md) | Bộ giải mã SC Polar tiết kiệm năng lượng cho liên kết IoT | T | L3 `C6` | Fixed-point SC in IoT context; BLER + energy/bit + latency; comparative evaluation |
| [`AB-R01`](AB-R01.md) | Hardware-aware design-space exploration cho Polar Decoder | R | L5 | Reproducible multi-objective experiments; BLER-area-latency-throughput-energy; manuscript … |
| [`AB-R02`](AB-R02.md) | Co-design thuật toán – phần cứng cho truyền thông tin cậy ở thiết bị biên | R | L4 | Adaptive Polar vs edge energy budget; experimental framework; >=2 strategies; analysis |
| [`AB-R03`](AB-R03.md) | Nền tảng biên tích hợp: truyền thông và suy luận chia sẻ tài nguyên phần cứng | R | L5 | Polar decoder + edge-AI inference on shared SoC/FPGA; resource scheduling and energy-budge… |

---

*[← Bản đồ 16 nhóm](../README.md)*
