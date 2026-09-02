# START HERE — B6-T01

**Engineering & Research Mentoring Program (Lucero)** · ThS. Đinh Văn Nam (Mr. Lucero Dinh) — Khoa Điện–Điện tử, Trường Kỹ thuật, Đại học Phenikaa

> **File sinh tự động** từ `06_Data/research_packs.json` bằng `scripts/generate_research_packs.py`. Sửa tay sẽ bị ghi đè — muốn đổi nội dung thì sửa JSON rồi chạy lại script.

**Đề tài:** Lightweight neural-assisted unreliable-frame detector  
**English:** Lightweight Neural-Assisted Unreliable-Frame Detector  
**Tên đầy đủ khi đăng ký:** Thiết kế bộ phát hiện frame không tin cậy hỗ trợ mạng neural nhẹ cho giải mã Polar thích ứng  
**Mã đối chiếu gói gốc:** T12 · **Track D** — Giải mã Polar thích ứng / hỗ trợ neural

---

## Câu hỏi nghiên cứu

> Một neural classifier rất nhỏ có thể cải thiện unreliable-frame detection đủ nhiều so với detector heuristic/statistical để justify phần cứng bổ sung hay không?

Đây là câu em phải trả lời được bằng **bằng chứng**, không phải bằng một bản cài đặt chạy được.

## Trước khi gõ dòng code đầu tiên — phải đọc

- T09 detector
- basic classification
- logistic regression
- small MLP
- feature normalization
- quantization-aware inference
- hardware cost of neural inference

Tài liệu cụ thể xem `09_References/READING-LIST.md`. Sau mỗi tài liệu, trả lời 10 câu trong `READING-QUESTIONS` ở cuối file này.

## Phải hiểu được (không nhìn tài liệu)

- why neural model is justified only after simple baseline
- train/val/test split
- data leakage
- class imbalance
- calibration/operating point
- MAC/parameter cost

## Phải dựng

- dataset pipeline
- threshold baseline
- logistic/simple ML baseline
- tiny MLP
- quantized inference model
- hardware-cost estimator

## Phải chạy thí nghiệm

- threshold vs logistic vs tiny MLP
- feature ablation
- model-size sweep
- quantization sweep
- ROC/PR
- end-to-end activation/BLER/average-cost

## Bằng chứng bắt buộc nộp

- split manifest
- learning curves
- ROC/PR
- ablation table
- parameter/MAC/memory table
- end-to-end adaptive-decoder benefit

## Khi nào mới đủ điều kiện nghĩ tới một bài báo

NN phải vượt simple baselines có ý nghĩa ở end-to-end decoder metric sau khi tính overhead; có ablation, quantization và complexity analysis.

Tiềm năng công bố mentor đánh giá cho đề tài này: **Rất cao**. Đây là ước lượng ban đầu, không phải lời hứa — quyết định thật nằm ở Gate G7.

## Bốn câu mentor sẽ hỏi đi hỏi lại

1. NN học được gì mà feature threshold không làm được?
2. Có leakage giữa train/test theo frame/SNR không?
3. AUC tăng có chuyển thành decoder gain không?
4. Quantization có làm mất lợi thế không?

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
