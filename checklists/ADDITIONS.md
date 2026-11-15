# Bổ sung checklist sau phản biện AI

Ba tiêu chí G49–G51 do Codex đề xuất/thực thi theo yêu cầu sinh viên. Giữ nguyên 48 tiêu chí đầu tại items.json; phần bổ sung ở additions.json. Tổng 51 tiêu chí, 153 kết quả trên ba browser: bộ gốc 144 kết quả (56 Passed, 88 Failed), bổ sung 9 Failed. Tổng 56 Passed, 97 Failed; 33 tiêu chí fail ít nhất một môi trường, 25 nhóm bug GUI. Năm finding usability tách riêng, tổng 30 GitHub Issues khi đã đăng hai bug mới.

## Vì sao bổ sung

- G49: bộ đầu đo alt và liên kết nhãn nhưng bỏ qua ngôn ngữ tài liệu. Prompt tập trung thành phần nhìn thấy; metadata phục vụ công nghệ hỗ trợ không nổi bật trong ảnh.
- G50: bộ đầu kiểm ký hiệu tiền và bố cục nhưng chưa tính tương phản. Nhận xét màu đẹp/nhìn rõ bằng mắt của AI không thay được phép đo định lượng.
- G51: G11 kiểm quy chuẩn màu xanh dương, G41 kiểm phản hồi thêm thành công. Cả hai không trả lời chữ nút có đủ tương phản hay không; việc thêm kiểm tra này tránh đánh đồng màu đúng chuẩn với dễ đọc.

## Kết quả thực thi

| ID | IA | Màn hình | Chrome | Firefox | Safari | Quan sát |
|---|---|---|---|---|---|---|
| G49 | IA-01 | Home | Failed | Failed | Failed | lang=en; nội dung tiếng Việt |
| G50 | IA-01 | Home | Failed | Failed | Failed | 3.7631:1 < 4.5:1; 16px, weight 700 |
| G51 | IA-02 | Detail | Failed | Failed | Failed | 3.2957:1 < 4.5:1; 16px, weight 400 |

## Bằng chứng và giới hạn

Đã mở các case qua native CUA trên ba browser; JSON gửi về collector localhost, ảnh chụp cửa sổ thật. Trang đo tự kiểm tra công thức trước khi gửi; collector chỉ lưu bản ghi thực tế. Không bật lại Safari Remote Automation. Không suy ra ngôn ngữ đọc thực tế của screen reader. Ảnh chụp có email/tên/MSSV và URL localhost; metadata môi trường đầy đủ ở JSON. Các tiêu chí là WCAG heuristic ngoài cam kết FR của SUT.

- [B24: Trang tiếng Việt khai báo ngôn ngữ mặc định en](../bug-reports/supplement/B24.md); Issue: https://github.com/NgBaoAnn/hw03-gui-usability/issues/29.
- [B25: Chữ giá và chữ nút thêm giỏ thiếu tương phản](../bug-reports/supplement/B25.md); Issue: https://github.com/NgBaoAnn/hw03-gui-usability/issues/30.

Nguồn: [WCAG 3.1.1](https://www.w3.org/WAI/WCAG22/Understanding/language-of-page.html), [WCAG 1.4.3](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html).
