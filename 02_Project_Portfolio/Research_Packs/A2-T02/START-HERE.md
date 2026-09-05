# START HERE — A2-T02

**Engineering & Research Mentoring Program (Lucero)** · ThS. Đinh Văn Nam (Mr. Lucero Dinh) — Khoa Điện–Điện tử, Trường Kỹ thuật, Đại học Phenikaa

> **File sinh tự động** từ `06_Data/research_packs.json` bằng `scripts/generate_research_packs.py`. Sửa tay sẽ bị ghi đè — muốn đổi nội dung thì sửa JSON rồi chạy lại script.

**Đề tài:** Thiết kế và tối ưu MAC datapath cho FPGA/ASIC  
**English:** Design and Optimization of a Fixed-Point MAC Datapath for FPGA/ASIC  
**Tên đầy đủ khi đăng ký:** Thiết kế MAC datapath và đánh giá ảnh hưởng của bit-width và pipeline đến độ chính xác và chi phí phần cứng  
**Mã đối chiếu gói gốc:** T03 · **Track B** — Kiến trúc phần cứng số

---

## Câu hỏi nghiên cứu

> Bit-width và mức pipeline thay đổi numerical accuracy, latency, throughput, area và power của MAC datapath như thế nào?

Đây là câu em phải trả lời được bằng **bằng chứng**, không phải bằng một bản cài đặt chạy được.

## Trước khi gõ dòng code đầu tiên — phải đọc

- fixed-point arithmetic
- quantization error
- MAC architecture
- pipelining
- RTL arithmetic
- FPGA/ASIC PPA metrics

Tài liệu cụ thể xem `09_References/READING-LIST.md`. Sau mỗi tài liệu, trả lời 10 câu ở cuối file này.

## Phải hiểu được (không nhìn tài liệu)

- Q-format
- overflow/saturation/rounding
- latency vs throughput
- critical path
- why pipeline may raise registers but improve fmax
- Pareto frontier

## Phải dựng

- floating-point golden model
- fixed-point model
- parameterized RTL MAC
- self-checking testbench
- sweep scripts

## Phải chạy thí nghiệm

- bit-width sweep
- fractional-bit allocation
- pipeline-depth sweep
- rounding/saturation comparison
- FPGA/ASIC resource/timing evaluation

## Bằng chứng bắt buộc nộp

- numerical error plots
- RTL-vs-golden equivalence results
- LUT/FF or area reports
- fmax/latency/throughput table
- Pareto plot

## Khi nào mới đủ điều kiện nghĩ tới một bài báo

Có design-space sweep đủ rộng, numerical + hardware metrics, Pareto analysis, ít nhất một insight kiến trúc/quantization có tính tổng quát.

Tiềm năng công bố mentor đánh giá cho đề tài này: **Cao**. Đây là ước lượng ban đầu, không phải lời hứa — quyết định thật nằm ở Gate G7.

## Bốn câu mentor sẽ hỏi đi hỏi lại

1. Accuracy được định nghĩa bằng metric nào?
2. Hai cấu hình pipeline có cùng chức năng và precision không?
3. Fmax cao hơn có thực sự cải thiện throughput ở interface này?
4. Điểm Pareto nào hợp lý và vì sao?

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

*Trang tổng quan đề tài: [`02_Project_Portfolio/Topic_Guides/A2/A2-T02.md`](../../Topic_Guides/A2/A2-T02.md) · Lộ trình: `ROADMAP.md` · Cửa: `MILESTONE-GATES.md` · Thí nghiệm: `EXPERIMENTS.md`*
