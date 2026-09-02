# Ghi chú cho mentor — A2-T02

**Engineering & Research Mentoring Program (Lucero)** · ThS. Đinh Văn Nam (Mr. Lucero Dinh) — Khoa Điện–Điện tử, Trường Kỹ thuật, Đại học Phenikaa

> **File sinh tự động** từ `06_Data/research_packs.json` bằng `scripts/generate_research_packs.py`. Sửa tay sẽ bị ghi đè — muốn đổi nội dung thì sửa JSON rồi chạy lại script.

**Đề tài:** Thiết kế và tối ưu MAC datapath cho FPGA/ASIC  
**English:** Design and Optimization of a Fixed-Point MAC Datapath for FPGA/ASIC  
**Tên đầy đủ khi đăng ký:** Thiết kế MAC datapath và đánh giá ảnh hưởng của bit-width và pipeline đến độ chính xác và chi phí phần cứng  
**Mã đối chiếu gói gốc:** T03 · **Track B** — Kiến trúc phần cứng số

---

## Câu hỏi nghiên cứu

> Bit-width và mức pipeline thay đổi numerical accuracy, latency, throughput, area và power của MAC datapath như thế nào?

## Bốn câu hỏi trọng tâm

1. Accuracy được định nghĩa bằng metric nào?
2. Hai cấu hình pipeline có cùng chức năng và precision không?
3. Fmax cao hơn có thực sự cải thiện throughput ở interface này?
4. Điểm Pareto nào hợp lý và vì sao?

## Ngưỡng công bố

Có design-space sweep đủ rộng, numerical + hardware metrics, Pareto analysis, ít nhất một insight kiến trúc/quantization có tính tổng quát.

**Tiềm năng đánh giá ban đầu:** Cao

## Phụ thuộc

Không phụ thuộc đề tài nào — có thể mở ngay.

## Cảnh báo sớm

- Sinh viên chạy proposed trước baseline.
- Chỉ đưa screenshot mà không có raw data/config.
- Metric thay đổi giữa các phương pháp.
- Kết luận dựa vào 1 run/1 SNR/1 seed khi bài toán cần thống kê.
- AI-generated code nhưng sinh viên không giải thích được.
- Không phân biệt implementation result với research contribution.

## Sau mỗi mốc

Ghi lại vào `04_Project_Template/MENTOR_LESSONS_LEARNED.md`: sinh viên hiểu sai chỗ nào, thiếu kiến thức tiên quyết nào, cách giải thích nào có tác dụng, thí nghiệm nào gây hiểu nhầm, tài liệu nào tốt nhất, và lần sau nên đổi gì.

## Checklist tuần

`03_Operations/MENTOR_WEEKLY_CHECKLIST.md` · Thang chấm: `03_Operations/PASS_FAIL_RUBRIC.md`
