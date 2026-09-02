# Hồ sơ thực thi chiều sâu — 13 đề tài nghiên cứu

**Engineering & Research Mentoring Program (Lucero)** · ThS. Đinh Văn Nam (Mr. Lucero Dinh) — Khoa Điện–Điện tử, Trường Kỹ thuật, Đại học Phenikaa

> **File sinh tự động** từ `06_Data/research_packs.json` bằng `scripts/generate_research_packs.py`. Sửa tay sẽ bị ghi đè — muốn đổi nội dung thì sửa JSON rồi chạy lại script.

Danh mục đề tài trả lời câu hỏi *"có những đề tài nào"*. Thư mục này trả lời câu tiếp theo:
*"làm đề tài đó cụ thể ra sao"*. Mỗi đề tài có tám file: phải đọc gì, hiểu gì, dựng gì,
chạy thí nghiệm nào, nộp bằng chứng gì, điều kiện qua từng cửa, và khi nào mới đủ điều kiện
nghĩ tới một bài báo.

Đây là **13 đề tài đã được chuẩn bị tới mức thực thi**, chọn từ danh mục
105 đề tài của chương trình. Các đề tài còn lại vẫn mở, chỉ chưa có lớp hồ sơ này.

## Bốn quy tắc không thương lượng

1. Không có baseline thì không có phương pháp đề xuất.
2. Không có bằng chứng thì không có kết luận.
3. Không tái lập được thì đề tài chưa hoàn thành ở mức nghiên cứu.
4. Không so sánh công bằng thì không được tuyên bố trong bài báo.

## Mức chiều sâu hoàn thành

| Mức | Tên | Nghĩa |
|---|---|---|
| **D0** | Readiness | Hiểu vấn đề, công cụ, baseline và metric. |
| **D1** | Engineering | Cài đặt đúng và được kiểm chứng. |
| **D2** | Research | Thí nghiệm có kiểm soát, baseline công bằng, bằng chứng tái lập. |
| **D3** | Publication | Câu hỏi nghiên cứu rõ, đóng góp có bằng chứng, hình/bảng sẵn sàng cho bản thảo. |

> Đừng nhầm với **L0–L5** trong danh mục đề tài: L là *mức sinh viên khi bắt đầu*,
> D là *mức chiều sâu khi kết thúc*. Một sinh viên L2 vẫn có thể đưa đề tài tới D2.

### Track A — Thiết kế IC số mã nguồn mở

_Năng lực RTL→GDSII bằng công cụ mã nguồn mở; nền dùng lại cho mọi đề tài ASIC phía sau._

| Mã đề tài | Tên | Mức vào | Phụ thuộc | Tiềm năng công bố | Hồ sơ |
|---|---|---|---|---|---|
| `A4-T01` | Thiết kế một Digital IP từ RTL đến GDSII | L2 | — | Trung bình | [mở](A4-T01/START-HERE.md) |
| `A5-T01` | Xây dựng quy trình ASIC tái lập sử dụng LibreLane + Nix | L3 | — | Trung bình | [mở](A5-T01/START-HERE.md) |

### Track B — Kiến trúc phần cứng số

_Datapath, fixed-point, pipeline, PPA và IP tái sử dụng — nền kỹ thuật cho trục C và D._

| Mã đề tài | Tên | Mức vào | Phụ thuộc | Tiềm năng công bố | Hồ sơ |
|---|---|---|---|---|---|
| `A2-T02` | Thiết kế và tối ưu MAC datapath cho FPGA/ASIC | L2 | — | Cao | [mở](A2-T02/START-HERE.md) |
| `A1-P04` | Thiết kế UART transmitter/receiver bằng RTL | L1 | — | Thấp, trừ khi làm thêm khảo sát độ bền | [mở](A1-P04/START-HERE.md) |

### Track C — Kiến trúc bộ giải mã Polar

_Từ SC baseline tới SC-Flip: đúng trước, nhanh sau; mọi cải tiến phải đo được trên cùng một baseline._

| Mã đề tài | Tên | Mức vào | Phụ thuộc | Tiềm năng công bố | Hồ sơ |
|---|---|---|---|---|---|
| `B2-T01` | Thiết kế bộ giải mã SC Polar trên FPGA | L3 | — | Trung bình | [mở](B2-T01/START-HERE.md) |
| `B3-T02` | Tối ưu fixed-point cho SC Polar decoder | L3 | B2-T01 | Cao | [mở](B3-T02/START-HERE.md) |
| `B4-T01` | Thiết kế và đánh giá SC-Flip Polar decoder | L3 | B3-T02 | Trung bình – cao | [mở](B4-T01/START-HERE.md) |
| `B4-T02` | Reliability-based candidate ranking cho SC-Flip | L3 | B4-T01 | Cao | [mở](B4-T02/START-HERE.md) |

### Track D — Giải mã Polar thích ứng / hỗ trợ neural

_Chỉ tiêu tốn tài nguyên cho frame khó; vùng có tiềm năng công bố cao nhất và cũng rủi ro nhất._

| Mã đề tài | Tên | Mức vào | Phụ thuộc | Tiềm năng công bố | Hồ sơ |
|---|---|---|---|---|---|
| `B5-T01` | Phát hiện frame không tin cậy cho adaptive Polar decoding | L3 | B4-T02 | Cao | [mở](B5-T01/START-HERE.md) |
| `B5-T02` | Adaptive decoder chỉ kích hoạt enhanced processing trên frame khó | L3 | B5-T01 | Rất cao | [mở](B5-T02/START-HERE.md) |
| `B5-T03` | Đồng thiết kế thuật toán - phần cứng cho bộ giải mã Polar thích ứng | L4 | B5-T02, B3-T02 | Rất cao | [mở](B5-T03/START-HERE.md) |
| `B6-T01` | Lightweight neural-assisted unreliable-frame detector | L4 | B5-T01 | Rất cao | [mở](B6-T01/START-HERE.md) |
| `B6-T02` | Neural-assisted candidate ranking cho SC-Flip Polar decoder | L4 | B4-T02 | Rất cao, kèm rủi ro cao | [mở](B6-T02/START-HERE.md) |

## Thứ tự kích hoạt

Không cần đợi đề tài trước xong 100%, nhưng **phải tôn trọng phụ thuộc**.

- **Mở được ngay:** `A4-T01`, `A5-T01`, `A2-T02`, `A1-P04`, `B2-T01`
- **Sau khi `B2-T01` có baseline chạy được:** `B3-T02`
- **Sau khi `B3-T02` có baseline chạy được:** `B4-T01`
- **Sau khi `B4-T01` có baseline chạy được:** `B4-T02`
- **Sau khi `B4-T02` có baseline chạy được:** `B5-T01`, `B6-T02`
- **Sau khi `B5-T01` có baseline chạy được:** `B5-T02`, `B6-T01`
- **Sau khi `B5-T02` và `B3-T02` có baseline chạy được:** `B5-T03`

> **Quy tắc baseline dùng chung.** Không nhân bản năm phiên bản SC khác nhau cho năm nhóm. Duy trì một 'golden baseline' dùng chung có tag/version; mọi đề tài phía sau phải ghi rõ commit/tag của baseline mà nó dùng.

## Cách mentor vận hành nhóm này

Xem `10_Documentation/RESEARCH-TRACKS.md` — họp theo track chứ không họp riêng từng đề tài,
điều kiện được escalation, và thang chấm PASS/FAIL.

## Bảng trạng thái

`03_Operations/STATUS_BOARD.md` — cập nhật sau mỗi buổi review.
