# Điều kiện qua từng cửa — B2-T01

**Engineering & Research Mentoring Program (Lucero)** · ThS. Đinh Văn Nam (Mr. Lucero Dinh) — Khoa Điện–Điện tử, Trường Kỹ thuật, Đại học Phenikaa

> **File sinh tự động** từ `06_Data/research_packs.json` bằng `scripts/generate_research_packs.py`. Sửa tay sẽ bị ghi đè — muốn đổi nội dung thì sửa JSON rồi chạy lại script.

**Đề tài:** Thiết kế bộ giải mã SC Polar trên FPGA  
**English:** FPGA Architecture and Implementation of an SC Polar Decoder  
**Tên đầy đủ khi đăng ký:** Thiết kế và đánh giá kiến trúc bộ giải mã Polar Successive Cancellation trên FPGA  
**Mã đối chiếu gói gốc:** T05 · **Track C** — Kiến trúc bộ giải mã Polar

---


Bảng dưới ghép **yêu cầu chung của chương trình** (G0–G7) với **nội dung riêng của đề tài này**. G0–G6 nằm gọn trong Gate 1–6 của khung 15 tuần; G7 là cửa mở rộng.


## G0 — Sẵn sàng (Readiness)

**Thuộc:** Gate 1

**Phải hiểu — riêng đề tài này:** N,K,R, frozen vs information bits, LLR sign/magnitude, SC traversal dependencies

**Đạt khi:**
- diễn giải vấn đề bằng lời của mình, không đọc slide
- vẽ được sơ đồ đầu vào → xử lý → đầu ra
- định nghĩa được baseline
- định nghĩa được metric
- chỉ ra biến độc lập và biến phụ thuộc
- mô tả được một thí nghiệm công bằng
- giải thích tối thiểu 5 thuật ngữ cốt lõi của đề tài

**Mentor hỏi:** Tại sao bit này frozen?

**Không đạt khi:** Chỉ đọc slide hoặc bản tóm tắt của AI mà không giải thích được bản chất.


## G1 — Tài liệu và phát biểu vấn đề (Literature & Problem Formulation)

**Thuộc:** Gate 1

**Đạt khi:**
- 8–15 nguồn liên quan, gồm cả nguồn nền tảng và nguồn gần nhất
- bảng so sánh tài liệu (literature matrix)
- problem statement 150–300 từ
- một câu hỏi nghiên cứu kiểm chứng được
- giả thuyết có thể bác bỏ được
- phạm vi và những gì cố tình không làm (non-goals)

**Không đạt khi:** Khoảng trống nghiên cứu mơ hồ, không có baseline/metric, hoặc phạm vi quá lớn.


## G2 — Tái lập baseline (Baseline Reproduction)

**Thuộc:** Gate 2

**Phải dựng — riêng đề tài này:** Python/MATLAB encoder+channel+SC golden model, RTL f/g/partial-sum/control modules

**Đạt khi:**
- baseline chạy được đầu-cuối
- kết quả khớp kỳ vọng/tài liệu, hoặc sai khác được giải thích
- config, seed và version đều được lưu
- người khác chạy lại được
- có ít nhất một hình hoặc bảng của baseline

**Mentor hỏi:** LLR âm/dương và độ lớn nói gì?

**Không đạt khi:** Baseline sai hoặc chưa rõ nhưng nhóm đã chuyển sang phương pháp đề xuất.


## G3 — Cài đặt phương pháp đề xuất (Proposed / Design Implementation)

**Thuộc:** Gate 3

**Phải dựng — riêng đề tài này:** testbench co-verification, FPGA synthesis scripts

**Đạt khi:**
- phương pháp hoặc kiến trúc mới có block diagram / pseudocode
- cài đặt có unit test
- không phá vỡ baseline
- có sanity check và các trường hợp biên

**Mentor hỏi:** Latency được đo từ cycle nào tới cycle nào?

**Không đạt khi:** Thay nhiều cơ chế cùng lúc nên không quy được kết quả về nguyên nhân nào.


## G4 — Thí nghiệm có kiểm soát (Controlled Experiment)

**Thuộc:** Gate 4

**Thí nghiệm trọng tâm — riêng đề tài này:** software BLER baseline, small-N hand check, Python/MATLAB↔RTL vector test, N/K or SNR sweeps, FPGA synthesis and timing

**Đạt khi:**
- ma trận thí nghiệm được khóa trước khi chạy
- baseline và phương pháp đề xuất chạy cùng điều kiện
- đủ số seed/mẫu/frame theo yêu cầu của bài toán
- log tự động hoặc bán tự động
- hình và bảng sinh từ dữ liệu gốc

**Không đạt khi:** Chọn lọc kết quả đẹp, hoặc đổi giao thức sau khi đã thấy kết quả mà không ghi nhận.


## G5 — Bằng chứng và phân tích (Evidence & Analysis)

**Thuộc:** Gate 5

**Bằng chứng trọng tâm — riêng đề tài này:** BLER/BER curves, known-vector tests, RTL waveforms, bit-exact co-verification logs, LUT/FF/BRAM/fmax/latency/throughput table

**Đạt khi:**
- mọi kết luận đều trỏ tới một hình/bảng/log cụ thể
- có phân tích nguyên nhân, không chỉ mô tả xu hướng
- có ít nhất một failure case
- có sensitivity hoặc ablation khi cần
- có phần giới hạn của nghiên cứu

**Mentor hỏi:** RTL và software mismatch ở f/g hay partial sum?

**Không đạt khi:** Chỉ mô tả 'tăng/giảm' mà không lý giải được vì sao.


## G6 — Khả năng tái lập (Reproducibility)

**Thuộc:** Gate 6

**Đạt khi:**
- clone sạch và chạy được theo README
- ghi rõ môi trường và phiên bản công cụ
- config và seed cố định
- tách riêng kết quả thô và kết quả đã xử lý
- có script tạo lại hình/bảng

**Không đạt khi:** Kết quả chỉ tồn tại trên máy sinh viên hoặc phụ thuộc thao tác thủ công không ghi lại.


## G7 — Sẵn sàng viết bài (Paper Readiness)

**Thuộc:** mở rộng (ngoài khung 15 tuần)

**Ngưỡng riêng của đề tài — riêng đề tài này:** Baseline architecture validated; FPGA metrics đầy đủ; chỉ paper nếu có architectural choice/optimization/comparison tạo insight ngoài việc implement SC.

**Đạt khi:**
- đóng góp mới phát biểu được trong 1–3 câu
- baseline công bằng và đủ mạnh
- kết quả không dừng ở mức 'chạy được'
- có 2–4 hình/bảng đạt chuẩn bản thảo
- có dàn ý abstract, danh sách đóng góp và giới hạn
- mentor xác nhận venue phù hợp

**Không đạt khi:** Chỉ có bản cài đặt hoặc demo; hoặc phương pháp đề xuất không tạo lợi ích ròng đáng kể.
