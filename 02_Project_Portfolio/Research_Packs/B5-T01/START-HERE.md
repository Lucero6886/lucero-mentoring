# START HERE — B5-T01

**Engineering & Research Mentoring Program (Lucero)** · ThS. Đinh Văn Nam (Mr. Lucero Dinh) — Khoa Điện–Điện tử, Trường Kỹ thuật, Đại học Phenikaa

> **File sinh tự động** từ `06_Data/research_packs.json` bằng `scripts/generate_research_packs.py`. Sửa tay sẽ bị ghi đè — muốn đổi nội dung thì sửa JSON rồi chạy lại script.

**Đề tài:** Phát hiện frame không tin cậy cho adaptive Polar decoding  
**English:** Unreliable-Frame Detection for Adaptive Polar Decoding  
**Tên đầy đủ khi đăng ký:** Phát hiện frame không tin cậy cho giải mã Polar thích ứng dựa trên đặc trưng độ tin cậy  
**Mã đối chiếu gói gốc:** T09 · **Track D** — Giải mã Polar thích ứng / hỗ trợ neural

---

## Câu hỏi nghiên cứu

> Có thể nhận biết sớm frame SC có nguy cơ sai bằng một detector độ phức tạp thấp để tránh kích hoạt enhanced decoding trên mọi frame hay không?

Đây là câu em phải trả lời được bằng **bằng chứng**, không phải bằng một bản cài đặt chạy được.

## Trước khi gõ dòng code đầu tiên — phải đọc

- SC reliability outputs
- binary classification metrics
- ROC/PR curves
- threshold detector
- feature engineering
- selective/adaptive decoding concepts

Tài liệu cụ thể xem `09_References/READING-LIST.md`. Sau mỗi tài liệu, trả lời 10 câu ở cuối file này.

## Phải hiểu được (không nhìn tài liệu)

- frame label definition
- false positive vs false negative
- class imbalance
- AUC vs operating point
- activation rate
- why detector accuracy alone is insufficient

## Phải dựng

- dataset generator from SC
- feature extractor
- threshold/rule baseline
- evaluation pipeline
- optional simple statistical classifier

## Phải chạy thí nghiệm

- feature distribution correct vs error frames
- ROC/PR
- threshold sweep
- activation rate vs miss rate
- end-to-end BLER when coupled to oracle/enhanced path

## Bằng chứng bắt buộc nộp

- dataset manifest
- feature histograms
- ROC/PR plots
- confusion matrix
- activation/BLER trade-off

## Khi nào mới đủ điều kiện nghĩ tới một bài báo

Detector phải tạo end-to-end benefit: giảm activation/average cost trong khi BLER gần target; có baseline, sensitivity và no-leakage validation.

Tiềm năng công bố mentor đánh giá cho đề tài này: **Cao**. Đây là ước lượng ban đầu, không phải lời hứa — quyết định thật nằm ở Gate G7.

## Bốn câu mentor sẽ hỏi đi hỏi lại

1. Label có leakage không?
2. Feature này có sẵn trước khi quyết định activate không?
3. False negative gây hậu quả gì?
4. Operating point nào tối ưu cho decoder chứ không chỉ classifier?

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

*Trang tổng quan đề tài: [`Topic_Guides/B5/B5-T01.md`](../../Topic_Guides/B5/B5-T01.md) · Lộ trình: `ROADMAP.md` · Cửa: `MILESTONE-GATES.md` · Thí nghiệm: `EXPERIMENTS.md`*
