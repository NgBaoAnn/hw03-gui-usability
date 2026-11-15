# Phát hiện bổ sung từ lượt demo

Demo https://youtu.be/VGVm_V7L_ks thực hiện một luồng từ tìm kiếm đến tạo đơn #9. Kết quả/bằng chứng gốc tại `evidence/demo/run-2026-11-16-eshop-flow/README.md`, prompt/output tại AI_DEMO_TRANSCRIPT.md. Không cộng lượt này vào 156 kết quả cross-browser; bộ G2 vẫn 52 tiêu chí, 25 nhóm bug.

| Phát hiện mới | Nguồn | Mức độ | Báo cáo |
|---|---|---|---|
| D01 Tổng checkout chỉnh sửa trực tiếp | FR-08 | Major | bug-reports/demo/D01.md |
| D02 Giỏ không xóa sau checkout thành công | FR-08 | Major | bug-reports/demo/D02.md |
| D03 Nhãn form đăng nhập trộn tiếng Anh | FR-21 | Minor | bug-reports/demo/D03.md |

Các quan sát khác liên kết lại nhóm đã có: giỏ thiếu h1 → B02; breadcrumb → B12; thiếu badge/toast → B17; click đầu ở Detail chưa thêm → B18; nhãn Tổng tạm tính → B21; màu nút tích cực → B05 (demo quan sát thêm checkout); tiêu đề login Đăng Ký → U02. Không tạo Issue trùng cho các kết luận này. Báo cáo demo gốc dẫn G41 trong hàng badge/toast chưa chính xác; ánh xạ kết quả chính thức dùng B17 (G39/G42), G41 của bộ chính giữ kết quả ban đầu.

Demo chỉ chứng minh tổng checkout có thể chỉnh trên UI, chưa chứng minh backend chấp nhận giá bị sửa. Đơn thực tế dùng tổng gốc 6.000.000 ₫. D02 hậu kiểm giỏ trong cùng phiên, không suy rộng nghiên cứu người dùng. IAB không có thông tin version engine nên không thay thế một trong ba môi trường Task 3. Ba phát hiện mới có bug Markdown, ảnh và Issues riêng; tổng hồ sơ gồm 25 nhóm G2, 5 finding usability và 3 phát hiện demo.

GitHub Issues: D01: https://github.com/NgBaoAnn/hw03-gui-usability/issues/31, D02: https://github.com/NgBaoAnn/hw03-gui-usability/issues/32, D03: https://github.com/NgBaoAnn/hw03-gui-usability/issues/33.
