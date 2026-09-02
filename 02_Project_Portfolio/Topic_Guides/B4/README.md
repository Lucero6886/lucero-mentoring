# Nhóm B4 — SC-Flip và giải mã theo độ tin cậy

**Engineering & Research Mentoring Program (Lucero)** · ThS. Đinh Văn Nam (Mr. Lucero Dinh) — Khoa Điện–Điện tử, Trường Kỹ thuật, Đại học Phenikaa

> **File sinh tự động** từ `06_Data/research_packs.json` bằng `scripts/generate_research_packs.py`. Sửa tay sẽ bị ghi đè — muốn đổi nội dung thì sửa JSON rồi chạy lại script.

**SC-Flip & Reliability-Aware Decoding** · 6 đề tài

## Nền chung của cả nhóm

Mọi đề tài trong nhóm này đều đi qua bốn mục dưới đây. Trang của từng đề tài chỉ thêm
**sản phẩm riêng** mà đề tài đó phải làm ra.

**Phải đọc**

- SC error propagation
- SC-Flip
- reliability metrics
- Top-k ranking
- retry complexity

**Phải hiểu**

- first-error phenomenon
- ranking vs classification
- average attempts
- BLER-latency trade-off

**Phải dựng**

- SCF baseline
- failure data collector
- candidate ranking
- reproducible evaluation

**Thí nghiệm mặc định**

- Top-k
- BLER vs SNR
- Tmax/attempts
- metric complexity/ablation

**Câu hỏi mentor**

1. True error label định nghĩa thế nào?
2. Ranking tốt hơn có giảm attempts thật không?
3. Tmax có diminishing return ở đâu?
4. Overhead metric có ăn hết lợi ích không?

**Bước đi tiếp:** B5/B6 → B4-R01/B6-R02

## Danh sách đề tài

| Mã | Tên | Loại | Sàn | Sản phẩm phải làm ra |
|---|---|---|---|---|
| [`B4-P01`](B4-P01.md) | Phân tích các lỗi SC decoding | P | L2 | Failure cases; reliability traces; categorized analysis |
| [`B4-P02`](B4-P02.md) | Reliability ranking dựa trên trị tuyệt đối LLR | P | L2 | Candidate ranking; Top-k metrics; plots |
| [`B4-I01`](B4-I01.md) | Xây dựng SC-Flip software decoder | I | L2 | SCF code; validation; BLER/attempts; reproducible scripts |
| [`B4-T01`](B4-T01.md) | Thiết kế và đánh giá SC-Flip Polar decoder | T | L3 `B6` | SC vs SCF; BLER; attempts; latency/complexity proxy; analysis · 📘 hồ sơ sâu |
| [`B4-T02`](B4-T02.md) | Reliability-based candidate ranking cho SC-Flip | T | L3 `B8` | Top-1/Top-k ranking; BLER; attempts; baselines; thesis · 📘 hồ sơ sâu |
| [`B4-R01`](B4-R01.md) | Improved reliability metric cho SCF | R | L4 | New/combined metric; ablation; statistical evaluation; paper-ready figures |

---

*[← Bản đồ 16 nhóm](../README.md)*
