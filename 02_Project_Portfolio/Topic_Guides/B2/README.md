# Nhóm B2 — Bộ giải mã SC Polar trên phần cứng

**Engineering & Research Mentoring Program (Lucero)** · ThS. Đinh Văn Nam (Mr. Lucero Dinh) — Khoa Điện–Điện tử, Trường Kỹ thuật, Đại học Phenikaa

> **File sinh tự động** từ `06_Data/research_packs.json` bằng `scripts/generate_research_packs.py`. Sửa tay sẽ bị ghi đè — muốn đổi nội dung thì sửa JSON rồi chạy lại script.

**SC Polar Decoder Hardware** · 4 đề tài

## Nền chung của cả nhóm

Mọi đề tài trong nhóm này đều đi qua bốn mục dưới đây. Trang của từng đề tài chỉ thêm
**sản phẩm riêng** mà đề tài đó phải làm ra.

**Phải đọc**

- full SC decoding schedule
- memory/partial sums
- controller/datapath
- fixed-point
- FPGA metrics

**Phải hiểu**

- tree traversal/dependencies
- cycle latency
- memory architecture
- software↔RTL bit-exactness

**Phải dựng**

- golden model
- fixed-point RTL decoder
- co-verification
- FPGA implementation

**Thí nghiệm mặc định**

- BLER baseline
- vector co-verification
- resource/Fmax/latency/throughput
- architecture/resource-sharing comparison

**Câu hỏi mentor**

1. Latency đo từ đâu tới đâu?
2. Bottleneck controller hay datapath/memory?
3. RTL có bit-exact với golden không?
4. Architecture này scale theo N ra sao?

**Bước đi tiếp:** B3/B4/B5 → B2-R01/AB-R01

## Danh sách đề tài

| Mã | Tên | Loại | Sàn | Sản phẩm phải làm ra |
|---|---|---|---|---|
| [`B2-I01`](B2-I01.md) | Xây dựng kiến trúc SC decoder theo từng module | I | L2 | Module interfaces; f/g/partial-sum/control integration tests; documentation |
| [`B2-T01`](B2-T01.md) | Thiết kế bộ giải mã SC Polar trên FPGA | T | L3 `B3` | Golden model; fixed-point; RTL decoder; co-verification; FPGA; BER/BLER + resource/Fmax/la… · 📘 hồ sơ sâu |
| [`B2-T02`](B2-T02.md) | Software-RTL co-verification cho SC Polar decoder | T | L3 | Automated vector generation; RTL comparison; regression; mismatch diagnosis; report |
| [`B2-R01`](B2-R01.md) | Architecture optimization cho SC decoder | R | L4 | 2+ architectures or parallelism/resource-sharing configurations; controlled evaluation |

---

*[← Bản đồ 16 nhóm](../README.md)*
