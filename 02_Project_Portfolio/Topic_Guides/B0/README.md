# Nhóm B0 — Nền Polar và baseline phần mềm

**Engineering & Research Mentoring Program (Lucero)** · ThS. Đinh Văn Nam (Mr. Lucero Dinh) — Khoa Điện–Điện tử, Trường Kỹ thuật, Đại học Phenikaa

> **File sinh tự động** từ `06_Data/research_packs.json` bằng `scripts/generate_research_packs.py`. Sửa tay sẽ bị ghi đè — muốn đổi nội dung thì sửa JSON rồi chạy lại script.

**Polar Fundamentals & Software Baseline** · 5 đề tài

## Nền chung của cả nhóm

Mọi đề tài trong nhóm này đều đi qua bốn mục dưới đây. Trang của từng đề tài chỉ thêm
**sản phẩm riêng** mà đề tài đó phải làm ra.

**Phải đọc**

- Polar code construction basics
- BPSK/AWGN
- LLR
- SC decoding
- BER/BLER simulation methodology

**Phải hiểu**

- N/K/R frozen-information bits
- LLR sign/magnitude
- SC dependency
- confidence intervals / sufficient error counts

**Phải dựng**

- encoder/channel/decoder golden model
- seeded experiment scripts
- unit/known-vector tests
- BLER/BER plots

**Thí nghiệm mặc định**

- Eb/N0 sweep
- small-N hand validation
- N/K sensitivity if applicable
- repeatability/seeds

**Câu hỏi mentor**

1. Frozen set đến từ đâu?
2. LLR này có đúng convention không?
3. Bao nhiêu frame/error đủ để tin BLER?
4. Baseline có khớp xu hướng lý thuyết/literature không?

**Bước đi tiếp:** B1/B2 → B3/B4/B5

## Danh sách đề tài

| Mã | Tên | Loại | Sàn | Sản phẩm phải làm ra |
|---|---|---|---|---|
| [`B0-P01`](B0-P01.md) | Mô phỏng Polar Encoder | P | L0 | Encoder implementation; known-vector validation; report |
| [`B0-P02`](B0-P02.md) | Mô phỏng BPSK/AWGN và tính LLR | P | L0 | Channel simulation; LLR sanity checks; plots |
| [`B0-P03`](B0-P03.md) | Xây dựng SC decoder cơ bản bằng MATLAB/Python | P | L1 | SC decoder; unit tests; small BER/BLER result |
| [`B0-I01`](B0-I01.md) | Xây dựng bộ mô phỏng Polar Code có khả năng tái lập | I | L2 | Configurable N/K/EbN0; seeded runs; BER/BLER; README; scripts |
| [`B0-T01`](B0-T01.md) | Xây dựng và đánh giá hệ thống Polar Code sử dụng SC decoding | T | L2 `B1` | Full encode-channel-decode chain; validation; BER/BLER sweeps; complexity discussion; lega… |

---

*[← Bản đồ 16 nhóm](../README.md)*
