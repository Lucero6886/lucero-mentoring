#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sinh bộ hồ sơ thực thi chiều sâu cho từng đề tài nghiên cứu.

Vì sao cần: danh mục đề tài trả lời *"có những đề tài nào"*. Nó không trả lời
*"làm đề tài đó cụ thể ra sao"* — phải đọc gì, hiểu gì trước khi gõ dòng code đầu
tiên, dựng cái gì, chạy thí nghiệm nào, nộp bằng chứng gì, và khi nào mới đủ điều
kiện nghĩ tới một bài báo. Đó là khoảng trống mà bộ hồ sơ này lấp.

Nguyên tắc: **06_Data/research_packs.json là bản gốc duy nhất**. Toàn bộ file
trong 02_Project_Portfolio/Research_Packs/ đều sinh tự động — sửa tay sẽ bị ghi
đè ở lần chạy sau. Muốn đổi nội dung thì sửa JSON rồi chạy lại script này.

Lộ trình tuần bám khung tương đối của chương trình (milestone_gates.json):
mọi mốc đếm theo **số tuần kể từ ngày sinh viên chính thức nhận đề tài**, nên bộ
hồ sơ dùng được cho mọi khóa mà không phải sửa ngày ở đâu cả.

Cách dùng (từ thư mục gốc dự án):
    python3 scripts/generate_research_packs.py
"""
import json, pathlib, sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import cohort_schedule as cs

BASE = pathlib.Path(__file__).resolve().parents[1]
DATA = BASE / "06_Data"
OUT = BASE / "02_Project_Portfolio" / "Research_Packs"

BANNER = ("> **File sinh tự động** từ `06_Data/research_packs.json` bằng "
          "`scripts/generate_research_packs.py`. Sửa tay sẽ bị ghi đè — "
          "muốn đổi nội dung thì sửa JSON rồi chạy lại script.\n")

SIG = ("**Engineering & Research Mentoring Program (Lucero)** · "
       "ThS. Đinh Văn Nam (Mr. Lucero Dinh) — Khoa Điện–Điện tử, Trường Kỹ thuật, Đại học Phenikaa")


def load(name):
    return json.loads((DATA / name).read_text(encoding="utf-8"))


def bullets(items):
    return "\n".join(f"- {x}" for x in items) if items else "_(chưa khai báo)_"


def numbered(items):
    return "\n".join(f"{i}. {x}" for i, x in enumerate(items, 1))


# ---------------------------------------------------------------- lộ trình tuần
# Mỗi dòng: (tuần, mốc, việc sinh viên làm, bằng chứng nộp, câu hỏi mentor chung,
#            chỉ số câu hỏi riêng của đề tài hoặc None, điều kiện qua)
WEEKS = [
 (1,  "Nhận đề tài · nền khái niệm",
      "Đọc START-HERE, chốt phạm vi, kiểm tra tiên quyết, dựng môi trường; tự viết glossary.",
      "Sơ đồ vấn đề một trang + glossary + trả lời câu hỏi sẵn sàng.",
      "Giải thích đề tài trong 2 phút, không slide, không AI: đầu vào, đầu ra, baseline, metric là gì?",
      0, "G0 đạt."),
 (2,  "Tài liệu · câu hỏi nghiên cứu",
      "Hoàn thành bảng so sánh tài liệu; phát biểu vấn đề, câu hỏi nghiên cứu, giả thuyết, phạm vi và non-goals.",
      "Literature matrix 8–15 nguồn + problem statement + RQ.",
      "Bài nào gần câu hỏi của em nhất? Khoảng trống nào là thật, khoảng trống nào chỉ là chưa ai cài đặt?",
      None, "**Gate 1 đạt** (G0 + G1)."),
 (3,  "Thiết kế baseline",
      "Chốt baseline, đầu vào/đầu ra, metric và giao thức thí nghiệm.",
      "Baseline spec + test plan.",
      "Baseline này đã đủ mạnh và công bằng chưa?",
      1, "Mentor duyệt tính công bằng của baseline."),
 (4,  "Cài đặt baseline",
      "Cài đặt hoặc chuẩn hóa baseline; viết unit test cho phần dễ sai nhất.",
      "Code + test chạy xanh.",
      "Unit test nào có thể bắt được lỗi logic nguy hiểm nhất?",
      None, "Các unit test cốt lõi đều qua."),
 (5,  "Baseline chạy đầu-cuối · kiểm chứng",
      "Chạy đầu-cuối, sanity check, đối chiếu với vector đã biết hoặc tài liệu.",
      "Log baseline + hình đầu tiên + ghi chú kiểm chứng.",
      "Nếu baseline lệch tài liệu, em đã loại trừ những nguyên nhân nào? Kiểm chứng độc lập nào cho thấy cài đặt đúng chứ không chỉ tự nhất quán?",
      None, "**Gate 2 đạt** (G2). Chưa đạt thì không mở phần mở rộng nghiên cứu."),
 (6,  "Phương pháp đề xuất v1",
      "Cài đặt kiến trúc hoặc phương pháp cần khảo sát.",
      "Block diagram/pseudocode + code v1.",
      "Phương pháp mới thay đổi đúng **một** cơ chế nào so với baseline?",
      None, "G3 một phần."),
 (7,  "Hoàn thiện · trường hợp biên",
      "Hoàn thiện cài đặt, xử lý trường hợp biên.",
      "Kết quả regression.",
      "Trường hợp biên nào có thể làm hỏng thiết kế này?",
      None, "Regression không phá baseline."),
 (8,  "Chốt phương pháp đề xuất",
      "Đóng băng phiên bản đem đi đo; ghi rõ chi phí phát sinh so với baseline.",
      "Bản v2 + bảng so sánh chi phí.",
      "Chi phí mới sinh ra ở đâu?",
      2, "**Gate 3 đạt** (G3)."),
 (9,  "Khóa ma trận thí nghiệm",
      "Khóa biến độc lập, biến kiểm soát, metric, số seed/mẫu/frame **trước khi chạy**.",
      "EXPERIMENT-PLAN với Experiment ID.",
      "Thí nghiệm này trả lời đúng một câu hỏi nghiên cứu nào? Biến nào bắt buộc giữ cố định?",
      None, "Mentor duyệt giao thức."),
 (10, "Thí nghiệm chính · đợt 1",
      "Chạy sweep/thí nghiệm chính; lưu kết quả thô, không ghi đè.",
      "Kết quả thô + log + config.",
      "Kết quả hiện tại có thể do yếu tố gây nhiễu nào thay vì do phương pháp đề xuất?",
      None, "Không chọn lọc kết quả; chạy lại được."),
 (11, "Sensitivity · chiều thứ hai",
      "Chạy chiều biến thứ hai hoặc khảo sát độ nhạy.",
      "Kết quả thô + kết quả đã xử lý.",
      "Xu hướng có ổn định khi đổi seed, SNR, config hoặc kích thước không?",
      None, "**Gate 4 đạt** (G4). Sau tuần này không thêm thuật toán lớn mới."),
 (12, "Phân tích · failure case",
      "Giải thích xu hướng bằng nguyên nhân; tìm và mô tả failure case.",
      "2–4 hình/bảng + phân tích.",
      "Failure case quan trọng nhất là gì?",
      3, "G5 đạt."),
 (13, "Bản thảo · phát biểu đóng góp",
      "Viết kết luận, đóng góp và giới hạn; mỗi kết luận trỏ tới một hình/bảng/log.",
      "Bản thảo báo cáo/khóa luận + ghi chú nghiên cứu 2 trang.",
      "Nếu chỉ được giữ một kết luận, kết luận nào có bằng chứng mạnh nhất?",
      None, "**Gate 5 đạt**."),
 (14, "Tái lập",
      "Clone sạch và chạy lại từ README; script tạo lại hình chính; tách kết quả thô/đã xử lý.",
      "Checklist tái lập + script sinh hình.",
      "Người khác có thể clone và tạo lại hình chính mà không hỏi em không?",
      None, "G6 đạt."),
 (15, "Bảo vệ · bàn giao · chuyển giao giảng dạy",
      "Dọn repository, chuẩn bị slide/demo, viết Teaching Transfer Note, bàn giao cho khóa sau.",
      "Repo cuối + slide + teaching note.",
      "Điều gì của đề tài này nên trở thành tài sản dùng lại cho khóa sau và cho bài giảng?",
      None, "**Gate 6 đạt** — kết thúc đề tài."),
]

STOP_RULES = [
 "Gate 2 chưa đạt thì không chuyển sang phương pháp đề xuất.",
 "Giả thuyết sai thì ghi nhận là kết quả — không uốn dữ liệu để cứu giả thuyết.",
 "Phương pháp đề xuất không tạo lợi ích ròng thì cân nhắc đổi hướng hoặc dừng, thay vì cố viết bài.",
 "Sinh viên không giải thích được đoạn code do AI sinh ra thì mốc tuần đó không đạt.",
]

READING_QUESTIONS = [
 "Bài này giải quyết vấn đề gì?", "Baseline của họ là gì?",
 "Giả định nào là quan trọng?", "Họ dùng metric nào?",
 "Kết quả chính là gì?", "Giới hạn của bài là gì?",
 "Phần nào tái lập được?", "Phần nào liên quan trực tiếp tới câu hỏi nghiên cứu của em?",
 "Có kết luận nào cần kiểm chứng độc lập không?",
 "Nếu chỉ lấy được một insight cho đề tài, đó là gì?",
]


def head(title, pack, extra=""):
    return (f"# {title} — {pack['code']}\n\n{SIG}\n\n{BANNER}\n"
            f"**Đề tài:** {pack['title_vi']}  \n"
            f"**English:** {pack['title_en']}  \n"
            f"**Tên đầy đủ khi đăng ký:** {pack['title_registration_vi']}  \n"
            f"**Mã đối chiếu gói gốc:** {pack['pack_id']} · "
            f"**Track {pack['track']}** — {pack['track_name']}{extra}\n\n---\n\n")


def f_start_here(p, gates, ladder):
    q = p["mentor_questions"]
    return head("START HERE", p) + f"""## Câu hỏi nghiên cứu

> {p['research_question']}

Đây là câu em phải trả lời được bằng **bằng chứng**, không phải bằng một bản cài đặt chạy được.

## Trước khi gõ dòng code đầu tiên — phải đọc

{bullets(p['must_read'])}

Tài liệu cụ thể xem `09_References/READING-LIST.md`. Sau mỗi tài liệu, trả lời {len(READING_QUESTIONS)} câu trong `READING-QUESTIONS` ở cuối file này.

## Phải hiểu được (không nhìn tài liệu)

{bullets(p['must_understand'])}

## Phải dựng

{bullets(p['must_build'])}

## Phải chạy thí nghiệm

{bullets(p['experiments'])}

## Bằng chứng bắt buộc nộp

{bullets(p['evidence'])}

## Khi nào mới đủ điều kiện nghĩ tới một bài báo

{p['paper_threshold']}

Tiềm năng công bố mentor đánh giá cho đề tài này: **{p['paper_potential']}**. Đây là ước lượng ban đầu, không phải lời hứa — quyết định thật nằm ở Gate G7.

## Bốn câu mentor sẽ hỏi đi hỏi lại

{numbered(q)}

Nếu tuần nào em cũng trả lời được bốn câu này bằng bằng chứng của chính mình, đề tài đang đi đúng.

## Bốn quy tắc không thương lượng

{numbered(RULES)}

## READING-QUESTIONS — trả lời sau mỗi tài liệu

{numbered(READING_QUESTIONS)}

---

*Lộ trình từng tuần: `ROADMAP.md` · Điều kiện qua từng cửa: `MILESTONE-GATES.md` · Thí nghiệm: `EXPERIMENTS.md`*
"""


def f_roadmap(p, gates, deadlines, note):
    q = p["mentor_questions"]
    ends = {g["week_end"]: str(g["gate"]) for g in gates}
    rows = []
    for wk, milestone, doing, evid, ask, qi, cond in WEEKS:
        if qi is not None and qi < len(q):
            ask = f"{ask} {q[qi]}"
        iso = deadlines.get(ends.get(wk, ""), "")
        if iso:
            cond = f"{cond} <br>_hạn {cs.dmy(iso)}_"
        rows.append(f"| {wk} | {milestone} | {doing} | {evid} | {ask} | {cond} |")
    return head("Lộ trình theo tuần", p) + f"""{note}

> Được phép kéo dài một mốc, **không được bỏ một cửa nào**. Mọi buổi review bắt đầu từ bằng chứng, không từ lời kể.

| Tuần | Mốc | Sinh viên làm | Nộp bằng chứng | Mentor hỏi | Điều kiện qua |
|---:|---|---|---|---|---|
{chr(10).join(rows)}

## Sau tuần 15 — cửa mở rộng G7

Chỉ mở khi đề tài có tiềm năng công bố và mentor đồng ý. Xem `PAPER-READINESS.md`.

## Quy tắc dừng

{bullets(STOP_RULES)}
"""


def f_gates(p, ladder):
    q = p["mentor_questions"]
    out = [head("Điều kiện qua từng cửa", p)]
    out.append("Bảng dưới ghép **yêu cầu chung của chương trình** (G0–G7) với **nội dung riêng của đề tài này**. "
               "G0–G6 nằm gọn trong Gate 1–6 của khung 15 tuần; G7 là cửa mở rộng.\n")
    spec = {
        "G0": ("Phải hiểu", p["g0_core_concepts"] or ", ".join(p["must_understand"])),
        "G2": ("Phải dựng", ", ".join(p["must_build"][:2])),
        "G3": ("Phải dựng", ", ".join(p["must_build"][2:]) or ", ".join(p["must_build"])),
        "G4": ("Thí nghiệm trọng tâm", ", ".join(p["experiments"])),
        "G5": ("Bằng chứng trọng tâm", ", ".join(p["evidence"])),
        "G7": ("Ngưỡng riêng của đề tài", p["paper_threshold"]),
    }
    askmap = {"G0": q[0], "G2": q[1] if len(q) > 1 else "", "G3": q[2] if len(q) > 2 else "",
              "G5": q[3] if len(q) > 3 else ""}
    for g in ladder["gates"]:
        gid = g["id"]
        out.append(f"\n## {gid} — {g['name_vi']} ({g['name']})\n")
        out.append(f"**Thuộc:** {'Gate ' + str(g['maps_to_gate']) if isinstance(g['maps_to_gate'], int) else g['maps_to_gate']}\n")
        if gid in spec and spec[gid][1]:
            out.append(f"**{spec[gid][0]} — riêng đề tài này:** {spec[gid][1]}\n")
        out.append("**Đạt khi:**\n" + bullets(g["pass_criteria"]) + "\n")
        if askmap.get(gid):
            out.append(f"**Mentor hỏi:** {askmap[gid]}\n")
        out.append(f"**Không đạt khi:** {g['fail_rule']}\n")
    return "\n".join(out)


def f_experiments(p):
    return head("Kế hoạch thí nghiệm", p) + f"""## Câu hỏi nghiên cứu

> {p['research_question']}

## Baseline

Sinh viên phải mô tả baseline cụ thể — phiên bản, cấu hình và **lý do baseline này là công bằng** — trước khi chạy bất kỳ thí nghiệm nào. Baseline yếu làm cho mọi con số phía sau mất giá trị.

## Danh mục thí nghiệm

{bullets(p['experiments'])}

## Bằng chứng cần sinh ra

{bullets(p['evidence'])}

## Trước mỗi thí nghiệm — bảy bước bắt buộc

1. Viết giả thuyết.
2. Xác định biến độc lập.
3. Khóa biến kiểm soát.
4. Chốt metric.
5. Chốt số mẫu / frame / seed.
6. Đặt Experiment ID.
7. Không đổi giao thức sau khi đã thấy kết quả — nếu buộc phải đổi thì ghi rõ lý do vào nhật ký.

## Sau mỗi thí nghiệm — năm mục bắt buộc

- **Quan sát** — con số nói gì.
- **Diễn giải** — vì sao lại thế.
- **Cách giải thích khác** — điều gì khác cũng tạo ra kết quả này.
- **Failure case** — chỗ nào không hoạt động.
- **Thí nghiệm tiếp theo** — và nó trả lời câu hỏi nào.

Mẫu ghi chép: `04_Project_Template/EXPERIMENT_LOG_TEMPLATE.md`.
"""


def f_deliverables(p, depth):
    L = {d["level"]: d for d in depth}
    return head("Sản phẩm phải nộp", p) + f"""Bốn mức chiều sâu. Đề tài dừng ở mức nào là quyết định của mentor dựa trên bằng chứng, không dựa trên nỗ lực bỏ ra.

## {L['D0']['level']} — {L['D0']['name']}: {L['D0']['meaning']}

- sơ đồ vấn đề
- glossary
- literature matrix
- câu hỏi nghiên cứu

## {L['D1']['level']} — {L['D1']['name']}: {L['D1']['meaning']}

- bản cài đặt chạy được
- test / testbench
- README
- bằng chứng kiểm chứng

## {L['D2']['level']} — {L['D2']['name']}: {L['D2']['meaning']}

- ma trận thí nghiệm có kiểm soát
- kết quả thô và kết quả đã xử lý (tách riêng)
- {", ".join(p['evidence'][:3])}
- phân tích và failure case
- gói tái lập

## {L['D3']['level']} — {L['D3']['name']}: {L['D3']['meaning']}

- checklist paper readiness
- phát biểu đóng góp
- dàn ý bản thảo
- hình/bảng đạt chuẩn bản thảo
- gói phụ lục / repository nếu phù hợp

## Chuyển giao giảng dạy (bắt buộc với mọi mức)

- Teaching Transfer Note 2–4 trang
- 1 block diagram
- 1 bài lab tối thiểu
- 1 hiểu lầm thường gặp
- 1 câu hỏi đánh giá

Mẫu: `04_Project_Template/TEACHING_TRANSFER_NOTE.md`.
"""


def f_mentor(p, deps_txt):
    return head("Ghi chú cho mentor", p) + f"""## Câu hỏi nghiên cứu

> {p['research_question']}

## Bốn câu hỏi trọng tâm

{numbered(p['mentor_questions'])}

## Ngưỡng công bố

{p['paper_threshold']}

**Tiềm năng đánh giá ban đầu:** {p['paper_potential']}

## Phụ thuộc

{deps_txt}

## Cảnh báo sớm

{bullets(p['red_flags'])}

## Sau mỗi mốc

Ghi lại vào `04_Project_Template/MENTOR_LESSONS_LEARNED.md`: sinh viên hiểu sai chỗ nào, thiếu kiến thức tiên quyết nào, cách giải thích nào có tác dụng, thí nghiệm nào gây hiểu nhầm, tài liệu nào tốt nhất, và lần sau nên đổi gì.

## Checklist tuần

`03_Operations/MENTOR_WEEKLY_CHECKLIST.md` · Thang chấm: `03_Operations/PASS_FAIL_RUBRIC.md`
"""


def f_paper(p):
    return head("Sẵn sàng viết bài (G7)", p) + f"""> Cửa này **không nằm trong khung 15 tuần**. Nó chỉ mở khi Gate 1–6 đã đạt và mentor thấy có bằng chứng đủ mạnh.

## Ngưỡng riêng của đề tài này

{p['paper_threshold']}

## Điều kiện chung

- [ ] G0–G6 đã đạt.
- [ ] Câu hỏi nghiên cứu đã được trả lời bằng bằng chứng.
- [ ] Có baseline mạnh và công bằng.
- [ ] Có khảo sát độ nhạy / robustness phù hợp.
- [ ] Có ít nhất một insight không hiển nhiên.
- [ ] Có phần giới hạn.
- [ ] Repository clone sạch và chạy lại được.
- [ ] Hình/bảng đạt chuẩn bản thảo.
- [ ] Phát biểu đóng góp **không vượt quá** bằng chứng đang có.

## Kết luận nghiên cứu (tối đa 3 câu)

## Đóng góp

1.
2.
3.

## Tính công bằng của so sánh

- [ ] Cùng dữ liệu / kênh / cấu hình
- [ ] Cùng giả định về điều kiện dừng và độ trễ
- [ ] Đã có baseline mạnh
- [ ] Không chọn lọc kết quả đẹp

## Quyết định

- [ ] Chỉ là đề tài kỹ thuật
- [ ] Báo cáo nghiên cứu nội bộ / sinh viên
- [ ] Ứng viên hội nghị sinh viên
- [ ] Ứng viên hội nghị trong nước
- [ ] Ứng viên hội nghị / letter quốc tế

Mẫu đầy đủ: `04_Project_Template/PAPER_READINESS_TEMPLATE.md`.
"""


def f_registration(p):
    exps = p["experiments"]
    return head("Nội dung đăng ký đề tài", p) + f"""> Dùng để điền vào biểu mẫu đăng ký của Khoa/Trường. Nội dung sinh từ dữ liệu gốc nên không lệch với danh mục.

## Tên đề tài

**{p['title_registration_vi']}**

**English:** {p['title_registration_en']}

_Mã trong danh mục: `{p['code']}` — {p['title_vi']}_

## Mục tiêu nghiên cứu

- Làm rõ và kiểm chứng câu hỏi nghiên cứu: {p['research_question']}
{chr(10).join(f"- Xây dựng và triển khai: {b}." for b in p['must_build'])}
- Thực hiện đánh giá có kiểm soát theo các thí nghiệm trọng tâm: {", ".join(exps[:3])}.
- Đánh giá kết quả bằng chỉ số định lượng, bảo đảm khả năng tái lập và phân tích giới hạn.
- Phát triển năng lực đọc tài liệu, thiết kế thí nghiệm, kiểm chứng, phân tích và viết báo cáo khoa học.

## Dự kiến sản phẩm, kết quả

- Repository mã nguồn/thiết kế, cấu hình và hướng dẫn tái lập.
{chr(10).join(f"- {e}" for e in p['evidence'])}
- Báo cáo và slide trình bày.
- Teaching Transfer Note để tái sử dụng trong đào tạo.
- Phấn đấu hoàn thiện bản thảo bài báo nếu đạt cửa G7.

## Dự kiến tham gia giải thưởng nghiên cứu khoa học sinh viên

- Hội nghị sinh viên nghiên cứu khoa học cấp Khoa/Trường.
- Các giải thưởng nghiên cứu khoa học sinh viên cấp Trường/Bộ hoặc cuộc thi học thuật chuyên ngành phù hợp.
- Kết quả đạt chất lượng được định hướng hoàn thiện thành bài báo hội nghị/tạp chí; **không cam kết công bố trước khi đạt cửa G7**.

## Ghi chú định hướng công bố

{p['paper_threshold']}
"""


def main():
    rp = load("research_packs.json")
    port = load("project_portfolio.json")
    mg = load("milestone_gates.json")
    ladder = mg["research_ladder"]
    global RULES
    RULES = rp["rules"]

    by_code = {t["code"]: t for t in port["topics"]}
    by_pack = {p["pack_id"]: p for p in rp["packs"]}

    # lớp phủ ngày của khóa hiện hành, nếu có
    cohorts = sorted(DATA.glob("cohort_*.json"))
    cal, deadlines, note = [], {}, cs.frame_note()
    if cohorts:
        co = json.loads(cohorts[-1].read_text(encoding="utf-8"))
        cal = cs.build_calendar(co.get("start_date"), mg["frame"]["duration_weeks"], co.get("breaks"))
        deadlines = cs.gate_deadlines(mg["gates"], cal)
        note = cs.frame_note(co, cal)

    OUT.mkdir(parents=True, exist_ok=True)
    codes = {p["code"] for p in rp["packs"]}
    stale = sorted(d.name for d in OUT.iterdir() if d.is_dir() and d.name not in codes)
    if stale:
        print("  ! thư mục thừa (đề tài đã gỡ khỏi JSON), xóa thủ công:", ", ".join(stale))

    missing = [p["code"] for p in rp["packs"] if p["code"] not in by_code]
    if missing:
        print("LỖI: mã không có trong danh mục:", ", ".join(missing))
        return 1

    for p in rp["packs"]:
        d = OUT / p["code"]
        d.mkdir(exist_ok=True)
        deps = [f"`{by_pack[x]['code']}` ({x})" for x in p["depends_on"] if x in by_pack]
        deps_txt = ("Cần baseline của " + ", ".join(deps) + " trước khi mở."
                    if deps else "Không phụ thuộc đề tài nào — có thể mở ngay.")
        (d / "START-HERE.md").write_text(f_start_here(p, mg["gates"], ladder), encoding="utf-8")
        (d / "ROADMAP.md").write_text(f_roadmap(p, mg["gates"], deadlines, note), encoding="utf-8")
        (d / "MILESTONE-GATES.md").write_text(f_gates(p, ladder), encoding="utf-8")
        (d / "EXPERIMENTS.md").write_text(f_experiments(p), encoding="utf-8")
        (d / "DELIVERABLES.md").write_text(f_deliverables(p, rp["depth_levels"]), encoding="utf-8")
        (d / "MENTOR-NOTES.md").write_text(f_mentor(p, deps_txt), encoding="utf-8")
        (d / "PAPER-READINESS.md").write_text(f_paper(p), encoding="utf-8")
        (d / "REGISTRATION.md").write_text(f_registration(p), encoding="utf-8")

    (OUT / "README.md").write_text(index_page(rp, by_code, by_pack), encoding="utf-8")
    (BASE / "03_Operations" / "STATUS_BOARD.md").write_text(status_board(rp, by_pack), encoding="utf-8")

    n = sum(1 for _ in OUT.rglob("*.md"))
    print(f"XONG — {len(rp['packs'])} gói · {n} file trong 02_Project_Portfolio/Research_Packs/")
    print("      + 03_Operations/STATUS_BOARD.md")
    return 0


def index_page(rp, by_code, by_pack):
    rows, secs = [], []
    for tr in rp["tracks"]:
        ps = [p for p in rp["packs"] if p["track"] == tr["track"]]
        if not ps:
            continue
        secs.append(f"\n### Track {tr['track']} — {tr['name']}\n\n_{tr['focus']}_\n")
        secs.append("| Mã đề tài | Tên | Mức vào | Phụ thuộc | Tiềm năng công bố | Hồ sơ |")
        secs.append("|---|---|---|---|---|---|")
        for p in ps:
            t = by_code[p["code"]]
            dep = ", ".join(by_pack[x]["code"] for x in p["depends_on"] if x in by_pack) or "—"
            secs.append(f"| `{p['code']}` | {p['title_vi']} | L{t['min_level']} | {dep} | "
                        f"{p['paper_potential']} | [mở]({p['code']}/START-HERE.md) |")
    order, waves = [], {}
    for p in rp["packs"]:
        dep = tuple(by_pack[x]["code"] for x in p["depends_on"] if x in by_pack)
        order.append((p["code"], dep))
        waves.setdefault(dep, []).append(p["code"])
    ready = waves.pop((), [])
    wave_lines = "\n".join(
        f"- **Sau khi {' và '.join('`' + c + '`' for c in dep)} có baseline chạy được:** "
        + ", ".join(f"`{c}`" for c in codes)
        for dep, codes in sorted(waves.items(), key=lambda kv: (len(kv[0]), kv[0])))
    return f"""# Hồ sơ thực thi chiều sâu — {len(rp['packs'])} đề tài nghiên cứu

{SIG}

{BANNER}
Danh mục đề tài trả lời câu hỏi *"có những đề tài nào"*. Thư mục này trả lời câu tiếp theo:
*"làm đề tài đó cụ thể ra sao"*. Mỗi đề tài có tám file: phải đọc gì, hiểu gì, dựng gì,
chạy thí nghiệm nào, nộp bằng chứng gì, điều kiện qua từng cửa, và khi nào mới đủ điều kiện
nghĩ tới một bài báo.

Đây là **{len(rp['packs'])} đề tài đã được chuẩn bị tới mức thực thi**, chọn từ danh mục
{len(by_code)} đề tài của chương trình. Các đề tài còn lại vẫn mở, chỉ chưa có lớp hồ sơ này.

## Bốn quy tắc không thương lượng

{numbered(rp['rules'])}

## Mức chiều sâu hoàn thành

| Mức | Tên | Nghĩa |
|---|---|---|
{chr(10).join(f"| **{d['level']}** | {d['name']} | {d['meaning']} |" for d in rp['depth_levels'])}

> Đừng nhầm với **L0–L5** trong danh mục đề tài: L là *mức sinh viên khi bắt đầu*,
> D là *mức chiều sâu khi kết thúc*. Một sinh viên L2 vẫn có thể đưa đề tài tới D2.
{chr(10).join(secs)}

## Thứ tự kích hoạt

Không cần đợi đề tài trước xong 100%, nhưng **phải tôn trọng phụ thuộc**.

- **Mở được ngay:** {", ".join(f"`{c}`" for c in ready)}
{wave_lines}

> **Quy tắc baseline dùng chung.** {rp['shared_baseline_rule']}

## Cách mentor vận hành nhóm này

Xem `10_Documentation/RESEARCH-TRACKS.md` — họp theo track chứ không họp riêng từng đề tài,
điều kiện được escalation, và thang chấm PASS/FAIL.

## Bảng trạng thái

`03_Operations/STATUS_BOARD.md` — cập nhật sau mỗi buổi review.
"""


def status_board(rp, by_pack):
    rows = [f"| `{p['code']}` | {p['pack_id']} | {p['track']} | — | Kho đề tài | G0 | — | Giao sinh viên |"
            for p in rp["packs"]]
    return f"""# Bảng trạng thái đề tài nghiên cứu

{SIG}

{BANNER}
Bảng này là **khung khởi tạo**. Mentor cập nhật cột trạng thái sau mỗi buổi review —
nhưng **không sửa file này**: nó bị ghi đè mỗi lần chạy lại script. Chép sang
`07_Private/` (không đẩy lên GitHub) hoặc theo dõi bằng Project board trên GitHub,
xem `10_Documentation/GITHUB-WORKFLOW.md`.

| Mã | Gói | Track | Sinh viên/Nhóm | Trạng thái | Cửa hiện tại | Bằng chứng gần nhất | Quyết định tiếp theo |
|---|---|---|---|---|---|---|---|
{chr(10).join(rows)}

## Quy ước trạng thái

- **Kho đề tài** — đã chuẩn bị, chưa giao.
- **Đang chạy** — đã giao, đang trong khung 15 tuần.
- **Tạm dừng** — chờ tiên quyết hoặc chờ quyết định của mentor.
- **Đổi hướng** — đã đổi phạm vi sau khi không đạt một cửa.
- **Hoàn thành** — Gate 6 đạt.
- **Ứng viên công bố** — đã qua G7.
"""


if __name__ == "__main__":
    sys.exit(main())
