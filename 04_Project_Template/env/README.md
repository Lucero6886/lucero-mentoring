# Script dựng môi trường

**Engineering & Research Mentoring Program (Lucero)** · ThS. Đinh Văn Nam (Mr. Lucero Dinh)
Khoa Điện–Điện tử, Trường Kỹ thuật, Đại học Phenikaa

Ba script ở đây **rút ngắn** [`10_Documentation/SETUP-GUIDE.md`](../../10_Documentation/SETUP-GUIDE.md).
Chúng không thay thế tài liệu đó: script cài hộ, tài liệu giải thích **vì sao**. Sinh viên vẫn phải
đọc tài liệu, vì mentor sẽ hỏi vì sao chứ không hỏi đã gõ lệnh gì.

## Hai lớp khác nhau — đừng nhầm

| | Làm gì | Bảo đảm điều gì |
|---|---|---|
| **`bootstrap.sh`** | **Tự động hóa**: cài hộ những gì tài liệu bảo cài | Đỡ gõ tay, đỡ sai chính tả. **Không** bảo đảm hai máy giống nhau |
| **`flake.nix`** (trong repo đề tài) | **Tái lập**: ghim đúng phiên bản từng công cụ | Máy nào cũng ra **đúng cùng một** phiên bản, hôm nay và sáu tháng sau |

`apt install iverilog` hôm nay và sáu tháng sau cho hai phiên bản khác nhau — script không cứu được
điều đó. Chỉ `flake.nix` kèm `flake.lock` đã commit mới cứu được. Với đề tài `A4`, `A5` thì đây
**là nội dung đề tài**, không phải tiểu tiết kỹ thuật.

## Ba script

| File | Chạy ở đâu | Làm gì |
|---|---|---|
| `setup-windows.ps1` | PowerShell 64-bit, quyền Administrator | WSL2, Git, VS Code, Windows Terminal, KiCad, extension |
| `bootstrap.sh` | terminal Ubuntu (WSL) | gói nền, cấu hình Git, khóa SSH, công cụ theo nhánh, Nix + LibreLane |
| `doctor.sh` | terminal Ubuntu (WSL) | **chỉ kiểm, không cài** — in bảng đạt/chưa đạt |

Cả ba **chạy lại được nhiều lần**: mỗi bước kiểm trước, có rồi thì bỏ qua.

## Dùng thế nào

**Bước 1 — phía Windows** (một lần cho mỗi máy):

```powershell
cd "C:\...\EEE Projects\04_Project_Template\env"
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force
.\setup-windows.ps1 -DryRun          # xem trước sẽ làm gì
.\setup-windows.ps1                  # chạy thật
```

> **Phải `cd` trước.** *Run as administrator* mở PowerShell ở `C:\Windows\System32`, nên
> `.\setup-windows.ps1` sẽ báo *"is not recognized"*. Đường dẫn có khoảng trắng thì để trong
> dấu nháy kép. Lấy đường dẫn nhanh: Shift + chuột phải vào thư mục → *Copy as path*.

Khởi động lại máy nếu script vừa cài WSL.

**Bước 2 — trong Ubuntu (WSL)**, chọn cờ theo nhánh đề tài:

```bash
cd <thư-mục-env>                     # ls *.sh phải thấy bootstrap.sh
bash bootstrap.sh --dry-run          # xem trước
bash bootstrap.sh                    # nền chung, ai cũng chạy
bash bootstrap.sh --rtl              # nhánh A1–A3
bash bootstrap.sh --asic             # nhánh A4–A5 (Nix + LibreLane)
bash bootstrap.sh --polar            # nhánh B0–B6
bash bootstrap.sh --all              # tất cả
```

**Bước 3 — nghiệm thu:**

```bash
bash doctor.sh --all
```

Mã thoát `0` là đạt. **Chụp màn hình kết quả nộp kèm báo cáo tuần 1** — đây là thứ mentor xem thay
cho câu *"em cài xong rồi ạ"*.

## Script KHÔNG làm được gì

Bốn việc dưới đây không tự động hóa được, và tài liệu ghi rõ từng bước:

1. **Bật ảo hóa trong BIOS** — nằm ngoài hệ điều hành.
2. **Dán khóa SSH lên GitHub** — cần tài khoản của chính em. Script tạo khóa và in ra sẵn để chép.
3. **Quartus Prime Lite** — trình cài đồ họa, phải tick đúng dòng device của board trong lab.
4. **Driver CH340/CP2102** — phụ thuộc chip thật trên board ESP8266 đang cầm.

## Khi script báo lỗi

`bootstrap.sh` ghi toàn bộ đầu ra vào `~/.mentoring-bootstrap.log`. Gặp lỗi thì mở file đó xem dòng
cuối, đối chiếu [`SETUP-GUIDE.md`](../../10_Documentation/SETUP-GUIDE.md) Phần F. Vẫn kẹt quá hai
giờ thì mở Issue, kèm **nguyên văn** dòng lỗi và kết quả `bash doctor.sh --all`.
