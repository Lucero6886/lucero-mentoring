# -*- coding: utf-8 -*-
"""Suy ra lịch của một khóa từ khung tuần tương đối.

NGUYÊN TẮC: khung tiến độ của chương trình là **tương đối** — đếm theo số tuần
kể từ ngày sinh viên chính thức nhận đề tài. Nó dùng chung cho mọi khóa, mọi học
kỳ, mọi loại hoạt động; không khóa vào một lịch cụ thể nào.

Ngày tháng chỉ là **lớp phủ của từng khóa**: file `06_Data/cohort_*.json` chỉ cần
khai `start_date`, còn lịch từng tuần và hạn từng gate được suy ra ở đây. Nhờ vậy
không có ngày nào bị lưu trùng ở hai nơi — và do đó không thể lệch nhau.

Khóa không công bố ngày (`start_date` để trống) vẫn chạy được: mọi tài liệu khi đó
chỉ hiển thị mốc tuần, ví dụ *"hết tuần 5"*.

Dùng chung bởi: validate_portfolio.py · generate_catalogs.py · generate_site.py ·
generate_ban_do.py
"""
import datetime


def build_calendar(start_date, duration_weeks, breaks=None):
    """Sinh lịch tuần: [{week, start, end}, ...]

    Mỗi tuần dài 7 ngày và nối tiếp nhau. `breaks` cho phép chèn kỳ nghỉ giữa kỳ:
        [{"after_week": 8, "weeks": 1, "reason": "Nghỉ giữa kỳ"}]
    Trả về [] nếu khóa chưa công bố ngày bắt đầu.
    """
    if not start_date:
        return []
    day = datetime.date.fromisoformat(start_date)
    pause = {int(b["after_week"]): int(b.get("weeks", 1)) for b in (breaks or [])}
    cal = []
    for w in range(1, int(duration_weeks) + 1):
        cal.append({"week": w,
                    "start": day.isoformat(),
                    "end": (day + datetime.timedelta(days=6)).isoformat()})
        day += datetime.timedelta(days=7)
        if w in pause:
            day += datetime.timedelta(days=7 * pause[w])
    return cal


def gate_deadlines(gates, calendar):
    """{ '1': '2026-09-20', ... } — hạn mỗi gate là ngày cuối tuần mà gate đó khép lại.

    Trả về {} khi khóa chưa công bố ngày.
    """
    end_of = {w["week"]: w["end"] for w in calendar}
    return {str(g["gate"]): end_of[g["week_end"]]
            for g in gates if g.get("week_end") in end_of}


def end_date(calendar):
    """Ngày kết thúc khóa, hoặc None nếu chưa công bố ngày."""
    return calendar[-1]["end"] if calendar else None


def dmy(iso):
    """2026-09-20 → 20/09/2026. Chuỗi rỗng nếu không có ngày."""
    if not iso:
        return ""
    y, m, d = str(iso).split("-")
    return f"{d}/{m}/{y}"


def week_label(gate):
    """Nhãn tuần tương đối: 'Tuần 3–5' hoặc 'Tuần 7'."""
    a, b = gate.get("week_start"), gate.get("week_end")
    return f"Tuần {a}" if a == b else f"Tuần {a}–{b}"


def due_label(gate, deadlines=None):
    """Hạn của gate, ưu tiên mốc tuần và chỉ thêm ngày khi khóa có công bố.

    'hết tuần 5'              — khóa chưa công bố ngày
    'hết tuần 5 · 11/10/2026' — khóa đã công bố ngày bắt đầu
    """
    base = f"hết tuần {gate.get('week_end')}"
    iso = (deadlines or {}).get(str(gate.get("gate")))
    return f"{base} · {dmy(iso)}" if iso else base


def due_compact(gate, deadlines=None):
    """Nhãn hạn ngắn, dùng khi cột đã có sẵn mốc tuần: '20/09/2026' hoặc 'hết tuần 5'."""
    iso = (deadlines or {}).get(str(gate.get("gate")))
    return dmy(iso) if iso else f"hết tuần {gate.get('week_end')}"


def frame_note(cohort=None, calendar=None):
    """Câu giải thích khung tuần, dùng chung ở đầu các tài liệu có bảng gate."""
    s = ("Mọi mốc dưới đây tính theo **số tuần kể từ ngày sinh viên chính thức nhận đề tài** "
         "— khung này dùng chung cho mọi khóa, không gắn với một học kỳ cụ thể.")
    if calendar:
        s += (f" Khóa hiện tại bắt đầu **{dmy(calendar[0]['start'])}**, "
              f"nên tuần 1 là {dmy(calendar[0]['start'])}–{dmy(calendar[0]['end'])} "
              f"và ngày tương ứng của từng mốc được ghi kèm.")
    else:
        s += " Khóa này chưa công bố ngày bắt đầu, nên chỉ hiển thị mốc tuần."
    return s
