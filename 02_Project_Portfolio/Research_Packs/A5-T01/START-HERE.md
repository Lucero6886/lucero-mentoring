# START HERE — A5-T01

**Engineering & Research Mentoring Program (Lucero)** · ThS. Đinh Văn Nam (Mr. Lucero Dinh) — Khoa Điện–Điện tử, Trường Kỹ thuật, Đại học Phenikaa

> **File sinh tự động** từ `06_Data/research_packs.json` bằng `scripts/generate_research_packs.py`. Sửa tay sẽ bị ghi đè — muốn đổi nội dung thì sửa JSON rồi chạy lại script.

**Đề tài:** Xây dựng quy trình ASIC tái lập sử dụng LibreLane + Nix  
**English:** Reproducible ASIC Workflow Using LibreLane and Nix  
**Tên đầy đủ khi đăng ký:** Xây dựng và đánh giá quy trình RTL-to-GDSII mã nguồn mở có khả năng tái lập phục vụ đào tạo thiết kế vi mạch số  
**Mã đối chiếu gói gốc:** T02 · **Track A** — Thiết kế IC số mã nguồn mở

---

## Câu hỏi nghiên cứu

> Làm thế nào xây dựng một RTL-to-GDSII environment mà người học khác có thể tái lập kết quả một cách ổn định trên các máy/môi trường khác nhau?

Đây là câu em phải trả lời được bằng **bằng chứng**, không phải bằng một bản cài đặt chạy được.

## Trước khi gõ dòng code đầu tiên — phải đọc

- reproducible research
- container/Nix/environment management concepts
- open-source RTL-to-GDSII flow
- CI/regression basics
- EDA versioning
- engineering education evaluation basics

Tài liệu cụ thể xem `09_References/READING-LIST.md`. Sau mỗi tài liệu, trả lời 10 câu ở cuối file này.

## Phải hiểu được (không nhìn tài liệu)

- reproducibility vs repeatability
- toolchain pinning
- deterministic và non-deterministic sources
- benchmark design
- clean-room rerun
- tại sao ModifiedAt/version mới không đảm bảo kết quả mới/đúng

## Phải dựng

- bootstrap/setup scripts
- version manifest
- benchmark runner
- result parser
- optional CI workflow

## Phải chạy thí nghiệm

- Fresh install test
- multi-machine or multi-environment rerun
- version/config sensitivity
- benchmark suite run
- runtime + PPA consistency

## Bằng chứng bắt buộc nộp

- setup time log
- success/failure matrix
- version manifest
- PPA/run-time variance
- clean-clone demonstration
- student reproduction checklist

## Khi nào mới đủ điều kiện nghĩ tới một bài báo

Có protocol tái lập rõ, benchmark đủ đa dạng, thử nghiệm trên nhiều môi trường/người dùng hoặc nhiều clean runs, có định lượng consistency và bài học giáo dục.

Tiềm năng công bố mentor đánh giá cho đề tài này: **Trung bình**. Đây là ước lượng ban đầu, không phải lời hứa — quyết định thật nằm ở Gate G7.

## Bốn câu mentor sẽ hỏi đi hỏi lại

1. Cái gì đang được 'reproduced': chức năng hay PPA hay cả hai?
2. Nguồn biến thiên nào do tool, nguồn nào do environment?
3. Một sinh viên mới cần bao nhiêu bước thủ công?
4. Đóng góp nghiên cứu/giáo dục nằm ở đâu ngoài việc viết script?

Nếu tuần nào em cũng trả lời được bốn câu này bằng bằng chứng của chính mình, đề tài đang đi đúng.

## Bốn quy tắc không thương lượng

1. Không có baseline thì không có phương pháp đề xuất.
2. Không có bằng chứng thì không có kết luận.
3. Không tái lập được thì đề tài chưa hoàn thành ở mức nghiên cứu.
4. Không so sánh công bằng thì không được tuyên bố trong bài báo.

## READING-QUESTIONS — trả lời sau mỗi tài liệu

1. Bài này giải quyết vấn đề gì?
2. Baseline của họ là gì?
3. Giả định nào là quan trọng?
4. Họ dùng metric nào?
5. Kết quả chính là gì?
6. Giới hạn của bài là gì?
7. Phần nào tái lập được?
8. Phần nào liên quan trực tiếp tới câu hỏi nghiên cứu của em?
9. Có kết luận nào cần kiểm chứng độc lập không?
10. Nếu chỉ lấy được một insight cho đề tài, đó là gì?

---

*Trang tổng quan đề tài: [`Topic_Guides/A5/A5-T01.md`](../../Topic_Guides/A5/A5-T01.md) · Lộ trình: `ROADMAP.md` · Cửa: `MILESTONE-GATES.md` · Thí nghiệm: `EXPERIMENTS.md`*
