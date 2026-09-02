# Nội dung đăng ký đề tài — A5-T01

**Engineering & Research Mentoring Program (Lucero)** · ThS. Đinh Văn Nam (Mr. Lucero Dinh) — Khoa Điện–Điện tử, Trường Kỹ thuật, Đại học Phenikaa

> **File sinh tự động** từ `06_Data/research_packs.json` bằng `scripts/generate_research_packs.py`. Sửa tay sẽ bị ghi đè — muốn đổi nội dung thì sửa JSON rồi chạy lại script.

**Đề tài:** Xây dựng quy trình ASIC tái lập sử dụng LibreLane + Nix  
**English:** Reproducible ASIC Workflow Using LibreLane and Nix  
**Tên đầy đủ khi đăng ký:** Xây dựng và đánh giá quy trình RTL-to-GDSII mã nguồn mở có khả năng tái lập phục vụ đào tạo thiết kế vi mạch số  
**Mã đối chiếu gói gốc:** T02 · **Track A** — Thiết kế IC số mã nguồn mở

---

> Dùng để điền vào biểu mẫu đăng ký của Khoa/Trường. Nội dung sinh từ dữ liệu gốc nên không lệch với danh mục.

## Tên đề tài

**Xây dựng và đánh giá quy trình RTL-to-GDSII mã nguồn mở có khả năng tái lập phục vụ đào tạo thiết kế vi mạch số**

**English:** Development and Evaluation of a Reproducible Open-Source RTL-to-GDSII Flow for Digital IC Design Education

_Mã trong danh mục: `A5-T01` — Xây dựng quy trình ASIC tái lập sử dụng LibreLane + Nix_

## Mục tiêu nghiên cứu

- Làm rõ và kiểm chứng câu hỏi nghiên cứu: Làm thế nào xây dựng một RTL-to-GDSII environment mà người học khác có thể tái lập kết quả một cách ổn định trên các máy/môi trường khác nhau?
- Xây dựng và triển khai: bootstrap/setup scripts.
- Xây dựng và triển khai: version manifest.
- Xây dựng và triển khai: benchmark runner.
- Xây dựng và triển khai: result parser.
- Xây dựng và triển khai: optional CI workflow.
- Thực hiện đánh giá có kiểm soát theo các thí nghiệm trọng tâm: Fresh install test, multi-machine or multi-environment rerun, version/config sensitivity.
- Đánh giá kết quả bằng chỉ số định lượng, bảo đảm khả năng tái lập và phân tích giới hạn.
- Phát triển năng lực đọc tài liệu, thiết kế thí nghiệm, kiểm chứng, phân tích và viết báo cáo khoa học.

## Dự kiến sản phẩm, kết quả

- Repository mã nguồn/thiết kế, cấu hình và hướng dẫn tái lập.
- setup time log
- success/failure matrix
- version manifest
- PPA/run-time variance
- clean-clone demonstration
- student reproduction checklist
- Báo cáo và slide trình bày.
- Teaching Transfer Note để tái sử dụng trong đào tạo.
- Phấn đấu hoàn thiện bản thảo bài báo nếu đạt cửa G7.

## Dự kiến tham gia giải thưởng nghiên cứu khoa học sinh viên

- Hội nghị sinh viên nghiên cứu khoa học cấp Khoa/Trường.
- Các giải thưởng nghiên cứu khoa học sinh viên cấp Trường/Bộ hoặc cuộc thi học thuật chuyên ngành phù hợp.
- Kết quả đạt chất lượng được định hướng hoàn thiện thành bài báo hội nghị/tạp chí; **không cam kết công bố trước khi đạt cửa G7**.

## Ghi chú định hướng công bố

Có protocol tái lập rõ, benchmark đủ đa dạng, thử nghiệm trên nhiều môi trường/người dùng hoặc nhiều clean runs, có định lượng consistency và bài học giáo dục.
