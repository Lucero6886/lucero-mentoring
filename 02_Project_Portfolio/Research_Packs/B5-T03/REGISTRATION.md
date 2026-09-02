# Nội dung đăng ký đề tài — B5-T03

**Engineering & Research Mentoring Program (Lucero)** · ThS. Đinh Văn Nam (Mr. Lucero Dinh) — Khoa Điện–Điện tử, Trường Kỹ thuật, Đại học Phenikaa

> **File sinh tự động** từ `06_Data/research_packs.json` bằng `scripts/generate_research_packs.py`. Sửa tay sẽ bị ghi đè — muốn đổi nội dung thì sửa JSON rồi chạy lại script.

**Đề tài:** Đồng thiết kế thuật toán - phần cứng cho bộ giải mã Polar thích ứng  
**English:** Algorithm-Hardware Co-Design of an Adaptive Polar Decoder  
**Tên đầy đủ khi đăng ký:** Đồng thiết kế thuật toán–phần cứng cho bộ giải mã Polar thích ứng trên FPGA  
**Mã đối chiếu gói gốc:** T11 · **Track D** — Giải mã Polar thích ứng / hỗ trợ neural

---

> Dùng để điền vào biểu mẫu đăng ký của Khoa/Trường. Nội dung sinh từ dữ liệu gốc nên không lệch với danh mục.

## Tên đề tài

**Đồng thiết kế thuật toán–phần cứng cho bộ giải mã Polar thích ứng trên FPGA**

**English:** Algorithm–Hardware Co-Design of an Adaptive Polar Decoder on FPGA

_Mã trong danh mục: `B5-T03` — Đồng thiết kế thuật toán - phần cứng cho bộ giải mã Polar thích ứng_

## Mục tiêu nghiên cứu

- Làm rõ và kiểm chứng câu hỏi nghiên cứu: Làm thế nào ánh xạ adaptive Polar decoding thành kiến trúc phần cứng để lợi thế average-case của thuật toán vẫn tồn tại sau fixed-point, control, memory và interface overhead?
- Xây dựng và triển khai: fixed-point adaptive model.
- Xây dựng và triển khai: module partition.
- Xây dựng và triển khai: SC datapath.
- Xây dựng và triển khai: reliability unit.
- Xây dựng và triển khai: controller.
- Xây dựng và triển khai: enhanced-processing interface.
- Xây dựng và triển khai: RTL TB + FPGA build.
- Thực hiện đánh giá có kiểm soát theo các thí nghiệm trọng tâm: bit-exact verification, resource-sharing alternatives, fmax/latency/throughput.
- Đánh giá kết quả bằng chỉ số định lượng, bảo đảm khả năng tái lập và phân tích giới hạn.
- Phát triển năng lực đọc tài liệu, thiết kế thí nghiệm, kiểm chứng, phân tích và viết báo cáo khoa học.

## Dự kiến sản phẩm, kết quả

- Repository mã nguồn/thiết kế, cấu hình và hướng dẫn tái lập.
- architecture diagram
- bit-exact logs
- resource/timing reports
- average/worst latency
- power/energy table
- comparison with non-adaptive hardware baseline
- Báo cáo và slide trình bày.
- Teaching Transfer Note để tái sử dụng trong đào tạo.
- Phấn đấu hoàn thiện bản thảo bài báo nếu đạt cửa G7.

## Dự kiến tham gia giải thưởng nghiên cứu khoa học sinh viên

- Hội nghị sinh viên nghiên cứu khoa học cấp Khoa/Trường.
- Các giải thưởng nghiên cứu khoa học sinh viên cấp Trường/Bộ hoặc cuộc thi học thuật chuyên ngành phù hợp.
- Kết quả đạt chất lượng được định hướng hoàn thiện thành bài báo hội nghị/tạp chí; **không cam kết công bố trước khi đạt cửa G7**.

## Ghi chú định hướng công bố

FPGA implementation validated; algorithmic gain survives hardware overhead; có architecture comparison và average/worst-case metrics; paper-ready khi co-design tạo insight rõ.
