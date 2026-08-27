# Hướng dẫn cho mentor

**Engineering & Research Mentoring Program (Lucero)** · ThS. Đinh Văn Nam (Mr. Lucero Dinh)

Trang này là bản thao tác: mở ra, làm theo. Lý thuyết đằng sau nằm ở `01_Governance/Master_Mentoring_Handbook.docx`;
kiến trúc hệ thống nằm ở `implementation-notes.md`. **Không lặp lại nội dung hai file đó ở đây.**

---

## 1. Giao đề tài

1. **Thu Phiếu 1–3** — thông tin, Top-3 nguyện vọng (**mã chuẩn**, vd `A4-T01`), TR tự chấm, cam kết giờ/tuần.
2. **Giao readiness test** (Phiếu 4): literature task + technical mini-task 4–10h + oral check 5–10 phút.
   Chọn mini-task chạm đúng prerequisite quan trọng nhất của đề tài Top-1 — không phải một bài tập chung chung.
3. **Chấm Phiếu 5**: WR /20 · RR /20 + nhận định · TR **đã kiểm chứng bằng mini-task** · Level của SV.
4. **Đối chiếu prerequisite**: mở đề tài trong danh mục, đọc dòng *"Đầu vào … (mã tham chiếu: …)"*.
   Mã có dấu `*` (vd `A1-P*`) nghĩa là *"ít nhất một đề tài loại P của family A1, hoặc năng lực tương đương **có evidence**"*.
5. **Đối chiếu level**: `min_level` của đề tài là **sàn**. SV dưới sàn mà vẫn nhận → ghi lý do vào `DECISION_LOG.md`.
6. **Kết luận**: Nhận / Nhận có điều kiện / Đổi scope-đề tài / Chưa nhận.

> **Interest là nguyện vọng — readiness quyết định scope.** Không xác nhận đề tài advanced trước khi có evidence.
> Ngưỡng WR là gợi ý, mentor được override — nhưng phải ghi lý do.

**Onboarding tuần 1:** ký Working Agreement · tạo thư mục project từ `04_Project_Template/` ·
chép `checkpoints_15w` của đề tài vào Project Charter · chốt **MVT và Extension tách biệt** · đăng charter ·
nhập sheet `Students` + `Readiness` + 6 dòng `Milestones` trong workbook.

## 2. Nhịp một tuần

| Lúc | Việc |
|---|---|
| Trước buổi gặp | SV nộp Weekly Report. Mentor skim, đánh dấu blocker/decision cần xử lý. *Không đọc lại chat để đoán tiến độ.* |
| Trong buổi gặp | SV trình: **Goal → Evidence → Failure → Diagnosis → Đã thử gì → Đề xuất bước tiếp → Câu hỏi**. Mentor teach-back để xác nhận hiểu, không hỏi "em hiểu chưa?" |
| Cuối buổi | Chốt **1–3** deliverable + deadline thực tế. Gán risk Green/Yellow/Red. |
| Sau buổi | Ghi decision/scope change vào workbook (`Weekly_Status` + `Milestones`). *Mentor không giữ task trong trí nhớ.* |

**Kiểm tra dưới 1 phút mỗi sáng thứ Hai:** mở workbook → sheet `Students` → 4 cột `Risk`, `Last Evidence`,
`Next Deliverable`, `Next Deadline`. Ai Yellow/Red hoặc evidence quá 7 ngày → mở `Weekly_Status` của SV đó.

**Bảy câu rà trong buổi gặp** — và dấu hiệu cần chú ý:

| Hỏi | Dấu hiệu |
|---|---|
| Tuần trước chốt gì? | SV không nhớ → quy trình ghi chép hỏng |
| Cho xem evidence | Chỉ có lời nói → chưa có tiến độ |
| Cái gì không chạy? | "Mọi thứ ổn" nhiều tuần liền → nghi ngờ |
| Vì sao em nghĩ nó hỏng? | Không có giả thuyết → thiếu kỹ năng chẩn đoán, cần dạy |
| Đã thử gì để kiểm chứng? | Không thử gì → kiên trì (WR) thấp |
| Em đề xuất làm gì tiếp? | Hỏi ngược → chủ động (WR) thấp |
| Giải thích dòng code/hình bất kỳ | Không giải thích được → **task chưa đạt**, làm lại |

## 3. Khi sinh viên chậm

Chẩn đoán **ba biến** trước khi kết luận: *độ khó task × thời gian thực tế bỏ ra × cách học*.
Đừng mặc định là lười — thường là một trong ba biến lệch.

| Mức | Kích hoạt | Hành động |
|---|---|---|
| Nhắc | 1 chu kỳ thiếu update | Nhắn hỏi blocker, xác nhận lại deadline |
| Formal warning | 2 chu kỳ liên tiếp thiếu evidence | Warning + recovery plan ngắn có thời hạn |
| Scope review | Trượt Gate 2 hoặc 3 | Reduce scope, giữ chuẩn kỹ thuật |
| Dừng extension / chuyển track | Tiếp tục disengage sau warning + hỗ trợ | Theo quy định đơn vị; **không cứu ở phút cuối** |

**Thứ tự cắt khi reduce scope:** bỏ extension → giảm parameter sweep → giảm số kiến trúc → thu nhỏ subsystem.
**Không bao giờ cắt:** MVT, verification, reproducibility, ownership.

> Nếu thấy mình đang debug hộ một SV hàng giờ → sai nhịp. Quay lại thang cảnh báo.
> Phân bổ thời gian: common 50–60% · theme (nhóm A / nhóm B) 25–35% · individual 15–20%.

## 4. Chạy một gate review

1. Mở `Milestones` của SV, tìm dòng gate tới hạn — cột `Requirement` đã prefill từ `06_Data/milestone_gates.json`.
2. Đối chiếu evidence với `pass_criteria` — dùng đúng câu chữ trong nguồn, **không nới ngầm**.
3. Kết luận: `PASS` · `CONDITIONAL_PASS` (kèm điều kiện + hạn) · `FAIL` · `NOT_ENOUGH_EVIDENCE`.
4. Áp hard rule: Gate 2 trượt → **extension đóng** · Gate 3 trượt → **reduce scope** ·
   sau Gate 4 → không thêm thuật toán lớn · Gate 5 → không dùng viết lách che lỗ hổng ·
   Gate 6 → chỉ xác nhận hoàn thành khi **đủ cả ba**: technical + reproducibility + ownership.
5. Ghi Status/Evidence/Decision/Reviewed Date. Scope change phải cập nhật **cả** charter lẫn cột MVT sheet Students.

## 5. Kiểm tra evidence

Sổ cái từng SV: `EVIDENCE_LEDGER.md`. Mentor điền cột Trạng thái:
`SUBMITTED` → `VERIFIED` / `PARTIAL` / `REJECTED` / `SUPERSEDED`.

Ở Gate 5–6, mỗi claim định lượng trong báo cáo phải trỏ được về một dòng `VERIFIED`.
Claim không trỏ được → bỏ khỏi báo cáo hoặc hạ xuống mức phỏng đoán có ghi rõ.

## 6. Mở research extension

Dùng `04_Project_Template/EXTENSION_PROPOSAL_TEMPLATE.md`: 8 điều kiện tiên quyết + 7 câu hỏi.
Extension mặc định `CLOSED`. Điều kiện quan trọng nhất: **extension thất bại không được phá vỡ tính hợp lệ của DATN core.**

Riêng family B6 (neural-assisted): không chấp nhận kết quả neural nếu thiếu so sánh heuristic/classical.

## 7. Chuẩn bị bảo vệ và đóng kỳ

- Rà kỹ thuật: `THESIS_REVIEW_CHECKLIST.md` (phần chung + phần A digital IC hoặc phần B Polar).
- Ownership: `DEFENSE_QUESTIONS.md` — 10 câu Definition of Done + câu theo artifact + câu phản thực.
  Kết luận `UNCERTAIN` / `NEEDS_ORAL_CHECK` → **chưa xác nhận hoàn thành**.
- Reproducibility check: một người khác chạy lại từ hướng dẫn sạch, không hỏi miệng. Không pass = chưa xong.
- Gói bàn giao: `LEGACY_PACKAGE_CHECKLIST.md`, 11 mục.
- Sau bảo vệ: đánh giá nên mời SV tiếp NCKH hay chuyển hướng engineering/industry.
  *Không ép mọi SV thành researcher — hai đích đến ngang giá trị.*

## 8. Bootcamp chung

Nhiều SV cùng thiếu một prerequisite → dạy một lần cho cả nhóm thay vì giải thích 1:1 lặp lại.
Nhóm A: Git/GitHub · Linux/WSL · Verilog · simulation · debug waveform · synthesis · STA cơ bản · đo FPGA · ASIC flow.
Nhóm nhúng-IoT (A6/A7): C và toolchain nhúng · đọc datasheet ngoại vi · debug bằng logic analyzer · Git · RTOS cơ bản · MQTT và đo năng lượng · quy trình đo trên thiết bị thật.
Nhóm B: chuỗi truyền thông số · Polar encoding · SC decoding · BER/BLER · Eb/N0 · kỷ luật thí nghiệm · Python/MATLAB · thí nghiệm ngẫu nhiên tái lập được · fixed-point/LLR quantization.

**Bootcamp không tự động đổi scope cá nhân của ai.**

---
*Sửa nội dung hệ thống: xem `WORKFLOW.md`. Kiến trúc và quyết định thiết kế: `implementation-notes.md`.*
