# DRY RUN — B-track · `B2-T01` (alias cohort: B3)

**Mục đích:** kiểm tra end-to-end quy trình hệ thống v1.1 trên một sinh viên giả định làm đề tài
**B2-T01 — Thiết kế bộ giải mã SC Polar trên FPGA**, có kịch bản **trượt Gate 3 → reduce scope** để
kiểm tra các hard rule và thang cảnh báo. Dry-run GIẤY (bước 8 roadmap) — dữ liệu giả định, không PII thật.

Sinh viên giả định: **SV-B** (năm 4, đã qua Thực tập tốt nghiệp ✔).

---

## Giai đoạn 0 — Admission (20/08 → 03/09)

| Bước | Thực hiện trong dry-run | Kiểm tra quy tắc | OK? |
|---|---|---|---|
| Top-3 (Phiếu 1) | Top-1 `B6-T02` (neural-assisted!), Top-2 `B2-T01`, Top-3 `B0-T01` | Top-3 là nguyện vọng, không phải quyền chọn tuyệt đối | ✔ |
| Chặn nhảy cóc lên NN | `B6-T02.min_level = 4`, prereq `B4 stable + ML` — SV-B chưa có SCF baseline → mentor **từ chối Top-1**, đúng chuỗi chống nhảy cóc B-track | `project_portfolio.json` + Handbook §7 | ✔ |
| Readiness test 2 tuần | Literature (paper SC decoding): pass · Mini-task: viết SC decoder Python N=8, BER khớp lý thuyết: pass · Oral: giải thích f/g function: pass | Phiếu 4 | ✔ |
| Kiểm prerequisite `B2-T01` | `prereq_codes = ["B0-P03", "B1-P*"]` → mini-task chứng minh tương đương B0-P03 ✔; RTL: SV-B có đồ án FIFO/UART (tương đương A1-P) nhưng **chưa làm B1-P nào** → gap thật | JSON | ⚠ gap |
| Mentor evaluation (Phiếu 5) | WR: 3+3+4+3+3 = **16/20** ≥ 15 (DATN research-oriented) ✔ · RR: literature 3, baseline 3, experiment 2, interpretation 2, ownership 2 — đạt mức "khá" · min_level 3 = sát năng lực | Ngưỡng rubrics JSON | ✔ |
| Kết luận | **Nhận có điều kiện:** 2 tuần đầu phải hoàn thành f/g PE mini-module (lấp gap B1-P); ghi vào "Lý do/điều kiện" | 4 lựa chọn chuẩn | ✔ |

## Giai đoạn 1 — Onboarding (W1)

- Charter: Code `B2-T01`; **MVT từ JSON:** SC golden model; RTL decoder *hoặc subsystem đủ lớn*; test vectors + co-verification; resource/Fmax/latency/throughput; architecture report. **Extension:** optimization chỉ sau khi đúng chức năng. Ghi rõ N mục tiêu ban đầu: **N=64** (subsystem N=16 là mức lùi). ✔
- Workbook: Students (Risk=Green, điều kiện probation ghi ở Notes), Milestones block 6 gate. ✔
- **Nhận xét:** field "Điều kiện probation" không có cột riêng trong Students — dùng Notes. Chấp nhận được.

## Giai đoạn 2 — Vận hành 15 tuần (có kịch bản trượt)

| Gate (deadline) | Kịch bản | Quy tắc hệ thống kích hoạt | Kết quả |
|---|---|---|---|
| G1 (20/09) | Architecture plan xong; điều kiện probation (f/g PE) hoàn thành W2 | Probation → Official scope đúng SOP §2 | **Pass** |
| G2 (11/10) | W5: golden model + f/g/partial-sum unit tests pass; BER N=64 khớp reference. Baseline CÓ | Gate 2 có baseline → extension *có thể* mở về sau | **Pass** |
| W6–7 | SV-B im lặng 1 chu kỳ (thi giữa kỳ các môn khác) | **Thang cảnh báo mức 1:** nhắc + hỏi blocker (Agreement §E) | kích hoạt đúng |
| W7–8 | Tiếp tục thiếu evidence chu kỳ 2: control FSM tích hợp bị deadlock chưa gỡ | **Mức 2: formal warning + recovery plan** (1 tuần, mục tiêu: gỡ deadlock trên subsystem N=16 trước) | kích hoạt đúng |
| G3 (01/11) | W8: decoder N=64 tích hợp CHƯA chạy (chỉ subsystem N=16 chạy đúng) → **TRƯỢT Gate 3** | **Hard rule G3: reduce scope, mentor không làm thay.** Chẩn đoán 3 biến: difficulty cao (tích hợp control) × time thiếu (2 tuần thi) × strategy ổn → quyết định: **scope chính thức = SC decoder N=16 hoàn chỉnh + phân tích scaling lên N=64 bằng model**; extension đóng vĩnh viễn | **Fail → Reduce scope** ✔ đúng thiết kế |
| Ghi nhận quyết định | Meeting Record + Milestones (G3 = "Failed/Scope Review") + Students (Risk=Yellow, MVT cập nhật) + charter sửa scope có ghi ngày | Mọi nơi có chỗ ghi ✔ | ✔ |
| G4 (22/11) | W11: N=16 decoder trên FPGA: resource/Fmax/latency/throughput đo xong; BER/BLER co-verification khớp golden | Sau 22/11 không thêm thuật toán mới — tuân thủ | **Pass** |
| G5 (06/12) | Bản thảo: kết quả N=16 + scaling analysis + phân tích trung thực về reduce scope | "Không polish che lỗ hổng" — chương limitation ghi rõ | **Pass** |
| G6 (19/12) | Mentor chạy lại co-verification từ README: tái lập ✔; oral defense: SV giải thích được deadlock cũ đã gỡ thế nào | Legacy 11/11 + Definition of Done 10/10 | **Pass** |

## Giai đoạn 3 — Closeout

- Reduce scope KHÔNG bị coi là thất bại: khóa luận N=16 correct + complete + reproducible + quantitatively evaluated = đạt chuẩn DATN theo định nghĩa thành công (Handbook §15). ✔
- `KNOWN_ISSUES.md` ghi deadlock pattern; `NEXT_STEPS.md` ghi "scale N=64 với partial-sum memory tối ưu" → cohort sau nhận legacy để làm `B2-R01`. Đúng tinh thần technical lineage. ✔
- Mời tiếp NCKH? RR sau kỳ ≈ khá → **có thể** mời `B2-R01` kỳ sau nếu SV muốn. ✔

## KẾT LUẬN B-TRACK: **PASS** — các hard rule (chặn nhảy cóc, warning ladder, G3 reduce-scope, không làm thay, legacy) đều kích hoạt đúng chỗ và có nơi ghi nhận.

### Ghi nhận (đưa vào FINAL_SYSTEM_AUDIT):
1. Students sheet không có cột riêng cho "điều kiện probation" — dùng Notes; nếu cohort đông, cân nhắc thêm cột "Conditions" ở version sau (không sửa trong dry-run).
2. Khi reduce scope, cần nhớ cập nhật MVT trong **cả** charter lẫn cột MVT của Students — SOP §5 đã yêu cầu ghi tracker, hoạt động đúng, nhưng nên nêu ví dụ này trong buổi hướng dẫn mentor mới.
