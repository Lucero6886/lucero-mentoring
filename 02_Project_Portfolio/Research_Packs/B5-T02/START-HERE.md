# START HERE — B5-T02

**Engineering & Research Mentoring Program (Lucero)** · ThS. Đinh Văn Nam (Mr. Lucero Dinh) — Khoa Điện–Điện tử, Trường Kỹ thuật, Đại học Phenikaa

> **File sinh tự động** từ `06_Data/research_packs.json` bằng `scripts/generate_research_packs.py`. Sửa tay sẽ bị ghi đè — muốn đổi nội dung thì sửa JSON rồi chạy lại script.

**Đề tài:** Adaptive decoder chỉ kích hoạt enhanced processing trên frame khó  
**English:** Adaptive Polar Decoding with Selective Enhanced Processing  
**Tên đầy đủ khi đăng ký:** Thiết kế bộ giải mã Polar thích ứng dựa trên độ tin cậy với cơ chế xử lý tăng cường có chọn lọc  
**Mã đối chiếu gói gốc:** T10 · **Track D** — Giải mã Polar thích ứng / hỗ trợ neural

---

## Câu hỏi nghiên cứu

> Selective enhanced processing có thể đạt BLER gần always-on enhanced decoder nhưng giảm average latency/operations/energy trên các frame dễ hay không?

Đây là câu em phải trả lời được bằng **bằng chứng**, không phải bằng một bản cài đặt chạy được.

## Trước khi gõ dòng code đầu tiên — phải đọc

- SC/SCF baseline
- reliability gating
- selective computation
- average-case complexity
- latency/energy accounting
- adaptive system evaluation

Tài liệu cụ thể xem `09_References/READING-LIST.md`. Sau mỗi tài liệu, trả lời 10 câu ở cuối file này.

## Phải hiểu được (không nhìn tài liệu)

- easy vs hard frame
- gate operating point
- always-on vs selective baseline
- average vs tail latency
- activation cost
- quality–cost trade-off

## Phải dựng

- SC baseline
- reliability gate
- enhanced decoder interface
- adaptive controller
- metrics logger

## Phải chạy thí nghiệm

- BLER vs SNR
- activation rate vs SNR
- average operations/latency
- threshold sensitivity
- oracle gate upper bound
- always-on enhanced comparison

## Bằng chứng bắt buộc nộp

- BLER plot
- activation plot
- average-cost table
- threshold Pareto curve
- failure/missed-hard-frame analysis

## Khi nào mới đủ điều kiện nghĩ tới một bài báo

Có clear adaptive gain: gần performance của enhanced baseline với giảm average cost đáng kể; có oracle/strong baselines và sensitivity.

Tiềm năng công bố mentor đánh giá cho đề tài này: **Rất cao**. Đây là ước lượng ban đầu, không phải lời hứa — quyết định thật nằm ở Gate G7.

## Bốn câu mentor sẽ hỏi đi hỏi lại

1. Gate biết gì tại thời điểm quyết định?
2. Savings đến từ đâu?
3. BLER gap với always-on là bao nhiêu?
4. Nếu SNR thay đổi, threshold có còn hợp lý?

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

*Trang tổng quan đề tài: [`02_Project_Portfolio/Topic_Guides/B5/B5-T02.md`](../../Topic_Guides/B5/B5-T02.md) · Lộ trình: `ROADMAP.md` · Cửa: `MILESTONE-GATES.md` · Thí nghiệm: `EXPERIMENTS.md`*
