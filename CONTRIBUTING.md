# Tham gia thảo luận và đóng góp

Kho này mở để sinh viên **đọc, chọn đề tài, hỏi và thảo luận công khai** — và để đồng nghiệp góp ý cải tiến
chương trình. Trang này nói rõ kênh nào dùng cho việc gì, và một ranh giới quan trọng về dữ liệu cá nhân.

---

## 🚫 Ranh giới quan trọng nhất: không đăng thông tin cá nhân

Đây là repo **công khai** — ai có link cũng đọc được, và nội dung có thể được lưu lại vĩnh viễn.

**Không bao giờ đăng vào Issue, Discussion hay Pull Request:**

- Họ tên đầy đủ kèm mã số sinh viên, email cá nhân, số điện thoại
- Phiếu nguyện vọng đã điền, bảng điểm, kết quả đánh giá năng lực
- Ảnh chụp màn hình có chứa các thông tin trên
- Bất kỳ thông tin nào của người khác mà bạn không được phép chia sẻ

**Những việc đó gửi riêng cho mentor** theo kênh đã thông báo trong lớp (email hoặc kênh liên lạc trực tiếp).
Nếu bạn lỡ đăng, hãy báo ngay để được gỡ — nhưng hãy coi như nội dung đã có thể bị lưu lại ở nơi khác.

---

## Kênh nào dùng cho việc gì

| Bạn muốn | Dùng |
|---|---|
| Hỏi một đề tài cụ thể yêu cầu gì, khó tới đâu, cần học trước cái gì | **Issue** → mẫu *Hỏi về một đề tài* |
| Thảo luận mở, chia sẻ tài liệu, tìm bạn cùng hướng | **Discussions** |
| Đề xuất một đề tài mới hoặc mở rộng đề tài có sẵn | **Issue** → mẫu *Đề xuất đề tài mới* |
| Báo lỗi tài liệu: sai chính tả, link hỏng, số liệu lệch, mô tả khó hiểu | **Issue** → mẫu *Báo lỗi tài liệu* |
| Nộp nguyện vọng, hồ sơ, câu hỏi riêng tư | **Gửi riêng cho mentor** (không dùng repo) |

---

## Hỏi sao cho nhận được câu trả lời hữu ích

Một câu hỏi tốt tiết kiệm thời gian cho cả hai bên. Trước khi hỏi:

1. **Xem [danh mục](https://lucero6886.github.io/lucero-mentoring/) và [`Ban_do_de_tai.md`](Ban_do_de_tai.md)** —
   phần lớn câu hỏi "đề tài này làm gì, nộp gì" đã có sẵn câu trả lời ở đó.
2. **Đọc [`10_Documentation/STUDENT-GUIDE.md`](10_Documentation/STUDENT-GUIDE.md)** cho các câu về cách chấm,
   cách nộp hằng tuần, quy tắc dùng AI.
3. **Tìm trong Issue đã có** — có thể người khác đã hỏi rồi.

Khi hỏi, nêu rõ: **mã đề tài** bạn quan tâm · **bạn đã biết/đã làm gì** liên quan · **chỗ bạn thấy chưa rõ**.
So sánh hai cách hỏi:

> ❌ "Đề tài A4-T01 có khó không ạ?"
>
> ✅ "Em quan tâm `A4-T01` (RTL → GDSII). Em đã viết được vài module Verilog và chạy mô phỏng, nhưng chưa
> từng dùng synthesis. Với nền đó thì em nên làm `A4-P01` trước một kỳ, hay vào thẳng `A4-T01` với phạm vi nhỏ hơn?"

Câu hỏi thứ hai nhận được lời khuyên dùng được ngay; câu đầu chỉ nhận được "còn tùy".

---

## Đề xuất đề tài mới

Rất hoan nghênh — nhiều đề tài tốt xuất phát từ chính sinh viên. Một đề xuất dùng được cần trả lời:

- **Bài toán là gì**, đầu vào và đầu ra cụ thể
- **Sản phẩm nộp được** ở cuối kỳ (cái gì chạy được, đo được)
- **Đo bằng gì** — tiêu chí định lượng nào chứng minh nó hoạt động
- **Cần biết trước những gì** để bắt đầu
- **Thuộc nhóm nào** trong 16 nhóm hiện có, hoặc vì sao cần nhóm mới

Đề xuất được chấp nhận sẽ được mentor chuẩn hóa và thêm vào `06_Data/project_portfolio.json`
với một mã chuẩn mới — và bạn được ghi nhận trong CHANGELOG.

---

## Nếu bạn muốn sửa trực tiếp (Pull Request)

Chỉ nhận PR cho **tài liệu người viết tay**: `10_Documentation/`, `CONTRIBUTING.md`, `README.md`, sửa lỗi trong `04_Project_Template/`.

**Không nhận PR sửa tay các file sinh tự động** — chúng sẽ bị ghi đè ở lần phát hành sau:

- `02_Project_Portfolio/*` · `Danh_muc_*` · `Phieu_*` · `docs/index.html` · `Ban_do_de_tai.*` · `build/*`

Muốn đổi nội dung đề tài: sửa `06_Data/project_portfolio.json`, chạy `python3 scripts/validate_portfolio.py`
(phải PASS) rồi chạy lại các script sinh tài liệu — hoặc đơn giản là mở Issue mô tả thay đổi mong muốn,
mentor sẽ làm phần còn lại.

---

## Quy tắc ứng xử

Tôn trọng, thẳng thắn, tập trung vào nội dung kỹ thuật. Không hạ thấp người khác vì họ chưa biết —
mọi người ở đây đều đang học. Câu hỏi "cơ bản" luôn được chào đón; câu trả lời trịch thượng thì không.

Nội dung vi phạm ranh giới dữ liệu cá nhân ở đầu trang này sẽ bị gỡ mà không cần báo trước.
