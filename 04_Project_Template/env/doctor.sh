#!/usr/bin/env bash
# ---------------------------------------------------------------------------
# doctor.sh — kiểm tra môi trường làm việc đã sẵn sàng chưa.
#
# Engineering & Research Mentoring Program (Lucero)
# ThS. Đinh Văn Nam (Mr. Lucero Dinh) — Khoa Điện–Điện tử, ĐH Phenikaa
#
# Script này KHÔNG cài gì cả. Nó chỉ kiểm và báo cáo — nên chạy bao nhiêu lần
# cũng an toàn. Đây là thứ sinh viên nộp kèm báo cáo tuần 1 thay cho câu
# "em cài xong rồi ạ".
#
#   bash doctor.sh                 # kiểm phần chung
#   bash doctor.sh --rtl           # + nhánh A1-A3 (mô phỏng, FPGA)
#   bash doctor.sh --asic          # + nhánh A4-A5 (Nix, LibreLane)
#   bash doctor.sh --polar         # + nhánh B0-B6 (mô phỏng Polar)
#   bash doctor.sh --all           # tất cả
#
# Mã thoát: 0 = mọi mục đạt · 1 = còn mục chưa đạt.
# ---------------------------------------------------------------------------
set -uo pipefail

# Nhãn tiếng Việt có dấu là ký tự nhiều byte; printf '%-22s' đếm BYTE nên cột sẽ
# lệch. Ép locale UTF-8 rồi tự chèn khoảng trắng theo số KÝ TỰ (${#s}).
export LC_ALL="${LC_ALL:-C.UTF-8}" 2>/dev/null || true

WANT_RTL=0; WANT_ASIC=0; WANT_POLAR=0
for a in "$@"; do
  case "$a" in
    --rtl)   WANT_RTL=1 ;;
    --asic)  WANT_ASIC=1 ;;
    --polar) WANT_POLAR=1 ;;
    --all)   WANT_RTL=1; WANT_ASIC=1; WANT_POLAR=1 ;;
    -h|--help) sed -n '3,20p' "$0" | sed 's/^# \{0,1\}//'; exit 0 ;;
    *) echo "Tham số lạ: $a  (dùng --help)"; exit 2 ;;
  esac
done

if [ -t 1 ]; then G=$'\033[32m'; R=$'\033[31m'; Y=$'\033[33m'; D=$'\033[2m'; N=$'\033[0m'
else G=""; R=""; Y=""; D=""; N=""; fi

PASS=0; FAIL=0

section() { printf '\n%s%s%s\n' "$D" "$1" "$N"; }

# pad <chuỗi> — chèn khoảng trắng cho đủ 22 ký tự hiển thị
pad() { local s="$1" n=${#1}; printf '%s' "$s"
        while [ "$n" -lt 22 ]; do printf ' '; n=$((n+1)); done; }

# cut40 <chuỗi> — cắt bớt chuỗi phiên bản quá dài (curl in ra cả trang)
cut40() { local s="$1"; [ ${#s} -gt 40 ] && printf '%s…' "${s:0:39}" || printf '%s' "$s"; }

# ok <nhãn> <giá trị hiện có>
ok()   { PASS=$((PASS+1)); printf '  %s✔%s %s %s\n' "$G" "$N" "$(pad "$1")" "$(cut40 "${2:-}")"; }
# bad <nhãn> <vấn đề> <cách sửa>
bad()  { FAIL=$((FAIL+1)); printf '  %s✘%s %s %s\n' "$R" "$N" "$(pad "$1")" "$2"
         [ -n "${3:-}" ] && printf '      %s→ %s%s\n' "$Y" "$3" "$N"; return 0; }

# have <lệnh> <nhãn> <lệnh-lấy-version> <gợi-ý-sửa>
have() {
  if command -v "$1" >/dev/null 2>&1; then
    ok "$2" "$(eval "$3" 2>/dev/null | head -1)"
  else
    bad "$2" "chưa cài" "$4"
  fi
}

printf '%s\n' "════════════════════════════════════════════════════════════════"
printf 'KIỂM TRA MÔI TRƯỜNG · Mentoring Lucero\n'
printf '%sMáy: %s · %s%s\n' "$D" "$(hostname)" "$(date '+%d/%m/%Y %H:%M')" "$N"
printf '%s\n' "════════════════════════════════════════════════════════════════"

# ----------------------------------------------------------------- phần chung
section "PHẦN CHUNG — mọi sinh viên"

if grep -qiE 'microsoft|wsl' /proc/version 2>/dev/null; then
  ok "WSL2" "$(grep -oP '(?<=^PRETTY_NAME=").*(?=")' /etc/os-release 2>/dev/null || echo Linux)"
else
  ok "Linux" "$(grep -oP '(?<=^PRETTY_NAME=").*(?=")' /etc/os-release 2>/dev/null || uname -s)"
fi

have git    "git"     "git --version"            "sudo apt install -y git"
have python3 "python3" "python3 --version"       "sudo apt install -y python3 python3-venv"
have gcc    "build-essential" "gcc --version"    "sudo apt install -y build-essential"
have curl   "curl"    "curl --version"           "sudo apt install -y curl"

gn="$(git config --global user.name  2>/dev/null || true)"
ge="$(git config --global user.email 2>/dev/null || true)"
[ -n "$gn" ] && ok "git user.name"  "$gn" \
              || bad "git user.name"  "chưa đặt" 'git config --global user.name "Họ Tên"'
[ -n "$ge" ] && ok "git user.email" "$ge" \
              || bad "git user.email" "chưa đặt" 'git config --global user.email "ten@st.phenikaa-uni.edu.vn"'

if [ -f "$HOME/.ssh/id_ed25519.pub" ] || [ -f "$HOME/.ssh/id_rsa.pub" ]; then
  ok "khóa SSH" "đã có"
  if timeout 12 ssh -o StrictHostKeyChecking=accept-new -o BatchMode=yes \
       -T git@github.com 2>&1 | grep -q 'successfully authenticated'; then
    ok "GitHub nhận khóa" "xác thực được"
  else
    bad "GitHub nhận khóa" "chưa nhận hoặc không có mạng" \
        "dán nội dung ~/.ssh/id_ed25519.pub vào GitHub → Settings → SSH keys"
  fi
else
  bad "khóa SSH" "chưa tạo" 'ssh-keygen -t ed25519 -C "email của em"'
fi

# thư mục làm việc — chỉ cảnh báo, không tính là lỗi
if [ -d "$HOME/projects" ]; then ok "~/projects" "đã có"
else printf '  %s•%s %s %s\n' "$Y" "$N" "$(pad "~/projects")" "chưa có (mkdir -p ~/projects)"; fi

# ----------------------------------------------------------------- nhánh RTL
if [ "$WANT_RTL" = 1 ]; then
  section "NHÁNH A1–A3 — mô phỏng RTL và FPGA"
  have iverilog "iverilog" "iverilog -V"   "sudo apt install -y iverilog"
  have gtkwave  "gtkwave"  "gtkwave --version" "sudo apt install -y gtkwave"
  have verilator "verilator" "verilator --version" "sudo apt install -y verilator"
fi

# ----------------------------------------------------------------- nhánh ASIC
if [ "$WANT_ASIC" = 1 ]; then
  section "NHÁNH A4–A5 — Nix và LibreLane"
  have nix "nix" "nix --version" "xem SETUP-GUIDE §C6 bước 2"

  CACHE="nix-cache.fossi-foundation.org"
  if [ -r /etc/nix/nix.conf ] && grep -q "$CACHE" /etc/nix/nix.conf 2>/dev/null; then
    if grep -q "trusted-public-keys.*$CACHE" /etc/nix/nix.conf 2>/dev/null; then
      ok "bộ nhớ đệm FOSSi" "đã cấu hình đủ"
    else
      bad "bộ nhớ đệm FOSSi" "thiếu dòng trusted-public-keys" "xem SETUP-GUIDE §F8a"
    fi
  else
    bad "bộ nhớ đệm FOSSi" "chưa cấu hình — nix sẽ tự biên dịch hàng giờ" "xem SETUP-GUIDE §F8a"
  fi

  if [ -r /etc/nix/nix.conf ] && grep -qE 'experimental-features.*flakes' /etc/nix/nix.conf 2>/dev/null; then
    ok "nix flakes" "đã bật"
  else
    bad "nix flakes" "chưa bật" "thêm: extra-experimental-features = nix-command flakes"
  fi

  if [ -d "$HOME/projects/librelane/.git" ]; then
    ok "kho librelane" "$(git -C "$HOME/projects/librelane" rev-parse --short HEAD 2>/dev/null)"
  else
    bad "kho librelane" "chưa clone" "cd ~/projects && git clone https://github.com/librelane/librelane"
  fi

  # dung lượng trống — Nix store cần chỗ
  FREE_GB=$(df -BG --output=avail "$HOME" 2>/dev/null | tail -1 | tr -dc '0-9')
  if [ -n "$FREE_GB" ] && [ "$FREE_GB" -ge 20 ]; then
    ok "dung lượng trống" "${FREE_GB} GB"
  else
    bad "dung lượng trống" "${FREE_GB:-?} GB — nên có ≥ 20 GB" "xem SETUP-GUIDE §F8d"
  fi
fi

# ---------------------------------------------------------------- nhánh Polar
if [ "$WANT_POLAR" = 1 ]; then
  section "NHÁNH B0–B6 — mô phỏng Polar"
  for m in numpy scipy matplotlib; do
    if python3 -c "import $m" 2>/dev/null; then
      ok "python: $m" "$(python3 -c "import $m; print($m.__version__)" 2>/dev/null)"
    else
      bad "python: $m" "chưa cài" "source venv/bin/activate && pip install $m"
    fi
  done
  if [ -n "${VIRTUAL_ENV:-}" ]; then ok "môi trường ảo" "$(basename "$VIRTUAL_ENV")"
  else bad "môi trường ảo" "chưa kích hoạt" "source venv/bin/activate"; fi
fi

# ------------------------------------------------------------------- kết luận
printf '\n%s\n' "────────────────────────────────────────────────────────────────"
if [ "$FAIL" -eq 0 ]; then
  printf '%sKẾT QUẢ: %d mục đạt · 0 chưa đạt — môi trường sẵn sàng.%s\n' "$G" "$PASS" "$N"
  printf '%sChụp màn hình phần này nộp kèm báo cáo tuần 1.%s\n' "$D" "$N"
  exit 0
else
  printf '%sKẾT QUẢ: %d đạt · %d CHƯA ĐẠT — làm theo dòng → ở trên rồi chạy lại.%s\n' "$R" "$PASS" "$FAIL" "$N"
  printf '%sKẹt quá hai giờ ở một mục thì hỏi, đừng ngồi một mình.%s\n' "$D" "$N"
  exit 1
fi
