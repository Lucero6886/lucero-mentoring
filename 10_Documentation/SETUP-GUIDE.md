# Dựng môi trường làm việc — hướng dẫn thực hành cho sinh viên

**Engineering & Research Mentoring Program (Lucero)** · ThS. Đinh Văn Nam (Mr. Lucero Dinh)
Khoa Điện–Điện tử, Trường Kỹ thuật, Đại học Phenikaa

> **Tài liệu này dành cho em, làm trong tuần đầu tiên.** Nó không dạy em làm đề tài — nó dạy em
> dựng cái bàn làm việc để bắt đầu làm được. Mọi lệnh trong đây đều đã được kiểm; em gõ theo,
> không cần hiểu ngay vì sao.
>
> **Xong tài liệu này là một phần điều kiện của Gate 1.** Mentor sẽ hỏi: *"chạy thử cho thầy xem"*.

---

## Cách dùng tài liệu này

Tài liệu chia hai lớp. **Ai cũng phải làm Phần A.** Sau đó chỉ làm **một** phần nhánh, đúng nhánh
đề tài của em.

| Phần | Dành cho | Thời gian |
|---|---|---|
| **A · Nền chung** | **Mọi sinh viên, không trừ ai** | 3–5 giờ |
| **B · Điện tử thực hành và PCB** | nhánh `A0` | +3 giờ |
| **C · RTL → FPGA → ASIC** | nhánh `A1`–`A5` | +4 giờ |
| **D · Nhúng và IoT với ESP8266** | nhánh `A6`, `A7` | +3 giờ |
| **E · Mô phỏng Polar** | nhánh `B0`–`B6` | +2 giờ |
| **F · Sự cố thường gặp** | tra khi kẹt | — |
| **G · Checklist nghiệm thu** | trước buổi gặp mentor | 30 phút |

Chưa biết mình thuộc nhánh nào? Mã đề tài nói cho em biết: hai ký tự đầu là nhóm (`A4-T01` → nhóm `A4`).
Xem [trang hướng dẫn chọn đề tài](https://lucero6886.github.io/lucero-mentoring/guide.html).

**Quy ước trong tài liệu:**

- Dòng bắt đầu bằng `$` là lệnh gõ trong **terminal Ubuntu (WSL)**.
- Dòng bắt đầu bằng `PS>` là lệnh gõ trong **PowerShell của Windows**.
- Khối *"Phải thấy gì"* là kết quả đúng. Không thấy đúng thì **dừng lại**, đừng đi tiếp.

---

# Phần A · Nền chung

Bốn thứ em dựng ở đây dùng cho mọi đề tài, mọi nhánh: **một máy Linux để chạy công cụ**,
**Git để lưu vết công việc**, **Python có kiểm soát**, và **kỷ luật ghi chép thí nghiệm**.

## A1. Vì sao phải có Linux, và WSL2 là gì

Gần như toàn bộ công cụ của ngành thiết kế vi mạch và xử lý tín hiệu được viết cho Linux. Cài
Windows-only nghĩa là tự cắt mình khỏi phần lớn tài liệu, ví dụ và cộng đồng.

**WSL2** cho phép chạy một máy Ubuntu thật ngay bên trong Windows, dùng chung file và mạng, không
cần chia ổ hay khởi động lại. Em vẫn dùng Windows như thường ngày; Ubuntu chỉ là một cửa sổ terminal.

### Trước khi cài — kiểm ba điều kiện

Bỏ qua bước này là nguyên nhân số một của lỗi *"wsl is not recognized"*. Mở PowerShell
(chưa cần quyền admin) và chạy:

```powershell
PS> "PowerShell 64-bit? " + [Environment]::Is64BitProcess
PS> "Windows build   : " + [System.Environment]::OSVersion.Version.Build
PS> "System32\wsl.exe: " + (Test-Path C:\Windows\System32\wsl.exe)
```

**Phải thấy gì**

```text
PowerShell 64-bit? True
Windows build   : 19045          # phải ≥ 19041
System32\wsl.exe: True
```

Ba dòng đó đúng thì đi tiếp. Sai bất kỳ dòng nào — **xem §F1 trước khi gõ lệnh cài**.

### Mở đúng cửa sổ PowerShell

Bấm `Start`, gõ `powershell`. Danh sách sẽ có **hai** mục:

- **Windows PowerShell** ← chọn mục này
- **Windows PowerShell (x86)** ← **không** chọn mục này

Bản `(x86)` là 32-bit. Windows tự chuyển hướng `System32` của tiến trình 32-bit sang `SysWOW64`,
nơi **không có** `wsl.exe` — nên máy báo không nhận lệnh dù WSL vẫn cài được bình thường.

Chuột phải **Windows PowerShell** → *Run as administrator*. Máy nào có **Windows Terminal** thì
dùng nó, mặc định đã là 64-bit.

### Cài WSL2

```powershell
PS> wsl --install -d Ubuntu
```

Khởi động lại máy. Sau khi khởi động lại, cửa sổ Ubuntu tự mở và hỏi:

- **username**: đặt chữ thường, không dấu, không khoảng trắng — ví dụ `nam`
- **password**: gõ vào sẽ **không hiện gì cả**, kể cả dấu sao. Đó là bình thường, không phải máy treo.

**Phải thấy gì**

```text
nam@DESKTOP-XXXX:~$
```

Gặp lỗi ở bước này — *"wsl is not recognized"*, đòi virtualization, hay treo giữa chừng — thì
**xem §F1**, ở đó có bảng chẩn đoán cho từng trường hợp.

### Cập nhật và cài bộ công cụ nền

```bash
$ sudo apt update && sudo apt upgrade -y
$ sudo apt install -y build-essential git curl wget unzip \
      python3 python3-pip python3-venv
```

**Phải thấy gì**

```bash
$ git --version
git version 2.43.0          # số có thể khác, miễn là ≥ 2.30
$ python3 --version
Python 3.12.3               # ≥ 3.10 là được
$ gcc --version | head -1
gcc (Ubuntu 13.2.0-...) 13.2.0
```

### Hai thế giới file — chỗ sai phổ biến nhất

WSL có **hai hệ thống file riêng biệt**, và để nhầm chỗ sẽ làm mọi thứ chậm gấp 10–20 lần:

| Đường dẫn | Là gì | Tốc độ |
|---|---|---|
| `/home/nam/` (viết tắt `~`) | ổ đĩa của Ubuntu | **nhanh** |
| `/mnt/c/Users/admin/` | ổ C: của Windows nhìn từ Ubuntu | **rất chậm** khi build |
| `\\wsl.localhost\Ubuntu\home\nam\` | ổ Ubuntu nhìn từ Windows Explorer | chậm vừa |

**Quy tắc đặt repo — tra bảng này, đừng đoán:**

| Nhánh đề tài | Đặt repo ở đâu | Vì sao |
|---|---|---|
| `A1`, `A2`, `A5`, `B0`–`B6` | **WSL**: `~/projects/<tên-repo>` | mô phỏng và build chạy hoàn toàn trong Linux |
| `A3`, `A4` (dùng Quartus) | **Windows**: `C:\Users\<tên>\projects\<tên-repo>` | Quartus là phần mềm Windows, hay lỗi với đường dẫn `\\wsl` |
| `A0` (KiCad), `A6`, `A7` (ESP8266) | **Windows** | KiCad và việc nạp qua USB đều nằm ở Windows |

Nếu repo ở Windows mà cần chạy công cụ Linux, truy cập qua `/mnt/c/Users/<tên>/projects/...` —
chấp nhận chậm, chỉ dùng cho việc nhẹ.

Tạo thư mục làm việc:

```bash
$ mkdir -p ~/projects && cd ~/projects && pwd
/home/nam/projects
```

### Mười hai lệnh terminal phải thuộc

Không thuộc mười hai lệnh này thì mọi phần sau sẽ rất chật vật.

| Lệnh | Làm gì |
|---|---|
| `pwd` | đang đứng ở thư mục nào |
| `ls -la` | liệt kê file, kể cả file ẩn |
| `cd <thư-mục>` · `cd ..` · `cd ~` | đi vào · lùi ra · về nhà |
| `mkdir -p a/b/c` | tạo thư mục, tạo cả cây |
| `cp a b` · `mv a b` · `rm a` | chép · đổi tên hoặc di chuyển · xóa |
| `cat f` · `less f` | xem cả file · xem có cuộn (`q` để thoát) |
| `grep -rn "chữ" .` | tìm chuỗi trong mọi file từ đây trở xuống |
| `nano f` | sửa nhanh (`Ctrl+O` lưu, `Ctrl+X` thoát) |
| `<lệnh> > out.txt` · `>> out.txt` | ghi ra file · ghi nối thêm |
| `<lệnh> \| tee out.txt` | vừa hiện màn hình vừa ghi file |
| `history \| grep <chữ>` | tìm lại lệnh đã gõ |
| `Tab` · `Ctrl+C` · `Ctrl+R` | tự hoàn thành · dừng lệnh · tìm lệnh cũ |

> `Tab` là phím quan trọng nhất trong terminal. Gõ vài chữ rồi bấm `Tab` để máy tự điền tên
> file — vừa nhanh vừa tránh gõ sai tên.

### VS Code nối vào WSL

Cài **VS Code** trên Windows, rồi cài extension **WSL** (`ms-vscode-remote.remote-wsl`).

Mở dự án từ terminal Ubuntu:

```bash
$ cd ~/projects
$ code .
```

Lần đầu VS Code tự cài phần máy chủ vào WSL, mất 1–2 phút. **Phải thấy gì:** góc trái dưới cửa sổ
VS Code hiện `WSL: Ubuntu` màu xanh. Nếu không có, em đang sửa file bằng VS Code phía Windows —
extension và terminal sẽ không khớp.

Ba extension nên cài thêm: **Python**, **Verilog-HDL/SystemVerilog**, **Markdown All in One**.

---

## A2. Git và GitHub

Git là thứ biến "em đã làm suốt tuần" thành **bằng chứng kiểm chứng được**. Ở chương trình này,
lịch sử commit là một phần hồ sơ đánh giá: nó cho thấy em làm đều hay dồn vào ba ngày cuối, và cho
phép quay lại đúng phiên bản đã tạo ra một kết quả.

### Cấu hình lần đầu

```bash
$ git config --global user.name "Nguyễn Văn A"
$ git config --global user.email "a.nguyenvan@st.phenikaa-uni.edu.vn"
$ git config --global init.defaultBranch main
$ git config --global core.editor "nano"
```

Dùng **email trường**, đúng email đã đăng ký tài khoản GitHub — nếu lệch, commit của em sẽ không
gắn với tài khoản và hội đồng không thấy đó là công của em.

### Nối máy với GitHub bằng SSH

Cách này không phải nhập mật khẩu mỗi lần push.

```bash
$ ssh-keygen -t ed25519 -C "a.nguyenvan@st.phenikaa-uni.edu.vn"
```

Bấm `Enter` ba lần (chấp nhận đường dẫn mặc định, để trống passphrase). Rồi lấy khóa công khai:

```bash
$ cat ~/.ssh/id_ed25519.pub
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAA... a.nguyenvan@st.phenikaa-uni.edu.vn
```

Chép **toàn bộ dòng đó**, lên GitHub → ảnh đại diện → **Settings** → **SSH and GPG keys** →
**New SSH key** → dán vào → **Add SSH key**.

Kiểm tra:

```bash
$ ssh -T git@github.com
Hi <tên-tài-khoản>! You've successfully authenticated, but GitHub does not provide shell access.
```

Câu *"does not provide shell access"* là **đúng**, không phải lỗi.

### Bảy lệnh Git dùng hằng ngày

```bash
$ git status                     # đang có gì thay đổi — gõ trước mọi thứ khác
$ git add <file>                 # chọn file đưa vào lần lưu này
$ git add -A                     # chọn tất cả
$ git commit -m "thông điệp"     # chốt một lần lưu
$ git log --oneline -10          # xem 10 lần lưu gần nhất
$ git push                       # đẩy lên GitHub
$ git pull                       # kéo về thay đổi từ GitHub
```

### Viết thông điệp commit thế nào

Thông điệp phải trả lời **"vì sao"**, không phải "cái gì" — cái gì thì `git diff` đã nói rồi.

| Tệ | Được |
|---|---|
| `update` | `Sửa FIFO đầy sai một chu kỳ do so sánh con trỏ thiếu bit wrap` |
| `fix bug` | `Đổi seed cố định cho mô phỏng để chạy lại ra cùng kết quả` |
| `add file` | `Thêm testbench kiểm trường hợp reset giữa lúc đang ghi` |

**Nhịp làm việc:** commit **nhỏ và thường xuyên** — mỗi khi một việc nhỏ chạy được. Đừng để một
commit khổng lồ cuối tuần: nó vô dụng khi cần tìm chỗ hỏng.

### `.gitignore` — cái gì tuyệt đối không đưa lên

Tạo file `.gitignore` ở gốc repo:

```gitignore
# Môi trường Python
venv/
__pycache__/
*.pyc

# Kết quả nặng và file tạm của công cụ
results/raw/**/*.bin
*.vcd
*.log
db/
incremental_db/
output_files/
simulation/
.pio/

# Hệ điều hành
.DS_Store
Thumbs.db

# TUYỆT ĐỐI không đưa lên
*.key
secrets.*
diem_*.xlsx
```

Ba thứ **không bao giờ** commit:

1. **Dữ liệu cá nhân** — họ tên, mã số sinh viên, điểm, nhận xét của người khác.
2. **File nhị phân khổng lồ** — bitstream, waveform hàng trăm MB, dataset thô. Repo phình lên là
   không gỡ lại được.
3. **Mật khẩu, khóa, token** — kể cả trong file cấu hình, kể cả "để tạm rồi xóa sau". Git nhớ mãi.

### Dựng repo đề tài từ bộ khởi tạo

1. Lên GitHub → **New repository** → tên dạng `datn-<mã-đề-tài>`, ví dụ `datn-a4-t01`.
   Chọn **Private**. **Không** tick *Add a README*.
2. Chép bộ khởi tạo từ kho chương trình:
   [`04_Project_Template/student_repo_starter/`](../04_Project_Template/student_repo_starter/README.md)
3. Đẩy lên:

```bash
$ cd ~/projects/datn-a4-t01
$ git init
$ git add -A
$ git commit -m "Khởi tạo repo đề tài từ bộ template của chương trình"
$ git remote add origin git@github.com:<tài-khoản>/datn-a4-t01.git
$ git push -u origin main
```

4. **Settings** → **Collaborators** → mời mentor. Không mời thì mentor không xem được, và tuần
   nào cũng phải hỏi lại.

---

## A3. Python có kiểm soát

Mọi nhánh đều cần Python: nhánh B để mô phỏng, các nhánh khác để xử lý số liệu và vẽ hình.

### Vì sao phải dùng môi trường ảo

Cài thư viện thẳng vào hệ thống thì sáu tháng sau, khi thư viện lên phiên bản mới, code của em
**chạy ra kết quả khác** mà không ai biết vì sao. Môi trường ảo (`venv`) khóa phiên bản lại trong
thư mục dự án.

```bash
$ cd ~/projects/datn-a4-t01
$ python3 -m venv venv
$ source venv/bin/activate
```

**Phải thấy gì:** dấu nhắc có thêm `(venv)` ở đầu:

```text
(venv) nam@DESKTOP:~/projects/datn-a4-t01$
```

Mỗi lần mở terminal mới phải chạy lại `source venv/bin/activate`. Quên bước này là nguyên nhân
của phần lớn lỗi *"ModuleNotFoundError"*.

### Cài thư viện và khóa phiên bản

```bash
(venv) $ pip install numpy scipy matplotlib pandas jupyter
(venv) $ pip freeze > requirements.txt
```

`requirements.txt` phải được **commit**. Nó là thứ cho phép người khác — và chính em sáu tháng sau —
dựng lại đúng môi trường:

```bash
(venv) $ pip install -r requirements.txt
```

**Phải thấy gì**

```bash
(venv) $ python3 -c "import numpy, matplotlib; print(numpy.__version__)"
2.1.3
```

---

## A4. Cấu trúc repo và README

Dùng chung một cấu trúc cho mọi đề tài. Xóa thư mục nào không dùng, đừng để rỗng.

```text
datn-a4-t01/
├── README.md              ← người chấm đọc đầu tiên
├── docs/                  ← ghi chú kỹ thuật, báo cáo tuần
├── references/            ← tài liệu đã đọc, bảng so sánh
├── src/                   ← mã nguồn phần mềm
├── rtl/                   ← mã RTL (nhánh A1–A5, B)
├── firmware/              ← mã nhúng (nhánh A6, A7)
├── pcb/                   ← thiết kế mạch (nhánh A0)
├── tb/                    ← testbench
├── scripts/               ← script chạy thí nghiệm và vẽ hình
├── configs/               ← cấu hình có đặt tên, có phiên bản
├── tests/                 ← unit test
├── results/
│   ├── raw/               ← kết quả thô — KHÔNG BAO GIỜ ghi đè, không sửa tay
│   └── processed/         ← kết quả đã xử lý, sinh từ raw bằng script
├── figures/               ← hình sinh từ script, không vẽ tay
├── weekly/                ← báo cáo tuần
├── requirements.txt
└── .gitignore
```

Chi tiết và checklist: [`04_Project_Template/REPRODUCIBILITY_STANDARD.md`](../04_Project_Template/REPRODUCIBILITY_STANDARD.md).

**README viết dần từ tuần 1**, không phải tuần cuối. Tối thiểu phải có: bài toán trong 3 câu ·
cách chạy lại (lệnh cụ thể, phiên bản công cụ) · kết quả chính · trạng thái hiện tại.

---

## A5. Kỷ luật thí nghiệm — phần quan trọng nhất của Phần A

Ở chương trình này, **một kết quả không truy ngược được về script và commit thì coi như không có**.
Đây không phải sự khắt khe hình thức: một con số không tái tạo được thì không dùng để kết luận
bất cứ điều gì.

### Bốn quy tắc

1. **Không ghi đè `results/raw/`.** Chạy lại thì tạo thư mục mới có ngày giờ.
2. **Không sửa số liệu bằng tay** trong Excel hay trong hình.
3. **Mọi hình phải có script sinh ra nó.** Hình không tái tạo được, ở Gate 5 tính là không có bằng chứng.
4. **Mỗi lần chạy phải ghi lại**: ngày giờ · git commit · config · seed · phiên bản công cụ ·
   nền tảng · đường dẫn kết quả thô.

### Bài thực hành — một script đúng chuẩn

Tạo `scripts/demo_experiment.py`:

```python
# -*- coding: utf-8 -*-
"""Ví dụ tối thiểu một thí nghiệm ĐÚNG CHUẨN: có seed, có log, hình sinh từ dữ liệu."""
import json, pathlib, subprocess, datetime
import numpy as np
import matplotlib
matplotlib.use("Agg")          # vẽ không cần màn hình
import matplotlib.pyplot as plt

SEED = 12345                    # cố định để chạy lại ra đúng kết quả
rng = np.random.default_rng(SEED)

stamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
out = pathlib.Path("results/raw") / stamp
out.mkdir(parents=True, exist_ok=True)

# --- thí nghiệm: đo trung bình mẫu hội tụ thế nào theo số mẫu ---
ns = np.array([10, 30, 100, 300, 1000, 3000, 10000])
err = np.array([abs(rng.normal(0, 1, n).mean()) for n in ns])
np.savetxt(out / "raw.csv", np.c_[ns, err], delimiter=",", header="n,abs_error")

# --- siêu dữ liệu: thiếu cái này thì kết quả vô giá trị ---
commit = subprocess.run(["git", "rev-parse", "--short", "HEAD"],
                        capture_output=True, text=True).stdout.strip() or "chưa-commit"
(out / "meta.json").write_text(json.dumps({
    "experiment_id": stamp,
    "seed": SEED,
    "git_commit": commit,
    "numpy": np.__version__,
    "mo_ta": "Sai số trung bình mẫu giảm theo 1/sqrt(n)",
}, ensure_ascii=False, indent=1), encoding="utf-8")

# --- hình sinh từ chính dữ liệu vừa lưu ---
plt.figure(figsize=(5, 3.4))
plt.loglog(ns, err, "o-", label="đo được")
plt.loglog(ns, 1 / np.sqrt(ns), "--", label=r"$1/\sqrt{n}$")
plt.xlabel("số mẫu n"); plt.ylabel("|sai số|"); plt.legend(); plt.grid(True, which="both", alpha=.3)
plt.tight_layout()
pathlib.Path("figures").mkdir(exist_ok=True)
plt.savefig(f"figures/convergence-{stamp}.png", dpi=150)
print("XONG →", out)
```

Chạy:

```bash
(venv) $ python3 scripts/demo_experiment.py
XONG → results/raw/20260910-143022
```

**Phải thấy gì:** một thư mục `results/raw/<ngày-giờ>/` chứa `raw.csv` và `meta.json`, cộng một
file hình trong `figures/`.

**Thử phép kiểm tái lập:** chạy lại lần nữa. `raw.csv` của hai lần chạy phải **giống hệt nhau** —
vì seed cố định. Nếu khác, em đang có nguồn ngẫu nhiên chưa kiểm soát; tìm cho ra trước khi làm tiếp.

Mẫu ghi chép đầy đủ: [`04_Project_Template/EXPERIMENT_LOG_TEMPLATE.md`](../04_Project_Template/EXPERIMENT_LOG_TEMPLATE.md).

---

## A6. Kiểm tra Phần A đã xong

Làm được cả sáu việc dưới đây thì chuyển sang phần nhánh.

- [ ] Mở Ubuntu, `cd ~/projects`, `ls -la` chạy được.
- [ ] `ssh -T git@github.com` trả lời `Hi <tên>!`.
- [ ] Đã có repo riêng trên GitHub, mentor là collaborator, có ít nhất 3 commit.
- [ ] `source venv/bin/activate` rồi `python3 -c "import numpy"` không lỗi.
- [ ] Chạy `scripts/demo_experiment.py`, có `results/raw/<ngày-giờ>/` và một hình.
- [ ] Chạy lại lần hai ra **đúng** `raw.csv` như lần đầu.

---

# Phần B · Điện tử thực hành và PCB (nhánh `A0`)

## B1. Công cụ

**KiCad** — miễn phí, mã nguồn mở, đủ dùng cho mọi đề tài `A0`. Cài **trên Windows**, không cài trong WSL.

Tải tại [kicad.org/download](https://www.kicad.org/download/) → bản Windows → cài mặc định.
Chọn cài kèm thư viện linh kiện và 3D models.

Repo đặt ở `C:\Users\<tên>\projects\datn-a0-p01\`, thư mục `pcb/` chứa file KiCad.

## B2. Quy trình bảy bước

| Bước | Việc | Sản phẩm |
|---|---|---|
| 1 | Vẽ sơ đồ nguyên lý (Schematic Editor) | `.kicad_sch` |
| 2 | Gán chân thực tế cho từng linh kiện (Footprint Assignment) | bảng gán chân |
| 3 | Kiểm lỗi điện (ERC) | **0 lỗi** trước khi đi tiếp |
| 4 | Vẽ mạch in (PCB Editor) | `.kicad_pcb` |
| 5 | Kiểm lỗi thiết kế (DRC) | **0 lỗi** |
| 6 | Xuất file gia công (Gerber + Drill) + BOM | thư mục `fab/` |
| 7 | Gia công, hàn, đo | board thật + số liệu đo |

> **Luật cứng:** ERC và DRC còn lỗi thì **không gửi đi gia công**. Một board hỏng vì bỏ qua bước
> kiểm mất hai tuần chờ làm lại.

## B3. Bốn nguyên tắc thiết kế người mới hay sai

1. **Đường hồi dòng.** Dòng điện luôn chạy thành vòng kín. Vẽ được đường đi thì phải vẽ được
   đường về — thường là mặt đất (ground plane). Thiếu suy nghĩ này là nguồn của phần lớn nhiễu.
2. **Tụ lọc (decoupling).** Mỗi chân nguồn của mỗi IC cần một tụ 100nF **đặt sát chân**, không phải
   ở góc board.
3. **Độ rộng đường mạch theo dòng.** Đường tín hiệu 0.25mm là đủ; đường nguồn phải rộng hơn.
   Dùng bảng tra độ rộng theo dòng, đừng ước lượng.
4. **Điểm đo (test point).** Bố trí sẵn điểm đo cho các nút quan trọng **trước khi** gia công.
   Không có điểm đo thì lúc board hỏng không biết dò ở đâu.

## B4. An toàn phòng lab

- Kính bảo hộ khi hàn và khi cắt chân linh kiện.
- Mỏ hàn **luôn** để về giá, không đặt trên bàn.
- Hút khói khi hàn; chì và nhựa thông độc.
- **Trước khi cấp nguồn lần đầu**: đo thông mạch, kiểm chập nguồn–đất, kiểm chiều tụ hóa và diode.
- Nguồn giới hạn dòng (current limit) đặt thấp cho lần bật đầu tiên.

## B5. Năm phép đo phải làm được

| Phép đo | Dụng cụ | Ghi lại gì |
|---|---|---|
| Thông mạch / chập | đồng hồ số, thang bíp | ảnh chụp hoặc bảng kết quả |
| Điện áp DC ở các nút | đồng hồ số | giá trị + điều kiện tải |
| Độ gợn (ripple) của nguồn | oscilloscope, ghép AC | ảnh sóng + Vpp + thang đo |
| Dạng sóng số, thời gian sườn | oscilloscope | ảnh sóng + tần số + thang đo |
| Chuỗi bit giao thức (I2C/SPI/UART) | logic analyzer | ảnh giải mã + tốc độ |

> **Ảnh chụp màn hình máy đo bắt buộc kèm điều kiện đo**: thang thời gian, thang điện áp, đầu dò
> ×1 hay ×10, tải là gì. Ảnh không có điều kiện đo thì ở Gate 5 không tính là bằng chứng.

---

# Phần C · RTL → FPGA → ASIC (nhánh `A1`–`A5`)

Nhánh này có **hai môi trường song song**: mô phỏng và tổng hợp mã nguồn mở chạy **trong WSL**;
nạp lên board chạy bằng **Quartus trên Windows**.

## C1. Bộ công cụ mô phỏng trong WSL

```bash
$ sudo apt install -y iverilog gtkwave verilator
$ pip install cocotb pytest        # trong venv của dự án
```

**Phải thấy gì**

```bash
$ iverilog -V | head -1
Icarus Verilog version 12.0
$ verilator --version
Verilator 5.020 ...
```

## C2. Bài lab 1 — mô phỏng và xem dạng sóng

Tạo `rtl/mux2.v`:

```verilog
module mux2 (input wire a, b, sel, output wire y);
    assign y = sel ? b : a;
endmodule
```

Tạo `tb/tb_mux2.v`:

```verilog
`timescale 1ns/1ps
module tb_mux2;
    reg a, b, sel; wire y;
    mux2 dut (.a(a), .b(b), .sel(sel), .y(y));

    task check(input exp);
        begin
            #1;
            if (y !== exp) begin
                $display("SAI: a=%b b=%b sel=%b -> y=%b, mong đợi %b", a, b, sel, y, exp);
                $fatal;
            end
        end
    endtask

    initial begin
        $dumpfile("tb_mux2.vcd");
        $dumpvars(0, tb_mux2);
        a=0; b=1; sel=0; check(0);
        sel=1;           check(1);
        a=1; b=0; sel=0; check(1);
        sel=1;           check(0);
        $display("TAT CA TRUONG HOP DUNG");
        $finish;
    end
endmodule
```

Chạy:

```bash
$ iverilog -o sim.out rtl/mux2.v tb/tb_mux2.v
$ vvp sim.out
```

**Phải thấy gì**

```text
VCD info: dumpfile tb_mux2.vcd opened for output.
TAT CA TRUONG HOP DUNG
```

Xem dạng sóng:

```bash
$ gtkwave tb_mux2.vcd
```

Cửa sổ GTKWave mở ra (WSL2 trên Windows 11 hiện được giao diện đồ họa sẵn). Kéo tín hiệu từ cột
trái vào vùng sóng để xem.

> **Testbench phải tự kiểm.** Testbench chỉ in ra sóng rồi để người nhìn bằng mắt là testbench
> kém: nó không bắt được lỗi khi em sửa code tuần sau. Luôn có `check()` và `$fatal` như trên.

## C3. Quartus và board Intel/Altera

Lab dùng board Intel/Altera nên phần mềm là **Quartus Prime Lite Edition** — miễn phí, không cần license.

**Cài trên Windows** (không cài trong WSL):

1. Tải tại [intel.com/content/www/us/en/software-kit/…quartus-prime-lite](https://www.intel.com/content/www/us/en/products/details/fpga/development-tools/quartus-prime/resource.html)
   → chọn **Lite Edition**.
2. Khi cài, **bắt buộc tick đúng dòng device** của board trong lab: `MAX 10` cho DE10-Lite,
   `Cyclone IV/V` cho DE2/DE1-SoC. Không tick thì tổng hợp sẽ báo không có device.
3. Cài kèm **USB-Blaster driver**. Nếu Windows không nhận board: Device Manager → thiết bị có dấu
   chấm than → *Update driver* → trỏ tới `C:\intelFPGA_lite\<phiên-bản>\quartus\drivers\usb-blaster`.

**Phải thấy gì:** cắm board, mở Quartus → *Tools* → *Programmer* → *Hardware Setup* thấy
`USB-Blaster [USB-0]`.

## C4. Bài lab 2 — nạp lên board

1. Quartus → *File* → *New Project Wizard*. Thư mục dự án đặt trong repo ở Windows:
   `C:\Users\<tên>\projects\datn-a3-p01\fpga\`.
2. Chọn đúng device (tra trên nhãn chip của board, ví dụ `10M50DAF484C7G` cho DE10-Lite).
3. Thêm file `.v`, đặt module đỉnh làm *top-level entity*.
4. Gán chân: *Assignments* → *Pin Planner*. **Lấy tên chân từ file `.qsf` hoặc user manual của
   board**, đừng đoán — gán sai chân có thể làm hỏng board.
5. *Processing* → *Start Compilation*.
6. *Tools* → *Programmer* → *Add File* chọn `.sof` → *Start*.

**Ba con số phải ghi lại sau mỗi lần tổng hợp** — đây là bằng chứng của Gate 3:

| Số liệu | Lấy ở đâu trong Quartus |
|---|---|
| Tài nguyên (LE/ALM, FF, block RAM, DSP) | *Compilation Report* → *Fitter* → *Resource Usage Summary* |
| Fmax | *Timing Analyzer* → *Reports* → *Fmax Summary* |
| Slack có âm không | *Timing Analyzer* → *Setup Summary* |

> **Slack âm nghĩa là mạch không chạy đúng ở tần số đó**, dù board vẫn nhấp nháy đèn. Đừng báo
> cáo Fmax mà bỏ qua slack.

## C5. Dòng chảy ASIC mã nguồn mở (nhánh `A4`, `A5`)

Phần này chỉ chạy trong WSL. Cách cài ổn định nhất là dùng **Docker**, tránh vật lộn với phụ thuộc.

```bash
$ sudo apt install -y docker.io
$ sudo usermod -aG docker $USER
```

Đóng và mở lại terminal Ubuntu để nhóm `docker` có hiệu lực.

Thử Yosys — công cụ tổng hợp RTL:

```bash
$ sudo apt install -y yosys
$ yosys -V
Yosys 0.33 ...
```

Tổng hợp thử module ở §C2:

```bash
$ yosys -p "read_verilog rtl/mux2.v; synth; stat"
```

**Phải thấy gì:** một bảng `=== mux2 ===` liệt kê số cell sau tổng hợp.

Dòng chảy đầy đủ RTL → GDSII dùng **OpenROAD** hoặc **LibreLane** với thư viện **SkyWater SKY130**.
Đây là phần nặng nhất của nhánh này; làm theo hướng dẫn *getting started* chính thức của công cụ và
**chạy được ví dụ mẫu của họ trước** khi đụng tới đề tài của mình. Tài liệu nền:
[`09_References/READING-LIST.md`](../09_References/READING-LIST.md) §2.

---

# Phần D · Nhúng và IoT với ESP8266 (nhánh `A6`, `A7`)

Lab dùng **ESP8266** (NodeMCU v3 hoặc Wemos D1 mini). Việc nạp chương trình qua USB nên
làm **hoàn toàn ở phía Windows** — đưa cổng USB vào WSL được nhưng thêm rắc rối không đáng.

## D1. Cài PlatformIO

1. Mở **VS Code phía Windows** (không phải cửa sổ `WSL: Ubuntu`).
2. Cài extension **PlatformIO IDE**. Lần đầu mất 3–5 phút để tải bộ công cụ.
3. Cài **driver USB-UART**: NodeMCU v3 thường dùng chip **CH340**, Wemos D1 mini dùng **CH340**
   hoặc **CP2102**. Tải driver theo đúng chip, cài, cắm board.

**Phải thấy gì:** Device Manager → *Ports (COM & LPT)* xuất hiện `USB-SERIAL CH340 (COM5)`.
Nhớ số COM đó.

## D2. Dự án đầu tiên

PlatformIO → *New Project*:

- **Board**: `NodeMCU 1.0 (ESP-12E Module)` — hoặc `WEMOS D1 R2 & mini`
- **Framework**: `Arduino`
- **Location**: `C:\Users\<tên>\projects\datn-a6-p01\firmware\`

File `platformio.ini` sinh ra, sửa thành:

```ini
[env:nodemcuv2]
platform = espressif8266
board = nodemcuv2
framework = arduino
monitor_speed = 115200
lib_deps =
    knolleary/PubSubClient@^2.8
```

`src/main.cpp`:

```cpp
#include <Arduino.h>

const int LED = LED_BUILTIN;

void setup() {
  Serial.begin(115200);
  pinMode(LED, OUTPUT);
  Serial.println("\nESP8266 san sang");
}

void loop() {
  digitalWrite(LED, LOW);   // ESP8266: LOW là SÁNG
  delay(500);
  digitalWrite(LED, HIGH);
  delay(500);
  Serial.printf("uptime=%lu ms  heap=%u byte\n", millis(), ESP.getFreeHeap());
}
```

Nạp và xem log: bấm **PlatformIO: Upload** (mũi tên →) rồi **Serial Monitor** (phích cắm).

**Phải thấy gì**

```text
ESP8266 san sang
uptime=1004 ms  heap=48120 byte
```

Nạp không được? Xem §F4.

## D3. Ba giới hạn thật của ESP8266 — biết trước để chọn đề tài đúng

| Giới hạn | Con số | Ảnh hưởng |
|---|---|---|
| RAM khả dụng | ~40–50 KB heap | Không đủ cho mô hình học máy cỡ vừa |
| Chỉ một lõi, không có FPU | 80/160 MHz | Tính toán dấu phẩy động rất chậm |
| Một ADC 10-bit, dải 0–1V | 1 kênh | Đo nhiều cảm biến analog phải thêm mạch ngoài |

> **Với đề tài TinyML (`A7-P03`, `A7-T02`), ESP8266 không đủ.** TensorFlow Lite Micro cần
> RAM và tập lệnh mà ESP8266 không có. Hai lựa chọn: đổi sang **ESP32** (có FPU, RAM lớn hơn
> nhiều, được TFLite Micro hỗ trợ chính thức), hoặc thu hẹp đề tài về mức phân loại bằng ngưỡng
> và đặc trưng thủ công. **Bàn với mentor ở tuần 1**, đừng để tới tuần 8 mới phát hiện.

## D4. Bài lab — cảm biến, MQTT, đo năng lượng

**Bước 1 — đọc cảm biến.** Nối cảm biến (DHT22, BMP280…) theo sơ đồ, đọc và in ra Serial mỗi 2 giây.

**Bước 2 — dựng MQTT broker trong WSL:**

```bash
$ sudo apt install -y mosquitto mosquitto-clients
$ sudo service mosquitto start
$ hostname -I          # lấy địa chỉ IP của WSL, ví dụ 172.24.31.5
```

Lắng nghe:

```bash
$ mosquitto_sub -h localhost -t "lab/#" -v
```

**Bước 3 — ESP8266 gửi dữ liệu lên broker.** Trong code, `mqtt_server` đặt bằng IP vừa lấy. Board
và máy tính phải cùng mạng Wi-Fi.

**Phải thấy gì:** cửa sổ `mosquitto_sub` in ra dòng mới mỗi 2 giây:

```text
lab/node01/temp 27.4
lab/node01/humi 71.2
```

> **WSL đổi IP mỗi lần khởi động lại.** Kết nối hôm nay chạy, mai không chạy thì chạy lại
> `hostname -I` và cập nhật. Đây là hiện tượng bình thường, không phải hỏng code.

**Bước 4 — đo năng lượng** (đề tài `A7-P02`). Đo dòng tiêu thụ ở ba trạng thái: hoạt động ·
Wi-Fi phát · deep sleep. Ghi kèm điện áp cấp và điều kiện đo. Đây là bằng chứng cốt lõi của
nhánh IoT chạy pin.

---

# Phần E · Mô phỏng Polar (nhánh `B0`–`B6`)

Nhánh này chạy hoàn toàn trong WSL, chỉ cần Python.

## E1. Môi trường

```bash
$ cd ~/projects/datn-b2-t01
$ python3 -m venv venv && source venv/bin/activate
(venv) $ pip install numpy scipy matplotlib pandas numba jupyter
(venv) $ pip freeze > requirements.txt
```

`numba` là tùy chọn nhưng đáng cài: nó biên dịch vòng lặp Python nóng thành mã máy, giúp mô phỏng
số lượng frame lớn nhanh hơn hàng chục lần.

## E2. Kiến trúc bộ mô phỏng

Mọi đề tài nhánh B đều dựng cùng một chuỗi. Tách thành các hàm riêng ngay từ đầu, đừng viết một
file khổng lồ:

```text
bit thông tin  →  chèn bit đóng băng  →  mã hóa Polar  →  điều chế BPSK
                                                              ↓
        đếm lỗi  ←  giải mã SC  ←  tính LLR  ←  cộng nhiễu AWGN
```

| Thành phần | File gợi ý | Kiểm bằng cách nào |
|---|---|---|
| Xây tập bit đóng băng | `src/construction.py` | so với bảng trong tài liệu gốc |
| Mã hóa | `src/encoder.py` | mã hóa rồi giải mã kênh sạch phải ra đúng bit gốc |
| Kênh AWGN + LLR | `src/channel.py` | phương sai nhiễu đo được khớp giá trị đặt |
| Giải mã SC | `src/sc_decoder.py` | **kiểm tay với N=4 hoặc N=8** |
| Vòng mô phỏng | `scripts/run_ber.py` | đường BLER khớp tài liệu |

## E3. Ba phép kiểm bắt buộc trước khi tin vào đường cong

1. **Kênh không nhiễu.** Đặt SNR rất cao: BLER phải bằng **đúng 0**. Không bằng 0 nghĩa là
   encoder hoặc decoder sai, không phải "nhiễu còn cao".
2. **Kiểm tay N nhỏ.** Với `N=4`, `K=2`, tự tính bằng giấy rồi so với chương trình. Đây là phép
   kiểm rẻ nhất và bắt được nhiều lỗi nhất.
3. **So với tài liệu.** Chọn một cấu hình đã công bố (ví dụ `N=1024, R=0.5`, AWGN) và đối chiếu
   đường BLER. Lệch thì phải giải thích được vì sao, đừng bỏ qua.

## E4. Cần bao nhiêu frame — chỗ sinh viên hay làm sai

Muốn đo BLER tới mức `1e-4` một cách tin cậy, cần thu được **ít nhất 100 khung lỗi** ở mỗi điểm SNR,
tức khoảng **10⁶ khung**. Chạy 1000 khung rồi vẽ ra đường cong ở vùng `1e-4` là **vô nghĩa** —
con số đó chỉ là nhiễu thống kê.

```python
TARGET_ERRORS = 100          # dừng khi đủ số khung lỗi
MAX_FRAMES    = 10_000_000   # trần an toàn, tránh chạy vô hạn
```

Ghi lại **số khung thực chạy** và **số lỗi thu được** ở mỗi điểm — thiếu hai con số này thì
đường cong không kiểm chứng được.

## E5. Bài lab — dựng lại một đường BLER

Mục tiêu: vẽ BLER theo Eb/N0 cho SC decoder, `N=1024`, `K=512`, Eb/N0 từ 1.0 đến 3.0 dB.

Yêu cầu bắt buộc: seed cố định · lưu `results/raw/<ngày-giờ>/` gồm `raw.csv` và `meta.json` ·
hình sinh bằng script từ chính `raw.csv` · ghi số khung và số lỗi mỗi điểm.

Xong bài này là em đã có **baseline** — thứ mà Gate 2 đòi hỏi, và là nền để so sánh cho mọi cải
tiến về sau.

---

# Phần F · Sự cố thường gặp

## F1. WSL không cài được

### F1a · `wsl : The term 'wsl' is not recognized...`

Lỗi này **không phải** do gõ sai lệnh. Nó nghĩa là cửa sổ PowerShell đang mở không nhìn thấy
`wsl.exe`. Chạy khối chẩn đoán sau để biết vì sao:

```powershell
PS> "PowerShell 64-bit? " + [Environment]::Is64BitProcess
PS> "Windows build    : " + [System.Environment]::OSVersion.Version.Build
PS> "System32\wsl.exe : " + (Test-Path C:\Windows\System32\wsl.exe)
PS> "Sysnative\wsl.exe: " + (Test-Path C:\Windows\Sysnative\wsl.exe)
```

| Kết quả | Nguyên nhân | Cách sửa |
|---|---|---|
| `64-bit? False` (và `Sysnative` là `True`) | Đang mở **PowerShell (x86)** — bản 32-bit | Đóng đi, mở **Windows PowerShell** (không có chữ x86), chạy lại |
| `build` **< 19041** | Windows quá cũ, chưa có lệnh `wsl --install` | Xem F1b |
| 64-bit `True`, build ≥ 19041, `System32\wsl.exe` là `False` | Tính năng WSL chưa bật | Xem F1c |

### F1b · Windows build < 19041

Bật hai tính năng, khởi động lại, cài nhân WSL2 rồi lấy Ubuntu từ Store:

```powershell
PS> dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
PS> dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
```

Khởi động lại → tải và cài **WSL2 Linux kernel update** từ trang Microsoft → rồi:

```powershell
PS> wsl --set-default-version 2
```

Cuối cùng mở **Microsoft Store**, tìm **Ubuntu**, bấm *Get*.

> Nếu được, hãy cập nhật Windows lên bản mới rồi làm theo F1c. Build cũ sẽ còn gây rắc rối ở
> nhiều chỗ khác, không riêng WSL.

### F1c · Bật tính năng WSL

```powershell
PS> dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
PS> dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
```

Khởi động lại, rồi chạy lại `wsl --install -d Ubuntu`.

### F1d · Báo cần virtualization

Máy báo *"WSL requires virtualization"* hoặc *"Please enable the Virtual Machine Platform"*:
khởi động lại vào BIOS/UEFI (thường bấm `F2`, `Del` hoặc `F10` lúc vừa bật máy), bật
**Intel VT-x** / **AMD-V** / **SVM Mode**, lưu và thoát. Rồi làm lại F1c.

## F2. `git push` báo `Permission denied (publickey)`

```bash
$ ssh -T git@github.com
```

Nếu không ra `Hi <tên>!` thì khóa SSH chưa được thêm đúng. Kiểm ba điều: khóa đã dán **đầy đủ**
lên GitHub chưa · dán đúng mục *SSH keys* (không phải *GPG keys*) · địa chỉ remote có dạng
`git@github.com:...` chứ không phải `https://...`:

```bash
$ git remote -v
$ git remote set-url origin git@github.com:<tài-khoản>/<repo>.git
```

## F3. `ModuleNotFoundError` dù vừa `pip install`

Gần như chắc chắn là quên kích hoạt môi trường ảo. Nhìn dấu nhắc có `(venv)` không:

```bash
$ source venv/bin/activate
```

Nếu vẫn lỗi, kiểm xem đang dùng đúng Python nào:

```bash
(venv) $ which python3
/home/nam/projects/datn-a4-t01/venv/bin/python3     # phải trỏ vào venv
```

## F4. ESP8266 nạp không được

| Triệu chứng | Cách xử lý |
|---|---|
| Không thấy cổng COM | Chưa cài driver CH340/CP2102, hoặc dùng cáp **chỉ để sạc** — đổi cáp có dây dữ liệu |
| `Failed to connect ... Timed out waiting for packet header` | Giữ nút **FLASH** khi bắt đầu nạp; nhấn **RST** một lần rồi thả FLASH |
| Nạp xong Serial Monitor toàn ký tự rác | Sai tốc độ — đặt `monitor_speed = 115200` cho khớp `Serial.begin(115200)` |
| Board khởi động lại liên tục | Nguồn USB yếu — dùng cổng USB khác hoặc cấp nguồn ngoài 5V |

## F5. Quartus không thấy USB-Blaster

Device Manager → thiết bị có dấu chấm than → *Update driver* → *Browse my computer* → trỏ tới
`C:\intelFPGA_lite\<phiên-bản>\quartus\drivers\usb-blaster`. Cắm thẳng vào máy, không qua hub USB.

## F6. Build trong WSL chậm bất thường

Kiểm xem có đang đứng trong `/mnt/c/` không:

```bash
$ pwd
/mnt/c/Users/admin/projects/...     # ← đây là nguyên nhân
```

Chuyển repo về `~/projects/` (xem bảng ở §A1). Với nhánh bắt buộc để repo ở Windows (`A3`, `A4`,
`A0`, `A6`, `A7`) thì chấp nhận, chỉ tránh chạy mô phỏng nặng ở đó.

## F7. GTKWave không mở được cửa sổ

Windows 11 hỗ trợ giao diện đồ họa WSL sẵn. Nếu không mở được, cập nhật WSL:

```powershell
PS> wsl --update
PS> wsl --shutdown
```

Vẫn không được thì mở file `.vcd` bằng **Surfer** hoặc GTKWave bản Windows.

---

# Phần G · Checklist nghiệm thu môi trường

Mang checklist này tới buổi gặp mentor. Mentor sẽ yêu cầu **chạy thử tại chỗ**, không chỉ xem ảnh chụp.

**Phần chung — mọi sinh viên**

- [ ] Mở Ubuntu và di chuyển thư mục bằng terminal.
- [ ] `ssh -T git@github.com` ra `Hi <tên>!`.
- [ ] Repo riêng trên GitHub, mentor là collaborator, ≥ 3 commit có thông điệp nói được **vì sao**.
- [ ] `.gitignore` có, và `git status` sạch sau khi build.
- [ ] `venv` hoạt động, `requirements.txt` đã commit.
- [ ] README có bài toán 3 câu và phần "chạy lại thế nào".
- [ ] Chạy `demo_experiment.py` hai lần ra **đúng cùng** một `raw.csv`.

**Theo nhánh**

- [ ] `A0` — KiCad mở được, dự án trống có ERC và DRC 0 lỗi; biết chụp ảnh đo kèm điều kiện đo.
- [ ] `A1`–`A5` — chạy `iverilog` + `vvp` ra `TAT CA TRUONG HOP DUNG`; mở được `.vcd`;
      Quartus tổng hợp xong và Programmer thấy USB-Blaster.
- [ ] `A6`, `A7` — nạp được chương trình nháy đèn; Serial Monitor in `heap`; `mosquitto_sub`
      nhận được bản tin từ board.
- [ ] `B0`–`B6` — kênh không nhiễu ra BLER = 0; kiểm tay `N=4` khớp; vẽ được một đường BLER
      từ `raw.csv` bằng script.

---

## Đọc tiếp

| Cần gì | Mở |
|---|---|
| Chọn đề tài | [trang Guide Notes](https://lucero6886.github.io/lucero-mentoring/guide.html) |
| Chương trình vận hành thế nào | [`10_Documentation/STUDENT-GUIDE.md`](STUDENT-GUIDE.md) |
| Chuẩn tổ chức repo và dữ liệu thô | [`04_Project_Template/REPRODUCIBILITY_STANDARD.md`](../04_Project_Template/REPRODUCIBILITY_STANDARD.md) |
| Mẫu ghi chép thí nghiệm | [`04_Project_Template/EXPERIMENT_LOG_TEMPLATE.md`](../04_Project_Template/EXPERIMENT_LOG_TEMPLATE.md) |
| Nên đọc tài liệu gì trước | [`09_References/READING-LIST.md`](../09_References/READING-LIST.md) |
| Làm việc trên GitHub với mentor | [`10_Documentation/GITHUB-WORKFLOW.md`](GITHUB-WORKFLOW.md) |

---

> **Kẹt quá hai giờ ở một bước cài đặt thì dừng lại và hỏi.** Hỏi bạn cùng nhóm và tài liệu chính
> thức trước; vẫn không xong thì mở Issue trong kho chương trình, ghi rõ: em làm bước nào, lệnh gì,
> máy báo **nguyên văn** gì. Ngồi một mình với lỗi cài đặt suốt ba ngày không phải là chăm chỉ —
> đó là mất ba ngày.
