# Ghi chú cho mentor — B6-T01

**Engineering & Research Mentoring Program (Lucero)** · ThS. Đinh Văn Nam (Mr. Lucero Dinh) — Khoa Điện–Điện tử, Trường Kỹ thuật, Đại học Phenikaa

> **File sinh tự động** từ `06_Data/research_packs.json` bằng `scripts/generate_research_packs.py`. Sửa tay sẽ bị ghi đè — muốn đổi nội dung thì sửa JSON rồi chạy lại script.

**Đề tài:** Lightweight neural-assisted unreliable-frame detector  
**English:** Lightweight Neural-Assisted Unreliable-Frame Detector  
**Tên đầy đủ khi đăng ký:** Thiết kế bộ phát hiện frame không tin cậy hỗ trợ mạng neural nhẹ cho giải mã Polar thích ứng  
**Mã đối chiếu gói gốc:** T12 · **Track D** — Giải mã Polar thích ứng / hỗ trợ neural

---

## Câu hỏi nghiên cứu

> Một neural classifier rất nhỏ có thể cải thiện unreliable-frame detection đủ nhiều so với detector heuristic/statistical để justify phần cứng bổ sung hay không?

## Bốn câu hỏi trọng tâm

1. NN học được gì mà feature threshold không làm được?
2. Có leakage giữa train/test theo frame/SNR không?
3. AUC tăng có chuyển thành decoder gain không?
4. Quantization có làm mất lợi thế không?

## Ngưỡng công bố

NN phải vượt simple baselines có ý nghĩa ở end-to-end decoder metric sau khi tính overhead; có ablation, quantization và complexity analysis.

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
