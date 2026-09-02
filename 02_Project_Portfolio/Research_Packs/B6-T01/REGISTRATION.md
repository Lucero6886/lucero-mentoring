# Nội dung đăng ký đề tài — B6-T01

**Engineering & Research Mentoring Program (Lucero)** · ThS. Đinh Văn Nam (Mr. Lucero Dinh) — Khoa Điện–Điện tử, Trường Kỹ thuật, Đại học Phenikaa

> **File sinh tự động** từ `06_Data/research_packs.json` bằng `scripts/generate_research_packs.py`. Sửa tay sẽ bị ghi đè — muốn đổi nội dung thì sửa JSON rồi chạy lại script.

**Đề tài:** Lightweight neural-assisted unreliable-frame detector  
**English:** Lightweight Neural-Assisted Unreliable-Frame Detector  
**Tên đầy đủ khi đăng ký:** Thiết kế bộ phát hiện frame không tin cậy hỗ trợ mạng neural nhẹ cho giải mã Polar thích ứng  
**Mã đối chiếu gói gốc:** T12 · **Track D** — Giải mã Polar thích ứng / hỗ trợ neural

---

> Dùng để điền vào biểu mẫu đăng ký của Khoa/Trường. Nội dung sinh từ dữ liệu gốc nên không lệch với danh mục.

## Tên đề tài

**Thiết kế bộ phát hiện frame không tin cậy hỗ trợ mạng neural nhẹ cho giải mã Polar thích ứng**

**English:** Lightweight Neural-Assisted Unreliable-Frame Detection for Adaptive Polar Decoding

_Mã trong danh mục: `B6-T01` — Lightweight neural-assisted unreliable-frame detector_

## Mục tiêu nghiên cứu

- Làm rõ và kiểm chứng câu hỏi nghiên cứu: Một neural classifier rất nhỏ có thể cải thiện unreliable-frame detection đủ nhiều so với detector heuristic/statistical để justify phần cứng bổ sung hay không?
- Xây dựng và triển khai: dataset pipeline.
- Xây dựng và triển khai: threshold baseline.
- Xây dựng và triển khai: logistic/simple ML baseline.
- Xây dựng và triển khai: tiny MLP.
- Xây dựng và triển khai: quantized inference model.
- Xây dựng và triển khai: hardware-cost estimator.
- Thực hiện đánh giá có kiểm soát theo các thí nghiệm trọng tâm: threshold vs logistic vs tiny MLP, feature ablation, model-size sweep.
- Đánh giá kết quả bằng chỉ số định lượng, bảo đảm khả năng tái lập và phân tích giới hạn.
- Phát triển năng lực đọc tài liệu, thiết kế thí nghiệm, kiểm chứng, phân tích và viết báo cáo khoa học.

## Dự kiến sản phẩm, kết quả

- Repository mã nguồn/thiết kế, cấu hình và hướng dẫn tái lập.
- split manifest
- learning curves
- ROC/PR
- ablation table
- parameter/MAC/memory table
- end-to-end adaptive-decoder benefit
- Báo cáo và slide trình bày.
- Teaching Transfer Note để tái sử dụng trong đào tạo.
- Phấn đấu hoàn thiện bản thảo bài báo nếu đạt cửa G7.

## Dự kiến tham gia giải thưởng nghiên cứu khoa học sinh viên

- Hội nghị sinh viên nghiên cứu khoa học cấp Khoa/Trường.
- Các giải thưởng nghiên cứu khoa học sinh viên cấp Trường/Bộ hoặc cuộc thi học thuật chuyên ngành phù hợp.
- Kết quả đạt chất lượng được định hướng hoàn thiện thành bài báo hội nghị/tạp chí; **không cam kết công bố trước khi đạt cửa G7**.

## Ghi chú định hướng công bố

NN phải vượt simple baselines có ý nghĩa ở end-to-end decoder metric sau khi tính overhead; có ablation, quantization và complexity analysis.
