# Nội dung đăng ký đề tài — A2-T02

**Engineering & Research Mentoring Program (Lucero)** · ThS. Đinh Văn Nam (Mr. Lucero Dinh) — Khoa Điện–Điện tử, Trường Kỹ thuật, Đại học Phenikaa

> **File sinh tự động** từ `06_Data/research_packs.json` bằng `scripts/generate_research_packs.py`. Sửa tay sẽ bị ghi đè — muốn đổi nội dung thì sửa JSON rồi chạy lại script.

**Đề tài:** Thiết kế và tối ưu MAC datapath cho FPGA/ASIC  
**English:** Design and Optimization of a Fixed-Point MAC Datapath for FPGA/ASIC  
**Tên đầy đủ khi đăng ký:** Thiết kế MAC datapath và đánh giá ảnh hưởng của bit-width và pipeline đến độ chính xác và chi phí phần cứng  
**Mã đối chiếu gói gốc:** T03 · **Track B** — Kiến trúc phần cứng số

---

> Dùng để điền vào biểu mẫu đăng ký của Khoa/Trường. Nội dung sinh từ dữ liệu gốc nên không lệch với danh mục.

## Tên đề tài

**Thiết kế MAC datapath và đánh giá ảnh hưởng của bit-width và pipeline đến độ chính xác và chi phí phần cứng**

**English:** Hardware-Aware Design of a MAC Datapath: Accuracy–Cost Trade-offs under Bit-Width and Pipeline Scaling

_Mã trong danh mục: `A2-T02` — Thiết kế và tối ưu MAC datapath cho FPGA/ASIC_

## Mục tiêu nghiên cứu

- Làm rõ và kiểm chứng câu hỏi nghiên cứu: Bit-width và mức pipeline thay đổi numerical accuracy, latency, throughput, area và power của MAC datapath như thế nào?
- Xây dựng và triển khai: floating-point golden model.
- Xây dựng và triển khai: fixed-point model.
- Xây dựng và triển khai: parameterized RTL MAC.
- Xây dựng và triển khai: self-checking testbench.
- Xây dựng và triển khai: sweep scripts.
- Thực hiện đánh giá có kiểm soát theo các thí nghiệm trọng tâm: bit-width sweep, fractional-bit allocation, pipeline-depth sweep.
- Đánh giá kết quả bằng chỉ số định lượng, bảo đảm khả năng tái lập và phân tích giới hạn.
- Phát triển năng lực đọc tài liệu, thiết kế thí nghiệm, kiểm chứng, phân tích và viết báo cáo khoa học.

## Dự kiến sản phẩm, kết quả

- Repository mã nguồn/thiết kế, cấu hình và hướng dẫn tái lập.
- numerical error plots
- RTL-vs-golden equivalence results
- LUT/FF or area reports
- fmax/latency/throughput table
- Pareto plot
- Báo cáo và slide trình bày.
- Teaching Transfer Note để tái sử dụng trong đào tạo.
- Phấn đấu hoàn thiện bản thảo bài báo nếu đạt cửa G7.

## Dự kiến tham gia giải thưởng nghiên cứu khoa học sinh viên

- Hội nghị sinh viên nghiên cứu khoa học cấp Khoa/Trường.
- Các giải thưởng nghiên cứu khoa học sinh viên cấp Trường/Bộ hoặc cuộc thi học thuật chuyên ngành phù hợp.
- Kết quả đạt chất lượng được định hướng hoàn thiện thành bài báo hội nghị/tạp chí; **không cam kết công bố trước khi đạt cửa G7**.

## Ghi chú định hướng công bố

Có design-space sweep đủ rộng, numerical + hardware metrics, Pareto analysis, ít nhất một insight kiến trúc/quantization có tính tổng quát.
