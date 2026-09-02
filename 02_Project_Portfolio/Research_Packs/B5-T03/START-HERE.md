# START HERE — B5-T03

**Engineering & Research Mentoring Program (Lucero)** · ThS. Đinh Văn Nam (Mr. Lucero Dinh) — Khoa Điện–Điện tử, Trường Kỹ thuật, Đại học Phenikaa

> **File sinh tự động** từ `06_Data/research_packs.json` bằng `scripts/generate_research_packs.py`. Sửa tay sẽ bị ghi đè — muốn đổi nội dung thì sửa JSON rồi chạy lại script.

**Đề tài:** Đồng thiết kế thuật toán - phần cứng cho bộ giải mã Polar thích ứng  
**English:** Algorithm-Hardware Co-Design of an Adaptive Polar Decoder  
**Tên đầy đủ khi đăng ký:** Đồng thiết kế thuật toán–phần cứng cho bộ giải mã Polar thích ứng trên FPGA  
**Mã đối chiếu gói gốc:** T11 · **Track D** — Giải mã Polar thích ứng / hỗ trợ neural

---

## Câu hỏi nghiên cứu

> Làm thế nào ánh xạ adaptive Polar decoding thành kiến trúc phần cứng để lợi thế average-case của thuật toán vẫn tồn tại sau fixed-point, control, memory và interface overhead?

Đây là câu em phải trả lời được bằng **bằng chứng**, không phải bằng một bản cài đặt chạy được.

## Trước khi gõ dòng code đầu tiên — phải đọc

- T05–T10 foundations
- algorithm–hardware co-design
- fixed-point
- resource sharing
- FSM/control
- memory architecture
- FPGA timing/power

Tài liệu cụ thể xem `09_References/READING-LIST.md`. Sau mỗi tài liệu, trả lời 10 câu ở cuối file này.

## Phải hiểu được (không nhìn tài liệu)

- algorithmic operation vs hardware cycle
- resource sharing vs parallelism
- buffer/memory bottlenecks
- average/worst latency
- energy/frame
- control overhead

## Phải dựng

- fixed-point adaptive model
- module partition
- SC datapath
- reliability unit
- controller
- enhanced-processing interface
- RTL TB + FPGA build

## Phải chạy thí nghiệm

- bit-exact verification
- resource-sharing alternatives
- fmax/latency/throughput
- activation-dependent average latency
- power/energy estimate
- ASIC-feasibility synthesis if available

## Bằng chứng bắt buộc nộp

- architecture diagram
- bit-exact logs
- resource/timing reports
- average/worst latency
- power/energy table
- comparison with non-adaptive hardware baseline

## Khi nào mới đủ điều kiện nghĩ tới một bài báo

FPGA implementation validated; algorithmic gain survives hardware overhead; có architecture comparison và average/worst-case metrics; paper-ready khi co-design tạo insight rõ.

Tiềm năng công bố mentor đánh giá cho đề tài này: **Rất cao**. Đây là ước lượng ban đầu, không phải lời hứa — quyết định thật nằm ở Gate G7.

## Bốn câu mentor sẽ hỏi đi hỏi lại

1. Algorithm saving nào biến mất khi đưa lên hardware?
2. Control/memory overhead là bao nhiêu?
3. Average-case metric đo trên distribution nào?
4. Kiến trúc có scale với N không?

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

*Trang tổng quan đề tài: [`Topic_Guides/B5/B5-T03.md`](../../Topic_Guides/B5/B5-T03.md) · Lộ trình: `ROADMAP.md` · Cửa: `MILESTONE-GATES.md` · Thí nghiệm: `EXPERIMENTS.md`*
