# Nhóm A7 — Hệ IoT và trí tuệ biên

**Engineering & Research Mentoring Program (Lucero)** · ThS. Đinh Văn Nam (Mr. Lucero Dinh) — Khoa Điện–Điện tử, Trường Kỹ thuật, Đại học Phenikaa

> **File sinh tự động** từ `06_Data/research_packs.json` bằng `scripts/generate_research_packs.py`. Sửa tay sẽ bị ghi đè — muốn đổi nội dung thì sửa JSON rồi chạy lại script.

**IoT Systems & Edge Intelligence** · 8 đề tài

## Nền chung của cả nhóm

Mọi đề tài trong nhóm này đều đi qua bốn mục dưới đây. Trang của từng đề tài chỉ thêm
**sản phẩm riêng** mà đề tài đó phải làm ra.

**Phải đọc**

- IoT architecture
- MQTT/BLE/LoRa basics
- energy measurement
- TinyML deployment/quantization

**Phải hiểu**

- uptime/loss/energy per operation
- duty cycle
- accuracy-latency-energy trade-off
- field reliability

**Phải dựng**

- real node/system
- logging pipeline
- measurement setup
- reproducible deployment

**Thí nghiệm mặc định**

- long-run reliability
- range/loss
- energy profile
- model/quantization trade-off

**Câu hỏi mentor**

1. System chạy ổn bao lâu và failure nào xảy ra?
2. Energy đo ở đâu và tích phân thế nào?
3. Accuracy tăng có đáng energy/latency cost không?
4. Lab result có chuyển sang field condition không?

**Bước đi tiếp:** AB-T05/AB-T06 → A7-R01/AB-R02/AB-R03

## Danh sách đề tài

| Mã | Tên | Loại | Sàn | Sản phẩm phải làm ra |
|---|---|---|---|---|
| [`A7-P01`](A7-P01.md) | Nút cảm biến IoT truyền dữ liệu qua MQTT | P | L1 | ESP32/STM32 real sensor; MQTT reconnect handling; minimal broker/dashboard; >=48h log; REA… |
| [`A7-P02`](A7-P02.md) | Đo và tối ưu năng lượng cho nút IoT chạy pin | P | L2 | Current profiles active/tx/sleep; duty-cycle strategy; battery-life estimate before/after |
| [`A7-P03`](A7-P03.md) | Suy luận TinyML trên vi điều khiển | P | L2 | Small model; INT8 quantization; MCU deployment; accuracy/latency/RAM/Flash; demo |
| [`A7-P04`](A7-P04.md) | Đánh giá kết nối không dây tầm ngắn/tầm xa cho IoT | P | L1 | BLE/LoRa or approved pair; range/loss/energy-per-packet vs distance; comparative report |
| [`A7-I01`](A7-I01.md) | Thực tập xây dựng hệ thống IoT đầu-cuối | I | L2 | Node→gateway→storage→dashboard >=2 weeks; uptime/loss; incident log; docs |
| [`A7-T01`](A7-T01.md) | Thiết kế và đánh giá hệ thống giám sát IoT đa nút hoàn chỉnh | T | L2 `C2` | >=3 battery nodes + gateway + dashboard; uptime/loss/battery-life evaluation; thesis; repr… |
| [`A7-T02`](A7-T02.md) | Triển khai và tối ưu mô hình AI gọn nhẹ trên thiết bị biên | T | L3 `C4` | Reproducible train→quantize→deploy; float/INT8 accuracy/latency/RAM/Flash/energy compariso… |
| [`A7-R01`](A7-R01.md) | Nghiên cứu đánh đổi độ chính xác – năng lượng – độ trễ cho suy luận tại biên | R | L4 | Hypothesis; model×quantization×frequency/voltage experiment matrix; trade-off curves |

---

*[← Bản đồ 16 nhóm](../README.md)*
