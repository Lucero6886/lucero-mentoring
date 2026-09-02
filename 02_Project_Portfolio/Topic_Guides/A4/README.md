# Nhóm A4 — Thiết kế ASIC và hiện thực vật lý

**Engineering & Research Mentoring Program (Lucero)** · ThS. Đinh Văn Nam (Mr. Lucero Dinh) — Khoa Điện–Điện tử, Trường Kỹ thuật, Đại học Phenikaa

> **File sinh tự động** từ `06_Data/research_packs.json` bằng `scripts/generate_research_packs.py`. Sửa tay sẽ bị ghi đè — muốn đổi nội dung thì sửa JSON rồi chạy lại script.

**ASIC Design & Physical Implementation** · 6 đề tài

## Nền chung của cả nhóm

Mọi đề tài trong nhóm này đều đi qua bốn mục dưới đây. Trang của từng đề tài chỉ thêm
**sản phẩm riêng** mà đề tài đó phải làm ra.

**Phải đọc**

- logic synthesis
- STA
- floorplan/place/CTS/route
- DRC/LVS
- PPA và open-source ASIC flow

**Phải hiểu**

- slack/critical path
- utilization/congestion
- logical vs physical correctness
- same RTL + different constraints → different PPA

**Phải dựng**

- verified RTL
- flow configs/scripts
- GDSII/physical evidence
- PPA extraction

**Thí nghiệm mặc định**

- clock-period sweep
- utilization/architecture sweep
- repeatability run
- PPA/DRC/LVS analysis

**Câu hỏi mentor**

1. Constraint nào đang chi phối kết quả?
2. DRC pass có nghĩa LVS pass không?
3. PPA comparison có cùng điều kiện không?
4. Insight nào vượt khỏi việc 'chạy được tool'?

**Bước đi tiếp:** A5/AB → A4-R01/AB-R01

## Danh sách đề tài

| Mã | Tên | Loại | Sàn | Sản phẩm phải làm ra |
|---|---|---|---|---|
| [`A4-P01`](A4-P01.md) | Làm quen RTL-to-Gates bằng Yosys | P | L1 | RTL; synthesis script; netlist/report; explanation |
| [`A4-P02`](A4-P02.md) | Khảo sát ảnh hưởng của RTL coding style tới synthesis | P | L2 | Equivalent RTL variants; synthesis evidence; comparison |
| [`A4-I01`](A4-I01.md) | Xây dựng môi trường RTL-to-GDSII mã nguồn mở | I | L2 | Reproducible setup; sample designs; documented commands; troubleshooting notes |
| [`A4-T01`](A4-T01.md) | Thiết kế một Digital IP từ RTL đến GDSII | T | L2 `A1` | Spec; RTL; testbench; synthesis; STA; physical implementation; DRC/LVS evidence; GDSII; PP… · 📘 hồ sơ sâu |
| [`A4-T02`](A4-T02.md) | Khảo sát ảnh hưởng kiến trúc RTL đến PPA | T | L3 `A2` | 2+ functionally equivalent architectures; controlled PPA comparison; analysis |
| [`A4-R01`](A4-R01.md) | Design-space exploration cho một Digital IP | R | L4 | Automated experiments; statistical/controlled analysis; research report |

---

*[← Bản đồ 16 nhóm](../README.md)*
