# Ghi chú cho mentor — B5-T02

**Engineering & Research Mentoring Program (Lucero)** · ThS. Đinh Văn Nam (Mr. Lucero Dinh) — Khoa Điện–Điện tử, Trường Kỹ thuật, Đại học Phenikaa

> **File sinh tự động** từ `06_Data/research_packs.json` bằng `scripts/generate_research_packs.py`. Sửa tay sẽ bị ghi đè — muốn đổi nội dung thì sửa JSON rồi chạy lại script.

**Đề tài:** Adaptive decoder chỉ kích hoạt enhanced processing trên frame khó  
**English:** Adaptive Polar Decoding with Selective Enhanced Processing  
**Tên đầy đủ khi đăng ký:** Thiết kế bộ giải mã Polar thích ứng dựa trên độ tin cậy với cơ chế xử lý tăng cường có chọn lọc  
**Mã đối chiếu gói gốc:** T10 · **Track D** — Giải mã Polar thích ứng / hỗ trợ neural

---

## Câu hỏi nghiên cứu

> Selective enhanced processing có thể đạt BLER gần always-on enhanced decoder nhưng giảm average latency/operations/energy trên các frame dễ hay không?

## Bốn câu hỏi trọng tâm

1. Gate biết gì tại thời điểm quyết định?
2. Savings đến từ đâu?
3. BLER gap với always-on là bao nhiêu?
4. Nếu SNR thay đổi, threshold có còn hợp lý?

## Ngưỡng công bố

Có clear adaptive gain: gần performance của enhanced baseline với giảm average cost đáng kể; có oracle/strong baselines và sensitivity.

**Tiềm năng đánh giá ban đầu:** Rất cao

## Phụ thuộc

Cần baseline của `B5-T01` (T09) trước khi mở.

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
