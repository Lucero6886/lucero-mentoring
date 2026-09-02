# Ghi chú cho mentor — B4-T01

**Engineering & Research Mentoring Program (Lucero)** · ThS. Đinh Văn Nam (Mr. Lucero Dinh) — Khoa Điện–Điện tử, Trường Kỹ thuật, Đại học Phenikaa

> **File sinh tự động** từ `06_Data/research_packs.json` bằng `scripts/generate_research_packs.py`. Sửa tay sẽ bị ghi đè — muốn đổi nội dung thì sửa JSON rồi chạy lại script.

**Đề tài:** Thiết kế và đánh giá SC-Flip Polar decoder  
**English:** Design and Performance Evaluation of SC-Flip Polar Decoding  
**Tên đầy đủ khi đăng ký:** Thiết kế và đánh giá bộ giải mã Polar SC-Flip hướng đến triển khai phần cứng  
**Mã đối chiếu gói gốc:** T07 · **Track C** — Kiến trúc bộ giải mã Polar

---

## Câu hỏi nghiên cứu

> SC-Flip cải thiện BLER của SC với trade-off average/worst-case latency và complexity như thế nào khi hướng tới phần cứng?

## Bốn câu hỏi trọng tâm

1. SCF sửa first error hay mọi error?
2. Average complexity có ý nghĩa gì so với worst case?
3. Tmax tăng đem lại diminishing returns khi nào?
4. SCF có lợi phần cứng hơn SCL ở giả định nào?

## Ngưỡng công bố

Có strong baseline, BLER–latency/complexity trade-off rõ, không chỉ reproduce algorithm; tốt hơn nếu có hardware-oriented modification/analysis.

**Tiềm năng đánh giá ban đầu:** Trung bình – cao

## Phụ thuộc

Cần baseline của `B3-T02` (T06) trước khi mở.

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
