# Nhóm A1 — Logic số và thiết kế RTL

**Engineering & Research Mentoring Program (Lucero)** · ThS. Đinh Văn Nam (Mr. Lucero Dinh) — Khoa Điện–Điện tử, Trường Kỹ thuật, Đại học Phenikaa

> **File sinh tự động** từ `06_Data/research_packs.json` bằng `scripts/generate_research_packs.py`. Sửa tay sẽ bị ghi đè — muốn đổi nội dung thì sửa JSON rồi chạy lại script.

**Digital Logic & RTL Design** · 7 đề tài

## Nền chung của cả nhóm

Mọi đề tài trong nhóm này đều đi qua bốn mục dưới đây. Trang của từng đề tài chỉ thêm
**sản phẩm riêng** mà đề tài đó phải làm ra.

**Phải đọc**

- combinational/sequential logic
- Verilog synthesizable subset
- clock/reset/FSM
- self-checking testbench và waveform reasoning

**Phải hiểu**

- RTL mô tả phần cứng, không phải phần mềm tuần tự
- blocking vs non-blocking
- reset/clock-cycle semantics
- spec→assertion/test→evidence

**Phải dựng**

- spec/interface
- RTL
- self-checking testbench
- regression/synthesis evidence

**Thí nghiệm mặc định**

- directed + random tests
- corner/illegal-state tests
- parameter sweep nếu có
- synthesis resource/timing comparison

**Câu hỏi mentor**

1. Mỗi always block này suy ra phần cứng gì?
2. Test nào có thể chứng minh thiết kế sai?
3. Interface timing contract là gì?
4. Kết quả synthesis có phù hợp kiến trúc em nghĩ không?

**Bước đi tiếp:** A2/A3/A5 → A4 → A4-R01/A5-R01/AB

## Danh sách đề tài

| Mã | Tên | Loại | Sàn | Sản phẩm phải làm ra |
|---|---|---|---|---|
| [`A1-P01`](A1-P01.md) | Thiết kế các mạch logic tổ hợp bằng Verilog | P | L0 | RTL; testbench; waveform; short report |
| [`A1-P02`](A1-P02.md) | Thiết kế các mạch tuần tự bằng Verilog | P | L0 | RTL; reset tests; waveform; report |
| [`A1-P03`](A1-P03.md) | Thiết kế FSM cho một bộ điều khiển số | P | L1 | Specification; state diagram; RTL; tests; waveform |
| [`A1-P04`](A1-P04.md) | Thiết kế UART transmitter/receiver bằng RTL | P | L1 | UART RTL; loopback testbench; waveform; README · 📘 hồ sơ sâu |
| [`A1-P05`](A1-P05.md) | Thiết kế synchronous FIFO bằng RTL | P | L1 | FIFO RTL; full/empty/overflow/underflow tests; waveform |
| [`A1-I01`](A1-I01.md) | Thiết kế và kiểm chứng reusable Digital IP Core | I | L1 | Specification; reusable RTL; testbench; regression; documentation; repo |
| [`A1-T01`](A1-T01.md) | Thiết kế và kiểm chứng một IP số có khả năng tái sử dụng | T | L2 `A4` | Complete IP; systematic verification; synthesis report; documentation; legacy package |

---

*[← Bản đồ 16 nhóm](../README.md)*
