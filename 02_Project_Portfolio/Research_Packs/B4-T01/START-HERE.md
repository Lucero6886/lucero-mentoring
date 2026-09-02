# START HERE — B4-T01

**Engineering & Research Mentoring Program (Lucero)** · ThS. Đinh Văn Nam (Mr. Lucero Dinh) — Khoa Điện–Điện tử, Trường Kỹ thuật, Đại học Phenikaa

> **File sinh tự động** từ `06_Data/research_packs.json` bằng `scripts/generate_research_packs.py`. Sửa tay sẽ bị ghi đè — muốn đổi nội dung thì sửa JSON rồi chạy lại script.

**Đề tài:** Thiết kế và đánh giá SC-Flip Polar decoder  
**English:** Design and Performance Evaluation of SC-Flip Polar Decoding  
**Tên đầy đủ khi đăng ký:** Thiết kế và đánh giá bộ giải mã Polar SC-Flip hướng đến triển khai phần cứng  
**Mã đối chiếu gói gốc:** T07 · **Track C** — Kiến trúc bộ giải mã Polar

---

## Câu hỏi nghiên cứu

> SC-Flip cải thiện BLER của SC với trade-off average/worst-case latency và complexity như thế nào khi hướng tới phần cứng?

Đây là câu em phải trả lời được bằng **bằng chứng**, không phải bằng một bản cài đặt chạy được.

## Trước khi gõ dòng code đầu tiên — phải đọc

- SC decoding
- first-error phenomenon
- SC-Flip literature
- CRC/check mechanism if used
- candidate selection
- average vs worst-case latency

Tài liệu cụ thể xem `09_References/READING-LIST.md`. Sau mỗi tài liệu, trả lời 10 câu ở cuối file này.

## Phải hiểu được (không nhìn tài liệu)

- why flipping may recover a frame
- true first error vs propagated errors
- retry mechanism
- Tmax
- average attempts
- hardware reuse opportunities

## Phải dựng

- SCF software baseline
- candidate selector
- retry controller model
- optional RTL controller integration

## Phải chạy thí nghiệm

- BLER vs SNR
- Tmax sweep
- average attempts vs SNR
- latency distribution
- comparison SC/SCF/strong baseline where feasible

## Bằng chứng bắt buộc nộp

- BLER curves
- attempt histogram
- average/worst latency table
- candidate-hit diagnostics
- complexity accounting

## Khi nào mới đủ điều kiện nghĩ tới một bài báo

Có strong baseline, BLER–latency/complexity trade-off rõ, không chỉ reproduce algorithm; tốt hơn nếu có hardware-oriented modification/analysis.

Tiềm năng công bố mentor đánh giá cho đề tài này: **Trung bình – cao**. Đây là ước lượng ban đầu, không phải lời hứa — quyết định thật nằm ở Gate G7.

## Bốn câu mentor sẽ hỏi đi hỏi lại

1. SCF sửa first error hay mọi error?
2. Average complexity có ý nghĩa gì so với worst case?
3. Tmax tăng đem lại diminishing returns khi nào?
4. SCF có lợi phần cứng hơn SCL ở giả định nào?

Nếu tuần nào em cũng trả lời được bốn câu này bằng bằng chứng của chính mình, đề tài đang đi đúng.

## Bốn quy tắc không thương lượng

1. Không có baseline thì không có phương pháp đề xuất.
2. Không có bằng chứng thì không có kết luận.
3. Không tái lập được thì đề tài chưa hoàn thành ở mức nghiên cứu.
4. Không so sánh công bằng thì không được tuyên bố trong bài báo.

## READING-QUESTIONS — trả lời sau mỗi tài liệu

1. Bài này giải quyết vấn đề gì?
2. Baseline của họ là gì?
3. Giả định nào là quan trọng?
4. Họ dùng metric nào?
5. Kết quả chính là gì?
6. Giới hạn của bài là gì?
7. Phần nào tái lập được?
8. Phần nào liên quan trực tiếp tới câu hỏi nghiên cứu của em?
9. Có kết luận nào cần kiểm chứng độc lập không?
10. Nếu chỉ lấy được một insight cho đề tài, đó là gì?

---

*Trang tổng quan đề tài: [`Topic_Guides/B4/B4-T01.md`](../../Topic_Guides/B4/B4-T01.md) · Lộ trình: `ROADMAP.md` · Cửa: `MILESTONE-GATES.md` · Thí nghiệm: `EXPERIMENTS.md`*
