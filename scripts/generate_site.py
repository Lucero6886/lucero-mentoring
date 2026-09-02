#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sinh trang catalog công khai cho sinh viên từ 06_Data/ (CHỈ dữ liệu public).

Outputs:
  docs/index.html          — trang tĩnh đầy đủ (GitHub Pages: Settings → Pages → main /docs)
  build/site_artifact.html — cùng nội dung, dạng fragment để xuất bản claude.ai Artifact

Không nhúng bất kỳ dữ liệu sinh viên/riêng tư nào. Chạy validate trước khi sinh.
"""
import json, pathlib, html, sys
import cohort_schedule as cs

BASE = pathlib.Path(__file__).resolve().parents[1]
DATA, DOCS, BUILD = BASE/"06_Data", BASE/"docs", BASE/"build"
DOCS.mkdir(exist_ok=True); BUILD.mkdir(exist_ok=True)

pf = json.loads((DATA/"project_portfolio.json").read_text(encoding="utf-8"))
mg = json.loads((DATA/"milestone_gates.json").read_text(encoding="utf-8"))
co = json.loads((DATA/"cohort_HK1_2026_2027.json").read_text(encoding="utf-8"))
rr = json.loads((DATA/"readiness_rubrics.json").read_text(encoding="utf-8"))

TOPICS, FAMS, LEVELS, TYPES = pf["topics"], pf["families"], pf["levels"], pf["types"]
BYCODE = {t["code"]: t for t in TOPICS}
VER, UPD = pf["meta"]["version"], pf["meta"]["updated"]
AUTHOR = pf["meta"]["author"]
FAM_ORDER = ["A0","A1","A2","A3","A4","A5","A6","A7","B0","B1","B2","B3","B4","B5","B6","AB"]
TYPE_LABEL = {k: v[0] for k, v in TYPES.items()}
DIFF = {0:"Cơ bản",1:"Cơ bản",2:"Trung bình",3:"Trung bình–khá",4:"Khá–cao",5:"Cao"}

def esc(s): return html.escape(str(s or ""), quote=True)

def dmy(iso):  # 2026-09-20 -> 20/09/2026
    y, m, d = iso.split("-"); return f"{d}/{m}/{y}"

# ---------------- phong cách dùng chung (scripts/site_style.py) ----------------
from site_style import CSS, FONTS

JS = """
(function(){
  var q=document.getElementById('q'), fam=document.getElementById('fam'),
      lv=document.getElementById('lv'), chips=document.querySelectorAll('.typechips button'),
      cards=Array.prototype.slice.call(document.querySelectorAll('.card')),
      heads=Array.prototype.slice.call(document.querySelectorAll('.fam-block')),
      count=document.getElementById('count');
  var typ='ALL';
  function norm(s){return (s||'').toLowerCase();}
  function apply(){
    var text=norm(q.value), f=fam.value, l=lv.value, shown=0;
    cards.forEach(function(c){
      var ok=true;
      if(typ!=='ALL' && c.dataset.type!==typ) ok=false;
      if(f!=='ALL' && c.dataset.fam!==f) ok=false;
      if(l!=='ALL' && parseInt(c.dataset.level,10)>parseInt(l,10)) ok=false;
      if(text && norm(c.dataset.search).indexOf(text)<0) ok=false;
      c.style.display=ok?'':'none'; if(ok) shown++;
    });
    heads.forEach(function(h){
      var any=h.querySelectorAll('.card:not([style*="display: none"])').length>0;
      h.style.display=any?'':'none';
    });
    count.textContent='Hiển thị '+shown+'/'+cards.length+' đề tài';
  }
  chips.forEach(function(b){b.addEventListener('click',function(){
    typ=b.dataset.type;
    chips.forEach(function(x){x.setAttribute('aria-pressed', x===b?'true':'false');});
    apply();
  });});
  [q,fam,lv].forEach(function(el){el.addEventListener('input',apply);});
  apply();
})();
"""

# ---------------- HTML pieces ----------------
def pill(t): return f'<span class="pill {t}">{esc(TYPE_LABEL[t])}</span>'
def lvpill(n): return f'<span class="pill lv">L{n}+ · {esc(LEVELS[str(n)])}</span>'

def topic_card(t):
    alias = (t.get("cohort_alias") or {}).get(co["cohort_id"])
    alias_html = f' <span class="pill alias">HK1: {esc(alias)}</span>' if alias else ""
    search = " ".join([t["code"], alias or "", t["title_vi"], t["title_en"], t["family"], t["prerequisites"], t["tools"]])
    rows = [
        ("Phạm vi", esc(t["scope"])),
        ("Điều kiện đầu vào", esc(t["prerequisites"]) +
            (f' <span class="muted">(mã: {esc(", ".join(t["prereq_codes"]))})</span>' if t.get("prereq_codes") else "")),
        ("Sản phẩm", esc(t["outputs"])),
    ]
    if t.get("mvt"):
        rows.append(("Bắt buộc (MVT)", f'<span class="mvt">{esc(t["mvt"])}</span>'))
    rows += [
        ("Extension", esc(t["extension"])),
        ("Công cụ", esc(t["tools"])),
        ("Nghề nghiệp", esc(t["career_relevance"])),
    ]
    if t.get("checkpoints_15w"):
        rows.append(("Checkpoint 15 tuần", esc(t["checkpoints_15w"])))
    if t.get("eligibility"):
        rows.append(("Điều kiện cứng", esc(t["eligibility"])))
    dl = "".join(f"<dt>{k}</dt><dd>{v}</dd>" for k, v in rows)
    return (
        f'<details class="card" data-fam="{t["family"]}" data-type="{t["type"]}" '
        f'data-level="{t["min_level"]}" data-search="{esc(search)}">'
        f'<summary><span class="code">{t["code"]}</span>'
        f'<span class="title">{esc(t["title_vi"])}<small>{esc(t["title_en"])}</small></span>'
        f'{pill(t["type"])} {lvpill(t["min_level"])}{alias_html}</summary>'
        f'<div class="body"><dl>{dl}</dl></div></details>'
    )

def catalog_section():
    fam_opts = "".join(f'<option value="{f}">{f} — {esc(FAMS[f]["name_vi"])}</option>' for f in FAM_ORDER)
    lv_opts = "".join(f'<option value="{n}">≤ L{n} — {esc(LEVELS[str(n)])}</option>' for n in range(6))
    chips = '<button data-type="ALL" aria-pressed="true">Tất cả</button>' + "".join(
        f'<button data-type="{t}" aria-pressed="false">{t}</button>' for t in "PITR")
    blocks = []
    for f in FAM_ORDER:
        cards = "".join(topic_card(t) for t in TOPICS if t["family"] == f)
        blocks.append(
            f'<div class="fam-block"><div class="fam-head">{f} — {esc(FAMS[f]["name_vi"])}</div>'
            f'<div class="fam-sub">{esc(FAMS[f]["purpose"])}</div>{cards}</div>')
    return f"""
<section id="catalog"><div class="wrap">
<h2>Danh mục đầy đủ — {len(TOPICS)} đề tài</h2>
<p class="muted">P = Project môn học · I = Thực tập · T = Đồ án tốt nghiệp · R = Nghiên cứu khoa học.
Bấm vào đề tài để xem chi tiết. Level là <em>mức tối thiểu</em> — mentor chốt scope theo readiness thực tế.</p>
<div class="filters">
  <div class="typechips" role="group" aria-label="Lọc theo loại">{chips}</div>
  <label for="fam">Nhóm</label>
  <select id="fam"><option value="ALL">Tất cả</option>{fam_opts}</select>
  <label for="lv">Level của tôi</label>
  <select id="lv"><option value="ALL">Mọi level</option>{lv_opts}</select>
  <input type="search" id="q" placeholder="Tìm theo mã, tên, công cụ… (vd: A4-T01, FPGA, Polar)" aria-label="Tìm kiếm đề tài">
</div>
<div class="count" id="count" aria-live="polite"></div>
{''.join(blocks)}
</div></section>"""

CAL = cs.build_calendar(co.get("start_date"), co.get("duration_weeks"), co.get("breaks"))
DL  = cs.gate_deadlines(mg["gates"], CAL)

def cohort_section():
    GROUPS = co.get("alias_groups") or [{"prefix": "A", "name": "Nhóm A"}, {"prefix": "B", "name": "Nhóm B"}]
    gates = ""
    for g in mg["gates"]:
        iso = DL.get(str(g["gate"]))
        due = (f'hết tuần {g["week_end"]}<br><span class="muted">{dmy(iso)}</span>'
               if iso else f'hết tuần {g["week_end"]}')
        hard = ' class="hard"' if g["gate"] in (2, 3, 4) else ""
        gates += (f'<tr><td><strong>{g["gate"]}</strong> · {esc(g["name"].split(" - ")[1])}</td>'
                  f'<td class="date">{esc(cs.week_label(g))}</td><td class="date">{due}</td>'
                  f'<td>{esc(g["pass_criteria"])}</td><td{hard}>{esc(g["fail_rule"])}</td></tr>')
    def qrows(group):
        rows = sorted((x for x in co["topics"] if x["alias"].startswith(group)),
                      key=lambda x: int(x["alias"][1:]))
        out = ""
        for x in rows:
            t = BYCODE[x["code"]]
            out += (f'<tr><td class="date">{esc(x["alias"])}</td>'
                    f'<td class="date"><b>{t["code"]}</b></td><td>{esc(t["title_vi"])}</td>'
                    f'<td>{esc(DIFF[t["min_level"]])}</td></tr>')
        return out
    group_tables = ""
    for _g in GROUPS:
        _rows = qrows(_g["prefix"])
        if not _rows:
            continue
        _n = len([x for x in co["topics"] if x["alias"].startswith(_g["prefix"])])
        group_tables += (f'<h3>{esc(_g["name"])} — {_n} đề tài mở</h3>'
                         '<div class="tw"><table><thead><tr><th>Mã ngắn</th><th>Mã chuẩn</th>'
                         f'<th>Đề tài</th><th>Độ khó</th></tr></thead><tbody>{_rows}</tbody></table></div>')
    _opened = {x["code"] for x in co["topics"]}
    _rest = [t for t in TOPICS if t["type"] == co.get("activity_type", "T")
             and t.get("status") == "active" and t["code"] not in _opened]
    if _rest and co.get("remaining_topics_policy", "on_request") == "on_request":
        _li = " · ".join(f'<code>{esc(t["code"])}</code>' for t in sorted(_rest, key=lambda x: x["code"]))
        group_tables += (f'<p class="muted"><b>Mở theo yêu cầu:</b> kho còn {len(_rest)} đề tài '
                         f'{esc(co.get("activity_type","T"))} không phát đại trà kỳ này ({_li}). '
                         'Nếu bạn chứng minh được nền tương ứng qua bài kiểm tra năng lực, hãy trao đổi trực tiếp '
                         'với mentor — quyết định theo từng trường hợp.</p>')
    career = "".join(
        f'<tr><td>{esc(g["goal"])}{(" <span class=muted>(" + esc(g["note"]) + ")</span>") if g.get("note") else ""}</td>'
        f'<td class="date">{esc(", ".join(g["primary"]))}</td><td class="date">{esc(", ".join(g["next"]))}</td></tr>'
        for g in co["career_guide"])
    return f"""
<section id="cohort"><div class="wrap">
<h2>Đồ án tốt nghiệp HK1 2026–2027</h2>
<h3>6 cửa kiểm soát tiến độ (gate) và hạn chót</h3>
<div class="tw"><table><thead><tr><th>Gate</th><th>Tuần</th><th>Hạn chót</th><th>Điều kiện qua</th><th>Nếu không đạt</th></tr></thead><tbody>{gates}</tbody></table></div>
{group_tables}
<p class="muted">Khi điền phiếu nguyện vọng, ghi <b>mã chuẩn</b> (vd <code>A4-T01</code>); mã ngắn chỉ để đọc nhanh.
Chi tiết từng đề tài: xem mục Danh mục bên dưới (có gắn nhãn "HK1").</p>
<h3>Chọn theo mục tiêu nghề nghiệp</h3>
<div class="tw"><table><thead><tr><th>Mục tiêu</th><th>Đề tài ưu tiên</th><th>Lộ trình tiếp theo</th></tr></thead><tbody>{career}</tbody></table></div>
</div></section>"""

def howto_section():
    tr = rr["technical_readiness"]; wr = rr["working_readiness"]
    scale = " · ".join(f"<b>{k}</b> = {esc(v)}" for k, v in tr["scale"].items())
    return f"""
<section id="howto"><div class="wrap">
<h2>Cách chọn đề tài và readiness test</h2>
<ol class="steps">
<li><b>Xác định hướng:</b> vi mạch số (RTL/FPGA/ASIC) · Polar coding · hệ nhúng, IoT và co-design.</li>
<li><b>Đối chiếu năng lực:</b> dùng bộ lọc "Level của tôi" ở Danh mục; đọc kỹ "Điều kiện đầu vào" từng đề tài.</li>
<li><b>Chọn Top-3 nguyện vọng</b> theo thứ tự ưu tiên, ghi <b>mã chuẩn</b> vào phiếu được phát. Nguyện vọng là input — <em>readiness mới quyết định scope</em>.</li>
<li><b>Readiness test 2 tuần:</b> literature task (problem–input–output–method–metric–điểm chưa hiểu) · technical mini-task 4–10 giờ · oral check 5–10 phút bằng lời của chính mình.</li>
<li><b>Nhận đề tài & làm việc theo milestone:</b> mỗi tuần nộp báo cáo kèm evidence trước buổi gặp.</li>
</ol>
<h3>Tự đánh giá kỹ năng (thang 0–5)</h3>
<p class="muted">{scale}. Tự đánh giá chỉ là dữ liệu ban đầu — sẽ kiểm chứng bằng mini-task.</p>
<h3>Evidence là gì?</h3>
<p>“Đã đọc / đã tìm hiểu” <b>không</b> được tính là tiến độ. Evidence = code/commit, schematic, PCB,
kết quả đo, waveform, log, figure, bảng số liệu, test pass, technical note hoặc demo.</p>
</div></section>"""

def rules_section():
    return f"""
<section id="rules"><div class="wrap">
<h2>Quy tắc chương trình</h2>
<ul class="plain">
<li><b>Baseline trước novelty:</b> chưa có baseline chạy đúng thì chưa mở phần mở rộng nghiên cứu.</li>
<li><b>MVT tách khỏi Extension:</b> mỗi đồ án có phần bắt buộc đủ để tốt nghiệp chuẩn kỹ thuật; phần mở rộng là tùy chọn, chỉ mở khi qua Gate 2 đúng hạn.</li>
<li><b>Trượt Gate 3 → thu hẹp phạm vi</b> nhưng giữ chuẩn kỹ thuật — một đồ án nhỏ, đúng, tái lập được và hiểu sâu tốt hơn một đồ án "đẹp" nhưng không sở hữu.</li>
<li><b>AI được phép dùng</b> để học, gợi ý, debug, cải thiện câu chữ — nhưng bạn chịu trách nhiệm cuối cùng về mọi code, số liệu, trích dẫn và kết luận. <b>Cannot explain = Not completed.</b></li>
<li><b>Mỗi project để lại Legacy Package:</b> README chạy lại được, code + test, kết quả, known issues, next steps — để khóa sau kế thừa.</li>
<li><b>Engineering và Research ngang giá trị:</b> không bắt buộc mọi sinh viên theo hướng nghiên cứu.</li>
</ul>
</div></section>"""

body = f"""
<nav class="topnav"><div class="wrap">
  <span class="logo">Mentoring Lucero · EEE</span>
  <a href="guide.html">Hướng dẫn chọn đề tài</a>
  <a href="#cohort">DATN HK1 2026–2027</a>
  <a href="#catalog">Danh mục ({len(TOPICS)})</a>
  <a href="#howto">Cách chọn đề tài</a>
  <a href="#rules">Quy tắc</a>
</div></nav>
<header class="hero"><div class="wrap">
  <span class="eyebrow">Engineering &amp; Research Mentoring Program (Lucero)</span>
  <h1>Danh mục đề tài — Digital IC / FPGA / ASIC &amp; Hardware-Aware Polar Decoding</h1>
  <p class="meta">Project môn học · Thực tập · Đồ án tốt nghiệp · Nghiên cứu khoa học — phiên bản dữ liệu {esc(VER)} · {esc(UPD)}</p>
  <p class="meta">GVHD: {esc(AUTHOR)}</p>
  <div class="golden"><b>Quy tắc vàng:</b> nguyện vọng là điểm bắt đầu — <b>readiness quyết định scope</b>.
  Baseline trước novelty. Sản phẩm không giải thích được = chưa hoàn thành.</div>
</div></header>
{cohort_section()}
{catalog_section()}
{howto_section()}
{rules_section()}
<footer><div class="wrap">
Trang này sinh tự động từ dữ liệu chuẩn <code>06_Data/</code> (scripts/generate_site.py) — chỉ chứa thông tin công khai,
không có dữ liệu cá nhân sinh viên. · {esc(AUTHOR)} · v{esc(VER)} · {esc(UPD)}
</div></footer>
<script>{JS}</script>
"""


TITLE = "Danh mục Đề tài Lucero"

full = f"""<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{TITLE}</title>
{FONTS}
<style>{CSS}</style>
</head>
<body>
{body}
</body>
</html>"""

fragment = f"""<title>{TITLE}</title>
{FONTS}
<style>{CSS}</style>
{body}"""

(DOCS/"index.html").write_text(full, encoding="utf-8")
(BUILD/"site_artifact.html").write_text(fragment, encoding="utf-8")
n_cards = full.count('class="card"')
print(f"docs/index.html ({len(full)//1024} KB) + build/site_artifact.html — {n_cards} topic cards")
assert n_cards == len(TOPICS), "card count mismatch!"
print("OK")
