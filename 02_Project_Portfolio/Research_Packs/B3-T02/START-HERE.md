# START HERE — B3-T02

**Engineering & Research Mentoring Program (Lucero)** · ThS. Đinh Văn Nam (Mr. Lucero Dinh) — Khoa Điện–Điện tử, Trường Kỹ thuật, Đại học Phenikaa

> **File sinh tự động** từ `06_Data/research_packs.json` bằng `scripts/generate_research_packs.py`. Sửa tay sẽ bị ghi đè — muốn đổi nội dung thì sửa JSON rồi chạy lại script.

**Đề tài:** Tối ưu fixed-point cho SC Polar decoder  
**English:** Fixed-Point Optimization of an SC Polar Decoder  
**Tên đầy đủ khi đăng ký:** Tối ưu biểu diễn fixed-point cho bộ giải mã Polar Successive Cancellation theo ràng buộc phần cứng  
**Mã đối chiếu gói gốc:** T06 · **Track C** — Kiến trúc bộ giải mã Polar

---

## Câu hỏi nghiên cứu

> Có thể giảm precision của LLR/processing trong SC decoder tới mức nào mà BLER degradation nhỏ trong khi hardware cost giảm đáng kể?

Đây là câu em phải trả lời được bằng **bằng chứng**, không phải bằng một bản cài đặt chạy được.

## Trước khi gõ dòng code đầu tiên — phải đọc

- SC baseline
- LLR dynamic range
- fixed-point quantization
- saturation/rounding
- quantized decoders
- FPGA PPA

Tài liệu cụ thể xem `09_References/READING-LIST.md`. Sau mỗi tài liệu, trả lời 10 câu trong `READING-QUESTIONS` ở cuối file này.

## Phải hiểu được (không nhìn tài liệu)

- where quantization error enters SC
- integer/fractional allocation
- saturation vs wrap-around
- BLER sensitivity to precision
- fair floating/fixed comparison

## Phải dựng

- floating SC reference
- quantized SC model
- parameterized fixed-point RTL
- bit-exact co-verification
- sweep scripts

## Phải chạy thí nghiệm

- total-bit sweep
- fractional/integer split sweep
- rounding/saturation study
- BLER vs Eb/N0
- resource/fmax/power vs precision

## Bằng chứng bắt buộc nộp

- floating vs fixed BLER curves
- quantization error diagnostics
- bit-exact logs
- hardware cost table
- accuracy–cost Pareto plot

## Khi nào mới đủ điều kiện nghĩ tới một bài báo

Có quantization design-space study, statistically reliable BLER, hardware evaluation và một precision strategy/Pareto point có lý do rõ.

Tiềm năng công bố mentor đánh giá cho đề tài này: **Cao**. Đây là ước lượng ban đầu, không phải lời hứa — quyết định thật nằm ở Gate G7.

## Bốn câu mentor sẽ hỏi đi hỏi lại

1. Vì sao chọn range này?
2. BLER loss được đo tại những SNR nào?
3. Có overflow âm thầm không?
4. Bit-width tối ưu có ổn định theo N/K/SNR không?

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
