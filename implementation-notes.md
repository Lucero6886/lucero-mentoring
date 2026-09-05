# Tài liệu hệ thống — Engineering & Research Mentoring Program (Lucero)

**ThS. Đinh Văn Nam (Mr. Lucero Dinh)** — Khoa Điện–Điện tử, Trường Kỹ thuật, Đại học Phenikaa
Phiên bản hệ thống **1.10.0** · cập nhật **04/09/2026**

> Đây là tài liệu dành cho **người vận hành**: mentor, giảng viên đồng hướng dẫn, và bất kỳ ai
> (kể cả một phiên AI về sau) phải sửa hệ thống này mà không được làm hỏng nó. Nó đi từ **bản chất**
> — hệ thống giải quyết vấn đề gì và bằng ý tưởng nào — tới **triển khai** — chạy lệnh nào, sửa file
> nào, tuần nào làm gì.
>
> Sinh viên **không cần** đọc file này. Phần dành cho sinh viên là
> [`10_Documentation/STUDENT-GUIDE.md`](10_Documentation/STUDENT-GUIDE.md) và
> [trang Guide Notes](https://lucero6886.github.io/lucero-mentoring/guide.html).

**Đọc theo nhu cầu:**

| Anh đang cần gì | Đọc mục |
|---|---|
| Hiểu hệ thống này *là gì* trong 10 phút | §1 · §2 |
| Biết dữ liệu nằm đâu, sửa ở đâu thì an toàn | §3 · §4 |
| Chạy lại toàn bộ tài liệu sau khi sửa | §5 |
| Vận hành một học kỳ: tuần nào làm gì | §6 |
| Đưa lên GitHub, phát cho sinh viên | §7 |
| Làm một việc cụ thể (thêm đề tài, mở khóa mới…) | §8 |
| Biết cái gì tuyệt đối không được đụng | §9 |

---

## 1. Bản chất

### 1.1 Vấn đề

Một mentor có thể hướng dẫn tốt hai sinh viên. Với mười lăm, ba thứ vỡ cùng lúc:

1. **Không nhìn thấy tiến độ thật.** Sinh viên báo "em đang làm" suốt sáu tuần, tới tuần mười hai
   mới lộ ra là chưa có gì chạy được. Lúc đó cứu không kịp.
2. **Chuẩn trôi theo người.** Em chăm thì được thông cảm, em ít gặp thì bị đánh giá thấp — trong khi
   cái đáng đo là **bằng chứng**, không phải nỗ lực hay tần suất xuất hiện.
3. **Mỗi khóa bắt đầu lại từ số không.** Đề tài, kinh nghiệm, môi trường, lỗi đã gặp — tất cả tan
   theo sinh viên tốt nghiệp. Khóa sau tốn lại đúng số tuần đó cho đúng những lỗi đó.

### 1.2 Ý tưởng

Hệ thống này chỉ có **một ý tưởng**, ba lớp còn lại đều là hệ quả:

> **Thay "mentor theo dõi từng người" bằng "mọi người đi qua cùng một khuôn, và khuôn đó
> đòi bằng chứng ở những điểm cố định."**

Khi khuôn đủ rõ, mentor không cần nhớ mười lăm câu chuyện — chỉ cần hỏi *"tuần này em ở cửa nào,
bằng chứng đâu"*. Khi bằng chứng là thứ được chấm, sự chăm chỉ không còn thay thế được kết quả, và
sinh viên biết trước mình bị đánh giá bằng gì. Khi khuôn dùng chung cho nhiều khóa, thứ để lại
được cho khóa sau là **tài sản**, không phải kỷ niệm.

### 1.3 Ba lớp

| Lớp | Trả lời câu hỏi | Nằm ở đâu |
|---|---|---|
| **Danh mục** | *Có những đề tài nào?* | `06_Data/project_portfolio.json` → catalog, trang web, phiếu đăng ký |
| **Thực thi** | *Làm đề tài đó cụ thể ra sao?* | `06_Data/research_packs.json` → `Topic_Guides/` (105 trang), `Research_Packs/` (13 hồ sơ sâu) |
| **Vận hành** | *Mentor và sinh viên làm gì mỗi tuần?* | `06_Data/milestone_gates.json` + `03_Operations/` + `01_Governance/` |

Ba lớp này **không trùng nhau và không mâu thuẫn được**, vì cả ba đều sinh ra từ cùng một tập
dữ liệu nguồn — xem §3.

### 1.4 Hệ thống này **không** phải cái gì

- **Không phải công cụ chấm điểm.** Nó nói *đủ điều kiện qua cửa hay chưa*; điểm số là việc của
  quy chế nhà trường.
- **Không phải nơi lưu hồ sơ sinh viên.** Dữ liệu cá nhân nằm ở `07_Private/`, không bao giờ lên kho công khai.
- **Không ép mọi đề tài thành nghiên cứu.** Một project PCB hay RTL làm tốt có giá trị riêng.
  Xem mô hình P → I → T → R ở §6.3.
- **Không phải danh mục của một học kỳ.** Khung tiến độ tính theo **số tuần kể từ ngày nhận đề tài**,
  dùng chung cho mọi khóa.

---

## 2. Từ điển — 15 khái niệm

Tra nhanh khi đọc bất kỳ tài liệu nào trong kho.

| Khái niệm | Nghĩa |
|---|---|
| **Mã chuẩn** | `Family-TypeNN`, ví dụ `A4-T01`. Định danh duy nhất của một đề tài. **Không bao giờ đổi.** |
| **Family / nhóm** | 16 nhóm chuyên môn: `A0`–`A7`, `AB`, `B0`–`B6`. Quyết định nền kiến thức chung. |
| **Type / loại** | `P` project môn học · `I` thực tập · `T` đồ án tốt nghiệp · `R` nghiên cứu khoa học. Quyết định kỳ vọng đầu ra. |
| **Level L0–L5** | **Sàn năng lực khi bắt đầu** — đề tài giả định sinh viên đã có sẵn gì. |
| **Depth D0–D3** | **Chiều sâu khi kết thúc**: D0 sẵn sàng · D1 kỹ thuật · D2 nghiên cứu · D3 ứng viên công bố. **L ≠ D**: sinh viên vào ở L2 vẫn có thể đưa đề tài tới D2. |
| **Cohort / khóa** | Một đợt mở đề tài, ví dụ `HK1_2026_2027`. Khai trong `06_Data/cohort_*.json`. |
| **Alias / mã ngắn** | Mã đọc nhanh trong một khóa (`A4`, `B6`, `C1`). Chỉ để nói miệng — **phiếu đăng ký luôn ghi mã chuẩn**. |
| **Khung tuần tương đối** | Mọi mốc đếm theo **số tuần kể từ ngày sinh viên chính thức nhận đề tài**. Ngày dương lịch chỉ là lớp phủ của từng khóa. |
| **Gate 1–6** | Sáu cửa kiểm soát tiến độ trong khung 15 tuần. Đây là **cửa hành chính**: qua hay không qua. |
| **G0–G7** | Thang chi tiết mô tả *cửa đó đòi hỏi gì* khi đề tài đi tới mức nghiên cứu. G0–G6 nằm gọn trong Gate 1–6; **G7 nằm ngoài khung 15 tuần**. |
| **MVT** | *Minimum Viable Thesis* — phần lõi không bao giờ bị cắt khi trễ tiến độ. |
| **Research extension** | Phần mở rộng nghiên cứu. Chỉ mở khi Gate 2 đã đạt; là thứ bị cắt đầu tiên khi trễ. |
| **Readiness** | Mức sẵn sàng, đo bằng ba thang: **TR** kỹ thuật (16 năng lực, 0–5) · **WR** làm việc (5 phẩm chất, /20) · **RR** nghiên cứu (5 tiêu chí, 0–4). |
| **Evidence / bằng chứng** | Hình, bảng, log, kết quả thô — **truy ngược được về script và commit**. Không truy ngược được thì coi như không có. |
| **Bản sinh (generated view)** | File do script tạo ra từ dữ liệu nguồn. **Sửa tay sẽ bị ghi đè.** Xem §5.3. |

---

## 3. Kiến trúc: một nguồn chuẩn, mọi thứ khác là bản sinh

### 3.1 Nguyên tắc

> **`06_Data/*.json` là nguồn chuẩn duy nhất. Mọi danh mục, phiếu, trang web, hồ sơ đề tài đều là
> bản sinh tự động từ đó.**

Lý do không phải là gọn gàng, mà là **không thể lệch**. Một con số lưu ở hai chỗ thì sớm muộn sẽ
khác nhau, và không ai biết bên nào đúng. Dự án này đã trả giá cho đúng lỗi đó ba lần — nhãn phiên
bản trên sáu file Word, lịch tuần lưu tay trong cohort, và bộ tên đề tài thứ hai trong một trang
HTML tải về. Cả ba lần cách chữa đều giống nhau: **xóa bản sao, sinh lại từ nguồn**.

### 3.2 Sơ đồ

```text
                      ┌──────────────────────────────────────┐
                      │            06_Data/*.json            │
                      │           NGUỒN CHUẨN DUY NHẤT       │
                      ├──────────────────────────────────────┤
                      │ project_portfolio.json  105 đề tài   │
                      │ research_packs.json     105 gói      │
                      │ milestone_gates.json    6 gate·G0-G7 │
                      │ readiness_rubrics.json  TR·WR·RR     │
                      │ cohort_<mã>.json        từng khóa    │
                      └───────────────┬──────────────────────┘
                                      │
                      validate_portfolio.py  ← PHẢI PASS trước
                                      │
        ┌──────────────┬──────────────┼───────────────┬──────────────┐
        ▼              ▼              ▼               ▼              ▼
  generate_      generate_      generate_       generate_      generate_
  catalogs.py    site.py        guide.py        ban_do.py      research_packs.py
        │              │              │               │              │
   5 catalog     docs/          docs/          Ban_do_de_tai   Topic_Guides/ (122)
   + danh mục    index.html     guide.html     .md · .html     Research_Packs/ (105)
   + phiếu (docx/pdf)                                          STATUS_BOARD.md

  sync_docx_version.py → export_governance_md.py   (6 .docx chính sách → 6 .md đọc trên web)
  build_release.py · release_cohort.py             (đóng gói phát hành)
```

Hai module dùng chung, không sinh gì cả:

- **`scripts/cohort_schedule.py`** — suy ra lịch tuần và hạn từng gate từ `start_date`. Bốn generator
  đều gọi nó; **không script nào tự tính ngày**.
- **`scripts/site_style.py`** — CSS, bộ font và địa chỉ kho dùng chung cho hai trang web, để chúng
  không lệch phong cách.

### 3.3 Vùng thẩm quyền — ai nói gì thì đúng

Khi hai tài liệu mâu thuẫn, thứ tự ưu tiên là:

1. **`06_Data/*.json`** — dữ liệu đề tài, thang đánh giá, cửa, khóa. Thắng tuyệt đối.
2. **`.docx` trong `01_Governance/` và `03_Operations/`** — chính sách và quy trình. Bản `.md` cạnh
   chúng là bản sinh, không phải bản gốc.
3. **`10_Documentation/*.md`** — hướng dẫn theo vai trò. Diễn giải, không định nghĩa.
4. **Mọi thứ còn lại** — bản sinh hoặc ghi chú.

---

## 4. Mô hình dữ liệu

### 4.1 `project_portfolio.json` — danh mục 105 đề tài

```text
{ meta, families{16}, levels{L0..L5}, types{P,I,T,R}, topics[105] }
```

Mỗi đề tài:

| Trường | Nghĩa |
|---|---|
| `code` | mã chuẩn `Family-TypeNN` — khóa chính, không đổi |
| `family` · `type` · `min_level` | nhóm · loại · sàn năng lực |
| `title_vi` · `title_en` | **tên chuẩn**; mọi nơi khác phải lấy nguyên từ đây |
| `prerequisites` · `prereq_codes` | kiến thức đầu vào (mô tả) và chuỗi tiền đề (mã hoặc mẫu `A1-P*`) |
| `outputs` · `scope` · `extension` | sản phẩm · phạm vi lõi · phần mở rộng nghiên cứu |
| `tools` · `career_relevance` | công cụ · hướng nghề nghiệp đề tài phục vụ |
| `status` | `active` hoặc không mở |
| `cohort_alias` | **dict** khóa theo `cohort_id`, ví dụ `{"HK1_2026_2027": "A4"}` |
| `mvt` · `checkpoints_15w` · `eligibility` | tùy chọn, có ở các đề tài đã chuẩn bị kỹ |

> **Cạm bẫy đã từng vấp:** `cohort_alias` là *dict*, không phải chuỗi. In thẳng nó ra tài liệu sẽ
> hiện `{'HK1_2026_2027': 'A4'}`. Luôn giải mã qua `cohort_id` của khóa hiện hành.

### 4.2 `research_packs.json` — lớp thực thi, chuẩn hóa theo mức

Đây là file dễ hiểu sai nhất, nên nói kỹ. Nó **không** lặp cùng một nội dung cho 105 đề tài. Nó
tách theo mức chi tiết thật của từng thuộc tính:

| Khối | Số mục | Chứa gì |
|---|---:|---|
| `groups` | 16 | Nền chung **của một nhóm**: phải đọc, phải hiểu, phải dựng, thí nghiệm mặc định, câu hỏi mentor, bước đi tiếp |
| `maturity.levels` | 4 | Kỳ vọng **của một loại** P/I/T/R: mục tiêu, bằng chứng lõi, vai trò, ngưỡng công bố |
| `maturity.red_flags` | 1 bộ | Cảnh báo sớm dùng chung cho mọi đề tài |
| `ladders` | 5 + 7 | Năm thang đi từ board thật tới công bố, và bảy điều kiện của cửa công bố |
| `tracks` · `depth_levels` · `rules` · `raw_data_rule` | | Bốn track nghiên cứu · D0–D3 · bốn quy tắc · quy tắc dữ liệu thô |
| `packs` | 105 | Phần **thật sự riêng** của từng đề tài |

Trong `packs`, đề tài thường chỉ khai vài trường; trường đáng giá nhất là **`expected_output`** —
sản phẩm cuối kỳ phải nộp, và là thứ **duy nhất khác nhau ở cả 105 đề tài**. 13 đề tài có
`depth: "full"` khai thêm 17 trường (câu hỏi nghiên cứu, bằng chứng bắt buộc, phụ thuộc, bốn câu
hỏi mentor riêng…) và **được phép ghi đè** giá trị mặc định của nhóm.

> Vì sao chuẩn hóa: bản chép nguyên si từ gói nguồn nặng 261 KB và lặp cùng một câu hỏi mentor 6 lần
> trong nhóm B4. Bản chuẩn hóa nặng 110 KB, và sửa câu hỏi đó chỉ phải sửa **một** chỗ.

### 4.3 `milestone_gates.json` — cửa và thang nghiên cứu

```text
{ meta, frame{duration_weeks:15, counted_from}, gates[6], research_ladder{gates[G0..G7]} }
```

- **`frame`** — khung tương đối. Không chứa ngày nào.
- **`gates[6]`** — mỗi cửa có `week_start`, `week_end`, `pass_criteria`, `fail_rule`, và
  `research_gates` trỏ tới các mục G tương ứng.
- **`research_ladder`** — G0…G7, mỗi mục có `maps_to_gate` (số, hoặc *"mở rộng"* với G7),
  danh sách điều kiện đạt, và luật không đạt.

Ánh xạ: Gate 1 ⊃ {G0, G1} · Gate 2 ⊃ {G2} · Gate 3 ⊃ {G3} · Gate 4 ⊃ {G4} · Gate 5 ⊃ {G5} ·
Gate 6 ⊃ {G6} · **G7 nằm ngoài 15 tuần**.

### 4.4 `readiness_rubrics.json` — ba thang sẵn sàng

| Thang | Cấu trúc | Dùng khi |
|---|---|---|
| **TR** — technical readiness | 16 năng lực, chấm 0–5 | Chốt phạm vi đề tài đầu kỳ |
| **WR** — working readiness | 5 phẩm chất, tổng /20 | Quyết định nhịp gặp và mức giám sát |
| **RR** — research readiness | 5 tiêu chí, chấm 0–4 | Quyết định có mở phần mở rộng nghiên cứu không |

Kèm `mentor_decision_options` — các phương án mentor được chọn khi một thang chưa đạt ngưỡng.

### 4.5 `cohort_<mã>.json` — lớp phủ của một khóa

```text
{ cohort_id, activity_type, duration_weeks, start_date, breaks[],
  alias_groups[], remaining_topics_policy, topics[], career_guide }
```

- **Chỉ khai `start_date`.** Lịch từng tuần và hạn từng gate **suy ra** bằng `cohort_schedule.py`.
- Khóa chưa công bố ngày thì để trống — tài liệu khi đó chỉ hiển thị mốc tuần (*"hết tuần 5"*).
- `alias_groups` quyết định cách nhóm hiển thị trong danh mục; `remaining_topics_policy: "on_request"`
  sinh ra mục *"đề tài mở theo yêu cầu"* cho phần kho không phát đại trà.

> **Validator sẽ báo lỗi** nếu cohort chứa lại `week_calendar`, `gate_deadlines` hoặc `end_date` —
> ba trường từng được lưu tay và từng lệch nhau.

---

## 5. Chuỗi sinh — chạy gì, theo thứ tự nào

### 5.1 Thứ tự bắt buộc

```bash
# 0. BẮT BUỘC — không PASS thì dừng, mọi thứ phía sau vô nghĩa
python3 scripts/validate_portfolio.py

# 1. Danh mục, danh mục khóa, phiếu đăng ký  (--pdf cần Chrome/Chromium)
python3 scripts/generate_catalogs.py --docx --pdf

# 2. Hai trang web
python3 scripts/generate_site.py            # docs/index.html — danh mục có lọc
python3 scripts/generate_guide.py           # docs/guide.html — hướng dẫn chọn đề tài

# 3. Bản đồ đề tài (bản kể chuyện cho người mới)
python3 scripts/generate_ban_do.py

# 4. Lớp thực thi: 105 trang hướng dẫn + 13 hồ sơ sâu + bảng trạng thái
python3 scripts/generate_research_packs.py

# 5. Chính sách: đồng bộ nhãn phiên bản trong .docx rồi xuất bản .md đọc-trên-web
python3 scripts/sync_docx_version.py
python3 scripts/export_governance_md.py

# 6. Khi phát hành: sửa VERSION rồi đóng gói
python3 scripts/build_release.py
```

Mỗi bước in ra số lượng nó vừa sinh. **Con số lệch với kỳ vọng là tín hiệu, không phải nhiễu** —
dừng lại đọc trước khi chạy tiếp.

### 5.2 Kiểm tra sau khi sinh

Ba phép kiểm rẻ, nên chạy trước mỗi lần commit:

```bash
# a. Nguồn chuẩn nhất quán
python3 scripts/validate_portfolio.py       # phải in "VALIDATION PASS"

# b. Sinh lại hai lần không được lệch một byte (tính idempotent)
#    Chạy chuỗi sinh lần nữa rồi xem git status — phải trống.

# c. Không còn link markdown hỏng
#    Quét mọi *.md, thử phân giải từng link tương đối.
```

### 5.3 File sinh tự động — tuyệt đối không sửa tay

Mọi file dưới đây bị **ghi đè** ở lần sinh sau. Muốn đổi nội dung thì sửa nguồn rồi chạy lại script.

| Bản sinh | Sinh từ |
|---|---|
| 5 catalog `.docx` trong `02_Project_Portfolio/` | `project_portfolio.json` |
| `Danh_muc_de_tai_DATN_<khóa>.docx` / `.pdf`, `Phieu_lua_chon_*.docx` | + `cohort_*.json` |
| `docs/index.html` · `docs/guide.html` | + `research_packs.json` |
| `Ban_do_de_tai.md` · `.html` | + `milestone_gates.json` |
| `02_Project_Portfolio/Topic_Guides/**` (122 file) | `research_packs.json` |
| `02_Project_Portfolio/Research_Packs/**` (105 file) | `research_packs.json` |
| `03_Operations/STATUS_BOARD.md` | `research_packs.json` |
| 6 bản `.md` cạnh các `.docx` chính sách | chính các `.docx` đó |
| `implementation-notes.html` | **chính file `.md` này** |

Mỗi file sinh ra đều mang một dòng cảnh báo ở đầu. Nếu anh thấy dòng đó, đừng sửa file đó.

---

## 6. Mô hình vận hành

### 6.1 Khung 15 tuần tương đối

Mọi mốc đếm theo **số tuần kể từ ngày sinh viên chính thức nhận đề tài**. Khung dùng chung cho mọi
khóa; ngày dương lịch chỉ là lớp phủ suy ra từ `start_date`.

| Gate | Tuần | Đạt khi | Luật cứng nếu chưa đạt |
|---|---|---|---|
| **1** Problem & Foundation | 1–2 | Hiểu bài toán, input/output, baseline, metric, lỗ hổng kiến thức | Điều chỉnh đề tài hoặc kế hoạch học |
| **2** Baseline | 3–5 | Baseline chạy được **và** có bằng chứng tái lập | **Đóng phần mở rộng nghiên cứu** |
| **3** Core Implementation | 6–8 | Phần lõi chạy + kết quả định lượng trung gian | **Thu nhỏ phạm vi** |
| **4** Experiments | 9–11 | Thực nghiệm chính xong, bảng/hình chính hình thành | Không thêm thuật toán lớn mới |
| **5** Analysis & Draft | 12–13 | Phân tích có nguyên nhân + bản thảo đầy đủ | Không dùng viết lách che lỗ hổng |
| **6** Reproducibility & Defense | 14–15 | Người khác chạy lại được; slide, demo, gói bàn giao | Chỉ xác nhận hoàn thành khi đủ ba trục |

**Ba trục đánh giá, thiếu một trục là chưa xong:** technical completion · reproducibility · ownership.
**Không có trục "chăm chỉ".**

### 6.2 G0–G7 — cửa đó đòi hỏi gì

Sáu cửa ở trên là *hành chính*. Thang G mô tả *nội dung*:

`G0` sẵn sàng → `G1` tài liệu và câu hỏi nghiên cứu → `G2` tái lập baseline →
`G3` cài đặt phương pháp đề xuất → `G4` thí nghiệm có kiểm soát → `G5` bằng chứng và phân tích →
`G6` khả năng tái lập → **`G7` sẵn sàng viết bài (ngoài khung 15 tuần)**.

G7 chỉ mở khi Gate 1–6 đã đạt **và** mentor thấy bằng chứng đủ mạnh. Đây là chỗ chặn "paper hóa" giả.

### 6.3 P → I → T → R: kỳ vọng đi theo loại đề tài

| Loại | Mục tiêu | Bằng chứng lõi | Kỳ vọng nghiên cứu |
|---|---|---|---|
| **P** | Học một kỹ năng | sản phẩm chạy được + đo kiểm | novelty không bắt buộc |
| **I** | Làm theo quy trình kỹ sư | quy trình tái lập + tài liệu + gói bàn giao | bài báo không phải KPI mặc định |
| **T** | Sở hữu một sản phẩm hoàn chỉnh | đầu-cuối + đánh giá định lượng + tái lập | có thể mở phần mở rộng nghiên cứu |
| **R** | Trả lời một câu hỏi nghiên cứu | giả thuyết + baseline mạnh + bằng chứng có kiểm soát | sẵn sàng bản thảo nếu G7 đạt |

> **Một project PCB không trở thành nghiên cứu chỉ vì thêm chữ "nghiên cứu" vào tên đề tài.**
> Muốn lên `R` phải có biến nghiên cứu, baseline, metric, giả thuyết và thí nghiệm có kiểm soát.

### 6.4 Nhịp một tuần

**Sinh viên gửi trước buổi gặp — bảy mục:** kế hoạch tuần trước · việc đã xong · bằng chứng ·
cái không chạy · giả thuyết nguyên nhân · thí nghiệm tiếp theo · **một** quyết định cần mentor.

Thiếu bảy mục này thì buổi gặp **bị hoãn**, không phải bị rút ngắn. Mentor không có nghĩa vụ tái
tạo lại tuần làm việc của sinh viên ngay tại chỗ.

**Mentor review 15–25 phút mỗi nhóm**, theo checklist 10 câu ở
[`03_Operations/MENTOR_WEEKLY_CHECKLIST.md`](03_Operations/MENTOR_WEEKLY_CHECKLIST.md).

**Họp gộp theo nhóm chuyên môn, không theo từng đề tài.** Với nhóm nghiên cứu, một buổi ~3 giờ chia
theo track — chi tiết ở [`10_Documentation/RESEARCH-TRACKS.md`](10_Documentation/RESEARCH-TRACKS.md).

**Quy tắc office hour:** lỗi cài đặt, cú pháp, môi trường → hỏi bạn cùng nhóm, trưởng nhóm, tài liệu
chính thức **trước**. Mentor tập trung vào bốn thứ chỉ mentor làm được: tính đúng đắn, kiến trúc,
phương pháp luận, và quyết định công bố.

### 6.5 Chấm một cửa

Thang 2/1/0 cho từng mục, kèm **năm mục trọng yếu**: baseline đúng · so sánh công bằng · toàn vẹn
dữ liệu thô · sinh viên thật sự hiểu · kết quả tái lập được.

> **Một mục trọng yếu bị 0 thì cửa đó không đạt, dù tổng điểm cao.** Cho qua ở đây chỉ là dời chi phí
> sang tuần sau với lãi suất cao hơn.

Chi tiết: [`03_Operations/PASS_FAIL_RUBRIC.md`](03_Operations/PASS_FAIL_RUBRIC.md).

### 6.6 Khi nào dừng hoặc đổi hướng

Mentor chủ động can thiệp khi: baseline chưa đúng nhưng nhóm đã chạy sang phương pháp đề xuất ·
kết quả chỉ đứng vững trên một seed hoặc một cấu hình · phương pháp đề xuất không vượt được một
heuristic đơn giản nhưng lại tốn kém hơn · câu hỏi nghiên cứu đã thoái hóa thành bài toán cài đặt ·
sinh viên không giải thích được đoạn code do AI sinh ra.

Đổi hướng ở tuần 8 rẻ hơn nhiều so với cứu vãn ở tuần 14. **Ghi quyết định vào `DECISION_LOG.md`** —
đó là bằng chứng trước hội đồng rằng phạm vi được thu hẹp có căn cứ, không phải làm không xong.

---

## 7. Triển khai

### 7.1 Kho công khai

`https://github.com/Lucero6886/lucero-mentoring` — công khai, để sinh viên đọc, chọn và thảo luận.

**Ba tầng riêng tư:**

| Tầng | Nội dung | Ở đâu |
|---|---|---|
| **Công khai** | Danh mục, hướng dẫn, chính sách, biểu mẫu trống, script | kho này |
| **Chia sẻ có kiểm soát** | Repo riêng của từng sinh viên, mentor là collaborator | repo riêng |
| **Riêng tư tuyệt đối** | Phiếu đăng ký đã điền, họ tên, MSSV, điểm, đánh giá | `07_Private/` — bị `.gitignore` chặn |

> **Không bao giờ** đưa dữ liệu cá nhân sinh viên vào kho công khai. Đây là ràng buộc, không phải khuyến nghị.

### 7.2 GitHub Pages — cấu hình bắt buộc

Trang web gồm **hai trang**, cả hai nằm trong `docs/`:

| Đường dẫn công bố | Trang |
|---|---|
| `/` | Danh mục có lọc và tìm kiếm |
| `/guide.html` | Hướng dẫn chọn đề tài cho sinh viên |

**Settings → Pages → Build and deployment** phải là **Branch `main`, Folder `/docs`**.

Đặt nhầm thành `/ (root)` thì Pages chạy Jekyll trên cả kho và dựng `README.md` thành trang chủ; hai
trang thật bị đẩy xuống `/docs/…`. Kho có sẵn **hai file chuyển hướng ở thư mục gốc**
(`index.html`, `guide.html`) làm lưới an toàn cho tình huống đó — chúng không chứa nội dung, đừng
xóa và đừng viết gì vào. Chi tiết: [`10_Documentation/GITHUB-WORKFLOW.md`](10_Documentation/GITHUB-WORKFLOW.md) §10b.

### 7.3 Repo của sinh viên

Mỗi sinh viên một repo riêng, dựng từ
[`04_Project_Template/student_repo_starter/`](04_Project_Template/student_repo_starter/README.md).
Tuần 1 phải có: `PROJECT_CHARTER.md` chốt phạm vi và mức chiều sâu nhắm tới · 6 milestone theo hạn
gate của khóa · mentor là collaborator.

Chuẩn tổ chức thư mục và quy tắc dữ liệu thô:
[`04_Project_Template/REPRODUCIBILITY_STANDARD.md`](04_Project_Template/REPRODUCIBILITY_STANDARD.md).

### 7.4 Việc phải làm trước khi phát danh mục cho một khóa

1. Cập nhật `cohort_*.json`: `start_date`, danh sách đề tài mở, `alias_groups`.
2. Chạy toàn bộ chuỗi §5.1, kiểm §5.2.
3. Kiểm tay ba con số trên bản PDF: tổng số đề tài, số đề tài mở, ngày hết hạn từng gate.
4. Push, đợi Pages dựng lại, mở `/guide.html` và `/` bằng **Ctrl+F5**.
5. Gửi sinh viên **một** link duy nhất: trang Guide Notes. Mọi thứ khác dẫn từ đó.

---

## 8. Công thức cho từng việc cụ thể

### 8.1 Thêm hoặc sửa một đề tài

1. Sửa `06_Data/project_portfolio.json` — thêm object vào `topics`, đủ các trường ở §4.1.
2. Nếu đề tài cần lớp thực thi: thêm một mục vào `packs` trong `research_packs.json`
   (tối thiểu `code`, `group`, `type`, `min_level`, `title_vi/en`, `title_v2_proposed_vi`,
   `expected_output`, `depth: "standard"`).
3. `validate_portfolio.py` → phải PASS.
4. Chạy lại chuỗi sinh §5.1.
5. Ghi vào `00_START_HERE/CHANGELOG.md`.

**Không đổi `code` của đề tài đã phát hành.** Sai tên thì sửa `title_vi`; sai mã thì thêm mã mới và
đặt `status` của mã cũ thành không mở.

### 8.2 Đổi tên đề tài hàng loạt

Chỉ sửa `title_vi` / `title_en` trong `project_portfolio.json`, rồi chạy lại chuỗi sinh. Validator
sẽ tự bắt nếu `research_packs.json` còn giữ tên cũ. Bộ tên thay thế đang cân nhắc nằm ở
[`09_References/TITLE-REVIEW-v2.md`](09_References/TITLE-REVIEW-v2.md) — **chưa áp dụng**.

### 8.3 Mở một khóa mới

1. Chép `06_Data/cohort_HK1_2026_2027.json` thành `cohort_<mã mới>.json`.
2. Đổi `cohort_id`, `start_date`, `activity_type`, danh sách `topics` và `alias_groups`.
3. Với mỗi đề tài được mở, thêm khóa mới vào `cohort_alias` của nó trong `project_portfolio.json`.
4. Chạy chuỗi sinh. Danh mục, phiếu và hạn gate của khóa mới sinh ra tự động.

Khóa cũ để nguyên — hệ thống đọc mọi `cohort_*.json`.

### 8.4 Nâng phiên bản và phát hành

```bash
echo "<phiên bản mới>" > VERSION
# cập nhật meta.version + meta.updated trong 4 file 06_Data/*.json
python3 scripts/sync_docx_version.py       # đồng bộ nhãn trong 6 .docx
python3 scripts/export_governance_md.py
# ... chạy lại toàn bộ chuỗi sinh §5.1 ...
python3 scripts/build_release.py           # dist/<tên>-v<VERSION>/ + ZIP
# ghi CHANGELOG, commit, push
```

### 8.5 Nhận một sinh viên mới

1. Chấm ba thang readiness (§4.4) → quyết định phạm vi và mức giám sát.
2. Chốt MVT và phần mở rộng, ghi vào `PROJECT_CHARTER.md` **ngay trong buổi**.
3. Dựng repo từ starter, tạo 6 milestone theo hạn gate.
4. Ghi ngày nhận đề tài — đó là mốc tuần 1, mọi hạn khác suy ra từ đó.

### 8.6 Khôi phục khi hỏng

Toàn bộ hệ thống tái tạo được từ `06_Data/*.json` + `scripts/`. Mất mọi bản sinh cũng không sao —
chạy lại chuỗi §5.1. Thứ **không** tái tạo được: `01_Governance/*.docx`, `03_Operations/*.docx`,
`07_Private/`, và lịch sử git. Ba thứ đó phải có bản sao lưu riêng.

---

## 9. Chín điều bất biến

Đây là những ràng buộc đã được trả giá để học. Đừng thương lượng lại chúng nếu chưa đọc lý do.

1. **`06_Data/*.json` là nguồn chuẩn duy nhất.** Mọi thứ khác là bản sinh.
2. **Không bao giờ đổi mã chuẩn của một đề tài đã phát hành.**
3. **Không sửa tay file sinh tự động.** Có dòng cảnh báo ở đầu file thì đừng động vào.
4. **Không lưu cùng một dữ kiện ở hai nơi.** Ngày, tên, số đếm, nhãn phiên bản — một chỗ duy nhất.
5. **Validator phải PASS trước mọi thao tác sinh.** Không PASS thì mọi thứ phía sau vô nghĩa.
6. **Không đưa dữ liệu cá nhân sinh viên lên kho công khai.**
7. **Khung tiến độ là tương đối theo tuần.** Không ghi cứng ngày của một học kỳ vào tài liệu dùng chung.
8. **Baseline trước cái mới.** Gate 2 chưa đạt thì không mở phần mở rộng nghiên cứu.
9. **Không giải thích được thì chưa hoàn thành.** Áp dụng cho sinh viên, và cho cả mentor khi nhận
   một thay đổi vào hệ thống.

---

## 10. Hạn chế đã biết

Ghi ra để không ai tưởng là lỗi mới phát hiện:

- **Nhãn phiên bản trong `.docx` là chữ soạn tay trong Word.** Nay có `sync_docx_version.py` đồng bộ
  tự động, nhưng nó vẫn là một bước phải nhớ chạy, không phải một ràng buộc do máy áp đặt.
- **PDF danh mục cần Chrome/Chromium.** Máy không có trình duyệt thì `--pdf` báo lỗi; bản `.docx`
  vẫn sinh bình thường.
- **`STATUS_BOARD.md` là khung khởi tạo, không phải bảng theo dõi sống.** Nó bị ghi đè mỗi lần sinh.
  Theo dõi thật thì dùng Project board trên GitHub hoặc bản chép trong `07_Private/`.
- **13 đề tài có hồ sơ sâu, 92 đề tài còn lại chỉ có trang hướng dẫn.** Đó là lựa chọn về công sức,
  không phải thiếu sót: lớp sâu chỉ đáng làm cho đề tài thật sự đi tới mức nghiên cứu.
- **Cấu hình GitHub Pages nằm ngoài kho.** Không script nào bảo đảm được nó; hai file chuyển hướng
  ở gốc là lưới an toàn, không phải lời giải.

---

## Phụ lục A · Bản đồ thư mục

```text
06_Data/              NGUỒN CHUẨN — 4 file JSON + cohort_*.json
scripts/              12 file: 1 validator · 7 generator · 2 module dùng chung · 2 đóng gói
01_Governance/        Chính sách (.docx là gốc, .md là bản sinh)
02_Project_Portfolio/ Catalog .docx · Topic_Guides/ (105 trang) · Research_Packs/ (13 hồ sơ sâu)
03_Operations/        SOP · workbook · checklist tuần · thang PASS/FAIL · định nghĩa "xong"
04_Project_Template/  20 biểu mẫu hồ sơ + student_repo_starter/
07_Private/           Dữ liệu cá nhân — .gitignore chặn
09_References/        Tài liệu nền theo hướng · đối chiếu tên v2
10_Documentation/     Hướng dẫn theo vai trò: sinh viên · mentor · vận hành · GitHub · track nghiên cứu
docs/                 Hai trang web: index.html (danh mục) · guide.html (hướng dẫn chọn)
tests/                Hai bài diễn tập toàn quy trình (A-track và B-track)
00_START_HERE/        CHANGELOG · FILE_MANIFEST · roadmap
```

## Phụ lục B · Prompt cho phiên AI về sau

> Đọc `implementation-notes.md` (file này) trước tiên, rồi `CLAUDE.md`.
> Nguồn chuẩn là `06_Data/*.json`; mọi thứ khác là bản sinh — đừng sửa tay bản sinh.
> Chạy `python3 scripts/validate_portfolio.py` trước và sau mọi thay đổi dữ liệu; phải PASS.
> Không đổi mã chuẩn đề tài. Không đưa dữ liệu cá nhân lên kho công khai.
> Sau khi sửa dữ liệu, chạy lại toàn bộ chuỗi sinh ở §5.1 rồi kiểm §5.2.
> Ghi mọi thay đổi vào `00_START_HERE/CHANGELOG.md`.

## Phụ lục C · Nhắc nhanh về riêng tư

Trước mỗi lần push, tự hỏi ba câu: *File này có tên sinh viên không? Có mã số sinh viên không?
Có điểm hoặc nhận xét cá nhân không?* Một câu "có" thì file đó thuộc `07_Private/`.

---

*Lịch sử thay đổi của hệ thống nằm ở [`00_START_HERE/CHANGELOG.md`](00_START_HERE/CHANGELOG.md) —
tài liệu này chỉ mô tả trạng thái **hiện tại**.*
