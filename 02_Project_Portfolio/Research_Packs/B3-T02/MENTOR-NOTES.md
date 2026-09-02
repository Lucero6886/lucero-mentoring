# Ghi chú cho mentor — B3-T02

**Engineering & Research Mentoring Program (Lucero)** · ThS. Đinh Văn Nam (Mr. Lucero Dinh) — Khoa Điện–Điện tử, Trường Kỹ thuật, Đại học Phenikaa

> **File sinh tự động** từ `06_Data/research_packs.json` bằng `scripts/generate_research_packs.py`. Sửa tay sẽ bị ghi đè — muốn đổi nội dung thì sửa JSON rồi chạy lại script.

**Đề tài:** Tối ưu fixed-point cho SC Polar decoder  
**English:** Fixed-Point Optimization of an SC Polar Decoder  
**Tên đầy đủ khi đăng ký:** Tối ưu biểu diễn fixed-point cho bộ giải mã Polar Successive Cancellation theo ràng buộc phần cứng  
**Mã đối chiếu gói gốc:** T06 · **Track C** — Kiến trúc bộ giải mã Polar

---

## Câu hỏi nghiên cứu

> Có thể giảm precision của LLR/processing trong SC decoder tới mức nào mà BLER degradation nhỏ trong khi hardware cost giảm đáng kể?

## Bốn câu hỏi trọng tâm

1. Vì sao chọn range này?
2. BLER loss được đo tại những SNR nào?
3. Có overflow âm thầm không?
4. Bit-width tối ưu có ổn định theo N/K/SNR không?

## Ngưỡng công bố

Có quantization design-space study, statistically reliable BLER, hardware evaluation và một precision strategy/Pareto point có lý do rõ.

**Tiềm năng đánh giá ban đầu:** Cao

## Phụ thuộc

Cần baseline của `B2-T01` (T05) trước khi mở.

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
