# Nội dung đăng ký đề tài — A4-T01

**Engineering & Research Mentoring Program (Lucero)** · ThS. Đinh Văn Nam (Mr. Lucero Dinh) — Khoa Điện–Điện tử, Trường Kỹ thuật, Đại học Phenikaa

> **File sinh tự động** từ `06_Data/research_packs.json` bằng `scripts/generate_research_packs.py`. Sửa tay sẽ bị ghi đè — muốn đổi nội dung thì sửa JSON rồi chạy lại script.

**Đề tài:** Thiết kế một Digital IP từ RTL đến GDSII  
**English:** Design and Evaluation of a Digital IP from RTL to GDSII  
**Tên đầy đủ khi đăng ký:** Thiết kế và đánh giá một IP số từ RTL đến GDSII sử dụng quy trình EDA mã nguồn mở  
**Mã đối chiếu gói gốc:** T01 · **Track A** — Thiết kế IC số mã nguồn mở

---

> Dùng để điền vào biểu mẫu đăng ký của Khoa/Trường. Nội dung sinh từ dữ liệu gốc nên không lệch với danh mục.

## Tên đề tài

**Thiết kế và đánh giá một IP số từ RTL đến GDSII sử dụng quy trình EDA mã nguồn mở**

**English:** Design and Evaluation of a Digital IP from RTL to GDSII Using an Open-Source EDA Flow

_Mã trong danh mục: `A4-T01` — Thiết kế một Digital IP từ RTL đến GDSII_

## Mục tiêu nghiên cứu

- Làm rõ và kiểm chứng câu hỏi nghiên cứu: Các lựa chọn kiến trúc và ràng buộc physical design ảnh hưởng như thế nào đến timing, area, power và khả năng đóng thiết kế của một IP số?
- Xây dựng và triển khai: Chọn và viết/chuẩn hóa một IP số tham số hóa.
- Xây dựng và triển khai: testbench + regression.
- Xây dựng và triển khai: automation scripts cho flow.
- Xây dựng và triển khai: script trích xuất PPA/timing.
- Thực hiện đánh giá có kiểm soát theo các thí nghiệm trọng tâm: Baseline RTL→GDSII, clock-period sweep, core-utilization sweep.
- Đánh giá kết quả bằng chỉ số định lượng, bảo đảm khả năng tái lập và phân tích giới hạn.
- Phát triển năng lực đọc tài liệu, thiết kế thí nghiệm, kiểm chứng, phân tích và viết báo cáo khoa học.

## Dự kiến sản phẩm, kết quả

- Repository mã nguồn/thiết kế, cấu hình và hướng dẫn tái lập.
- waveform/regression pass
- synthesis report
- STA report
- layout/GDS screenshot
- DRC/LVS summary
- CSV PPA sweep + scripts
- Pareto/summary plots
- Báo cáo và slide trình bày.
- Teaching Transfer Note để tái sử dụng trong đào tạo.
- Phấn đấu hoàn thiện bản thảo bài báo nếu đạt cửa G7.

## Dự kiến tham gia giải thưởng nghiên cứu khoa học sinh viên

- Hội nghị sinh viên nghiên cứu khoa học cấp Khoa/Trường.
- Các giải thưởng nghiên cứu khoa học sinh viên cấp Trường/Bộ hoặc cuộc thi học thuật chuyên ngành phù hợp.
- Kết quả đạt chất lượng được định hướng hoàn thiện thành bài báo hội nghị/tạp chí; **không cam kết công bố trước khi đạt cửa G7**.

## Ghi chú định hướng công bố

Có systematic design-space/PPA study; ít nhất 2 cấu hình/kiến trúc có so sánh công bằng; DRC/LVS sạch; có insight tái lập vượt quá demo flow.
