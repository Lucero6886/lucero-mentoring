# Evidence Ledger — <MÃ_ĐỀ_TÀI> · <HỌ TÊN>

> Sổ cái bằng chứng (MASTER_PROMPT §11). Mục đích duy nhất: **truy được một claim trong khóa luận
> ngược về artifact kỹ thuật thật**. Không có sổ này thì tiến độ tuần chỉ còn là lời kể.
>
> Sinh viên thêm dòng khi nộp; mentor điền `Trạng thái` và `Ghi chú review`.
> **Chứa đường dẫn tới sản phẩm của SV → lưu trong `07_Private/` nếu có dữ liệu cá nhân.**

## Quy tắc

- Mỗi artifact **một dòng**, `evidence_id` không tái sử dụng (E001, E002, …).
- Cột `Claim hỗ trợ` phải viết thành **một mệnh đề kiểm chứng được**, không phải tên file.
  Sai: *"file bler.png"* · Đúng: *"SC decoder N=1024 K=512 đạt BLER 1e-3 tại Eb/N0 = 2.5 dB"*.
- Không xóa dòng cũ. Kết quả bị thay thế → đặt `SUPERSEDED` và trỏ sang `evidence_id` mới.
- "Đã đọc / đã tìm hiểu" **không phải** evidence — không tạo dòng cho nó.

## Trạng thái kiểm chứng

| Trạng thái | Nghĩa |
|---|---|
| `SUBMITTED` | SV đã nộp, mentor chưa xem |
| `VERIFIED` | Mentor đã kiểm và evidence đủ đỡ cho claim |
| `PARTIAL` | Có thật nhưng chưa đủ đỡ claim — ghi rõ còn thiếu gì |
| `REJECTED` | Không đỡ được claim, hoặc không tái lập được |
| `SUPERSEDED` | Bị thay bởi evidence mới hơn — ghi id thay thế |

## Loại artifact được chấp nhận

source code · commit · testbench · waveform · simulation log · synthesis report · STA report ·
PPA table · experiment config · script · notebook · figure · bảng số · README · technical note ·
measurement data · demo · giải thích bằng lời (oral).

## Sổ cái

| ID | Ngày | Tuần | Gate | Loại artifact | Đường dẫn / link | Claim được hỗ trợ | Trạng thái | Ghi chú review |
|---|---|---|---|---|---|---|---|---|
| E001 |  |  |  |  |  |  | `SUBMITTED` |  |
| E002 |  |  |  |  |  |  | `SUBMITTED` |  |
| E003 |  |  |  |  |  |  | `SUBMITTED` |  |

## Truy vết claim → evidence (điền ở Gate 5–6)

Mỗi phát biểu định lượng trong báo cáo/khóa luận phải trỏ được về ít nhất một dòng `VERIFIED`.

| Claim trong báo cáo | Mục/hình/bảng | Evidence ID | Đã kiểm |
|---|---|---|---|
|  |  |  | ☐ |
|  |  |  | ☐ |

**Claim không trỏ được về evidence `VERIFIED` thì phải bỏ khỏi báo cáo hoặc hạ xuống mức phỏng đoán có ghi rõ.**
