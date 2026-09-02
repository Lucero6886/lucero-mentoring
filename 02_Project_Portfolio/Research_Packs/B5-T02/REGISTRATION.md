# Nội dung đăng ký đề tài — B5-T02

**Engineering & Research Mentoring Program (Lucero)** · ThS. Đinh Văn Nam (Mr. Lucero Dinh) — Khoa Điện–Điện tử, Trường Kỹ thuật, Đại học Phenikaa

> **File sinh tự động** từ `06_Data/research_packs.json` bằng `scripts/generate_research_packs.py`. Sửa tay sẽ bị ghi đè — muốn đổi nội dung thì sửa JSON rồi chạy lại script.

**Đề tài:** Adaptive decoder chỉ kích hoạt enhanced processing trên frame khó  
**English:** Adaptive Polar Decoding with Selective Enhanced Processing  
**Tên đầy đủ khi đăng ký:** Thiết kế bộ giải mã Polar thích ứng dựa trên độ tin cậy với cơ chế xử lý tăng cường có chọn lọc  
**Mã đối chiếu gói gốc:** T10 · **Track D** — Giải mã Polar thích ứng / hỗ trợ neural

---

> Dùng để điền vào biểu mẫu đăng ký của Khoa/Trường. Nội dung sinh từ dữ liệu gốc nên không lệch với danh mục.

## Tên đề tài

**Thiết kế bộ giải mã Polar thích ứng dựa trên độ tin cậy với cơ chế xử lý tăng cường có chọn lọc**

**English:** Reliability-Gated Adaptive Polar Decoding with Selective Enhanced Processing

_Mã trong danh mục: `B5-T02` — Adaptive decoder chỉ kích hoạt enhanced processing trên frame khó_

## Mục tiêu nghiên cứu

- Làm rõ và kiểm chứng câu hỏi nghiên cứu: Selective enhanced processing có thể đạt BLER gần always-on enhanced decoder nhưng giảm average latency/operations/energy trên các frame dễ hay không?
- Xây dựng và triển khai: SC baseline.
- Xây dựng và triển khai: reliability gate.
- Xây dựng và triển khai: enhanced decoder interface.
- Xây dựng và triển khai: adaptive controller.
- Xây dựng và triển khai: metrics logger.
- Thực hiện đánh giá có kiểm soát theo các thí nghiệm trọng tâm: BLER vs SNR, activation rate vs SNR, average operations/latency.
- Đánh giá kết quả bằng chỉ số định lượng, bảo đảm khả năng tái lập và phân tích giới hạn.
- Phát triển năng lực đọc tài liệu, thiết kế thí nghiệm, kiểm chứng, phân tích và viết báo cáo khoa học.

## Dự kiến sản phẩm, kết quả

- Repository mã nguồn/thiết kế, cấu hình và hướng dẫn tái lập.
- BLER plot
- activation plot
- average-cost table
- threshold Pareto curve
- failure/missed-hard-frame analysis
- Báo cáo và slide trình bày.
- Teaching Transfer Note để tái sử dụng trong đào tạo.
- Phấn đấu hoàn thiện bản thảo bài báo nếu đạt cửa G7.

## Dự kiến tham gia giải thưởng nghiên cứu khoa học sinh viên

- Hội nghị sinh viên nghiên cứu khoa học cấp Khoa/Trường.
- Các giải thưởng nghiên cứu khoa học sinh viên cấp Trường/Bộ hoặc cuộc thi học thuật chuyên ngành phù hợp.
- Kết quả đạt chất lượng được định hướng hoàn thiện thành bài báo hội nghị/tạp chí; **không cam kết công bố trước khi đạt cửa G7**.

## Ghi chú định hướng công bố

Có clear adaptive gain: gần performance của enhanced baseline với giảm average cost đáng kể; có oracle/strong baselines và sensitivity.
