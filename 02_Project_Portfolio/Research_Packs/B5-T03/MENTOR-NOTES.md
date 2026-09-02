# Ghi chú cho mentor — B5-T03

**Engineering & Research Mentoring Program (Lucero)** · ThS. Đinh Văn Nam (Mr. Lucero Dinh) — Khoa Điện–Điện tử, Trường Kỹ thuật, Đại học Phenikaa

> **File sinh tự động** từ `06_Data/research_packs.json` bằng `scripts/generate_research_packs.py`. Sửa tay sẽ bị ghi đè — muốn đổi nội dung thì sửa JSON rồi chạy lại script.

**Đề tài:** Đồng thiết kế thuật toán - phần cứng cho bộ giải mã Polar thích ứng  
**English:** Algorithm-Hardware Co-Design of an Adaptive Polar Decoder  
**Tên đầy đủ khi đăng ký:** Đồng thiết kế thuật toán–phần cứng cho bộ giải mã Polar thích ứng trên FPGA  
**Mã đối chiếu gói gốc:** T11 · **Track D** — Giải mã Polar thích ứng / hỗ trợ neural

---

## Câu hỏi nghiên cứu

> Làm thế nào ánh xạ adaptive Polar decoding thành kiến trúc phần cứng để lợi thế average-case của thuật toán vẫn tồn tại sau fixed-point, control, memory và interface overhead?

## Bốn câu hỏi trọng tâm

1. Algorithm saving nào biến mất khi đưa lên hardware?
2. Control/memory overhead là bao nhiêu?
3. Average-case metric đo trên distribution nào?
4. Kiến trúc có scale với N không?

## Ngưỡng công bố

FPGA implementation validated; algorithmic gain survives hardware overhead; có architecture comparison và average/worst-case metrics; paper-ready khi co-design tạo insight rõ.

**Tiềm năng đánh giá ban đầu:** Rất cao

## Phụ thuộc

Cần baseline của `B5-T02` (T10), `B3-T02` (T06) trước khi mở.

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
