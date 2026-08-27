# Thesis Technical Review Checklist — <MÃ_ĐỀ_TÀI>

> Rà soát kỹ thuật báo cáo/khóa luận trước bảo vệ (MASTER_PROMPT §14).
> Dùng ở Gate 5–6. Chỉ tick phần **áp dụng được** với đề tài; phần không áp dụng ghi "n/a" kèm lý do một dòng.

## A · Chung — mọi đề tài

- [ ] Bài toán, input/output, giả định nêu rõ ngay đầu
- [ ] Baseline được định nghĩa cụ thể tới mức cấu hình
- [ ] Mỗi claim định lượng trỏ được về một dòng `VERIFIED` trong `EVIDENCE_LEDGER.md`
- [ ] Hình/bảng truy được về script sinh ra chúng
- [ ] Limitation viết thật, không phải câu lịch sự
- [ ] Kết quả âm/không như kỳ vọng được giữ lại nếu cần cho phân tích công bằng
- [ ] Không đổi metric/baseline sau khi thấy kết quả mà không nói rõ

## B · Digital IC / FPGA / ASIC

- [ ] Specification · [ ] Interface · [ ] Clock/reset · [ ] Parameterization
- [ ] Functional correctness · [ ] Testbench · [ ] Corner cases · [ ] Waveform
- [ ] Synthesis · [ ] STA · [ ] Resource usage · [ ] Fmax
- [ ] Latency · [ ] Throughput · [ ] PPA · [ ] Fixed-point behavior
- [ ] Implementation constraints · [ ] Regression · [ ] Reproducibility

**Ba cảnh báo cứng:**
1. Synthesis chạy được **≠** đúng chức năng.
2. Một vector pass **≠** đã verify đủ.
3. So sánh PPA dưới các ràng buộc khác nhau **không** tự động công bằng — phải nêu rõ điều kiện.

## C · Polar Code / Hardware-Aware Decoding

- [ ] N · [ ] K · [ ] Code rate · [ ] Construction · [ ] Frozen/information set
- [ ] Encoder consistency · [ ] Modulation · [ ] Channel · [ ] Quy ước Eb/N0 hay SNR
- [ ] LLR definition · [ ] Decoder definition · [ ] BER · [ ] BLER
- [ ] Random seed · [ ] Stopping rule · [ ] Số frame/số lỗi · [ ] Quantization
- [ ] Complexity metric · [ ] Average attempts · [ ] Latency/cost proxy
- [ ] Dataset generation · [ ] Train/val/test split · [ ] Kiểm rò rỉ dữ liệu
- [ ] Baseline fairness · [ ] Reproducibility

**Với đề tài ML-assisted:** không chấp nhận kết quả neural nếu thiếu so sánh heuristic/classical tương ứng.

## D · Kết luận rà soát

| Mức | Số lượng | Ghi chú |
|---|---|---|
| CRITICAL — phải sửa trước bảo vệ |  |  |
| MAJOR — nên sửa |  |  |
| MINOR |  |  |

Kết luận: ☐ Đủ điều kiện bảo vệ ☐ Sửa rồi rà lại ☐ Chưa đủ
Mentor: ______________________  Ngày: ____/____/______
