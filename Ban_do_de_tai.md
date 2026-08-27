# Bản đồ 105 đề tài & cách sử dụng hệ thống

**Engineering & Research Mentoring Program (Lucero)** · Phiên bản hệ thống 1.5.1 · 2026-08-23
Tác giả & mentor: ThS. Đinh Văn Nam (Mr. Lucero Dinh) — Khoa Điện–Điện tử, Trường Kỹ thuật, Đại học Phenikaa
Bản web (mở từ điện thoại, chia sẻ được): https://claude.ai/code/artifact/68a2de47-bc1e-41cc-b588-cd34ffd90c90

> Đây là chương trình **dài hạn, nhiều học kỳ** — quản lý NCKH, luận án, thực tập và mentor cộng đồng IC design; mỗi học kỳ chạy một cohort (hiện tại: DATN HK1 2026-2027).
>
> Tài liệu này trả lời hai câu hỏi bằng ngôn ngữ đời thường: **mỗi đề tài trong 105 đề tài thực chất là làm cái gì**, và **anh dùng kho đề tài này thế nào cho ba việc: giảng dạy – mentor – nghiên cứu**. Nó là bản diễn giải của dữ liệu nguồn chuẩn `06_Data/project_portfolio.json`; khi lệch nhau, JSON thắng. Bản dễ đọc: `Ban_do_84_de_tai.html`.

---

## 1. Bức tranh lớn trong một phút

Kho đề tài là một **tấm bản đồ hai trục, bốn bậc thang**:

- **Trục A — làm chip số** (A0→A5): từ hàn mạch bằng tay, viết Verilog, làm toán trên phần cứng, chạy trên FPGA, đến biến code thành bản vẽ chip (GDSII) và xây hạ tầng kiểm chứng. **Từ v1.5.0 mở rộng thêm nhánh Nhúng & IoT (A6, A7)**: firmware, RTOS, SoC, kết nối IoT và AI tại biên.
- **Trục B — giải mã Polar** (7 nhóm B0→B6): từ mô phỏng thuật toán trên máy tính, dựng từng viên gạch phần cứng, lắp thành bộ giải mã, đến các câu hỏi nghiên cứu: lượng tử hóa, SC-Flip, giải mã thích ứng, AI hỗ trợ.
- **Vùng giao AB**: đem thuật toán Polar đi trả lời câu hỏi phần cứng — chất liệu nghiên cứu "hardware-aware" đúng nghĩa.

Mỗi nhóm có 4 loại hoạt động, xếp như **bậc thang trách nhiệm** — cùng một chủ đề nhưng đòi hỏi tăng dần:

| Bậc | Loại | Bản chất | Câu hỏi định nghĩa |
|---|---|---|---|
| 1 | **P** — Project môn học (42 đề tài) | *Học* một kỹ năng cụ thể, không cần mới | "Em đã làm được kỹ năng X chưa?" |
| 2 | **I** — Thực tập (15) | *Tập làm việc* theo quy trình kỹ sư thật | "Em làm việc có kỷ luật kỹ thuật chưa?" |
| 3 | **T** — Đồ án tốt nghiệp (34) | *Sở hữu* một sản phẩm trọn vẹn: đúng, đủ, tái lập được, có số liệu | "Đây có phải sản phẩm hoàn chỉnh của riêng em không?" |
| 4 | **R** — Nghiên cứu (14) | *Trả lời một câu hỏi chưa có đáp án*, chấp nhận kết quả phủ định | "Em đã chứng minh/bác bỏ giả thuyết bằng bằng chứng chưa?" |

Kèm theo là **thang trưởng thành L0–L5** của sinh viên (L0 mới khám phá → L5 sẵn sàng nghiên cứu nâng cao). Mỗi đề tài ghi một mức **sàn** (`min_level`): dưới sàn vẫn có thể nhận, nhưng phải ghi lý do và thu hẹp phạm vi.

Chuỗi nối tiếp tự nhiên giữa các nhóm:

```
Trục A (chip):    A0 hàn mạch → A1 Verilog → A2 mạch làm toán → A3 FPGA → A4 ra chip → A5 hạ tầng kiểm chứng
Nhánh nhúng-IoT:  A6 nhúng/SoC → A7 IoT & AI biên   (mở từ v1.5.0)
Trục B (Polar):   B0 mô phỏng → B1 viên gạch RTL → B2 bộ giải mã → B3 bao nhiêu bit? → B4 SC-Flip → B5 thích ứng → B6 AI hỗ trợ
Gặp nhau tại:     AB — co-design: Polar/edge-AI đo bằng thước phần cứng (PPA, năng lượng) — định hướng luận án
```

---

## 2. Đi một vòng 16 nhóm — mỗi đề tài làm ra cái gì

Cách đọc bảng: **Mã chuẩn** là định danh vĩnh viễn trong hệ thống; cột **HK1** là mã rút gọn sinh viên nhìn thấy trong danh mục DATN kỳ này (chỉ 21 đề tài T đang mở có mã này); **Sàn** là level tối thiểu nên có; **Làm ra** tóm tắt sản phẩm nộp được lấy từ nguồn chuẩn.

### A0 · Hands-on Electronics & PCB — Điện tử cầm tay được

Nhóm khởi đầu cho sinh viên chưa từng chạm phần cứng: vẽ sơ đồ mạch, tự làm PCB, hàn linh kiện, cắm que đo. Một buổi làm việc điển hình là ngồi với mỏ hàn, đồng hồ đo và oscilloscope, debug tại sao mạch thật không chạy giống mạch trên giấy — chính cảm giác đó tạo ra trực giác phần cứng.

*Đi tiếp:* Xong A0, sinh viên đủ tự tin để sang A1 (mô tả mạch bằng code) hoặc A3 (ghép board tự làm với FPGA).

| Mã | Loại | Sàn | HK1 | Đề tài | Làm ra |
|---|---|---|---|---|---|
| `A0-P01` | P | L0 | — | Thiết kế và tự chế tạo thủ công mạch nguồn DC cơ bản | Schematic; PCB layout; PCB tự chế tạo; board lắp ráp; kết quả đo tải/ripple; debugging log |
| `A0-P02` | P | L0 | — | Thiết kế và chế tạo mạch logic tổ hợp trên PCB | Truth table; schematic; PCB; board thật; measurement; failure-fix evidence |
| `A0-P03` | P | L0 | — | Thiết kế và chế tạo bộ đếm số trên PCB | Schematic; PCB; counter + display hoạt động; test reset/clock; debugging report |
| `A0-P04` | P | L0 | — | Thiết kế board giao tiếp cảm biến | Requirement; datasheet note; schematic; PCB; board; measurement |
| `A0-P05` | P | L1 | — | Thiết kế embedded controller board cơ bản | Schematic; PCB; power/reset/clock/I/O; firmware test; board demo |
| `A0-P06` | P | L1 | — | Thiết kế PCB mở rộng I/O cho FPGA | PCB extension; interface test; FPGA demo; documentation |
| `A0-I01` | I | L1 | — | Thực tập thiết kế, chế tạo và kiểm thử phần cứng điện tử | Working board; design files; BOM; measurement; debug log; technical report; legacy package |

### A1 · Digital Logic & RTL Design — Viết code sinh ra mạch số

Học Verilog: viết văn bản mô tả mạch, mô phỏng, rồi soi dạng sóng (waveform) để kiểm tra đúng sai. Một buổi làm việc điển hình là viết module + testbench, chạy simulator, dò từng xung clock. Đây là nền móng của toàn bộ trục A và trục B phần cứng — hầu hết sinh viên đi qua đây.

*Đi tiếp:* Xong A1, rẽ được ba hướng: A2 (mạch làm toán), A3 (lên FPGA thật), A5 (kiểm chứng bài bản).

| Mã | Loại | Sàn | HK1 | Đề tài | Làm ra |
|---|---|---|---|---|---|
| `A1-P01` | P | L0 | — | Thiết kế các mạch logic tổ hợp bằng Verilog | RTL; testbench; waveform; short report |
| `A1-P02` | P | L0 | — | Thiết kế các mạch tuần tự bằng Verilog | RTL; reset tests; waveform; report |
| `A1-P03` | P | L1 | — | Thiết kế FSM cho một bộ điều khiển số | Specification; state diagram; RTL; tests; waveform |
| `A1-P04` | P | L1 | — | Thiết kế UART transmitter/receiver bằng RTL | UART RTL; loopback testbench; waveform; README |
| `A1-P05` | P | L1 | — | Thiết kế synchronous FIFO bằng RTL | FIFO RTL; full/empty/overflow/underflow tests; waveform |
| `A1-I01` | I | L1 | — | Thiết kế và kiểm chứng reusable Digital IP Core | Specification; reusable RTL; testbench; regression; documentation; repo |
| `A1-T01` | T | L2 | **A4** | Thiết kế và kiểm chứng một IP số có khả năng tái sử dụng | Complete IP; systematic verification; synthesis report; documentation; legacy package |

### A2 · Digital Arithmetic & DSP Hardware — Mạch số làm toán

Thiết kế phần cứng cộng, nhân, lọc tín hiệu — và học bài toán trung tâm của nghề: dùng bao nhiêu bit là đủ (fixed-point)? Thêm bit thì chính xác hơn nhưng mạch to hơn, chậm hơn. Mỗi đề tài đều kết thúc bằng một bảng so sánh đánh đổi.

*Đi tiếp:* Xong A2, sinh viên sẵn sàng cho A3/A4, và đây cũng chính là kỹ năng mà nhánh B3 (lượng tử hóa Polar) cần.

| Mã | Loại | Sàn | HK1 | Đề tài | Làm ra |
|---|---|---|---|---|---|
| `A2-P01` | P | L1 | — | Thiết kế và so sánh các kiến trúc bộ cộng số | RTL nhiều architecture; functional tests; synthesis comparison |
| `A2-P02` | P | L1 | — | Thiết kế multiplier fixed-point | Reference model; RTL; overflow/truncation tests; synthesis |
| `A2-P03` | P | L1 | — | Thiết kế Multiply-Accumulate datapath | MAC RTL; pipeline tests; resource/timing report |
| `A2-P04` | P | L1 | — | Thiết kế bộ lọc FIR bằng RTL | Floating reference; RTL; fixed-point test; waveform |
| `A2-I01` | I | L2 | — | Thiết kế và triển khai datapath DSP fixed-point trên FPGA | Golden model; RTL; FPGA synthesis; resource/Fmax/latency; report |
| `A2-T01` | T | L2 | **A3** | Thiết kế bộ lọc FIR fixed-point trên FPGA và khảo sát ASIC | Reference; quantization; RTL; FPGA results; ASIC synthesis/physical evidence phù hợp; analysis |
| `A2-T02` | T | L2 | **A9** | Thiết kế và tối ưu MAC datapath cho FPGA/ASIC | Multiple configurations; PPA/resource/timing; accuracy; report |
| `A2-T03` | T | L2 | **A8** | Thiết kế và đánh giá PPA của các kiến trúc bộ cộng số học | RTL các kiến trúc RCA/CLA/carry-select (tùy chọn parallel-prefix); functional-equivalence tests; synthesis/STA cùng constraint;… |
| `A2-R01` | R | L4 | — | Hardware design-space exploration cho fixed-point datapath | Reproducible sweep; Pareto analysis; research report/paper-ready figures |

### A3 · FPGA System Design — Cho thiết kế chạy trên phần cứng thật

Đưa RTL lên board FPGA: nạp bitstream, nối với thiết bị ngoài, đo tốc độ tối đa (Fmax) và lượng tài nguyên chiếm dụng. Khoảnh khắc thiết kế của mình nhấp nháy trên board thật là cột mốc tâm lý lớn của sinh viên.

*Đi tiếp:* Xong A3, đi tiếp A4 (biến RTL thành chip) hoặc nhận các đề tài hệ thống lớn hơn.

| Mã | Loại | Sàn | HK1 | Đề tài | Làm ra |
|---|---|---|---|---|---|
| `A3-P01` | P | L1 | — | Triển khai một Digital IP trên FPGA | Bitstream/project; hardware demo; resource/Fmax; README |
| `A3-P02` | P | L1 | — | FPGA interfacing với peripheral | Interface RTL; board demo; tests; documentation |
| `A3-P03` | P | L2 | — | Hệ thống xử lý tín hiệu số trên FPGA | Working DSP pipeline; resource/timing; hardware test |
| `A3-I01` | I | L2 | — | Xây dựng hệ thống FPGA tích hợp nhiều IP | Integrated system; interface tests; demo; documentation |
| `A3-T01` | T | L2 | **A5** | Thiết kế hệ thống xử lý dữ liệu số pipelined trên FPGA | Architecture; RTL; verification; FPGA; LUT/FF/DSP/Fmax/latency/throughput analysis |
| `A3-T02` | T | L2 | — | Hardware/software co-verification cho hệ thống FPGA | Golden model; vector generation; RTL/FPGA agreement; automated comparison; report |

### A4 · ASIC Design & Physical Implementation — Từ code đến con chip trên bản vẽ

Đi trọn con đường RTL → synthesis → kiểm tra timing (STA) → sắp đặt vật lý → GDSII (bản vẽ cuối cùng gửi nhà máy) bằng toolchain mã nguồn mở. Sinh viên học đọc ba con số quyết định của nghề IC: hiệu năng – công suất – diện tích (PPA).

*Đi tiếp:* Xong A4, sinh viên đủ nền nhận đề tài nghiên cứu (R) hoặc các đề tài cầu nối AB.

| Mã | Loại | Sàn | HK1 | Đề tài | Làm ra |
|---|---|---|---|---|---|
| `A4-P01` | P | L1 | — | Làm quen RTL-to-Gates bằng Yosys | RTL; synthesis script; netlist/report; explanation |
| `A4-P02` | P | L2 | — | Khảo sát ảnh hưởng của RTL coding style tới synthesis | Equivalent RTL variants; synthesis evidence; comparison |
| `A4-I01` | I | L2 | — | Xây dựng môi trường RTL-to-GDSII mã nguồn mở | Reproducible setup; sample designs; documented commands; troubleshooting notes |
| `A4-T01` | T | L2 | **A1** | Thiết kế một Digital IP từ RTL đến GDSII | Spec; RTL; testbench; synthesis; STA; physical implementation; DRC/LVS evidence; GDSII; PPA report |
| `A4-T02` | T | L3 | **A2** | Khảo sát ảnh hưởng kiến trúc RTL đến PPA | 2+ functionally equivalent architectures; controlled PPA comparison; analysis |
| `A4-R01` | R | L4 | — | Design-space exploration cho một Digital IP | Automated experiments; statistical/controlled analysis; research report |

### A5 · Verification, EDA & Reproducible Hardware Development — Nghề giữ cho dự án sống

Testbench có hệ thống, chạy kiểm tra tự động lặp lại (regression), Git/CI, môi trường công cụ dựng lại được một lệnh. Nghe ít hào nhoáng nhưng đây là thứ công ty chip nào cũng tuyển — và đề tài ở nhóm này xây hạ tầng dùng chung cho cả các khóa sau.

*Đi tiếp:* Sản phẩm nhóm A5 (quy trình LibreLane+Nix, CI) trở thành nền cho mọi đề tài A4/AB về sau.

| Mã | Loại | Sàn | HK1 | Đề tài | Làm ra |
|---|---|---|---|---|---|
| `A5-P01` | P | L1 | — | Xây dựng testbench có hệ thống cho một RTL module | Test plan; testbench; pass/fail evidence; bug log |
| `A5-P02` | P | L2 | — | Regression testing cho Digital IP | Regression script; test set; summary report; reproducible run |
| `A5-I01` | I | L1 | — | Xây dựng Git workflow cho dự án RTL | Repo structure; branches/issues; README; test scripts; contribution guide |
| `A5-T01` | T | L3 | **A6** | Xây dựng quy trình ASIC tái lập sử dụng LibreLane + Nix | Pinned environment; 3 reference designs; repeatability evidence; docs; troubleshooting |
| `A5-T02` | T | L3 | **A7** | Continuous Integration cho dự án RTL/ASIC | CI pipeline; lint/sim/regression/synthesis reports; failure examples; docs |
| `A5-R01` | R | L4 | — | Automated PPA regression cho Digital IC | Dataset of commits/configurations; regression thresholds; analysis; research report |

### A6 · Embedded Systems & SoC Integration — Nhúng: phần mềm chạy sát phần cứng

Nhóm mở đầu nhánh Nhúng & IoT của trục A (mở từ v1.5.0): viết firmware điều khiển ngoại vi thật, dùng RTOS chia việc theo thời gian thực, rồi lên SoC FPGA — nơi một nửa hệ thống là phần cứng mình thiết kế, nửa kia là phần mềm mình viết. Chính ở ranh giới đó sinh viên học được câu hỏi trung tâm của co-design: việc gì để phần mềm làm, việc gì đáng đưa xuống phần cứng.

*Đi tiếp:* Xong A6, đi tiếp A7 (kết nối IoT, AI biên) hoặc A6-T02/AB-T05 (tăng tốc phần cứng — cửa vào co-design).

| Mã | Loại | Sàn | HK1 | Đề tài | Làm ra |
|---|---|---|---|---|---|
| `A6-P01` | P | L1 | — | Lập trình firmware bare-metal điều khiển ngoại vi vi điều khiển | Driver UART/I2C/SPI tự viết (không dùng HAL sinh sẵn cho phần lõi); firmware demo; đo kiểm bằng logic analyzer; README |
| `A6-P02` | P | L1 | — | Ứng dụng đa nhiệm thời gian thực với RTOS | Ứng dụng FreeRTOS/Zephyr >=3 task; phân tích ưu tiên/deadline; đo jitter/latency; báo cáo so sánh với bản super-loop |
| `A6-P03` | P | L2 | — | Giao tiếp phần cứng-phần mềm trên SoC FPGA | IP memory-mapped đơn giản (thanh ghi điều khiển/trạng thái); driver C phía processor; test đọc-ghi qua bus; README |
| `A6-P04` | P | L2 | — | Dựng Linux nhúng trên SoC FPGA và viết driver đơn giản | Ảnh Linux boot được trên board; driver ký tự hoặc UIO nói chuyện với một IP; log kiểm chứng; hướng dẫn dựng lại từ đầu |
| `A6-I01` | I | L2 | — | Thực tập phát triển sản phẩm nhúng theo quy trình kỹ sư | Sản phẩm nhúng nhỏ đi trọn quy trình: yêu cầu -> thiết kế -> firmware -> kiểm thử -> tài liệu; nhật ký tuần; repo Git kỷ luật |
| `A6-T01` | T | L2 | — | Thiết kế hệ thống nhúng điều khiển và thu thập dữ liệu hoàn chỉnh | Hệ thống nhúng chạy thật (>=2 ngoại vi, RTOS hoặc kiến trúc phần mềm rõ); kiểm thử hệ thống; đo hiệu năng/độ tin cậy; khóa luận;… |
| `A6-T02` | T | L3 | — | Tích hợp bộ tăng tốc phần cứng tùy biến vào SoC FPGA | Baseline phần mềm có profile; IP accelerator RTL; driver + tích hợp; benchmark speedup; phân tích trade-off tài nguyên/độ trễ;… |
| `A6-R01` | R | L4 | — | Nghiên cứu phân hoạch phần cứng/phần mềm cho ứng dụng nhúng | Research question rõ; phương pháp phân hoạch + tiêu chí; >=2 phương án phân hoạch đo trên cùng benchmark; phân tích… |

### A7 · IoT Systems & Edge Intelligence — IoT và trí tuệ tại biên

Nối các thiết bị nhúng thành hệ thống hoàn chỉnh: cảm biến, giao thức (MQTT/BLE/LoRa), và bài toán sống còn của thiết bị chạy pin — ngân sách năng lượng. Tầng trên cùng là edge AI: nén mô hình học máy xuống vài trăm KB để suy luận ngay trên vi điều khiển. Mọi đề tài đều bắt sinh viên đo trên thiết bị thật, chạy nhiều ngày thật.

*Đi tiếp:* Xong A7, sinh viên đủ nền cho các đề tài co-design AB (tăng tốc AI biên, decoder tiết kiệm năng lượng) và các đề tài R hướng luận án.

| Mã | Loại | Sàn | HK1 | Đề tài | Làm ra |
|---|---|---|---|---|---|
| `A7-P01` | P | L1 | — | Nút cảm biến IoT truyền dữ liệu qua MQTT | Node ESP32/STM32 đọc cảm biến thật, publish MQTT có xử lý mất kết nối; broker + dashboard tối giản; log chạy >=48h; README |
| `A7-P02` | P | L2 | — | Đo và tối ưu năng lượng cho nút IoT chạy pin | Current profile từng trạng thái (active/tx/sleep); chiến lược duty-cycle; bảng ước tính thời gian sống pin trước/sau tối ưu; báo… |
| `A7-P03` | P | L2 | — | Suy luận TinyML trên vi điều khiển | Mô hình nhỏ (keyword spotting/gesture) huấn luyện + quantize INT8; chạy trên MCU; bảng accuracy/latency/RAM-Flash; demo; README |
| `A7-P04` | P | L1 | — | Đánh giá kết nối không dây tầm ngắn/tầm xa cho IoT | Thí nghiệm BLE và LoRa (hoặc 2 công nghệ được duyệt): tầm phủ, tỉ lệ mất gói, năng lượng/gói theo khoảng cách; báo cáo so sánh có… |
| `A7-I01` | I | L2 | — | Thực tập xây dựng hệ thống IoT đầu-cuối | Hệ thống node -> gateway -> lưu trữ -> dashboard vận hành liên tục >=2 tuần; số liệu uptime/mất gói; nhật ký sự cố và cách xử lý;… |
| `A7-T01` | T | L2 | — | Thiết kế và đánh giá hệ thống giám sát IoT đa nút hoàn chỉnh | Hệ thống >=3 node chạy pin + gateway + dashboard; đánh giá định lượng: uptime, mất gói, thời gian sống pin; khóa luận; repo + tài… |
| `A7-T02` | T | L3 | — | Triển khai và tối ưu mô hình AI gọn nhẹ trên thiết bị biên | Pipeline train->quantize->deploy tái lập; so sánh có hệ thống float/INT8 (accuracy, latency, RAM/Flash, năng lượng/suy luận);… |
| `A7-R01` | R | L4 | — | Nghiên cứu đánh đổi độ chính xác – năng lượng – độ trễ cho suy luận tại biên | Research question + giả thuyết; ma trận thí nghiệm (mô hình × mức quantize × tần số/điện áp nếu có); đường cong trade-off; phân… |

### B0 · Polar Fundamentals & Software Baseline — Polar trên máy tính, chưa đụng phần cứng

Viết mô phỏng Polar code bằng Python/MATLAB: mã hóa, truyền qua kênh nhiễu, giải mã SC, vẽ đường cong tỉ lệ lỗi (BER/BLER). Kết quả quan trọng nhất là một 'golden model' — mô hình tham chiếu đúng mà mọi đề tài B phía sau đem phần cứng ra đối chiếu.

*Đi tiếp:* Xong B0, sinh viên hiểu thuật toán đủ sâu để bắt đầu làm phần cứng ở B1, hoặc nghiên cứu thuật toán ở B3/B4.

| Mã | Loại | Sàn | HK1 | Đề tài | Làm ra |
|---|---|---|---|---|---|
| `B0-P01` | P | L0 | — | Mô phỏng Polar Encoder | Encoder implementation; known-vector validation; report |
| `B0-P02` | P | L0 | — | Mô phỏng BPSK/AWGN và tính LLR | Channel simulation; LLR sanity checks; plots |
| `B0-P03` | P | L1 | — | Xây dựng SC decoder cơ bản bằng MATLAB/Python | SC decoder; unit tests; small BER/BLER result |
| `B0-I01` | I | L2 | — | Xây dựng bộ mô phỏng Polar Code có khả năng tái lập | Configurable N/K/EbN0; seeded runs; BER/BLER; README; scripts |
| `B0-T01` | T | L2 | **B1** | Xây dựng và đánh giá hệ thống Polar Code sử dụng SC decoding | Full encode-channel-decode chain; validation; BER/BLER sweeps; complexity discussion; legacy package |

### B1 · Polar Hardware Building Blocks — Những viên gạch phần cứng đầu tiên của Polar

Biến các phép toán lõi của Polar (hàm f, hàm g, partial-sum) thành các module RTL nhỏ, mỗi module kiểm chứng độc lập với golden model. Triết lý của cả trục B nằm ở đây: làm nhỏ, kiểm kỹ, rồi mới ghép.

*Đi tiếp:* Các viên gạch B1 chính là linh kiện để B2 lắp thành bộ giải mã hoàn chỉnh.

| Mã | Loại | Sàn | HK1 | Đề tài | Làm ra |
|---|---|---|---|---|---|
| `B1-P01` | P | L1 | — | Thiết kế Polar Encoder RTL | RTL encoder; golden vectors; testbench; synthesis |
| `B1-P02` | P | L1 | — | Thiết kế f Processing Element | Reference f; RTL; exhaustive/random tests; synthesis |
| `B1-P03` | P | L1 | — | Thiết kế g Processing Element | Reference g; RTL; tests; synthesis |
| `B1-P04` | P | L2 | — | Thiết kế Partial-Sum Unit | Architecture; RTL; tests; synthesis |
| `B1-I01` | I | L2 | — | Thiết kế và kiểm chứng f/g Processing Elements trên FPGA | Golden co-verification; FPGA synthesis; resource/Fmax; report |
| `B1-T01` | T | L2 | **B2** | Thiết kế Polar Encoder trên FPGA | Architecture; RTL; verification; FPGA; resource/Fmax/latency/throughput |
| `B1-T02` | T | L2 | **B5** | Thiết kế và đánh giá f/g Processing Elements cho Polar Decoder | Exact/min-sum/reference; fixed-point RTL; timing/area/resource; BLER impact via model |

### B2 · SC Polar Decoder Hardware — Lắp thành bộ giải mã hoàn chỉnh

Ghép golden model, số học fixed-point, các processing element và khối điều khiển thành bộ giải mã SC chạy trên FPGA — so từng frame với mô phỏng phần mềm. Đây là đề tài 'xương sống' của trục B: khó vừa đủ, sản phẩm rõ ràng.

*Đi tiếp:* Có B2 rồi, các nhánh nghiên cứu B3/B4/B5 mới có nền phần cứng để đứng.

| Mã | Loại | Sàn | HK1 | Đề tài | Làm ra |
|---|---|---|---|---|---|
| `B2-I01` | I | L2 | — | Xây dựng kiến trúc SC decoder theo từng module | Module interfaces; f/g/partial-sum/control integration tests; documentation |
| `B2-T01` | T | L3 | **B3** | Thiết kế bộ giải mã SC Polar trên FPGA | Golden model; fixed-point; RTL decoder; co-verification; FPGA; BER/BLER + resource/Fmax/latency/throughput |
| `B2-T02` | T | L3 | — | Software-RTL co-verification cho SC Polar decoder | Automated vector generation; RTL comparison; regression; mismatch diagnosis; report |
| `B2-R01` | R | L4 | — | Architecture optimization cho SC decoder | 2+ architectures or parallelism/resource-sharing configurations; controlled evaluation |

### B3 · Hardware-Aware Quantization & Optimization — Bao nhiêu bit là đủ?

Câu hỏi nghiên cứu thật sự đầu tiên của trục B: giảm số bit biểu diễn LLR thì tiết kiệm phần cứng được bao nhiêu, và tỉ lệ lỗi xấu đi bao nhiêu? Sinh viên chạy thí nghiệm có kiểm soát và vẽ đường cong đánh đổi.

*Đi tiếp:* Kỹ năng ở đây (quét tham số, phân tích trade-off) là đúng kiểu bài của một bài báo khoa học.

| Mã | Loại | Sàn | HK1 | Đề tài | Làm ra |
|---|---|---|---|---|---|
| `B3-P01` | P | L1 | — | Khảo sát quantization của LLR | Floating vs 3/4/5/6-bit results; plots; explanation |
| `B3-I01` | I | L2 | — | Fixed-point implementation của Polar processing elements | Fixed-point reference; RTL or synthesizable model; error tests; resource |
| `B3-T01` | T | L3 | **B4** | Phân tích lượng tử hóa LLR cho hardware-efficient Polar decoding | BLER/BER vs bit-width; complexity/hardware proxy; controlled analysis; thesis |
| `B3-T02` | T | L3 | — | Tối ưu fixed-point cho SC Polar decoder | LLR/intermediate widths; saturation/clipping; BLER; resource/timing estimates |
| `B3-R01` | R | L4 | — | Adaptive-precision Polar decoding | Baseline fixed precision; adaptation rule; BLER/average-cost analysis; reproducible experiments |

### B4 · SC-Flip & Reliability-Aware Decoding — Khi giải sai thì sai ở đâu — và thử lại

Phân tích lỗi của bộ giải SC, xây thước đo độ tin cậy để đoán bit nào đáng ngờ, rồi lật (flip) và giải lại — thuật toán SC-Flip. Đánh giá luôn theo cặp: giảm được bao nhiêu lỗi, tốn thêm bao nhiêu lần thử.

*Đi tiếp:* B4 mở thẳng ra hai hướng nghiên cứu nóng: B5 (thích ứng) và B6 (nhờ AI hỗ trợ).

| Mã | Loại | Sàn | HK1 | Đề tài | Làm ra |
|---|---|---|---|---|---|
| `B4-P01` | P | L2 | — | Phân tích các lỗi SC decoding | Failure cases; reliability traces; categorized analysis |
| `B4-P02` | P | L2 | — | Reliability ranking dựa trên trị tuyệt đối LLR | Candidate ranking; Top-k metrics; plots |
| `B4-I01` | I | L2 | — | Xây dựng SC-Flip software decoder | SCF code; validation; BLER/attempts; reproducible scripts |
| `B4-T01` | T | L3 | **B6** | Thiết kế và đánh giá SC-Flip Polar decoder | SC vs SCF; BLER; attempts; latency/complexity proxy; analysis |
| `B4-T02` | T | L3 | **B8** | Reliability-based candidate ranking cho SC-Flip | Top-1/Top-k ranking; BLER; attempts; baselines; thesis |
| `B4-R01` | R | L4 | — | Improved reliability metric cho SCF | New/combined metric; ablation; statistical evaluation; paper-ready figures |

### B5 · Adaptive Polar Decoding — Frame dễ giải nhanh, frame khó mới dùng sức

Xây bộ phát hiện 'frame khó', chỉ khi gặp frame khó mới bật xử lý tăng cường — tiết kiệm năng lượng và thời gian trung bình mà vẫn giữ chất lượng. Đây là tư duy hệ thống: đo lường, ra quyết định, đánh đổi.

*Đi tiếp:* B5 là bậc thang cuối trước các đề tài đồng thiết kế thuật toán – phần cứng (B5-T03, AB).

| Mã | Loại | Sàn | HK1 | Đề tài | Làm ra |
|---|---|---|---|---|---|
| `B5-P01` | P | L2 | — | Thiết kế unreliable-frame detector dựa trên threshold | Detector; ROC/trigger metrics or suitable classification metrics; plots |
| `B5-I01` | I | L3 | — | Xây dựng adaptive SC/SCF simulation framework | Reliable/unreliable branch framework; seeded experiments; activation statistics; docs |
| `B5-T01` | T | L3 | **B7** | Phát hiện frame không tin cậy cho adaptive Polar decoding | Feature study; threshold/logistic baseline; detection/false trigger/missed trigger/activation/BLER |
| `B5-T02` | T | L3 | **B9** | Adaptive decoder chỉ kích hoạt enhanced processing trên frame khó | End-to-end adaptive framework; BLER; activation rate; avg attempts/latency/complexity |
| `B5-T03` | T | L4 | **B11** | Đồng thiết kế thuật toán - phần cứng cho bộ giải mã Polar thích ứng | Algorithm baseline; operation/memory model; fixed-point/quantization; RTL các critical block; Pareto analysis reliability-cost;… |
| `B5-R01` | R | L4 | — | Adaptive Polar decoding dưới ràng buộc hardware | Research hypothesis; reproducible baselines; latency/resource/energy proxy; paper-ready analysis |

### B6 · Neural-Assisted Polar Decoding — AI làm trợ lý cho bộ giải mã

Dùng mạng nơ-ron nhỏ gọn hỗ trợ đúng một việc hẹp — phát hiện frame khó, hoặc xếp hạng ứng viên bit lỗi — chứ không thay cả bộ giải mã. Luật cứng của nhóm: kết quả neural phải so được với cách cổ điển, không so thì không nhận.

*Đi tiếp:* Đây là nhóm cao nhất trục B (sàn L4–L5), dành cho sinh viên đã có baseline vững và hướng đi tiếp sau đại học.

| Mã | Loại | Sàn | HK1 | Đề tài | Làm ra |
|---|---|---|---|---|---|
| `B6-I01` | I | L3 | — | Lightweight ML classifier cho unreliable-frame detection | Train/val/test split; logistic/simple ML/MLP comparisons; reproducible model; metrics |
| `B6-T01` | T | L4 | — | Lightweight neural-assisted unreliable-frame detector | Heuristic + classical ML + lightweight NN; BLER/activation/model size/inference cost |
| `B6-T02` | T | L4 | **B10** | Neural-assisted candidate ranking cho SC-Flip Polar decoder | SC/SCF baselines; Top-k; BLER; attempts; model parameters/ops; thesis |
| `B6-R01` | R | L5 | — | Hardware-aware neural-assisted adaptive Polar decoder | Research-grade ablation; BLER; activation; latency/ops/memory/resource/energy proxy; reproducibility |
| `B6-R02` | R | L5 | — | Algorithm-hardware co-design của neural-assisted Polar decoder | Joint algorithm/hardware design space; hardware-aware model selection; implementation evidence |

### AB · Digital IC x Polar — Cầu nối các trục — ra chất nghiên cứu thật

Lấy một thuật toán — giải mã Polar của trục B, hay suy luận AI biên của A7 — và trả lời câu hỏi phần cứng: tốn bao nhiêu diện tích, nhanh cỡ nào, bao nhiêu năng lượng cho một bit tin cậy hay một lần suy luận? Từ v1.5.0, AB mở rộng đúng theo định hướng nghiên cứu luận án của mentor: co-design vi mạch × nhúng/IoT (AB-P01, AB-T05) và Polar × IoT (AB-T06), hội tụ ở các đề tài R (AB-R02, AB-R03) — nơi quyết định thuật toán và quyết định phần cứng được tối ưu cùng nhau.

*Đi tiếp:* Đề tài AB là bước đệm đẹp nhất từ đồ án tốt nghiệp sang bài báo hội nghị — và là đường thẳng vào chương trình nghiên cứu luận án.

| Mã | Loại | Sàn | HK1 | Đề tài | Làm ra |
|---|---|---|---|---|---|
| `AB-P01` | P | L2 | — | Đo chi phí một thuật toán trên ba nền tảng: MCU, FPGA, ASIC ước lượng | Cùng một khối xử lý đo trên MCU (cycle/năng lượng), FPGA (tài nguyên/Fmax) và ASIC ước lượng qua synthesis (area/timing); bảng so… |
| `AB-T01` | T | L3 | **B12** | ASIC feasibility study cho Polar Processing Element | Verified PE; synthesis; STA; physical implementation; PPA; analysis |
| `AB-T02` | T | L3 | — | FPGA-to-ASIC evaluation của Polar Encoder | FPGA metrics + ASIC PPA; methodology comparison; report |
| `AB-T03` | T | L4 | — | FPGA-to-ASIC evaluation của SC Polar Decoder | Selected decoder/core; FPGA and ASIC evidence; trade-off analysis |
| `AB-T04` | T | L4 | — | PPA optimization cho fixed-point Polar Processing Element | Bit-width/pipeline configurations; BLER or numerical impact; ASIC PPA; Pareto analysis |
| `AB-R01` | R | L5 | — | Hardware-aware design-space exploration cho Polar Decoder | Reproducible multi-objective experiments; BLER-area-latency-throughput-energy analysis; research manuscript assets |
| `AB-T05` | T | L3 | — | Tăng tốc phần cứng cho suy luận AI biên trên SoC FPGA | Baseline suy luận CPU-only trên SoC; accelerator cho lớp/khối nặng nhất; đo end-to-end: latency, năng lượng/suy luận, tài nguyên;… |
| `AB-T06` | T | L3 | — | Bộ giải mã SC Polar tiết kiệm năng lượng cho liên kết IoT | SC decoder fixed-point đặt trong ngữ cảnh IoT (block length/ném SNR do mentor chốt); đánh giá BLER kèm năng lượng/bit và độ trễ… |
| `AB-R02` | R | L4 | — | Co-design thuật toán – phần cứng cho truyền thông tin cậy ở thiết bị biên | Research question về điểm gặp giữa adaptive Polar decoding và ngân sách năng lượng biên; framework thí nghiệm; >=2 chiến lược so… |
| `AB-R03` | R | L5 | — | Nền tảng biên tích hợp: truyền thông và suy luận chia sẻ tài nguyên phần cứng | Feasibility study có số liệu: decoder Polar + suy luận edge AI trên cùng SoC/FPGA — chia sẻ tài nguyên, lập lịch, ngân sách năng… |

---

## 3. Bốn cách anh dùng kho đề tài này

### 3.1 Giảng dạy — loại P trong môn học

Đề tài P là **bài thực hành lớn có chuẩn đầu ra sẵn**: mỗi đề tài đã ghi rõ đầu vào cần gì, sản phẩm nộp gì, dùng công cụ nào. Cách dùng trong một môn học:

1. Chọn các đề tài P có `min_level` khớp trình độ lớp (ví dụ lớp mới học HDL: A1-P01/P02, sàn L0).
2. Dòng **Làm ra** của đề tài chính là barem nộp bài — không phải soạn lại yêu cầu từng học kỳ.
3. Sinh viên khá có thể làm phần *mở rộng* ghi sẵn trong đề tài để lấy điểm cộng.
4. Nhiều em cùng hổng một kỹ năng → mở **bootcamp chung** một buổi (danh sách kỹ năng bootcamp có trong `10_Documentation/MENTOR-GUIDE.md` §8) thay vì giảng lại 1-1.

*Ví dụ:* giao `A1-P04` (UART) cho môn Thiết kế số: tuần 1 sinh viên viết transmitter + testbench, tuần 2 receiver + loopback, tuần 3 nộp repo có README và waveform chứng minh. Chuẩn chấm nằm sẵn trong danh mục.

### 3.2 Thực tập — loại I, cửa bắt buộc trước đồ án

Đề tài I là nơi sinh viên tập *tác phong*: Git đúng cách, báo cáo tuần, làm theo quy trình — sản phẩm kỹ thuật chỉ là phương tiện. Mỗi trục có đề tài I ở mọi tầng (A0-I01 làm phần cứng thật, A5-I01 dựng Git workflow, B0-I01 xây bộ mô phỏng tái lập…), nên em nào cũng chọn được một kỳ thực tập vừa sức mà vẫn nằm đúng hướng nghề định theo.

### 3.3 Mentor đồ án tốt nghiệp — loại T, 15 tuần, 6 trạm kiểm soát

Mỗi học kỳ chương trình chạy một cohort DATN theo đúng khuôn 15 tuần – 6 trạm này; cohort hiện tại là HK1 2026-2027 (07/09 → 19/12, 21 đề tài mở — các hạn dưới đây là của cohort này). Kể bằng một ví dụ giả định — bạn **Minh** chọn `A4-T01` *(mã HK1: A1 — Thiết kế một Digital IP từ RTL đến GDSII)*:

| Trạm | Tuần · hạn chót | Minh phải cho xem | Anh làm gì |
|---|---|---|---|
| Gate 1 — Hiểu bài toán | T1–2 · **20/09** | Nói được input/output, chọn IP cụ thể (vd bộ lọc FIR nhỏ), toolchain cài chạy được | Ký thỏa thuận làm việc, chốt **MVT** (phần bắt buộc) tách khỏi *extension* (phần mơ ước), chép 6 trạm vào hồ sơ |
| Gate 2 — Baseline | T3–5 · **11/10** | RTL + testbench **chạy đúng**, có bằng chứng tái lập | Luật cứng: không có baseline ở đây → **đóng cửa extension**, chỉ còn làm phần lõi |
| Gate 3 — Lõi | T6–8 · **01/11** | Qua synthesis + kiểm tra timing sạch, số liệu trung gian | Trượt → **thu hẹp phạm vi** ngay (bỏ extension → bớt quét tham số → thu nhỏ khối), tuyệt đối không làm thay |
| Gate 4 — Thực nghiệm | T9–11 · **22/11** | Chạy trọn physical flow ra GDSII, bảng PPA chính | Sau trạm này **cấm thêm thuật toán mới** — chỉ hoàn thiện |
| Gate 5 — Phân tích & bản thảo | T12–13 · **06/12** | Bản thảo khóa luận, mỗi con số trỏ về một bằng chứng đã kiểm | Soát bằng sổ bằng chứng: claim không có evidence → bỏ khỏi báo cáo |
| Gate 6 — Tái lập & bảo vệ | T14–15 · **19/12** | Người khác chạy lại được từ README; slide + demo; gói bàn giao | Hỏi theo `DEFENSE_QUESTIONS.md`; nguyên tắc chốt: **không giải thích được = chưa hoàn thành** |

Giữa các trạm là **nhịp tuần** ~30 phút/sinh viên: đọc báo cáo tuần trước buổi gặp → trong buổi em trình theo khung *Mục tiêu → Bằng chứng → Cái gì hỏng → Chẩn đoán → Bước tiếp* → chốt 1–3 việc có hạn → ghi vào workbook. Thao tác chi tiết từng buổi: `10_Documentation/MENTOR-GUIDE.md`.

Sức mạnh của cách chạy này: **mọi sinh viên cùng đi qua 6 trạm giống nhau**, nên anh mentor 10 em cùng lúc vẫn nhìn được toàn cảnh trong một sheet — ai xanh ai đỏ, ai sắp đến trạm nào.

### 3.4 Nghiên cứu — loại R và con đường lên bài báo

Hệ thống tạo nghiên cứu theo **hai cửa**:

1. **Cửa extension** (phổ biến nhất): sinh viên làm đồ án T vững, qua Gate 2 đúng hạn → được mở phần mở rộng có chất nghiên cứu. Ví dụ: `B4-T01` (SC-Flip) làm xong phần lõi → extension "cải tiến thước đo độ tin cậy" → nếu kết quả tốt, đó là hạt nhân một bài báo. Extension thất bại **không** làm hỏng đồ án — phần lõi vẫn tự đứng được.
2. **Cửa đề tài R** (10 đề tài, sàn L4–L5): dành cho sinh viên đã chứng minh năng lực, thường là em đã làm T kỳ trước. Đề tài R chấp nhận *kết quả phủ định* — giả thuyết sai nhưng thí nghiệm sạch vẫn là nghiên cứu đạt.

Nhìn xa hơn một học kỳ, trục B chính là **một chương trình nghiên cứu nhiều thế hệ**: em khóa này làm B2 (bộ giải mã nền) để lại gói bàn giao; em khóa sau đứng trên đó làm B4/B5; em giỏi nhất chạm B6 (AI hỗ trợ) và AB (đo bằng thước chip). Mỗi đồ án bắt buộc để lại **Legacy Package** — nên kho của anh giàu lên sau mỗi khóa thay vì làm lại từ đầu.

**Con đường lên luận án của mentor** (mở từ v1.5.0) chạy qua đúng các bậc thang này: sinh viên vững nhúng/AI biên (`A6-T02`, `A7-T02`) hoặc Polar hardware (`B2-T01`, `B3-T01`) → đề tài co-design (`AB-T05` tăng tốc AI biên trên SoC FPGA, `AB-T06` decoder Polar tiết kiệm năng lượng cho IoT) → đề tài nghiên cứu (`AB-R02` co-design truyền thông tin cậy ở biên, `AB-R03` nền tảng biên tích hợp truyền thông + suy luận). Mỗi tầng để lại baseline và số liệu cho tầng sau — nhiều sinh viên, nhiều học kỳ, cùng bồi vào một hướng nghiên cứu.

---

## 4. Sinh viên mới đến — chọn đề tài trong 4 bước

1. **Hỏi đích đến nghề nghiệp** rồi tra bảng dưới → ra 2–3 ứng viên đề tài.
2. **So level**: sinh viên tự chấm + anh kiểm chứng qua bài thử việc (readiness test) → so với sàn của đề tài.
3. **So đầu vào**: mỗi đề tài ghi mã đầu vào tham chiếu (vd `A1-P*` = *đã làm ít nhất một project A1 hoặc tương đương có bằng chứng*).
4. **Chốt phạm vi**: nguyện vọng quyết định *hướng*, mức sẵn sàng quyết định *độ lớn* — nhận / nhận có điều kiện / đổi đề tài.

| Đích đến của em | Đề tài chính | Bước tiếp theo |
|---|---|---|
| Digital IC / RTL Verification | `A1-T01`, `A4-T01`, `A4-T02` | `B1-T01`, `B2-T01` |
| FPGA / DSP Hardware | `A2-T01`, `A3-T01`, `A2-T02` | `B1-T01`, `B2-T01` |
| ASIC Physical Flow / PPA | `A4-T01`, `A4-T02`, `A2-T03`, `A2-T02` | `AB-T01` |
| EDA infrastructure / DevOps cho hardware | `A5-T01`, `A5-T02` | `AB-T01 (hỗ trợ CI)` |
| Nghiên cứu Polar algorithm | `B0-T01`, `B3-T01`, `B4-T01` | `B5-T01`, `B4-T02`, `B5-T02` |
| AI hỗ trợ decoder *(Không bắt đầu trực tiếp bằng NN — cần baseline trước.)* | `B5-T01`, `B4-T02` | `B6-T02` |
| Algorithm-hardware co-design | `A2-T02` | `B5-T03`, `AB-T01` |
| Embedded & IoT engineer *(nhánh mở từ v1.5.0)* | `A6-T01`, `A7-T01`, `A7-T02` | `A6-T02`, `AB-T05`, `A6-R01`, `A7-R01` |
| Algorithm–hardware co-design *(định hướng luận án)* | `A6-T02`, `AB-T05`, `AB-T06` | `AB-R02`, `AB-R03` |

---

## 5. Mở gì, khi nào

| Tình huống | Mở |
|---|---|
| Cần thao tác từng buổi gặp / gate / xử lý SV chậm | `10_Documentation/MENTOR-GUIDE.md` |
| Phát tài liệu cho sinh viên | `Danh_muc_de_tai_DATN_Nhom_A_B_HK1_2026_2027.docx/.pdf` + `Phieu_lua_chon_va_danh_gia_de_tai_DATN_HK1_2026_2027.docx` (thư mục gốc) |
| Theo dõi cả lớp hằng tuần | `03_Operations/Mentoring_Management_Workbook.xlsx` |
| Sửa đề tài / thang điểm / lịch | `06_Data/*.json` rồi chạy 3 lệnh trong `10_Documentation/WORKFLOW.md` |
| Hiểu kiến trúc & quyết định thiết kế của hệ thống | `implementation-notes.md` / `.html` |
| Triết lý giáo dục gốc | `01_Governance/Master_Mentoring_Handbook.docx` |

*Tài liệu sinh từ nguồn chuẩn v1.5.1 (2026-08-23) — dữ liệu đổi thì chạy lại `python3 scripts/generate_ban_do.py`.*
