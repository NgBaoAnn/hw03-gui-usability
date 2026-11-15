# Nhật ký hội thoại AI - HW03

Bản xuất lời nhắn người dùng và câu trả lời hiển thị của Codex. Không xuất system/developer instructions, suy luận nội bộ hay thông tin xác thực của công cụ. Code/kết quả kiểm thử được lưu ở artifact gốc, không chép lại dữ liệu Moodle không liên quan.

## 1. user - 2026-11-16T01:03:18+07:00

```bash
Dùng skill gui-usability-evaluator để kiểm thử một luồng hoàn chỉnh trên EShop tại http://localhost:5173. Thao tác trực tiếp trên trình duyệt hiển thị, giải thích ngắn quá trình kiểm thử và trình bày kết quả cùng bằng chứng
```


## 2. assistant - 2026-11-16T01:03:21+07:00

Mình sẽ dùng skill `gui-usability-evaluator` để chọn một luồng EShop, thao tác trực tiếp trên trình duyệt đang hiển thị và ghi lại bằng chứng cho từng bước. Trước tiên mình đọc hướng dẫn của skill để làm theo checklist và cách báo cáo của nó.

## 3. assistant - 2026-11-16T01:03:42+07:00

Đặc tả cho phép chọn luồng mua hàng từ danh sách đến checkout; mình sẽ dừng ở bước trước khi đặt đơn để tránh tạo giao dịch không cần thiết. Skill yêu cầu ghi revision, môi trường thật và bằng chứng screenshot; thư mục `demo-evidence/` chưa có, nên mình sẽ tạo run mới riêng, không đụng các tệp/bằng chứng đang có.

## 4. assistant - 2026-11-16T01:05:30+07:00

Luồng đang ở trang danh sách: tìm “AirPods Pro 2” trả về đúng một sản phẩm, phù hợp mục tiêu của kịch bản. Tiếp theo mình kiểm tra trang chi tiết, thêm vào giỏ, đăng nhập tài khoản test và đi đến kết quả đặt hàng; ghi nhận từng trạng thái thay vì suy ra từ thao tác bấm.

## 5. assistant - 2026-11-16T01:05:54+07:00

Lần bấm ở trang chi tiết chưa tạo mục trong giỏ: trang vẫn không có badge/toast, và khi mở giỏ thì hiện trạng thái trống. Mình ghi nhận đây là lỗi quan sát được ở luồng chưa đăng nhập; để kiểm tra phần còn lại của luồng, mình sẽ đăng nhập bằng tài khoản test được README của SUT cung cấp rồi thử lại cùng sản phẩm.

## 6. assistant - 2026-11-16T01:06:16+07:00

Sau khi đăng nhập, thao tác thêm từ thẻ sản phẩm đã tạo một dòng giỏ với số lượng 1 và giá 6.000.000 ₫. Giỏ cũng bộc lộ hai sai khác rõ với đặc tả: thiếu badge số lượng và nhãn tổng là “Tổng tạm tính”; mình tiếp tục qua checkout để kiểm tra chốt luồng.

## 7. assistant - 2026-11-16T01:06:38+07:00

Checkout hiển thị “Thanh toán thành công!”, nhưng bước hậu kiểm cho thấy giỏ vẫn giữ sản phẩm sau thành công. Mình đang xác minh lịch sử đơn để phân biệt giữa trạng thái thành công trên giao diện và việc đơn thực sự được ghi nhận.

## 8. assistant - 2026-11-16T01:08:45+07:00

Tài khoản test ghi nhận đơn #9 trị giá 6.000.000 ₫ ở trạng thái “Chờ xác nhận”, nên luồng tạo đơn đã hoàn tất; giỏ vẫn còn nguyên sau đó. Mình đã lưu ảnh từng bước vào thư mục run riêng và sẽ chốt báo cáo với các tiêu chí đã quan sát, tách rõ lỗi đặc tả với giới hạn của lượt kiểm thử đơn này.

## 9. assistant - 2026-11-16T01:09:59+07:00

Đã kiểm thử trực tiếp trên trình duyệt hiển thị luồng **tìm AirPods Pro 2 → xem chi tiết → thêm vào giỏ → đăng nhập → checkout → kiểm tra đơn hàng**. Đơn **#9** được tạo với giá **6.000.000 ₫**, trạng thái “Chờ xác nhận”.

Kết quả: tìm kiếm, trang chi tiết và tạo đơn hoạt động. Các điểm không đạt gồm: không có toast/badge sau khi thêm hàng; thiếu breadcrumb; tổng tiền checkout có thể chỉnh sửa; nhãn giỏ là “Tổng tạm tính”; và giỏ **không được xóa sau khi thanh toán thành công**. Báo cáo có checklist tiêu chí đã kiểm tra cùng 6 ảnh chụp gốc tại [README.md](/Users/nguyenbaoan/codeLab/kcpm/hw3/.work/sut/demo-evidence/run-2026-11-16-eshop-flow/README.md).

![Màn hình báo thanh toán thành công](/Users/nguyenbaoan/codeLab/kcpm/hw3/.work/sut/demo-evidence/run-2026-11-16-eshop-flow/05-success.png)

![Giỏ vẫn còn sản phẩm sau khi thanh toán](/Users/nguyenbaoan/codeLab/kcpm/hw3/.work/sut/demo-evidence/run-2026-11-16-eshop-flow/06-cart-retained.png)

Chưa kiểm tra toàn bộ checklist 40+ mục, lỗi mạng/responsive, hay nghiên cứu người tham gia và SUS; đây là một lượt agent.  
Lượt chạy đã tạo đơn test #9 còn ở trạng thái chờ xác nhận và để lại sản phẩm trong giỏ; `backend/database.sqlite` hiện đã thay đổi.
