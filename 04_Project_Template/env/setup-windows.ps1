# ---------------------------------------------------------------------------
# setup-windows.ps1 — cài phần PHÍA WINDOWS của môi trường làm việc.
#
# Engineering & Research Mentoring Program (Lucero)
# ThS. Đinh Văn Nam (Mr. Lucero Dinh) — Khoa Điện–Điện tử, ĐH Phenikaa
#
# Chạy trong Windows PowerShell 64-bit, QUYỀN ADMINISTRATOR:
#     Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force
#     .\setup-windows.ps1
#     .\setup-windows.ps1 -DryRun      # chỉ in ra sẽ làm gì
#     .\setup-windows.ps1 -Pcb         # thêm KiCad (nhánh A0)
#     .\setup-windows.ps1 -Esp         # thêm PlatformIO (nhánh A6, A7)
#
# CHẠY LẠI ĐƯỢC NHIỀU LẦN: mỗi bước kiểm trước, có rồi thì bỏ qua.
#
# KHÔNG tự cài được (phải làm tay, script sẽ nhắc ở cuối):
#   · Quartus Prime Lite  — trình cài đồ họa, phải chọn đúng dòng device của board
#                           (board AMD/Xilinx thì là Vivado — xem SETUP-GUIDE §C7)
#   · Driver CH340/CP2102 — theo đúng chip trên board ESP8266
#   · Bật ảo hóa trong BIOS — không phần mềm nào làm thay được
# ---------------------------------------------------------------------------
[CmdletBinding()]
param(
  [switch]$DryRun,
  [switch]$Pcb,
  [switch]$Esp
)

$ErrorActionPreference = 'Stop'

function Say  ($m) { Write-Host "`n> $m" -ForegroundColor White }
function Good ($m) { Write-Host "  [OK]   $m" -ForegroundColor Green }
function Warn ($m) { Write-Host "  [!]    $m" -ForegroundColor Yellow }
function Info ($m) { Write-Host "  $m"       -ForegroundColor DarkGray }
function Die  ($m) { Write-Host "`n[LOI] $m" -ForegroundColor Red; exit 1 }

# ------------------------------------------------------------- điều kiện chạy
if (-not [Environment]::Is64BitProcess) {
  Die "Dang chay PowerShell 32-bit (x86). Dong lai, mo 'Windows PowerShell' KHONG co chu (x86)."
}
$admin = ([Security.Principal.WindowsPrincipal] `
          [Security.Principal.WindowsIdentity]::GetCurrent()
         ).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
if (-not $admin) { Die "Can quyen Administrator. Chuot phai PowerShell -> Run as administrator." }

$build = [System.Environment]::OSVersion.Version.Build
if ($build -lt 19041) {
  Die "Windows build $build qua cu (can >= 19041). Cap nhat Windows truoc, xem SETUP-GUIDE muc F1b."
}

Write-Host "================================================================"
Write-Host "CAI MOI TRUONG PHIA WINDOWS - Mentoring Lucero" -ForegroundColor White
Write-Host "Windows build $build - PowerShell 64-bit - quyen Administrator" -ForegroundColor DarkGray
if ($DryRun) { Write-Host "CHE DO THU - khong cai gi ca" -ForegroundColor Yellow }
Write-Host "================================================================"

# ------------------------------------------------------------------- winget
Say "Kiem tra winget"
if (-not (Get-Command winget -ErrorAction SilentlyContinue)) {
  Warn "Khong co winget. Cai 'App Installer' tu Microsoft Store roi chay lai."
  Warn "Cac buoc con lai se bi bo qua."
  $NoWinget = $true
} else {
  Good "winget $(winget --version)"
  $NoWinget = $false
}

# Install-App <winget-id> <ten-hien-thi> <lenh-kiem-tra>
function Install-App ($Id, $Name, $Probe) {
  if ($Probe -and (Get-Command $Probe -ErrorAction SilentlyContinue)) {
    Good "$Name da co"
    return
  }
  if ($NoWinget) { Warn "$Name - bo qua (khong co winget)"; return }
  if ($DryRun)   { Write-Host "  [dry-run] winget install --id $Id" -ForegroundColor Yellow; return }
  Info "dang cai $Name ..."
  winget install --id $Id --exact --silent `
        --accept-package-agreements --accept-source-agreements | Out-Null
  if ($LASTEXITCODE -eq 0) { Good "$Name da cai" }
  else { Warn "$Name cai khong thanh cong (ma $LASTEXITCODE) - cai tay neu can" }
}

# ---------------------------------------------------------------------- WSL2
Say "WSL2"
if (Test-Path C:\Windows\System32\wsl.exe) {
  $distros = (wsl --list --quiet 2>$null) -join ' '
  if ($distros -match 'Ubuntu') {
    Good "WSL2 co san, da co Ubuntu"
  } else {
    if ($DryRun) { Write-Host "  [dry-run] wsl --install -d Ubuntu" -ForegroundColor Yellow }
    else { Info "cai Ubuntu..."; wsl --install -d Ubuntu; Good "da goi lenh cai Ubuntu - KHOI DONG LAI may" }
  }
} else {
  Warn "Khong thay wsl.exe - bat tinh nang WSL truoc (SETUP-GUIDE muc F1c)"
}

# ----------------------------------------------------------- phần mềm chung
Say "Phan mem dung chung"
Install-App 'Git.Git'                     'Git for Windows'   'git'
Install-App 'Microsoft.VisualStudioCode'  'VS Code'           'code'
Install-App 'Microsoft.WindowsTerminal'   'Windows Terminal'  $null

# ------------------------------------------------------------ VS Code extras
if (-not $DryRun -and (Get-Command code -ErrorAction SilentlyContinue)) {
  Say "Extension VS Code"
  $exts = @('ms-vscode-remote.remote-wsl', 'ms-python.python', 'mshr-h.veriloghdl')
  if ($Esp) { $exts += 'platformio.platformio-ide' }
  foreach ($e in $exts) {
    code --install-extension $e --force 2>$null | Out-Null
    Good $e
  }
}

# --------------------------------------------------------------- nhánh A0
if ($Pcb) {
  Say "Nhanh A0 - thiet ke PCB"
  Install-App 'KiCad.KiCad' 'KiCad' $null
}

# ------------------------------------------------------------- việc làm tay
Say "Ba viec script KHONG lam duoc - phai lam tay"
Write-Host ""
Write-Host "  1. QUARTUS PRIME LITE (nhanh A3, A4)" -ForegroundColor Yellow
Write-Host "     Tai ban Lite tu trang Intel. Khi cai PHAI tick dung dong device cua board:"
Write-Host "     MAX 10 cho DE10-Lite, Cyclone IV/V cho DE2/DE1-SoC. Nho cai ca USB-Blaster driver."
Write-Host "     Board AMD/Xilinx: cai VIVADO thay Quartus - xem SETUP-GUIDE muc C7." -ForegroundColor DarkGray
Write-Host "     Chi cai MOT bo cong cu, moi bo chiem hang chuc GB." -ForegroundColor DarkGray
Write-Host ""
Write-Host "  2. DRIVER USB-UART (nhanh A6, A7)" -ForegroundColor Yellow
Write-Host "     NodeMCU/Wemos thuong dung chip CH340, doi khi CP2102. Cai driver theo dung chip,"
Write-Host "     roi kiem Device Manager > Ports (COM & LPT) phai thay cong COM."
Write-Host ""
Write-Host "  3. BAT AO HOA TRONG BIOS (neu WSL bao loi)" -ForegroundColor Yellow
Write-Host "     Khoi dong lai vao BIOS, bat Intel VT-x / AMD-V / SVM Mode."
Write-Host ""

Say "Buoc tiep theo"
Info "Mo Ubuntu (WSL) roi chay phan Linux:"
Write-Host "     bash bootstrap.sh --rtl        # hoac --asic / --polar / --all"
Write-Host "     bash doctor.sh --all"
Write-Host ""
