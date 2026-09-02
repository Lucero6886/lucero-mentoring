# Nội dung đăng ký đề tài — B3-T02

**Engineering & Research Mentoring Program (Lucero)** · ThS. Đinh Văn Nam (Mr. Lucero Dinh) — Khoa Điện–Điện tử, Trường Kỹ thuật, Đại học Phenikaa

> **File sinh tự động** từ `06_Data/research_packs.json` bằng `scripts/generate_research_packs.py`. Sửa tay sẽ bị ghi đè — muốn đổi nội dung thì sửa JSON rồi chạy lại script.

**Đề tài:** Tối ưu fixed-point cho SC Polar decoder  
**English:** Fixed-Point Optimization of an SC Polar Decoder  
**Tên đầy đủ khi đăng ký:** Tối ưu biểu diễn fixed-point cho bộ giải mã Polar Successive Cancellation theo ràng buộc phần cứng  
**Mã đối chiếu gói gốc:** T06 · **Track C** — Kiến trúc bộ giải mã Polar

---

> Dùng để điền vào biểu mẫu đăng ký của Khoa/Trường. Nội dung sinh từ dữ liệu gốc nên không lệch với danh mục.

## Tên đề tài

**Tối ưu biểu diễn fixed-point cho bộ giải mã Polar Successive Cancellation theo ràng buộc phần cứng**

**English:** Hardware-Aware Fixed-Point Optimization of Successive-Cancellation Polar Decoders

_Mã trong danh mục: `B3-T02` — Tối ưu fixed-point cho SC Polar decoder_

## Mục tiêu nghiên cứu

- Làm rõ và kiểm chứng câu hỏi nghiên cứu: Có thể giảm precision của LLR/processing trong SC decoder tới mức nào mà BLER degradation nhỏ trong khi hardware cost giảm đáng kể?
- Xây dựng và triển khai: floating SC reference.
- Xây dựng và triển khai: quantized SC model.
- Xây dựng và triển khai: parameterized fixed-point RTL.
- Xây dựng và triển khai: bit-exact co-verification.
- Xây dựng và triển khai: sweep scripts.
- Thực hiện đánh giá có kiểm soát theo các thí nghiệm trọng tâm: total-bit sweep, fractional/integer split sweep, rounding/saturation study.
- Đánh giá kết quả bằng chỉ số định lượng, bảo đảm khả năng tái lập và phân tích giới hạn.
- Phát triển năng lực đọc tài liệu, thiết kế thí nghiệm, kiểm chứng, phân tích và viết báo cáo khoa học.

## Dự kiến sản phẩm, kết quả

- Repository mã nguồn/thiết kế, cấu hình và hướng dẫn tái lập.
- floating vs fixed BLER curves
- quantization error diagnostics
- bit-exact logs
- hardware cost table
- accuracy–cost Pareto plot
- Báo cáo và slide trình bày.
- Teaching Transfer Note để tái sử dụng trong đào tạo.
- Phấn đấu hoàn thiện bản thảo bài báo nếu đạt cửa G7.

## Dự kiến tham gia giải thưởng nghiên cứu khoa học sinh viên

- Hội nghị sinh viên nghiên cứu khoa học cấp Khoa/Trường.
- Các giải thưởng nghiên cứu khoa học sinh viên cấp Trường/Bộ hoặc cuộc thi học thuật chuyên ngành phù hợp.
- Kết quả đạt chất lượng được định hướng hoàn thiện thành bài báo hội nghị/tạp chí; **không cam kết công bố trước khi đạt cửa G7**.

## Ghi chú định hướng công bố

Có quantization design-space study, statistically reliable BLER, hardware evaluation và một precision strategy/Pareto point có lý do rõ.
