# Ghi chú cho mentor — A5-T01

**Engineering & Research Mentoring Program (Lucero)** · ThS. Đinh Văn Nam (Mr. Lucero Dinh) — Khoa Điện–Điện tử, Trường Kỹ thuật, Đại học Phenikaa

> **File sinh tự động** từ `06_Data/research_packs.json` bằng `scripts/generate_research_packs.py`. Sửa tay sẽ bị ghi đè — muốn đổi nội dung thì sửa JSON rồi chạy lại script.

**Đề tài:** Xây dựng quy trình ASIC tái lập sử dụng LibreLane + Nix  
**English:** Reproducible ASIC Workflow Using LibreLane and Nix  
**Tên đầy đủ khi đăng ký:** Xây dựng và đánh giá quy trình RTL-to-GDSII mã nguồn mở có khả năng tái lập phục vụ đào tạo thiết kế vi mạch số  
**Mã đối chiếu gói gốc:** T02 · **Track A** — Thiết kế IC số mã nguồn mở

---

## Câu hỏi nghiên cứu

> Làm thế nào xây dựng một RTL-to-GDSII environment mà người học khác có thể tái lập kết quả một cách ổn định trên các máy/môi trường khác nhau?

## Bốn câu hỏi trọng tâm

1. Cái gì đang được 'reproduced': chức năng hay PPA hay cả hai?
2. Nguồn biến thiên nào do tool, nguồn nào do environment?
3. Một sinh viên mới cần bao nhiêu bước thủ công?
4. Đóng góp nghiên cứu/giáo dục nằm ở đâu ngoài việc viết script?

## Ngưỡng công bố

Có protocol tái lập rõ, benchmark đủ đa dạng, thử nghiệm trên nhiều môi trường/người dùng hoặc nhiều clean runs, có định lượng consistency và bài học giáo dục.

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
