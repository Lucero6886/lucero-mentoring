# START HERE — B4-T02

**Engineering & Research Mentoring Program (Lucero)** · ThS. Đinh Văn Nam (Mr. Lucero Dinh) — Khoa Điện–Điện tử, Trường Kỹ thuật, Đại học Phenikaa

> **File sinh tự động** từ `06_Data/research_packs.json` bằng `scripts/generate_research_packs.py`. Sửa tay sẽ bị ghi đè — muốn đổi nội dung thì sửa JSON rồi chạy lại script.

**Đề tài:** Reliability-based candidate ranking cho SC-Flip  
**English:** Reliability-Based Candidate Ranking for SC-Flip Polar Decoding  
**Tên đầy đủ khi đăng ký:** Nghiên cứu phương pháp xếp hạng ứng viên dựa trên độ tin cậy cho bộ giải mã Polar SC-Flip  
**Mã đối chiếu gói gốc:** T08 · **Track C** — Kiến trúc bộ giải mã Polar

---

## Câu hỏi nghiên cứu

> Có thể dùng thông tin độ tin cậy tốt hơn |LLR| đơn thuần để tăng xác suất đưa true error vào top-k candidate và giảm số lần SC-Flip retry hay không?

Đây là câu em phải trả lời được bằng **bằng chứng**, không phải bằng một bản cài đặt chạy được.

## Trước khi gõ dòng code đầu tiên — phải đọc

- SCF candidate metrics
- LLR reliability
- error propagation
- ranking metrics
- top-k evaluation
- complexity-aware algorithm design

Tài liệu cụ thể xem `09_References/READING-LIST.md`. Sau mỗi tài liệu, trả lời 10 câu trong `READING-QUESTIONS` ở cuối file này.

## Phải hiểu được (không nhìn tài liệu)

- ranking vs classification
- candidate-hit rate
- top-k accuracy
- why low |LLR| may not equal true first error
- metric cost

## Phải dựng

- failed-frame data collector
- candidate feature extractor
- baseline |LLR| ranking
- proposed handcrafted metric
- SCF integration

## Phải chạy thí nghiệm

- Top-1/3/5 hit rate
- BLER vs SNR
- average attempts
- metric complexity
- sensitivity to candidate pool/Tmax

## Bằng chứng bắt buộc nộp

- ranking accuracy table
- BLER curves
- attempt reduction
- failure examples
- operation-count/hardware-cost estimate

## Khi nào mới đủ điều kiện nghĩ tới một bài báo

Có ranking improvement ổn định, end-to-end SCF benefit, complexity analysis và ablation/interpretation rõ.

Tiềm năng công bố mentor đánh giá cho đề tài này: **Cao**. Đây là ước lượng ban đầu, không phải lời hứa — quyết định thật nằm ở Gate G7.

## Bốn câu mentor sẽ hỏi đi hỏi lại

1. Metric mới dùng thông tin nào mà |LLR| không có?
2. Improvement có còn khi candidate pool thay đổi?
3. Ranking tốt hơn có thực sự cải thiện BLER/latency?
4. Overhead của metric có ăn hết lợi ích không?

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

*Lộ trình từng tuần: `ROADMAP.md` · Điều kiện qua từng cửa: `MILESTONE-GATES.md` · Thí nghiệm: `EXPERIMENTS.md`*
