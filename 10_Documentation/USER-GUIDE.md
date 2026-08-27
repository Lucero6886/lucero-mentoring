# USER-GUIDE — dùng bộ hồ sơ này thế nào

Trang vào việc. Mỗi mục trỏ tới tài liệu chi tiết, không lặp lại nội dung.

---

## Bạn là ai, đọc gì

| Bạn là | Bắt đầu ở |
|---|---|
| Mentor, lần đầu mở dự án | `implementation-notes.md` mục ★ ("Hiểu bản chất hệ thống trong 10 phút") |
| Mentor, cần thao tác hằng tuần | `10_Documentation/MENTOR-GUIDE.md` |
| Sinh viên | `10_Documentation/STUDENT-GUIDE.md` |
| Người sửa dữ liệu/script | `10_Documentation/WORKFLOW.md` |
| Phiên Claude/AI | `CLAUDE.md` rồi `05_Claude/CLAUDE_PROJECT_CONTEXT.md` |

## Hai thư mục — đừng gộp

- **`EEE Projects`** (thư mục này) = **dự án tổng**: nguồn chuẩn 105 đề tài P/I/T/R, script, governance,
  operations, template, website. **Mọi chỉnh sửa nội dung diễn ra ở đây.**
- **`DATN_mentor`** = **dự án con**: chỉ giữ tài liệu phát hành cho cohort DATN HK1 2026-2027.

## Bốn nhóm A/B và mã đề tài

Nhóm **A** = phần cứng số: PCB → RTL → FPGA → ASIC (family A0–A5).
Nhóm **B** = giải mã Polar Code (family B0–B6). **AB** = giao thoa hai nhóm.

Mã chuẩn dạng `<Family>-<Type><NN>`, vd `A4-T01`. Type: **P** project môn học · **I** thực tập ·
**T** đồ án tốt nghiệp · **R** nghiên cứu khoa học. Mã ngắn (A1…B12) chỉ để đọc nhanh trong kỳ —
**mọi hồ sơ ghi mã chuẩn**.

## MVT là gì

**MVT** (Minimum Viable Thesis) = phần lõi bắt buộc, đủ để đồ án đạt chuẩn kỹ thuật.
**Research Extension** = phần mở rộng, **không bắt buộc**, chỉ mở khi qua Gate 2 đúng hạn.
Hai phần luôn tách bạch trong Project Charter.

## Sáu gate

Gate 1 Problem & Foundation (T1–2) · Gate 2 Baseline (T3–5) · Gate 3 Core Implementation (T6–8) ·
Gate 4 Experiments (T9–11) · Gate 5 Analysis & Draft (T12–13) · Gate 6 Reproducibility & Defense (T14–15).

Hai luật cứng: **trượt Gate 2 → extension đóng** · **trượt Gate 3 → thu nhỏ đề tài**.
Ngày cụ thể của từng cohort nằm trong `06_Data/cohort_<id>.json`.

## Việc thường làm — tìm ở đâu

| Việc | Xem |
|---|---|
| Giao đề tài cho SV mới | MENTOR-GUIDE §1 |
| Chạy buổi review hằng tuần | MENTOR-GUIDE §2 |
| SV chậm tiến độ | MENTOR-GUIDE §3 |
| Chạy gate review | MENTOR-GUIDE §4 |
| Mở research extension | MENTOR-GUIDE §6 + `04_Project_Template/EXTENSION_PROPOSAL_TEMPLATE.md` |
| Chuẩn bị bảo vệ | MENTOR-GUIDE §7 + `THESIS_REVIEW_CHECKLIST.md` + `DEFENSE_QUESTIONS.md` |
| Thêm/sửa một đề tài | WORKFLOW §4 |
| Regenerate mọi tài liệu | WORKFLOW §3 |
| Mở cohort kỳ sau | WORKFLOW §5 |
| Đóng gói bản phát hành | `python3 scripts/build_release.py` |

## Hồ sơ sinh viên nằm ở đâu

**Bản tổng hợp:** `03_Operations/Mentoring_Management_Workbook.xlsx` — 8 sheet,
trong đó `Students` là màn hình trạng thái 1 phút, `Weekly_Status` là nhật ký tuần, `Milestones` là 6 gate mỗi SV.

**Bản chi tiết từng SV:** thư mục project tạo từ `04_Project_Template/` —
`STUDENT_PROFILE.md` · `EVIDENCE_LEDGER.md` · `DECISION_LOG.md` · `PROJECT_CHARTER_TEMPLATE.md` · weekly report.

> **Có dữ liệu thật (tên, email, điểm, cảnh báo) → lưu vào `07_Private/`.**
> `.gitignore` đã chặn thư mục này. Không gửi cho SV, không đưa lên repo public,
> không đưa vào công cụ AI ngoài khi chưa được phép.

## Bảng theo dõi cohort

Sheet `Dashboard` + `Students` của workbook trả lời: ai ON_TRACK / AT_RISK / OFF_TRACK / BLOCKED ·
ai chưa qua Gate 2 · ai đang mở extension · ai cần oral check · ai quá hạn evidence · ai cần can thiệp tuần này.

## Tài liệu hệ thống

`implementation-notes.md` (+ `.html`) — 23 mục: nguồn chuẩn, kiến trúc, mô hình dữ liệu, từng script,
quyết định thiết kế kèm phương án đã loại, hạn chế, tồn đọng, 9 quy trình vận hành.
Đây là nơi trả lời *"vì sao hệ thống được làm như vậy"*.
