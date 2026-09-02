# Hướng dẫn thực thi — toàn bộ 105 đề tài

**Engineering & Research Mentoring Program (Lucero)** · ThS. Đinh Văn Nam (Mr. Lucero Dinh) — Khoa Điện–Điện tử, Trường Kỹ thuật, Đại học Phenikaa

> **File sinh tự động** từ `06_Data/research_packs.json` bằng `scripts/generate_research_packs.py`. Sửa tay sẽ bị ghi đè — muốn đổi nội dung thì sửa JSON rồi chạy lại script.

Danh mục trả lời câu *"có những đề tài nào"*. Thư mục này trả lời câu tiếp theo:
**"làm đề tài đó cụ thể ra sao"** — phải đọc gì, hiểu gì, dựng gì, sản phẩm phải ra là gì,
đo kiểm thế nào, và khi nào mới đủ điều kiện nghĩ tới một bài báo.

Mỗi đề tài có một trang. **13 đề tài nghiên cứu** có thêm hồ sơ sâu tám file trong [`../Research_Packs/`](../Research_Packs/README.md).

## Đây là một chương trình, không phải 105 đề tài rời rạc

Các đề tài xếp thành những nấc năng lực nối tiếp nhau:

**PCB/board thật → RTL → Số học/DSP → FPGA → ASIC/EDA → Nhúng/IoT → Polar → Thích ứng/Neural → Co-design → Công bố**

Không phải đề tài nào cũng phải thành bài báo. Một project PCB, RTL hay FPGA tốt có giá trị
riêng nếu tạo ra kỹ năng và bằng chứng thật.

## Bốn mức trưởng thành P → I → T → R

| Loại | Mục tiêu | Bằng chứng lõi | Kỳ vọng nghiên cứu |
|---|---|---|---|
| **P** — Project môn học | Học một kỹ năng | working artifact + test/measurement | novelty không bắt buộc |
| **I** — Thực tập | Làm theo quy trình kỹ sư | reproducible workflow + documentation + legacy | paper không phải KPI mặc định |
| **T** — Đồ án tốt nghiệp | Sở hữu sản phẩm hoàn chỉnh | end-to-end + quantitative evaluation + reproducibility | có thể mở research extension |
| **R** — Nghiên cứu khoa học | Trả lời research question | hypothesis + strong baseline + controlled evidence | manuscript-ready nếu G7 PASS |

> Một PCB project không trở thành nghiên cứu chỉ vì thêm chữ “nghiên cứu” vào tên. Muốn lên R phải có biến, baseline, metric, hypothesis và experiment có kiểm soát.

## Bản đồ 16 nhóm

| Nhóm | Tên | Số đề tài | Theo loại | Hồ sơ sâu |
|---|---|---:|---|---:|
| [`A0`](A0/README.md) | Điện tử thực hành và PCB | 7 | P:6 · I:1 | — |
| [`A1`](A1/README.md) | Logic số và thiết kế RTL | 7 | P:5 · I:1 · T:1 | 1 |
| [`A2`](A2/README.md) | Số học số và phần cứng DSP | 9 | P:4 · I:1 · T:3 · R:1 | 1 |
| [`A3`](A3/README.md) | Thiết kế hệ thống trên FPGA | 6 | P:3 · I:1 · T:2 | — |
| [`A4`](A4/README.md) | Thiết kế ASIC và hiện thực vật lý | 6 | P:2 · I:1 · T:2 · R:1 | 1 |
| [`A5`](A5/README.md) | Kiểm chứng, EDA và phát triển tái lập | 6 | P:2 · I:1 · T:2 · R:1 | 1 |
| [`A6`](A6/README.md) | Hệ nhúng và tích hợp SoC | 8 | P:4 · I:1 · T:2 · R:1 | — |
| [`A7`](A7/README.md) | Hệ IoT và trí tuệ biên | 8 | P:4 · I:1 · T:2 · R:1 | — |
| [`AB`](AB/README.md) | Vùng giao: IC số × Polar × Edge co-design | 10 | P:1 · T:6 · R:3 | — |
| [`B0`](B0/README.md) | Nền Polar và baseline phần mềm | 5 | P:3 · I:1 · T:1 | — |
| [`B1`](B1/README.md) | Khối phần cứng cho Polar | 7 | P:4 · I:1 · T:2 | — |
| [`B2`](B2/README.md) | Bộ giải mã SC Polar trên phần cứng | 4 | I:1 · T:2 · R:1 | 1 |
| [`B3`](B3/README.md) | Lượng tử hóa và tối ưu theo phần cứng | 5 | P:1 · I:1 · T:2 · R:1 | 1 |
| [`B4`](B4/README.md) | SC-Flip và giải mã theo độ tin cậy | 6 | P:2 · I:1 · T:2 · R:1 | 2 |
| [`B5`](B5/README.md) | Giải mã Polar thích ứng | 6 | P:1 · I:1 · T:3 · R:1 | 3 |
| [`B6`](B6/README.md) | Giải mã Polar hỗ trợ mạng neural | 5 | I:1 · T:2 · R:2 | 2 |

## Năm thang đi từ board thật tới công bố


**1. PCB → Digital IC**  
`A0-P02/P03` → `A1-P*/A1-I01` → `A1-T01` → `A3-P01/A3-T01` → `A4-T01/T02` → `A4-R01` hoặc `A2-R01`  
_board thật tạo trực giác → RTL tạo IP → FPGA tạo product evidence → ASIC/PPA tạo metric → R tạo research question._

**2. PCB + FPGA interface**  
`A0-P06` → `A3-P02` → `A3-I01/T01` → `A4-T01/T02` → `AB-*`

**3. PCB → Embedded/IoT → Edge AI**  
`A0-P04/P05` → `A6-P*/I01/T01` → `A7-T01/T02` → `A7-R01` → `AB-T05` → `AB-R03`

**4. Digital/FPGA → Polar → Publication**  
`A1 + B0` → `B1` → `B2-T01` → `B3/B4` → `B5` → `B6` → `AB-R01/R02`

**5. PhD-aligned adaptive Polar**  
`B2-T01` → `B3-T02` → `B4-T01/T02` → `B5-T01/T02/T03` → `B6-T01/T02` → `B6-R01/R02` → `AB-R01/R02`

### Cửa công bố

Sản phẩm tốt chưa chắc là bài báo. Chỉ mở hướng công bố khi đủ cả bảy:

1. baseline đúng
2. question không tầm thường
3. comparison công bằng
4. có quantitative evidence
5. có robustness/failure analysis
6. có reproducibility
7. contribution không vượt evidence

## Bốn quy tắc không thương lượng

1. Không có baseline thì không có phương pháp đề xuất.
2. Không có bằng chứng thì không có kết luận.
3. Không tái lập được thì đề tài chưa hoàn thành ở mức nghiên cứu.
4. Không so sánh công bằng thì không được tuyên bố trong bài báo.

## Quy tắc dữ liệu thô

- Không overwrite raw measurement/simulation
- Mỗi run lưu config, seed, git commit, tool version, date
- Figure/table phải được tạo lại từ script
- Ảnh oscilloscope/logic analyzer phải có test condition
- Board revision/BOM/firmware/bitstream phải versioned

---

| Cần gì | Đọc đâu |
|---|---|
| Chọn đề tài thế nào | [`10_Documentation/STUDENT-GUIDE.md`](../../10_Documentation/STUDENT-GUIDE.md) |
| Vận hành nhóm nghiên cứu theo track | [`10_Documentation/RESEARCH-TRACKS.md`](../../10_Documentation/RESEARCH-TRACKS.md) |
| Hồ sơ sâu 13 đề tài nghiên cứu | [`../Research_Packs/README.md`](../Research_Packs/README.md) |
| Đề xuất đổi tên đề tài (chưa áp dụng) | [`09_References/TITLE-REVIEW-v2.md`](../../09_References/TITLE-REVIEW-v2.md) |
