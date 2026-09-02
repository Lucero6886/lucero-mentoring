#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sinh docs/guide.html — trang hướng dẫn sinh viên trước khi chọn đề tài.

Vì sao tách khỏi trang danh mục: `docs/index.html` trả lời *"có những đề tài nào"*
và phục vụ người đã biết mình tìm gì. Trang này phục vụ người **chưa biết bắt đầu
từ đâu**: chương trình vận hành ra sao, 16 nhóm khác nhau chỗ nào, P/I/T/R nghĩa
là gì, phải làm gì trước khi đăng ký, và mỗi đề tài đòi hỏi sản phẩm gì.

Nguyên tắc: mọi nội dung sinh từ `06_Data/*.json`. Tên đề tài lấy nguyên từ
`project_portfolio.json` nên trang này **không bao giờ lệch** với danh mục, phiếu
đăng ký hay bản PDF.

Cách dùng (từ thư mục gốc dự án):
    python3 scripts/generate_guide.py
"""
import html, json, pathlib, sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from site_style import CSS, FONTS, GUIDE_CSS, REPO

BASE = pathlib.Path(__file__).resolve().parents[1]
DATA = BASE / "06_Data"
DOCS = BASE / "docs"
BUILD = BASE / "build"


def esc(s):
    return html.escape(str(s or ""), quote=True)


def load(n):
    return json.loads((DATA / n).read_text(encoding="utf-8"))


def ul(items, cls=""):
    c = f' class="{cls}"' if cls else ""
    return f"<ul{c}>" + "".join(f"<li>{esc(x)}</li>" for x in items) + "</ul>"


def ol(items):
    return "<ol>" + "".join(f"<li>{esc(x)}</li>" for x in items) + "</ol>"


PORT = load("project_portfolio.json")
RP = load("research_packs.json")
MG = load("milestone_gates.json")
TOPICS = {t["code"]: t for t in PORT["topics"]}
GROUPS = {g["group"]: g for g in RP["groups"]}
TYPES = {m["type"]: m for m in RP["maturity"]["levels"]}
FAM = PORT["families"]
LEVELS = PORT["levels"]
VER, UPD = RP["meta"]["version"], RP["meta"]["updated"]
_co = sorted(DATA.glob("cohort_*.json"))
COHORT = json.loads(_co[-1].read_text(encoding="utf-8"))["cohort_id"] if _co else ""


def alias_of(p):
    """Mã ngắn của đề tài trong khóa hiện hành, rỗng nếu khóa này không mở đề tài đó."""
    a = p.get("cohort_alias")
    return (a or {}).get(COHORT, "") if isinstance(a, dict) else (a or "")
AUTHOR = RP["meta"]["author"]

BY_GROUP = {}
for p in RP["packs"]:
    BY_GROUP.setdefault(p["group"], []).append(p)

N = len(RP["packs"])
N_R = sum(1 for p in RP["packs"] if p["type"] == "R")
N_T = sum(1 for p in RP["packs"] if p["type"] == "T")
N_DEEP = sum(1 for p in RP["packs"] if p["depth"] == "full")

TYPE_CLS = {"P": "low", "I": "warn", "T": "accent", "R": "r"}

# ---------------------------------------------------------------- các mục

def sec_intro():
    lad = ("PCB / board thật  →  RTL  →  Số học &amp; DSP  →  FPGA  →  ASIC / EDA  →  "
           "Nhúng &amp; IoT  →  Polar  →  Thích ứng / Neural  →  Co-design  →  Công bố")
    return f"""
<section id="hieu"><div class="wrap">
<h2>1. Điều cần hiểu trước tiên</h2>
<p>Đây là <b>một chương trình nghiên cứu</b>, không phải {N} đề tài rời rạc. Các đề tài xếp thành
những nấc năng lực nối tiếp nhau — em có thể bắt đầu ở một project kỹ năng, đi qua thực tập và
đồ án, rồi mới nâng lên nghiên cứu <b>khi đã có đủ bằng chứng</b>.</p>
<div class="ladder">{lad}</div>
<div class="stat-row">
  <div class="stat"><b>{N}</b><span>Đề tài</span></div>
  <div class="stat"><b>{len(GROUPS)}</b><span>Nhóm năng lực</span></div>
  <div class="stat"><b>{N_T}</b><span>Đồ án tốt nghiệp (T)</span></div>
  <div class="stat"><b>{N_R}</b><span>Nghiên cứu (R)</span></div>
  <div class="stat"><b>{N_DEEP}</b><span>Có hồ sơ sâu</span></div>
</div>
<div class="okbox"><b>Không phải đề tài nào cũng phải thành bài báo.</b> Một project PCB, RTL hay
FPGA làm tốt có giá trị riêng nếu nó tạo ra kỹ năng thật và bằng chứng thật. Chỉ nâng lên mức
nghiên cứu khi có <b>biến nghiên cứu, baseline, metric, giả thuyết và thí nghiệm có kiểm soát</b>.</div>
</div></section>"""


def sec_groups():
    cards = []
    for gid in sorted(GROUPS):
        g, ps = GROUPS[gid], BY_GROUP.get(gid, [])
        cnt = {}
        for p in ps:
            cnt[p["type"]] = cnt.get(p["type"], 0) + 1
        mix = " · ".join(f"{k}:{cnt[k]}" for k in "PITR" if k in cnt)
        desc = FAM.get(gid, {}).get("purpose") or g["name_en"]
        cards.append(
            f'<button class="gcard" data-g="{esc(gid)}" aria-pressed="false">'
            f'<span class="gid">{esc(gid)} · {len(ps)} đề tài</span>'
            f'<span class="gn">{esc(g["name_vi"])}</span>'
            f'<span class="gd">{esc(desc)}</span>'
            f'<span class="gm">{esc(mix)}</span></button>')
    return f"""
<section id="nhom"><div class="wrap">
<h2>2. Bản đồ {len(GROUPS)} nhóm đề tài</h2>
<p>Bấm vào một nhóm để lọc danh sách {N} đề tài ở mục 6. Nếu chưa biết mình thích gì,
hãy đọc mô tả từng nhóm <b>trước khi</b> nhìn tên đề tài cụ thể — chọn theo tên nghe hay
là cách chọn sai phổ biến nhất.</p>
<div class="groupgrid">{''.join(cards)}</div>
</div></section>"""


def sec_types():
    rows = "".join(
        f'<tr><td><span class="pill {TYPE_CLS[m["type"]]}">{m["type"]}</span> {esc(m["name_vi"])}</td>'
        f'<td>{esc(m["goal"])}</td><td>{esc(m["core_evidence"])}</td>'
        f'<td>{esc(m["research_expectation"])}</td></tr>' for m in RP["maturity"]["levels"])
    lv = "".join(f'<tr><td><b>L{k}</b></td><td>{esc(v)}</td></tr>' for k, v in sorted(LEVELS.items()))
    return f"""
<section id="loai"><div class="wrap">
<h2>3. Đọc đúng loại đề tài và mức sàn</h2>
<h3>Bốn mức trưởng thành P → I → T → R</h3>
<table><thead><tr><th>Loại</th><th>Mục tiêu</th><th>Bằng chứng lõi</th><th>Kỳ vọng nghiên cứu</th></tr></thead>
<tbody>{rows}</tbody></table>
<div class="rulebox"><b>Quy tắc chống “paper hóa” giả.</b> {esc(RP["maturity"]["anti_fake_research_rule"])}</div>
<h3>Mức sàn năng lực L0–L5</h3>
<p>Mỗi đề tài ghi một <b>sàn</b>. Sàn không phải điểm số — nó nói đề tài này giả định em đã có sẵn gì.
Chọn đề tài trên sàn của mình một bậc là hợp lý; trên hai bậc thì cần kế hoạch bù kiến thức được mentor duyệt.</p>
<table><thead><tr><th>Mức</th><th>Nghĩa</th></tr></thead><tbody>{lv}</tbody></table>
</div></section>"""


STEPS = [
 ("Chọn 1–2 nhánh năng lực, chưa chọn đề tài",
  "Đọc mục 2 và chọn nhánh em muốn giỏi lên sau một năm nữa, không phải đề tài nghe kêu nhất."),
 ("Tự đánh giá mức sẵn sàng",
  "Đối chiếu sàn L0–L5 với những gì em đã thật sự tự làm được — không tính những thứ mới chỉ nghe giảng."),
 ("Chọn 3 đề tài ứng viên",
  "Ba đề tài trong cùng một nhánh, khác mức khó. Ghi bằng mã chuẩn, ví dụ <code>A4-T01</code>."),
 ("Đọc nền và tự viết lại bài toán",
  "Mở trang hướng dẫn của từng đề tài, đọc mục “phải đọc”, rồi tự viết lại bài toán bằng lời của mình trong 5–7 câu."),
 ("Xác định baseline và metric",
  "Với mỗi ứng viên: so với cái gì, đo bằng gì. Không trả lời được hai câu này thì chưa hiểu đề tài."),
 ("Chạy một mini-proof 4–10 giờ",
  "Một việc nhỏ chạm đúng kỹ năng khó nhất của đề tài. Đây là bài kiểm tra rẻ nhất để biết mình có hợp không."),
 ("Viết rủi ro và phương án B",
  "Cái gì có thể làm đề tài kẹt ở tuần 6, và khi đó thu nhỏ phạm vi theo hướng nào."),
 ("Trao đổi mentor để chốt",
  "Mang theo bảy thứ trên. Buổi chốt đề tài là buổi bàn về bằng chứng, không phải buổi xin đề tài."),
]


def sec_steps():
    li = "".join(f"<li><b>{esc(t)}</b><p>{d}</p></li>" for t, d in STEPS)
    return f"""
<section id="lotrinh"><div class="wrap">
<h2>4. Lộ trình bắt buộc trước khi chọn đề tài</h2>
<p>Tám bước này mất khoảng một tuần. Bỏ qua chúng thì tiết kiệm được một tuần và
thường mất sáu tuần ở giữa kỳ.</p>
<ol class="steps">{li}</ol>
</div></section>"""


def sec_gates():
    lad = MG["research_ladder"]
    gs = {g["gate"]: g for g in MG["gates"]}
    rows = []
    for g in lad["gates"]:
        m = g["maps_to_gate"]
        where = (f"Gate {m} · {gs[m]['weeks_label'].replace('Tuần','tuần')}"
                 if isinstance(m, int) else "ngoài khung 15 tuần")
        rows.append(f'<div class="gate"><div class="gg">{esc(g["id"])}</div>'
                    f'<div class="gt"><b>{esc(g["name_vi"])}</b> — {esc(where)}<br>'
                    f'{esc(g["pass_criteria"][0])}…</div></div>')
    return f"""
<section id="gate"><div class="wrap">
<h2>5. Một đề tài được mentor như thế nào: G0 → G7</h2>
<p>Mọi đề tài đi qua cùng một khuôn. Mốc tính theo <b>số tuần kể từ ngày em chính thức nhận đề tài</b>,
nên khung này dùng chung cho mọi khóa. G0–G6 nằm trong sáu cửa của khung {MG['frame']['duration_weeks']} tuần;
<b>G7 chỉ mở khi đề tài thật sự có bằng chứng để viết bài</b>.</p>
<div class="gates">{''.join(rows)}</div>
<div class="rulebox"><b>Luật cứng.</b> Không có baseline ở Gate 2 → không mở phần mở rộng nghiên cứu.
Trễ tiến độ → <b>thu nhỏ phạm vi, không hạ chuẩn</b>. Không giải thích được sản phẩm của mình = chưa hoàn thành.</div>
</div></section>"""


def sec_table():
    rows = []
    for gid in sorted(BY_GROUP):
        for p in sorted(BY_GROUP[gid], key=lambda x: ("PITR".index(x["type"]), x["code"])):
            t = TOPICS[p["code"]]
            url = f"{REPO}/blob/main/02_Project_Portfolio/Topic_Guides/{gid}/{p['code']}.md"
            deep = (f'<br><a href="{REPO}/blob/main/02_Project_Portfolio/Research_Packs/{p["code"]}'
                    f'/START-HERE.md">📘 hồ sơ thực thi chi tiết</a>' if p["depth"] == "full" else "")
            al = alias_of(p)
            alias = f' <span class="pill low">{esc(al)}</span>' if al else ""
            search = f"{p['code']} {t['title_vi']} {t['title_en']} {p['expected_output']} {GROUPS[gid]['name_vi']}".lower()
            rows.append(
                f'<tr class="topic-row" data-g="{esc(gid)}" data-t="{esc(p["type"])}" '
                f'data-l="{p["min_level"]}" data-s="{esc(search)}">'
                f'<td><code>{esc(p["code"])}</code>{alias}</td>'
                f'<td><a href="{url}">{esc(t["title_vi"])}</a>{deep}</td>'
                f'<td><span class="pill {TYPE_CLS[p["type"]]}">{p["type"]}</span></td>'
                f'<td>L{p["min_level"]}</td>'
                f'<td class="out">{esc(p["expected_output"])}</td></tr>')
    gopt = "".join(f'<option value="{esc(g)}">{esc(g)} — {esc(GROUPS[g]["name_vi"])}</option>'
                   for g in sorted(GROUPS))
    lopt = "".join(f'<option value="{k}">L{k} — {esc(v)}</option>' for k, v in sorted(LEVELS.items()))
    return f"""
<section id="tracuu"><div class="wrap">
<h2>6. Tra cứu đầy đủ {N} đề tài</h2>
<p>Cột <b>sản phẩm phải làm ra</b> là thứ đáng đọc nhất: nó nói cuối kỳ em phải nộp cái gì.
Bấm tên đề tài để mở trang hướng dẫn đầy đủ.</p>
<div class="filters">
  <label for="q">Tìm</label><input id="q" type="search" placeholder="mã, tên, sản phẩm…">
  <label for="fg">Nhóm</label><select id="fg"><option value="">Tất cả</option>{gopt}</select>
  <label for="ft">Loại</label><select id="ft"><option value="">Tất cả</option>
    <option value="P">P — Project môn học</option><option value="I">I — Thực tập</option>
    <option value="T">T — Đồ án tốt nghiệp</option><option value="R">R — Nghiên cứu</option></select>
  <label for="fl">Sàn</label><select id="fl"><option value="">Tất cả</option>{lopt}</select>
</div>
<p class="count" id="cnt"></p>
<table><thead><tr><th>Mã</th><th>Tên đề tài</th><th>Loại</th><th>Sàn</th><th>Sản phẩm phải làm ra</th></tr></thead>
<tbody id="tb">{''.join(rows)}</tbody></table>
</div></section>"""


def sec_rules():
    return f"""
<section id="luat"><div class="wrap">
<h2>7. Luật làm nghiên cứu và cách dùng AI</h2>
<div class="two">
<div>
<h3>Bốn quy tắc không thương lượng</h3>
{ol(RP["rules"])}
<h3>Tám câu phải trả lời mỗi tuần</h3>
{ol(["Tôi đọc gì?","Tôi hiểu thêm được gì?","Tôi dựng/code cái gì?","Tôi đo hoặc chạy thí nghiệm nào?",
     "Bằng chứng nằm ở đâu?","Cái gì hỏng?","Tôi nghĩ nguyên nhân là gì?",
     "Bước tiếp theo kiểm chứng giả thuyết nào?"])}
</div>
<div>
<h3>AI được dùng để</h3>
{ul(["giải thích khái niệm","gợi ý pseudocode và skeleton","hỗ trợ gỡ lỗi",
     "trau chuốt câu chữ","gợi ý hướng thí nghiệm"])}
<h3>AI không thay thế được</h3>
{ul(["đọc nguồn gốc","kiểm chứng baseline","diễn giải kết quả",
     "kiểm tra trích dẫn","quyền sở hữu và hiểu biết về code của chính em"])}
<div class="rulebox"><b>Cấm tuyệt đối:</b> bịa dữ liệu · chọn lọc kết quả đẹp ·
trích dẫn do AI bịa ra · sửa tay kết quả thô cho đẹp.<br><br>
<b>Phép thử:</b> mentor chỉ vào một dòng code và hỏi <i>“vì sao cái này đúng?”</i> —
trả lời được mà không mở chatbot thì đạt.</div>
</div>
</div>
<h3>Quy tắc dữ liệu thô</h3>
{ul(RP["raw_data_rule"])}
</div></section>"""


def sec_checklist():
    return f"""
<section id="phieu"><div class="wrap">
<h2>8. Tự kiểm trước khi đăng ký</h2>
<p>In hoặc chép mục này ra, tự đánh dấu. Còn ô nào trống thì chưa nên đăng ký.</p>
<div class="two">
<div>
<h3>Về đề tài đã chọn</h3>
<ul class="checklist">
<li>Tôi viết lại được bài toán bằng lời của mình trong 5–7 câu.</li>
<li>Tôi nói được đầu vào là gì, đầu ra là gì.</li>
<li>Tôi biết mình sẽ so sánh với baseline nào.</li>
<li>Tôi biết sẽ đo bằng metric nào.</li>
<li>Tôi biết cuối kỳ phải nộp ra những sản phẩm gì.</li>
<li>Tôi đã đọc ít nhất hai tài liệu nền của nhóm này.</li>
</ul>
</div>
<div>
<h3>Về bản thân</h3>
<ul class="checklist">
<li>Tôi đã chạy được một mini-proof 4–10 giờ liên quan tới đề tài.</li>
<li>Tôi biết kỹ năng nào mình còn thiếu và kế hoạch bù.</li>
<li>Tôi có phương án B nếu hướng chính kẹt ở tuần 6.</li>
<li>Tôi hiểu rằng trễ tiến độ dẫn tới thu nhỏ phạm vi, không phải trượt.</li>
<li>Tôi chấp nhận rằng bỏ nhiều thời gian mà không ra bằng chứng thì chưa tính là tiến độ.</li>
<li>Tôi sẵn sàng giải thích mọi dòng code mình nộp.</li>
</ul>
</div>
</div>
<div class="okbox">Nộp <b>3 nguyện vọng theo thứ tự</b>, ghi bằng <b>mã chuẩn</b> (ví dụ <code>A4-T01</code>),
gửi riêng cho mentor theo kênh đã thông báo.
<b>Đừng đăng phiếu, họ tên, mã số sinh viên hay điểm số lên kho công khai.</b></div>
</div></section>"""


JS = """
(function(){
 var rows=[].slice.call(document.querySelectorAll('.topic-row')),
     q=document.getElementById('q'), fg=document.getElementById('fg'),
     ft=document.getElementById('ft'), fl=document.getElementById('fl'),
     cnt=document.getElementById('cnt'), cards=[].slice.call(document.querySelectorAll('.gcard'));
 function apply(){
  var s=(q.value||'').trim().toLowerCase(), g=fg.value, t=ft.value, l=fl.value, n=0;
  rows.forEach(function(r){
   var ok=(!s||r.dataset.s.indexOf(s)>-1)&&(!g||r.dataset.g===g)&&(!t||r.dataset.t===t)&&(!l||r.dataset.l===l);
   r.classList.toggle('hidden',!ok); if(ok)n++;
  });
  cnt.textContent=n+' / '+rows.length+' đề tài';
  cards.forEach(function(c){c.setAttribute('aria-pressed', String(c.dataset.g===g));});
 }
 [q,fg,ft,fl].forEach(function(el){el.addEventListener('input',apply);el.addEventListener('change',apply);});
 cards.forEach(function(c){c.addEventListener('click',function(){
   fg.value=(fg.value===c.dataset.g)?'':c.dataset.g; apply();
   document.getElementById('tracuu').scrollIntoView({behavior:'smooth',block:'start'});
 });});
 apply();
})();
"""


def main():
    body = f"""
<nav class="topnav"><div class="wrap">
  <span class="logo">Mentoring Lucero · EEE</span>
  <a href="index.html">Danh mục ({N})</a>
  <a href="#nhom">{len(GROUPS)} nhóm</a>
  <a href="#lotrinh">Lộ trình chọn</a>
  <a href="#tracuu">Tra cứu</a>
  <a href="#phieu">Tự kiểm</a>
</div></nav>
<header class="hero"><div class="wrap">
  <span class="eyebrow">Engineering &amp; Research Mentoring Program (Lucero)</span>
  <h1>Guide Notes — đọc trước khi chọn đề tài</h1>
  <p class="meta">Chương trình nghiên cứu {N} đề tài · {len(GROUPS)} nhóm năng lực · phiên bản dữ liệu {esc(VER)} · {esc(UPD)}</p>
  <p class="meta">GVHD: {esc(AUTHOR)}</p>
  <div class="golden"><b>Đọc trang này trước khi mở danh mục.</b> Chọn đúng nhánh năng lực
  quan trọng hơn chọn đúng tên đề tài — và quan trọng hơn cả hai là biết mình sẽ phải
  <b>nộp ra bằng chứng gì</b> vào cuối kỳ.</div>
</div></header>
{sec_intro()}{sec_groups()}{sec_types()}{sec_steps()}{sec_gates()}{sec_table()}{sec_rules()}{sec_checklist()}
<footer><div class="wrap">
<p>Sinh tự động từ <code>06_Data/*.json</code> bằng <code>scripts/generate_guide.py</code> —
tên đề tài lấy nguyên từ danh mục nên trang này không lệch với bản in.</p>
<p><a href="{REPO}">Kho tài liệu trên GitHub</a> · <a href="index.html">Danh mục đề tài</a></p>
</div></footer>
<script>{JS}</script>"""

    TITLE = "Guide Notes — Chọn đề tài · Mentoring Lucero"
    full = (f'<!DOCTYPE html>\n<html lang="vi">\n<head>\n<meta charset="UTF-8">\n'
            f'<meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
            f'<title>{TITLE}</title>\n{FONTS}\n<style>{CSS}{GUIDE_CSS}</style>\n</head>\n<body>\n'
            f'{body}\n</body>\n</html>')
    DOCS.mkdir(exist_ok=True)
    BUILD.mkdir(exist_ok=True)
    (DOCS / "guide.html").write_text(full, encoding="utf-8")
    (BUILD / "guide_artifact.html").write_text(
        f"<title>{TITLE}</title>\n{FONTS}\n<style>{CSS}{GUIDE_CSS}</style>\n{body}", encoding="utf-8")
    n = full.count('class="topic-row"')
    print(f"docs/guide.html ({len(full)//1024} KB) + build/guide_artifact.html — {n} đề tài")
    assert n == N, f"số dòng đề tài {n} != {N}"
    return 0


if __name__ == "__main__":
    sys.exit(main())
