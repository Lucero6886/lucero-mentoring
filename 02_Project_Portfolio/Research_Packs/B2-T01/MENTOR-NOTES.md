# Ghi chú cho mentor — B2-T01

**Engineering & Research Mentoring Program (Lucero)** · ThS. Đinh Văn Nam (Mr. Lucero Dinh) — Khoa Điện–Điện tử, Trường Kỹ thuật, Đại học Phenikaa

> **File sinh tự động** từ `06_Data/research_packs.json` bằng `scripts/generate_research_packs.py`. Sửa tay sẽ bị ghi đè — muốn đổi nội dung thì sửa JSON rồi chạy lại script.

**Đề tài:** Thiết kế bộ giải mã SC Polar trên FPGA  
**English:** FPGA Architecture and Implementation of an SC Polar Decoder  
**Tên đầy đủ khi đăng ký:** Thiết kế và đánh giá kiến trúc bộ giải mã Polar Successive Cancellation trên FPGA  
**Mã đối chiếu gói gốc:** T05 · **Track C** — Kiến trúc bộ giải mã Polar

---

## Câu hỏi nghiên cứu

> Một kiến trúc SC Polar decoder có thể được ánh xạ lên FPGA với correctness, latency, throughput và resource cost như thế nào?

## Bốn câu hỏi trọng tâm

1. Tại sao bit này frozen?
2. LLR âm/dương và độ lớn nói gì?
3. Latency được đo từ cycle nào tới cycle nào?
4. RTL và software mismatch ở f/g hay partial sum?

## Ngưỡng công bố

Baseline architecture validated; FPGA metrics đầy đủ; chỉ paper nếu có architectural choice/optimization/comparison tạo insight ngoài việc implement SC.

**Tiềm năng đánh giá ban đầu:** Trung bình

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
