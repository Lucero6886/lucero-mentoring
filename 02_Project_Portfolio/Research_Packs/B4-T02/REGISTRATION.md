# Nội dung đăng ký đề tài — B4-T02

**Engineering & Research Mentoring Program (Lucero)** · ThS. Đinh Văn Nam (Mr. Lucero Dinh) — Khoa Điện–Điện tử, Trường Kỹ thuật, Đại học Phenikaa

> **File sinh tự động** từ `06_Data/research_packs.json` bằng `scripts/generate_research_packs.py`. Sửa tay sẽ bị ghi đè — muốn đổi nội dung thì sửa JSON rồi chạy lại script.

**Đề tài:** Reliability-based candidate ranking cho SC-Flip  
**English:** Reliability-Based Candidate Ranking for SC-Flip Polar Decoding  
**Tên đầy đủ khi đăng ký:** Nghiên cứu phương pháp xếp hạng ứng viên dựa trên độ tin cậy cho bộ giải mã Polar SC-Flip  
**Mã đối chiếu gói gốc:** T08 · **Track C** — Kiến trúc bộ giải mã Polar

---

> Dùng để điền vào biểu mẫu đăng ký của Khoa/Trường. Nội dung sinh từ dữ liệu gốc nên không lệch với danh mục.

## Tên đề tài

**Nghiên cứu phương pháp xếp hạng ứng viên dựa trên độ tin cậy cho bộ giải mã Polar SC-Flip**

**English:** Reliability-Based Candidate Ranking for SC-Flip Polar Decoding

_Mã trong danh mục: `B4-T02` — Reliability-based candidate ranking cho SC-Flip_

## Mục tiêu nghiên cứu

- Làm rõ và kiểm chứng câu hỏi nghiên cứu: Có thể dùng thông tin độ tin cậy tốt hơn |LLR| đơn thuần để tăng xác suất đưa true error vào top-k candidate và giảm số lần SC-Flip retry hay không?
- Xây dựng và triển khai: failed-frame data collector.
- Xây dựng và triển khai: candidate feature extractor.
- Xây dựng và triển khai: baseline |LLR| ranking.
- Xây dựng và triển khai: proposed handcrafted metric.
- Xây dựng và triển khai: SCF integration.
- Thực hiện đánh giá có kiểm soát theo các thí nghiệm trọng tâm: Top-1/3/5 hit rate, BLER vs SNR, average attempts.
- Đánh giá kết quả bằng chỉ số định lượng, bảo đảm khả năng tái lập và phân tích giới hạn.
- Phát triển năng lực đọc tài liệu, thiết kế thí nghiệm, kiểm chứng, phân tích và viết báo cáo khoa học.

## Dự kiến sản phẩm, kết quả

- Repository mã nguồn/thiết kế, cấu hình và hướng dẫn tái lập.
- ranking accuracy table
- BLER curves
- attempt reduction
- failure examples
- operation-count/hardware-cost estimate
- Báo cáo và slide trình bày.
- Teaching Transfer Note để tái sử dụng trong đào tạo.
- Phấn đấu hoàn thiện bản thảo bài báo nếu đạt cửa G7.

## Dự kiến tham gia giải thưởng nghiên cứu khoa học sinh viên

- Hội nghị sinh viên nghiên cứu khoa học cấp Khoa/Trường.
- Các giải thưởng nghiên cứu khoa học sinh viên cấp Trường/Bộ hoặc cuộc thi học thuật chuyên ngành phù hợp.
- Kết quả đạt chất lượng được định hướng hoàn thiện thành bài báo hội nghị/tạp chí; **không cam kết công bố trước khi đạt cửa G7**.

## Ghi chú định hướng công bố

Có ranking improvement ổn định, end-to-end SCF benefit, complexity analysis và ablation/interpretation rõ.
