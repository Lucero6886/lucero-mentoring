# Quy tắc sử dụng AI và liêm chính học thuật

**Engineering & Research Mentoring Program (Lucero)** · ThS. Đinh Văn Nam (Mr. Lucero Dinh) — Khoa Điện–Điện tử, Trường Kỹ thuật, Đại học Phenikaa

> **File này được sinh tự động** từ `AI_and_Academic_Integrity_Policy.docx` bằng `scripts/export_governance_md.py`.
> Bản `.docx` là bản gốc dùng để in, ký và nộp — **mọi chỉnh sửa nội dung phải làm trên `.docx`**,
> rồi chạy lại script để cập nhật bản này. Sửa tay file `.md` sẽ bị ghi đè ở lần sinh sau.

---

**Quy định sử dụng ChatGPT / Claude / Copilot và các công cụ AI trong mentoring**

Engineering & Research Mentoring Program | Version 1.6.0 | 23/08/2026

> 
| **Nguyên tắc trung tâm: AI use is allowed. AI dependency is not. Người học chịu trách nhiệm cuối cùng về mọi nội dung, code, dữ liệu, kết quả và claim được nộp.** |

## 1\. Được phép

  - Giải thích khái niệm và tạo ví dụ học tập.

  - Brainstorm keyword/literature search strategy.

  - Gợi ý cấu trúc code, testbench, debugging hypothesis.

  - Hỗ trợ viết lại câu chữ sau khi sinh viên đã hiểu nội dung.

  - Tạo checklist, câu hỏi tự kiểm tra, test cases.

  - Hỗ trợ phân tích lỗi nhưng sinh viên phải tự xác nhận bằng experiment/evidence.

## 2\. Không được chấp nhận

  - Copy code/report mà không hiểu.

  - Tạo citation/reference không kiểm chứng.

  - Bịa dữ liệu, figure, log, result hoặc mô tả experiment chưa thực hiện.

  - Dùng AI để che giấu việc chưa làm hoặc chưa hiểu.

  - Đưa dữ liệu nhạy cảm/confidential vào công cụ ngoài khi chưa được phép.

## 3\. Ownership check

  - Mentor có thể hỏi bất kỳ dòng code/công thức/figure nào.

  - Sinh viên phải giải thích “vì sao”, không chỉ “nó làm gì”.

  - Nếu bỏ/thay block/parameter, sinh viên phải dự đoán được tác động ở mức phù hợp.

  - Không giải thích được → task chưa đạt và phải học/làm lại.

## 4\. AI Usage Log

| **Ngày** | **Công cụ** | **Mục đích** | **Prompt/tóm tắt** | **Phần đã kiểm chứng thế nào?** |
| -------- | ----------- | ------------ | ------------------ | ------------------------------- |
|          |             |              |                    |                                 |
|          |             |              |                    |                                 |
|          |             |              |                    |                                 |

## 5\. Quy tắc theo loại sản phẩm

| **Sản phẩm**   | **AI có thể hỗ trợ** | **Sinh viên bắt buộc phải làm**                                              |
| -------------- | -------------------- | ---------------------------------------------------------------------------- |
| Literature     | Keyword, giải thích  | Đọc nguồn gốc; xác minh claim/citation; ghi limitation.                      |
| Code/RTL       | Skeleton, debug idea | Chạy test; hiểu logic; kiểm tra corner cases; chịu trách nhiệm correctness.  |
| Experiment     | Gợi ý plan           | Tự chốt variables/metrics/seeds; chạy thật; lưu config/log.                  |
| Writing        | Grammar/clarity      | Sở hữu argument; kiểm chứng số liệu/citation; không tạo claim vượt evidence. |
| Figures/Tables | Gợi ý trình bày      | Dữ liệu phải traceable về script/raw result.                                 |

## 6\. Research integrity

  - Giữ cả kết quả không thuận lợi khi chúng cần cho phân tích công bằng.

  - Không đổi metric/baseline sau khi thấy kết quả chỉ để làm phương pháp “đẹp” hơn mà không disclosure.

  - Không dùng test data trong training/model selection khi protocol yêu cầu tách biệt.

  - Mọi thay đổi experiment phải được ghi lại đủ để audit.
