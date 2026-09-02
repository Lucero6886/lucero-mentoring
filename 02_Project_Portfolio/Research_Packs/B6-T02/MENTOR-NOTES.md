# Ghi chú cho mentor — B6-T02

**Engineering & Research Mentoring Program (Lucero)** · ThS. Đinh Văn Nam (Mr. Lucero Dinh) — Khoa Điện–Điện tử, Trường Kỹ thuật, Đại học Phenikaa

> **File sinh tự động** từ `06_Data/research_packs.json` bằng `scripts/generate_research_packs.py`. Sửa tay sẽ bị ghi đè — muốn đổi nội dung thì sửa JSON rồi chạy lại script.

**Đề tài:** Neural-assisted candidate ranking cho SC-Flip Polar decoder  
**English:** Lightweight Neural-Assisted Candidate Ranking for SC-Flip Polar Decoding  
**Tên đầy đủ khi đăng ký:** Xếp hạng ứng viên hỗ trợ mạng neural nhẹ cho bộ giải mã Polar SC-Flip  
**Mã đối chiếu gói gốc:** T13 · **Track D** — Giải mã Polar thích ứng / hỗ trợ neural

---

## Câu hỏi nghiên cứu

> Một learned lightweight ranking function có thể đưa true error lên top-k tốt hơn heuristic reliability và giảm average SC-Flip retries với overhead chấp nhận được hay không?

## Bốn câu hỏi trọng tâm

1. Label nào thực sự cần rank?
2. Ranking accuracy tăng có giảm retries không?
3. NN có thắng handcrafted metric ở nhiều SNR/N không?
4. Net cost sau NN overhead là bao nhiêu?

## Ngưỡng công bố

NN ranking phải cải thiện top-k và end-to-end SCF cost/performance ổn định; có strong heuristic baseline, ablation, quantization và net-complexity analysis.

**Tiềm năng đánh giá ban đầu:** Rất cao, kèm rủi ro cao

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
