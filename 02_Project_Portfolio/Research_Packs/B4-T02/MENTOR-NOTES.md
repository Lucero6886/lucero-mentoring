# Ghi chú cho mentor — B4-T02

**Engineering & Research Mentoring Program (Lucero)** · ThS. Đinh Văn Nam (Mr. Lucero Dinh) — Khoa Điện–Điện tử, Trường Kỹ thuật, Đại học Phenikaa

> **File sinh tự động** từ `06_Data/research_packs.json` bằng `scripts/generate_research_packs.py`. Sửa tay sẽ bị ghi đè — muốn đổi nội dung thì sửa JSON rồi chạy lại script.

**Đề tài:** Reliability-based candidate ranking cho SC-Flip  
**English:** Reliability-Based Candidate Ranking for SC-Flip Polar Decoding  
**Tên đầy đủ khi đăng ký:** Nghiên cứu phương pháp xếp hạng ứng viên dựa trên độ tin cậy cho bộ giải mã Polar SC-Flip  
**Mã đối chiếu gói gốc:** T08 · **Track C** — Kiến trúc bộ giải mã Polar

---

## Câu hỏi nghiên cứu

> Có thể dùng thông tin độ tin cậy tốt hơn |LLR| đơn thuần để tăng xác suất đưa true error vào top-k candidate và giảm số lần SC-Flip retry hay không?

## Bốn câu hỏi trọng tâm

1. Metric mới dùng thông tin nào mà |LLR| không có?
2. Improvement có còn khi candidate pool thay đổi?
3. Ranking tốt hơn có thực sự cải thiện BLER/latency?
4. Overhead của metric có ăn hết lợi ích không?

## Ngưỡng công bố

Có ranking improvement ổn định, end-to-end SCF benefit, complexity analysis và ablation/interpretation rõ.

**Tiềm năng đánh giá ban đầu:** Cao

## Phụ thuộc

Cần baseline của `B4-T01` (T07) trước khi mở.

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
