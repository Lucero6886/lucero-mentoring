# START HERE — A4-T01

**Engineering & Research Mentoring Program (Lucero)** · ThS. Đinh Văn Nam (Mr. Lucero Dinh) — Khoa Điện–Điện tử, Trường Kỹ thuật, Đại học Phenikaa

> **File sinh tự động** từ `06_Data/research_packs.json` bằng `scripts/generate_research_packs.py`. Sửa tay sẽ bị ghi đè — muốn đổi nội dung thì sửa JSON rồi chạy lại script.

**Đề tài:** Thiết kế một Digital IP từ RTL đến GDSII  
**English:** Design and Evaluation of a Digital IP from RTL to GDSII  
**Tên đầy đủ khi đăng ký:** Thiết kế và đánh giá một IP số từ RTL đến GDSII sử dụng quy trình EDA mã nguồn mở  
**Mã đối chiếu gói gốc:** T01 · **Track A** — Thiết kế IC số mã nguồn mở

---

## Câu hỏi nghiên cứu

> Các lựa chọn kiến trúc và ràng buộc physical design ảnh hưởng như thế nào đến timing, area, power và khả năng đóng thiết kế của một IP số?

Đây là câu em phải trả lời được bằng **bằng chứng**, không phải bằng một bản cài đặt chạy được.

## Trước khi gõ dòng code đầu tiên — phải đọc

- RTL design & verification fundamentals
- logic synthesis và standard-cell mapping
- static timing analysis
- floorplan, placement, CTS, routing
- DRC/LVS và sign-off concepts
- PPA và thiết kế experiment sweep

Tài liệu cụ thể xem `09_References/READING-LIST.md`. Sau mỗi tài liệu, trả lời 10 câu ở cuối file này.

## Phải hiểu được (không nhìn tài liệu)

- Khác biệt functional correctness và physical closure
- critical path/slack
- utilization và congestion
- PPA trade-off
- DRC vs LVS
- tại sao cùng RTL nhưng constraint khác tạo kết quả khác

## Phải dựng

- Chọn và viết/chuẩn hóa một IP số tham số hóa
- testbench + regression
- automation scripts cho flow
- script trích xuất PPA/timing

## Phải chạy thí nghiệm

- Baseline RTL→GDSII
- clock-period sweep
- core-utilization sweep
- architecture hoặc pipeline comparison
- re-run để kiểm tra reproducibility

## Bằng chứng bắt buộc nộp

- waveform/regression pass
- synthesis report
- STA report
- layout/GDS screenshot
- DRC/LVS summary
- CSV PPA sweep + scripts
- Pareto/summary plots

## Khi nào mới đủ điều kiện nghĩ tới một bài báo

Có systematic design-space/PPA study; ít nhất 2 cấu hình/kiến trúc có so sánh công bằng; DRC/LVS sạch; có insight tái lập vượt quá demo flow.

Tiềm năng công bố mentor đánh giá cho đề tài này: **Trung bình**. Đây là ước lượng ban đầu, không phải lời hứa — quyết định thật nằm ở Gate G7.

## Bốn câu mentor sẽ hỏi đi hỏi lại

1. IP này đủ phức tạp để có research question nhưng vẫn đóng được không?
2. Tại sao constraint này làm timing/area thay đổi?
3. Nếu layout pass DRC nhưng fail LVS nghĩa là gì?
4. Kết quả nào là insight chứ không chỉ tool output?

Nếu tuần nào em cũng trả lời được bốn câu này bằng bằng chứng của chính mình, đề tài đang đi đúng.

## Bốn quy tắc không thương lượng

1. Không có baseline thì không có phương pháp đề xuất.
2. Không có bằng chứng thì không có kết luận.
3. Không tái lập được thì đề tài chưa hoàn thành ở mức nghiên cứu.
4. Không so sánh công bằng thì không được tuyên bố trong bài báo.

## READING-QUESTIONS — trả lời sau mỗi tài liệu

1. Bài này giải quyết vấn đề gì?
2. Baseline của họ là gì?
3. Giả định nào là quan trọng?
4. Họ dùng metric nào?
5. Kết quả chính là gì?
6. Giới hạn của bài là gì?
7. Phần nào tái lập được?
8. Phần nào liên quan trực tiếp tới câu hỏi nghiên cứu của em?
9. Có kết luận nào cần kiểm chứng độc lập không?
10. Nếu chỉ lấy được một insight cho đề tài, đó là gì?

---

*Trang tổng quan đề tài: [`Topic_Guides/A4/A4-T01.md`](../../Topic_Guides/A4/A4-T01.md) · Lộ trình: `ROADMAP.md` · Cửa: `MILESTONE-GATES.md` · Thí nghiệm: `EXPERIMENTS.md`*
