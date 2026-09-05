# Engineering & Research Mentoring Program (Lucero)

**ThS. Đinh Văn Nam (Mr. Lucero Dinh)** — Khoa Điện–Điện tử, Trường Kỹ thuật, Đại học Phenikaa
Phiên bản hệ thống **1.10.0** · cập nhật **04/09/2026**

Bộ hồ sơ vận hành mentoring cho bốn mức tham gia — **P** project môn học · **I** thực tập ·
**T** đồ án tốt nghiệp · **R** nghiên cứu khoa học — trên **105 đề tài** thuộc **16 nhóm chuyên môn**.

Chương trình chạy **dài hạn, qua nhiều học kỳ**. Mỗi kỳ mở một khóa lấy đề tài từ kho chung;
khung tiến độ tính theo **số tuần kể từ ngày sinh viên nhận đề tài**, không gắn với một học kỳ cụ thể.

## Vào đâu trước

| Anh là ai / cần gì | Mở |
|---|---|
| **Mentor lần đầu đọc hệ thống** | [`implementation-notes.md`](../implementation-notes.md) — từ bản chất tới triển khai |
| **Sinh viên chọn đề tài** | [trang Guide Notes](https://lucero6886.github.io/lucero-mentoring/guide.html) |
| **Xem có những đề tài gì** | [trang danh mục](https://lucero6886.github.io/lucero-mentoring/) · [`Ban_do_de_tai.md`](../Ban_do_de_tai.md) |
| **Làm một đề tài cụ thể** | [`02_Project_Portfolio/Topic_Guides/`](../02_Project_Portfolio/Topic_Guides/README.md) |
| **Chính sách gốc** | [`01_Governance/Master_Mentoring_Handbook.md`](../01_Governance/Master_Mentoring_Handbook.md) |
| **Vận hành hằng tuần** | [`03_Operations/MENTOR_WEEKLY_CHECKLIST.md`](../03_Operations/MENTOR_WEEKLY_CHECKLIST.md) |
| **Bản đồ toàn bộ file** | [`FILE_MANIFEST.md`](FILE_MANIFEST.md) |
| **Lịch sử thay đổi** | [`CHANGELOG.md`](CHANGELOG.md) |

## Bốn trục chuyên môn

1. **A0–A5 — Điện tử thực hành → RTL → DSP → FPGA → ASIC/EDA**
2. **A6–A7 — Hệ nhúng, IoT và trí tuệ biên**
3. **B0–B6 — Giải mã Polar: từ thuật toán tới phần cứng, tới thích ứng và hỗ trợ neural**
4. **AB — Vùng giao thoa co-design**: IC số × Polar × ràng buộc nhúng/IoT, theo định hướng nghiên cứu luận án

## Nguyên tắc kiến trúc

- **`06_Data/*.json` là nguồn chuẩn duy nhất.** Danh mục, phiếu, trang web, hồ sơ đề tài đều là bản
  sinh tự động. Sửa dữ liệu → chạy lại script; **không sửa tay bản sinh**.
- **Kiểm trước, sinh sau.** `python3 scripts/validate_portfolio.py` phải PASS trước mọi thao tác sinh.
- **Không lưu dữ liệu cá nhân sinh viên trong kho công khai.** Dữ liệu thật nằm ở `07_Private/`.

Chuỗi lệnh đầy đủ: [`implementation-notes.md`](../implementation-notes.md) §5.

## Chín điều bất biến

1. `06_Data/*.json` là nguồn chuẩn duy nhất.
2. Không đổi mã chuẩn của đề tài đã phát hành.
3. Không sửa tay file sinh tự động.
4. Không lưu cùng một dữ kiện ở hai nơi.
5. Validator phải PASS trước mọi thao tác sinh.
6. Không đưa dữ liệu cá nhân sinh viên lên kho công khai.
7. Khung tiến độ là tương đối theo tuần.
8. Baseline trước cái mới — Gate 2 chưa đạt thì không mở phần mở rộng nghiên cứu.
9. Không giải thích được thì chưa hoàn thành.

Lý do đằng sau từng điều: [`implementation-notes.md`](../implementation-notes.md) §9.
