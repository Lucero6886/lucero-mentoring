# Ghi chú cho mentor — B5-T01

**Engineering & Research Mentoring Program (Lucero)** · ThS. Đinh Văn Nam (Mr. Lucero Dinh) — Khoa Điện–Điện tử, Trường Kỹ thuật, Đại học Phenikaa

> **File sinh tự động** từ `06_Data/research_packs.json` bằng `scripts/generate_research_packs.py`. Sửa tay sẽ bị ghi đè — muốn đổi nội dung thì sửa JSON rồi chạy lại script.

**Đề tài:** Phát hiện frame không tin cậy cho adaptive Polar decoding  
**English:** Unreliable-Frame Detection for Adaptive Polar Decoding  
**Tên đầy đủ khi đăng ký:** Phát hiện frame không tin cậy cho giải mã Polar thích ứng dựa trên đặc trưng độ tin cậy  
**Mã đối chiếu gói gốc:** T09 · **Track D** — Giải mã Polar thích ứng / hỗ trợ neural

---

## Câu hỏi nghiên cứu

> Có thể nhận biết sớm frame SC có nguy cơ sai bằng một detector độ phức tạp thấp để tránh kích hoạt enhanced decoding trên mọi frame hay không?

## Bốn câu hỏi trọng tâm

1. Label có leakage không?
2. Feature này có sẵn trước khi quyết định activate không?
3. False negative gây hậu quả gì?
4. Operating point nào tối ưu cho decoder chứ không chỉ classifier?

## Ngưỡng công bố

Detector phải tạo end-to-end benefit: giảm activation/average cost trong khi BLER gần target; có baseline, sensitivity và no-leakage validation.

**Tiềm năng đánh giá ban đầu:** Cao

## Phụ thuộc

Cần baseline của `B4-T02` (T08) trước khi mở.

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
