# Nội dung đăng ký đề tài — B5-T01

**Engineering & Research Mentoring Program (Lucero)** · ThS. Đinh Văn Nam (Mr. Lucero Dinh) — Khoa Điện–Điện tử, Trường Kỹ thuật, Đại học Phenikaa

> **File sinh tự động** từ `06_Data/research_packs.json` bằng `scripts/generate_research_packs.py`. Sửa tay sẽ bị ghi đè — muốn đổi nội dung thì sửa JSON rồi chạy lại script.

**Đề tài:** Phát hiện frame không tin cậy cho adaptive Polar decoding  
**English:** Unreliable-Frame Detection for Adaptive Polar Decoding  
**Tên đầy đủ khi đăng ký:** Phát hiện frame không tin cậy cho giải mã Polar thích ứng dựa trên đặc trưng độ tin cậy  
**Mã đối chiếu gói gốc:** T09 · **Track D** — Giải mã Polar thích ứng / hỗ trợ neural

---

> Dùng để điền vào biểu mẫu đăng ký của Khoa/Trường. Nội dung sinh từ dữ liệu gốc nên không lệch với danh mục.

## Tên đề tài

**Phát hiện frame không tin cậy cho giải mã Polar thích ứng dựa trên đặc trưng độ tin cậy**

**English:** Reliability-Based Unreliable-Frame Detection for Adaptive Polar Decoding

_Mã trong danh mục: `B5-T01` — Phát hiện frame không tin cậy cho adaptive Polar decoding_

## Mục tiêu nghiên cứu

- Làm rõ và kiểm chứng câu hỏi nghiên cứu: Có thể nhận biết sớm frame SC có nguy cơ sai bằng một detector độ phức tạp thấp để tránh kích hoạt enhanced decoding trên mọi frame hay không?
- Xây dựng và triển khai: dataset generator from SC.
- Xây dựng và triển khai: feature extractor.
- Xây dựng và triển khai: threshold/rule baseline.
- Xây dựng và triển khai: evaluation pipeline.
- Xây dựng và triển khai: optional simple statistical classifier.
- Thực hiện đánh giá có kiểm soát theo các thí nghiệm trọng tâm: feature distribution correct vs error frames, ROC/PR, threshold sweep.
- Đánh giá kết quả bằng chỉ số định lượng, bảo đảm khả năng tái lập và phân tích giới hạn.
- Phát triển năng lực đọc tài liệu, thiết kế thí nghiệm, kiểm chứng, phân tích và viết báo cáo khoa học.

## Dự kiến sản phẩm, kết quả

- Repository mã nguồn/thiết kế, cấu hình và hướng dẫn tái lập.
- dataset manifest
- feature histograms
- ROC/PR plots
- confusion matrix
- activation/BLER trade-off
- Báo cáo và slide trình bày.
- Teaching Transfer Note để tái sử dụng trong đào tạo.
- Phấn đấu hoàn thiện bản thảo bài báo nếu đạt cửa G7.

## Dự kiến tham gia giải thưởng nghiên cứu khoa học sinh viên

- Hội nghị sinh viên nghiên cứu khoa học cấp Khoa/Trường.
- Các giải thưởng nghiên cứu khoa học sinh viên cấp Trường/Bộ hoặc cuộc thi học thuật chuyên ngành phù hợp.
- Kết quả đạt chất lượng được định hướng hoàn thiện thành bài báo hội nghị/tạp chí; **không cam kết công bố trước khi đạt cửa G7**.

## Ghi chú định hướng công bố

Detector phải tạo end-to-end benefit: giảm activation/average cost trong khi BLER gần target; có baseline, sensitivity và no-leakage validation.
