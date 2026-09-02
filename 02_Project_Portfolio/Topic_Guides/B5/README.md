# Nhóm B5 — Giải mã Polar thích ứng

**Engineering & Research Mentoring Program (Lucero)** · ThS. Đinh Văn Nam (Mr. Lucero Dinh) — Khoa Điện–Điện tử, Trường Kỹ thuật, Đại học Phenikaa

> **File sinh tự động** từ `06_Data/research_packs.json` bằng `scripts/generate_research_packs.py`. Sửa tay sẽ bị ghi đè — muốn đổi nội dung thì sửa JSON rồi chạy lại script.

**Adaptive Polar Decoding** · 6 đề tài

## Nền chung của cả nhóm

Mọi đề tài trong nhóm này đều đi qua bốn mục dưới đây. Trang của từng đề tài chỉ thêm
**sản phẩm riêng** mà đề tài đó phải làm ra.

**Phải đọc**

- adaptive/selective decoding
- classification metrics
- reliability features
- average-case cost
- gating

**Phải hiểu**

- false trigger vs missed hard frame
- activation rate
- operating point
- always-on vs selective

**Phải dựng**

- detector/gate
- adaptive framework
- metrics logger
- optional hardware model

**Thí nghiệm mặc định**

- ROC/PR or trigger trade-off
- BLER vs SNR
- activation/average attempts/latency
- threshold sensitivity/oracle comparison

**Câu hỏi mentor**

1. Feature có sẵn trước lúc ra quyết định không?
2. False negative làm hỏng BLER thế nào?
3. Savings đến từ đâu?
4. Threshold có ổn định khi SNR thay đổi không?

**Bước đi tiếp:** B6/AB → B5-R01/B6-R01/AB-R02

## Danh sách đề tài

| Mã | Tên | Loại | Sàn | Sản phẩm phải làm ra |
|---|---|---|---|---|
| [`B5-P01`](B5-P01.md) | Thiết kế unreliable-frame detector dựa trên threshold | P | L2 | Detector; ROC/trigger or classification metrics; plots |
| [`B5-I01`](B5-I01.md) | Xây dựng adaptive SC/SCF simulation framework | I | L3 | Reliable/unreliable branch framework; seeded experiments; activation statistics; docs |
| [`B5-T01`](B5-T01.md) | Phát hiện frame không tin cậy cho adaptive Polar decoding | T | L3 `B7` | Feature study; threshold/logistic baseline; detection/false trigger/missed trigger/activat… · 📘 hồ sơ sâu |
| [`B5-T02`](B5-T02.md) | Adaptive decoder chỉ kích hoạt enhanced processing trên frame khó | T | L3 `B9` | End-to-end adaptive framework; BLER; activation rate; avg attempts/latency/complexity · 📘 hồ sơ sâu |
| [`B5-T03`](B5-T03.md) | Đồng thiết kế thuật toán - phần cứng cho bộ giải mã Polar thích ứng | T | L4 `B11` | Algorithm baseline; operation/memory model; fixed-point; RTL critical blocks; reliability-… · 📘 hồ sơ sâu |
| [`B5-R01`](B5-R01.md) | Adaptive Polar decoding dưới ràng buộc hardware | R | L4 | Research hypothesis; reproducible baselines; latency/resource/energy proxy; paper-ready an… |

---

*[← Bản đồ 16 nhóm](../README.md)*
