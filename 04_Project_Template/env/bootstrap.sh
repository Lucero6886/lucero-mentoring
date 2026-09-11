#!/usr/bin/env bash
# ---------------------------------------------------------------------------
# bootstrap.sh — dựng môi trường làm việc trong WSL2 / Ubuntu.
#
# Engineering & Research Mentoring Program (Lucero)
# ThS. Đinh Văn Nam (Mr. Lucero Dinh) — Khoa Điện–Điện tử, ĐH Phenikaa
#
# Script này làm được phần CHẠY TRONG LINUX của SETUP-GUIDE. Phần phía Windows
# (cài WSL, Quartus, KiCad, driver USB) phải làm tay hoặc dùng setup-windows.ps1.
#
#   bash bootstrap.sh              # nền chung — mọi sinh viên
#   bash bootstrap.sh --rtl        # + iverilog, gtkwave, verilator (A1-A3)
#   bash bootstrap.sh --asic       # + Nix và LibreLane            (A4-A5)
#   bash bootstrap.sh --polar      # + numpy/scipy/matplotlib      (B0-B6)
#   bash bootstrap.sh --all        # tất cả
#   bash bootstrap.sh --dry-run    # chỉ in ra sẽ làm gì, không cài
#
# CHẠY LẠI ĐƯỢC NHIỀU LẦN: mỗi bước đều kiểm trước, có rồi thì bỏ qua.
# ---------------------------------------------------------------------------
set -euo pipefail
export LC_ALL="${LC_ALL:-C.UTF-8}" 2>/dev/null || true

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LOG="$HOME/.mentoring-bootstrap.log"
DO_RTL=0; DO_ASIC=0; DO_POLAR=0; DRY=0

for a in "$@"; do
  case "$a" in
    --rtl) DO_RTL=1 ;; --asic) DO_ASIC=1 ;; --polar) DO_POLAR=1 ;;
    --all) DO_RTL=1; DO_ASIC=1; DO_POLAR=1 ;;
    --dry-run) DRY=1 ;;
    -h|--help) sed -n '3,18p' "$0" | sed 's/^# \{0,1\}//'; exit 0 ;;
    *) echo "Tham số lạ: $a  (dùng --help)"; exit 2 ;;
  esac
done

if [ -t 1 ]; then G=$'\033[32m'; R=$'\033[31m'; Y=$'\033[33m'; B=$'\033[1m'; D=$'\033[2m'; N=$'\033[0m'
else G=""; R=""; Y=""; B=""; D=""; N=""; fi

say()  { printf '\n%s▸ %s%s\n' "$B" "$1" "$N"; }
info() { printf '  %s%s%s\n' "$D" "$1" "$N"; }
good() { printf '  %s✔%s %s\n' "$G" "$N" "$1"; }
warn() { printf '  %s!%s %s\n' "$Y" "$N" "$1"; }
die()  { printf '\n%s✘ %s%s\n' "$R" "$1" "$N"; exit 1; }

run() {  # run <mô tả> <lệnh...>
  local what="$1"; shift
  if [ "$DRY" = 1 ]; then printf '  %s[dry-run]%s %s\n' "$Y" "$N" "$*"; return 0; fi
  info "$what"
  if ! "$@" >>"$LOG" 2>&1; then
    die "Lỗi ở bước: $what — xem chi tiết trong $LOG"
  fi
}

# ------------------------------------------------------------- kiểm tra đầu vào
[ "$(id -u)" -eq 0 ] && die "Đừng chạy bằng root hay sudo. Chạy với tài khoản thường; script tự gọi sudo khi cần."
command -v apt-get >/dev/null 2>&1 || die "Script này dành cho Ubuntu/Debian (WSL2). Máy này không có apt."

grep -qiE 'microsoft|wsl' /proc/version 2>/dev/null && WSL=1 || WSL=0

printf '%s\n' "════════════════════════════════════════════════════════════════"
printf '%sDỰNG MÔI TRƯỜNG · Mentoring Lucero%s\n' "$B" "$N"
printf '%sNhật ký đầy đủ: %s%s\n' "$D" "$LOG" "$N"
[ "$DRY" = 1 ] && printf '%sCHẾ ĐỘ THỬ — không cài gì cả%s\n' "$Y" "$N"
printf '%s\n' "════════════════════════════════════════════════════════════════"
: >"$LOG" 2>/dev/null || true
[ "$WSL" = 0 ] && warn "Không nhận ra WSL — vẫn chạy được trên Ubuntu thường."

# ------------------------------------------------------------------ gói nền
say "Gói nền hệ thống"
PKGS=(build-essential git curl wget unzip ca-certificates
      python3 python3-pip python3-venv openssh-client)
MISSING=()
for p in "${PKGS[@]}"; do
  dpkg -s "$p" >/dev/null 2>&1 || MISSING+=("$p")
done
if [ ${#MISSING[@]} -eq 0 ]; then
  good "đã đủ (${#PKGS[@]} gói)"
else
  info "thiếu: ${MISSING[*]}"
  run "cập nhật danh sách gói" sudo apt-get update -qq
  run "cài ${#MISSING[@]} gói còn thiếu" sudo apt-get install -y -qq "${MISSING[@]}"
  [ "$DRY" = 0 ] && good "đã cài xong"
fi

# --------------------------------------------------------------------- git
say "Cấu hình Git"
gn="$(git config --global user.name  2>/dev/null || true)"
ge="$(git config --global user.email 2>/dev/null || true)"

if [ -z "$gn" ] || [ -z "$ge" ]; then
  if [ -t 0 ] && [ "$DRY" = 0 ]; then
    [ -z "$gn" ] && { read -rp "  Họ tên đầy đủ của em: " gn; git config --global user.name "$gn"; }
    [ -z "$ge" ] && { read -rp "  Email trường (đã đăng ký GitHub): " ge; git config --global user.email "$ge"; }
  else
    warn "chưa đặt user.name / user.email — chạy lại script này trong terminal để nhập"
  fi
fi
[ -n "$(git config --global user.name 2>/dev/null || true)" ] && good "user.name  = $(git config --global user.name)"
[ -n "$(git config --global user.email 2>/dev/null || true)" ] && good "user.email = $(git config --global user.email)"

git config --global init.defaultBranch main 2>/dev/null || true
git config --global core.editor nano 2>/dev/null || true
git config --global pull.rebase false 2>/dev/null || true
good "init.defaultBranch = main · core.editor = nano"

# --------------------------------------------------------------------- ssh
say "Khóa SSH cho GitHub"
KEY="$HOME/.ssh/id_ed25519"
if [ -f "$KEY.pub" ]; then
  good "đã có $KEY.pub"
elif [ "$DRY" = 1 ]; then
  printf '  %s[dry-run]%s ssh-keygen -t ed25519\n' "$Y" "$N"
else
  mkdir -p "$HOME/.ssh"; chmod 700 "$HOME/.ssh"
  ssh-keygen -t ed25519 -C "${ge:-sinhvien@phenikaa}" -f "$KEY" -N "" >>"$LOG" 2>&1
  good "đã tạo khóa mới"
fi

if [ -f "$KEY.pub" ] && [ "$DRY" = 0 ]; then
  if timeout 12 ssh -o StrictHostKeyChecking=accept-new -o BatchMode=yes \
       -T git@github.com 2>&1 | grep -q 'successfully authenticated'; then
    good "GitHub đã nhận khóa này"
  else
    warn "GitHub CHƯA nhận khóa — làm nốt bước tay dưới đây"
    printf '\n%s  1. Chép TOÀN BỘ dòng dưới:%s\n\n' "$Y" "$N"
    printf '%s\n\n' "$(cat "$KEY.pub")"
    printf '%s  2. GitHub → ảnh đại diện → Settings → SSH and GPG keys → New SSH key → dán → Add.%s\n' "$Y" "$N"
    printf '%s  3. Kiểm lại:  ssh -T git@github.com%s\n' "$Y" "$N"
  fi
fi

# ---------------------------------------------------------------- thư mục
say "Thư mục làm việc"
if [ -d "$HOME/projects" ]; then good "$HOME/projects (đã có)"
elif [ "$DRY" = 1 ]; then printf '  %s[dry-run]%s mkdir -p %s/projects\n' "$Y" "$N" "$HOME"
else mkdir -p "$HOME/projects"; good "$HOME/projects (vừa tạo)"; fi
[ "$WSL" = 1 ] && info "Nhớ: repo để trong ~/projects (nhanh), KHÔNG để trong /mnt/c (chậm 10–20 lần)."

# ------------------------------------------------------------- nhánh RTL
if [ "$DO_RTL" = 1 ]; then
  say "Nhánh A1–A3 · mô phỏng RTL"
  RPKGS=(iverilog gtkwave verilator)
  RMISS=(); for p in "${RPKGS[@]}"; do dpkg -s "$p" >/dev/null 2>&1 || RMISS+=("$p"); done
  if [ ${#RMISS[@]} -eq 0 ]; then good "đã đủ (${RPKGS[*]})"
  else
    run "cài ${RMISS[*]}" sudo apt-get install -y -qq "${RMISS[@]}"
    [ "$DRY" = 0 ] && good "đã cài ${RMISS[*]}"
  fi
fi

# ------------------------------------------------------------ nhánh Polar
if [ "$DO_POLAR" = 1 ]; then
  say "Nhánh B0–B6 · mô phỏng Polar"
  info "Thư viện Python cài trong TỪNG repo, không cài toàn cục."
  cat <<'EOF'
      cd ~/projects/<repo-của-em>
      python3 -m venv venv
      source venv/bin/activate
      pip install numpy scipy matplotlib pandas jupyter
      pip freeze > requirements.txt      # nhớ commit file này
EOF
  good "hướng dẫn ở trên — chạy trong repo của em"
fi

# ------------------------------------------------------------- nhánh ASIC
if [ "$DO_ASIC" = 1 ]; then
  say "Nhánh A4–A5 · Nix và LibreLane"

  # a. systemd
  if [ "$WSL" = 1 ] && ! systemctl is-system-running >/dev/null 2>&1; then
    warn "WSL chưa bật systemd — Nix cần nó."
    printf '%s      sudo nano /etc/wsl.conf   →  [boot]\\nsystemd=true%s\n' "$Y" "$N"
    printf '%s      rồi từ PowerShell:  wsl --shutdown%s\n' "$Y" "$N"
    die "Bật systemd xong chạy lại script này."
  fi
  [ "$WSL" = 1 ] && good "systemd đang chạy"

  # b. dung lượng
  FREE_GB=$(df -BG --output=avail "$HOME" 2>/dev/null | tail -1 | tr -dc '0-9')
  if [ -n "$FREE_GB" ] && [ "$FREE_GB" -lt 20 ]; then
    warn "chỉ còn ${FREE_GB} GB trống — Nix store cần 10–20 GB. Xem SETUP-GUIDE §F8d."
  else
    good "dung lượng trống ${FREE_GB:-?} GB"
  fi

  # c. Nix — lệnh lấy nguyên văn từ tài liệu chính thức của LibreLane
  if command -v nix >/dev/null 2>&1; then
    good "nix đã cài — $(nix --version 2>/dev/null)"
  elif [ "$DRY" = 1 ]; then
    printf '  %s[dry-run]%s cài Nix kèm bộ nhớ đệm FOSSi\n' "$Y" "$N"
  else
    info "cài Nix (vài phút)…"
    curl --proto '=https' --tlsv1.2 -fsSL https://artifacts.nixos.org/nix-installer \
      | sh -s -- install --no-confirm --extra-conf "
    extra-substituters = https://nix-cache.fossi-foundation.org
    extra-trusted-public-keys = nix-cache.fossi-foundation.org:3+K59iFwXqKsL7BNu6Guy0v+uTlwsxYQxjspXzqLYQs=
    extra-experimental-features = nix-command flakes
" >>"$LOG" 2>&1 || die "Cài Nix thất bại — xem $LOG"
    good "đã cài Nix"
    warn "ĐÓNG HẲN cửa sổ Ubuntu rồi mở lại, sau đó chạy lại script này."
  fi

  # d. bộ nhớ đệm — kiểm cả khi Nix có sẵn từ trước
  CACHE="nix-cache.fossi-foundation.org"
  if [ -r /etc/nix/nix.conf ] && grep -q "trusted-public-keys.*$CACHE" /etc/nix/nix.conf 2>/dev/null; then
    good "bộ nhớ đệm FOSSi đã cấu hình"
  else
    warn "THIẾU bộ nhớ đệm FOSSi — Nix sẽ tự biên dịch OpenROAD hàng giờ."
    printf '%s      Thêm ba dòng này vào /etc/nix/nix.conf rồi: sudo systemctl restart nix-daemon%s\n' "$Y" "$N"
    cat <<'EOF'
      extra-substituters = https://nix-cache.fossi-foundation.org
      extra-trusted-public-keys = nix-cache.fossi-foundation.org:3+K59iFwXqKsL7BNu6Guy0v+uTlwsxYQxjspXzqLYQs=
      extra-experimental-features = nix-command flakes
EOF
  fi

  # e. LibreLane
  if [ -d "$HOME/projects/librelane/.git" ]; then
    good "kho librelane đã có"
  elif [ "$DRY" = 1 ]; then
    printf '  %s[dry-run]%s git clone https://github.com/librelane/librelane\n' "$Y" "$N"
  else
    run "clone librelane" git clone --depth 1 https://github.com/librelane/librelane "$HOME/projects/librelane"
    [ "$DRY" = 0 ] && good "đã clone librelane"
  fi

  info "Bước cuối làm tay (tải vài GB, 20–40 phút):"
  printf '      cd ~/projects/librelane && nix-shell\n'
  printf '      librelane --smoke-test\n'
fi

# ------------------------------------------------------------------ kết thúc
say "Kiểm lại bằng doctor.sh"
if [ "$DRY" = 1 ]; then
  info "bỏ qua ở chế độ thử"
elif [ -f "$HERE/doctor.sh" ]; then
  FLAGS=""
  [ "$DO_RTL"   = 1 ] && FLAGS="$FLAGS --rtl"
  [ "$DO_ASIC"  = 1 ] && FLAGS="$FLAGS --asic"
  [ "$DO_POLAR" = 1 ] && FLAGS="$FLAGS --polar"
  # shellcheck disable=SC2086
  bash "$HERE/doctor.sh" $FLAGS || true
else
  warn "không tìm thấy doctor.sh cạnh script này"
fi

printf '\n%sXong. Nhật ký: %s%s\n' "$D" "$LOG" "$N"
