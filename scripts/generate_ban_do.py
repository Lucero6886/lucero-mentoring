# -*- coding: utf-8 -*-
"""Sinh Ban_do_84_de_tai.md + .html (bản đồ trực quan 84 đề tài) từ nguồn chuẩn 06_Data/.

Cách dùng (từ gốc repo):  python3 scripts/generate_ban_do.py
Đây là VIEW sinh tự động — không sửa tay file đầu ra; sửa 06_Data/ rồi chạy lại.
"""
import json, html, io, sys, pathlib
import cohort_schedule as cs

ROOT = pathlib.Path(__file__).resolve().parents[1]

BASE = (sys.argv[1].rstrip("/\\") if len(sys.argv) > 1 else str(ROOT / "06_Data")) + "/"
OUT = pathlib.Path(sys.argv[2]) if len(sys.argv) > 2 else ROOT
P = json.load(open(BASE + "project_portfolio.json", encoding="utf-8"))
C = json.load(open(BASE + "cohort_HK1_2026_2027.json", encoding="utf-8"))
G = json.load(open(BASE + "milestone_gates.json", encoding="utf-8"))

TOPICS = P["topics"]
FAM = P["families"]
ALIAS = {t["code"]: t["alias"] for t in C["topics"]}  # 21 đề tài mở HK1
TYPE_NAME = {"P": "Project môn học", "I": "Thực tập", "T": "Đồ án tốt nghiệp", "R": "Nghiên cứu"}
META = P["meta"]; VER = META["version"]; UPD = META["updated"]
from collections import Counter as _Counter
NTYPE = _Counter(t["type"] for t in TOPICS)
NTOP = len(TOPICS); NFAM = len(FAM); NOPEN = len(ALIAS)
CAL = cs.build_calendar(C.get("start_date"), C.get("duration_weeks"), C.get("breaks"))
DL  = cs.gate_deadlines(G["gates"], CAL)
NW  = C.get("duration_weeks")
GEND = cs.end_date(CAL)
# Nội dung sư phạm của từng trạm (không phải dữ liệu lịch) — ghép với khung tuần suy ra
GATE_TEXT = {
 1: ("Nói được input/output; chọn IP cụ thể (vd bộ lọc FIR nhỏ); toolchain cài chạy được",
     "Ký thỏa thuận làm việc; chốt **MVT** (phần bắt buộc) tách khỏi *extension* (phần mơ ước); chép 6 trạm vào hồ sơ"),
 2: ("RTL + testbench **chạy đúng**, có bằng chứng tái lập",
     "Luật cứng: không có baseline ở đây → **đóng cửa extension**, chỉ còn phần lõi"),
 3: ("Qua synthesis + kiểm tra timing sạch; số liệu trung gian",
     "Trượt → **thu hẹp phạm vi** ngay (bỏ extension → bớt quét tham số → thu nhỏ khối); tuyệt đối không làm thay"),
 4: ("Chạy trọn physical flow ra GDSII; bảng PPA chính",
     "Sau trạm này **cấm thêm thuật toán mới** — chỉ hoàn thiện"),
 5: ("Bản thảo khóa luận; mỗi con số trỏ về một bằng chứng đã kiểm",
     "Soát bằng sổ bằng chứng: claim không có evidence → bỏ khỏi báo cáo"),
 6: ("Người khác chạy lại được từ README; slide + demo; gói bàn giao",
     "Hỏi theo `DEFENSE_QUESTIONS.md`; nguyên tắc chốt: **không giải thích được = chưa hoàn thành**"),
}
GATE_SHORT = {1:"Hiểu bài toán",2:"Baseline",3:"Lõi",4:"Thực nghiệm",5:"Phân tích & bản thảo",6:"Tái lập & bảo vệ"}

# ---------- lời dẫn từng nhóm (ngôn ngữ đời thường) ----------
BLURB = {
"A0": ("Điện tử cầm tay được", "Nhóm khởi đầu cho sinh viên chưa từng chạm phần cứng: vẽ sơ đồ mạch, tự làm PCB, hàn linh kiện, cắm que đo. Một buổi làm việc điển hình là ngồi với mỏ hàn, đồng hồ đo và oscilloscope, debug tại sao mạch thật không chạy giống mạch trên giấy — chính cảm giác đó tạo ra trực giác phần cứng.", "Xong A0, sinh viên đủ tự tin để sang A1 (mô tả mạch bằng code) hoặc A3 (ghép board tự làm với FPGA)."),
"A1": ("Viết code sinh ra mạch số", "Học Verilog: viết văn bản mô tả mạch, mô phỏng, rồi soi dạng sóng (waveform) để kiểm tra đúng sai. Một buổi làm việc điển hình là viết module + testbench, chạy simulator, dò từng xung clock. Đây là nền móng của toàn bộ trục A và trục B phần cứng — hầu hết sinh viên đi qua đây.", "Xong A1, rẽ được ba hướng: A2 (mạch làm toán), A3 (lên FPGA thật), A5 (kiểm chứng bài bản)."),
"A2": ("Mạch số làm toán", "Thiết kế phần cứng cộng, nhân, lọc tín hiệu — và học bài toán trung tâm của nghề: dùng bao nhiêu bit là đủ (fixed-point)? Thêm bit thì chính xác hơn nhưng mạch to hơn, chậm hơn. Mỗi đề tài đều kết thúc bằng một bảng so sánh đánh đổi.", "Xong A2, sinh viên sẵn sàng cho A3/A4, và đây cũng chính là kỹ năng mà nhánh B3 (lượng tử hóa Polar) cần."),
"A3": ("Cho thiết kế chạy trên phần cứng thật", "Đưa RTL lên board FPGA: nạp bitstream, nối với thiết bị ngoài, đo tốc độ tối đa (Fmax) và lượng tài nguyên chiếm dụng. Khoảnh khắc thiết kế của mình nhấp nháy trên board thật là cột mốc tâm lý lớn của sinh viên.", "Xong A3, đi tiếp A4 (biến RTL thành chip) hoặc nhận các đề tài hệ thống lớn hơn."),
"A4": ("Từ code đến con chip trên bản vẽ", "Đi trọn con đường RTL → synthesis → kiểm tra timing (STA) → sắp đặt vật lý → GDSII (bản vẽ cuối cùng gửi nhà máy) bằng toolchain mã nguồn mở. Sinh viên học đọc ba con số quyết định của nghề IC: hiệu năng – công suất – diện tích (PPA).", "Xong A4, sinh viên đủ nền nhận đề tài nghiên cứu (R) hoặc các đề tài cầu nối AB."),
"A5": ("Nghề giữ cho dự án sống", "Testbench có hệ thống, chạy kiểm tra tự động lặp lại (regression), Git/CI, môi trường công cụ dựng lại được một lệnh. Nghe ít hào nhoáng nhưng đây là thứ công ty chip nào cũng tuyển — và đề tài ở nhóm này xây hạ tầng dùng chung cho cả các khóa sau.", "Sản phẩm nhóm A5 (quy trình LibreLane+Nix, CI) trở thành nền cho mọi đề tài A4/AB về sau."),
"B0": ("Polar trên máy tính, chưa đụng phần cứng", "Viết mô phỏng Polar code bằng Python/MATLAB: mã hóa, truyền qua kênh nhiễu, giải mã SC, vẽ đường cong tỉ lệ lỗi (BER/BLER). Kết quả quan trọng nhất là một 'golden model' — mô hình tham chiếu đúng mà mọi đề tài B phía sau đem phần cứng ra đối chiếu.", "Xong B0, sinh viên hiểu thuật toán đủ sâu để bắt đầu làm phần cứng ở B1, hoặc nghiên cứu thuật toán ở B3/B4."),
"B1": ("Những viên gạch phần cứng đầu tiên của Polar", "Biến các phép toán lõi của Polar (hàm f, hàm g, partial-sum) thành các module RTL nhỏ, mỗi module kiểm chứng độc lập với golden model. Triết lý của cả trục B nằm ở đây: làm nhỏ, kiểm kỹ, rồi mới ghép.", "Các viên gạch B1 chính là linh kiện để B2 lắp thành bộ giải mã hoàn chỉnh."),
"B2": ("Lắp thành bộ giải mã hoàn chỉnh", "Ghép golden model, số học fixed-point, các processing element và khối điều khiển thành bộ giải mã SC chạy trên FPGA — so từng frame với mô phỏng phần mềm. Đây là đề tài 'xương sống' của trục B: khó vừa đủ, sản phẩm rõ ràng.", "Có B2 rồi, các nhánh nghiên cứu B3/B4/B5 mới có nền phần cứng để đứng."),
"B3": ("Bao nhiêu bit là đủ?", "Câu hỏi nghiên cứu thật sự đầu tiên của trục B: giảm số bit biểu diễn LLR thì tiết kiệm phần cứng được bao nhiêu, và tỉ lệ lỗi xấu đi bao nhiêu? Sinh viên chạy thí nghiệm có kiểm soát và vẽ đường cong đánh đổi.", "Kỹ năng ở đây (quét tham số, phân tích trade-off) là đúng kiểu bài của một bài báo khoa học."),
"B4": ("Khi giải sai thì sai ở đâu — và thử lại", "Phân tích lỗi của bộ giải SC, xây thước đo độ tin cậy để đoán bit nào đáng ngờ, rồi lật (flip) và giải lại — thuật toán SC-Flip. Đánh giá luôn theo cặp: giảm được bao nhiêu lỗi, tốn thêm bao nhiêu lần thử.", "B4 mở thẳng ra hai hướng nghiên cứu nóng: B5 (thích ứng) và B6 (nhờ AI hỗ trợ)."),
"B5": ("Frame dễ giải nhanh, frame khó mới dùng sức", "Xây bộ phát hiện 'frame khó', chỉ khi gặp frame khó mới bật xử lý tăng cường — tiết kiệm năng lượng và thời gian trung bình mà vẫn giữ chất lượng. Đây là tư duy hệ thống: đo lường, ra quyết định, đánh đổi.", "B5 là bậc thang cuối trước các đề tài đồng thiết kế thuật toán – phần cứng (B5-T03, AB)."),
"B6": ("AI làm trợ lý cho bộ giải mã", "Dùng mạng nơ-ron nhỏ gọn hỗ trợ đúng một việc hẹp — phát hiện frame khó, hoặc xếp hạng ứng viên bit lỗi — chứ không thay cả bộ giải mã. Luật cứng của nhóm: kết quả neural phải so được với cách cổ điển, không so thì không nhận.", "Đây là nhóm cao nhất trục B (sàn L4–L5), dành cho sinh viên đã có baseline vững và hướng đi tiếp sau đại học."),
"A6": ("Nhúng: phần mềm chạy sát phần cứng", "Nhóm mở đầu nhánh Nhúng & IoT của trục A (mở từ v1.5.0): viết firmware điều khiển ngoại vi thật, dùng RTOS chia việc theo thời gian thực, rồi lên SoC FPGA — nơi một nửa hệ thống là phần cứng mình thiết kế, nửa kia là phần mềm mình viết. Chính ở ranh giới đó sinh viên học được câu hỏi trung tâm của co-design: việc gì để phần mềm làm, việc gì đáng đưa xuống phần cứng.", "Xong A6, đi tiếp A7 (kết nối IoT, AI biên) hoặc A6-T02/AB-T05 (tăng tốc phần cứng — cửa vào co-design)."),
"A7": ("IoT và trí tuệ tại biên", "Nối các thiết bị nhúng thành hệ thống hoàn chỉnh: cảm biến, giao thức (MQTT/BLE/LoRa), và bài toán sống còn của thiết bị chạy pin — ngân sách năng lượng. Tầng trên cùng là edge AI: nén mô hình học máy xuống vài trăm KB để suy luận ngay trên vi điều khiển. Mọi đề tài đều bắt sinh viên đo trên thiết bị thật, chạy nhiều ngày thật.", "Xong A7, sinh viên đủ nền cho các đề tài co-design AB (tăng tốc AI biên, decoder tiết kiệm năng lượng) và các đề tài R hướng luận án."),
"AB": ("Cầu nối các trục — ra chất nghiên cứu thật", "Lấy một thuật toán — giải mã Polar của trục B, hay suy luận AI biên của A7 — và trả lời câu hỏi phần cứng: tốn bao nhiêu diện tích, nhanh cỡ nào, bao nhiêu năng lượng cho một bit tin cậy hay một lần suy luận? Từ v1.5.0, AB mở rộng đúng theo định hướng nghiên cứu luận án của mentor: co-design vi mạch × nhúng/IoT (AB-P01, AB-T05) và Polar × IoT (AB-T06), hội tụ ở các đề tài R (AB-R02, AB-R03) — nơi quyết định thuật toán và quyết định phần cứng được tối ưu cùng nhau.", "Đề tài AB là bước đệm đẹp nhất từ đồ án tốt nghiệp sang bài báo hội nghị — và là đường thẳng vào chương trình nghiên cứu luận án."),
}

CHAIN_A = ["A0", "A1", "A2", "A3", "A4", "A5"]
CHAIN_A2 = ["A6", "A7"]
CHAIN_B = ["B0", "B1", "B2", "B3", "B4", "B5", "B6"]

def fam_topics(f):
    return [t for t in TOPICS if t["family"] == f]

def trim(s, n=150):
    s = (s or "").strip().rstrip(".")
    return s if len(s) <= n else s[:n].rsplit(" ", 1)[0] + "…"

# ============================================================ MD ============
md = io.StringIO()
w = md.write
w(f"# Bản đồ {NTOP} đề tài & cách sử dụng hệ thống\n\n")
w(f"**Engineering & Research Mentoring Program (Lucero)** · Phiên bản hệ thống {VER} · {UPD}\n")
w("Tác giả & mentor: ThS. Đinh Văn Nam (Mr. Lucero Dinh) — Khoa Điện–Điện tử, Trường Kỹ thuật, Đại học Phenikaa\n")
w("Bản web (mở từ điện thoại, chia sẻ được): https://claude.ai/code/artifact/68a2de47-bc1e-41cc-b588-cd34ffd90c90\n\n")
w("> Đây là chương trình **dài hạn, nhiều học kỳ** — quản lý NCKH, luận án, thực tập và mentor cộng đồng IC design; mỗi học kỳ chạy một cohort (hiện tại: DATN HK1 2026-2027).\n>\n")
w(f"> Tài liệu này trả lời hai câu hỏi bằng ngôn ngữ đời thường: **mỗi đề tài trong {NTOP} đề tài thực chất là làm cái gì**, và **anh dùng kho đề tài này thế nào cho ba việc: giảng dạy – mentor – nghiên cứu**. ")
w("Nó là bản diễn giải của dữ liệu nguồn chuẩn `06_Data/project_portfolio.json`; khi lệch nhau, JSON thắng. Bản dễ đọc: `Ban_do_84_de_tai.html`.\n\n---\n\n")

w("## 1. Bức tranh lớn trong một phút\n\n")
w("Kho đề tài là một **tấm bản đồ hai trục, bốn bậc thang**:\n\n")
w("- **Trục A — làm chip số** (A0→A5): từ hàn mạch bằng tay, viết Verilog, làm toán trên phần cứng, chạy trên FPGA, đến biến code thành bản vẽ chip (GDSII) và xây hạ tầng kiểm chứng. **Từ v1.5.0 mở rộng thêm nhánh Nhúng & IoT (A6, A7)**: firmware, RTOS, SoC, kết nối IoT và AI tại biên.\n")
w("- **Trục B — giải mã Polar** (7 nhóm B0→B6): từ mô phỏng thuật toán trên máy tính, dựng từng viên gạch phần cứng, lắp thành bộ giải mã, đến các câu hỏi nghiên cứu: lượng tử hóa, SC-Flip, giải mã thích ứng, AI hỗ trợ.\n")
w("- **Vùng giao AB**: đem thuật toán Polar đi trả lời câu hỏi phần cứng — chất liệu nghiên cứu \"hardware-aware\" đúng nghĩa.\n\n")
w("Mỗi nhóm có 4 loại hoạt động, xếp như **bậc thang trách nhiệm** — cùng một chủ đề nhưng đòi hỏi tăng dần:\n\n")
w("| Bậc | Loại | Bản chất | Câu hỏi định nghĩa |\n|---|---|---|---|\n")
w(f"| 1 | **P** — Project môn học ({NTYPE[chr(80)]} đề tài) | *Học* một kỹ năng cụ thể, không cần mới | \"Em đã làm được kỹ năng X chưa?\" |\n")
w(f"| 2 | **I** — Thực tập ({NTYPE[chr(73)]}) | *Tập làm việc* theo quy trình kỹ sư thật | \"Em làm việc có kỷ luật kỹ thuật chưa?\" |\n")
w(f"| 3 | **T** — Đồ án tốt nghiệp ({NTYPE[chr(84)]}) | *Sở hữu* một sản phẩm trọn vẹn: đúng, đủ, tái lập được, có số liệu | \"Đây có phải sản phẩm hoàn chỉnh của riêng em không?\" |\n")
w(f"| 4 | **R** — Nghiên cứu ({NTYPE[chr(82)]}) | *Trả lời một câu hỏi chưa có đáp án*, chấp nhận kết quả phủ định | \"Em đã chứng minh/bác bỏ giả thuyết bằng bằng chứng chưa?\" |\n\n")
w("Kèm theo là **thang trưởng thành L0–L5** của sinh viên (L0 mới khám phá → L5 sẵn sàng nghiên cứu nâng cao). Mỗi đề tài ghi một mức **sàn** (`min_level`): dưới sàn vẫn có thể nhận, nhưng phải ghi lý do và thu hẹp phạm vi.\n\n")
w("Chuỗi nối tiếp tự nhiên giữa các nhóm:\n\n")
w("```\nTrục A (chip):    A0 hàn mạch → A1 Verilog → A2 mạch làm toán → A3 FPGA → A4 ra chip → A5 hạ tầng kiểm chứng\nNhánh nhúng-IoT:  A6 nhúng/SoC → A7 IoT & AI biên   (mở từ v1.5.0)\nTrục B (Polar):   B0 mô phỏng → B1 viên gạch RTL → B2 bộ giải mã → B3 bao nhiêu bit? → B4 SC-Flip → B5 thích ứng → B6 AI hỗ trợ\nGặp nhau tại:     AB — co-design: Polar/edge-AI đo bằng thước phần cứng (PPA, năng lượng) — định hướng luận án\n```\n\n---\n\n")

w(f"## 2. Đi một vòng {NFAM} nhóm — mỗi đề tài làm ra cái gì\n\n")
w("Cách đọc bảng: **Mã chuẩn** là định danh vĩnh viễn trong hệ thống; cột **HK1** là mã rút gọn sinh viên nhìn thấy trong danh mục DATN kỳ này (chỉ 21 đề tài T đang mở có mã này); **Sàn** là level tối thiểu nên có; **Làm ra** tóm tắt sản phẩm nộp được lấy từ nguồn chuẩn.\n\n")
for f in CHAIN_A + CHAIN_A2 + CHAIN_B + ["AB"]:
    fd = FAM[f]; tag, body, nxt = BLURB[f]
    w(f"### {f} · {fd['name_vi']} — {tag}\n\n{body}\n\n*Đi tiếp:* {nxt}\n\n")
    w("| Mã | Loại | Sàn | HK1 | Đề tài | Làm ra |\n|---|---|---|---|---|---|\n")
    for t in fam_topics(f):
        al = ALIAS.get(t["code"], "")
        w(f"| `{t['code']}` | {t['type']} | L{t['min_level']} | {('**'+al+'**') if al else '—'} | {t['title_vi']} | {trim(t.get('outputs'),130)} |\n")
    w("\n")
w("---\n\n")

w("## 3. Bốn cách anh dùng kho đề tài này\n\n")
w("### 3.1 Giảng dạy — loại P trong môn học\n\n")
w("Đề tài P là **bài thực hành lớn có chuẩn đầu ra sẵn**: mỗi đề tài đã ghi rõ đầu vào cần gì, sản phẩm nộp gì, dùng công cụ nào. Cách dùng trong một môn học:\n\n")
w("1. Chọn các đề tài P có `min_level` khớp trình độ lớp (ví dụ lớp mới học HDL: A1-P01/P02, sàn L0).\n")
w("2. Dòng **Làm ra** của đề tài chính là barem nộp bài — không phải soạn lại yêu cầu từng học kỳ.\n")
w("3. Sinh viên khá có thể làm phần *mở rộng* ghi sẵn trong đề tài để lấy điểm cộng.\n")
w("4. Nhiều em cùng hổng một kỹ năng → mở **bootcamp chung** một buổi (danh sách kỹ năng bootcamp có trong `10_Documentation/MENTOR-GUIDE.md` §8) thay vì giảng lại 1-1.\n\n")
w("*Ví dụ:* giao `A1-P04` (UART) cho môn Thiết kế số: tuần 1 sinh viên viết transmitter + testbench, tuần 2 receiver + loopback, tuần 3 nộp repo có README và waveform chứng minh. Chuẩn chấm nằm sẵn trong danh mục.\n\n")
w("### 3.2 Thực tập — loại I, cửa bắt buộc trước đồ án\n\n")
w("Đề tài I là nơi sinh viên tập *tác phong*: Git đúng cách, báo cáo tuần, làm theo quy trình — sản phẩm kỹ thuật chỉ là phương tiện. ")
w("Mỗi trục có đề tài I ở mọi tầng (A0-I01 làm phần cứng thật, A5-I01 dựng Git workflow, B0-I01 xây bộ mô phỏng tái lập…), nên em nào cũng chọn được một kỳ thực tập vừa sức mà vẫn nằm đúng hướng nghề định theo.\n\n")
w("### 3.3 Mentor đồ án tốt nghiệp — loại T, 15 tuần, 6 trạm kiểm soát\n\n")
w(f"Khuôn {NW} tuần – 6 trạm này **dùng chung cho mọi khóa**: các mốc đếm theo số tuần kể từ ngày sinh viên chính thức nhận đề tài, không gắn với một học kỳ cụ thể. Khóa đang chạy ({NOPEN} đề tài mở) "
  + (f"bắt đầu {cs.dmy(CAL[0][chr(39)+'start'+chr(39)]) if False else cs.dmy(CAL[0]['start'])} nên có thêm ngày tương ứng ở cột hạn. " if CAL else "chưa công bố ngày bắt đầu, nên chỉ hiện mốc tuần. ")
  + "Kể bằng một ví dụ giả định — bạn **Minh** chọn `A4-T01` *(mã HK1: A1 — Thiết kế một Digital IP từ RTL đến GDSII)*:\n\n")
w("| Trạm | Tuần · hạn chót | Minh phải cho xem | Anh làm gì |\n|---|---|---|---|\n")
for _g in G["gates"]:
    _n = _g["gate"]; _sv, _me = GATE_TEXT[_n]
    w(f"| Gate {_n} — {GATE_SHORT[_n]} | {cs.week_label(_g)} · **{cs.due_compact(_g, DL)}** | {_sv} | {_me} |\n")
w("\n")
w("Giữa các trạm là **nhịp tuần** ~30 phút/sinh viên: đọc báo cáo tuần trước buổi gặp → trong buổi em trình theo khung *Mục tiêu → Bằng chứng → Cái gì hỏng → Chẩn đoán → Bước tiếp* → chốt 1–3 việc có hạn → ghi vào workbook. Thao tác chi tiết từng buổi: `10_Documentation/MENTOR-GUIDE.md`.\n\n")
w("Sức mạnh của cách chạy này: **mọi sinh viên cùng đi qua 6 trạm giống nhau**, nên anh mentor 10 em cùng lúc vẫn nhìn được toàn cảnh trong một sheet — ai xanh ai đỏ, ai sắp đến trạm nào.\n\n")
w("### 3.4 Nghiên cứu — loại R và con đường lên bài báo\n\n")
w("Hệ thống tạo nghiên cứu theo **hai cửa**:\n\n")
w("1. **Cửa extension** (phổ biến nhất): sinh viên làm đồ án T vững, qua Gate 2 đúng hạn → được mở phần mở rộng có chất nghiên cứu. Ví dụ: `B4-T01` (SC-Flip) làm xong phần lõi → extension \"cải tiến thước đo độ tin cậy\" → nếu kết quả tốt, đó là hạt nhân một bài báo. Extension thất bại **không** làm hỏng đồ án — phần lõi vẫn tự đứng được.\n")
w("2. **Cửa đề tài R** (10 đề tài, sàn L4–L5): dành cho sinh viên đã chứng minh năng lực, thường là em đã làm T kỳ trước. Đề tài R chấp nhận *kết quả phủ định* — giả thuyết sai nhưng thí nghiệm sạch vẫn là nghiên cứu đạt.\n\n")
w("Nhìn xa hơn một học kỳ, trục B chính là **một chương trình nghiên cứu nhiều thế hệ**: em khóa này làm B2 (bộ giải mã nền) để lại gói bàn giao; em khóa sau đứng trên đó làm B4/B5; em giỏi nhất chạm B6 (AI hỗ trợ) và AB (đo bằng thước chip). Mỗi đồ án bắt buộc để lại **Legacy Package** — nên kho của anh giàu lên sau mỗi khóa thay vì làm lại từ đầu.\n\n")
w("**Con đường lên luận án của mentor** (mở từ v1.5.0) chạy qua đúng các bậc thang này: sinh viên vững nhúng/AI biên (`A6-T02`, `A7-T02`) hoặc Polar hardware (`B2-T01`, `B3-T01`) → đề tài co-design (`AB-T05` tăng tốc AI biên trên SoC FPGA, `AB-T06` decoder Polar tiết kiệm năng lượng cho IoT) → đề tài nghiên cứu (`AB-R02` co-design truyền thông tin cậy ở biên, `AB-R03` nền tảng biên tích hợp truyền thông + suy luận). Mỗi tầng để lại baseline và số liệu cho tầng sau — nhiều sinh viên, nhiều học kỳ, cùng bồi vào một hướng nghiên cứu.\n\n---\n\n")

w("## 4. Sinh viên mới đến — chọn đề tài trong 4 bước\n\n")
w("1. **Hỏi đích đến nghề nghiệp** rồi tra bảng dưới → ra 2–3 ứng viên đề tài.\n")
w("2. **So level**: sinh viên tự chấm + anh kiểm chứng qua bài thử việc (readiness test) → so với sàn của đề tài.\n")
w("3. **So đầu vào**: mỗi đề tài ghi mã đầu vào tham chiếu (vd `A1-P*` = *đã làm ít nhất một project A1 hoặc tương đương có bằng chứng*).\n")
w("4. **Chốt phạm vi**: nguyện vọng quyết định *hướng*, mức sẵn sàng quyết định *độ lớn* — nhận / nhận có điều kiện / đổi đề tài.\n\n")
w("| Đích đến của em | Đề tài chính | Bước tiếp theo |\n|---|---|---|\n")
for cg in C["career_guide"]:
    note = (" *(" + cg["note"] + ")*") if cg.get("note") else ""
    w(f"| {cg['goal']}{note} | {', '.join('`'+x+'`' for x in cg['primary'])} | {', '.join('`'+x+'`' for x in cg['next'])} |\n")
w("| Embedded & IoT engineer *(nhánh mở từ v1.5.0)* | `A6-T01`, `A7-T01`, `A7-T02` | `A6-T02`, `AB-T05`, `A6-R01`, `A7-R01` |\n")
w("| Algorithm–hardware co-design *(định hướng luận án)* | `A6-T02`, `AB-T05`, `AB-T06` | `AB-R02`, `AB-R03` |\n")
w("\n---\n\n")

w("## 5. Mở gì, khi nào\n\n")
w("| Tình huống | Mở |\n|---|---|\n")
w("| Cần thao tác từng buổi gặp / gate / xử lý SV chậm | `10_Documentation/MENTOR-GUIDE.md` |\n")
w("| Phát tài liệu cho sinh viên | `Danh_muc_de_tai_DATN_Nhom_A_B_HK1_2026_2027.docx/.pdf` + `Phieu_lua_chon_va_danh_gia_de_tai_DATN_HK1_2026_2027.docx` (thư mục gốc) |\n")
w("| Theo dõi cả lớp hằng tuần | `03_Operations/Mentoring_Management_Workbook.xlsx` |\n")
w("| Sửa đề tài / thang điểm / lịch | `06_Data/*.json` rồi chạy 3 lệnh trong `10_Documentation/WORKFLOW.md` |\n")
w("| Hiểu kiến trúc & quyết định thiết kế của hệ thống | `implementation-notes.md` / `.html` |\n")
w("| Triết lý giáo dục gốc | `01_Governance/Master_Mentoring_Handbook.docx` |\n\n")
w(f"*Tài liệu sinh từ nguồn chuẩn v{VER} ({UPD}) — dữ liệu đổi thì chạy lại `python3 scripts/generate_ban_do.py`.*\n")

MD = md.getvalue()
io.open(str(OUT / "Ban_do_de_tai.md"), "w", encoding="utf-8").write(MD)
print("MD OK:", len(MD), "chars")


# ======================= PHẦN HTML =======================

esc = html.escape

CSS = """
:root{
  --paper:#F7F8F6; --card:#FFFFFF; --ink:#1C2733; --mut:#5A6772; --line:#DCE2DE;
  --acc:#0E7C6B; --acc-soft:#E3EFEB; --amb:#8F6400; --amb-soft:#F4ECD9;
  --ind:#4C5FD5; --ind-soft:#E7EAFA; --code-bg:#EDF1EE; --head:#12332D;
}
@media (prefers-color-scheme: dark){
  :root:not([data-theme="light"]){
    --paper:#12181D; --card:#1A222A; --ink:#E4EAE7; --mut:#98A4AC; --line:#2B353D;
    --acc:#4CC2AD; --acc-soft:#17352F; --amb:#E3B341; --amb-soft:#332B14;
    --ind:#93A2FF; --ind-soft:#232A47; --code-bg:#212B33; --head:#BFE6DC;
  }
}
:root[data-theme="dark"]{
  --paper:#12181D; --card:#1A222A; --ink:#E4EAE7; --mut:#98A4AC; --line:#2B353D;
  --acc:#4CC2AD; --acc-soft:#17352F; --amb:#E3B341; --amb-soft:#332B14;
  --ind:#93A2FF; --ind-soft:#232A47; --code-bg:#212B33; --head:#BFE6DC;
}
*{box-sizing:border-box}
body{margin:0;background:var(--paper);color:var(--ink);
  font:400 16px/1.65 "Be Vietnam Pro",-apple-system,"Segoe UI",Roboto,Arial,sans-serif;
  -webkit-font-smoothing:antialiased}
.wrap{max-width:920px;margin:0 auto;padding:40px 22px 72px}
h1,h2,h3{font-family:"Archivo","Be Vietnam Pro",Arial,sans-serif;line-height:1.25;text-wrap:balance;color:var(--ink)}
h1{font-size:clamp(26px,4.2vw,38px);font-weight:800;margin:10px 0 6px;letter-spacing:-.01em}
h2{font-size:clamp(20px,3vw,26px);font-weight:700;margin:52px 0 14px;padding-top:22px;border-top:1px solid var(--line)}
h3{font-size:18px;font-weight:700;margin:32px 0 8px}
p{margin:10px 0;max-width:74ch}
.eyebrow{font:600 12px/1.4 "IBM Plex Mono",ui-monospace,monospace;letter-spacing:.14em;text-transform:uppercase;color:var(--acc)}
.meta{color:var(--mut);font-size:14px;margin:2px 0 0}
.lede{font-size:17px;color:var(--ink);border-left:3px solid var(--acc);
  background:var(--card);padding:14px 18px;border-radius:0 10px 10px 0;margin:22px 0;max-width:none}
.lede p{max-width:none}
code,.mono{font-family:"IBM Plex Mono",ui-monospace,SFMono-Regular,Consolas,monospace;font-size:.92em}
code{background:var(--code-bg);padding:1px 5px;border-radius:5px;white-space:nowrap}
.tw{overflow-x:auto;margin:14px 0;border:1px solid var(--line);border-radius:10px;background:var(--card)}
table{border-collapse:collapse;width:100%;font-size:14.5px;font-variant-numeric:tabular-nums}
th{font:600 12px/1.4 "Be Vietnam Pro",sans-serif;letter-spacing:.06em;text-transform:uppercase;color:var(--mut);
  text-align:left;padding:10px 12px;border-bottom:1px solid var(--line);background:var(--code-bg)}
td{padding:9px 12px;border-bottom:1px solid var(--line);vertical-align:top}
tr:last-child td{border-bottom:none}
.chip{display:inline-block;font:500 12.5px/1 "IBM Plex Mono",monospace;padding:4px 8px;border-radius:999px;
  border:1px solid var(--line);color:var(--mut);white-space:nowrap}
.badge{display:inline-block;font:600 12px/1 "IBM Plex Mono",monospace;padding:4px 8px;border-radius:6px;white-space:nowrap}
.badge.a{background:var(--acc-soft);color:var(--acc)}
.badge.b{background:var(--amb-soft);color:var(--amb)}
.badge.ab{background:var(--ind-soft);color:var(--ind)}
.famhead{display:flex;align-items:baseline;gap:12px;flex-wrap:wrap;margin:44px 0 4px}
.famhead .fcode{font:700 15px/1 "IBM Plex Mono",monospace;padding:7px 10px;border-radius:8px}
.famhead h3{margin:0;font-size:19px}
.famhead .tag{color:var(--mut);font-style:italic}
.next{color:var(--mut);font-size:14.5px;margin:6px 0 10px}
.next b{color:var(--ink)}
.chainbox{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:16px 18px;margin:18px 0}
.chain{display:flex;flex-wrap:wrap;align-items:center;gap:7px;margin:8px 0}
.chain .lab{font:600 11.5px/1.3 "IBM Plex Mono",monospace;letter-spacing:.1em;text-transform:uppercase;
  min-width:64px;color:var(--mut)}
.node{font:500 13px/1.35 "Be Vietnam Pro",sans-serif;padding:5px 10px;border-radius:8px;border:1px solid var(--line)}
.node b{font-family:"IBM Plex Mono",monospace;font-weight:600}
.node.a{border-color:var(--acc);color:var(--acc)}
.node.b{border-color:var(--amb);color:var(--amb)}
.node.ab{border-color:var(--ind);color:var(--ind);border-style:dashed}
.arr{color:var(--mut)}
.toc{display:flex;flex-wrap:wrap;gap:8px;margin:20px 0 0}
.toc a{font:500 13.5px/1.3 "Be Vietnam Pro",sans-serif;color:var(--acc);text-decoration:none;
  border:1px solid var(--line);border-radius:999px;padding:6px 12px;background:var(--card)}
.toc a:hover{border-color:var(--acc)}
a{color:var(--acc)}
.note{color:var(--mut);font-size:13.5px}
.klist{margin:10px 0 10px 0;padding-left:22px}
.klist li{margin:7px 0;max-width:72ch}
footer{margin-top:56px;padding-top:18px;border-top:1px solid var(--line);color:var(--mut);font-size:13.5px}
:focus-visible{outline:2px solid var(--acc);outline-offset:2px}
@media (prefers-reduced-motion: reduce){*{scroll-behavior:auto!important}}
"""

def track(f): return "ab" if f == "AB" else ("a" if f.startswith("A") else "b")

def type_cell(tp):
    return f'<span class="chip" title="{esc(("Project môn học","Thực tập","Đồ án tốt nghiệp","Nghiên cứu")[("P","I","T","R").index(tp)])}">{tp}</span>'

B = io.StringIO(); w = B.write

w('<header>')
w('<div class="eyebrow">Engineering &amp; Research Mentoring Program · Lucero</div>')
w(f'<h1>Bản đồ {NTOP} đề tài &amp; cách sử dụng hệ thống</h1>')
w(f'<p class="meta">Phiên bản hệ thống {VER} · {UPD} · ThS. Đinh Văn Nam (Mr. Lucero Dinh) — Khoa Điện–Điện tử, Trường Kỹ thuật, Đại học Phenikaa · <a href="https://claude.ai/code/artifact/68a2de47-bc1e-41cc-b588-cd34ffd90c90">bản web</a></p>')
w('<div class="lede"><p>Đây là chương trình <strong>dài hạn, nhiều học kỳ</strong> — quản lý NCKH, luận án, thực tập và mentor cộng đồng IC design; mỗi học kỳ chạy một cohort (hiện tại: DATN HK1 2026-2027).</p></div>')
w(f'<div class="lede" style="margin-top:10px"><p>Tài liệu này trả lời hai câu hỏi bằng ngôn ngữ đời thường: <strong>mỗi đề tài trong {NTOP} đề tài thực chất là làm cái gì</strong>, và <strong>anh dùng kho đề tài này thế nào cho ba việc: giảng dạy – mentor – nghiên cứu</strong>. Đây là bản diễn giải của nguồn chuẩn <code>06_Data/project_portfolio.json</code>; khi lệch nhau, JSON thắng.</p></div>')
w('<nav class="toc" aria-label="Mục lục">')
for hid, lab in [("s1","1 · Bức tranh lớn"),("s2",f"2 · Đi một vòng {NFAM} nhóm"),("s3","3 · Bốn cách sử dụng"),("s4","4 · Chọn đề tài 4 bước"),("s5","5 · Mở gì khi nào")]:
    w(f'<a href="#{hid}">{lab}</a>')
w('</nav></header>')

# ---------- 1 ----------
w('<h2 id="s1">1 · Bức tranh lớn trong một phút</h2>')
w('<p>Kho đề tài là một <strong>tấm bản đồ hai trục, bốn bậc thang</strong>. Trục A dạy nghề <strong>làm chip số</strong> — và từ v1.5.0 mở rộng thêm nhánh <strong>Nhúng &amp; IoT</strong> (A6, A7); trục B đi sâu một chủ đề nghiên cứu — <strong>giải mã Polar</strong>; vùng AB nối các trục lại thành nghiên cứu co-design đúng nghĩa, theo định hướng luận án của mentor.</p>')
w('<div class="chainbox">')
w('<div class="chain"><span class="lab">Trục A</span>')
A_SHORT = {"A0":"hàn mạch thật","A1":"Verilog","A2":"mạch làm toán","A3":"FPGA","A4":"ra chip (GDSII)","A5":"hạ tầng kiểm chứng"}
for i,f in enumerate(CHAIN_A):
    if i: w('<span class="arr">→</span>')
    w(f'<span class="node a"><b>{f}</b> {esc(A_SHORT[f])}</span>')
w('</div><div class="chain"><span class="lab">Nhúng-IoT</span>')
A2_SHORT = {"A6":"nhúng / SoC","A7":"IoT & AI biên"}
for i,f in enumerate(CHAIN_A2):
    if i: w('<span class="arr">→</span>')
    w(f'<span class="node a"><b>{f}</b> {esc(A2_SHORT[f])}</span>')
w('<span class="arr note">(mở từ v1.5.0)</span>')
w('</div><div class="chain"><span class="lab">Trục B</span>')
B_SHORT = {"B0":"mô phỏng","B1":"viên gạch RTL","B2":"bộ giải mã SC","B3":"bao nhiêu bit?","B4":"SC-Flip","B5":"thích ứng","B6":"AI hỗ trợ"}
for i,f in enumerate(CHAIN_B):
    if i: w('<span class="arr">→</span>')
    w(f'<span class="node b"><b>{f}</b> {esc(B_SHORT[f])}</span>')
w('</div><div class="chain"><span class="lab">Gặp nhau</span>')
w('<span class="node ab"><b>AB</b> co-design: Polar / edge-AI đo bằng thước phần cứng — định hướng luận án</span>')
w('</div></div>')
w('<p>Mỗi nhóm có tối đa 4 loại hoạt động, xếp như <strong>bậc thang trách nhiệm</strong> — cùng một chủ đề nhưng đòi hỏi tăng dần:</p>')
w('<div class="tw"><table><thead><tr><th>Bậc</th><th>Loại</th><th>Bản chất</th><th>Câu hỏi định nghĩa</th></tr></thead><tbody>')
for row in [
 ("1",f"P — Project môn học <span class='note'>({NTYPE[chr(80)]} đề tài)</span>","<em>Học</em> một kỹ năng cụ thể; không cần tính mới","“Em đã làm được kỹ năng X chưa?”"),
 ("2",f"I — Thực tập <span class='note'>({NTYPE[chr(73)]})</span>","<em>Tập làm việc</em> theo quy trình kỹ sư thật","“Em làm việc có kỷ luật kỹ thuật chưa?”"),
 ("3",f"T — Đồ án tốt nghiệp <span class='note'>({NTYPE[chr(84)]})</span>","<em>Sở hữu</em> một sản phẩm trọn vẹn: đúng, đủ, tái lập được, có số liệu","“Đây có phải sản phẩm hoàn chỉnh của riêng em?”"),
 ("4",f"R — Nghiên cứu <span class='note'>({NTYPE[chr(82)]})</span>","<em>Trả lời câu hỏi chưa có đáp án</em>; chấp nhận kết quả phủ định","“Em đã chứng minh/bác bỏ giả thuyết bằng bằng chứng chưa?”"),
]:
    w(f'<tr><td>{row[0]}</td><td><strong>{row[1]}</strong></td><td>{row[2]}</td><td>{row[3]}</td></tr>')
w('</tbody></table></div>')
w('<p>Kèm theo là <strong>thang trưởng thành L0–L5</strong> của sinh viên (L0 mới khám phá → L5 sẵn sàng nghiên cứu nâng cao). Mỗi đề tài ghi một mức <strong>sàn</strong>: dưới sàn vẫn có thể nhận, nhưng phải ghi lý do và thu hẹp phạm vi.</p>')

# ---------- 2 ----------
w(f'<h2 id="s2">2 · Đi một vòng {NFAM} nhóm — mỗi đề tài làm ra cái gì</h2>')
w('<p class="note">Cách đọc bảng: <strong>Mã chuẩn</strong> là định danh vĩnh viễn; cột <strong>HK1</strong> là mã rút gọn sinh viên thấy trong danh mục DATN kỳ này (chỉ 21 đề tài T đang mở); <strong>Sàn</strong> là level tối thiểu nên có; <strong>Làm ra</strong> tóm tắt sản phẩm nộp được, lấy nguyên từ nguồn chuẩn.</p>')
for f in CHAIN_A + CHAIN_A2 + CHAIN_B + ["AB"]:
    fd = FAM[f]; tag, body, nxt = BLURB[f]; tr = track(f)
    w(f'<div class="famhead"><span class="fcode badge {tr}">{f}</span><h3 id="f{f}">{esc(fd["name_vi"])} — {esc(tag)}</h3></div>')
    w(f'<p>{esc(body)}</p><p class="next"><b>Đi tiếp:</b> {esc(nxt)}</p>')
    w('<div class="tw"><table><thead><tr><th>Mã</th><th>Loại</th><th>Sàn</th><th>HK1</th><th>Đề tài</th><th>Làm ra</th></tr></thead><tbody>')
    for t in fam_topics(f):
        al = ALIAS.get(t["code"])
        alcell = f'<span class="badge {tr}">{al}</span>' if al else '<span class="note">—</span>'
        w(f'<tr><td><code>{t["code"]}</code></td><td>{type_cell(t["type"])}</td><td class="mono">L{t["min_level"]}</td><td>{alcell}</td>'
          f'<td>{esc(t["title_vi"])}</td><td class="note">{esc(trim(t.get("outputs"),130))}</td></tr>')
    w('</tbody></table></div>')

# ---------- 3 ----------
w('<h2 id="s3">3 · Bốn cách anh dùng kho đề tài này</h2>')
w('<h3>3.1 · Giảng dạy — loại P trong môn học</h3>')
w('<p>Đề tài P là <strong>bài thực hành lớn có chuẩn đầu ra sẵn</strong>: mỗi đề tài ghi rõ đầu vào cần gì, sản phẩm nộp gì, dùng công cụ nào.</p>')
w('<ul class="klist"><li>Chọn đề tài P có sàn level khớp trình độ lớp — ví dụ lớp mới học HDL: <code>A1-P01</code>/<code>A1-P02</code> (sàn L0).</li>'
  '<li>Cột <strong>Làm ra</strong> của đề tài chính là barem nộp bài — không phải soạn lại yêu cầu mỗi học kỳ.</li>'
  '<li>Sinh viên khá làm phần <em>mở rộng</em> ghi sẵn trong đề tài để lấy điểm cộng.</li>'
  '<li>Nhiều em cùng hổng một kỹ năng → mở <strong>bootcamp chung</strong> một buổi (danh mục kỹ năng: <code>10_Documentation/MENTOR-GUIDE.md</code> §8) thay vì giảng lại 1-1.</li></ul>')
w('<p><em>Ví dụ:</em> giao <code>A1-P04</code> (UART) cho môn Thiết kế số — tuần 1 viết transmitter + testbench, tuần 2 receiver + loopback, tuần 3 nộp repo có README và waveform chứng minh. Chuẩn chấm nằm sẵn trong danh mục.</p>')
w('<h3>3.2 · Thực tập — loại I, cửa bắt buộc trước đồ án</h3>')
w('<p>Đề tài I là nơi sinh viên tập <em>tác phong</em>: Git đúng cách, báo cáo tuần, làm theo quy trình — sản phẩm kỹ thuật chỉ là phương tiện. Mỗi trục có đề tài I ở mọi tầng (<code>A0-I01</code> làm phần cứng thật, <code>A5-I01</code> dựng Git workflow, <code>B0-I01</code> xây bộ mô phỏng tái lập…), nên em nào cũng chọn được kỳ thực tập vừa sức mà vẫn nằm đúng hướng nghề định theo.</p>')
w('<h3>3.3 · Mentor đồ án tốt nghiệp — loại T, 15 tuần, 6 trạm kiểm soát</h3>')
w(f'<p>Khuôn {NW} tuần – 6 trạm này <strong>dùng chung cho mọi khóa</strong>: các mốc đếm theo số tuần kể từ ngày sinh viên chính thức nhận đề tài, không gắn với một học kỳ cụ thể. '
  + (f'Khóa đang chạy ({NOPEN} đề tài mở) bắt đầu {cs.dmy(CAL[0]["start"])}, nên cột hạn có kèm ngày tương ứng. ' if CAL else f'Khóa đang chạy ({NOPEN} đề tài mở) chưa công bố ngày bắt đầu, nên chỉ hiện mốc tuần. ')
  + 'Kể bằng một ví dụ giả định — bạn <strong>Minh</strong> chọn <code>A4-T01</code> <em>(mã HK1: A1 — Thiết kế một Digital IP từ RTL đến GDSII)</em>:</p>')
w('<div class="tw"><table><thead><tr><th>Trạm</th><th>Tuần · hạn</th><th>Minh phải cho xem</th><th>Anh làm gì</th></tr></thead><tbody>')
import html as _h, re as _re
def _md2html(t):
    t = _h.escape(t)
    t = _re.sub(r"\*\*(.+?)\*\*", r"<strong>\\1</strong>", t)
    t = _re.sub(r"\*(.+?)\*", r"<em>\\1</em>", t)
    t = _re.sub(r"`(.+?)`", r"<code>\\1</code>", t)
    return t
GATE_ROWS = [(f"Gate {g['gate']} · {GATE_SHORT[g['gate']]}",
              f"{_h.escape(cs.week_label(g))} · <b>{_h.escape(cs.due_compact(g, DL))}</b>",
              _md2html(GATE_TEXT[g["gate"]][0]), _md2html(GATE_TEXT[g["gate"]][1]))
             for g in G["gates"]]
for r in GATE_ROWS:
    w(f'<tr><td><strong>{r[0]}</strong></td><td class="mono">{r[1]}</td><td>{r[2]}</td><td>{r[3]}</td></tr>')
w('</tbody></table></div>')
w('<p>Giữa các trạm là <strong>nhịp tuần</strong> ~30 phút/sinh viên: đọc báo cáo tuần trước buổi gặp → trong buổi em trình theo khung <em>Mục tiêu → Bằng chứng → Cái gì hỏng → Chẩn đoán → Bước tiếp</em> → chốt 1–3 việc có hạn → ghi vào workbook. Thao tác chi tiết từng buổi: <code>10_Documentation/MENTOR-GUIDE.md</code>.</p>')
w('<p>Sức mạnh của cách chạy này: <strong>mọi sinh viên cùng đi qua 6 trạm giống nhau</strong>, nên anh mentor 10 em cùng lúc vẫn nhìn được toàn cảnh trong một sheet — ai xanh ai đỏ, ai sắp đến trạm nào.</p>')
w('<h3>3.4 · Nghiên cứu — loại R và con đường lên bài báo</h3>')
w('<p>Hệ thống tạo nghiên cứu theo <strong>hai cửa</strong>:</p>')
w('<ul class="klist"><li><strong>Cửa extension</strong> (phổ biến nhất): làm đồ án T vững, qua Gate 2 đúng hạn → được mở phần mở rộng có chất nghiên cứu. Ví dụ <code>B4-T01</code> (SC-Flip) xong phần lõi → extension “cải tiến thước đo độ tin cậy” → kết quả tốt là hạt nhân một bài báo. Extension thất bại <strong>không</strong> làm hỏng đồ án — phần lõi vẫn tự đứng.</li>'
  '<li><strong>Cửa đề tài R</strong> (10 đề tài, sàn L4–L5): cho sinh viên đã chứng minh năng lực, thường là em đã làm T kỳ trước. Đề tài R chấp nhận <em>kết quả phủ định</em> — giả thuyết sai nhưng thí nghiệm sạch vẫn là nghiên cứu đạt.</li></ul>')
w('<p>Nhìn xa hơn một học kỳ, trục B là <strong>một chương trình nghiên cứu nhiều thế hệ</strong>: em khóa này làm B2 (bộ giải mã nền) để lại gói bàn giao; em khóa sau đứng trên đó làm B4/B5; em giỏi nhất chạm B6 và AB. Mỗi đồ án bắt buộc để lại <strong>Legacy Package</strong> — kho của anh giàu lên sau mỗi khóa thay vì làm lại từ đầu.</p>')
w('<p><strong>Con đường lên luận án của mentor</strong> (mở từ v1.5.0) chạy qua đúng các bậc thang này: vững nhúng/AI biên (<code>A6-T02</code>, <code>A7-T02</code>) hoặc Polar hardware (<code>B2-T01</code>, <code>B3-T01</code>) → đề tài co-design (<code>AB-T05</code> tăng tốc AI biên trên SoC FPGA, <code>AB-T06</code> decoder Polar tiết kiệm năng lượng cho IoT) → đề tài nghiên cứu (<code>AB-R02</code> co-design truyền thông tin cậy ở biên, <code>AB-R03</code> nền tảng biên tích hợp truyền thông + suy luận). Mỗi tầng để lại baseline và số liệu cho tầng sau — nhiều sinh viên, nhiều học kỳ, cùng bồi vào một hướng nghiên cứu.</p>')

# ---------- 4 ----------
w('<h2 id="s4">4 · Sinh viên mới đến — chọn đề tài trong 4 bước</h2>')
w('<ul class="klist">'
  '<li><strong>Hỏi đích đến nghề nghiệp</strong> rồi tra bảng dưới → ra 2–3 ứng viên đề tài.</li>'
  '<li><strong>So level</strong>: em tự chấm + anh kiểm chứng qua bài thử việc (readiness test) → so với sàn của đề tài.</li>'
  '<li><strong>So đầu vào</strong>: mỗi đề tài ghi mã tham chiếu — <code>A1-P*</code> nghĩa là <em>đã làm ít nhất một project A1, hoặc tương đương có bằng chứng</em>.</li>'
  '<li><strong>Chốt phạm vi</strong>: nguyện vọng quyết định <em>hướng</em>, mức sẵn sàng quyết định <em>độ lớn</em> — nhận / nhận có điều kiện / đổi đề tài.</li></ul>')
w('<div class="tw"><table><thead><tr><th>Đích đến của em</th><th>Đề tài chính</th><th>Bước tiếp theo</th></tr></thead><tbody>')
for cg in C["career_guide"]:
    note = f' <span class="note">({esc(cg["note"])})</span>' if cg.get("note") else ""
    pri = " · ".join(f'<code>{esc(x)}</code>' for x in cg["primary"])
    nxt = " · ".join(f'<code>{esc(x)}</code>' for x in cg["next"])
    w(f'<tr><td><strong>{esc(cg["goal"])}</strong>{note}</td><td>{pri}</td><td>{nxt}</td></tr>')
w('<tr><td><strong>Embedded &amp; IoT engineer</strong> <span class="note">(nhánh mở từ v1.5.0)</span></td><td><code>A6-T01</code> · <code>A7-T01</code> · <code>A7-T02</code></td><td><code>A6-T02</code> · <code>AB-T05</code> · <code>A6-R01</code> · <code>A7-R01</code></td></tr>')
w('<tr><td><strong>Algorithm–hardware co-design</strong> <span class="note">(định hướng luận án)</span></td><td><code>A6-T02</code> · <code>AB-T05</code> · <code>AB-T06</code></td><td><code>AB-R02</code> · <code>AB-R03</code></td></tr>')
w('</tbody></table></div>')

# ---------- 5 ----------
w('<h2 id="s5">5 · Mở gì, khi nào</h2>')
w('<div class="tw"><table><thead><tr><th>Tình huống</th><th>Mở</th></tr></thead><tbody>')
for a,b in [
 ("Cần thao tác từng buổi gặp / gate / xử lý SV chậm","<code>10_Documentation/MENTOR-GUIDE.md</code>"),
 ("Phát tài liệu cho sinh viên","<code>Danh_muc_de_tai_DATN_Nhom_A_B_HK1_2026_2027.docx/.pdf</code> + <code>Phieu_lua_chon_va_danh_gia_de_tai_DATN_HK1_2026_2027.docx</code> (thư mục gốc)"),
 ("Theo dõi cả lớp hằng tuần","<code>03_Operations/Mentoring_Management_Workbook.xlsx</code>"),
 ("Sửa đề tài / thang điểm / lịch","<code>06_Data/*.json</code> rồi chạy 3 lệnh trong <code>10_Documentation/WORKFLOW.md</code>"),
 ("Hiểu kiến trúc &amp; quyết định thiết kế","<code>implementation-notes.md</code> / <code>.html</code>"),
 ("Triết lý giáo dục gốc","<code>01_Governance/Master_Mentoring_Handbook.docx</code>"),
]:
    w(f'<tr><td>{a}</td><td>{b}</td></tr>')
w('</tbody></table></div>')
w(f'<footer>Sinh từ nguồn chuẩn v{VER} ({UPD}, <code>06_Data/</code>) bằng <code>scripts/generate_ban_do.py</code> — dữ liệu đổi thì chạy lại script để bản đồ luôn khớp nguồn. · Engineering &amp; Research Mentoring Program (Lucero)</footer>')

BODY = B.getvalue()
FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@600;700;800&family=Be+Vietnam+Pro:ital,wght@0,400;0,500;0,600;0,700;1,400&family=IBM+Plex+Mono:wght@400;500;600&display=swap">'

# Bản đứng độc lập (mở từ máy anh)
full = ("<!doctype html>\n<html lang=\"vi\">\n<head>\n<meta charset=\"utf-8\">\n"
        "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n"
        "<title>Bản đồ đề tài Lucero</title>\n" + FONTS + "\n<style>" + CSS + "</style>\n</head>\n<body>\n"
        "<div class=\"wrap\">\n" + BODY + "\n</div>\n</body>\n</html>\n")
io.open(str(OUT / "Ban_do_de_tai.html"), "w", encoding="utf-8").write(full)

# Bản artifact (không doctype/head/body)
art = ("<title>Bản đồ đề tài Lucero</title>\n" + FONTS + "\n<style>" + CSS + "\nbody{background:var(--paper)}</style>\n"
       "<div class=\"wrap\">\n" + BODY + "\n</div>\n")
(OUT / "build").mkdir(exist_ok=True)
io.open(str(OUT / "build" / "ban_do_artifact.html"), "w", encoding="utf-8").write(art)
print("HTML OK:", len(full), "| artifact:", len(art))
