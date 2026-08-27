# Tài liệu nền tảng theo từng hướng nghiên cứu

**Engineering & Research Mentoring Program (Lucero)** · ThS. Đinh Văn Nam (Mr. Lucero Dinh)
Khoa Điện–Điện tử, Trường Kỹ thuật, Đại học Phenikaa

Danh sách này trả lời câu hỏi *"em nên đọc gì trước khi bắt đầu đề tài này"*. Nó **không phải** thư mục
tham khảo đầy đủ của một luận văn — đó là việc của chính em. Đây là **điểm xuất phát đã được chọn lọc**:
mỗi mục kèm một dòng nói rõ đọc nó để làm gì và đọc vào lúc nào.

> **Quy tắc trích dẫn.** Thông tin thư mục dưới đây để **tra cứu nhanh**. Khi đưa vào báo cáo hay khóa luận,
> em phải mở nguồn gốc, kiểm lại tên tác giả, năm, tập, số trang và DOI rồi mới trích dẫn.
> Trích dẫn không kiểm chứng là lỗi học thuật — kể cả khi nó được sao từ đây, từ một bài báo khác, hay từ AI.
> Xem `01_Governance/AI_and_Academic_Integrity_Policy.md`.

**Đọc thế nào cho hiệu quả.** Đừng đọc tuần tự từ đầu đến cuối. Vòng một: đọc *abstract → hình vẽ → kết luận*
để biết bài báo trả lời câu hỏi gì. Vòng hai: đọc phần phương pháp của đúng phần em cần. Vòng ba (chỉ khi bài
đó thật sự là nền của đề tài): đọc kỹ và **tự tái lập lại một kết quả nhỏ nhất** trong đó. Một bài đã tái lập
được đáng giá hơn hai mươi bài chỉ lướt qua.

---

## 1. Nền chung — đọc trước, dùng cho mọi hướng

| Tài liệu | Đọc để làm gì |
|---|---|
| G. Wilson và cộng sự, *"Good Enough Practices in Scientific Computing"*, **PLOS Computational Biology**, 13(6), 2017. DOI: 10.1371/journal.pcbi.1005510 | Cách tổ chức dữ liệu, code và thư mục dự án sao cho sáu tháng sau chính em còn chạy lại được. Đọc trong tuần 1. |
| G. K. Sandve và cộng sự, *"Ten Simple Rules for Reproducible Computational Research"*, **PLOS Computational Biology**, 9(10), 2013. DOI: 10.1371/journal.pcbi.1003285 | Mười quy tắc ngắn về tính tái lập — đúng thứ Gate 6 kiểm tra. Đọc trước Gate 2. |
| G. M. Whitesides, *"Whitesides' Group: Writing a Paper"*, **Advanced Materials**, 16(15), 2004. DOI: 10.1002/adma.200400767 | Viết báo cáo khoa học bắt đầu từ dàn ý và hình vẽ, không phải từ câu chữ. Đọc trước Gate 5. |

---

## 2. Trục A — Thiết kế vi mạch số (A0–A5)

**Nền RTL và kiến trúc số (A1, A2, A3)**

| Tài liệu | Đọc để làm gì |
|---|---|
| D. M. Harris, S. L. Harris, *Digital Design and Computer Architecture*, Morgan Kaufmann (ấn bản RISC-V hoặc ARM) | Sách nền: logic tổ hợp/tuần tự, FSM, datapath, pipeline. Tra khi thiếu nền, không cần đọc hết. |
| C. E. Cummings, *"Nonblocking Assignments in Verilog Synthesis, Coding Styles That Kill!"*, SNUG 2000 | Vì sao dùng sai `=` và `<=` làm mạch mô phỏng đúng nhưng tổng hợp ra sai. Đọc **trước** khi viết RTL nghiêm túc. |
| C. E. Cummings, *"Simulation and Synthesis Techniques for Asynchronous FIFO Design"*, SNUG 2002 | Bài chuẩn mực về FIFO bất đồng bộ và gray-code pointer — nền cho `A1-P05` và mọi thiết kế đa miền clock. |
| Tài liệu **Verilator** và **cocotb** (trang chính thức) | Dựng testbench và kiểm chứng tự động — nền của nhóm A5 và của mọi Gate 2. |

**Tổng hợp, ASIC và dòng chảy mã nguồn mở (A4, A5)**

| Tài liệu | Đọc để làm gì |
|---|---|
| N. H. E. Weste, D. M. Harris, *CMOS VLSI Design: A Circuits and Systems Perspective*, Pearson | Hiểu điều gì thực sự diễn ra dưới lớp RTL: delay, công suất, diện tích. Tra theo chương khi làm A4. |
| T. Ajayi và cộng sự, *"Toward an Open-Source Digital Flow: First Learnings from the OpenROAD Project"*, **DAC 2019**. DOI: 10.1145/3316781.3326334 | Bức tranh tổng thể dòng chảy RTL→GDSII mã nguồn mở và những bài học khi tự động hóa nó. |
| Tài liệu **Yosys** (Y. Wolf) · **OpenROAD** · **LibreLane** (hậu thân của OpenLane 2) · **SkyWater SKY130 PDK** | Bốn tài liệu công cụ bắt buộc của nhóm A4/A5. Đọc phần *getting started* rồi chạy được ví dụ trước khi đụng đề tài. |
| J. Bhasker, R. Chadha, *Static Timing Analysis for Nanometer Designs*, Springer | Đọc khi bắt đầu phải giải thích báo cáo STA — thường rơi vào Gate 3 của đề tài A4. |

---

## 3. Nhánh Nhúng & IoT (A6, A7)

| Tài liệu | Đọc để làm gì |
|---|---|
| Tài liệu chính thức của **FreeRTOS** hoặc **Zephyr** (phần Kernel Services) | Task, ưu tiên, semaphore, hàng đợi — nền của `A6-P02` và mọi hệ thời gian thực. |
| Reference manual + datasheet của đúng vi điều khiển em dùng | Không thay thế được bằng tutorial. Kỹ năng đọc datasheet là một chuẩn đầu ra của nhánh này. |
| P. Warden, D. Situnayake, *TinyML: Machine Learning with TensorFlow Lite on Arduino and Ultra-Low-Power Microcontrollers*, O'Reilly, 2019 | Sách nền cho `A7-P03` và `A7-T02`: pipeline train → quantize → deploy trên vi điều khiển. |
| R. David và cộng sự, *"TensorFlow Lite Micro: Embedded Machine Learning for TinyML Systems"*, **MLSys 2021**. arXiv:2010.08678 | Vì sao suy luận trên MCU phải thiết kế khác trên máy chủ: bộ nhớ, cấp phát, toán tử. |
| C. Banbury và cộng sự, *"MLPerf Tiny Benchmark"*, **NeurIPS Datasets and Benchmarks**, 2021. arXiv:2106.07597 | Cách đo edge AI cho công bằng — dùng làm khung đo cho `A7-R01`. |

---

## 4. Trục B — Polar coding (B0–B6)

**Bắt buộc trước mọi đề tài trục B**

| Tài liệu | Đọc để làm gì |
|---|---|
| E. Arıkan, *"Channel Polarization: A Method for Constructing Capacity-Achieving Codes for Symmetric Binary-Input Memoryless Channels"*, **IEEE Trans. Inform. Theory**, 55(7), 2009 | Bài gốc khai sinh mã Polar. Vòng đầu chỉ cần nắm: phân cực là gì, kênh tốt/xấu, và giải mã SC hoạt động ra sao. |
| Tài liệu môn học về kênh AWGN, BPSK và LLR (bất kỳ giáo trình truyền thông số nào) | Không hiểu LLR thì không đọc được phần còn lại. Bắt buộc trước `B0-P02`. |

**Giải mã nâng cao (B3, B4, B5, B6)**

| Tài liệu | Đọc để làm gì |
|---|---|
| I. Tal, A. Vardy, *"List Decoding of Polar Codes"*, **IEEE Trans. Inform. Theory**, 61(5), 2015 | Vì sao SC đơn thuần chưa đủ tốt và list decoding vá chỗ nào — nền so sánh cho mọi cải tiến. |
| O. Afisiadis, A. Balatsoukas-Stimming, A. Burg, *"A Low-Complexity Improved Successive Cancellation Decoder for Polar Codes"*, arXiv:1412.5501, 2014 (Asilomar 2014) | Bài gốc của thuật toán **SC-Flip** — nền trực tiếp của nhóm B4 (`B4-T01`, `B4-T02`). |
| A. Balatsoukas-Stimming, M. Bastani Parizi, A. Burg, *"LLR-Based Successive Cancellation List Decoding of Polar Codes"*, **IEEE Trans. Signal Processing**, 63(19), 2015 | Chuyển SCL sang miền LLR — bước bắt buộc để đưa thuật toán xuống phần cứng. |

**Hiện thực phần cứng (B1, B2, AB)**

| Tài liệu | Đọc để làm gì |
|---|---|
| C. Leroux, A. J. Raymond, G. Sarkis, W. J. Gross, *"A Semi-Parallel Successive-Cancellation Decoder for Polar Codes"*, **IEEE Trans. Signal Processing**, 61(2), 2013 | Kiến trúc tham chiếu của bộ giải mã SC trên phần cứng — đọc trước `B2-T01`. |
| G. Sarkis và cộng sự, *"Fast Polar Decoders: Algorithm and Implementation"*, **IEEE J. Sel. Areas Commun.**, 32(5), 2014 | Cách rút ngắn độ trễ bằng cách nhận diện các nút đặc biệt trong cây giải mã. Đọc khi tối ưu. |
| **3GPP TS 38.212**, *Multiplexing and channel coding* (phần mã Polar cho kênh điều khiển 5G NR) | Bằng chứng mã Polar đang chạy trong chuẩn thật; dùng để chọn tham số cho sát thực tế. |

---

## 5. Vùng AB — Co-design thuật toán × phần cứng

| Tài liệu | Đọc để làm gì |
|---|---|
| V. Sze, Y.-H. Chen, T.-J. Yang, J. S. Emer, *"Efficient Processing of Deep Neural Networks: A Tutorial and Survey"*, **Proceedings of the IEEE**, 105(12), 2017 | Khung tư duy chuẩn cho câu hỏi "thuật toán này tốn bao nhiêu phần cứng" — nền của `AB-T05`. |
| J. L. Hennessy, D. A. Patterson, *"A New Golden Age for Computer Architecture"*, **Communications of the ACM**, 62(2), 2019 | Vì sao thiết kế chuyên dụng theo bài toán đang quay lại — bối cảnh chung của cả vùng AB. |
| M. Horowitz, *"Computing's Energy Problem (and what we can do about it)"*, **ISSCC 2014** | Con số năng lượng cho từng phép toán và từng lần truy cập bộ nhớ — nền để lập luận về `AB-T06`, `AB-R02`. |

---

## 6. Nên tra ở đâu

- **IEEE Xplore** — nguồn chính của cả hai trục A và B. Truy cập qua thư viện trường.
- **arXiv.org** (cs.IT, eess.SP) — bản tiền ấn phẩm, thường có trước bản tạp chí một đến hai năm.
- **Google Scholar** — dùng nút *Cited by* để đi ngược từ bài gốc tới các cải tiến mới nhất.
- **Semantic Scholar / Connected Papers** — dựng bản đồ quan hệ giữa các bài, hữu ích khi bắt đầu một hướng mới.

> **Cảnh báo thường gặp.** Đừng để "đọc tài liệu" trở thành chỗ trốn khỏi việc làm. Ở chương trình này,
> đọc chỉ được tính là tiến độ khi biến thành một **ghi chú kỹ thuật** nêu rõ: *bài toán – đầu vào – đầu ra –
> phương pháp – tiêu chí đo – chỗ em chưa hiểu*. Xem `10_Documentation/STUDENT-GUIDE.md` §2.

---

*Đề xuất bổ sung tài liệu cho danh sách này: mở Issue trong repo, nêu rõ tài liệu và nó phục vụ nhóm đề tài nào.*
