#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Validate 06_Data/ — fail-fast theo MASTER_PROMPT §5.

Chạy:  python3 scripts/validate_portfolio.py
Exit 0 = PASS; exit 1 = FAIL (in danh sách lỗi).
Chỉ dùng stdlib. Nguồn chuẩn: 06_Data/*.json.
"""
import json, re, sys, pathlib, datetime
import cohort_schedule

BASE = pathlib.Path(__file__).resolve().parents[1]
DATA = BASE / "06_Data"

errors, warnings = [], []
def err(msg):  errors.append(msg)
def warn(msg): warnings.append(msg)

def load(name):
    p = DATA / name
    if not p.exists():
        err(f"Thiếu file nguồn chuẩn: {p.name}")
        return None
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        err(f"{p.name}: JSON hỏng — {e}")
        return None

pf = load("project_portfolio.json")
rr = load("readiness_rubrics.json")
mg = load("milestone_gates.json")
rp = load("research_packs.json")
cohorts = sorted(DATA.glob("cohort_*.json"))

CODE_RE = re.compile(r"^(A[0-7]|B[0-6]|AB)-([PITR])(\d{2})$")
PAT_RE  = re.compile(r"^(A[0-7]|B[0-6]|AB)-([PITR])\*$")

if pf:
    fams, topics = pf.get("families", {}), pf.get("topics", [])
    levels = pf.get("levels", {})
    codes = [t.get("code","?") for t in topics]
    # 1. duplicate codes
    seen = set()
    for c in codes:
        if c in seen: err(f"Mã trùng lặp: {c}")
        seen.add(c)
    codeset = set(codes)
    REQUIRED = ["code","family","type","title_vi","title_en","min_level",
                "prerequisites","outputs","scope","extension","tools",
                "status","career_relevance","prereq_codes"]
    STATUS_OK = set(pf.get("meta",{}).get("status_values",["active","candidate","archived"]))
    for t in topics:
        c = t.get("code","?")
        m = CODE_RE.match(c)
        # 2. code format + type/family agreement
        if not m:
            err(f"{c}: mã sai format <Family>-<Type><NN>")
        else:
            if m.group(1) != t.get("family"): err(f"{c}: field family='{t.get('family')}' lệch mã")
            if m.group(2) != t.get("type"):   err(f"{c}: field type='{t.get('type')}' lệch mã")
        # 3. family exists
        if t.get("family") not in fams: err(f"{c}: family '{t.get('family')}' không tồn tại")
        # 4. required fields non-blank
        for k in REQUIRED:
            v = t.get(k, None)
            if v is None or (isinstance(v,str) and not v.strip()):
                err(f"{c}: field bắt buộc trống/thiếu: {k}")
        # 5. status hợp lệ
        if t.get("status") not in STATUS_OK: err(f"{c}: status '{t.get('status')}' không hợp lệ")
        # 6. min_level hợp lệ
        ml = t.get("min_level")
        if not (isinstance(ml,int) and str(ml) in levels): err(f"{c}: min_level '{ml}' không hợp lệ")
        # 7. T phải có MVT
        if t.get("type") == "T" and not (t.get("mvt") or "").strip():
            err(f"{c}: đề tài T thiếu MVT (invariant #4)")
        # 8. advanced phải khai prerequisite
        if isinstance(ml,int) and ml >= 3:
            if not (t.get("prerequisites") or "").strip(): err(f"{c}: min_level>={ml} nhưng prerequisites trống")
            if not t.get("prereq_codes"): err(f"{c}: min_level>={ml} nhưng prereq_codes rỗng")
        # 9. prereq_codes phải resolve
        for pc in t.get("prereq_codes", []):
            pc_clean = pc.split(" ")[0]
            if CODE_RE.match(pc_clean):
                if pc_clean not in codeset: err(f"{c}: prereq_codes tham chiếu mã không tồn tại: {pc}")
            elif PAT_RE.match(pc_clean):
                fam, typ = pc_clean.split("-")[0], pc_clean.split("-")[1][0]
                if fam not in fams: err(f"{c}: prereq pattern family lạ: {pc}")
                elif not any(x["family"]==fam and x["type"]==typ for x in topics):
                    err(f"{c}: prereq pattern không khớp đề tài nào: {pc}")
            else:
                err(f"{c}: prereq_codes entry sai format: {pc}")
        # 10. mã kiểu 'A5-T2' còn sót trong text tự do
        for fld in ["prerequisites","scope","outputs","extension"]:
            for bad in re.findall(r"\b(?:A[0-7]|B[0-6]|AB)-[PITR]\d\b(?!\d)", t.get(fld,"")):
                err(f"{c}: tham chiếu mã sai format trong '{fld}': {bad}")

if rr:
    wr = rr.get("working_readiness", {})
    if len(rr.get("technical_readiness",{}).get("competencies",[])) != 16:
        err("readiness_rubrics: danh sách TR phải có đúng 16 năng lực")
    if len(wr.get("traits",[])) != 5: err("readiness_rubrics: WR phải có 5 phẩm chất")
    smax, total = wr.get("scale",{}).get("max"), wr.get("max_total")
    if smax is not None and total != 5*smax:
        err(f"readiness_rubrics: max_total={total} phải bằng 5 x scale.max={smax}")
    for k,v in wr.get("thresholds",{}).items():
        if not (isinstance(v,int) and 0 < v <= (total or 20)):
            err(f"readiness_rubrics: ngưỡng WR '{k}'={v} ngoài khoảng hợp lệ")
    rz = rr.get("research_readiness", {})
    if len(rz.get("traits",[])) != 5:
        err("readiness_rubrics: RR phải có 5 tiêu chí")
    rsmax, rtotal = rz.get("scale",{}).get("max"), rz.get("max_total")
    if rsmax is not None and rtotal != 5*rsmax:
        err(f"readiness_rubrics: RR max_total={rtotal} phải bằng 5 x scale.max={rsmax}")
    exp = rz.get("expectations", [])
    if not isinstance(exp, list) or not exp:
        err("readiness_rubrics: RR expectations phải là list không rỗng")
    else:
        for e in exp:
            for k in ["key","label","expectation"]:
                if not (e.get(k) or "").strip():
                    err(f"readiness_rubrics: RR expectation '{e.get('key')}' thiếu field {k}")
        # ngưỡng WR và kỳ vọng RR phải nói về cùng một tập loại hoạt động
        wr_keys = {"project":"P", "internship":"I", "datn_engineering":"T_engineering",
                   "datn_research_oriented":"T_research_oriented", "nckh":"R",
                   "advanced_b6_ab_r":"advanced_b6_ab_r"}
        missing = {v for v in wr_keys.values()} - {e.get("key") for e in exp}
        if missing:
            err(f"readiness_rubrics: RR expectations thiếu loại hoạt động có ngưỡng WR: {sorted(missing)}")

if mg:
    gs = mg.get("gates", [])
    if [g.get("gate") for g in gs] != [1,2,3,4,5,6]: err("milestone_gates: phải có đúng Gate 1..6 theo thứ tự")
    prev_end = 0
    for g in gs:
        if g.get("week_start") != prev_end + 1:
            err(f"milestone_gates: Gate {g.get('gate')} tuần không liên tục (bắt đầu {g.get('week_start')}, kỳ vọng {prev_end+1})")
        prev_end = g.get("week_end", prev_end)
        for k in ["name","weeks_label","pass_criteria","fail_rule"]:
            if not (g.get(k) or "").strip(): err(f"milestone_gates: Gate {g.get('gate')} thiếu {k}")
    if prev_end != 15: warn(f"milestone_gates: tổng tuần = {prev_end} (kỳ vọng 15)")

    rl = mg.get("research_ladder") or {}
    lg = rl.get("gates", [])
    if [g.get("id") for g in lg] != [f"G{i}" for i in range(8)]:
        err("milestone_gates.research_ladder: phải có đúng G0..G7 theo thứ tự")
    gate_ids = {g.get("gate") for g in gs}
    for g in lg:
        m = g.get("maps_to_gate")
        if isinstance(m, int) and m not in gate_ids:
            err(f"research_ladder {g.get('id')}: maps_to_gate={m} không có trong Gate 1..6")
        if not g.get("pass_criteria"):
            err(f"research_ladder {g.get('id')}: thiếu pass_criteria")
        if not (g.get("fail_rule") or "").strip():
            err(f"research_ladder {g.get('id')}: thiếu fail_rule")
    for g in gs:
        for gid in g.get("research_gates", []):
            if gid not in {x.get("id") for x in lg}:
                err(f"milestone_gates: Gate {g.get('gate')} trỏ tới {gid} không có trong research_ladder")

if rp and pf:
    by_code = {t["code"]: t for t in pf.get("topics", [])}
    packs = rp.get("packs", [])
    ids, pcodes = [], []
    REQ = ["code", "pack_id", "track", "title_vi", "title_en", "title_registration_vi",
           "title_registration_en", "research_question", "paper_potential", "depends_on",
           "must_read", "must_understand", "must_build", "experiments", "evidence",
           "paper_threshold", "mentor_questions", "red_flags"]
    tracks = {t.get("track") for t in rp.get("tracks", [])}
    for p in packs:
        c = p.get("code", "?")
        pcodes.append(c); ids.append(p.get("pack_id"))
        for k in REQ:
            if k not in p:
                err(f"research_packs {c}: thiếu trường '{k}'")
            elif k != "depends_on" and not p[k]:
                err(f"research_packs {c}: trường '{k}' rỗng")
        if c not in by_code:
            err(f"research_packs {c}: mã không có trong project_portfolio.json")
        else:
            for k in ("title_vi", "title_en"):
                if p.get(k) != by_code[c].get(k):
                    err(f"research_packs {c}: {k} lệch danh mục — phải lấy nguyên từ project_portfolio.json")
        if p.get("track") not in tracks:
            err(f"research_packs {c}: track '{p.get('track')}' không khai báo trong 'tracks'")
        if len(p.get("mentor_questions") or []) != 4:
            err(f"research_packs {c}: mentor_questions phải có đúng 4 câu (lộ trình dùng ở tuần 1, 3, 8, 12)")
    for x in (ids, pcodes):
        dup = {v for v in x if x.count(v) > 1}
        if dup: err(f"research_packs: trùng lặp {sorted(dup)}")
    idset = set(ids)
    for p in packs:
        for d in p.get("depends_on", []):
            if d not in idset:
                err(f"research_packs {p.get('code')}: depends_on trỏ pack_id không tồn tại: {d}")
    # phát hiện phụ thuộc vòng
    dep = {p["pack_id"]: list(p.get("depends_on", [])) for p in packs if p.get("pack_id")}
    seen_, stack_ = set(), set()
    def walk(n):
        if n in stack_: err(f"research_packs: phụ thuộc vòng tại {n}"); return
        if n in seen_: return
        stack_.add(n)
        for m in dep.get(n, []): walk(m)
        stack_.discard(n); seen_.add(n)
    for n in dep: walk(n)
    if not (rp.get("depth_levels") and len(rp["depth_levels"]) == 4):
        err("research_packs: depth_levels phải có đúng 4 mức D0..D3")
    if len(rp.get("rules", [])) < 4:
        err("research_packs: thiếu bộ 4 quy tắc không thương lượng")

for cpath in cohorts:
    co = json.loads(cpath.read_text(encoding="utf-8"))
    name = cpath.name
    if pf:
        codeset = {t["code"] for t in pf["topics"]}
        aliases = [x.get("alias") for x in co.get("topics",[])]
        if len(aliases) != len(set(aliases)): err(f"{name}: alias trùng lặp")
        for x in co.get("topics", []):
            if x.get("code") not in codeset: err(f"{name}: alias {x.get('alias')} trỏ mã không tồn tại: {x.get('code')}")
            else:
                t = next(t for t in pf["topics"] if t["code"]==x["code"])
                if t["type"] != co.get("activity_type","T"):
                    err(f"{name}: {x['code']} không phải type {co.get('activity_type')}")
                al = (t.get("cohort_alias") or {}).get(co.get("cohort_id",""))
                if al != x.get("alias"):
                    err(f"{name}: alias '{x.get('alias')}' lệch cohort_alias trong portfolio ('{al}') cho {x['code']}")
        # career guide dùng mã tồn tại
        for gset in co.get("career_guide", []):
            for ref in gset.get("primary",[]) + gset.get("next",[]):
                ref0 = ref.split(" ")[0]
                if CODE_RE.match(ref0) and ref0 not in codeset:
                    err(f"{name}: career_guide tham chiếu mã lạ: {ref}")
    # --- khung tuần là TƯƠNG ĐỐI: cohort chỉ khai start_date, mọi ngày đều suy ra ---
    frame_weeks = (mg.get("frame", {}) or {}).get("duration_weeks") or max(
        (g.get("week_end", 0) for g in mg.get("gates", [])), default=0)
    dw = co.get("duration_weeks")
    if dw != frame_weeks:
        err(f"{name}: duration_weeks={dw} nhưng khung gate dài {frame_weeks} tuần")

    for legacy in ("week_calendar", "gate_deadlines", "end_date"):
        if legacy in co:
            err(f"{name}: không được lưu '{legacy}' trong cohort — ngày phải suy ra từ start_date "
                f"bằng scripts/cohort_schedule.py. Xóa trường này để tránh hai nguồn ngày lệch nhau.")

    sd = co.get("start_date")
    if sd:
        try:
            datetime.date.fromisoformat(sd)
        except ValueError:
            err(f"{name}: start_date '{sd}' không phải ngày ISO dạng YYYY-MM-DD")

    for b in (co.get("breaks") or []):
        if not isinstance(b, dict) or "after_week" not in b:
            err(f"{name}: mỗi mục trong breaks phải có 'after_week' (kèm tùy chọn 'weeks', 'reason')")
            continue
        aw = b.get("after_week")
        if not isinstance(aw, int) or not (1 <= aw < (dw or 1)):
            err(f"{name}: breaks.after_week={aw} phải nằm trong khoảng 1..{(dw or 1) - 1}")

    cal = cohort_schedule.build_calendar(sd, dw or 0, co.get("breaks"))
    if sd and len(cal) != dw:
        err(f"{name}: lịch suy ra được {len(cal)} tuần nhưng khóa dài {dw} tuần")
    for g in mg.get("gates", []):
        if g.get("week_end", 0) > (dw or 0):
            err(f"{name}: Gate {g.get('gate')} kết ở tuần {g.get('week_end')} — vượt quá {dw} tuần của khóa")

print("=" * 56)
if errors:
    print(f"VALIDATION FAIL — {len(errors)} lỗi:")
    for e in errors: print("  ✗", e)
else:
    print("VALIDATION PASS — dữ liệu nguồn chuẩn nhất quán.")
if warnings:
    print(f"{len(warnings)} cảnh báo:")
    for w in warnings: print("  !", w)
print(f"Đã kiểm: {len(pf['topics']) if pf else 0} topics · rubrics · gates · "
      f"{len(rp['packs']) if rp else 0} research pack(s) · {len(cohorts)} cohort file(s).")
sys.exit(1 if errors else 0)
