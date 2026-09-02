# Nhóm A5 — Kiểm chứng, EDA và phát triển tái lập

**Engineering & Research Mentoring Program (Lucero)** · ThS. Đinh Văn Nam (Mr. Lucero Dinh) — Khoa Điện–Điện tử, Trường Kỹ thuật, Đại học Phenikaa

> **File sinh tự động** từ `06_Data/research_packs.json` bằng `scripts/generate_research_packs.py`. Sửa tay sẽ bị ghi đè — muốn đổi nội dung thì sửa JSON rồi chạy lại script.

**Verification, EDA & Reproducible Hardware Development** · 6 đề tài

## Nền chung của cả nhóm

Mọi đề tài trong nhóm này đều đi qua bốn mục dưới đây. Trang của từng đề tài chỉ thêm
**sản phẩm riêng** mà đề tài đó phải làm ra.

**Phải đọc**

- verification planning
- regression
- Git/CI
- reproducible environments
- PPA regression

**Phải hiểu**

- repeatability vs reproducibility
- test coverage intent
- version pinning
- failure triage

**Phải dựng**

- automation scripts
- CI/regression pipeline
- version manifest
- failure reports

**Thí nghiệm mặc định**

- clean-clone run
- multi-commit regression
- intentional failure tests
- runtime/reproducibility evaluation

**Câu hỏi mentor**

1. Một người khác có thể tái lập từ zero không?
2. Failure nào pipeline bắt được?
3. Threshold regression có false alarm không?
4. Hạ tầng này tiết kiệm công sức/giảm lỗi bằng số liệu nào?

**Bước đi tiếp:** A4/AB → A5-R01

## Danh sách đề tài

| Mã | Tên | Loại | Sàn | Sản phẩm phải làm ra |
|---|---|---|---|---|
| [`A5-P01`](A5-P01.md) | Xây dựng testbench có hệ thống cho một RTL module | P | L1 | Test plan; testbench; pass/fail evidence; bug log |
| [`A5-P02`](A5-P02.md) | Regression testing cho Digital IP | P | L2 | Regression script; test set; summary report; reproducible run |
| [`A5-I01`](A5-I01.md) | Xây dựng Git workflow cho dự án RTL | I | L1 | Repo structure; branches/issues; README; test scripts; contribution guide |
| [`A5-T01`](A5-T01.md) | Xây dựng quy trình ASIC tái lập sử dụng LibreLane + Nix | T | L3 `A6` | Pinned environment; 3 reference designs; repeatability evidence; docs; troubleshooting · 📘 hồ sơ sâu |
| [`A5-T02`](A5-T02.md) | Continuous Integration cho dự án RTL/ASIC | T | L3 `A7` | CI pipeline; lint/sim/regression/synthesis reports; failure examples; docs |
| [`A5-R01`](A5-R01.md) | Automated PPA regression cho Digital IC | R | L4 | Dataset of commits/configurations; regression thresholds; analysis; research report |

---

*[← Bản đồ 16 nhóm](../README.md)*
