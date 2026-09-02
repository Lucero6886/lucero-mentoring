# Nhóm B6 — Giải mã Polar hỗ trợ mạng neural

**Engineering & Research Mentoring Program (Lucero)** · ThS. Đinh Văn Nam (Mr. Lucero Dinh) — Khoa Điện–Điện tử, Trường Kỹ thuật, Đại học Phenikaa

> **File sinh tự động** từ `06_Data/research_packs.json` bằng `scripts/generate_research_packs.py`. Sửa tay sẽ bị ghi đè — muốn đổi nội dung thì sửa JSON rồi chạy lại script.

**Neural-Assisted Polar Decoding** · 5 đề tài

## Nền chung của cả nhóm

Mọi đề tài trong nhóm này đều đi qua bốn mục dưới đây. Trang của từng đề tài chỉ thêm
**sản phẩm riêng** mà đề tài đó phải làm ra.

**Phải đọc**

- classical ML baselines
- small neural networks
- train/val/test hygiene
- quantization-aware inference
- hardware cost

**Phải hiểu**

- data leakage
- class imbalance
- NN justification
- parameters/MACs/memory vs end-to-end gain

**Phải dựng**

- dataset pipeline
- heuristic/classical baseline
- tiny NN
- quantized/hardware-aware evaluation

**Thí nghiệm mặc định**

- baseline vs NN
- feature/model ablation
- quantization/model-size sweep
- end-to-end BLER/activation/attempts/cost

**Câu hỏi mentor**

1. NN học được gì heuristic không làm được?
2. Có leakage không?
3. AUC/Top-k gain có biến thành decoder gain không?
4. Net saving sau NN overhead là bao nhiêu?

**Bước đi tiếp:** AB → B6-R01/B6-R02/AB-R01

## Danh sách đề tài

| Mã | Tên | Loại | Sàn | Sản phẩm phải làm ra |
|---|---|---|---|---|
| [`B6-I01`](B6-I01.md) | Lightweight ML classifier cho unreliable-frame detection | I | L3 | Train/val/test split; logistic/simple ML/MLP comparisons; reproducible model; metrics |
| [`B6-T01`](B6-T01.md) | Lightweight neural-assisted unreliable-frame detector | T | L4 | Heuristic + classical ML + lightweight NN; BLER/activation/model size/inference cost · 📘 hồ sơ sâu |
| [`B6-T02`](B6-T02.md) | Neural-assisted candidate ranking cho SC-Flip Polar decoder | T | L4 `B10` | SC/SCF baselines; Top-k; BLER; attempts; model parameters/ops; thesis · 📘 hồ sơ sâu |
| [`B6-R01`](B6-R01.md) | Hardware-aware neural-assisted adaptive Polar decoder | R | L5 | Research-grade ablation; BLER; activation; latency/ops/memory/resource/energy proxy; repro… |
| [`B6-R02`](B6-R02.md) | Algorithm-hardware co-design của neural-assisted Polar decoder | R | L5 | Joint algorithm/hardware design space; hardware-aware model selection; implementation evid… |

---

*[← Bản đồ 16 nhóm](../README.md)*
