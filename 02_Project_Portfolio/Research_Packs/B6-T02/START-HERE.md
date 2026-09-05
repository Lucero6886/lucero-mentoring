# START HERE — B6-T02

**Engineering & Research Mentoring Program (Lucero)** · ThS. Đinh Văn Nam (Mr. Lucero Dinh) — Khoa Điện–Điện tử, Trường Kỹ thuật, Đại học Phenikaa

> **File sinh tự động** từ `06_Data/research_packs.json` bằng `scripts/generate_research_packs.py`. Sửa tay sẽ bị ghi đè — muốn đổi nội dung thì sửa JSON rồi chạy lại script.

**Đề tài:** Neural-assisted candidate ranking cho SC-Flip Polar decoder  
**English:** Lightweight Neural-Assisted Candidate Ranking for SC-Flip Polar Decoding  
**Tên đầy đủ khi đăng ký:** Xếp hạng ứng viên hỗ trợ mạng neural nhẹ cho bộ giải mã Polar SC-Flip  
**Mã đối chiếu gói gốc:** T13 · **Track D** — Giải mã Polar thích ứng / hỗ trợ neural

---

## Câu hỏi nghiên cứu

> Một learned lightweight ranking function có thể đưa true error lên top-k tốt hơn heuristic reliability và giảm average SC-Flip retries với overhead chấp nhận được hay không?

Đây là câu em phải trả lời được bằng **bằng chứng**, không phải bằng một bản cài đặt chạy được.

## Trước khi gõ dòng code đầu tiên — phải đọc

- T07–T08 SCF
- ranking/classification basics
- learning-to-rank intuition
- feature engineering
- small neural networks
- quantization/hardware cost

Tài liệu cụ thể xem `09_References/READING-LIST.md`. Sau mỗi tài liệu, trả lời 10 câu ở cuối file này.

## Phải hiểu được (không nhìn tài liệu)

- label definition for candidate ranking
- first-error vs propagated error
- top-k metric
- dataset leakage
- end-to-end ranking utility
- overhead vs saved retries

## Phải dựng

- failed-frame candidate dataset
- |LLR| baseline
- handcrafted reliability baseline
- simple learned baseline
- tiny NN ranker
- SCF integration

## Phải chạy thí nghiệm

- Top-1/3/5
- BLER
- average attempts
- model-size sweep
- feature ablation
- quantization
- operation/latency cost

## Bằng chứng bắt buộc nộp

- ranking table
- BLER curve
- attempt histogram
- ablation
- model complexity
- hardware-aware net saving estimate

## Khi nào mới đủ điều kiện nghĩ tới một bài báo

NN ranking phải cải thiện top-k và end-to-end SCF cost/performance ổn định; có strong heuristic baseline, ablation, quantization và net-complexity analysis.

Tiềm năng công bố mentor đánh giá cho đề tài này: **Rất cao, kèm rủi ro cao**. Đây là ước lượng ban đầu, không phải lời hứa — quyết định thật nằm ở Gate G7.

## Bốn câu mentor sẽ hỏi đi hỏi lại

1. Label nào thực sự cần rank?
2. Ranking accuracy tăng có giảm retries không?
3. NN có thắng handcrafted metric ở nhiều SNR/N không?
4. Net cost sau NN overhead là bao nhiêu?

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

*Trang tổng quan đề tài: [`02_Project_Portfolio/Topic_Guides/B6/B6-T02.md`](../../Topic_Guides/B6/B6-T02.md) · Lộ trình: `ROADMAP.md` · Cửa: `MILESTONE-GATES.md` · Thí nghiệm: `EXPERIMENTS.md`*
