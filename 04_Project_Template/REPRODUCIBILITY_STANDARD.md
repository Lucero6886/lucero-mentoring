# Chuẩn tái lập cho repository đề tài

**Engineering & Research Mentoring Program (Lucero)** · ThS. Đinh Văn Nam (Mr. Lucero Dinh) — Khoa Điện–Điện tử, Trường Kỹ thuật, Đại học Phenikaa

> Áp dụng cho mọi đề tài. Kiểm ở **Gate 6**, nhưng phải dựng từ **tuần 1** —
> dựng ngược lại vào tuần 14 thì gần như luôn thất bại.

## Cấu trúc thư mục

```text
topic-repo/
├── README.md            # người khác đọc đầu tiên: chạy lại thế nào
├── docs/                # ghi chú kỹ thuật, báo cáo tuần
├── references/          # tài liệu đã đọc, literature matrix
├── src/                 # mã nguồn phần mềm
├── rtl/                 # mã RTL (nếu có)
├── tb/                  # testbench
├── scripts/             # script chạy thí nghiệm và sinh hình
├── configs/             # cấu hình đã đặt tên, có phiên bản
├── tests/               # unit test / regression
├── results/
│   ├── raw/             # kết quả thô — KHÔNG BAO GIỜ ghi đè, không sửa tay
│   └── processed/       # kết quả đã xử lý, sinh từ raw bằng script
├── figures/             # hình sinh từ script, không vẽ tay
├── hardware/            # báo cáo tổng hợp, timing, tài nguyên
├── paper/               # bản thảo, nếu có
└── weekly/              # báo cáo tuần
```

Không bắt buộc đề tài nào cũng dùng đủ mọi thư mục — **xóa thư mục không dùng** thay vì để rỗng.

## Mỗi thí nghiệm phải ghi lại

| Mục | Vì sao |
|---|---|
| Ngày giờ chạy | Ghép được với nhật ký và với commit |
| Git commit | Biết chính xác code nào tạo ra số này |
| Config | Chạy lại được mà không đoán |
| Seed | Ngẫu nhiên nhưng lặp lại được |
| Phiên bản công cụ | Kết quả đổi khi công cụ đổi, và điều đó sẽ xảy ra |
| Nền tảng / phần cứng | Thời gian chạy và giới hạn tài nguyên phụ thuộc máy |
| Đường dẫn kết quả thô | Truy ngược từ hình về dữ liệu gốc |
| Script xử lý | Hình phải tái tạo được từ raw bằng một lệnh |

Mẫu: `04_Project_Template/EXPERIMENT_LOG_TEMPLATE.md`

## Ba điều tuyệt đối không làm

1. **Không ghi đè `results/raw/`.** Chạy lại thì tạo thư mục mới có timestamp.
2. **Không sửa số liệu bằng tay** trong bảng tính hay trong hình.
3. **Không để hình tồn tại mà không có script sinh ra nó.** Hình không truy ngược được
   thì ở Gate 5 coi như không có bằng chứng.

## Kiểm tra ở Gate 6

- [ ] Clone sang máy khác (hoặc thư mục sạch) và chạy theo README, không hỏi tác giả.
- [ ] Hình chính được tạo lại đúng bằng một lệnh.
- [ ] Ghi rõ môi trường và phiên bản mọi công cụ.
- [ ] `raw/` và `processed/` tách bạch.
- [ ] Không có đường dẫn tuyệt đối kiểu `C:\Users\...` trong script.
