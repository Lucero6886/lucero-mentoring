# Bộ khởi tạo repo cho sinh viên

Dùng bộ này để tạo repo làm việc của em trong **buổi onboarding tuần 1**, không phải để dành đến cuối kỳ.
Repo dựng đúng ngay từ đầu tiết kiệm cho em hàng chục giờ ở tuần 13.

## Ba bước

**1. Tạo repo trên tài khoản GitHub của em**

```
Tên:     <mã-đề-tài>-<tên-ngắn>     ví dụ  a4-t01-minh
Chế độ:  Private
Không tick thêm README/gitignore/license (bộ này đã có sẵn)
```

**2. Copy toàn bộ nội dung thư mục `template/` vào repo mới** — kể cả các file ẩn (`.gitignore`, `.github/`).

Trên Windows, bật *Hiện file ẩn* trong File Explorer trước khi copy, nếu không `.github/` sẽ bị bỏ sót.

**3. Mời mentor vào repo:** Settings → Collaborators → Add people.

Rồi commit lần đầu:

```bash
git add -A
git commit -m "khởi tạo repo đồ án <mã đề tài>"
git push
```

## Sau đó, ngay trong buổi onboarding

- Điền `PROJECT_CHARTER.md`: chốt **MVT** (phần bắt buộc) tách khỏi **Extension** (phần mở rộng) — copy mẫu từ
  `../PROJECT_CHARTER_TEMPLATE.md` ở thư mục cha.
- Tạo **6 milestone** đúng tên và hạn gate của cohort (mentor đọc từ `06_Data/cohort_*.json`).
- Copy tiếp các biểu mẫu cần dùng từ thư mục cha `04_Project_Template/`: `EVIDENCE_LEDGER.md`,
  `DECISION_LOG.md`, `AI_USAGE_LOG.md`, `WEEKLY_REPORT_TEMPLATE.md`.

## Trong bộ này có gì

| File | Vai trò |
|---|---|
| `template/README.md` | Mẫu README của repo em — **viết dần từ tuần 1**, không để cuối kỳ |
| `template/.gitignore` | Chặn sẵn rác mô phỏng, tổng hợp, Vivado/Quartus, Python, hệ điều hành |
| `template/.github/ISSUE_TEMPLATE/bao-cao-tuan.yml` | Mẫu Issue báo cáo tuần (em mở mỗi tuần) |
| `template/.github/ISSUE_TEMPLATE/gate-review.yml` | Mẫu Issue gate review (mentor mở ở mỗi trạm) |

Cách vận hành đầy đủ: [`../../10_Documentation/GITHUB-WORKFLOW.md`](../../10_Documentation/GITHUB-WORKFLOW.md).
