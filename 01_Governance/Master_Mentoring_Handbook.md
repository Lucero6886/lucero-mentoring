# Sổ tay quản trị chương trình mentoring

**Engineering & Research Mentoring Program (Lucero)** · ThS. Đinh Văn Nam (Mr. Lucero Dinh) — Khoa Điện–Điện tử, Trường Kỹ thuật, Đại học Phenikaa

> **File này được sinh tự động** từ `Master_Mentoring_Handbook.docx` bằng `scripts/export_governance_md.py`.
> Bản `.docx` là bản gốc dùng để in, ký và nộp — **mọi chỉnh sửa nội dung phải làm trên `.docx`**,
> rồi chạy lại script để cập nhật bản này. Sửa tay file `.md` sẽ bị ghi đè ở lần sinh sau.

---

**Khung quản trị Project - Thực tập - Đồ án tốt nghiệp - Nghiên cứu khoa học**

Engineering & Research Mentoring Program | Version 1.10.0 | 04/09/2026

> 
| **Mục tiêu của hệ thống không phải là “có thật nhiều đề tài”, mà là xây các dòng năng lực để sinh viên có thể đi từ làm thật → hiểu thật → tự học → sở hữu project → nghiên cứu khi đủ readiness.** |

## 1\. Triết lý chương trình

  - Scaffolded independence: ban đầu cấu trúc cao, sau đó chuyển dần ownership sang sinh viên.

  - One portfolio, multiple views: một ngân hàng dự án gốc nhưng tách catalog cho P/I/T/R.

  - Engineering và Research là hai dòng phát triển bổ sung, không xếp hạng hơn-kém.

  - Mentor chịu trách nhiệm về direction, scope, standards, critical feedback và quality control; sinh viên chịu trách nhiệm learning, execution, evidence, deadline, documentation và presentation.

  - Một hệ thống mentoring tốt vẫn có thể có sinh viên thất bại nếu sinh viên không thực hiện phần trách nhiệm của mình.

## 2\. Hai dòng phát triển sinh viên

| **Dòng**             | **Trọng tâm**                              | **Chuỗi năng lực**                                                                 |
| -------------------- | ------------------------------------------ | ---------------------------------------------------------------------------------- |
| Engineering Practice | Design - Build - Test - Debug              | PCB/circuit → RTL → FPGA → ASIC/EDA                                          |
| Research Practice    | Question - Baseline - Experiment - Analyze | Software baseline → controlled experiment → research question → contribution |

## 3\. Các mức tham gia P/I/T/R

| **Mã** | **Hoạt động**       | **Mục tiêu**                                                                                              | **Novelty**                        | **Risk** |
| ------ | ------------------- | --------------------------------------------------------------------------------------------------------- | ---------------------------------- | -------- |
| P      | Project môn học     | Học và chứng minh một kỹ năng cụ thể; novelty không bắt buộc.                                             | Không bắt buộc                     | Rất thấp |
| I      | Thực tập            | Thực hành engineering workflow và tác phong làm việc kỹ thuật.                                            | Không bắt buộc                     | Thấp     |
| T      | Đồ án tốt nghiệp    | Sở hữu một project hoàn chỉnh: correct + complete + reproducible + quantitatively evaluated.              | Không bắt buộc                     | Thấp-TB  |
| R      | Nghiên cứu khoa học | Trả lời một research question với baseline, evidence và phân tích; hypothesis có thể không được xác nhận. | Cần research question/contribution | TB-Cao   |

## 4\. Student Development Levels

| **Level** | **Tên**                         | **Mô tả**                                                   |
| --------- | ------------------------------- | ----------------------------------------------------------- |
| 0         | Explorer                        | Chưa có evidence; khám phá hướng phù hợp.                   |
| 1         | Beginner Engineer               | Làm được task nhỏ có hướng dẫn.                             |
| 2         | Independent Engineering Student | Tự thực hiện engineering task, debug và báo cáo.            |
| 3         | Research-Ready Undergraduate    | Đọc paper, xây baseline và thiết kế experiment cơ bản.      |
| 4         | Undergraduate Researcher        | Sở hữu research question và thực nghiệm có kiểm soát.       |
| 5         | Advanced Research Student       | Research ownership cao; đủ sức co-design/advanced research. |

## 5\. Readiness trước khi giao đề tài

### 5.1 Technical Readiness (TR)

  - Thang 0-5: 0 chưa biết; 1 biết tên; 2 hiểu cơ bản; 3 làm được có hướng dẫn; 4 tự làm; 5 có thể giải thích/mentor người khác.

  - Các năng lực đánh giá: điện tử, logic số, RTL, simulation/debug, FPGA, Python, MATLAB, Linux/WSL, Git/GitHub, DSP, truyền thông số, xác suất, coding theory, Polar Code, đọc tiếng Anh, technical writing.

  - Self-assessment chỉ là dữ liệu ban đầu; phải kiểm chứng bằng mini-task.

### 5.2 Working Readiness (WR)

| **Phẩm chất**     | **Evidence quan sát được**                                                                      |
| ----------------- | ----------------------------------------------------------------------------------------------- |
| Cam kết & kỷ luật | Đúng deadline; tham gia/đổi lịch đúng quy ước; cập nhật đều; không để task “vâng dạ rồi để đó”. |
| Kiên trì          | Khi gặp lỗi có evidence về các thử nghiệm chẩn đoán, không bỏ cuộc ngay.                        |
| Trung thực        | Phân biệt rõ tự làm, tham khảo, AI hỗ trợ, chưa hiểu, kết quả âm/không như kỳ vọng.             |
| Chủ động          | Tự tìm từ khóa/tài liệu; đề xuất next step trước khi hỏi mentor “em làm gì tiếp?”.              |
| Tư duy phản biện  | Hỏi tại sao; so sánh alternatives; chấp nhận/sửa quan điểm theo evidence.                       |

  - Chấm 0-4 mỗi tiêu chí, tối đa 20.

  - Ngưỡng gợi ý: Project \>=10; Internship \>=12; DATN Engineering \>=14; DATN research-oriented \>=15; NCKH \>=16; advanced B6/AB-R \>=17. (Nguồn chuẩn của ngưỡng: 06\_Data/readiness\_rubrics.json — nếu hai nơi lệch nhau, JSON thắng.)

  - Không dùng ngưỡng như luật máy móc; mentor có thể override nhưng phải ghi lý do.

### 5.3 Research Readiness (RR)

| **Năng lực**             | **Evidence**                                                                        |
| ------------------------ | ----------------------------------------------------------------------------------- |
| Literature comprehension | Đọc được paper/tài liệu và tách problem, assumptions, method, metrics, limitations. |
| Baseline discipline      | Ưu tiên baseline đúng, tái lập trước novelty.                                       |
| Experimental design      | Biết control variables, seed/config, metric và so sánh công bằng.                   |
| Interpretation           | Giải thích kết quả, không chỉ báo số/figure.                                        |
| Research ownership       | Tự hình thành câu hỏi/giả thuyết nhỏ và biết giới hạn claim.                        |

## 6\. Readiness test 2 tuần

1.  Literature task: problem, input, output, method, metric, điểm chưa hiểu.

2.  Technical mini-task 4-10 giờ thực tế phù hợp family.

3.  Oral check 5-10 phút: sinh viên phải giải thích đã làm gì, vì sao, lỗi gì, đã thử gì và next step.

4.  Mentor đánh giá prerequisite gaps và chốt: nhận / nhận có điều kiện / đổi đề tài / chưa nhận.

## 7\. Quy trình matching đề tài

> 
| **Student interest → Top 3 → Self-assessment → Readiness test → Mentor evaluation → Gap analysis → Topic assignment → Probation → Official scope** |

  - Top 3 là nguyện vọng, không phải quyền lựa chọn tuyệt đối.

  - Đề tài advanced chỉ được giao khi prerequisite và WR/RR đạt.

  - B4 yêu cầu SC baseline; B5 yêu cầu SC/SCF; B6 nhánh detection yêu cầu baseline B5, nhánh candidate-ranking yêu cầu SCF/B4 ổn định — cả hai nhánh đều cần ML cơ bản và research maturity; AB yêu cầu cả nền A và B.

## 8\. Mô hình mentoring theo tầng

| **Tầng**             | **Tỷ lệ gợi ý** | **Nội dung**                                                              |
| -------------------- | --------------- | ------------------------------------------------------------------------- |
| Common mentoring     | 50-60%          | Git, literature, report, AI, experiment, presentation, debugging mindset. |
| Theme mentoring      | 25-35%          | Nhóm Digital IC/FPGA/ASIC hoặc nhóm Polar cùng chia sẻ technical context. |
| Individual mentoring | 15-20%          | Algorithm/bug khó/scope/research decision/critical thesis review.         |

## 9\. Weekly operating cycle

1.  Sinh viên cập nhật weekly report trước buổi gặp.

2.  Mentor đọc evidence trước; meeting không bắt đầu từ việc kể lại toàn bộ tuần.

3.  Sinh viên trình bày Goal → Evidence → Failure → Diagnosis → Proposed next step → Question.

4.  Mentor hỏi để kiểm chứng hiểu, không chỉ hỏi “em hiểu chưa?”.

5.  Cuối meeting chốt 1-3 deliverables và deadline; mọi quyết định được ghi lại.

## 10\. Milestone gates cho DATN 15 tuần

| **Gate**                           | **Thời điểm** | **Điều kiện qua**                                                           | **Nếu không đạt**                                                    |
| ---------------------------------- | ------------- | --------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| Gate 1 - Problem & Foundation      | Tuần 1-2      | Hiểu problem, input/output, baseline, metric, prerequisite gaps.            | Không đạt: điều chỉnh đề tài hoặc learning plan.                     |
| Gate 2 - Baseline                  | Tuần 3-5      | Baseline/chức năng cơ sở phải chạy và có evidence tái lập.                  | Không baseline ở tuần 5: không mở research extension.                |
| Gate 3 - Core Implementation       | Tuần 6-8      | Có core implementation và kết quả định lượng trung gian.                    | Không đạt tuần 8: reduce scope; không cứu bằng cách mentor làm thay. |
| Gate 4 - Experiments               | Tuần 9-11     | Thực nghiệm chính hoàn tất; table/figure chính hình thành.                  | Sau tuần 11: không thêm thuật toán lớn mới.                          |
| Gate 5 - Analysis & Draft          | Tuần 12-13    | Phân tích kết quả và bản thảo báo cáo/khóa luận đầy đủ.                     | Thiếu evidence: ưu tiên hoàn thiện core, không polish che lỗ hổng.   |
| Gate 6 - Reproducibility & Defense | Tuần 14-15    | Người khác có thể chạy lại; slides/demo; legacy package; defense readiness. | Chỉ xác nhận hoàn thành khi ownership và reproducibility đạt.        |

## 11\. Scope management

  - Mỗi DATN phải có MVT (Minimum Viable Thesis) và Research Extension tách biệt.

  - Khi tiến độ chậm, thứ tự xử lý: chẩn đoán task difficulty/time allocation/learning strategy → remove nonessential work → reduce scope → focused support.

  - Không giữ scope tham vọng bằng cách tăng effort của mentor đến mức làm thay.

  - Một khóa luận đúng, hoàn chỉnh và được sinh viên hiểu sâu tốt hơn một khóa luận “đẹp” nhưng ownership thấp.

## 12\. AI & academic integrity

> 
| **AI use is allowed. AI dependency is not. Cannot explain = Not completed.** |

  - Cho phép AI hỗ trợ giải thích, brainstorming, keyword, coding, debug, writing support.

  - Sinh viên chịu trách nhiệm code, equation, citation, figure, data, result và claim.

  - Sản phẩm AI tạo mà sinh viên không giải thích được phải làm lại.

  - Research data/result không được bịa, lựa chọn cherry-pick hoặc che giấu negative result.

## 13\. Peer mentoring

  - Peer/senior có thể giúp environment, concept, code review, known issues.

  - Không mặc nhiên giao sinh viên giỏi “cứu” sinh viên yếu.

  - Peer mentor không sở hữu deadline hoặc deliverable của bạn khác.

  - Khuyến khích technical lineage: cohort trước để lại legacy package cho cohort sau.

## 14\. Project Legacy Package

  - README và cách chạy lại

  - Source code + config/environment

  - Tests/regression

  - Results + figures + raw/processed data hợp lý

  - Literature notes

  - Known issues

  - Next steps

  - Report/thesis/slides

  - AI usage log khi áp dụng

## 15\. Định nghĩa thành công

| **Track**   | **Một outcome tốt**                                                                                    |
| ----------- | ------------------------------------------------------------------------------------------------------ |
| Engineering | Sinh viên có thể design-build-test-debug-document một hệ thống và giải thích được quyết định kỹ thuật. |
| DATN        | Correct + complete + reproducible + quantitatively evaluated + student ownership.                      |
| Research    | Có baseline đúng, research question rõ, experiment công bằng, claim giới hạn đúng evidence.            |
