#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sinh các view từ nguồn chuẩn 06_Data/ — KHÔNG sửa tay file sinh ra.

Outputs (build/):
  Master_Project_Portfolio_AB.md
  Course_Project_Catalog.md / Internship_Catalog.md /
  Graduation_Thesis_Catalog.md / Research_Opportunities_Catalog.md
  Danh_muc_de_tai_DATN_<cohort>.md (+ .html để in PDF)
  Phieu_lua_chon_va_danh_gia_de_tai_DATN_<cohort>.md

Cờ dòng lệnh:
  --docx  pandoc xuất .docx vào vị trí chuẩn (02_Project_Portfolio/ và thư mục gốc
          cho tài liệu cohort).
  --pdf   pandoc xuất HTML rồi in PDF bằng Chromium/Chrome/Edge headless (danh mục
          cohort ở thư mục gốc). Đặt CHROME_BIN nếu trình duyệt không nằm trên PATH.

Chạy validate trước khi generate. Chỉ dùng stdlib + pandoc (+ trình duyệt cho --pdf).
"""
import json, os, pathlib, subprocess, sys, html

BASE = pathlib.Path(__file__).resolve().parents[1]
DATA, BUILD = BASE/"06_Data", BASE/"build"
BUILD.mkdir(exist_ok=True)

pf = json.loads((DATA/"project_portfolio.json").read_text(encoding="utf-8"))
rr = json.loads((DATA/"readiness_rubrics.json").read_text(encoding="utf-8"))
mg = json.loads((DATA/"milestone_gates.json").read_text(encoding="utf-8"))
COHORT_FILES = sorted(DATA.glob("cohort_*.json"))

META    = pf["meta"]
FAMS    = pf["families"]
LEVELS  = pf["levels"]
TYPES   = pf["types"]
TOPICS  = pf["topics"]
BYCODE  = {t["code"]: t for t in TOPICS}
VERSION, UPDATED = META["version"], META["updated"]
PROGRAM, AUTHOR  = META["program"], META["author"]

GEN_NOTE = ("*File này được sinh tự động từ `06_Data/` (scripts/generate_catalogs.py). "
            "KHÔNG sửa tay — mọi thay đổi phải sửa nguồn chuẩn rồi generate lại.*")

def lv(n): return f"L{n} - {LEVELS[str(n)]}"
def type_label(t): return TYPES[t][0]
def difficulty(ml): return {0:"Cơ bản",1:"Cơ bản",2:"Trung bình",3:"Trung bình–khá",4:"Khá–cao",5:"Cao"}[ml]
def star(s):
    """Escape dấu '*' trong văn bản lấy nguyên văn từ nguồn chuẩn.

    Dữ liệu nguồn dùng '*' làm ký tự wildcard (pattern 'A1-P*'), trùng với cú pháp
    nhấn mạnh của Markdown. Không escape thì pandoc nuốt mất ký tự và làm lệch cả
    phần in nghiêng bao quanh.
    """
    return (s or "").replace("*", r"\*")

def esc(s): return star(s).replace("|", "/").replace("\n", " ").strip()

def prereq_ref(t):
    """Render prereq_codes an toàn cho Markdown.

    Mã pattern wildcard (vd 'A1-P*') chứa dấu '*'. Nếu nội suy thẳng vào cụm in
    nghiêng '*(...)*' thì pandoc đóng emphasis ngay tại dấu '*' của mã, làm mất
    ký tự wildcard và để lại một dấu '*' lạc không có chú giải. Bọc từng mã vào
    code span để dấu '*' được giữ nguyên văn.
    """
    codes = t.get("prereq_codes") or []
    if not codes: return ""
    return " *(mã tham chiếu: " + ", ".join(f"`{c}`" for c in codes) + ")*"

PREREQ_NOTE = f"*Quy ước mã tham chiếu: {star(META['prereq_codes_convention'])}*"

def header(title, subtitle=""):
    out = [f"# {title}", ""]
    if subtitle: out += [f"**{subtitle}**", ""]
    out += [f"{PROGRAM} · Phiên bản {VERSION} · {UPDATED}", "",
            f"Tác giả: {AUTHOR}", "", GEN_NOTE, "", "---", ""]
    return out

GUIDE = ["## Hướng dẫn lựa chọn", "",
 "- Sinh viên nộp Top 3 nguyện vọng; mentor chốt đề tài sau readiness test.",
 "- Đề tài level cao không được chọn chỉ vì “nghe hay”. Phải đủ prerequisite và WR/RR.",
 "- Với DATN/NCKH: baseline là điều kiện bắt buộc trước extension/novelty.",
 "- Mỗi đề tài phải có evidence và Project Legacy Package.", ""]

def family_block(fam):
    f = FAMS[fam]
    return [f"## {fam} - {star(f['name_vi'])}", "",
            f"**Mục tiêu:** {star(f['purpose'])}", "",
            f"**Điều kiện nền:** {star(f['min_skills'])}", "",
            f"**Công cụ gợi ý:** {star(f['default_tools'])}", ""]

def topic_table(rows):
    out = ["| Mã | Đề tài | Loại | Level | Điều kiện tối thiểu | Sản phẩm chính |",
           "|---|---|---|---|---|---|"]
    for t in rows:
        out.append(f"| {t['code']} | {esc(t['title_vi'])} | {type_label(t['type'])} | "
                   f"{lv(t['min_level'])} | {esc(t['prerequisites'])} | {esc(t['outputs'])} |")
    return out + [""]

def topic_detail(t, show_mvt=True):
    out = [f"### {t['code']} - {star(t['title_vi'])}", "",
           f"**English:** {star(t['title_en'])}", "",
           f"**Scope:** {star(t['scope'])}", "",
           f"**Prerequisites:** {star(t['prerequisites'])}"]
    out[-1] += prereq_ref(t)
    out += ["", f"**Deliverables:** {star(t['outputs'])}", ""]
    if show_mvt and t.get("mvt"):
        out += [f"**MVT (phần bắt buộc):** {star(t['mvt'])}", ""]
    out += [f"**Extension:** {star(t['extension'])}", "",
            f"**Công cụ:** {star(t['tools'])}", "",
            f"**Định hướng nghề nghiệp:** {star(t['career_relevance'])}", ""]
    if t.get("eligibility"):
        out += [f"**Điều kiện cứng:** {star(t['eligibility'])}", ""]
    return out

LEVEL_TABLE = ["## Điều kiện chung theo level", "",
 "| Level | Ý nghĩa | Gợi ý hoạt động |", "|---|---|---|",
 "| L0 | Explorer | A0/A1/B0 course project nhỏ. |",
 "| L1 | Beginner Engineer | Project/Internship có cấu trúc. |",
 "| L2 | Independent Engineering Student | Engineering thesis và system integration. |",
 "| L3 | Research-Ready Undergraduate | DATN có experiment/research orientation. |",
 "| L4 | Undergraduate Researcher | NCKH có research question; một số DATN advanced (B6/AB) cũng yêu cầu L4. |",
 "| L5 | Advanced Research Student | B6/AB co-design/advanced research. |", ""]

FAM_ORDER = ["A0","A1","A2","A3","A4","A5","A6","A7","B0","B1","B2","B3","B4","B5","B6","AB"]

# ---------------- master ----------------
def gen_master():
    out = header("Master Project Portfolio A/B/AB",
                 "Electronic Hardware → Digital Design → FPGA → ASIC | Hardware-Aware Polar Decoding")
    out += ["> Master Portfolio là nguồn tham chiếu chuyên môn đầy đủ. Sinh viên chỉ nên được xem "
            "catalog phù hợp với giai đoạn P/I/T/R và readiness của mình.", "",
            PREREQ_NOTE, ""]
    out += GUIDE
    for fam in FAM_ORDER:
        rows = [t for t in TOPICS if t["family"] == fam]
        out += family_block(fam) + topic_table(rows)
        for t in rows: out += topic_detail(t)
    out += LEVEL_TABLE
    return "\n".join(out)

# ---------------- P/I/T/R views ----------------
CAT_TITLES = {
 "P": ("Danh mục Project môn học", "Học kỹ năng và tạo engineering evidence", False, False),
 "I": ("Danh mục Thực tập", "Thực hành engineering workflow chuyên nghiệp", False, False),
 "T": ("Danh mục Đồ án tốt nghiệp", "Correct + complete + reproducible + quantitatively evaluated", True, True),
 "R": ("Danh mục Nghiên cứu khoa học", "Research question + baseline + evidence + phân tích", True, False),
}
def gen_catalog(typ):
    title, subtitle, detail, show_mvt = CAT_TITLES[typ]
    out = header(title, subtitle)
    out += [f"> View này chỉ hiển thị **{typ} = {type_label(typ)}**. Dữ liệu gốc nằm trong "
            "`06_Data/project_portfolio.json`; không quản lý catalog như danh sách độc lập.", ""]
    out += [PREREQ_NOTE, ""]
    out += GUIDE
    for fam in FAM_ORDER:
        rows = [t for t in TOPICS if t["family"] == fam and t["type"] == typ]
        if not rows: continue
        out += family_block(fam) + topic_table(rows)
        if detail:
            for t in rows: out += topic_detail(t, show_mvt=show_mvt)
    if not detail:
        out += ["*(View rút gọn theo thiết kế: chi tiết scope/extension/MVT xem Master Portfolio "
                "hoặc catalog T/R tương ứng.)*", ""]
    out += LEVEL_TABLE
    return "\n".join(out)

# ---------------- cohort catalog ----------------
def gen_cohort(co):
    cid = co["cohort_id"]
    label = cid.replace("HK1_", "HK1 ").replace("_", "-")
    out = header("Danh mục đề tài Đồ án tốt nghiệp",
                 f"Nhóm A - Digital IC / FPGA / ASIC · Nhóm B - Polar Code / Hardware-Aware Decoding · {label}")
    out += [
            "> **Mục tiêu tài liệu:** giúp sinh viên quan sát nhanh các hướng đề tài, hiểu yêu cầu đầu vào, "
            "sản phẩm bắt buộc (MVT) và lựa chọn phù hợp năng lực, sở thích, định hướng nghề nghiệp.", "",
            "**Quy ước mã:** mỗi đề tài có **mã chuẩn** dạng `Family-TypeNN` (vd `A4-T01`) dùng trong mọi hồ sơ/tracker, "
            f"kèm **mã ngắn cohort** (vd `A1`) chỉ để đọc nhanh trong kỳ {label}. Khi điền phiếu, ghi **mã chuẩn**.", "",
            PREREQ_NOTE, "",
            "## 1. Thông tin chung", ""]
    out += ["**Cách chọn đề tài:** (1) xác định hướng ưu tiên A hay B → (2) đối chiếu kiến thức đầu vào với mô tả đề tài → "
            "(3) chọn 3 nguyện vọng theo thứ tự (ghi mã chuẩn) → (4) hoàn thành readiness test → (5) làm việc theo milestone "
            "và evidence hằng tuần.", ""]
    # 15-week process from gates + cohort deadlines
    out += ["## 2. Quy trình 15 tuần và deadline gate", "",
            "| Gate | Tuần | Hạn chót | Điều kiện qua | Nếu không đạt |", "|---|---|---|---|---|"]
    for g in mg["gates"]:
        dl = co["gate_deadlines"][str(g["gate"])]
        out.append(f"| {g['name']} | {g['weeks_label']} | {dl} | {esc(g['pass_criteria'])} | {esc(g['fail_rule'])} |")
    out += ["", "**Nguyên tắc evidence:** không coi “đã đọc/tìm hiểu” là tiến độ nếu chưa có sản phẩm "
            "quan sát được (code, waveform, log, figure, bảng kết quả, technical note, demo).", ""]
    # quick tables
    def quick_table(group):
        rows = [x for x in co["topics"] if x["alias"].startswith(group)]
        rows.sort(key=lambda x: int(x["alias"][1:]))
        tb = ["| Mã ngắn | Mã chuẩn | Đề tài | Độ khó | Đầu vào chính | Công cụ |", "|---|---|---|---|---|---|"]
        for x in rows:
            t = BYCODE[x["code"]]
            tb.append(f"| {x['alias']} | **{t['code']}** | {esc(t['title_vi'])} | {difficulty(t['min_level'])} | "
                      f"{esc(t['prerequisites'])} | {esc(t['tools'])} |")
        return tb + [""]
    out += ["## 3. Bảng lựa chọn nhanh", "", "### Nhóm A - Digital IC / FPGA / ASIC", ""]
    out += quick_table("A")
    out += ["### Nhóm B - Polar Code / Hardware-Aware Decoding", ""]
    out += quick_table("B")
    # details
    for group, gname in [("A","4. NHÓM A - DIGITAL IC / FPGA / ASIC"),
                         ("B","5. NHÓM B - POLAR CODE / HARDWARE-AWARE DECODING")]:
        out += [f"## {gname}", ""]
        rows = [x for x in co["topics"] if x["alias"].startswith(group)]
        rows.sort(key=lambda x: int(x["alias"][1:]))
        for x in rows:
            t = BYCODE[x["code"]]
            out += [f"### {x['alias']} · {t['code']} — {star(t['title_vi'])}", "",
                    f"*{star(t['title_en'])}*", "",
                    f"**Độ khó:** {difficulty(t['min_level'])} · **Level tối thiểu:** {lv(t['min_level'])}", "",
                    f"**Đầu vào:** {star(t['prerequisites'])}" + prereq_ref(t), "",
                    f"**Phạm vi:** {star(t['scope'])}", "",
                    f"**Sản phẩm bắt buộc (MVT):** {star(t.get('mvt',''))}", "",
                    f"**Công cụ dự kiến:** {star(t['tools'])}", ""]
            if t.get("checkpoints_15w"):
                out += [f"**Checkpoint 15 tuần:** {star(t['checkpoints_15w'])}", ""]
            out += [f"**Research extension (không bắt buộc):** {star(t['extension'])}", "",
                    f"**Định hướng nghề nghiệp:** {star(t['career_relevance'])}", ""]
    # career guide
    out += ["## 6. Gợi ý chọn đề tài theo mục tiêu nghề nghiệp", "",
            "| Mục tiêu | Đề tài ưu tiên | Lộ trình tiếp theo |", "|---|---|---|"]
    for g in co["career_guide"]:
        note = f" *({star(g['note'])})*" if g.get("note") else ""
        out.append(f"| {g['goal']}{note} | {', '.join(g['primary'])} | {', '.join(g['next'])} |")
    out += ["", "## 7. Readiness test và nguyên tắc làm việc", "",
            "- **Literature task:** đọc một tài liệu ngắn; trình bày problem - input - output - method - metric - điểm chưa hiểu.",
            "- **Technical mini-task (4-10 giờ):** simulation nhỏ, module RTL, tái tạo figure hoặc xử lý dataset tùy đề tài.",
            "- **Oral check (5-10 phút):** trình bày bằng lời của chính mình; sản phẩm không giải thích được coi là chưa hoàn thành.",
            "",
            "Nguyên tắc: mentor chịu trách nhiệm scope/hướng kỹ thuật/milestone/quality control; sinh viên chịu trách nhiệm "
            "đọc, học, code, debug, experiment, deadline, báo cáo. Baseline chưa xong thì không mở research extension. "
            "Tiến độ không phù hợp giữa kỳ → ưu tiên giảm scope, giữ chuẩn kỹ thuật. AI được dùng để hỗ trợ nhưng "
            "**cannot explain = not completed**.", "",
            f"## 8. Phiếu đăng ký", "",
            f"Sử dụng file **Phieu_lua_chon_va_danh_gia_de_tai_DATN_{cid}.docx** (bản duy nhất, thang điểm chuẩn). "
            "Không dùng các bản phiếu cũ.", ""]
    return "\n".join(out)

# ---------------- phiếu (form) ----------------
def gen_phieu(co):
    cid = co["cohort_id"]; label = cid.replace("HK1_", "HK1 ").replace("_", "-")
    tr, wr, rz = rr["technical_readiness"], rr["working_readiness"], rr["research_readiness"]
    tr_max = max(int(k) for k in tr["scale"])
    out = header("Phiếu lựa chọn nguyện vọng & đánh giá readiness",
                 f"Đồ án tốt nghiệp {label} · Nhóm A - Digital IC/FPGA/ASIC · Nhóm B - Polar Code")
    out += ["> Sinh viên điền Phiếu 1-4 trước buổi trao đổi; mentor dùng Phiếu 5. "
            "Chọn đề tài dựa trên năng lực, định hướng và mức cam kết thực tế — không chỉ dựa trên tên đề tài. "
            "**Ghi mã chuẩn của đề tài (vd `A4-T01`).**", ""]
    out += ["## PHIẾU 1 - Thông tin & nguyện vọng", "",
            "| Mục | Thông tin |", "|---|---|",
            "| Họ và tên |  |", "| Mã sinh viên / Lớp |  |", "| Email / SĐT |  |",
            "| Mục tiêu nghề nghiệp 1-2 năm tới |  |", "| Thời gian có thể dành mỗi tuần |  |",
            "| Kinh nghiệm/project đã làm |  |", "",
            "| Nguyện vọng | Mã chuẩn đề tài | Tên đề tài | Vì sao phù hợp / mục tiêu muốn đạt |",
            "|---|---|---|---|", "| Top 1 |  |  |  |", "| Top 2 |  |  |  |", "| Top 3 |  |  |  |", ""]
    out += [f"## PHIẾU 2 - Technical Readiness (tự đánh giá 0-{tr_max})", "",
            "Thang: " + "; ".join(f"{k} = {v}" for k, v in tr["scale"].items()) + ".", "",
            f"| Năng lực | Điểm 0-{tr_max} | Bằng chứng/link nếu có |", "|---|---|---|"]
    out += [f"| {c} |  |  |" for c in tr["competencies"]]
    out += ["", f"*{star(tr['note'])}*", ""]
    out += ["## PHIẾU 3 - Cam kết thời gian & cách làm việc", "",
            "| Mục | Trả lời |", "|---|---|",
            "| Số giờ/tuần cam kết cho đồ án |  |",
            "| Khung thời gian làm việc cố định mỗi tuần |  |",
            "| Điểm mạnh có thể đóng góp |  |",
            "| Lỗ hổng kiến thức/kỹ năng cần bổ sung ngay |  |", "",
            "☐ Tôi xác nhận đã đọc mô tả đề tài và hiểu rằng kết quả đồ án phụ thuộc vào tiến độ "
            "và bằng chứng công việc hằng tuần.", ""]
    out += ["## PHIẾU 4 - Readiness test 2 tuần", "",
            "| Thành phần | Nhiệm vụ được giao | Evidence cần nộp | Deadline | Kết quả |", "|---|---|---|---|---|",
            "| Literature task |  | Problem/Input/Output/Method/Metric/Unknowns |  | ☐ Đạt ☐ Chưa đạt |",
            "| Technical mini-task (4-10h) |  | Code/schematic/simulation/measurement + README |  | ☐ Đạt ☐ Chưa đạt |",
            "| Oral check (5-10 phút) |  | Trình bày bằng lời của chính mình + Q&A |  | ☐ Đạt ☐ Chưa đạt |", "",
            "**Kế hoạch 2 tuần chuẩn bị:**", "",
            "| Tuần | Việc sẽ thực hiện | Bằng chứng dự kiến | Thời hạn |", "|---|---|---|---|",
            "| Tuần 1 |  |  |  |", "| Tuần 2 |  |  |  |", ""]
    out += ["## PHIẾU 5 - Mentor evaluation (dành cho giảng viên hướng dẫn)", "",
            f"> **Lưu ý thang điểm:** Phiếu 2 (TR) chấm **0-{tr_max}**; Phiếu 5.1 (WR) và 5.2 (RR) chấm "
            f"**0-{wr['scale']['max']}**. Hai thang khác nhau — không quy đổi trực tiếp.", "",
            f"### 5.1 Working Readiness — chấm 0-{wr['scale']['max']} mỗi tiêu chí, tổng /{wr['max_total']}", "",
            f"| Phẩm chất | Evidence quan sát được | Điểm 0-{wr['scale']['max']} | Ghi chú |", "|---|---|---|---|"]
    out += [f"| {t['name']} | {esc(t['evidence'])} |  |  |" for t in wr["traits"]]
    th = wr["thresholds"]
    out += ["", f"**Ngưỡng gợi ý (/{wr['max_total']}):** Project ≥{th['project']} · Internship ≥{th['internship']} · "
            f"DATN engineering ≥{th['datn_engineering']} · DATN research-oriented ≥{th['datn_research_oriented']} · "
            f"NCKH ≥{th['nckh']} · Advanced (đề tài family `B6`, hoặc đề tài loại R của family `AB`) "
            f"≥{th['advanced_b6_ab_r']}.", "",
            "*Lưu ý: ở dòng ngưỡng trên, `B6` là **family** trong mã chuẩn, không phải mã ngắn cohort `B6`.*", "",
            f"*{star(wr['note'])}*", ""]
    out += [f"### 5.2 Research Readiness — chấm 0-{rz['scale']['max']} mỗi tiêu chí, tổng /{rz['max_total']} "
            "(khi đề tài có định hướng nghiên cứu)", "",
            f"| Năng lực | Evidence | Điểm 0-{rz['scale']['max']} |", "|---|---|---|"]
    out += [f"| {t['name']} | {esc(t['evidence'])} |  |" for t in rz["traits"]]
    out += ["", "**Kỳ vọng RR theo loại hoạt động:**", "",
            "| Loại hoạt động | Mức RR kỳ vọng |", "|---|---|"]
    out += [f"| {esc(e['label'])} | {esc(e['expectation'])} |" for e in rz["expectations"]]
    out += ["", f"*{star(rz['note'])}*", ""]
    out += ["### 5.3 Kết quả đánh giá và phân công", "",
            "Level: " + " · ".join(f"L{k} {v}" for k, v in sorted(LEVELS.items())) + ".", "",
            "| Mục | Đánh giá |", "|---|---|",
            "| Technical Readiness (TR, đã kiểm chứng mini-task) |  |",
            f"| Working Readiness (WR /{wr['max_total']}) |  |",
            f"| Research Readiness (RR /{rz['max_total']} + nhận định) |  |",
            "| **Level đánh giá của sinh viên (L0-L5)** |  |",
            "| **Level tối thiểu của đề tài đề xuất** |  |",
            "| **Đối chiếu level** | ☐ Đạt sàn ☐ Chưa đạt sàn (ghi lý do nếu vẫn nhận) |",
            "| Prerequisite gaps |  |", "| Family phù hợp |  |",
            "| Đề tài đề xuất (mã chuẩn) |  |", "| MVT dự kiến |  |",
            "| Research Extension (nếu có) |  |",
            "| Kết luận | ☐ " + " ☐ ".join(rr["mentor_decision_options"]) + " |",
            "| Lý do/điều kiện |  |", "",
            "Giảng viên hướng dẫn: __________________________  Ngày: ____ / ____ / 2026", "",
            "Sinh viên ký/ghi rõ họ tên: ______________________________", ""]
    return "\n".join(out)

# ---------------- write ----------------
outputs = {
  "Master_Project_Portfolio_AB.md": gen_master(),
  "Course_Project_Catalog.md":       gen_catalog("P"),
  "Internship_Catalog.md":           gen_catalog("I"),
  "Graduation_Thesis_Catalog.md":    gen_catalog("T"),
  "Research_Opportunities_Catalog.md": gen_catalog("R"),
}
for co_path in COHORT_FILES:
    co = json.loads(co_path.read_text(encoding="utf-8"))
    cid = co["cohort_id"]
    outputs[f"Danh_muc_de_tai_DATN_Nhom_A_B_{cid}.md"] = gen_cohort(co)
    outputs[f"Phieu_lua_chon_va_danh_gia_de_tai_DATN_{cid}.md"] = gen_phieu(co)

for name, content in outputs.items():
    (BUILD/name).write_text(content, encoding="utf-8")
    print("built:", name)

if "--docx" in sys.argv:
    TARGETS = {
      "Master_Project_Portfolio_AB.md":      BASE/"02_Project_Portfolio/Master_Project_Portfolio_AB.docx",
      "Course_Project_Catalog.md":           BASE/"02_Project_Portfolio/Course_Project_Catalog.docx",
      "Internship_Catalog.md":               BASE/"02_Project_Portfolio/Internship_Catalog.docx",
      "Graduation_Thesis_Catalog.md":        BASE/"02_Project_Portfolio/Graduation_Thesis_Catalog.docx",
      "Research_Opportunities_Catalog.md":   BASE/"02_Project_Portfolio/Research_Opportunities_Catalog.docx",
    }
    for co_path in COHORT_FILES:
        cid = json.loads(co_path.read_text(encoding="utf-8"))["cohort_id"]
        TARGETS[f"Danh_muc_de_tai_DATN_Nhom_A_B_{cid}.md"] = BASE/f"Danh_muc_de_tai_DATN_Nhom_A_B_{cid}.docx"
        TARGETS[f"Phieu_lua_chon_va_danh_gia_de_tai_DATN_{cid}.md"] = BASE/f"Phieu_lua_chon_va_danh_gia_de_tai_DATN_{cid}.docx"
    for src, dst in TARGETS.items():
        subprocess.run(["pandoc", str(BUILD/src), "-f", "markdown", "-t", "docx",
                        "-o", str(dst), "--toc", "--toc-depth=2"], check=True)
        print("docx:", dst.relative_to(BASE))

# ---------------- pdf (cohort documents only) ----------------
PRINT_CSS = """
@page { size: A4; margin: 18mm 16mm 20mm 16mm; }
html { -webkit-print-color-adjust: exact; }
body { font-family: "Segoe UI", "Noto Sans", "DejaVu Sans", Arial, sans-serif;
       font-size: 10.5pt; line-height: 1.45; color: #14161a; margin: 0; }
h1 { font-size: 19pt; margin: 0 0 .35em; }
h2 { font-size: 13.5pt; margin: 1.5em 0 .4em; padding-bottom: .18em;
     border-bottom: 1.5px solid #c8ccd2; break-after: avoid; }
h3 { font-size: 11.5pt; margin: 1.1em 0 .3em; break-after: avoid; }
h2, h3, blockquote { break-inside: avoid; }
/* Bảng dài phải được phép ngắt trang, nhưng lặp lại dòng tiêu đề và không cắt
   ngang giữa một hàng — nếu để break-inside:avoid cả bảng thì bảng lớn bị đẩy
   nguyên khối sang trang mới và để lại nửa trang trắng. */
thead { display: table-header-group; }
tr { break-inside: avoid; }
p, li { margin: .35em 0; orphans: 2; widows: 2; }
code { font-family: "Consolas", "DejaVu Sans Mono", monospace; font-size: .92em;
       background: #eef0f3; padding: .05em .3em; border-radius: 3px; }
blockquote { margin: .7em 0; padding: .5em .9em; background: #f4f6f8;
             border-left: 3px solid #8f98a3; }
table { border-collapse: collapse; width: 100%; margin: .6em 0; font-size: 9.5pt; }
th, td { border: 1px solid #b9bec6; padding: 4px 7px; text-align: left;
         vertical-align: top; }
th { background: #eceff2; font-weight: 600; }
hr { border: none; border-top: 1px solid #c8ccd2; margin: 1.2em 0; }
"""

def find_browser():
    """Tìm Chromium/Chrome/Edge để in PDF. Ưu tiên biến môi trường CHROME_BIN."""
    import shutil
    env = os.environ.get("CHROME_BIN")
    if env and pathlib.Path(env).exists(): return env
    for name in ("chromium", "chromium-browser", "google-chrome",
                 "google-chrome-stable", "chrome", "msedge"):
        found = shutil.which(name)
        if found: return found
    for p in (r"C:\Program Files\Google\Chrome\Application\chrome.exe",
              r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
              r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
              r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
              "/opt/pw-browsers/chromium/chrome-linux/chrome"):
        if pathlib.Path(p).exists(): return p
    return None

if "--pdf" in sys.argv:
    browser = find_browser()
    if not browser:
        sys.exit("LỖI: không tìm thấy Chromium/Chrome/Edge để in PDF. "
                 "Đặt biến môi trường CHROME_BIN trỏ tới trình duyệt rồi chạy lại.")
    for co_path in COHORT_FILES:
        cid = json.loads(co_path.read_text(encoding="utf-8"))["cohort_id"]
        src = BUILD / f"Danh_muc_de_tai_DATN_Nhom_A_B_{cid}.md"
        htm = BUILD / f"Danh_muc_de_tai_DATN_Nhom_A_B_{cid}.html"
        css = BUILD / "print.css"
        css.write_text(PRINT_CSS, encoding="utf-8")
        # pagetitle (không phải title) — chỉ đặt <title> của trang, không chèn thêm
        # một H1 nữa vào thân tài liệu bên cạnh H1 sẵn có trong Markdown.
        title = f"Danh mục đề tài Đồ án tốt nghiệp — {cid.replace('_', ' ')}"
        subprocess.run(["pandoc", str(src), "-f", "markdown", "-t", "html5",
                        "--standalone", "--metadata", "charset=utf-8",
                        "--metadata", f"pagetitle={title}",
                        "--css", css.name, "-o", str(htm)], check=True)
        dst = BASE / f"Danh_muc_de_tai_DATN_Nhom_A_B_{cid}.pdf"
        subprocess.run([browser, "--headless", "--disable-gpu", "--no-sandbox",
                        "--no-pdf-header-footer", f"--print-to-pdf={dst}",
                        htm.as_uri()], check=True,
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print("pdf:", dst.relative_to(BASE), f"(browser: {browser})")
print("DONE")
