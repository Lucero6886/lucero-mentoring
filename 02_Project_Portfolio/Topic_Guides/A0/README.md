# Nhóm A0 — Điện tử thực hành và PCB

**Engineering & Research Mentoring Program (Lucero)** · ThS. Đinh Văn Nam (Mr. Lucero Dinh) — Khoa Điện–Điện tử, Trường Kỹ thuật, Đại học Phenikaa

> **File sinh tự động** từ `06_Data/research_packs.json` bằng `scripts/generate_research_packs.py`. Sửa tay sẽ bị ghi đè — muốn đổi nội dung thì sửa JSON rồi chạy lại script.

**Hands-on Electronics & PCB** · 7 đề tài

## Nền chung của cả nhóm

Mọi đề tài trong nhóm này đều đi qua bốn mục dưới đây. Trang của từng đề tài chỉ thêm
**sản phẩm riêng** mà đề tài đó phải làm ra.

**Phải đọc**

- datasheet và giới hạn tuyệt đối của linh kiện
- schematic capture và nguyên tắc PCB cơ bản
- nguồn, decoupling, ground, connector, polarity
- sử dụng DMM/oscilloscope/logic analyzer và an toàn phòng lab

**Phải hiểu**

- đường đi dòng điện và đường hồi dòng
- khác biệt schematic đúng và board thật chạy ổn
- measurement uncertainty và test point
- debug theo giả thuyết, không thay linh kiện ngẫu nhiên

**Phải dựng**

- schematic + BOM
- PCB tự chế tạo/board thật
- test plan + test points
- measurement + failure-fix log

**Thí nghiệm mặc định**

- continuity/short test trước cấp nguồn
- nominal functional test
- sweep tải/điện áp/tần số hoặc điều kiện phù hợp
- repeat measurement và failure injection đơn giản

**Câu hỏi mentor**

1. Điện/dòng đi theo đường nào trên board?
2. Nếu mô phỏng đúng nhưng board sai, em kiểm tra theo thứ tự nào?
3. Con số đo này có sai số và giới hạn dụng cụ gì?
4. Board này có thể nâng cấp thành một experiment có câu hỏi nghiên cứu nào?

**Bước đi tiếp:** A1/A3/A6 → A2/A4/A7 → đề tài R/AB

## Danh sách đề tài

| Mã | Tên | Loại | Sàn | Sản phẩm phải làm ra |
|---|---|---|---|---|
| [`A0-P01`](A0-P01.md) | Thiết kế và tự chế tạo thủ công mạch nguồn DC cơ bản | P | L0 | Schematic; PCB layout; PCB tự chế tạo; board lắp ráp; kết quả đo tải/ripple; debugging log |
| [`A0-P02`](A0-P02.md) | Thiết kế và chế tạo mạch logic tổ hợp trên PCB | P | L0 | Truth table; schematic; PCB; board thật; measurement; failure-fix evidence |
| [`A0-P03`](A0-P03.md) | Thiết kế và chế tạo bộ đếm số trên PCB | P | L0 | Schematic; PCB; counter + display hoạt động; test reset/clock; debugging report |
| [`A0-P04`](A0-P04.md) | Thiết kế board giao tiếp cảm biến | P | L0 | Requirement; datasheet note; schematic; PCB; board; measurement |
| [`A0-P05`](A0-P05.md) | Thiết kế embedded controller board cơ bản | P | L1 | Schematic; PCB; power/reset/clock/I/O; firmware test; board demo |
| [`A0-P06`](A0-P06.md) | Thiết kế PCB mở rộng I/O cho FPGA | P | L1 | PCB extension; interface test; FPGA demo; documentation |
| [`A0-I01`](A0-I01.md) | Thực tập thiết kế, chế tạo và kiểm thử phần cứng điện tử | I | L1 | Working board; design files; BOM; measurement; debug log; technical report; legacy package |

---

*[← Bản đồ 16 nhóm](../README.md)*
