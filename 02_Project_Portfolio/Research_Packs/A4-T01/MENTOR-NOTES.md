# Ghi chú cho mentor — A4-T01

**Engineering & Research Mentoring Program (Lucero)** · ThS. Đinh Văn Nam (Mr. Lucero Dinh) — Khoa Điện–Điện tử, Trường Kỹ thuật, Đại học Phenikaa

> **File sinh tự động** từ `06_Data/research_packs.json` bằng `scripts/generate_research_packs.py`. Sửa tay sẽ bị ghi đè — muốn đổi nội dung thì sửa JSON rồi chạy lại script.

**Đề tài:** Thiết kế một Digital IP từ RTL đến GDSII  
**English:** Design and Evaluation of a Digital IP from RTL to GDSII  
**Tên đầy đủ khi đăng ký:** Thiết kế và đánh giá một IP số từ RTL đến GDSII sử dụng quy trình EDA mã nguồn mở  
**Mã đối chiếu gói gốc:** T01 · **Track A** — Thiết kế IC số mã nguồn mở

---

## Câu hỏi nghiên cứu

> Các lựa chọn kiến trúc và ràng buộc physical design ảnh hưởng như thế nào đến timing, area, power và khả năng đóng thiết kế của một IP số?

## Bốn câu hỏi trọng tâm

1. IP này đủ phức tạp để có research question nhưng vẫn đóng được không?
2. Tại sao constraint này làm timing/area thay đổi?
3. Nếu layout pass DRC nhưng fail LVS nghĩa là gì?
4. Kết quả nào là insight chứ không chỉ tool output?

## Ngưỡng công bố

Có systematic design-space/PPA study; ít nhất 2 cấu hình/kiến trúc có so sánh công bằng; DRC/LVS sạch; có insight tái lập vượt quá demo flow.

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
