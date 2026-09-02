# Nhóm A6 — Hệ nhúng và tích hợp SoC

**Engineering & Research Mentoring Program (Lucero)** · ThS. Đinh Văn Nam (Mr. Lucero Dinh) — Khoa Điện–Điện tử, Trường Kỹ thuật, Đại học Phenikaa

> **File sinh tự động** từ `06_Data/research_packs.json` bằng `scripts/generate_research_packs.py`. Sửa tay sẽ bị ghi đè — muốn đổi nội dung thì sửa JSON rồi chạy lại script.

**Embedded Systems & SoC Integration** · 8 đề tài

## Nền chung của cả nhóm

Mọi đề tài trong nhóm này đều đi qua bốn mục dưới đây. Trang của từng đề tài chỉ thêm
**sản phẩm riêng** mà đề tài đó phải làm ra.

**Phải đọc**

- MCU architecture
- UART/I2C/SPI
- interrupt/RTOS
- SoC FPGA memory-mapped I/O
- profiling

**Phải hiểu**

- polling vs interrupt
- deadline/jitter
- HW/SW boundary
- profile before accelerate

**Phải dựng**

- firmware/driver
- hardware interface or accelerator where applicable
- system tests
- performance logs

**Thí nghiệm mặc định**

- latency/jitter
- throughput
- CPU utilization
- hardware acceleration speedup/resource trade-off

**Câu hỏi mentor**

1. Đoạn nào thật sự là bottleneck?
2. Tại sao đưa phần này xuống hardware?
3. Deadline đo thế nào?
4. End-to-end speedup có khớp kernel speedup không?

**Bước đi tiếp:** A7/AB-T05 → A6-R01/AB-R02/AB-R03

## Danh sách đề tài

| Mã | Tên | Loại | Sàn | Sản phẩm phải làm ra |
|---|---|---|---|---|
| [`A6-P01`](A6-P01.md) | Lập trình firmware bare-metal điều khiển ngoại vi vi điều khiển | P | L1 | Driver UART/I2C/SPI tự viết; firmware demo; logic-analyzer measurement; README |
| [`A6-P02`](A6-P02.md) | Ứng dụng đa nhiệm thời gian thực với RTOS | P | L1 | FreeRTOS/Zephyr >=3 task; priority/deadline analysis; jitter/latency; super-loop compariso… |
| [`A6-P03`](A6-P03.md) | Giao tiếp phần cứng-phần mềm trên SoC FPGA | P | L2 | Memory-mapped IP; processor-side C driver; bus read/write tests; README |
| [`A6-P04`](A6-P04.md) | Dựng Linux nhúng trên SoC FPGA và viết driver đơn giản | P | L2 | Bootable Linux image; char/UIO driver to IP; validation log; rebuild guide |
| [`A6-I01`](A6-I01.md) | Thực tập phát triển sản phẩm nhúng theo quy trình kỹ sư | I | L2 | Requirements→design→firmware→test→docs; weekly log; disciplined Git repo |
| [`A6-T01`](A6-T01.md) | Thiết kế hệ thống nhúng điều khiển và thu thập dữ liệu hoàn chỉnh | T | L2 `C1` | Working embedded system >=2 peripherals; RTOS/clear SW architecture; system tests; perform… |
| [`A6-T02`](A6-T02.md) | Tích hợp bộ tăng tốc phần cứng tùy biến vào SoC FPGA | T | L3 `C3` | Profiled software baseline; RTL accelerator; driver/integration; speedup; resource/latency… |
| [`A6-R01`](A6-R01.md) | Nghiên cứu phân hoạch phần cứng/phần mềm cho ứng dụng nhúng | R | L4 | Research question; partitioning method/criteria; >=2 partitions same benchmark; analysis |

---

*[← Bản đồ 16 nhóm](../README.md)*
