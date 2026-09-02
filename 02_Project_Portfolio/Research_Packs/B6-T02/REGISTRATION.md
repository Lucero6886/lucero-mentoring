# Nội dung đăng ký đề tài — B6-T02

**Engineering & Research Mentoring Program (Lucero)** · ThS. Đinh Văn Nam (Mr. Lucero Dinh) — Khoa Điện–Điện tử, Trường Kỹ thuật, Đại học Phenikaa

> **File sinh tự động** từ `06_Data/research_packs.json` bằng `scripts/generate_research_packs.py`. Sửa tay sẽ bị ghi đè — muốn đổi nội dung thì sửa JSON rồi chạy lại script.

**Đề tài:** Neural-assisted candidate ranking cho SC-Flip Polar decoder  
**English:** Lightweight Neural-Assisted Candidate Ranking for SC-Flip Polar Decoding  
**Tên đầy đủ khi đăng ký:** Xếp hạng ứng viên hỗ trợ mạng neural nhẹ cho bộ giải mã Polar SC-Flip  
**Mã đối chiếu gói gốc:** T13 · **Track D** — Giải mã Polar thích ứng / hỗ trợ neural

---

> Dùng để điền vào biểu mẫu đăng ký của Khoa/Trường. Nội dung sinh từ dữ liệu gốc nên không lệch với danh mục.

## Tên đề tài

**Xếp hạng ứng viên hỗ trợ mạng neural nhẹ cho bộ giải mã Polar SC-Flip**

**English:** Lightweight Neural-Assisted Candidate Ranking for SC-Flip Polar Decoding

_Mã trong danh mục: `B6-T02` — Neural-assisted candidate ranking cho SC-Flip Polar decoder_

## Mục tiêu nghiên cứu

- Làm rõ và kiểm chứng câu hỏi nghiên cứu: Một learned lightweight ranking function có thể đưa true error lên top-k tốt hơn heuristic reliability và giảm average SC-Flip retries với overhead chấp nhận được hay không?
- Xây dựng và triển khai: failed-frame candidate dataset.
- Xây dựng và triển khai: |LLR| baseline.
- Xây dựng và triển khai: handcrafted reliability baseline.
- Xây dựng và triển khai: simple learned baseline.
- Xây dựng và triển khai: tiny NN ranker.
- Xây dựng và triển khai: SCF integration.
- Thực hiện đánh giá có kiểm soát theo các thí nghiệm trọng tâm: Top-1/3/5, BLER, average attempts.
- Đánh giá kết quả bằng chỉ số định lượng, bảo đảm khả năng tái lập và phân tích giới hạn.
- Phát triển năng lực đọc tài liệu, thiết kế thí nghiệm, kiểm chứng, phân tích và viết báo cáo khoa học.

## Dự kiến sản phẩm, kết quả

- Repository mã nguồn/thiết kế, cấu hình và hướng dẫn tái lập.
- ranking table
- BLER curve
- attempt histogram
- ablation
- model complexity
- hardware-aware net saving estimate
- Báo cáo và slide trình bày.
- Teaching Transfer Note để tái sử dụng trong đào tạo.
- Phấn đấu hoàn thiện bản thảo bài báo nếu đạt cửa G7.

## Dự kiến tham gia giải thưởng nghiên cứu khoa học sinh viên

- Hội nghị sinh viên nghiên cứu khoa học cấp Khoa/Trường.
- Các giải thưởng nghiên cứu khoa học sinh viên cấp Trường/Bộ hoặc cuộc thi học thuật chuyên ngành phù hợp.
- Kết quả đạt chất lượng được định hướng hoàn thiện thành bài báo hội nghị/tạp chí; **không cam kết công bố trước khi đạt cửa G7**.

## Ghi chú định hướng công bố

NN ranking phải cải thiện top-k và end-to-end SCF cost/performance ổn định; có strong heuristic baseline, ablation, quantization và net-complexity analysis.
