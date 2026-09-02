# Đối chiếu tên đề tài — bản đề xuất v2 (CHƯA áp dụng)

**Engineering & Research Mentoring Program (Lucero)** · ThS. Đinh Văn Nam (Mr. Lucero Dinh)
Khoa Điện–Điện tử, Trường Kỹ thuật, Đại học Phenikaa

> **Trạng thái: đề xuất, chưa áp dụng.** Tên đang dùng trong danh mục, phiếu đăng ký, bản PDF và
> trang web vẫn là **tên hiện hành** ở cột giữa. Bảng này lưu lại phương án v2 để cân nhắc cho
> khóa sau. Dữ liệu nằm ở trường `title_v2_proposed_vi` trong `06_Data/research_packs.json`;
> không script nào dùng nó để hiển thị.

## Vì sao có bảng này

Gói `Research_Program_Package_v2_105_Topics` đề xuất chỉnh **101/105** tên đề tài theo một
quy tắc đặt tên thống nhất: **tên phải phản ánh đầu ra đo được**, không "nâng cấp" một project
thành nghiên cứu chỉ bằng từ ngữ.

| Loại | Khuôn tên đề xuất |
|---|---|
| **P** | Thiết kế / Xây dựng / Triển khai + đối tượng + **kiểm chứng hoặc đo kiểm** |
| **I** | Thực tập / Xây dựng quy trình + **tái lập** + tài liệu hóa |
| **T** | Thiết kế và **đánh giá** / Triển khai và **tối ưu** + **metric hoặc trade-off** |
| **R** | Nghiên cứu / Khảo sát không gian thiết kế / Đồng thiết kế + **ràng buộc nghiên cứu** |

## Vì sao chưa áp dụng

Đổi tên là thay đổi hướng ra sinh viên: nó chạm vào danh mục in, phiếu đăng ký và mọi bản đã phát.
**Mã đề tài không đổi** nên về kỹ thuật việc đổi tên là an toàn, nhưng quyết định thuộc về chủ
nhiệm chương trình. Nếu quyết định áp dụng: sửa `title_vi` trong `06_Data/project_portfolio.json`,
chạy lại toàn bộ chuỗi sinh, và ghi vào CHANGELOG — không sửa ở bất kỳ chỗ nào khác.

## Bảng đối chiếu 105 đề tài

### A0 — Điện tử thực hành và PCB

| Mã | Tên hiện hành (đang dùng) | Tên v2 đề xuất | Đổi gì |
|---|---|---|---|
| `A0-P01` | Thiết kế và tự chế tạo thủ công mạch nguồn DC cơ bản | **Thiết kế, chế tạo thủ công và đo kiểm mạch nguồn DC trên PCB** | thêm: đo kiểm trên PCB |
| `A0-P02` | Thiết kế và chế tạo mạch logic tổ hợp trên PCB | **Thiết kế, chế tạo và đo kiểm mạch logic tổ hợp trên PCB** | thêm: đo kiểm |
| `A0-P03` | Thiết kế và chế tạo bộ đếm số trên PCB | **Thiết kế, chế tạo và kiểm thử bộ đếm số hiển thị trên PCB** | thêm: kiểm thử hiển thị |
| `A0-P04` | Thiết kế board giao tiếp cảm biến | **Thiết kế, chế tạo và đo kiểm board giao tiếp cảm biến** | thêm: chế tạo và đo kiểm |
| `A0-P05` | Thiết kế embedded controller board cơ bản | **Thiết kế và chế tạo board điều khiển nhúng cơ bản** | thêm: và chế tạo điều khiển nhúng |
| `A0-P06` | Thiết kế PCB mở rộng I/O cho FPGA | **Thiết kế và đánh giá PCB mở rộng I/O cho hệ thống FPGA** | thêm: và đánh giá hệ thống |
| `A0-I01` | Thực tập thiết kế, chế tạo và kiểm thử phần cứng điện tử | **Thực tập thiết kế–chế tạo–đo kiểm phần cứng điện tử theo quy trình kỹ sư** | thêm: kế–chế tạo–đo theo quy trình kỹ sư |

### A1 — Logic số và thiết kế RTL

| Mã | Tên hiện hành (đang dùng) | Tên v2 đề xuất | Đổi gì |
|---|---|---|---|
| `A1-P01` | Thiết kế các mạch logic tổ hợp bằng Verilog | **Thiết kế và kiểm chứng các mạch logic tổ hợp bằng Verilog** | thêm: và kiểm chứng |
| `A1-P02` | Thiết kế các mạch tuần tự bằng Verilog | **Thiết kế và kiểm chứng các mạch tuần tự bằng Verilog** | thêm: và kiểm chứng |
| `A1-P03` | Thiết kế FSM cho một bộ điều khiển số | **Thiết kế và kiểm chứng bộ điều khiển số dựa trên FSM** | thêm: và kiểm chứng dựa trên |
| `A1-P04` | Thiết kế UART transmitter/receiver bằng RTL | **Thiết kế và kiểm chứng IP UART transmitter/receiver tham số hóa bằng RTL** | thêm: và kiểm chứng IP tham số hóa |
| `A1-P05` | Thiết kế synchronous FIFO bằng RTL | **Thiết kế và kiểm chứng synchronous FIFO tham số hóa bằng RTL** | thêm: và kiểm chứng tham số hóa |
| `A1-I01` | Thiết kế và kiểm chứng reusable Digital IP Core | **Thiết kế, kiểm chứng và đóng gói Digital IP Core có khả năng tái sử dụng** | thêm: đóng gói có khả năng tái sử dụng |
| `A1-T01` | Thiết kế và kiểm chứng một IP số có khả năng tái sử dụng | **Thiết kế, kiểm chứng và đánh giá một Digital IP có khả năng tái sử dụng** | thêm: đánh giá Digital |

### A2 — Số học số và phần cứng DSP

| Mã | Tên hiện hành (đang dùng) | Tên v2 đề xuất | Đổi gì |
|---|---|---|---|
| `A2-P01` | Thiết kế và so sánh các kiến trúc bộ cộng số | **Thiết kế và so sánh kiến trúc bộ cộng số theo tài nguyên và timing** | thêm: theo tài nguyên timing |
| `A2-P02` | Thiết kế multiplier fixed-point | **Thiết kế và đánh giá bộ nhân fixed-point bằng RTL** | thêm: và đánh giá bộ nhân bằng RTL |
| `A2-P03` | Thiết kế Multiply-Accumulate datapath | **Thiết kế và đánh giá MAC datapath tham số hóa** | thêm: và đánh giá MAC tham số hóa |
| `A2-P04` | Thiết kế bộ lọc FIR bằng RTL | **Thiết kế và kiểm chứng bộ lọc FIR fixed-point bằng RTL** | thêm: và kiểm chứng fixed-point |
| `A2-I01` | Thiết kế và triển khai datapath DSP fixed-point trên FPGA | **Thiết kế, triển khai và đánh giá datapath DSP fixed-point trên FPGA** | thêm: đánh giá |
| `A2-T01` | Thiết kế bộ lọc FIR fixed-point trên FPGA và khảo sát ASIC | **Thiết kế và đánh giá bộ lọc FIR fixed-point trên FPGA hướng tới triển khai ASIC** | thêm: đánh giá hướng tới triển khai |
| `A2-T02` | Thiết kế và tối ưu MAC datapath cho FPGA/ASIC | **Đồng thiết kế bit-width và pipeline cho MAC datapath trên FPGA/ASIC** | thêm: Đồng bit-width pipeline trên |
| `A2-T03` | Thiết kế và đánh giá PPA của các kiến trúc bộ cộng số học | **Thiết kế và đánh giá PPA của các kiến trúc bộ cộng số học dưới cùng ràng buộc** | thêm: dưới cùng ràng buộc |
| `A2-R01` | Hardware design-space exploration cho fixed-point datapath | **Khảo sát không gian thiết kế hardware-aware cho datapath fixed-point** | thêm: Khảo sát không gian thiết kế hardware-aware |

### A3 — Thiết kế hệ thống trên FPGA

| Mã | Tên hiện hành (đang dùng) | Tên v2 đề xuất | Đổi gì |
|---|---|---|---|
| `A3-P01` | Triển khai một Digital IP trên FPGA | **Triển khai và đánh giá một Digital IP trên FPGA** | thêm: và đánh giá |
| `A3-P02` | FPGA interfacing với peripheral | **Thiết kế và kiểm chứng giao tiếp FPGA với ngoại vi** | thêm: Thiết kế và kiểm chứng giao tiếp ngoại |
| `A3-P03` | Hệ thống xử lý tín hiệu số trên FPGA | **Thiết kế và đánh giá pipeline xử lý tín hiệu số trên FPGA** | thêm: Thiết kế và đánh giá pipeline |
| `A3-I01` | Xây dựng hệ thống FPGA tích hợp nhiều IP | **Tích hợp và kiểm chứng hệ thống FPGA đa IP theo quy trình kỹ sư** | thêm: và kiểm chứng đa theo quy trình kỹ |
| `A3-T01` | Thiết kế hệ thống xử lý dữ liệu số pipelined trên FPGA | **Thiết kế và đánh giá hệ thống xử lý dữ liệu số pipelined trên FPGA** | thêm: và đánh giá |
| `A3-T02` | Hardware/software co-verification cho hệ thống FPGA | **Xây dựng quy trình hardware/software co-verification tái lập cho hệ thống FPGA** | thêm: Xây dựng quy trình tái lập |

### A4 — Thiết kế ASIC và hiện thực vật lý

| Mã | Tên hiện hành (đang dùng) | Tên v2 đề xuất | Đổi gì |
|---|---|---|---|
| `A4-P01` | Làm quen RTL-to-Gates bằng Yosys | **Khảo sát quy trình RTL-to-Gates bằng Yosys** | thêm: Khảo sát quy trình |
| `A4-P02` | Khảo sát ảnh hưởng của RTL coding style tới synthesis | **Khảo sát ảnh hưởng của RTL coding style đến kết quả synthesis** | thêm: đến kết quả |
| `A4-I01` | Xây dựng môi trường RTL-to-GDSII mã nguồn mở | **Xây dựng và kiểm thử môi trường RTL-to-GDSII mã nguồn mở có khả năng tái lập** | thêm: và kiểm thử có khả năng tái lập |
| `A4-T01` | Thiết kế một Digital IP từ RTL đến GDSII | **Thiết kế và đánh giá Digital IP từ RTL đến GDSII bằng quy trình EDA mã nguồn mở** | thêm: và đánh giá bằng quy trình EDA mã |
| `A4-T02` | Khảo sát ảnh hưởng kiến trúc RTL đến PPA | **Khảo sát ảnh hưởng của kiến trúc RTL đến PPA trong quy trình ASIC mã nguồn mở** | thêm: của trong quy trình ASIC mã nguồn mở |
| `A4-R01` | Design-space exploration cho một Digital IP | **Khảo sát không gian thiết kế PPA cho Digital IP bằng quy trình EDA mã nguồn mở** | thêm: Khảo sát không gian thiết kế PPA bằng |

### A5 — Kiểm chứng, EDA và phát triển tái lập

| Mã | Tên hiện hành (đang dùng) | Tên v2 đề xuất | Đổi gì |
|---|---|---|---|
| `A5-P01` | Xây dựng testbench có hệ thống cho một RTL module | _giữ nguyên_ | — |
| `A5-P02` | Regression testing cho Digital IP | **Xây dựng regression testing tái lập cho Digital IP** | thêm: Xây dựng tái lập |
| `A5-I01` | Xây dựng Git workflow cho dự án RTL | _giữ nguyên_ | — |
| `A5-T01` | Xây dựng quy trình ASIC tái lập sử dụng LibreLane + Nix | **Xây dựng và đánh giá quy trình RTL-to-GDSII tái lập sử dụng LibreLane + Nix** | thêm: và đánh giá RTL-to-GDSII |
| `A5-T02` | Continuous Integration cho dự án RTL/ASIC | **Xây dựng và đánh giá quy trình Continuous Integration cho dự án RTL/ASIC** | thêm: Xây dựng và đánh giá quy trình |
| `A5-R01` | Automated PPA regression cho Digital IC | **Nghiên cứu automated PPA regression cho Digital IC** | thêm: Nghiên cứu |

### A6 — Hệ nhúng và tích hợp SoC

| Mã | Tên hiện hành (đang dùng) | Tên v2 đề xuất | Đổi gì |
|---|---|---|---|
| `A6-P01` | Lập trình firmware bare-metal điều khiển ngoại vi vi điều khiển | **Thiết kế firmware bare-metal và đo kiểm giao tiếp ngoại vi vi điều khiển** | thêm: Thiết kế và đo kiểm giao tiếp |
| `A6-P02` | Ứng dụng đa nhiệm thời gian thực với RTOS | **Thiết kế và đánh giá ứng dụng đa nhiệm thời gian thực với RTOS** | thêm: Thiết kế và đánh giá |
| `A6-P03` | Giao tiếp phần cứng-phần mềm trên SoC FPGA | **Thiết kế và kiểm chứng giao tiếp phần cứng–phần mềm trên SoC FPGA** | thêm: Thiết kế và kiểm chứng cứng–phần |
| `A6-P04` | Dựng Linux nhúng trên SoC FPGA và viết driver đơn giản | **Xây dựng Linux nhúng trên SoC FPGA và kiểm chứng driver cho IP tùy biến** | thêm: Xây kiểm chứng cho IP tùy biến |
| `A6-I01` | Thực tập phát triển sản phẩm nhúng theo quy trình kỹ sư | _giữ nguyên_ | — |
| `A6-T01` | Thiết kế hệ thống nhúng điều khiển và thu thập dữ liệu hoàn chỉnh | **Thiết kế và đánh giá hệ thống nhúng điều khiển–thu thập dữ liệu hoàn chỉnh** | thêm: đánh giá khiển–thu |
| `A6-T02` | Tích hợp bộ tăng tốc phần cứng tùy biến vào SoC FPGA | **Tích hợp và đánh giá bộ tăng tốc phần cứng tùy biến trên SoC FPGA** | thêm: và đánh giá trên |
| `A6-R01` | Nghiên cứu phân hoạch phần cứng/phần mềm cho ứng dụng nhúng | **Nghiên cứu phân hoạch phần cứng–phần mềm cho ứng dụng nhúng theo ràng buộc hiệu năng–tài nguyên** | thêm: cứng–phần theo ràng buộc hiệu năng–tài nguyên |

### A7 — Hệ IoT và trí tuệ biên

| Mã | Tên hiện hành (đang dùng) | Tên v2 đề xuất | Đổi gì |
|---|---|---|---|
| `A7-P01` | Nút cảm biến IoT truyền dữ liệu qua MQTT | **Thiết kế và đánh giá nút cảm biến IoT truyền dữ liệu qua MQTT** | thêm: Thiết kế và đánh giá |
| `A7-P02` | Đo và tối ưu năng lượng cho nút IoT chạy pin | **Đo kiểm và tối ưu năng lượng cho nút IoT chạy pin** | thêm: kiểm |
| `A7-P03` | Suy luận TinyML trên vi điều khiển | **Triển khai và đánh giá suy luận TinyML trên vi điều khiển** | thêm: Triển khai và đánh giá |
| `A7-P04` | Đánh giá kết nối không dây tầm ngắn/tầm xa cho IoT | **Đánh giá thực nghiệm kết nối không dây cho IoT theo tầm phủ–mất gói–năng lượng** | thêm: thực nghiệm theo phủ–mất gói–năng lượng |
| `A7-I01` | Thực tập xây dựng hệ thống IoT đầu-cuối | _giữ nguyên_ | — |
| `A7-T01` | Thiết kế và đánh giá hệ thống giám sát IoT đa nút hoàn chỉnh | **Thiết kế và đánh giá hệ thống giám sát IoT đa nút** | thêm:  |
| `A7-T02` | Triển khai và tối ưu mô hình AI gọn nhẹ trên thiết bị biên | **Triển khai và tối ưu mô hình AI gọn nhẹ trên thiết bị biên theo accuracy–latency–energy** | thêm: theo accuracy–latency–energy |
| `A7-R01` | Nghiên cứu đánh đổi độ chính xác – năng lượng – độ trễ cho suy luận tại biên | **Nghiên cứu trade-off độ chính xác–năng lượng–độ trễ cho suy luận tại biên** | thêm: trade-off xác–năng lượng–độ |

### AB — Vùng giao: IC số × Polar × Edge co-design

| Mã | Tên hiện hành (đang dùng) | Tên v2 đề xuất | Đổi gì |
|---|---|---|---|
| `AB-P01` | Đo chi phí một thuật toán trên ba nền tảng: MCU, FPGA, ASIC ước lượng | **Đánh giá chi phí một khối xử lý trên MCU, FPGA và ASIC ước lượng** | thêm: Đánh giá khối xử lý và |
| `AB-T01` | ASIC feasibility study cho Polar Processing Element | **Đánh giá khả năng triển khai ASIC của Polar Processing Element** | thêm: Đánh giá khả năng triển khai của |
| `AB-T02` | FPGA-to-ASIC evaluation của Polar Encoder | **Đánh giá FPGA-to-ASIC cho Polar Encoder** | thêm: Đánh giá cho |
| `AB-T03` | FPGA-to-ASIC evaluation của SC Polar Decoder | **Đánh giá FPGA-to-ASIC cho SC Polar Decoder** | thêm: Đánh giá cho |
| `AB-T04` | PPA optimization cho fixed-point Polar Processing Element | **Tối ưu PPA cho fixed-point Polar Processing Element theo bit-width và pipeline** | thêm: Tối ưu theo bit-width và pipeline |
| `AB-T05` | Tăng tốc phần cứng cho suy luận AI biên trên SoC FPGA | **Thiết kế và đánh giá bộ tăng tốc phần cứng cho suy luận AI biên trên SoC FPGA** | thêm: Thiết kế và đánh giá bộ |
| `AB-T06` | Bộ giải mã SC Polar tiết kiệm năng lượng cho liên kết IoT | **Thiết kế và đánh giá bộ giải mã SC Polar tiết kiệm năng lượng cho liên kết IoT** | thêm: Thiết kế và đánh giá |
| `AB-R01` | Hardware-aware design-space exploration cho Polar Decoder | **Khảo sát không gian thiết kế hardware-aware đa mục tiêu cho Polar decoder** | thêm: Khảo sát không gian thiết kế đa mục |
| `AB-R02` | Co-design thuật toán – phần cứng cho truyền thông tin cậy ở thiết bị biên | **Đồng thiết kế thuật toán–phần cứng cho truyền thông tin cậy trên thiết bị biên** | thêm: Đồng kế toán–phần trên |
| `AB-R03` | Nền tảng biên tích hợp: truyền thông và suy luận chia sẻ tài nguyên phần cứng | **Nghiên cứu nền tảng biên tích hợp truyền thông và suy luận chia sẻ tài nguyên phần cứng** | thêm: Nghiên cứu hợp |

### B0 — Nền Polar và baseline phần mềm

| Mã | Tên hiện hành (đang dùng) | Tên v2 đề xuất | Đổi gì |
|---|---|---|---|
| `B0-P01` | Mô phỏng Polar Encoder | **Xây dựng và kiểm chứng mô hình Polar Encoder** | thêm: Xây dựng và kiểm chứng hình |
| `B0-P02` | Mô phỏng BPSK/AWGN và tính LLR | **Xây dựng và kiểm chứng mô hình BPSK/AWGN và tính LLR** | thêm: Xây dựng kiểm chứng hình |
| `B0-P03` | Xây dựng SC decoder cơ bản bằng MATLAB/Python | **Xây dựng và kiểm chứng bộ giải mã SC Polar bằng MATLAB/Python** | thêm: và kiểm chứng bộ giải mã Polar |
| `B0-I01` | Xây dựng bộ mô phỏng Polar Code có khả năng tái lập | **Xây dựng bộ mô phỏng Polar Code có khả năng tái lập cho nghiên cứu** | thêm: cho nghiên cứu |
| `B0-T01` | Xây dựng và đánh giá hệ thống Polar Code sử dụng SC decoding | **Xây dựng và đánh giá hệ thống Polar Code sử dụng SC decoding trên kênh AWGN** | thêm: trên kênh AWGN |

### B1 — Khối phần cứng cho Polar

| Mã | Tên hiện hành (đang dùng) | Tên v2 đề xuất | Đổi gì |
|---|---|---|---|
| `B1-P01` | Thiết kế Polar Encoder RTL | **Thiết kế và kiểm chứng Polar Encoder bằng RTL** | thêm: và kiểm chứng bằng |
| `B1-P02` | Thiết kế f Processing Element | **Thiết kế và kiểm chứng f Processing Element cho Polar decoder** | thêm: và kiểm chứng cho Polar decoder |
| `B1-P03` | Thiết kế g Processing Element | **Thiết kế và kiểm chứng g Processing Element cho Polar decoder** | thêm: và kiểm chứng cho Polar decoder |
| `B1-P04` | Thiết kế Partial-Sum Unit | **Thiết kế và kiểm chứng Partial-Sum Unit cho Polar decoder** | thêm: và kiểm chứng cho Polar decoder |
| `B1-I01` | Thiết kế và kiểm chứng f/g Processing Elements trên FPGA | **Thiết kế, đồng kiểm chứng và đánh giá f/g Processing Elements trên FPGA** | thêm: đồng đánh giá |
| `B1-T01` | Thiết kế Polar Encoder trên FPGA | **Thiết kế và đánh giá Polar Encoder trên FPGA** | thêm: và đánh giá |
| `B1-T02` | Thiết kế và đánh giá f/g Processing Elements cho Polar Decoder | **Thiết kế và đánh giá fixed-point f/g Processing Elements cho Polar decoder** | thêm: fixed-point |

### B2 — Bộ giải mã SC Polar trên phần cứng

| Mã | Tên hiện hành (đang dùng) | Tên v2 đề xuất | Đổi gì |
|---|---|---|---|
| `B2-I01` | Xây dựng kiến trúc SC decoder theo từng module | **Xây dựng và kiểm chứng kiến trúc SC decoder theo module** | thêm: và kiểm chứng |
| `B2-T01` | Thiết kế bộ giải mã SC Polar trên FPGA | **Thiết kế và đánh giá bộ giải mã SC Polar trên FPGA** | thêm: và đánh giá |
| `B2-T02` | Software-RTL co-verification cho SC Polar decoder | **Xây dựng quy trình software–RTL co-verification tái lập cho SC Polar decoder** | thêm: Xây dựng quy trình software–RTL tái lập |
| `B2-R01` | Architecture optimization cho SC decoder | **Nghiên cứu tối ưu kiến trúc SC Polar decoder theo trade-off tài nguyên–độ trễ** | thêm: Nghiên cứu tối ưu kiến trúc Polar theo |

### B3 — Lượng tử hóa và tối ưu theo phần cứng

| Mã | Tên hiện hành (đang dùng) | Tên v2 đề xuất | Đổi gì |
|---|---|---|---|
| `B3-P01` | Khảo sát quantization của LLR | **Khảo sát ảnh hưởng của lượng tử hóa LLR đến SC Polar decoding** | thêm: ảnh hưởng lượng tử hóa đến SC Polar |
| `B3-I01` | Fixed-point implementation của Polar processing elements | **Triển khai fixed-point và đánh giá Polar processing elements** | thêm: Triển khai và đánh giá |
| `B3-T01` | Phân tích lượng tử hóa LLR cho hardware-efficient Polar decoding | **Phân tích ảnh hưởng lượng tử hóa LLR đến hiệu năng và chi phí phần cứng của Polar decoding** | thêm: ảnh hưởng đến hiệu năng và chi phí |
| `B3-T02` | Tối ưu fixed-point cho SC Polar decoder | **Tối ưu fixed-point cho SC Polar decoder theo BLER–resource–timing** | thêm: theo BLER–resource–timing |
| `B3-R01` | Adaptive-precision Polar decoding | **Nghiên cứu adaptive-precision Polar decoding dưới ràng buộc phần cứng** | thêm: Nghiên cứu dưới ràng buộc phần cứng |

### B4 — SC-Flip và giải mã theo độ tin cậy

| Mã | Tên hiện hành (đang dùng) | Tên v2 đề xuất | Đổi gì |
|---|---|---|---|
| `B4-P01` | Phân tích các lỗi SC decoding | **Phân tích cơ chế và vị trí lỗi trong SC Polar decoding** | thêm: cơ chế và vị trí trong Polar |
| `B4-P02` | Reliability ranking dựa trên trị tuyệt đối LLR | **Khảo sát xếp hạng ứng viên SC-Flip dựa trên độ lớn LLR** | thêm: Khảo sát xếp hạng ứng viên SC-Flip độ |
| `B4-I01` | Xây dựng SC-Flip software decoder | **Xây dựng và kiểm chứng SC-Flip Polar decoder có khả năng tái lập** | thêm: và kiểm chứng Polar có khả năng tái |
| `B4-T01` | Thiết kế và đánh giá SC-Flip Polar decoder | **Thiết kế và đánh giá SC-Flip Polar decoder theo BLER–attempts–latency** | thêm: theo BLER–attempts–latency |
| `B4-T02` | Reliability-based candidate ranking cho SC-Flip | **Nghiên cứu xếp hạng ứng viên dựa trên độ tin cậy cho SC-Flip Polar decoder** | thêm: Nghiên cứu xếp hạng ứng viên dựa trên |
| `B4-R01` | Improved reliability metric cho SCF | **Nghiên cứu thước đo độ tin cậy cải tiến cho SC-Flip Polar decoding** | thêm: Nghiên cứu thước đo độ tin cậy cải |

### B5 — Giải mã Polar thích ứng

| Mã | Tên hiện hành (đang dùng) | Tên v2 đề xuất | Đổi gì |
|---|---|---|---|
| `B5-P01` | Thiết kế unreliable-frame detector dựa trên threshold | **Thiết kế và đánh giá bộ phát hiện frame không tin cậy dựa trên threshold** | thêm: và đánh giá bộ phát hiện frame không |
| `B5-I01` | Xây dựng adaptive SC/SCF simulation framework | **Xây dựng framework mô phỏng adaptive SC/SCF có khả năng tái lập** | thêm: mô phỏng có khả năng tái lập |
| `B5-T01` | Phát hiện frame không tin cậy cho adaptive Polar decoding | **Phát hiện frame không tin cậy cho giải mã Polar thích ứng dựa trên đặc trưng độ tin cậy** | thêm: giải mã thích ứng dựa trên đặc trưng |
| `B5-T02` | Adaptive decoder chỉ kích hoạt enhanced processing trên frame khó | **Thiết kế bộ giải mã Polar thích ứng với xử lý tăng cường có chọn lọc** | thêm: Thiết kế bộ giải mã Polar thích ứng |
| `B5-T03` | Đồng thiết kế thuật toán - phần cứng cho bộ giải mã Polar thích ứng | **Đồng thiết kế thuật toán–phần cứng cho bộ giải mã Polar thích ứng** | thêm: toán–phần |
| `B5-R01` | Adaptive Polar decoding dưới ràng buộc hardware | **Nghiên cứu adaptive Polar decoding dưới ràng buộc độ trễ–tài nguyên–năng lượng** | thêm: Nghiên cứu độ trễ–tài nguyên–năng lượng |

### B6 — Giải mã Polar hỗ trợ mạng neural

| Mã | Tên hiện hành (đang dùng) | Tên v2 đề xuất | Đổi gì |
|---|---|---|---|
| `B6-I01` | Lightweight ML classifier cho unreliable-frame detection | **Xây dựng lightweight ML baseline cho phát hiện frame không tin cậy** | thêm: Xây dựng baseline phát hiện frame không tin |
| `B6-T01` | Lightweight neural-assisted unreliable-frame detector | **Thiết kế bộ phát hiện frame không tin cậy hỗ trợ mạng neural nhẹ cho adaptive Polar decoding** | thêm: Thiết kế bộ phát hiện frame không tin |
| `B6-T02` | Neural-assisted candidate ranking cho SC-Flip Polar decoder | **Xếp hạng ứng viên hỗ trợ mạng neural nhẹ cho SC-Flip Polar decoder** | thêm: Xếp hạng ứng viên hỗ trợ mạng neural |
| `B6-R01` | Hardware-aware neural-assisted adaptive Polar decoder | **Nghiên cứu hardware-aware neural-assisted adaptive Polar decoder** | thêm: Nghiên cứu |
| `B6-R02` | Algorithm-hardware co-design của neural-assisted Polar decoder | **Đồng thiết kế thuật toán–phần cứng cho neural-assisted Polar decoder** | thêm: Đồng thiết kế thuật toán–phần cứng cho |

---

*Nguồn: `Research_Program_Package_v2_105_Topics/00_PROGRAM/TITLE-REVIEW.md` và `TITLE-NAMING-RULES.md`.*
