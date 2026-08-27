# Student Profile — <MÃ_ĐỀ_TÀI> · <HỌ TÊN>

> Hồ sơ logic của một sinh viên (MASTER_PROMPT §5). Một file cho mỗi SV.
> **Chứa dữ liệu cá nhân → lưu trong `07_Private/`, không commit lên repo public.**
> Bản tổng hợp nhiều SV nằm ở workbook `03_Operations/Mentoring_Management_Workbook.xlsx` (sheet Students/Readiness).

```yaml
student:
  name:
  student_id:
  class:
  cohort:                 # vd HK1_2026_2027
  career_goal:            # mục tiêu 1-2 năm tới
  weekly_hours:           # số giờ/tuần cam kết

topic_selection:
  top_1:                  # MÃ CHUẨN, vd A4-T01
  top_2:
  top_3:
  assigned_canonical_code:
  assigned_date:
  alias_display:          # mã ngắn cohort, chỉ để đọc nhanh

readiness:
  level_student:          # L0..L5 — mức đánh giá của SV
  level_topic_min:        # min_level của đề tài được giao
  level_check:            # DAT_SAN | CHUA_DAT_SAN (nếu chưa đạt: ghi lý do vẫn nhận)
  technical:              # xem bảng TR bên dưới
  working:                # tổng /20
  research:               # tổng /20 + nhận định định tính
  prerequisite_gaps:
  readiness_test_status:  # NOT_STARTED | IN_PROGRESS | PASSED | FAILED

thesis_contract:
  problem:
  scope:
  mandatory_mvt:          # chép từ trường mvt của đề tài trong 06_Data
  optional_items:
  research_extension:     # CLOSED cho tới khi qua Gate 2
  tools:
  reproducibility_requirements:

progress:
  current_week:           # 1..15
  current_gate:           # 1..6
  gate_status:            # PASS | CONDITIONAL_PASS | FAIL | NOT_ENOUGH_EVIDENCE
  schedule_status:        # ON_TRACK | AT_RISK | OFF_TRACK | BLOCKED
  ownership_status:       # STRONG | ADEQUATE | UNCERTAIN | NEEDS_ORAL_CHECK
  completed_evidence:
  missing_evidence:
  blockers:
  risks:
```

## Technical Readiness — tách tự đánh giá khỏi kiểm chứng

Thang 0–5: 0 chưa biết · 1 biết tên · 2 hiểu cơ bản · 3 làm được có hướng dẫn · 4 tự làm được · 5 giải thích/mentor được người khác.

Cột **Trạng thái kiểm chứng** dùng đúng 5 giá trị của MASTER_PROMPT §2.3 — **không** gộp cả hồ sơ thành một số trung bình.

| Năng lực | Tự chấm 0–5 | Điểm sau kiểm chứng | Trạng thái | Evidence |
|---|---|---|---|---|
| Điện tử cơ bản |  |  | `UNKNOWN` |  |
| Logic số |  |  | `UNKNOWN` |  |
| Verilog/SystemVerilog |  |  | `UNKNOWN` |  |
| Simulation/debug waveform |  |  | `UNKNOWN` |  |
| FPGA |  |  | `UNKNOWN` |  |
| Python |  |  | `UNKNOWN` |  |
| MATLAB |  |  | `UNKNOWN` |  |
| Linux/WSL |  |  | `UNKNOWN` |  |
| Git/GitHub |  |  | `UNKNOWN` |  |
| DSP |  |  | `UNKNOWN` |  |
| Truyền thông số |  |  | `UNKNOWN` |  |
| Xác suất |  |  | `UNKNOWN` |  |
| Coding theory |  |  | `UNKNOWN` |  |
| Polar Codes |  |  | `UNKNOWN` |  |
| Đọc tài liệu tiếng Anh |  |  | `UNKNOWN` |  |
| Technical writing |  |  | `UNKNOWN` |  |

`SELF_REPORTED` = mới có điểm tự chấm · `EVIDENCE_VERIFIED` = đã chứng minh bằng mini-task/sản phẩm ·
`PARTIAL` = có evidence nhưng chưa đủ mức tự chấm · `MISSING` = tự chấm cao nhưng không có evidence ·
`UNKNOWN` = chưa xét.

## Working Readiness — /20

| Phẩm chất | Điểm 0–4 | Evidence quan sát được |
|---|---|---|
| Cam kết & kỷ luật |  |  |
| Kiên trì |  |  |
| Trung thực |  |  |
| Chủ động |  |  |
| Tư duy phản biện |  |  |

Ngưỡng gợi ý: Project ≥10 · Internship ≥12 · DATN engineering ≥14 · DATN research-oriented ≥15 · NCKH ≥16 · advanced (family B6 / AB-R) ≥17.
**Ngưỡng là gợi ý, không phải luật.** Mentor được override — bắt buộc ghi lý do vào `DECISION_LOG.md`.

## Research Readiness — /20 + nhận định

| Tiêu chí | Điểm 0–4 | Nhận định |
|---|---|---|
| Literature comprehension |  |  |
| Baseline discipline |  |  |
| Experimental design |  |  |
| Interpretation |  |  |
| Research ownership |  |  |

RR **không có ngưỡng số** — kết luận bằng nhận định + evidence, đối chiếu kỳ vọng theo loại hoạt động
(DATN engineering: cơ bản · DATN research-oriented: khá · NCKH: bắt buộc tốt · advanced B6/AB-R: rất tốt).

## Next actions

| Task | Owner | Evidence bắt buộc | Tiêu chí nghiệm thu | Deadline | Ưu tiên |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

---
*Nguồn chuẩn của rubric: `06_Data/readiness_rubrics.json`. Nguồn chuẩn của MVT/prerequisite: `06_Data/project_portfolio.json`.
File này là hồ sơ, không phải nguồn chuẩn — không sao chép định nghĩa rubric vào đây.*
