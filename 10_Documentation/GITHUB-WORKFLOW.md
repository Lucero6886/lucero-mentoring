# Vận hành chương trình trên GitHub

**Engineering & Research Mentoring Program (Lucero)** · ThS. Đinh Văn Nam (Mr. Lucero Dinh)
Khoa Điện–Điện tử, Trường Kỹ thuật, Đại học Phenikaa

Trang này trả lời ba câu: **cái gì công khai, cái gì riêng tư, và mọi người làm việc với nhau thế nào**
khi chương trình chạy trên GitHub. Dành cho cả sinh viên, mentor và giảng viên đồng hành.

---

## 1. Quy tắc phân loại — một câu duy nhất

> **Nội dung nói về ĐỀ TÀI thì công khai. Nội dung nói về MỘT CON NGƯỜI thì không.**

Mô tả đề tài `A4-T01`, tiêu chí qua Gate 2, cách chấm mức sẵn sàng — đều là *đề tài* → công khai được.
Bạn Minh đạt WR 13/20, bạn Lan bị cảnh báo tuần 6, danh sách điểm — đều là *con người* → không bao giờ lên GitHub công khai.

Áp dụng quy tắc này thì mọi trường hợp mập mờ đều tự giải quyết.

---

## 2. Ba tầng riêng tư

| Tầng | Ở đâu | Chứa gì | Ai thấy |
|---|---|---|---|
| **① Công khai** | Repo `lucero-mentoring` (Public) | Danh mục 105 đề tài, luật chơi, hướng dẫn, biểu mẫu trống, script, trang web | Cả thế giới |
| **② Riêng tư** | Một repo riêng cho **mỗi sinh viên** (Private) | Code, testbench, kết quả, báo cáo tuần, charter, sổ bằng chứng | Sinh viên đó + mentor |
| **③ Không lên GitHub** | `07_Private/` trên máy mentor | Workbook có tên thật/điểm, Phiếu 5 đã chấm, cảnh báo, dữ liệu cá nhân | Chỉ mentor |

Ba tầng này không phải để "giữ bí mật" mà để **mỗi thứ ở đúng chỗ có ích nhất**: luật chơi càng công khai càng
tốt (ai cũng biết mình được đánh giá bằng gì); công việc đang dở càng kín càng tốt (không ai bị nhìn khi chưa xong);
đánh giá cá nhân thì thuộc về hồ sơ đào tạo, không thuộc về một nền tảng thương mại nước ngoài.

---

## 3. Tầng ① — Repo công khai chứa chính xác những gì

**Có trên repo:**

| Nhóm | Vì sao công khai |
|---|---|
| `06_Data/` — nguồn chuẩn 105 đề tài, thang đánh giá, 6 gate | Sinh viên tự tra được, người khác tái lập được hệ thống |
| Danh mục, phiếu **trống**, bản đồ đề tài, trang web catalog | Đây là thứ sinh viên cần để chọn |
| `01_Governance/` — sổ tay, thỏa thuận, quy tắc AI | Luật chơi phải minh bạch trước khi ai đó tham gia |
| `10_Documentation/` — hướng dẫn theo vai trò | Ai cũng biết mình phải làm gì |
| `04_Project_Template/` — 15 biểu mẫu **trống** | Sinh viên copy về repo riêng để dùng |
| `scripts/` + `tests/` | Chứng minh danh mục sinh tự động, không phải gõ tay |

**Không bao giờ có trên repo:** phiếu đã điền · họ tên kèm mã số sinh viên · điểm, kết quả đánh giá năng lực ·
workbook có dữ liệu thật · ảnh chụp màn hình chứa các thứ trên · file PDF bài báo có bản quyền.

`.gitignore` đã chặn sẵn `07_Private/`, nhưng **`.gitignore` chỉ chặn thứ nằm đúng chỗ** — kỷ luật vẫn là:
dữ liệu thật chỉ được lưu trong `07_Private/`, không rải ra ngoài.

---

## 4. Tầng ② — Repo làm việc của từng sinh viên

Đây là phần thay đổi cách vận hành nhiều nhất, nên làm cho đúng ngay từ tuần 1.

### Ai tạo, đặt tên thế nào

**Sinh viên tự tạo trên tài khoản của mình** — không phải mentor tạo hộ. Lý do quan trọng: khi tốt nghiệp,
đó là **hồ sơ năng lực (portfolio)** của em, mang theo đi xin việc. Ngành thiết kế vi mạch tuyển người bằng
thứ nhìn thấy được; một repo sạch sẽ với lịch sử commit đều đặn nói nhiều hơn một dòng trong CV.

```
Tên repo:  <mã-đề-tài>-<tên-ngắn>       ví dụ:  a4-t01-minh   ·   b3-t01-lan
Chế độ:    Private trong suốt học kỳ
Mời:       mentor làm Collaborator (Settings → Collaborators)
```

### Cấu trúc chuẩn bên trong

```
README.md              ← chạy lại thế nào; cập nhật liên tục, không để cuối kỳ mới viết
PROJECT_CHARTER.md     ← MVT và Extension tách bạch (copy từ 04_Project_Template/)
EVIDENCE_LEDGER.md     ← sổ bằng chứng: claim nào dựa trên file/kết quả nào
DECISION_LOG.md        ← quyết định kỹ thuật và lý do (không sửa đè dòng cũ)
AI_USAGE_LOG.md        ← dùng AI làm gì, đã kiểm chứng bằng cách nào
rtl/  tb/  sim/  syn/  scripts/  docs/  results/
weekly/                ← báo cáo tuần (hoặc dùng Issue, xem §5)
```

Bộ khởi tạo có sẵn: **`04_Project_Template/student_repo_starter/`** — copy nguyên vào repo mới là chạy được.

### Cuối kỳ

1. Gắn tag và tạo **Release `v1.0-final`**, đính kèm gói bàn giao (Legacy Package).
2. Sinh viên **nên** chuyển repo sang Public sau bảo vệ — thành portfolio. Không bắt buộc; nếu đề tài có ràng buộc
   với đơn vị tài trợ thì giữ private.
3. Mentor được trao quyền lưu một bản (fork hoặc mirror) để khóa sau kế thừa — **thỏa thuận trước từ tuần 1**,
   không phải xin sau khi xong.

---

## 5. Nhịp một tuần trên GitHub

Nhịp cũ (chat + file đính kèm) hỏng ở ba chỗ: mentor phải nhớ ai nói gì, "em nộp rồi ạ" không kiểm chứng được,
và tiến độ tan vào lịch sử trò chuyện. GitHub sửa cả ba mà không cần thêm công cụ nào.

| Khi nào | Sinh viên | Mentor |
|---|---|---|
| **Trong tuần** | Commit theo từng bước nhỏ, thông điệp commit nói *đã làm gì* | (không can thiệp) |
| **Trước buổi gặp 24h** | Mở **Issue** *"Báo cáo tuần N"* theo mẫu, mỗi mục evidence là **một link tới commit/file/hình** | Đọc issue + lướt commit trong tuần |
| **Trong buổi gặp** | Trình bày: Mục tiêu → Bằng chứng → Cái gì hỏng → Chẩn đoán → Đề xuất bước tiếp | Gỡ vướng, không giảng lại |
| **Cuối buổi** | — | Comment chốt **1–3 việc + hạn** ngay trong issue, rồi đóng issue |

**Vì sao cách này hiệu quả:** mỗi dòng bằng chứng đã có sẵn dấu thời gian và tác giả — không ai phải chứng minh
"em có làm". Mentor mở đúng một trang là thấy cả tuần. Và khi cần rà lại tuần 4 vào lúc bảo vệ, nó vẫn nằm nguyên đó.

> **Lịch sử commit chính là bằng chứng về quyền sở hữu.** Một repo có commit đều đặn suốt 15 tuần kể một câu chuyện
> khác hẳn một repo chỉ có một commit khổng lồ ở tuần 14. Đây cũng là cách kiểm tra tự nhiên cho quy tắc
> *cannot explain = not completed*.

---

## 6. Sáu gate trên GitHub

Khung tiến độ của chương trình là **tương đối** — đếm theo số tuần kể từ ngày sinh viên nhận đề tài, nên dùng lại được cho mọi khóa. Trong repo của mỗi sinh viên, tạo **6 Milestone** theo khung này; ngày dương lịch của milestone thì quy đổi từ ngày khóa đó bắt đầu (`start_date` trong `06_Data/cohort_*.json`):

```
Gate 1 · Problem & Foundation        hết tuần 2
Gate 2 · Baseline                    hết tuần 5
Gate 3 · Core Implementation         hết tuần 8
Gate 4 · Experiments                 hết tuần 11
Gate 5 · Analysis & Draft            hết tuần 13
Gate 6 · Reproducibility & Defense   hết tuần 15
```

Mọi issue (báo cáo tuần, việc cần làm, lỗi) gán vào milestone tương ứng → thanh tiến độ của milestone chính là
tiến độ thật, tự cập nhật.

**Buổi gate review:** mentor mở issue *"Gate N — review"* chứa checklist đúng câu chữ tiêu chí trong nguồn chuẩn,
tick từng mục, kết luận một trong bốn: `PASS` · `CONDITIONAL_PASS` (kèm điều kiện + hạn) · `FAIL` ·
`NOT_ENOUGH_EVIDENCE`. Kết luận nằm trong issue → không ai nhớ nhầm về sau. Qua gate thì gắn tag `gate-2-passed`.

Luật cứng vẫn nguyên: không baseline ở Gate 2 → đóng extension · trượt Gate 3 → thu nhỏ phạm vi ·
sau Gate 4 → không thêm thuật toán lớn mới.

---

## 7. Bảng điều khiển của mentor — một phút mỗi sáng thứ Hai

Tạo **một GitHub Project** (loại bảng) ở cấp tài khoản/tổ chức, tên *"Cohort HK1 2026-2027"*.
Project cấp tài khoản gom được issue từ **nhiều repo khác nhau** — đó chính là điều cần cho việc mentor nhiều em.

- Cột: `Tuần này` · `Đang chờ mentor` · `Đã chốt` — hoặc theo gate.
- Trường tự thêm: `Sinh viên`, `Mã đề tài`, `Risk` (🟢🟡🔴), `Hạn kế tiếp`.
- Mỗi sáng thứ Hai nhìn cột `Risk` và cột `Hạn kế tiếp`: ai vàng/đỏ, ai quá 7 ngày không có commit → mở sâu em đó.

**Workbook `03_Operations/Mentoring_Management_Workbook.xlsx` vẫn giữ nguyên vai trò** — nhưng chỉ cho phần
GitHub không nên chứa: điểm số, đánh giá năng lực, ghi chú cảnh báo. GitHub theo dõi *công việc*; workbook lưu
*đánh giá*. Đừng trộn hai thứ.

---

## 8. Thảo luận chung — nơi cả lớp cùng lợi

Bật **Discussions** trên repo công khai, chia bốn mục:

| Mục | Dùng cho |
|---|---|
| **Hỏi đáp kỹ thuật** | Vướng mắc chung: cài toolchain, hiểu khái niệm, lỗi hay gặp |
| **Chọn đề tài** | "Nền của em thế này thì nên `A6-T01` hay `A7-T02`?" |
| **Chia sẻ tài liệu** | Bài báo hay, tutorial, ghi chú của các khóa trước |
| **Thông báo** | Mentor phát tin về cohort, bootcamp, hạn nộp |

Nguyên tắc dùng: **hỏi một lần, cả lớp cùng đọc.** Nhiều em cùng vướng một chỗ là tín hiệu mở bootcamp chung
một buổi thay vì giải thích 1-1 mười lần — đúng nguyên tắc phân bổ 50–60% thời gian cho việc chung.

Việc riêng của một em (kết quả của em, lỗi trong code của em) thì thảo luận trong repo riêng của em, không đưa ra đây.

---

## 9. Vai trò và quyền

| Vai trò | Repo công khai | Repo sinh viên | `07_Private/` |
|---|---|---|---|
| **Sinh viên** | Đọc · mở Issue · thảo luận · gửi PR sửa tài liệu | **Chủ sở hữu** repo của mình | Không truy cập |
| **Mentor** | Admin | Collaborator ở mọi repo sinh viên | Toàn quyền |
| **Giảng viên đồng hành / đồng hướng dẫn** | Đọc (hoặc Write nếu cùng biên soạn) | Collaborator ở repo em mình đồng hướng dẫn | Theo phân công của bộ môn |
| **Người ngoài, khóa sau** | Đọc · thảo luận · đề xuất đề tài | Không | Không |

**Khi số lượng lớn dần** (nhiều mentor, nhiều khóa cùng lúc), chuyển sang **GitHub Organization**: repo công khai
và toàn bộ repo sinh viên nằm dưới một tổ chức, phân quyền theo Team (`mentors`, `cohort-2026-1`). Miễn phí,
và giải quyết được việc bàn giao khi có người rời đi. Chưa cần làm ngay — chỉ cần biết đường đi khi tới lúc.

---

## 10. Điều tuyệt đối không làm

| Không | Vì sao |
|---|---|
| Đăng dữ liệu cá nhân của mình hoặc của người khác lên repo công khai | Không thu hồi được; vi phạm quyền riêng tư của người khác |
| Commit file PDF bài báo có bản quyền | Vi phạm bản quyền. Chỉ lưu **link + ghi chú của mình** |
| Commit file > 100 MB, dataset lớn, file build | GitHub chặn 100 MB; repo phình ra là không ai clone nổi. Dùng Release đính kèm hoặc Git LFS |
| `git push --force` xóa lịch sử | Lịch sử **chính là bằng chứng**. Xóa nó là xóa chứng minh quyền sở hữu của em |
| Một commit khổng lồ vào tuần cuối | Không chứng minh được quá trình; và thường đi kèm việc không giải thích được |
| Sửa tay các file sinh tự động rồi gửi PR | Bị ghi đè ở lần phát hành sau — sửa `06_Data/` rồi chạy script |

---

## 10b. Cấu hình GitHub Pages — phải là `main` / `/docs`

Trang web của chương trình gồm **hai trang**, cả hai nằm trong `docs/`:

| Đường dẫn | Trang |
|---|---|
| `/` | Danh mục đề tài có lọc và tìm kiếm (`docs/index.html`) |
| `/guide.html` | Hướng dẫn chọn đề tài cho sinh viên (`docs/guide.html`) |

Muốn hai đường dẫn đó đúng thì **Settings → Pages → Build and deployment** phải đặt
**Branch: `main`, Folder: `/docs`**.

> **Đặt nhầm thành `/ (root)` thì hỏng thế nào.** Pages sẽ chạy Jekyll trên cả kho và
> dựng `README.md` thành trang chủ; hai trang thật bị đẩy xuống `/docs/index.html` và
> `/docs/guide.html`, nên **mọi link tuyệt đối trong README đều 404**. Triệu chứng đặc
> trưng: mở `https://lucero6886.github.io/lucero-mentoring/` thấy đúng nội dung README
> chứ không phải bảng danh mục có ô tìm kiếm.

**Cách kiểm tra trong 5 giây.** Mở `https://lucero6886.github.io/lucero-mentoring/docs/guide.html`:

- **404** → cấu hình đúng (`/docs`).
- **Mở được** → cấu hình đang là `/ (root)`, phải sửa lại.

Sau khi đổi, Pages dựng lại khoảng 1–2 phút. Nếu trình duyệt vẫn hiện trang cũ thì tải lại
bỏ qua cache (Ctrl+F5) — đây là nguyên nhân giả thường gặp nhất sau khi sửa đúng.

### Hai file chuyển hướng ở thư mục gốc

Kho có sẵn `index.html` và `guide.html` **ở thư mục gốc**. Chúng **không chứa nội dung** —
chỉ chuyển hướng sang `docs/index.html` và `docs/guide.html`, và tồn tại để hai địa chỉ đã
công bố cho sinh viên luôn đúng **ở cả hai cấu hình**:

| Pages publish từ | Điều gì xảy ra |
|---|---|
| `/docs` (đúng) | Hai file gốc **không được phục vụ**; `/` và `/guide.html` là trang thật. Chúng nằm im, vô hại. |
| `/ (root)` | Hai file gốc nhận `/` và `/guide.html` rồi đẩy sang `docs/…`. Link vẫn chạy. |

Đừng viết nội dung vào hai file này và đừng xóa chúng — chúng là lưới an toàn cho cấu hình
Pages, thứ nằm ngoài kho nên không kiểm soát được bằng script.

---

## 11. Lộ trình triển khai — ba giai đoạn

**Giai đoạn 1 — Bây giờ (trước khi phát danh mục)**

- [x] Đẩy repo công khai `lucero-mentoring` lên GitHub
- [ ] Bật GitHub Pages đúng **`main` / `/docs`** (xem §10b — đặt nhầm `/ (root)` làm hỏng mọi link tuyệt đối)
- [ ] Bật Discussions và tạo 4 mục ở §8
- [ ] Gửi cho sinh viên **một** link duy nhất: trang danh mục. Mọi thứ khác dẫn từ đó

**Giai đoạn 2 — Tuần 1 của học kỳ, cùng buổi onboarding**

- [ ] Mỗi em tạo repo riêng theo §4, mời mentor làm collaborator
- [ ] Copy `04_Project_Template/student_repo_starter/` vào repo mới
- [ ] Tạo 6 milestone theo hạn gate của cohort
- [ ] Chốt MVT và Extension trong `PROJECT_CHARTER.md`, commit ngay trong buổi
- [ ] Mentor tạo Project board gom issue của cả nhóm

**Giai đoạn 3 — Từ tuần 2 đến hết kỳ**

- [ ] Nhịp tuần theo §5, gate review theo §6
- [ ] Mỗi lần sửa nội dung chương trình: sửa `06_Data/` → chạy script → `git push` (repo công khai tự cập nhật,
      trang web tự cập nhật theo)
- [ ] Cuối kỳ: release gói bàn giao, quyết định công khai hóa repo sinh viên

---

## Phụ lục · Bảy lệnh git sinh viên cần biết

```bash
git clone <url>                  # lấy repo về máy
git status                       # đang có gì thay đổi
git add <file>                   # chọn thứ muốn ghi lại
git commit -m "thêm testbench cho FIFO, chạy pass 3 case"   # ghi lại một bước
git push                         # đẩy lên GitHub
git pull                         # lấy thay đổi mới nhất về
git log --oneline                # xem lại lịch sử
```

**Thông điệp commit tốt** nói *đã làm gì và kết quả ra sao*: `sửa lỗi tràn ở stage 3 của MAC, sai số giảm còn 2 LSB`.
**Thông điệp tệ**: `update`, `fix`, `abc`. Một tháng sau chính em sẽ là người phải đọc lại chúng.

---

*Tài liệu liên quan: [`STUDENT-GUIDE.md`](STUDENT-GUIDE.md) — cách chương trình đánh giá ·
[`MENTOR-GUIDE.md`](MENTOR-GUIDE.md) — thao tác từng buổi ·
[`WORKFLOW.md`](WORKFLOW.md) — sửa dữ liệu và sinh lại tài liệu ·
[`../CONTRIBUTING.md`](../CONTRIBUTING.md) — quy tắc tham gia repo công khai.*
