# Research Extension Proposal — <MÃ_ĐỀ_TÀI> · <HỌ TÊN>

> Cổng mở phần mở rộng nghiên cứu (MASTER_PROMPT §13).
> **Mặc định `CLOSED`.** Không ai được bắt đầu extension trước khi phiếu này được mentor duyệt.
> Chính sách gốc: `01_Governance/Master_Mentoring_Handbook.docx` §11 · quy trình: `implementation-notes.md` §18.

## Phần 1 — Tám điều kiện tiên quyết (mentor tick, thiếu một là chưa mở)

- [ ] Baseline đã kiểm chứng — Gate 2 `PASS`, có evidence id: ______
- [ ] Core implementation ổn định
- [ ] Lịch còn dư địa (thường nghĩa là trước tuần 9)
- [ ] Câu hỏi nghiên cứu rõ ràng
- [ ] Giả thuyết hoặc mục tiêu so sánh rõ ràng
- [ ] Metric quyết định kết quả đã định nghĩa
- [ ] Sinh viên thể hiện research ownership (đối chiếu RR trong `STUDENT_PROFILE.md`)
- [ ] **Extension thất bại không phá vỡ tính hợp lệ của DATN core**

Điều cuối là quan trọng nhất: nếu extension hỏng mà đồ án hỏng theo, thì đó không phải extension — đó là scope đã phình ra thành lõi.

## Phần 2 — Bảy câu sinh viên phải trả lời

**1. Câu hỏi nghiên cứu là gì?**
> Một câu, trả lời được bằng thực nghiệm. Không phải "cải thiện hiệu năng".

**2. Baseline là gì?**
> Cụ thể tới mức cấu hình: thuật toán, tham số, N/K, điều kiện synthesis…

**3. Cái gì thay đổi?**
> Đúng một biến, hoặc một nhóm biến có lý do đi cùng nhau.

**4. Cái gì được giữ cố định?**
> Seed, dataset, kênh, ràng buộc timing, số frame, tiêu chí dừng…

**5. Metric nào quyết định kết quả?**
> Nêu cả ngưỡng: bao nhiêu thì coi là cải thiện thật, chứ không phải nhiễu.

**6. Evidence nào có thể BÁC BỎ giả thuyết?**
> Bắt buộc trả lời. Không nêu được điều kiện bác bỏ thì đây chưa phải câu hỏi nghiên cứu.

**7. Fallback nếu extension thất bại?**
> Kết quả âm vẫn có giá trị nếu thí nghiệm công bằng — nêu rõ sẽ báo cáo thế nào.

## Phần 3 — Riêng đề tài ML-assisted (family B6)

- [ ] Có heuristic/classical baseline tương ứng để so sánh
- [ ] Train/validation/test tách bạch, đã kiểm rò rỉ dữ liệu
- [ ] Seed và cấu hình được ghi lại đủ để tái lập
- [ ] Chi phí tính toán/phần cứng của mô hình được đo, không chỉ đo độ chính xác

**Không chấp nhận kết quả neural nếu thiếu so sánh baseline.** Đây là invariant, không phải khuyến nghị.

## Phần 4 — Quyết định của mentor

| Mục | Nội dung |
|---|---|
| Ngày xét |  |
| Gate hiện tại |  |
| Kết luận | ☐ MỞ extension ☐ MỞ có điều kiện ☐ CHƯA mở ☐ TỪ CHỐI |
| Điều kiện kèm theo |  |
| Ngày rà lại |  |
| Lý do |  |

→ Ghi kết quả thành một dòng trong `DECISION_LOG.md`. Extension đã mở vẫn có thể bị **đóng băng** nếu core tụt tiến độ.

Mentor: ______________________  Sinh viên: ______________________  Ngày: ____/____/______
