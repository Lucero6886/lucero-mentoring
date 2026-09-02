# AB-R01 — Hardware-aware design-space exploration cho Polar Decoder

**Engineering & Research Mentoring Program (Lucero)** · ThS. Đinh Văn Nam (Mr. Lucero Dinh) — Khoa Điện–Điện tử, Trường Kỹ thuật, Đại học Phenikaa

> **File sinh tự động** từ `06_Data/research_packs.json` bằng `scripts/generate_research_packs.py`. Sửa tay sẽ bị ghi đè — muốn đổi nội dung thì sửa JSON rồi chạy lại script.

**English:** Hardware-Aware Design-Space Exploration for Polar Decoding

**Nhóm:** `AB` — Vùng giao: IC số × Polar × Edge co-design (Digital IC × Polar / Edge Co-Design)
**Loại:** `R` — Nghiên cứu khoa học · **Sàn năng lực:** L5

> **Vai trò trong chương trình.** Research-first. Phải có hypothesis/RQ, strong baseline, controlled experiments, reproducibility; mục tiêu trực tiếp là manuscript-ready evidence.

## Sản phẩm phải làm ra

Reproducible multi-objective experiments; BLER-area-latency-throughput-energy; manuscript assets

Đây là phần **riêng của đề tài này**. Nếu cuối kỳ không có đủ những thứ trên thì đề tài chưa xong,
dù đã bỏ bao nhiêu thời gian.

> Bốn mục dưới đây là **nền chung của cả nhóm AB** — mọi đề tài trong nhóm đều đi qua. Phần riêng của đề tài này nằm ở mục *Sản phẩm phải làm ra*.

## Trước khi bắt đầu — phải đọc

- cross-platform benchmarking
- FPGA vs ASIC metrics
- energy/latency accounting
- algorithm-hardware co-design
- multi-objective optimization

Tài liệu cụ thể theo hướng: [`09_References/READING-LIST.md`](../../../09_References/READING-LIST.md)

## Phải hiểu được (không nhìn tài liệu)

- fair cross-platform comparison
- proxy vs measured energy
- algorithmic vs implementation gain
- Pareto dominance

## Phải dựng / code / chế tạo

- shared golden workload
- FPGA/ASIC/SoC implementations or estimates
- automated metric extraction
- trade-off analysis

## Thí nghiệm và đo kiểm mặc định

- platform/architecture sweep
- bit-width/pipeline sweep
- BLER/accuracy vs PPA/energy
- multi-objective Pareto

## Câu hỏi mentor sẽ hỏi đi hỏi lại

1. Comparison có cùng workload và precision không?
2. Metric nào measured, metric nào proxy?
3. Gain tồn tại sau hardware overhead không?
4. Điểm Pareto nào có ý nghĩa hệ thống?

## Khi nào mới nói tới bài báo

Paper-ready khi hypothesis được kiểm chứng/bác bỏ bằng controlled evidence; baseline đủ mạnh; có robustness/ablation/failure cases; claim không vượt evidence; package tái lập được.

> Một PCB project không trở thành nghiên cứu chỉ vì thêm chữ “nghiên cứu” vào tên. Muốn lên R phải có biến, baseline, metric, hypothesis và experiment có kiểm soát.

## Bước đi tiếp sau đề tài này

AB-R01/R02/R03 → manuscript/publication/PhD research line

## Cảnh báo sớm — mentor dừng đề tài khi thấy

- demo không có test/measurement
- chỉ screenshot, không raw/config
- so sánh khác constraint
- thay nhiều biến cùng lúc
- paper claim trước khi baseline đúng
- AI code không giải thích được

## Quy tắc dữ liệu thô

- Không overwrite raw measurement/simulation
- Mỗi run lưu config, seed, git commit, tool version, date
- Figure/table phải được tạo lại từ script
- Ảnh oscilloscope/logic analyzer phải có test condition
- Board revision/BOM/firmware/bitstream phải versioned

---

| Cần gì | Đọc đâu |
|---|---|
| Sáu cửa kiểm soát và thang G0–G7 | [`06_Data/milestone_gates.json`](../../../06_Data/milestone_gates.json) |
| Chuẩn tổ chức repository | [`04_Project_Template/REPRODUCIBILITY_STANDARD.md`](../../../04_Project_Template/REPRODUCIBILITY_STANDARD.md) |
| Toàn bộ nhóm `AB` | [`README.md`](README.md) |
| Bản đồ 16 nhóm | [`../README.md`](../README.md) |
