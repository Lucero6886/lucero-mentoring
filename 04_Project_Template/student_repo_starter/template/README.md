# <Tên đề tài> — <Mã chuẩn, ví dụ A4-T01>

> **Đây là mẫu.** Thay mọi chỗ `<...>` bằng nội dung của em, rồi xóa dòng này.
> Viết dần từ tuần 1 — README là thứ người chấm đọc đầu tiên và là thứ chứng minh đồ án **tái lập được**.

**Sinh viên:** <tên> · **Mentor:** ThS. Đinh Văn Nam (Mr. Lucero Dinh)
**Học kỳ:** <HK1 2026-2027> · **Loại:** <Đồ án tốt nghiệp>

---

## 1. Bài toán

<2–4 câu: đầu vào là gì, đầu ra là gì, đo bằng tiêu chí nào. Viết cho người chưa biết đề tài này.>

## 2. Trạng thái hiện tại

| Hạng mục | Trạng thái |
|---|---|
| Gate gần nhất đã qua | <Gate 2 — 11/10> |
| Phần lõi (MVT) | <đang làm / xong> |
| Phần mở rộng | <đóng / đang mở> |

## 3. Chạy lại thế nào

**Cần có:** <hệ điều hành, phiên bản công cụ — ví dụ: Ubuntu 22.04, Icarus Verilog 11, Yosys 0.36, Python 3.10>

```bash
# 1. Mô phỏng
<lệnh cụ thể>

# 2. Tổng hợp
<lệnh cụ thể>

# 3. Sinh lại kết quả trong results/
<lệnh cụ thể>
```

> Kiểm tra thật: đưa hướng dẫn này cho một bạn khác, để bạn ấy làm theo **mà không hỏi gì thêm**.
> Chỗ nào bạn ấy phải hỏi là chỗ README còn thiếu.

## 4. Cấu trúc thư mục

```
rtl/        thiết kế RTL
tb/         testbench
sim/        script và log mô phỏng
syn/        script tổng hợp, báo cáo timing/tài nguyên
scripts/    tự động hóa, xử lý số liệu
results/    hình và bảng cuối cùng (mỗi hình truy được về script sinh ra nó)
docs/       ghi chú kỹ thuật, tài liệu đọc
```

## 5. Kết quả chính

| Chỉ số | Giá trị | Sinh ra từ |
|---|---|---|
| <Fmax> | <...> | <syn/report_timing.txt> |
| <Tài nguyên LUT/FF> | <...> | <syn/report_utilization.txt> |
| <...> | <...> | <...> |

## 6. Hồ sơ quá trình

- [`PROJECT_CHARTER.md`](PROJECT_CHARTER.md) — MVT và Extension đã chốt
- [`EVIDENCE_LEDGER.md`](EVIDENCE_LEDGER.md) — mỗi kết quả dựa trên bằng chứng nào
- [`DECISION_LOG.md`](DECISION_LOG.md) — đã quyết định gì, vì sao
- [`AI_USAGE_LOG.md`](AI_USAGE_LOG.md) — dùng AI ở đâu, kiểm chứng thế nào

## 7. Còn hạn chế gì

<Nói thật. Một đồ án nêu rõ hạn chế của mình đáng tin hơn một đồ án tuyên bố hoàn hảo.>

## 8. Bước tiếp theo cho người kế thừa

<Khóa sau sẽ đứng lên vai em. Ghi rõ: nên làm gì tiếp, chỗ nào em đã thử mà không được và vì sao.>
