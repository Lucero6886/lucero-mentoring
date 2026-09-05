# START HERE — B2-T01

**Engineering & Research Mentoring Program (Lucero)** · ThS. Đinh Văn Nam (Mr. Lucero Dinh) — Khoa Điện–Điện tử, Trường Kỹ thuật, Đại học Phenikaa

> **File sinh tự động** từ `06_Data/research_packs.json` bằng `scripts/generate_research_packs.py`. Sửa tay sẽ bị ghi đè — muốn đổi nội dung thì sửa JSON rồi chạy lại script.

**Đề tài:** Thiết kế bộ giải mã SC Polar trên FPGA  
**English:** FPGA Architecture and Implementation of an SC Polar Decoder  
**Tên đầy đủ khi đăng ký:** Thiết kế và đánh giá kiến trúc bộ giải mã Polar Successive Cancellation trên FPGA  
**Mã đối chiếu gói gốc:** T05 · **Track C** — Kiến trúc bộ giải mã Polar

---

## Câu hỏi nghiên cứu

> Một kiến trúc SC Polar decoder có thể được ánh xạ lên FPGA với correctness, latency, throughput và resource cost như thế nào?

Đây là câu em phải trả lời được bằng **bằng chứng**, không phải bằng một bản cài đặt chạy được.

## Trước khi gõ dòng code đầu tiên — phải đọc

- Polar codes fundamentals
- channel polarization/frozen bits
- BPSK AWGN and LLR
- SC decoding tree
- f/g operations
- partial sums
- FPGA architecture/verification

Tài liệu cụ thể xem `09_References/READING-LIST.md`. Sau mỗi tài liệu, trả lời 10 câu ở cuối file này.

## Phải hiểu được (không nhìn tài liệu)

- N,K,R
- frozen vs information bits
- LLR sign/magnitude
- SC traversal dependencies
- BER vs BLER
- algorithm latency vs cycle latency

## Phải dựng

- Python/MATLAB encoder+channel+SC golden model
- RTL f/g/partial-sum/control modules
- testbench co-verification
- FPGA synthesis scripts

## Phải chạy thí nghiệm

- software BLER baseline
- small-N hand check
- Python/MATLAB↔RTL vector test
- N/K or SNR sweeps
- FPGA synthesis and timing

## Bằng chứng bắt buộc nộp

- BLER/BER curves
- known-vector tests
- RTL waveforms
- bit-exact co-verification logs
- LUT/FF/BRAM/fmax/latency/throughput table

## Khi nào mới đủ điều kiện nghĩ tới một bài báo

Baseline architecture validated; FPGA metrics đầy đủ; chỉ paper nếu có architectural choice/optimization/comparison tạo insight ngoài việc implement SC.

Tiềm năng công bố mentor đánh giá cho đề tài này: **Trung bình**. Đây là ước lượng ban đầu, không phải lời hứa — quyết định thật nằm ở Gate G7.

## Bốn câu mentor sẽ hỏi đi hỏi lại

1. Tại sao bit này frozen?
2. LLR âm/dương và độ lớn nói gì?
3. Latency được đo từ cycle nào tới cycle nào?
4. RTL và software mismatch ở f/g hay partial sum?

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

*Trang tổng quan đề tài: [`02_Project_Portfolio/Topic_Guides/B2/B2-T01.md`](../../Topic_Guides/B2/B2-T01.md) · Lộ trình: `ROADMAP.md` · Cửa: `MILESTONE-GATES.md` · Thí nghiệm: `EXPERIMENTS.md`*
